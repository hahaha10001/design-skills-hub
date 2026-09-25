#!/usr/bin/env python3
"""
ultra-frontend design system generator
Usage: python3 scripts/design-system.py "<keywords>" [--stack react|html|next|vue]
Example: python3 scripts/design-system.py "fintech dark premium SaaS"
         python3 scripts/design-system.py "wellness meditation soft pastel" --stack react
"""

import sys
import re
import argparse

AESTHETIC_MAP = {
    # Futurist Dark triggers
    "fintech": "futurist-dark", "ai": "futurist-dark", "startup": "futurist-dark",
    "futuristic": "futurist-dark", "neon": "futurist-dark", "dark": "futurist-dark",
    "tech": "futurist-dark", "saas": "futurist-dark", "developer": "futurist-dark",

    # Brutalist Editorial
    "editorial": "brutalist-editorial", "bold": "brutalist-editorial",
    "agency": "brutalist-editorial", "brutalist": "brutalist-editorial",
    "portfolio": "brutalist-editorial", "architecture": "brutalist-editorial",
    "magazine": "brutalist-editorial", "newspaper": "brutalist-editorial",

    # Cinematic Luxury
    "luxury": "cinematic-luxury", "premium": "cinematic-luxury",
    "exclusive": "cinematic-luxury", "fashion": "cinematic-luxury",
    "cinematic": "cinematic-luxury", "gold": "cinematic-luxury",
    "invite": "cinematic-luxury", "high-end": "cinematic-luxury",

    # Technical Blueprint
    "technical": "technical-blueprint", "infrastructure": "technical-blueprint",
    "blueprint": "technical-blueprint", "b2b": "technical-blueprint",
    "enterprise": "technical-blueprint", "data": "technical-blueprint",
    "dashboard": "technical-blueprint", "analytics": "technical-blueprint",

    # Glassmorphic SaaS
    "glassmorphism": "glassmorphic-saas", "glass": "glassmorphic-saas",
    "blur": "glassmorphic-saas", "translucent": "glassmorphic-saas",

    # Soft Gen-Z
    "wellness": "soft-genz", "meditation": "soft-genz", "soft": "soft-genz",
    "pastel": "soft-genz", "lifestyle": "soft-genz", "journal": "soft-genz",
    "calm": "soft-genz", "organic": "soft-genz",

    # DevTools Chrome
    "devtools": "devtools-chrome", "extension": "devtools-chrome",
    "system": "devtools-chrome", "utility": "devtools-chrome",
    "terminal": "devtools-chrome", "cli": "devtools-chrome",

    # Maximalist Chaos
    "maximalist": "maximalist-chaos", "wild": "maximalist-chaos",
    "creative": "maximalist-chaos", "experimental": "maximalist-chaos",
    "art": "maximalist-chaos", "chaos": "maximalist-chaos",

    # Refined Minimal
    "minimal": "refined-minimal", "minimal": "refined-minimal",
    "clean": "refined-minimal", "refined": "refined-minimal",
    "simple": "refined-minimal", "elegant": "refined-minimal",

    # Retro-Futuristic
    "retro": "retro-futuristic", "gaming": "retro-futuristic",
    "music": "retro-futuristic", "nostalgia": "retro-futuristic",
    "80s": "retro-futuristic", "90s": "retro-futuristic", "vhs": "retro-futuristic",
}

AESTHETICS = {
    "futurist-dark": {
        "name": "Futurist Dark",
        "css_vars": """  --bg: #0a0a0f;
  --surface: #12121a;
  --surface-2: #1a1a26;
  --border: rgba(255,255,255,0.08);
  --border-hover: rgba(255,255,255,0.15);
  --accent: #39ff14;
  --accent-2: #7b2fff;
  --accent-glow: rgba(57,255,20,0.25);
  --text: #e8e8f0;
  --text-muted: #6b6b80;
  --font-display: 'Plus Jakarta Sans', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --radius: 8px;
  --radius-lg: 16px;""",
        "font_link": "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap",
        "signature": "Bento grid, glassmorphism cards (backdrop-filter: blur(12px)), neon glow on hover, SplitText reveals",
    },
    "brutalist-editorial": {
        "name": "Brutalist Editorial",
        "css_vars": """  --bg: #f5f0e8;
  --surface: #ffffff;
  --surface-2: #ede8df;
  --border: #1a1a2e;
  --accent: #e63946;
  --text: #1a1a2e;
  --text-muted: #555;
  --font-display: 'Bebas Neue', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --radius: 0px;
  --leading-display: 0.85;""",
        "font_link": "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;600&display=swap",
        "signature": "Type at line-height: 0.85, 1px dividers, uppercase labels, diagonal clip-paths",
    },
    "cinematic-luxury": {
        "name": "Cinematic Luxury",
        "css_vars": """  --bg: #181818;
  --surface: #222;
  --surface-2: #1e1e1e;
  --border: rgba(201,168,76,0.2);
  --accent: #c9a84c;
  --accent-2: #EBDCC4;
  --text: #EBDCC4;
  --text-muted: #8a7d6a;
  --font-display: 'Playfair Display', serif;
  --font-body: 'Cormorant Garamond', serif;
  --radius: 2px;
  --radius-lg: 4px;""",
        "font_link": "https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&display=swap",
        "signature": "Grain SVG overlay (4% opacity), gold hairline rules, slow 1.2s fade-ins, full-bleed imagery",
    },
    "technical-blueprint": {
        "name": "Technical Blueprint",
        "css_vars": """  --bg: #F7F7F5;
  --surface: #EEECEA;
  --surface-dark: #1A3C2B;
  --border: #d0cdc8;
  --accent: #1A3C2B;
  --text: #1a1a1a;
  --text-muted: #666;
  --font-display: 'Space Grotesk', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --radius: 0px;""",
        "font_link": "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=DM+Sans:wght@400;500&family=JetBrains+Mono:wght@400;500&display=swap",
        "signature": "Monospace labels everywhere, flat 2D bento grid, 1px borders, data-dense layout",
    },
    "glassmorphic-saas": {
        "name": "Glassmorphic SaaS",
        "css_vars": """  --bg: #0f0f17;
  --surface: rgba(255,255,255,0.06);
  --surface-2: rgba(255,255,255,0.04);
  --glass-border: rgba(255,255,255,0.12);
  --glass-border-hover: rgba(255,255,255,0.2);
  --accent: #6366f1;
  --accent-2: #a78bfa;
  --glow: rgba(99,102,241,0.35);
  --text: #f0f0f8;
  --text-muted: #7b7b9a;
  --font-display: 'Cormorant Garamond', serif;
  --font-body: 'DM Sans', sans-serif;
  --radius: 16px;
  --radius-lg: 24px;""",
        "font_link": "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;500;600&display=swap",
        "signature": "backdrop-filter: blur(20px) on cards, indigo glow halos, serif+sans contrast",
    },
    "soft-genz": {
        "name": "Soft Gen-Z",
        "css_vars": """  --bg: #FDFCF8;
  --surface: #F5F0E8;
  --surface-2: #EDE8DC;
  --accent: #FFB7B2;
  --accent-2: #E8EFE8;
  --accent-3: #EFEDF4;
  --text: #2d2a26;
  --text-muted: #8a8070;
  --font-display: 'Playfair Display', serif;
  --font-body: 'Figtree', sans-serif;
  --radius: 20px;
  --radius-lg: 32px;""",
        "font_link": "https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Figtree:wght@400;500;600&display=swap",
        "signature": "Grain overlay (3%), organic blob shapes, slow scroll reveals, pastel conic-gradient backgrounds",
    },
    "devtools-chrome": {
        "name": "DevTools Chrome",
        "css_vars": """  --bg: #f8f9fa;
  --surface: #ffffff;
  --surface-2: #f1f3f4;
  --border: #dadce0;
  --accent: #06B6D4;
  --accent-2: #0ea5e9;
  --text: #202124;
  --text-muted: #5f6368;
  --font-display: 'DM Sans', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --radius: 4px;
  --radius-lg: 8px;""",
        "font_link": "https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap",
        "signature": "Monospace for ALL data, Chrome DevTools panel layout, high density, cyan accents",
    },
    "maximalist-chaos": {
        "name": "Maximalist Chaos",
        "css_vars": """  --bg: #0d0d0d;
  --surface: #1a1a1a;
  --accent: #ff2d55;
  --accent-2: #00ff88;
  --accent-3: #ffdc00;
  --text: #ffffff;
  --text-muted: #aaa;
  --font-display: 'Bebas Neue', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --radius: 0px;""",
        "font_link": "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500&display=swap",
        "signature": "Overlapping absolute elements, mixed font sizes 12px–200px, mix-blend-mode: difference",
    },
    "refined-minimal": {
        "name": "Refined Minimal",
        "css_vars": """  --bg: #fafafa;
  --surface: #ffffff;
  --surface-2: #f4f4f4;
  --border: #e5e5e5;
  --accent: #111;
  --text: #111;
  --text-muted: #777;
  --text-subtle: #bbb;
  --font-display: 'Cormorant Garamond', serif;
  --font-body: 'Figtree', sans-serif;
  --radius: 2px;
  --radius-lg: 4px;""",
        "font_link": "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Figtree:wght@400;500;600&display=swap",
        "signature": "Exquisite whitespace, hairline 0.5px rules, single accent used sparingly, micro hover: max 4px",
    },
    "retro-futuristic": {
        "name": "Retro-Futuristic",
        "css_vars": """  --bg: #0a0a1a;
  --surface: #111128;
  --crt-green: #00ff41;
  --accent: #ff6b35;
  --accent-2: #ffe66d;
  --text: #e8e8e8;
  --text-muted: #666;
  --font-display: 'Orbitron', sans-serif;
  --font-body: 'Space Grotesk', sans-serif;
  --font-mono: 'Share Tech Mono', monospace;
  --radius: 0px;""",
        "font_link": "https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Space+Grotesk:wght@400;500;600&family=Share+Tech+Mono&display=swap",
        "signature": "CRT scanlines (repeating-linear-gradient), phosphor glow (text-shadow: 0 0 8px), glitch via clip-path",
    },
}

def detect_aesthetic(keywords):
    keywords_lower = keywords.lower()
    scores = {}
    for word in keywords_lower.split():
        word = re.sub(r'[^a-z0-9-]', '', word)
        if word in AESTHETIC_MAP:
            aesthetic = AESTHETIC_MAP[word]
            scores[aesthetic] = scores.get(aesthetic, 0) + 1
    if scores:
        return max(scores, key=scores.get)
    return "futurist-dark"  # default

def generate_design_system(keywords, stack="html"):
    aesthetic_key = detect_aesthetic(keywords)
    aesthetic = AESTHETICS[aesthetic_key]

    print(f"\n{'='*60}")
    print(f"ultra-frontend Design System")
    print(f"{'='*60}")
    print(f"Keywords:  {keywords}")
    print(f"Aesthetic: {aesthetic['name']}")
    print(f"Stack:     {stack}")
    print(f"{'='*60}\n")

    print("## CSS Design Tokens\n")
    print("```css")
    print(":root {")
    print(aesthetic['css_vars'])
    print("}")
    print("```\n")

    print("## Font Loading\n")
    print("```html")
    print('<link rel="preconnect" href="https://fonts.googleapis.com">')
    print('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    print(f'<link href="{aesthetic["font_link"]}" rel="stylesheet">')
    print("```\n")

    print(f"## Signature Effects\n{aesthetic['signature']}\n")

    print("## GSAP Plugins for this Aesthetic\n")
    plugin_map = {
        "futurist-dark": ["ScrollTrigger", "SplitText", "ScrollSmoother", "CustomEase", "ScrambleText"],
        "brutalist-editorial": ["ScrollTrigger", "SplitText", "DrawSVGPlugin", "CustomEase"],
        "cinematic-luxury": ["ScrollTrigger", "ScrollSmoother", "SplitText", "CustomEase"],
        "technical-blueprint": ["ScrollTrigger", "Flip", "DrawSVGPlugin"],
        "glassmorphic-saas": ["ScrollTrigger", "ScrollSmoother", "SplitText", "MorphSVGPlugin"],
        "soft-genz": ["ScrollTrigger", "CustomEase"],
        "devtools-chrome": ["ScrollTrigger", "Flip"],
        "maximalist-chaos": ["ScrollTrigger", "SplitText", "Physics2DPlugin", "ScrambleText"],
        "refined-minimal": ["ScrollTrigger", "CustomEase"],
        "retro-futuristic": ["ScrollTrigger", "SplitText", "ScrambleText", "CustomEase"],
    }
    plugins = plugin_map.get(aesthetic_key, ["ScrollTrigger"])
    for p in plugins:
        print(f"  - {p}: cdn.jsdelivr.net/npm/gsap@3.14/dist/{p}.min.js")

    print("\n## Recommended Stack Setup\n")
    if stack == "react":
        print("```bash")
        print("npm install framer-motion gsap @gsap/react lucide-react")
        print("npx shadcn@latest init")
        print("```")
    elif stack == "next":
        print("```bash")
        print("npm install framer-motion gsap @gsap/react lucide-react")
        print("npx shadcn@latest init")
        print("```")
    elif stack == "vue":
        print("```bash")
        print("npm install @vueuse/motion gsap")
        print("```")
    else:
        print("HTML/CSS/JS — use CDN links above. No build step needed.")

    print("\n## Reference Files to Read\n")
    print("  - references/aesthetics.md      → full token set + all archetypes")
    print("  - references/gsap.md            → plugin cookbook")
    print("  - references/components.md      → React + framer-motion patterns")
    print("  - references/uiux-rules.md      → UX + accessibility rules")
    print("  - references/component-library.md → 21st.dev components")
    print(f"\n{'='*60}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate design system from keywords")
    parser.add_argument("keywords", nargs="?", default="dark modern SaaS",
                        help='Keywords like "fintech dark premium" or "wellness soft pastel"')
    parser.add_argument("--stack", default="html",
                        choices=["html", "react", "next", "vue", "svelte"],
                        help="Target stack")
    args = parser.parse_args()
    generate_design_system(args.keywords, args.stack)
