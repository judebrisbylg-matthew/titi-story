# TiTi Story

## 故事技能操作流程 · HTML

[打开网页预览（HTMLPreview）](https://htmlpreview.github.io/?https://github.com/judebrisbylg-matthew/titi-story-skill/blob/main/titi-skill-guide.html) · [查看 HTML 源文件](titi-skill-guide.html)

包含技能用途、操作步骤、8 秒片头时间轴、脚本交付顺序、任务指令示例和交付检查清单。网页预览使用第三方 HTMLPreview；也可下载 HTML 与同目录角色图片后在浏览器打开。

当前版本：2.2.0 · 制作模版3.0 · 常亮许愿灯、10秒复读与纯黑收幕。说明页与仓库 Skill 同步；个人已安装版需经确认后另行更新。

规则入口：[SKILL.md](../../skills/titi-story/SKILL.md) · [完整输出规范](../../skills/titi-story/references/output-format.md) · [HEAD完整示例](../../skills/titi-story/references/head-example.md)。旧第一集保留为历史创意资料，不作为当前格式样板。

中文说明在前，英文说明在后。  
Chinese section first, English section below.

---

## 中文说明

`TiTi Story` 是一个可复用的 Codex skill 仓库，用来围绕原创角色 `提提 (TiTi)` 产出固定格式的儿童英语动画故事脚本。

这个仓库不是单独备份一个 `SKILL.md`，而是一个完整的 skill 模板仓库，包含：

- 正式 skill 文件
- 固定写作标准
- 安装说明
- 模板复用说明
- 示例 prompt
- 维护规范
- 角色与项目源设定文档

### 这个仓库解决什么问题

在系列化儿童内容生产里，如果没有固定 skill，结果通常会漂：

- 模板段落漏掉
- 分镜数量不稳定
- 学习单词提示镜头被省略
- 台词节奏每集不一致
- 角色设定越写越偏
- 魔法规则越写越乱
- 后续出图、配音、剪辑衔接成本升高

这个仓库的目的，就是把这些容易漂的部分固定下来。

### Skill 的核心能力

这个 skill 专门服务于一条明确的生产链路：

`核心词 -> 脚本 -> 分镜 -> 画面提示词 -> 配音 -> 剪辑`

固定能力包括：

- 正片固定 `4 × 15秒`，每板块3个连贯分镜，共12张关键帧
- 脚本大图 `16:9、2行6列`，每格 `9:16`，外围补白、不拉伸不裁切
- 每板块交付分镜表、完整15秒视频提示词与衔接状态
- 正片核心词独立说出3次并留响应停顿，每镜有简短英文过渡
- 固定 `9:16` 竖构图设定
- 固定 `制作模版3.0` 输出结构
- 固定 `学习单词提示镜头分解`
- 中英双语脚本输出
- 面向儿童启蒙的 `CEFR A1` 英文难度
- 固定主角 `提提`
- 固定 `愿望灯` 规则
- 固定“不要背景音乐，只保留人声和特效音效”
- 固定“结尾要有轻松搞笑反转”

### 适用场景

适合用于：

- 围绕单个核心词生成一集新故事
- 保持每一集输出结构完全一致
- 做系列化儿童英语磨耳朵内容
- 直接给后续分镜、出图、配音、剪辑使用
- 把提提世界观和角色规则稳定下来

### 快速使用

在 Codex 中调用：

```text
$titi-story
```

示例：

```text
Use $titi-story to write a new TiTi script for the core word LIGHT.
```

安装说明：

- [docs/install.md](./docs/install.md)

### 仓库结构

```text
.
├── README.md
├── CHANGELOG.md
├── docs/
│   ├── example-output.md
│   ├── features.md
│   ├── install.md
│   ├── maintenance.md
│   ├── overview.md
│   ├── template-repo.md
│   └── workflow.md
├── examples/
│   ├── example-prompt.md
│   └── example-use-cases.md
├── templates/
│   └── story-brief-template.md
├── skills/
│   └── titi-story/
│       ├── SKILL.md
│       ├── references/  # output-format.md + head-example.md
│       └── agents/
│           └── openai.yaml
├── TiTi_人物设定补充_愿望灯.md
├── TiTi_儿童英语动画制作SOP.md
├── 第一集_愿望灯正式脚本_会发光的小路.md
└── 第一集_愿望灯逐镜头画面提示词_会发光的小路.md
```

### 输出标准

这个 skill 产出的每份故事脚本，默认都应包含：

1. 学习单词提示镜头分解
2. 文字表现建议
3. 分隔线
4. 开场生图总指令
5. 主人公（固定不变）
6. 场景（固定不变）
7. 质感表现（固定不变）
8. 风格
9. 情节概要
10. 角色 (Characters)（固定不变）
11. 分隔线
12. 正片镜头分解：4个15秒板块，每段3镜＋视频提示词＋衔接状态
13. 片尾单词复读镜头分解（10秒内，含固定四行文字表现建议）
14. 台词总汇
15. 分隔线
16. 中文版
17. 英文版
18. 智能文稿匹配（英文）：问候＋片头1次英文词＋正片全部英文＋跟读2次英文词＋告别

教学提示8秒＋正片60秒＋片尾跟读最多10秒；按10秒预算小计78秒，问候与告别另计。正片运镜新增起止构图、方向幅度和目的；真实相对体量不变，允许合理透视变化。完整中英文台词保留全部话语，智能文稿单独按环节筛选。

参考：

- [docs/example-output.md](./docs/example-output.md)
- [examples/example-prompt.md](./examples/example-prompt.md)

### 提提固定设定

当前 skill 默认绑定以下角色规则：

- 主角是 `提提 (TiTi)`
- 木质感小男孩木偶
- 棕色层次短发
- 圆润深色眼睛
- 米色上衣
- 蓝绿色短裤
- 蓝绿色叶片斗篷
- 棕色斜挎小包
- 腰间挂小提灯
- 夜晚默认使用 `不戴帽版`

### 愿望灯规则

`愿望灯` 是提提的核心叙事道具，不只是普通提灯。

固定规则：

- 只响应善良愿望
- 只用于帮助别人
- 只能实现温暖的小奇迹
- 不直接替提提解决一切
- 重点是让提提获得行动机会
- 同一盏灯固定自身左前腰，不拿起、不复制；未许愿时熄灭但实体仍在
- 念完 `Little light, shine bright!` 才发暖金光，帮助完成后继续常亮

源文档参考：

- [TiTi_人物设定补充_愿望灯.md](./TiTi_%E4%BA%BA%E7%89%A9%E8%AE%BE%E5%AE%9A%E8%A1%A5%E5%85%85_%E6%84%BF%E6%9C%9B%E7%81%AF.md)
- [TiTi_儿童英语动画制作SOP.md](./TiTi_%E5%84%BF%E7%AB%A5%E8%8B%B1%E8%AF%AD%E5%8A%A8%E7%94%BB%E5%88%B6%E4%BD%9CSOP.md)

### 如果你要把它当模板复用

这个仓库已经按模板仓库方式组织好了。  
后面如果你要做新的儿童故事 skill，通常只需要替换：

1. skill 名称
2. 角色锁定规则
3. 世界观规则
4. 示例 prompt
5. 相关说明文档

详细说明：

- [docs/template-repo.md](./docs/template-repo.md)

### 文档索引

- [docs/overview.md](./docs/overview.md)：项目定位
- [docs/features.md](./docs/features.md)：功能与约束
- [docs/workflow.md](./docs/workflow.md)：生产流程
- [docs/install.md](./docs/install.md)：安装说明
- [docs/template-repo.md](./docs/template-repo.md)：模板复用说明
- [docs/maintenance.md](./docs/maintenance.md)：维护规范

### 示例材料

- [examples/example-prompt.md](./examples/example-prompt.md)
- [examples/example-use-cases.md](./examples/example-use-cases.md)
- [第一集_愿望灯正式脚本_会发光的小路.md](./%E7%AC%AC%E4%B8%80%E9%9B%86_%E6%84%BF%E6%9C%9B%E7%81%AF%E6%AD%A3%E5%BC%8F%E8%84%9A%E6%9C%AC_%E4%BC%9A%E5%8F%91%E5%85%89%E7%9A%84%E5%B0%8F%E8%B7%AF.md)

### 当前版本

版本记录见：

- [CHANGELOG.md](./CHANGELOG.md)

---

## English

`TiTi Story` is a reusable Codex skill repository for generating fixed-format children's English animation story scripts around the original character `提提 (TiTi)`.

This repository is not just a backup of one `SKILL.md`. It is organized as a complete reusable skill template repository with:

- the production skill itself
- the fixed writing standard
- installation guidance
- template reuse guidance
- example prompts
- maintenance rules
- source documents for character and project constraints

### What This Repository Solves

In serialized children's content production, outputs drift quickly if the skill rules are not fixed:

- sections get omitted
- shot counts change
- word-learning intro blocks disappear
- dialogue pacing becomes inconsistent
- character rules drift
- magic rules become unstable
- downstream image, dubbing, and editing work becomes harder

This repository exists to lock those unstable parts down.

### Core Skill Capability

The skill is designed for one clear production chain:

`core word -> script -> storyboard -> image prompts -> dubbing -> editing`

The fixed capabilities include:

- four consecutive 15-second blocks, three frames per block, 60-second main story
- twelve 9:16 frames in a 16:9 board, two rows by six columns, outer padding without stretching or cropping
- each block includes a three-row table, a complete video prompt, and transition states
- three standalone core-word utterances in the main story, with response pauses and short English transitions in every shot
- fixed `9:16` vertical composition
- fixed `制作模版3.0` output structure
- fixed `学习单词提示镜头分解`
- bilingual Chinese + English script output
- `CEFR A1` level English for young children
- fixed TiTi protagonist rules
- fixed `Wish Lantern` rules
- fixed `no background music, voice and sound effects only`
- fixed light funny twist ending

### Best Use Cases

Use this repository when you want to:

- generate a new episode from one core word
- keep every episode in the exact same production structure
- build a serialized children's English listening series
- hand scripts directly into storyboard, image generation, dubbing, and edit workflows
- preserve TiTi's world and rule consistency

### Quick Start

Invoke the skill in Codex with:

```text
$titi-story
```

Example:

```text
Use $titi-story to write a new TiTi script for the core word LIGHT.
```

Install guide:

- [docs/install.md](./docs/install.md)

### Repository Structure

```text
.
├── README.md
├── CHANGELOG.md
├── docs/
│   ├── example-output.md
│   ├── features.md
│   ├── install.md
│   ├── maintenance.md
│   ├── overview.md
│   ├── template-repo.md
│   └── workflow.md
├── examples/
│   ├── example-prompt.md
│   └── example-use-cases.md
├── templates/
│   └── story-brief-template.md
├── skills/
│   └── titi-story/
│       ├── SKILL.md
│       ├── references/  # output-format.md + head-example.md
│       └── agents/
│           └── openai.yaml
├── TiTi_人物设定补充_愿望灯.md
├── TiTi_儿童英语动画制作SOP.md
├── 第一集_愿望灯正式脚本_会发光的小路.md
└── 第一集_愿望灯逐镜头画面提示词_会发光的小路.md
```

### Output Standard

Each generated story script is expected to include:

1. word-learning intro breakdown
2. word visual treatment notes
3. separator
4. storyboard generation instruction
5. fixed protagonist
6. fixed setting
7. fixed materials
8. style
9. story summary
10. fixed characters
11. separator
12. four 15-second blocks, each with three frames, a video prompt, and transition states
13. post-story repeat-along breakdown (up to 8 seconds)
14. dialogue summary
15. separator
16. Chinese version
17. English version
18. selected English matching text: greeting, one intro word, full story dialogue, two repeat-along words, farewell

The learning intro is 8 seconds, the main story 60 seconds, and the new repeat-along up to 8 seconds. Greeting and farewell are additional to the 76-second budget. Full bilingual records remain complete; matching text is separately filtered by section. Motivated camera movement preserves physical scale while allowing natural perspective changes.

References:

- [docs/example-output.md](./docs/example-output.md)
- [examples/example-prompt.md](./examples/example-prompt.md)

### TiTi Canonical Rules

The current skill is tied to the following character rules:

- protagonist: `TiTi`
- wooden puppet boy
- layered brown short hair
- round dark eyes
- beige shirt
- blue-green shorts
- blue-green leaf cape
- brown side bag
- small waist lantern
- night scenes default to the `no-hat` version

### Wish Lantern Rules

The `Wish Lantern` is TiTi's core narrative prop, not just a normal lamp.

Fixed rules:

- responds only to kind wishes
- can only be used to help others
- creates only small warm miracles
- does not solve everything for TiTi
- mainly creates a chance for TiTi to act
- exactly one lantern, fixed at TiTi’s own front-left waist, never hand-held or duplicated
- lights only after the full incantation `Little light, shine bright!`; fades after help is completed but remains physically present

Source references:

- [TiTi_人物设定补充_愿望灯.md](./TiTi_%E4%BA%BA%E7%89%A9%E8%AE%BE%E5%AE%9A%E8%A1%A5%E5%85%85_%E6%84%BF%E6%9C%9B%E7%81%AF.md)
- [TiTi_儿童英语动画制作SOP.md](./TiTi_%E5%84%BF%E7%AB%A5%E8%8B%B1%E8%AF%AD%E5%8A%A8%E7%94%BB%E5%88%B6%E4%BD%9CSOP.md)

### Reusing This Repository As A Template

This repository is already organized as a template repo.  
If you want to build a new children's story skill from it, you usually only need to replace:

1. the skill name
2. the character lock rules
3. the world rules
4. the example prompts
5. the related docs

Detailed guide:

- [docs/template-repo.md](./docs/template-repo.md)

### Documentation Index

- [docs/overview.md](./docs/overview.md): project overview
- [docs/features.md](./docs/features.md): features and constraints
- [docs/workflow.md](./docs/workflow.md): production workflow
- [docs/install.md](./docs/install.md): installation guide
- [docs/template-repo.md](./docs/template-repo.md): template reuse guide
- [docs/maintenance.md](./docs/maintenance.md): maintenance guidance

### Example Materials

- [examples/example-prompt.md](./examples/example-prompt.md)
- [examples/example-use-cases.md](./examples/example-use-cases.md)
- [第一集_愿望灯正式脚本_会发光的小路.md](./%E7%AC%AC%E4%B8%80%E9%9B%86_%E6%84%BF%E6%9C%9B%E7%81%AF%E6%AD%A3%E5%BC%8F%E8%84%9A%E6%9C%AC_%E4%BC%9A%E5%8F%91%E5%85%89%E7%9A%84%E5%B0%8F%E8%B7%AF.md)

### Current Version

Version history:

- [CHANGELOG.md](./CHANGELOG.md)

## v2.2.0 已确认补充

片尾固定引导：“故事看完啦！跟提提再念一遍今天的单词吧！”；10秒内先英文两遍（各留1秒回应），再中文一遍，最后“你学会了吗？”。片尾必须附固定四行文字表现建议，详见输出规范。片头片尾独立教学灯常亮；只有正片许愿前灯不亮、完整咒语后常亮；全程同一灯体仅切换光源。正片第四段13.5–14.5秒圆形收幕归零，14.5–15秒用不透明纯黑素材替换末尾0.5秒；导出尾帧不得残留小孔或灯光，不延长60秒正片。

## 最新视觉规则（v2.2.0）

片头片尾腰灯常亮；仅正片许愿前不亮、完整咒语后常亮。亮灭使用同一参考灯体，仅切换内部光源，外形、结构、材质及人物相对比例不变；先验收同机位亮灭对照。全片暖色近景、暗色远景，无大白月盘或明亮蓝雾；背景是稀疏缓慢漂移的柔焦小光点，不是具象萤火虫。每集第一镜按故事灵活设计，不固定仰望天空。详细规则见仓库 skill 与输出规范。
