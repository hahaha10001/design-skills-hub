---
name: chart-png-cjk
description: 用 matplotlib 生成含中文的深色金融图表 PNG（K线/走势图/对比图）。当需要导出带中文标签的行情图、股价走势图、K线图、金融数据可视化图片时使用。内含中文字体正确加载、$ 转义、纵轴标定等关键避坑要点。
agent_created: true
---

# 生成含中文的金融图表 PNG

在 Windows 环境下用 matplotlib 导出**带中文标注**的深色主题金融图表。

## 环境选择（重要）

**优先用系统 Python，不要急着建 venv。**

```bash
# 先探测系统 Python 是否已有 matplotlib / fontTools
/d/Python/Python312/python.exe -c "import matplotlib,fontTools; print('ok')"
```

原因：本机 `C:\Users\xxx\.workbuddy\binaries\python\envs\default` 里的 pip 安装
matplotlib 经常因网络问题长时间卡住（实测 >6 分钟无进展）。
系统 Python (`D:\Python\Python312`) 通常已预装 matplotlib + fontTools + Pillow，直接用。

只有当系统 Python 确实缺包、且 pip 可正常工作时，才新建 venv。

## 中文字体加载（最容易踩的坑）

Windows 可用的中文字体（已验证含 CJK 字形）：

| 字体 | 路径 | 备注 |
|---|---|---|
| HarmonyOS Sans SC | `C:\Windows\Fonts\HarmonyOS_Sans_SC_Regular.ttf` | 推荐，无衬线，字形干净 |
| HarmonyOS Sans SC Bold | `C:\Windows\Fonts\HarmonyOS_Sans_SC_Bold.ttf` | 标题用 |
| 微软雅黑 | `C:\Windows\Fonts\msyh.ttc` | 需 `fontNumber=0` |

注意 `Glob` 工具搜 `C:\Windows\Fonts\*.tt*` 可列出全部字体；
`ls` / `grep` / `head` 在 Git Bash shim 下不可用，不要依赖。

### 关键：必须用 fontproperties 显式下发

```python
import matplotlib
matplotlib.use("Agg")
from matplotlib import font_manager
from fontTools.ttLib import TTFont

P = r"C:\Windows\Fonts\HarmonyOS_Sans_SC_Regular.ttf"
font_manager.fontManager.addfont(P)
FP = font_manager.FontProperties(fname=P)

# 验证字体真的含中文字形（避免拿到只有拉丁字符的字体）
tt = TTFont(P, fontNumber=0, lazy=True)
assert ord("苹") in tt.getBestCmap(), "该字体无中文字形"
tt.close()

PB = r"C:\Windows\Fonts\HarmonyOS_Sans_SC_Bold.ttf"
font_manager.fontManager.addfont(PB)
FPB = font_manager.FontProperties(fname=PB, weight="bold")
```

**踩坑记录：** 仅设置 `plt.rcParams["font.sans-serif"]` 是**不够**的。
`ax.annotate()`、`legend(prop=...)`、`set_yticklabels()`、以及
mathtext 内部字体族 `'rm'` 都不吃 rcParams，会报
`Font 'rm' does not have a glyph for '\u5e74'`。

**正确做法：每一处文本都显式传 `fontproperties=FP`：**

```python
fig.text(..., fontproperties=FP)
ax.annotate(..., fontproperties=FPB)
ax.set_yticklabels(labels, fontproperties=FP)
ax.legend(..., prop=FP)          # legend 用 prop，不是 fontproperties
axv.set_xticklabels(labels, fontproperties=FP)
```

## `$` 符号转义（第二容易踩的坑）

matplotlib 默认把 `$...$` 当 LaTeX 数学公式解析。
文本里同时出现两个价格（如 `从 $705.07 跌至 $385.10`）会导致
中间内容被当成公式而**严重错乱/消失**。

```python
plt.rcParams["mathtext.default"] = "regular"

def tex(s):
    """转义 $，防止价格被当作数学公式"""
    return s.replace("$", r"\$")

fig.text(..., tex("从 $705.07 跌至 $385.10"), ...)
```

## 纵轴标定（K 线图必看）

**不要把纵轴按"历史极值"设范围。** 2014 年 7:1 拆股还原后的月度价格
在 95~176 区间波动，若纵轴设 `350~750` 去容纳 `$705` / `$385` 两个盘中极值，
K 线会被压成一条线，完全看不出走势。

做法：**纵轴按月度收盘价实际区间标定**（如 `92~180`），
把 `$705.07` / `$385.10` 这类盘中极值放进**标注卡文字**里单独说明。

```python
YLO, YHI = 92, 180                  # 按月度收盘价区间
ax.set_ylim(YLO, YHI)
ax.annotate(tex("2012.09 盘中高点 $705.07"), xy=(IPK, highs[IPK]), ...)
```

## K 线层级 zorder 约定

避免"底色遮住 K 线"：

| 元素 | zorder |
|---|---|
| 网格 | 1 |
| 下跌区间底色 `axvspan` | 2 |
| 阶段竖线 / 水平虚线 | 3 |
| K 线影线 | 4 |
| K 线实体 | 5 |
| 均线 | 6 |
| 箭弧 | 8 |
| 箭头 | 9 |
| 百分比徽章 | 10 |
| 标注卡 | 12 |

## 配色（中国市场惯例）

```
上涨 = 红  #e44a3f     下跌 = 绿  #20b26c
深色底:  BG #0d1015   PANEL #141920   GRID #2a323d
文字:    TXT #eef2f8   DIM #9aa7b7   FAINT #737f8d
强调:    ACC #f2a63e   BLUE #4e9eec
```

## 布局参数（避免重叠）

```python
fig = plt.figure(figsize=(17, 11.2), dpi=200, facecolor=BG)
gs = fig.add_gridspec(2, 1, height_ratios=[3.5, 1.0], hspace=0.09,
                      left=0.062, right=0.970,
                      top=0.800,     # 给 3 行标题留空间
                      bottom=0.150)  # 给年份标签+页脚留空间
```

- 标题三行分别放 `y=0.976 / 0.920 / 0.886`
- 年份标签用 `axv.text(..., y=-7.2, va="top")`，页脚 `fig.text(y=0.030)`，
  两者间距要够，否则重叠
- 标注卡放在绘图区**外侧**（`xytext` 超出 ylim 一点），避免遮挡 K 线

## 输出

```python
plt.savefig(out, facecolor=BG, dpi=200, bbox_inches="tight", pad_inches=0.32)
```

`dpi=200` + `figsize=(17,11.2)` ≈ 3312×2262，适合 PPT 全屏投放。

## 验证

渲染后**必须**用 Read 工具看图确认：
1. 中文是否全部正常显示（无方块/乱码）
2. 价格数字是否完整（`$` 转义是否生效）
3. K 线是否清晰可见（纵轴标定是否合理）
4. 各文字块是否重叠
