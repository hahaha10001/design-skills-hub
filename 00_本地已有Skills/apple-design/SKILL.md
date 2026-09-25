---
name: apple-design
display_name: Apple流体界面设计指南
display_name_en: Apple Fluid Interface Design Guide
description: 基于Apple WWDC流体交互设计，用于UI设计评审、手势驱动界面、弹簧动画、拖拽/侧滑/抽屉弹窗、动量过渡、毛玻璃材质、深度层级、光学字号排版、减弱动效无障碍场景；输出设计建议、参数、Web端CSS/JS代码示例。
description_zh: 提炼苹果流体交互设计思想，面向设计师与前端，可输出交互方案、弹簧参数、拖拽手势实现、毛玻璃样式、无障碍适配代码。
description_en: Distill Apple fluid interface design for designers and frontend engineers, output interaction proposals, spring parameters, gesture code samples, material style and accessibility adaptation.
category: UI设计
version: 1.0.0
author: 个人开发者
user-invocable: true
disable-model-invocation: false
allowed-tools:
  - Read
  - Write
  - Bash
---

# Apple流体界面设计技能
> 引用参考资料
> @references/spring‑param‑ref.md
> @references/wwdc‑design‑rules.md
> 使用评审模板 templates/apple‑ui‑review‑template.md

## 触发词
苹果界面设计、流体交互、弹簧动画、手势UI、抽屉弹窗、拖拽滑动、毛玻璃材质、Apple UI评审、动效参数、无障碍动效

## 执行SOP
### 步骤1：确认需求场景
1. 如果用户输入信息过少，主动询问：使用场景（抽屉/拖拽/弹窗/列表滑动）、运行平台（Web/H5）、是否需要无障碍适配。
2. 用户上传设计稿/需求文档，调用Read读取文档作为输入依据。

### 步骤2：依据苹果设计原则输出内容，按需输出以下模块
1. **核心设计思路**：流体交互核心思想，界面行为模拟现实物理世界，即时响应、动量传递、可中途打断动画。
2. **交互行为建议**：响应延迟、直接操纵、动画可中断、弹簧物理、速度移交、动量投射、橡胶边界、手势细节。
3. **物理参数推荐**：弹簧阻尼比、响应时间，参考 @references/spring‑param‑ref.md。
4. **样式与材质方案**：毛玻璃backdrop‑filter、层级深度、阴影、文字活力（Vibrancy）。
5. **排版规范**：光学字号、字间距、行高动态适配。
6. **无障碍方案**：减弱动效、降低透明度、高对比度适配媒体查询。
7. **Web可运行代码片段**：CSS、JS、Framer‑Motion/Motion示例。
8. **八大设计原则校验**：目的性、用户控制权、责任、熟悉感、灵活性、简洁、工艺、愉悦感。

### 步骤3：分支交互逻辑
1. 用户输入【UI评审】：读取 templates/apple‑ui‑review‑template.md，填充内容输出完整评审报告。
2. 用户输入【生成代码】：调用Bash执行 scripts/code‑snippet‑gen.py，输出格式化代码片段。
3. 用户输入【输出文件】：完成分析后，询问确认，调用Write将完整报告保存到本地 `AppleUI设计报告.md`。

## 输出约束
1. 使用Markdown，代码块使用```css ``````js ```标记。
2. 参数输出严格对齐苹果WWDC给出的物理参数。
3. 不编造不存在API，Web能力受限处明确标注限制。
4. 信息不足主动提问，不凭空给出设计方案。
5. 禁止高危系统操作。

## 调用示例
> 示例1：抽屉弹窗设计
苹果界面设计，做一个 Web 底部抽屉 sheet，输出交互参数和 css 示例

```
> 示例2：UI评审模式
```

UI 评审，我要做一个可拖拽卡片，按照 Apple 流体交互标准评审

```
> 示例3：输出报告文件
```

基于上面的分析，输出文件保存本地

```

## 参考核心思想
> 当界面对齐人的思考与运动方式，就不再像一台计算机，而是无缝的延伸。
> 流体界面特征：即时响应、连续运动、携带动量、边界阻力、运动过程可随时被打断重定向。
```