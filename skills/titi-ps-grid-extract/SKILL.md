---
name: titi-ps-grid-extract
description: Use when a user provides an approved TiTi 2-row 6-column storyboard and an output folder to extract twelve ordered 1242x2208 PNGs using Photoshop on macOS, including 去白边、十二宫格提取、PS单图保存. Not for creating or repainting storyboard content.
---

# TiTi Photoshop 十二宫格单图提取

输入只需要已确认原图和保存目录。用原图像素在 Photoshop 中裁切、缩放和保存，不能用屏幕截图替代。默认2行6列：第一行左到右1–6，第二行左到右7–12。输出1.png–12.png，1242×2208像素、72ppi、RGB8bit、PNG、不交错；脚本压缩级别6。

## 执行

1. 看原图，确认用户已批准、布局为2×6。未确认图不自行认定已批准；缺少路径才询问。不要改已确认故事或人物内容。
2. 找到能导入Pillow的Python。Codex桌面可用load_workspace_dependencies提供的Python；其他环境用已有Python与Pillow。无需安装Photoshop插件。
3. 用本skill目录下的脚本先检查坐标：
   ```sh
   python3 scripts/extract_grid.py "已确认宫格原图.png" "保存目录" --plan
   ```
   坐标动态识别白色外框和分隔线，不固定Apple示例坐标。边界内缩2源像素去除白分隔线的抗锯齿残留，此后不额外裁上下。检查12个框与原图一致。脚本仅支持可靠的白色分隔线；无白线、误判或不规则布局时先显示带编号的裁切预览，请用户确认边界，再决定手动Photoshop提取。不能硬切等份或把画面中的白色物体当白边。
4. 正常边界不用逐张询问；执行同一脚本去掉`--plan`。路径用独立参数传递，不能拼成可执行shell文本。当前自动调用目标为Adobe Photoshop 2026（实测27.0）；其他安装名需核实后调整调用，不能宣称已支持所有版本。
5. 脚本先创建原图临时副本并在独立文档中执行，保护用户打开的未保存文档。等比例铺满、画面整体居中、优先保留上下，必要时裁左右。居中不意味着移动人物或物件。不拉伸、不生成补边、不改图。若必须裁上下则停止说明取舍。
6. 输出先写到保存目录内的`.titi-extract-*`工作文件夹，全部校验后才交付。已有同名PNG先复制到`_backup/运行时间/`并逐字节验证；备份失败停止，禁止直接覆盖旧结果。保留原图及其他文件。工作文件夹保留坐标脚本、原图副本、联系表及失败证据，不上传用户素材到GitHub。
7. 脚本重新读取所有PNG，检查精确尺寸、RGB、72ppi和边缘。PNG读值72.009属于单位换算的正常误差。打开输出联系表并核对12格的顺序、边缘、居中、上下保留和相邻格污染；有疑问再打开该张全尺寸图。近白整边可能是画面内容，要看原图判断，不能机械删白。低清原图放大不会新增细节。

## 交付和失败

只有实际文件全部存在、重新读取通过、视觉核对通过才说完成。脚本的`files-verified; visual review required`只代表文件检查通过，不能跳过视觉检查。提供保存目录、1–12顺序、尺寸和联系表，区分已保存与用户最终验收。

失败时报告已导出/失败编号及工作目录，保留原图和旧文件。禁止把部分成功说成全部完成；重试先核对保存状态。后续只提供新原图和目录即可复用。
