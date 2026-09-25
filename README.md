# design-skills-hub

**面向 AI 消费的设计 Skill 合集。333 个 skill / 9 类。**

本仓库没有人类文档——唯一入口就是这份 README。读它，然后按需取用具体 skill。

## 加载流程

1. **找**：看下面分类表定位大类；或直接 grep 全量清单 `catalog.tsv`（每行：`id / category / trigger / resources / entry`）。
2. **清单**：打开 `<分类>/_INDEX.md`，按「何时用」列匹配任务。
3. **加载**：读 `entry` 指向的 `SKILL.md` **全文**，把它当指令执行。条目名格式 `来源--skill名`。
4. **按需展开**：`资源` 列标了 `references/` 的，是细节文档，只读当前需要的那一个；标了 `scripts/` 说明有可执行辅助脚本。
5. **同类只开一个**：设计品味类各 skill 主张互斥（极简 / 粗野 / 高对比 / 奢华），同时加载会互相冲突。

## 分类

| 目录 | 数量 | 用于 |
|---|---|---|
| `00_本地已有Skills/` | 16 | 本机直装。设计评审、画布设计、品牌/图/视频生成、素材处理、发布上线 |
| `01_设计品味与反AI味/` | 25 | 定视觉方向、定调性、摆脱默认模板感。做任何界面前先开一个 |
| `02_震撼视觉特效/` | 78 | 3D/WebGL/Shader/粒子/GSAP 滚动叙事——把页面做出视觉冲击 |
| `03_落地页与视觉风格/` | 48 | 整页结构、风格预设、定价页、作品集、Awwwards 级版式 |
| `04_视觉系统与规范/` | 61 | 设计 token、配色、字阶、栅格、间距、暗色模式、无障碍、Web 规范 |
| `05_交互与微动效/` | 31 | 缓动、时长、微交互、加载/错误/空状态、表单与导航模式 |
| `06_评审_审计_交付流程/` | 42 | 设计批评、UX 审计、落地页 48 项检查、响应式、交付规格 |
| `07_素材与图像生成/` | 17 | AI 配图、图标集、favicon、调色板、整页截图、录屏 |
| `08_工程流程与质量/` | 15 | Vue 3 全家桶、React/shadcn/Tailwind 实践、先出计划再写码 |

## 组合配方

- **一页有视觉冲击的 AI 能力展示落地页** → `anthropic--frontend-design` → `taste--taste-skill` → `mengto--threejs-landscape` → `oc--landing-page-generator` → `designer--design-token` → `emil--improve-animations` → `devgtm--landing-page-auditor`
- **救回一个已经做丑的页面** → `taste--redesign-skill` → `impeccable--impeccable` → `designer--design-critique` → `jezweb--responsiveness-check`
- **Vue 3 + 动效项目** → `oc--vue-best-practices` → `oc--gsap-frameworks` → `oc--vue-bits` → `oc--vue-testing-best-practices`
- **只靠现成风格预设快速出稿** → `mengto--dark-glass-clean-layout` → `mengto--editorial-tech` → `mengto--clean-minimal-beige-light-mode`

## 机器可读

- `catalog.tsv` — 全量平铺，一行一个 skill，便于 grep / awk / cut
- `catalog.json` — 同数据全字段版：`id` `category` `path` `entry` `when` `resources` `files`

## 来源与许可

这些 skill 来自 16 个上游开源仓库（多数 MIT，`pbakaus/impeccable` 为 Apache-2.0，`anthropics/skills` 逐 skill 各有 `LICENSE.txt`）。逐条署名与许可见 [`THIRD-PARTY-NOTICES.md`](THIRD-PARTY-NOTICES.md)。各 skill 目录内原有的 `LICENSE` 文件均已保留。

本仓库自有的索引文件与生成脚本以 MIT 发布，见 [`LICENSE`](LICENSE)。

> 已做的裁剪：剔除各 skill 的 `demo/` 演示资源（对 AI 执行无贡献）、剔除本机私有的运维/人格类 skill、移除含密钥的文件并对本机路径做了脱敏。
