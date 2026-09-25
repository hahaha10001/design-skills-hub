# design-skills-hub

**面向 AI 消费的设计 Skill 合集。571 个 skill / 10 类。**

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
| `01_设计品味与反AI味/` | 37 | 定视觉方向、定调性、摆脱默认模板感。做任何界面前先开一个 |
| `02_震撼视觉特效/` | 85 | 3D/WebGL/Shader/粒子/GSAP 滚动叙事，把页面做出视觉冲击 |
| `03_落地页与视觉风格/` | 110 | 整页结构、页面类型（落地页/定价页/作品集）、产品展示页 |
| `04_视觉系统与规范/` | 77 | 设计 token、配色、字阶、栅格、间距、暗色模式、无障碍、Web 规范 |
| `05_交互与微动效/` | 61 | 组件级交互与状态：按钮/表单/弹窗/导航/表格/加载/空状态/错误 |
| `06_评审_审计_交付流程/` | 72 | 设计批评、UX 审计、策略与研究、规格与交付、验收门禁 |
| `07_素材与图像生成/` | 18 | AI 配图、图标集、favicon、调色板、整页截图、录屏 |
| `08_工程流程与质量/` | 21 | React/Vue/Next/Tailwind/shadcn 实践、性能、容器查询 |
| `09_视觉风格预设/` | 74 | 一次定一种整体风格：glassmorphism / brutalism / editorial / 暗色科技 / 日式极简… |

## 组合配方

- **一页有视觉冲击的 AI 能力展示落地页** → `anthropic--frontend-design` → `taste--taste-skill` → `mengto--threejs-landscape` → `oc--landing-page-generator` → `designer--design-token` → `emil--improve-animations` → `devgtm--landing-page-auditor`
- **先定整体风格，再往下做** → `bergside--glassmorphism` → `bergside--premium` → `bergside--editorial` → `dsh--apple-minimal`
- **把已经做丑的页面救回来** → `taste--redesign-skill` → `impeccable--impeccable` → `ibelick--improve-ui` → `designer--design-critique`
- **组件级交互打磨** → `uxcel--buttons` → `uxcel--inputs-and-forms` → `uxcel--empty-states` → `uxcel--error-recovery` → `emil--improve-animations`
- **Vue 3 / React 项目实践** → `oc--vue-best-practices` → `oc--gsap-frameworks` → `jezweb--shadcn-ui` → `jezweb--react-patterns`

## 机器可读

- `catalog.tsv` — 全量平铺，一行一个 skill，便于 grep / awk / cut
- `catalog.json` — 同数据全字段版：`id` `slug` `category` `path` `entry` `source` `when` `trigger_short` `resources` `files`

## 兼容的客户端

所有 skill 都遵循 open Agent Skills 标准（`agentskills.io`），SKILL.md 即插即用。已在 Claude Code、Codex、Cursor、opencode、Gemini CLI、VS Code Copilot 等工具上通用。

## 来源与许可

聚合自 56 个上游开源仓库，逐条署名与许可见 [`THIRD-PARTY-NOTICES.md`](THIRD-PARTY-NOTICES.md)。各 skill 目录内原有的 `LICENSE` 文件均已保留。

本仓库自有的索引层（README / catalog.* / 各 `_INDEX.md`）以 MIT 发布，见 [`LICENSE`](LICENSE)。

> 已做的裁剪：剔除各 skill 的 `demo/` 演示资源（对 AI 执行无贡献）、剔除本机私有的运维与人格类 skill、移除含密钥的文件并对本机路径做了脱敏。
