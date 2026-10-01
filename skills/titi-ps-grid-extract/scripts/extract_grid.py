#!/usr/bin/env python3
"""Extract an approved 2x6 storyboard using Photoshop on macOS. Requires Pillow."""
import argparse
import json
import shutil
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw


def content_runs(values):
    runs = []
    for i, white in enumerate(values):
        if not white:
            if not runs or i != runs[-1][1]:
                runs.append([i, i + 1])
            else:
                runs[-1][1] = i + 1
    return runs


def detect_cells(source):
    with Image.open(source) as image:
        image = image.convert('RGB')
        w, h = image.size
        channels = image.split()
        minimum = ImageChops.darker(ImageChops.darker(channels[0], channels[1]), channels[2])
        mask = minimum.point(lambda v: 1 if v > 240 else 0)
        pixels = mask.tobytes()
        xs = content_runs([sum(pixels[x::w]) / h > .97 for x in range(w)])
        ys = content_runs([sum(pixels[y*w:(y+1)*w]) / w > .97 for y in range(h)])
    if len(xs) != 6 or len(ys) != 2:
        raise ValueError('Cannot reliably identify 2x6 content regions; inspect a numbered crop preview before proceeding.')
    for runs in (xs, ys):
        sizes = [b-a for a, b in runs]
        if min(sizes) < max(sizes)*.85:
            raise ValueError('Uneven content regions; manual crop review required.')
    cells = []
    for y1, y2 in ys:
        for x1, x2 in xs:
            # Remove the two-pixel antialias fringe of white separators.
            box = [x1+2, y1+2, x2-2, y2-2]
            if (box[2]-box[0]) / (box[3]-box[1]) < 1242/2208:
                raise ValueError('This panel requires trimming top/bottom; confirm the crop tradeoff first.')
            cells.append(box)
    return cells


def verify_outputs(folder):
    for i in range(1, 13):
        with Image.open(folder/f'{i}.png') as im:
            im.load()
            if im.size != (1242, 2208) or im.mode != 'RGB':
                raise ValueError(f'{i}.png has incorrect dimensions or RGB mode.')
            dpi = im.info.get('dpi', (0, 0))
            if any(abs(v-72) > .1 for v in dpi):
                raise ValueError(f'{i}.png has incorrect resolution metadata.')
            edges = [im.crop((0,0,1242,1)), im.crop((0,2207,1242,2208)),
                     im.crop((0,0,1,2208)), im.crop((1241,0,1242,2208))]
            for edge in edges:
                if sum(min(p)>240 for p in edge.getdata())/(edge.width*edge.height) > .97:
                    raise ValueError(f'{i}.png has a white edge; inspect whether it is a grid border or real scene content.')


def contact_sheet(folder, destination):
    board = Image.new('RGB', (1080,688), '#252525')
    draw = ImageDraw.Draw(board)
    for i in range(1,13):
        with Image.open(folder/f'{i}.png') as im:
            im.thumbnail((170,302))
            x,y = (i-1)%6*180+5, (i-1)//6*344+30
            board.paste(im,(x,y))
            draw.text((x,y-22),str(i),fill='white')
    board.save(destination)


def photoshop_script(source, stage, cells):
    return '''var oldUnits=app.preferences.rulerUnits, oldDialogs=app.displayDialogs;
var src=null, doc=null;
app.preferences.rulerUnits=Units.PIXELS;app.displayDialogs=DialogModes.NO;
try {
 src=app.open(new File(SOURCE)); var cells=CELLS;
 for(var i=0;i<12;i++) {
  doc=src.duplicate('TiTi-'+(i+1),false);doc.flatten();doc.crop(cells[i]);
  if(doc.mode!==DocumentMode.RGB)doc.changeMode(ChangeMode.RGB);
  doc.bitsPerChannel=BitsPerChannelType.EIGHT;
  doc.resizeImage(undefined,UnitValue(2208,'px'),72,ResampleMethod.BICUBIC);
  var left=Math.floor((doc.width.as('px')-1242)/2);
  doc.crop([left,0,left+1242,2208]);
  var opt=new PNGSaveOptions();opt.interlaced=false;opt.compression=6;
  doc.saveAs(new File(STAGE+'/'+(i+1)+'.png'),opt,true,Extension.LOWERCASE);
  doc.close(SaveOptions.DONOTSAVECHANGES);doc=null;
 }
} finally {
 if(doc)doc.close(SaveOptions.DONOTSAVECHANGES);
 if(src)src.close(SaveOptions.DONOTSAVECHANGES);
 app.preferences.rulerUnits=oldUnits;app.displayDialogs=oldDialogs;
}
'''.replace('SOURCE',json.dumps(str(source))).replace('STAGE',json.dumps(str(stage))).replace('CELLS',json.dumps(cells))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=Path)
    parser.add_argument('output',type=Path)
    parser.add_argument('--plan',action='store_true',help='Inspect detected coordinates without exporting.')
    args=parser.parse_args()
    source=args.source.expanduser().resolve()
    cells=detect_cells(source)
    if args.plan:
        print(json.dumps({'cells':cells,'order':'row-major','output_size':[1242,2208]},ensure_ascii=False))
        return
    output=args.output.expanduser().resolve()
    output.mkdir(parents=True,exist_ok=True)
    # A unique on-disk source copy prevents closing/modifying an existing Photoshop document.
    stage=Path(tempfile.mkdtemp(prefix='.titi-extract-',dir=output))
    working=stage/('source'+source.suffix)
    shutil.copy2(source,working)
    script=stage/'extract.jsx'
    script.write_text(photoshop_script(working,stage,cells),encoding='utf-8')
    command='tell application "Adobe Photoshop 2026" to do javascript file '+json.dumps(str(script))
    result=subprocess.run(['osascript','-e',command],capture_output=True,text=True)
    if result.returncode:
        done=[i for i in range(1,13) if (stage/f'{i}.png').exists() and (stage/f'{i}.png').stat().st_size]
        raise RuntimeError(f'Photoshop stopped; staged files {done}; inspect {stage}. {result.stderr.strip()}')
    contact_sheet(stage,stage/'contact-sheet.jpg')
    try:
        verify_outputs(stage)
    except ValueError as error:
        raise RuntimeError(f'{error} Staged files are 1–12; inspect {stage} and its contact-sheet.jpg.') from error
    existing=[output/f'{i}.png' for i in range(1,13) if (output/f'{i}.png').exists()]
    backup=None
    if existing:
        backup=output/'_backup'/datetime.now().strftime('%Y%m%d-%H%M%S-%f')
        backup.mkdir(parents=True)
        for file in existing:
            shutil.copy2(file,backup/file.name)
            if file.read_bytes() != (backup/file.name).read_bytes():
                raise RuntimeError('Backup verification failed; outputs have not been replaced.')
    # Keep staged evidence and verified originals if a filesystem write fails.
    for i in range(1,13):
        shutil.copy2(stage/f'{i}.png',output/f'{i}.png')
    verify_outputs(output)
    print(json.dumps({'saved':12,'output':str(output),'backup':str(backup) if backup else None,
                      'contact_sheet':str(stage/'contact-sheet.jpg'),'status':'files-verified; visual review required'},ensure_ascii=False))


if __name__ == '__main__':
    main()
