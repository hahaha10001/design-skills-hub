---
name: frontend-components
description: Use for choosing and implementing frontend UI components, feature modules, and interaction patterns.
---

# 前端功能模块总 Skill

> 一站式前端组件功能解决方案，参考 Ant Design、Material UI、Element Plus 等主流组件库设计体系

---

## 🎯 触发条件（自动识别）

当用户提到以下任何关键词时，**自动调用此 Skill**：

### 通用触发词
- 前端组件、UI 组件、功能模块、页面功能
- 组件实现、交互功能、界面元素

### 数据展示类（自动匹配子 Skill）
- 表格、Table、数据表格、列表、List
- 卡片、Card、树形、Tree、日历、Calendar
- 时间轴、Timeline、统计、Statistic、二维码、QRCode
- 图片展示、Image、轮播、Carousel、折叠面板、Collapse

### 数据录入类（自动匹配子 Skill）
- 表单、Form、输入框、Input、选择器、Select
- 日期选择、DatePicker、时间选择、TimePicker
- 文件上传、Upload、图片上传、多选、Checkbox
- 单选、Radio、开关、Switch、滑块、Slider

### 反馈类（自动匹配子 Skill）
- 弹窗、Modal、对话框、Dialog、抽屉、Drawer
- 消息提示、Message、通知、Notification
- 进度条、Progress、加载中、Loading、Spin
- 骨架屏、Skeleton、气泡卡片、Popover
- 确认框、Confirm、结果页、Result

### 导航类（自动匹配子 Skill）
- 菜单、Menu、导航、Navigation、标签页、Tabs
- 面包屑、Breadcrumb、分页、Pagination
- 步骤条、Steps、下拉菜单、Dropdown、锚点、Anchor

### 布局类（自动匹配子 Skill）
- 栅格、Grid、布局、Layout、间距、Space
- 分割线、Divider

### 其他功能类（自动匹配子 Skill）
- 水印、Watermark、回到顶部、BackTop
- 引导、Tour、拖拽排序、DragSort、拖动排序

---

## 🤖 AI 自动调用指南

### 调用逻辑
```
用户输入
    │
    ├─ 包含具体组件名？
    │   ├─ 是 → 直接调用对应子 Skill
    │   └─ 否 → 继续分析
    │
    ├─ 包含场景描述？
    │   ├─ 是 → 根据场景推荐组件
    │   └─ 否 → 询问具体需求
    │
    └─ 输出：完整实现代码
```

### 自动匹配规则
| 用户说 | AI 自动调用 |
|--------|-------------|
| "我要做个表格" | `sub-skills/data-display/table.md` |
| "需要表单验证" | `sub-skills/data-entry/form.md` |
| "做个弹窗" | `sub-skills/feedback/modal.md` |
| "上传功能" | `sub-skills/data-entry/upload.md` |
| "导航菜单" | `sub-skills/navigation/menu.md` |
| "加载状态" | `sub-skills/feedback/spin.md` |
| "步骤引导" | `sub-skills/navigation/steps.md` |

---

## 📚 功能模块分类体系

借鉴 Ant Design、Material UI、Element Plus 等主流组件库，将前端功能分为 **6 大类 40+ 子模块**：

### 1️⃣ 通用类（General）
基础视觉元素，构建页面的基石
- Button 按钮
- Icon 图标
- Typography 排版

### 2️⃣ 布局类（Layout）
页面结构组织
- Grid 栅格
- Layout 布局
- Space 间距
- Divider 分割线

### 3️⃣ 导航类（Navigation）
页面跳转和位置感知
- Menu 导航菜单
- Tabs 标签页
- Breadcrumb 面包屑
- Dropdown 下拉菜单
- Pagination 分页
- Steps 步骤条
- Anchor 锚点

### 4️⃣ 数据录入类（Data Entry）
用户输入和数据提交
- Form 表单
- Input 输入框
- Select 选择器
- Checkbox 多选框
- Radio 单选框
- Switch 开关
- Slider 滑块
- DatePicker 日期选择
- TimePicker 时间选择
- Upload 上传
- Transfer 穿梭框
- Mentions 提及

### 5️⃣ 数据展示类（Data Display）
数据呈现和可视化
- Table 表格
- List 列表
- Card 卡片
- Collapse 折叠面板
- Descriptions 描述列表
- Empty 空状态
- Image 图片
- Carousel 走马灯
- Calendar 日历
- Badge 徽标
- Tag 标签
- Timeline 时间轴
- Tree 树形控件
- Statistic 统计数值
- QRCode 二维码

### 6️⃣ 反馈类（Feedback）
用户操作反馈
- Modal 对话框
- Drawer 抽屉
- Message 消息提示
- Notification 通知
- Progress 进度条
- Spin 加载中
- Skeleton 骨架屏
- Popover 气泡卡片
- Popconfirm 气泡确认框
- Result 结果

### 7️⃣ 其他功能类（Other）
特殊场景功能
- Affix 固钉
- BackTop 回到顶部
- ConfigProvider 全局配置
- Watermark 水印
- Tour 漫游式引导
- FloatButton 浮动按钮

---

## 🚀 快速决策流程

```
用户需要实现某个功能
        │
        ├─ 是什么类型的功能？
        │   ├─ 基础元素 → 通用类
        │   ├─ 页面结构 → 布局类
        │   ├─ 页面跳转 → 导航类
        │   ├─ 用户输入 → 数据录入类
        │   ├─ 数据展示 → 数据展示类
        │   ├─ 操作反馈 → 反馈类
        │   └─ 特殊功能 → 其他功能类
        │
        └─ 调用对应子 Skill 生成代码
```

---

## 📖 子 Skill 调用指南

每个子 Skill 都包含：
1. **功能描述** - 该组件的作用和适用场景
2. **技术方案** - 推荐的技术栈和库
3. **基础用法** - 最简单的实现代码
4. **高级特性** - 复杂场景的配置
5. **最佳实践** - 性能优化和用户体验建议
6. **提示词模板** - 直接可用的 AI 提示词

---

## 🛠️ 技术栈支持

### React 生态
- **Ant Design** - 企业级 UI 设计语言
- **Material UI (MUI)** - Google Material Design
- **Chakra UI** - 模块化、可访问
- **Radix UI** - 无样式、可定制
- **shadcn/ui** - 基于 Tailwind 的组件库

### Vue 生态
- **Element Plus** - 饿了么开源组件库
- **Ant Design Vue** - Ant Design 的 Vue 实现
- **Vuetify** - Material Design 组件库
- **Naive UI** - 图森未来开源
- **Quasar** - 跨平台框架

### 原生/通用
- **Tailwind UI** - 基于 Tailwind CSS
- **Bootstrap** - 经典响应式框架
- **Bulma** - 现代 CSS 框架
- **自定义实现** - 从零构建

---

## 💡 使用示例

### 场景 1：用户说"我要做一个表格"
```
AI 识别：数据展示类 → Table 表格
调用子 Skill：table-component
输出：Table 的完整实现代码
```

### 场景 2：用户说"需要表单验证"
```
AI 识别：数据录入类 → Form 表单
调用子 Skill：form-component
输出：带验证的表单实现
```

### 场景 3：用户说"做个弹窗"
```
AI 识别：反馈类 → Modal 对话框
调用子 Skill：modal-component
输出：Modal 的多种用法
```

---

## 📁 目录结构

```
frontend-components/
├── SKILL.md                    # 本文件（总纲）
├── CATALOG.md                  # 功能模块速查表
├── PROMPTS.md                  # 提示词模板合集
└── sub-skills/                 # 子 Skill 目录
    ├── general/                # 通用类
    │   ├── button.md
    │   ├── icon.md
    │   └── typography.md
    ├── layout/                 # 布局类
    │   ├── grid.md
    │   ├── layout.md
    │   ├── space.md
    │   └── divider.md
    ├── navigation/             # 导航类
    │   ├── menu.md
    │   ├── tabs.md
    │   ├── breadcrumb.md
    │   ├── dropdown.md
    │   ├── pagination.md
    │   ├── steps.md
    │   └── anchor.md
    ├── data-entry/             # 数据录入类
    │   ├── form.md
    │   ├── input.md
    │   ├── select.md
    │   ├── checkbox.md
    │   ├── radio.md
    │   ├── switch.md
    │   ├── slider.md
    │   ├── date-picker.md
    │   ├── time-picker.md
    │   ├── upload.md
    │   ├── transfer.md
    │   └── mentions.md
    ├── data-display/           # 数据展示类
    │   ├── table.md
    │   ├── list.md
    │   ├── card.md
    │   ├── collapse.md
    │   ├── descriptions.md
    │   ├── empty.md
    │   ├── image.md
    │   ├── carousel.md
    │   ├── calendar.md
    │   ├── badge.md
    │   ├── tag.md
    │   ├── timeline.md
    │   ├── tree.md
    │   ├── statistic.md
    │   └── qrcode.md
    ├── feedback/               # 反馈类
    │   ├── modal.md
    │   ├── drawer.md
    │   ├── message.md
    │   ├── notification.md
    │   ├── progress.md
    │   ├── spin.md
    │   ├── skeleton.md
    │   ├── popover.md
    │   ├── popconfirm.md
    │   └── result.md
    └── other/                  # 其他功能类
        ├── affix.md
        ├── back-top.md
        ├── config-provider.md
        ├── watermark.md
        ├── tour.md
        ├── float-button.md
        └── drag-sort.md          # 拖拽排序
```

---

## 🔗 相关 Skill

- `sortablejs-drag-sort` - 拖拽排序专项
- `frontend-design` - 前端视觉设计
- `web-coding-workflow` - Web 开发标准化流程

---

## 📚 参考资源

- [Ant Design 组件总览](https://ant-design.antgroup.com/components/overview-cn)
- [Material UI 组件](https://mui.com/material-ui/all-components/)
- [Element Plus 组件](https://element-plus.org/zh-CN/component/button.html)
- [DevUI 组件](https://devui.design/components/get-start)

---

## 🎯 核心能力

提供前端功能模块的一站式解决方案：
1. **智能分类** - 自动识别功能类型
2. **方案推荐** - 根据技术栈推荐最佳实现
3. **代码生成** - 提供完整的实现代码
4. **最佳实践** - 性能优化和用户体验建议
5. **提示词模板** - 直接可用的 AI 提示词
