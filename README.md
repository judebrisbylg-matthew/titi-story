# TiTi 故事制作技能合集

从故事脚本到十二张分镜单图。合集包含两个独立 Codex skill：

| Skill | 用途 | 输入 |
|---|---|---|
| [titi-story](skills/titi-story/SKILL.md) | 制作模版3.0故事、双语脚本、连续12镜头和画面提示词 | 核心词与故事要求 |
| [titi-ps-grid-extract](skills/titi-ps-grid-extract/SKILL.md) | 用Photoshop按顺序提取已确认的2×6宫格 | 已确认原图＋保存目录 |

## 操作手册

[B版可视化提取流程](docs/ps-grid-workflow.html) · [浏览器预览](https://htmlpreview.github.io/?https://github.com/judebrisbylg-matthew/titi-story/blob/main/docs/ps-grid-workflow.html)

HTML中图片已内嵌，也可以下载后在浏览器打开；浏览器按钮只演示和复制指令，不直接执行Photoshop。HTMLPreview为第三方预览，未把预览加载视为skill运行成功。

## 使用与安装

把需要的整个skill文件夹复制到Codex个人技能目录。须保留agents、references或scripts；不要只复制SKILL.md。

```sh
mkdir -p ~/.codex/skills
cp -R skills/titi-ps-grid-extract ~/.codex/skills/
```

如果已有同名skill，先比较并备份再替换。`titi-story`也可安装，但本机版与仓库版不同，不应在未比较时自动覆盖。

后续调用：

```text
使用 $titi-ps-grid-extract，把这张已确认的十二宫格用Photoshop提取为1.png到12.png，保存到我提供的文件夹。
```

## Photoshop提取规则

- 第一行从左到右1–6，第二行从左到右7–12。
- 每张1242×2208像素、72ppi、RGB8bit、PNG、不交错。
- 去除宫格外框及白色分隔线，等比例居中铺满，优先保留上下画幅；不拉伸、不生成补边。
- 已有同名文件先备份并验证，再替换；原图、其他文件及用户未保存的Photoshop文档保留。
- 全部PNG重新读取校验后，还须看联系表逐张核对；部分成功不能说成全部完成。

自动脚本目前适用于macOS＋Adobe Photoshop 2026＋Python/Pillow。使用Codex桌面已有Python/Pillow运行环境即可；其他环境用已有Python或安装scripts/requirements.txt。无白色分隔线、不规则布局或需裁上下时停止，先确认裁切，不承诺所有宫格均可自动识别。

## 验证与来源

[实跑与测试记录](docs/validation.md)。源Apple宫格成功导出12张并视觉核验；同名文件备份行为已在独立目录测试。自动化默认2行6列，其他输入不能套用示例坐标。

故事skill完整同步自[原仓库](https://github.com/judebrisbylg-matthew/titi-story-skill)，源提交`8d877a4`，v2.2.0。原仓库保留，故事skill内容未修改；原说明、模板与示例存于[docs/story](docs/story)。

## 本地检查

```sh
python3 -m unittest discover -s tests -v
```
