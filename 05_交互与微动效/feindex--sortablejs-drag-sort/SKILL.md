---
name: sortablejs-drag-sort
description: Use when selecting or implementing drag sorting, draggable lists, SortableJS, dnd-kit, or related drag-and-drop UI.
---

# 拖拽排序方案选择 Skill

## 触发条件

当用户提到以下关键词时自动调用此 Skill：
- 拖拽排序
- 拖动排序
- drag sort
- 列表排序
- 可拖拽列表
- 拖拽功能
- 排序功能
- sortable
- 拖拽组件
- 拖拽库
- 拖拽方案
- 拖拽选型

---

## 🎯 方案选择指南

### 第一步：确定技术栈

| 技术栈 | 推荐方案 | 理由 |
|--------|----------|------|
| **原生 JS / 通用** | SortableJS | 零依赖、功能全、文档好 |
| **React 新项目** | dnd-kit | 现代化、TypeScript、社区活跃 |
| **React 老项目** | react-beautiful-dnd | 成熟稳定、生态丰富 |
| **Vue 2/3** | Vue.Draggable | 官方封装、与响应式集成 |
| **Angular** | @angular/cdk/drag-drop | 官方支持、符合 Angular 风格 |
| **包大小敏感** | 原生 HTML5 API | 零体积、性能最好 |

### 第二步：分析场景复杂度

#### 场景 A：简单列表排序
**特征**：
- 单一列表
- 垂直排列
- 无需跨列表
- 基础动画即可

**推荐**：SortableJS（最简单）或 原生 API

#### 场景 B：看板/多列拖拽
**特征**：
- 多列之间拖拽
- 卡片有复杂内容
- 需要状态管理

**推荐**：
- React: dnd-kit 或 react-beautiful-dnd
- Vue: Vue.Draggable
- 原生: SortableJS（group 配置）

#### 场景 C：网格/自由拖拽
**特征**：
- 二维布局
- 自由定位
- 可能需要缩放/旋转

**推荐**：
- React: dnd-kit（@dnd-kit/core）
- 原生: SortableJS（grid 模式）

#### 场景 D：复杂自定义
**特征**：
- 拖拽预览自定义
- 复杂动画
- 拖拽层叠关系

**推荐**：dnd-kit（React）或 react-dnd

#### 场景 E：树形/嵌套排序
**特征**：
- 层级结构
- 可折叠展开
- 父子关系

**推荐**：
- React: @dnd-kit/sortable + tree 扩展
- 原生: SortableJS（嵌套 group）

### 第三步：考虑特殊需求

| 需求 | 推荐方案 |
|------|----------|
| **触摸设备优先** | SortableJS（内置优化）或 dnd-kit |
| **无障碍访问** | dnd-kit（WCAG 支持最好） |
| **SSR 支持** | dnd-kit（Next.js 友好） |
| **旧浏览器兼容** | SortableJS（支持 IE9+） |
| **极致性能** | 原生 API 或 Pragmatic Drag and Drop |
| **快速上手** | SortableJS 或 react-beautiful-dnd |

---

## 📊 方案详细对比

### 1. SortableJS（通用首选）
```bash
npm install sortablejs
```
**优点**：
- ✅ 零依赖，体积小
- ✅ 框架无关
- ✅ 功能全面（列表、网格、看板、嵌套）
- ✅ 触摸设备优化
- ✅ IE9+ 兼容

**缺点**：
- ❌ React/Vue 需手动集成
- ❌ 复杂自定义较麻烦

**适用**：快速开发、通用场景、老项目

---

### 2. dnd-kit（React 现代化）
```bash
npm install @dnd-kit/core @dnd-kit/sortable
```
**优点**：
- ✅ TypeScript 原生
- ✅ 模块化设计
- ✅ 无障碍访问支持
- ✅ 动画系统完善
- ✅ SSR 友好

**缺点**：
- ❌ 学习曲线稍陡
- ❌ React 专用

**适用**：React 新项目、复杂交互、企业级应用

---

### 3. react-beautiful-dnd（React 经典）
```bash
npm install react-beautiful-dnd
```
**优点**：
- ✅ 设计精美
- ✅ 内置动画流畅
- ✅ API 简洁
- ✅ Atlassian 维护

**缺点**：
- ❌ 包体积较大
- ❌ 维护频率降低（推荐迁移到 Pragmatic）

**适用**：追求视觉效果、已有项目

---

### 4. Vue.Draggable（Vue 专用）
```bash
npm install vuedraggable
```
**优点**：
- ✅ Vue 组件化
- ✅ 与响应式系统集成
- ✅ SortableJS 封装

**缺点**：
- ❌ Vue 专用
- ❌ Vue 3 需用下一代版本

**适用**：Vue 项目

---

### 5. 原生 HTML5 Drag & Drop API
```javascript
// 无需安装
element.draggable = true;
```
**优点**：
- ✅ 零依赖
- ✅ 性能最好
- ✅ 浏览器原生支持

**缺点**：
- ❌ API 设计老旧
- ❌ 移动端支持差
- ❌ 需自行处理大量细节

**适用**：简单场景、包大小敏感

---

### 6. Pragmatic Drag and Drop（跨框架新贵）
```bash
npm install @atlaskit/pragmatic-drag-and-drop
```
**优点**：
- ✅ 跨框架（React/Vue/Angular/Svelte）
- ✅ 极轻量
- ✅ 性能优异
- ✅ Atlassian 2024 新版

**缺点**：
- ❌ 生态较新
- ❌ 文档待完善

**适用**：追求性能、多技术栈团队

---

## 🚀 快速决策流程

```
开始
  │
  ├─ 技术栈？
  │   ├─ React → 新项目用 dnd-kit，老项目用 react-beautiful-dnd
  │   ├─ Vue → Vue.Draggable
  │   ├─ Angular → @angular/cdk/drag-drop
  │   └─ 原生/通用 → SortableJS
  │
  ├─ 复杂度？
  │   ├─ 简单列表 → SortableJS
  │   ├─ 看板/多列 → 框架对应方案
  │   ├─ 网格/自由 → dnd-kit 或 SortableJS
  │   └─ 复杂自定义 → dnd-kit
  │
  └─ 特殊需求？
      ├─ 包大小敏感 → 原生 API 或 Pragmatic
      ├─ 无障碍优先 → dnd-kit
      └─ 旧浏览器 → SortableJS
```

---

## 💡 推荐组合

| 项目类型 | 推荐方案 | 理由 |
|----------|----------|------|
| **React 企业级** | dnd-kit | 现代化、可维护 |
| **React 后台系统** | react-beautiful-dnd | 快速开发、美观 |
| **Vue 项目** | Vue.Draggable | 生态成熟 |
| **多技术栈团队** | SortableJS | 统一方案 |
| **极致性能** | Pragmatic DnD | 轻量高效 |
| **快速原型** | SortableJS | 5 分钟上手 |

---

## 🔧 核心能力

提供拖拽排序的专业指导，包括：
1. **方案选型分析** - 根据场景推荐最佳方案
2. **安装和基础配置** - 各方案的快速开始
3. **常用 API 和选项** - 详细配置说明
4. **框架集成** - React/Vue/Angular 集成方案
5. **常见问题解决方案** - 踩坑指南
6. **最佳实践** - 性能优化、用户体验

## 快速开始

### 1. NPM 安装

```bash
npm install sortablejs
```

### 2. 基础用法

```javascript
import Sortable from 'sortablejs';

// 基础配置
const sortable = new Sortable(document.getElementById('list'), {
  animation: 150,           // 动画时长（毫秒）
  ghostClass: 'sortable-ghost',  // 占位符样式类
  chosenClass: 'sortable-chosen', // 选中项样式类
  dragClass: 'sortable-drag',     // 拖拽中样式类
});
```

### 3. HTML 结构

```html
<ul id="list">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```

### 4. 基础 CSS

```css
.sortable-ghost {
  opacity: 0.4;
  background: #f0f0f0;
}

.sortable-chosen {
  background: #e3f2fd;
}

.sortable-drag {
  opacity: 0.9;
  box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}
```

## 常用配置选项

| 选项 | 类型 | 说明 | 默认值 |
|------|------|------|--------|
| `animation` | Number | 动画时长（毫秒） | 0 |
| `delay` | Number | 延迟触发时间（毫秒） | 0 |
| `delayOnTouchOnly` | Boolean | 仅在触摸时延迟 | false |
| `handle` | String | 拖拽手柄选择器 | - |
| `draggable` | String | 可拖拽元素选择器 | - |
| `group` | String/Object | 分组名称，实现跨列表拖拽 | - |
| `sort` | Boolean | 是否允许排序 | true |
| `disabled` | Boolean | 是否禁用 | false |

## 事件回调

```javascript
const sortable = new Sortable(el, {
  onChoose: function(evt) { console.log('选中:', evt.oldIndex); },
  onStart: function(evt) { console.log('开始:', evt.oldIndex); },
  onEnd: function(evt) {
    console.log('从', evt.oldIndex, '移动到', evt.newIndex);
    console.log('原列表:', evt.from);
    console.log('目标列表:', evt.to);
  },
  onAdd: function(evt) { console.log('从其他列表添加'); },
  onRemove: function(evt) { console.log('移除到其他列表'); },
  onUpdate: function(evt) { console.log('排序更新'); },
  onSort: function(evt) { console.log('排序变化'); }
});
```

## 跨列表拖拽

```javascript
const listA = new Sortable(document.getElementById('list-a'), {
  group: { name: 'shared', pull: true, put: false }
});
const listB = new Sortable(document.getElementById('list-b'), {
  group: { name: 'shared', pull: false, put: true }
});
const listC = new Sortable(document.getElementById('list-c'), {
  group: 'shared'
});
```

## 框架集成

### React

```jsx
import { useEffect, useRef } from 'react';
import Sortable from 'sortablejs';

function SortableList({ items, onSort }) {
  const listRef = useRef(null);
  const sortableRef = useRef(null);

  useEffect(() => {
    if (listRef.current) {
      sortableRef.current = new Sortable(listRef.current, {
        animation: 150,
        onEnd: (evt) => {
          const newItems = [...items];
          const [moved] = newItems.splice(evt.oldIndex, 1);
          newItems.splice(evt.newIndex, 0, moved);
          onSort(newItems);
        }
      });
    }
    return () => sortableRef.current?.destroy();
  }, [items]);

  return (
    <ul ref={listRef}>
      {items.map((item) => (
        <li key={item.id} data-id={item.id}>{item.name}</li>
      ))}
    </ul>
  );
}
```

### Vue 3

```vue
<template>
  <ul ref="listRef">
    <li v-for="item in items" :key="item.id" :data-id="item.id">
      {{ item.name }}
    </li>
  </ul>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import Sortable from 'sortablejs';

const props = defineProps(['items']);
const emit = defineEmits(['sort']);
const listRef = ref(null);
let sortable = null;

onMounted(() => {
  sortable = new Sortable(listRef.value, {
    animation: 150,
    onEnd: (evt) => {
      const newItems = [...props.items];
      const [moved] = newItems.splice(evt.oldIndex, 1);
      newItems.splice(evt.newIndex, 0, moved);
      emit('sort', newItems);
    }
  });
});

onUnmounted(() => sortable?.destroy());
</script>
```

## 常用方法

```javascript
sortable.destroy();
const ids = sortable.toArray();
sortable.sort(['id-1', 'id-2', 'id-3']);
sortable.option('disabled', true);
sortable.option('disabled', false);
sortable.save();
```

## 最佳实践

### 1. 触摸设备优化

```javascript
const sortable = new Sortable(el, {
  delay: 200,
  delayOnTouchOnly: true,
  touchStartThreshold: 5
});
```

### 2. 拖拽手柄

```html
<li>
  <span class="handle">☰</span>
  <span>Item content</span>
</li>
```

```javascript
const sortable = new Sortable(el, { handle: '.handle' });
```

### 3. 过滤不可拖拽元素

```javascript
const sortable = new Sortable(el, {
  filter: '.no-drag',
  preventOnFilter: false
});
```

### 4. 保存和恢复排序

```javascript
sortable.options.store = {
  get: function(sortable) {
    const order = localStorage.getItem(sortable.options.group.name);
    return order ? order.split('|') : [];
  },
  set: function(sortable) {
    const order = sortable.toArray();
    localStorage.setItem(sortable.options.group.name, order.join('|'));
  }
};
```

## 常见问题

### Q: 移动端无法拖拽？
A: 添加 `delay` 和 `delayOnTouchOnly` 选项，避免与滚动冲突。

### Q: 如何获取排序后的数据？
A: 使用 `onEnd` 事件的 `newIndex` 和 `oldIndex` 更新数据数组。

### Q: 如何禁止某些元素拖拽？
A: 使用 `filter` 选项指定不可拖拽的元素选择器。

### Q: 拖拽时页面滚动怎么办？
A: 使用 `forceFallback: true` 启用备用拖拽模式。

## 参考资源

- **官方文档**: https://sortablejs.github.io/Sortable/
- **GitHub**: https://github.com/SortableJS/Sortable
- **TypeScript 定义**: @types/sortablejs
