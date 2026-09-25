# Apple弹簧参数参考（Web映射 Motion / Framer‑Motion）
## 概念说明
- 阻尼比damping ratio：控制过冲弹跳；1.0临界阻尼无弹跳；小于1产生弹跳震荡，数值越小弹跳越强
- 响应response：单位秒，代表物体趋近目标的速度，不是固定动画时长，弹簧无固定时长

### Apple官方交互参数
|交互类型|阻尼比|响应时间(s)|
|---|---|---|
|移动/画中画|1.0|0.4|
|旋转动画|0.8|0.4|
|抽屉/底部弹窗sheet|0.8|0.3|

### Web映射
1. 默认普通UI：damping=1.0（临界阻尼，无弹跳）
2. 手势抛动/轻扫：damping≈0.8，少量弹跳，仅在手势带有动量时使用

### 速度移交公式
相对速度 = 手势释放速度 / (目标值 − 当前值)
> Framer‑Motion/Motion支持直接传入px/s绝对速度，不需要手动归一化。

### 动量投射公式（苹果官方）
```js
// decelerationRate：0.998普通滚动；0.99更干脆
function project(initialVelocity, decelerationRate = 0.998) {
  return (initialVelocity / 1000) * decelerationRate / (1 - decelerationRate);
}
const projectedEndpoint = currentPosition + project(releaseVelocity);
const target = 最近吸附点(projectedEndpoint);
