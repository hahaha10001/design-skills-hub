#!/usr/bin/env python3
"""
Apple UI代码片段简易格式化生成脚本
WorkBuddy技能脚本，Bash调用
"""
import sys

CSS_TPL = """
/* Apple风格毛玻璃工具栏 */
.toolbar {{
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px) saturate(180%);
  border-top: 1px solid rgba(255, 255, 255, 0.4);
}}
/* 按钮按下即时反馈 */
.button:active {{
  transform: scale(0.97);
  transition: transform 100ms ease-out;
}}
"""

REDUCED_MOTION_TPL = """
@media (prefers-reduced-motion: reduce) {
  .sheet { transition: opacity 200ms ease; transform: none !important; }
}
@media (prefers-reduced-transparency: reduce) {
  .toolbar { background: white; backdrop-filter: none; }
}
"""

if __name__ == "__main__":
    arg = sys.stdin.read().strip()
    if "glass" in arg:
        print(CSS_TPL)
    elif "access" in arg:
        print(REDUCED_MOTION_TPL)
    else:
        print("# Apple‑UI 代码片段模板\n请输入关键词 glass / access 获取对应代码")
