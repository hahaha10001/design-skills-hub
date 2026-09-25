---
name: vue-bits
description: Vue Bits 动画组件库使用指南 — Vue 3 + TypeScript + Tailwind 的高端动画 UI 组件库（React Bits 的 Vue 移植版）。当用户需要为 Vue 项目添加背景动画、文字动画、交互组件（如 Aurora、SplitText、TiltedCard、SpotlightCard、Dock 等），或要求"动画像 React Bits 那样"、"用 Vue Bits 的组件"、"加个炫酷背景/文字特效"时使用。提供完整组件目录、安装方式和用法。
---

# Vue Bits — Animated UI Components For Vue

官方地址: https://vue-bits.dev/ | GitHub: https://github.com/DavidHDev/vue-bits

Vue Bits 是 React Bits (https://reactbits.dev) 的官方 Vue 移植版：大型动画 Vue 3 UI 组件集合，含 90+ 组件（背景、文字动画、动画、组件），全部 TypeScript + Tailwind，props 高度可定制，MIT 开源免费。

## 安装方式

```bash
npx jsrepo add https://vue-bits.dev/r/aurora.json
```

- 使用 **jsrepo** 或 **shadcn** 安装，组件直接落入项目代码库，随时可改。
- 用 jsrepo 安装后按需复制组件到项目中即可，无运行时依赖包袱。

## 组件目录（按分类）

### Backgrounds（背景，44 个）
Aurora, Balatro, Ballpit, Beams, ColorBends, DarkVeil, Dither, DotField, DotGrid, EvilEye, FaultyTerminal, Ferrofluid, FloatingLines, Galaxy, GradientBlinds, Grainient, GridDistortion, GridMotion, GridScan, Hyperspeed, Iridescence, LetterGlitch, Lightfall, Lightning, LightPillar, LightRays, LineWaves, LiquidChrome, LiquidEther, Orb, Particles, PixelBlast, PixelSnow, Plasma, PlasmaWave, Prism, PrismaticBurst, Radar, RippleGrid, ShapeGrid, SideRays, Silk, SoftAurora, Threads, Waves

### TextAnimations（文字动画，24 个）
ASCIIText, BlurText, CircularText, CountUp, CurvedLoop, DecryptedText, FallingText, FuzzyText, GlitchText, GradientText, RotatingText, ScrambleText, ScrollFloat, ScrollReveal, ScrollVelocity, ShinyText, Shuffle, SplitText, TextCursor, TextPressure, TextType, TrueFocus, VariableProximity

### Animations（动画，31 个）
AnimatedContent, Antigravity, BlobCursor, ClickSpark, Crosshair, Cubes, CursorGrid, ElectricBorder, FadeContent, GhostCursor, GlareHover, GradualBlur, ImageTrail, LaserFlow, LogoLoop, MagicRings, Magnet, MagnetLines, MetaBalls, MetallicPaint, Noise, OrbitImages, PixelTrail, PixelTransition, Ribbons, ShapeBlur, SplashCursor, StarBorder, StickerPeel, Strands, TargetCursor

### Components（交互组件，39 个）
AnimatedList, BorderGlow, BounceCards, BubbleMenu, CardNav, CardSwap, Carousel, ChromaGrid, CircularGallery, Counter, CurvedInput, DecayCard, Dock, DomeGallery, ElasticSlider, FlowingMenu, FlyingPosters, Folder, GlassIcons, GlassSurface, GooeyNav, InfiniteMenu, LineSidebar, MagicBento, Masonry, ModelViewer, OptionWheel, PillNav, PixelCard, ProfileCard, ReflectiveCard, ScrollStack, SpecularButton, SpotlightCard, Stack, StaggeredMenu, Stepper, TiltedCard

## 使用规则

1. **先查目录再写代码**：用户要求特定效果（如"光晕背景"→Aurora，"文字解密"→DecryptedText，"3D 卡片倾斜"→TiltedCard）时，从上方目录挑对应组件，不要手写轮子。
2. **组件都是 props 驱动的**：所有组件带 customization props，实现前先查看组件源码了解可调参数（如 color、speed、frequency、intensity 等）。
3. **技术栈约定**：Vue 3 + `<script setup>` + TypeScript + Tailwind。若项目不是此栈，先询问用户或做最小适配。
4. **性能**：背景类组件多为 canvas/GPU 密集型，仅在需要视觉冲击的场景使用，避免多个重量级背景叠加。
5. **AI 输出**：当用户要求"添加动画组件"时，输出可直接运行的 .vue 组件文件（含 props 类型定义），并说明如何引入到目标页面。
6. **无网络时**：组件代码直接从 vue-bits 仓库 (src/components/content) 复制，保持 MIT 许可声明。
