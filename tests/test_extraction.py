import importlib.util
import tempfile
import unittest
from pathlib import Path
from PIL import Image, ImageDraw

spec=importlib.util.spec_from_file_location('extract_grid',Path(__file__).resolve().parents[1]/'skills/titi-ps-grid-extract/scripts/extract_grid.py')
extract=importlib.util.module_from_spec(spec)
spec.loader.exec_module(extract)

class ExtractionChecks(unittest.TestCase):
    def test_rejects_missing_grid_and_vertical_crop(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'input.png'
            Image.new('RGB',(600,400),'#354a32').save(path)
            with self.assertRaises(ValueError):extract.detect_cells(path)
            grid=Image.new('RGB',(608,408),'white');draw=ImageDraw.Draw(grid)
            for row in range(2):
                for col in range(6):draw.rectangle((4+col*100,4+row*200,95+col*100,195+row*200),fill='#354a32')
            grid.save(path)
            with self.assertRaisesRegex(ValueError,'top/bottom'):extract.detect_cells(path)

    def test_rejects_one_pixel_white_border(self):
        with tempfile.TemporaryDirectory() as directory:
            folder=Path(directory)
            im=Image.new('RGB',(1242,2208),'#354a32')
            for i in range(1,13):im.save(folder/f'{i}.png',dpi=(72,72))
            extract.verify_outputs(folder)
            ImageDraw.Draw(im).line((0,2207,1241,2207),fill='white')
            im.save(folder/'12.png',dpi=(72,72))
            with self.assertRaisesRegex(ValueError,'12.png has a white edge'):extract.verify_outputs(folder)

if __name__=='__main__':unittest.main()
