# Changelog

All notable changes to this repository are tracked here.

## 2.2.0 — 2026-09-27

- 片头、片尾及固定问候告别腰灯常亮；仅正片执行许愿前不亮、完整咒语后常亮。
- 灯体参考模型锁定：尺寸、结构、材质和悬挂位置不变，只切换光源；新增亮灭对照验收。
- 统一暖色近景、暗色远景，背景改为稀疏漂移小光点，禁止具象飞虫。
- 首镜按故事灵活变化；保留HEAD单集开场，补充APPLE连续性示例。

## 2.1.0 — 2026-09-27

- 固定许愿前熄灭、咒语结束后持续常亮至本集告别，下一集重置。
- 片尾改为10秒：固定引导、英文两遍、中文一遍、回应与提问；新增固定四行文字表现建议。
- 正片结尾圆形窗口归零，最后0.5秒用纯黑素材兜底并检查导出尾帧。

- separate complete bilingual records from section-filtered English matching text
- retain only the actual English core word in the learning-intro matching segment; preserve all actual main-story dialogue
- add motivated camera direction per shot, allowing perspective changes without physical scale drift
- add a separate up-to-8-second repeat-along after the story: one Chinese word, two English words, response gaps and a warm question
- keep 4×15-second main story and 2×6 board unchanged; greeting and farewell remain additional

## 2.0.0 - 2026-09-27

- retained the 制作模版3.0 section identity while restoring the confirmed intro-first output order
- replaced independent shots with four 15-second blocks, three continuous frames each
- fixed board layout at two rows by six columns, overall16:9 and individual9:16, with outer padding
- added unique waist-lantern state continuity and the fixed incantation
- added three standalone teaching repetitions, English transitions in every frame, and complete four-part English transcript
- bundled full output rules and a HEAD example inside the installable skill
- synchronized the existing HTML guide without a visual redesign; retained historical episode-one sources with a historical notice
- validated skill format, local documentation links, desktop/mobile guide layout, and HEAD/BAG script structure; generated media and recorded audio timing remain separate production checks

## 1.1.0 - 2026-07-05

- upgraded the repository from a single published skill into a reusable skill template repository
- expanded `README.md` into a fuller project landing page
- added installation documentation
- added template reuse guidance
- added maintenance guidance
- added example prompts and use cases
- added a reusable story brief template

## 1.0.0 - 2026-07-05

- created the public repository `titi-story-skill`
- published the `titi-story` skill
- added core docs for overview, features, workflow, and output format
- added source project documents for TiTi character rules, SOP, and episode-one examples
