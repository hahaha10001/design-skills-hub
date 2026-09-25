#!/usr/bin/env python3
"""
ultra-frontend audit script
Usage: python3 scripts/audit.py <file.html|file.jsx|file.tsx>
Checks for: accessibility, performance, UX anti-patterns, CSS issues
"""

import sys
import re
from pathlib import Path

def audit(filepath):
    path = Path(filepath)
    if not path.exists():
        print(f"❌ File not found: {filepath}")
        sys.exit(1)

    content = path.read_text(encoding="utf-8")
    ext = path.suffix.lower()
    issues = []
    warnings = []
    passes = []

    # ─── ACCESSIBILITY ────────────────────────────────────────────────────────

    # Check for outline: none / outline: 0 without replacement
    if re.search(r'outline\s*:\s*(none|0)', content):
        issues.append("A11Y: outline:none found — removes focus rings. Add a custom :focus-visible replacement.")
    else:
        passes.append("A11Y: No blind outline:none found")

    # Check img tags for alt attributes
    img_tags = re.findall(r'<img[^>]+>', content)
    imgs_without_alt = [t for t in img_tags if 'alt=' not in t]
    if imgs_without_alt:
        issues.append(f"A11Y: {len(imgs_without_alt)} <img> tag(s) missing alt attribute")
    elif img_tags:
        passes.append(f"A11Y: All {len(img_tags)} <img> tags have alt attributes")

    # Icon-only buttons (buttons with no text content and no aria-label)
    button_tags = re.findall(r'<button[^>]*>.*?</button>', content, re.DOTALL)
    for btn in button_tags:
        inner = re.sub(r'<[^>]+>', '', btn).strip()
        has_aria = 'aria-label=' in btn or 'aria-labelledby=' in btn
        if not inner and not has_aria:
            warnings.append("A11Y: Icon-only button found without aria-label — add aria-label='...'")
            break

    # Check for lang attribute on html
    if ext == '.html' and '<html' in content:
        if not re.search(r'<html[^>]+lang=', content):
            issues.append("A11Y: <html> missing lang attribute — add lang='en'")
        else:
            passes.append("A11Y: <html lang> present")

    # Form inputs without labels
    input_tags = re.findall(r'<input[^>]+>', content)
    labeled_inputs = 0
    unlabeled = 0
    for inp in input_tags:
        inp_type = re.search(r'type=["\']([^"\']+)["\']', inp)
        if inp_type and inp_type.group(1) in ('hidden', 'submit', 'button', 'checkbox', 'radio'):
            continue
        inp_id = re.search(r'id=["\']([^"\']+)["\']', inp)
        if inp_id:
            label_for = f'for="{inp_id.group(1)}"'
            if label_for in content:
                labeled_inputs += 1
            else:
                unlabeled += 1
        else:
            unlabeled += 1
    if unlabeled:
        warnings.append(f"A11Y: {unlabeled} input(s) may be missing associated <label> elements")
    elif labeled_inputs:
        passes.append(f"A11Y: {labeled_inputs} inputs have associated labels")

    # ─── PERFORMANCE ─────────────────────────────────────────────────────────

    # Check for passive scroll listeners
    scroll_listeners = re.findall(r"addEventListener\s*\(\s*['\"]scroll['\"]", content)
    if scroll_listeners:
        passive_listeners = re.findall(r"addEventListener\s*\(\s*['\"]scroll['\"][^)]*passive.*?true", content)
        if len(passive_listeners) < len(scroll_listeners):
            warnings.append(f"PERF: {len(scroll_listeners)} scroll listener(s) — add {{passive:true}} for better performance")
        else:
            passes.append("PERF: Scroll listeners use passive:true")

    # Check for will-change overuse
    will_change_count = len(re.findall(r'will-change\s*:', content))
    if will_change_count > 5:
        warnings.append(f"PERF: {will_change_count} will-change declarations found — use sparingly (only on animated elements)")
    elif will_change_count > 0:
        passes.append(f"PERF: will-change used {will_change_count} time(s)")

    # Check for layout-triggering animations
    layout_animations = re.findall(r'(?:gsap\.to|gsap\.from|animate)\s*\([^)]+(?:width|height|margin|padding|top|left|right|bottom)\s*:', content)
    if layout_animations:
        warnings.append(f"PERF: {len(layout_animations)} animation(s) targeting layout properties (width/height/margin). Use transform instead.")

    # Check font-display
    if 'googleapis.com' in content or 'fontshare.com' in content:
        if 'display=swap' not in content and 'font-display' not in content:
            warnings.append("PERF: External fonts loaded without font-display:swap — may block render")
        else:
            passes.append("PERF: font-display:swap present")

    # Check for loading="lazy" on images
    if img_tags:
        lazy_imgs = len([t for t in img_tags if 'loading=' in t and 'lazy' in t])
        no_lazy = len(img_tags) - lazy_imgs
        if no_lazy > 1:
            warnings.append(f"PERF: {no_lazy} image(s) missing loading='lazy' (add to all below-fold images)")
        else:
            passes.append(f"PERF: {lazy_imgs} image(s) using lazy loading")

    # ─── CSS / DESIGN ─────────────────────────────────────────────────────────

    # Hardcoded colors (not CSS variables)
    hardcoded_colors = re.findall(r'(?:color|background(?:-color)?|border(?:-color)?)\s*:\s*#[0-9a-fA-F]{3,6}(?![0-9a-fA-F])', content)
    if len(hardcoded_colors) > 3:
        warnings.append(f"CSS: {len(hardcoded_colors)} hardcoded hex colors found — use CSS variables (--accent, --text, etc.)")

    # Fixed px font sizes for headings
    large_px_fonts = re.findall(r'font-size\s*:\s*([4-9][0-9]|[1-9][0-9]{2})px', content)
    if large_px_fonts:
        warnings.append(f"CSS: {len(large_px_fonts)} large fixed px font-size(s) — use clamp() for fluid type")

    # Check for clamp usage (good)
    if re.search(r'clamp\s*\(', content):
        clamp_count = len(re.findall(r'clamp\s*\(', content))
        passes.append(f"CSS: clamp() used {clamp_count} time(s) for fluid sizing")

    # Check for prefers-reduced-motion
    if re.search(r'prefers-reduced-motion', content):
        passes.append("CSS: prefers-reduced-motion media query present")
    elif re.search(r'animation|transition|gsap|framer', content):
        issues.append("CSS: Animation found but no prefers-reduced-motion media query — add reduced motion support")

    # ─── ANTI-PATTERNS ────────────────────────────────────────────────────────

    # Purple gradient on white (the AI slop classic)
    if re.search(r'(?:purple|#[89ab][0-5][0-9a-f][0-9a-f]|rgba?\(1[3-9][0-9].*?white|linear-gradient.*purple.*white)', content, re.IGNORECASE):
        warnings.append("DESIGN: Possible purple-on-white gradient detected — the most overused AI-generated pattern")

    # Inter as font (overused)
    if re.search(r"['\"]Inter['\"]|family=Inter", content):
        warnings.append("DESIGN: Inter font detected — consider a more distinctive display font (Plus Jakarta Sans, Space Grotesk, etc.)")

    # Emoji as icons
    emoji_in_buttons = re.findall(r'<button[^>]*>[^<]*[\U0001F300-\U0001FFFF][^<]*</button>', content)
    if emoji_in_buttons:
        warnings.append("DESIGN: Emoji used as button icons — use SVG icons (Lucide, Heroicons) instead")

    # ─── PRINT REPORT ────────────────────────────────────────────────────────

    print(f"\n{'='*60}")
    print(f"ultra-frontend Audit: {filepath}")
    print(f"{'='*60}")

    if issues:
        print(f"\n🔴 ISSUES ({len(issues)}) — fix before shipping:")
        for i in issues:
            print(f"  ✗ {i}")

    if warnings:
        print(f"\n🟡 WARNINGS ({len(warnings)}) — strongly recommended:")
        for w in warnings:
            print(f"  ⚠ {w}")

    if passes:
        print(f"\n🟢 PASSING ({len(passes)}):")
        for p in passes:
            print(f"  ✓ {p}")

    total = len(issues) + len(warnings)
    print(f"\n{'='*60}")
    if not issues and not warnings:
        print("✅ All checks passed! Ready to ship.")
    elif not issues:
        print(f"✅ No critical issues. {len(warnings)} warning(s) to review.")
    else:
        print(f"❌ {len(issues)} critical issue(s) + {len(warnings)} warning(s). Fix issues before shipping.")
    print(f"{'='*60}\n")

    return len(issues)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/audit.py <file.html|file.jsx>")
        sys.exit(1)
    exit_code = audit(sys.argv[1])
    sys.exit(1 if exit_code > 0 else 0)
