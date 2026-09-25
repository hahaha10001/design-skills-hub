---
name: tubiao-auto-icon-selector
description: 图标库选型与资源引用专项。仅在用户要求选择或比较图标库、查找特殊图标、离线图标资源时使用；普通按钮加图标先复用项目现有库，不为此启动选型或安装依赖。
---

# AI 自动图标选择器（国内网络优化版）

先复用项目已有图标库和本地资源，不擅自换库、安装依赖或修改包源。只有确实需要额外资源时才比较候选方案。

以下 CDN 说明和命令是候选示例，不是当前网络测速结果或执行授权；速度与可达性须现场核实。不要为了离线使用自动全局安装工具，优先复用已有资源。新增依赖或更换包源须先取得用户确认。

## 国内网络优化策略

### CDN 优先级（国内访问速度排序）

1. **jsdelivr** ⭐ 国内最快 - 有国内节点
2. **unpkg** - 国内可访问
3. **cdnjs** - Cloudflare 节点
4. **饿了么/百度/360 国内 CDN** - 国内源

### API 访问策略

- Iconify API 国内可直接访问
- 如无法访问，提供 npm 安装方案
- 提供 SVG 下载本地使用方案

## 快速使用

当用户需要图标时，自动执行以下流程：

### 1. 分析需求

从用户输入中提取：
- **项目类型**：Web/App/小程序/桌面应用
- **界面风格**：简约/商务/可爱/科技感/其他
- **使用场景**：导航/功能按钮/情绪/状态/分类
- **技术栈**：HTML/React/Vue/其他
- **网络环境**：国内/海外/不确定
- **特殊需求**：动态换色/动画/离线使用

### 2. 选择图标库（国内优化决策树）

```
项目类型判断：
├── Web/移动端 Web
│   ├── 简约现代风格 → Lucide（jsdelivr 国内加速）⭐ 推荐
│   ├── Material Design → Material Symbols（Google Fonts 国内可访问）
│   ├── 多种风格需求 → Phosphor Icons（jsdelivr）
│   └── 企业级应用 → Font Awesome（国内 CDN）
├── React 项目
│   └── 默认推荐 → Lucide React（npm 安装）
├── Vue 项目
│   └── 默认推荐 → Lucide Vue（npm 安装）
├── 小程序
│   └── 推荐 → 本地 SVG / 阿里巴巴矢量图标库
└── 通用/不确定
    └── 默认推荐 → Iconify（国内可访问）
```

### 3. 生成图标方案

根据选择，输出：
1. **图标库名称** + 推荐理由（含国内访问说明）
2. **国内优化的 CDN/npm 方案**
3. **按场景分类的图标列表**
4. **代码示例**（匹配用户技术栈）
5. **备选方案**（网络不稳定时的替代）

## 国内优化图标库速查表

| 图标库 | 风格 | 数量 | 最佳场景 | 国内 CDN 方案 |
|--------|------|------|----------|---------------|
| **Lucide** | 简约线条 | 1000+ | 现代Web/App | `https://cdn.jsdelivr.net/npm/lucide@latest` ⭐ |
| **Phosphor** | 多种风格 | 7000+ | 多样化需求 | `https://cdn.jsdelivr.net/npm/@phosphor-icons/web` |
| **Heroicons** | 简洁 | 300+ | Tailwind项目 | `https://cdn.jsdelivr.net/npm/heroicons@2.0.13` |
| **Material** | Material Design | 1500+ | Android/企业 | `https://fonts.googleapis.cn`（国内镜像） |
| **Tabler** | 线条风格 | 4000+ | 仪表盘/后台 | `https://cdn.jsdelivr.net/npm/@tabler/icons` |
| **Iconify** | 聚合所有 | 10万+ | 通用/不确定 | `https://api.iconify.design/`（国内可访问） |
| **Iconfont** | 多样 | 2000万+ | 国内项目 | 阿里巴巴矢量图标库 |

## 国内优化 CDN 链接

### 首选：jsdelivr（国内有节点）

```html
<!-- Lucide -->
<script src="https://cdn.jsdelivr.net/npm/lucide@0.263.1/dist/umd/lucide.min.js"></script>

<!-- Phosphor Icons -->
<script src="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.0.3"></script>

<!-- Tabler Icons -->
<script src="https://cdn.jsdelivr.net/npm/@tabler/icons@2.30.0"></script>

<!-- Heroicons -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/heroicons@2.0.13/24/outline/style.css">
```

### 备选：unpkg

```html
<!-- 当 jsdelivr 不稳定时使用 -->
<script src="https://unpkg.com/lucide@latest"></script>
```

### 国内 npm 镜像（安装包时）

```bash
# 使用淘宝镜像
npm install lucide-react --registry=https://registry.npmmirror.com

# 或使用 cnpm
cnpm install lucide-react
```

## 场景图标映射（国内可用）

### 导航类
```
首页: lucide:home / heroicons:home / material:home
搜索: lucide:search / heroicons:magnifying-glass
返回: lucide:arrow-left / heroicons:arrow-left
设置: lucide:settings / material:settings
用户: lucide:user / heroicons:user
菜单: lucide:menu / material:menu
```

### 功能操作类
```
添加: lucide:plus / heroicons:plus
编辑: lucide:pencil / heroicons:pencil
删除: lucide:trash-2 / heroicons:trash
保存: lucide:save / material:save
分享: lucide:share-2 / heroicons:share
上传: lucide:upload / heroicons:arrow-up-tray
下载: lucide:download / heroicons:arrow-down-tray
```

### 情绪/状态类
```
开心: lucide:smile / material:sentiment-satisfied
难过: lucide:frown / material:sentiment-dissatisfied
生气: lucide:angry (Phosphor) / material:sentiment-very-dissatisfied
平静: lucide:meh / material:sentiment-neutral
疲惫: lucide:zzz / material:fatigue
喜欢: lucide:heart / heroicons:heart
```

### 日常活动类
```
吃饭: lucide:utensils / material:restaurant
睡觉: lucide:moon / heroicons:moon
运动: lucide:dumbbell / material:fitness-center
工作: lucide:briefcase / material:work
学习: lucide:book-open / heroicons:book-open
娱乐: lucide:gamepad-2 / material:sports-esports
购物: lucide:shopping-bag / material:shopping-bag
```

## 国内优化代码生成模板

### HTML + jsdelivr CDN（推荐）

```html
<!-- Lucide - 国内最快 -->
<script src="https://cdn.jsdelivr.net/npm/lucide@0.263.1/dist/umd/lucide.min.js"></script>
<i data-lucide="home"></i>
<script>lucide.createIcons();</script>

<!-- Iconify - 国内可访问 -->
<span class="iconify" data-icon="lucide:home"></span>
<script src="https://code.iconify.design/3/3.1.0/iconify.min.js"></script>

<!-- Phosphor Icons -->
<script src="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.0.3"></script>
<i class="ph ph-house"></i>
```

### React（npm + 淘宝镜像）

```bash
npm install lucide-react --registry=https://registry.npmmirror.com
```

```jsx
import { Home, User, Settings } from 'lucide-react';
<Home size={24} color="#333" />

import { Icon } from '@iconify/react';
<Icon icon="lucide:home" width={24} />
```

### Vue（npm + 淘宝镜像）

```bash
npm install lucide-vue-next --registry=https://registry.npmmirror.com
```

```vue
<script setup>
import { Home, User } from 'lucide-vue-next';
</script>
<template>
  <Home :size="24" color="#333" />
</template>
```

### API 动态获取（国内可访问）

```javascript
fetch('https://api.iconify.design/lucide/home.svg?width=24&color=%23333')
  .then(r => r.text())
  .then(svg => console.log(svg));

fetch('https://api.iconify.design/lucide/home.json')
  .then(r => r.json())
  .then(data => console.log(data.body));
```

## 离线使用方案（国内网络不稳定时）

### 方案1：下载 SVG 到本地

```bash
npm install -g @iconify/tools
curl -o home.svg "https://api.iconify.design/lucide/home.svg"
```

### 方案2：使用 SVG Sprite

```html
<svg style="display: none;">
  <symbol id="icon-home" viewBox="0 0 24 24">
    <path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/>
  </symbol>
</svg>
<svg><use href="#icon-home"/></svg>
```

### 方案3：阿里巴巴 Iconfont（国内首选）

```html
<link rel="stylesheet" href="//at.alicdn.com/t/font_xxxxxx.css">
<i class="iconfont icon-home"></i>
```

## 网络问题排查

### CDN 无法访问时

1. **切换到 unpkg**：将 `cdn.jsdelivr.net` 替换为 `unpkg.com`
2. **使用本地文件**：下载 SVG 到项目目录
3. **使用 npm 安装**：配合淘宝镜像 `registry.npmmirror.com`
4. **使用 Iconfont**：阿里巴巴矢量图标库，国内最快

### API 无法访问时

1. **使用 npm 包**：`npm install @iconify/json`
2. **下载离线数据**：从 GitHub 下载图标 JSON
3. **使用 SVG Sprite**：将图标合并为本地文件

## 参考资料

- 完整图标库对比：见 `references/icon-libraries.md`
- 场景映射表：见 `references/scene-mapping.md`
- 国内 CDN 对比：见 `references/china-cdn-guide.md`
