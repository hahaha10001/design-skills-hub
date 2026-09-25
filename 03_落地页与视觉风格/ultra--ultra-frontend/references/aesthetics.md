# Aesthetics Reference

Ten design archetypes with complete CSS token sets and font loading. Paste the chosen block into your `:root {}`.

---

## Futurist Dark

*AI tools, fintech, dev platforms, anything "futuristic"*

```css
:root {
  --bg: #0a0a0f;          --surface: #12121a;       --surface-2: #1a1a26;
  --border: rgba(255,255,255,0.08);                  --border-hover: rgba(255,255,255,0.15);
  --accent: #39ff14;      --accent-2: #7b2fff;       --accent-glow: rgba(57,255,20,0.25);
  --text: #e8e8f0;        --text-muted: #6b6b80;     --text-subtle: #3a3a4a;
  --font-display: 'Plus Jakarta Sans', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --radius: 8px;          --radius-lg: 16px;
}
```

```html
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

**Signature effects**: bento grid, glassmorphism cards (`backdrop-filter: blur(12px)`), neon glow on hover, fluid oversized type

---

## Brutalist Editorial

*Agencies, portfolios, "editorial", "bold", architecture firms*

```css
:root {
  --bg: #f5f0e8;          --surface: #ffffff;        --surface-2: #ede8df;
  --border: #1a1a2e;      --accent: #e63946;         --accent-2: #1a1a2e;
  --text: #1a1a2e;        --text-muted: #555;
  --font-display: 'Bebas Neue', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --font-mono: 'Courier New', monospace;
  --radius: 0px;          --leading-display: 0.85;   --tracking-display: -0.02em;
}
```

```html
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<!-- For Monument Extended (stronger headline): load from fontshare instead -->
<!-- <link href="https://api.fontshare.com/v2/css?f[]=clash-display@600,700&display=swap" rel="stylesheet"> -->
```

**Signature effects**: type at `line-height: 0.85`, 1px dividers, uppercase labels, diagonal `clip-path` section cuts, negative margin bleeds

---

## Cinematic Luxury

*Luxury tech, invite-only products, fashion, premium brands*

```css
:root {
  --bg: #181818;          --surface: #222;           --surface-2: #1e1e1e;
  --border: rgba(201,168,76,0.2);                    --accent: #c9a84c;
  --accent-2: #EBDCC4;   --text: #EBDCC4;           --text-muted: #8a7d6a;
  --text-subtle: #4a4035;
  --font-display: 'Playfair Display', serif;
  --font-body: 'Cormorant Garamond', serif;
  --font-sans: 'DM Sans', sans-serif;
  --radius: 2px;          --radius-lg: 4px;
}
```

```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
```

**Signature effects**: grain SVG overlay at 4% opacity, gold hairline rules, slow 1.2s fade-ins, full-bleed editorial images, `letter-spacing: 0.15em` on small caps labels

---

## Technical Blueprint

*B2B SaaS, infrastructure, developer tools, "technical"*

```css
:root {
  --bg: #F7F7F5;          --surface: #EEECEA;        --surface-dark: #1A3C2B;
  --border: #d0cdc8;      --accent: #1A3C2B;         --accent-text: #F7F7F5;
  --text: #1a1a1a;        --text-muted: #666;
  --font-display: 'Space Grotesk', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --radius: 0px;          --radius-lg: 2px;
}
```

```html
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=DM+Sans:wght@400;500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

**Signature effects**: monospace for all data labels, flat 2D bento grid, 1px borders everywhere, data-dense layout with breathing room only in headers

---

## Glassmorphic SaaS

*AI startups, design tools, premium dark SaaS platforms*

```css
:root {
  --bg: #0f0f17;
  --surface: rgba(255,255,255,0.06);                 --surface-2: rgba(255,255,255,0.04);
  --glass-border: rgba(255,255,255,0.12);            --glass-border-hover: rgba(255,255,255,0.2);
  --accent: #6366f1;      --accent-2: #a78bfa;       --glow: rgba(99,102,241,0.35);
  --text: #f0f0f8;        --text-muted: #7b7b9a;
  --font-display: 'Cormorant Garamond', serif;
  --font-body: 'DM Sans', sans-serif;
  --radius: 16px;         --radius-lg: 24px;
}
```

```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
```

**Signature effects**: `backdrop-filter: blur(20px)` on cards, indigo gradient glow halos behind feature sections, serif headline contrasting with clean sans body, subtle `box-shadow: 0 0 60px var(--glow)` bloom

---

## Soft Gen-Z

*Wellness, meditation, journaling, lifestyle, "soft"*

```css
:root {
  --bg: #FDFCF8;          --surface: #F5F0E8;        --surface-2: #EDE8DC;
  --accent: #FFB7B2;      --accent-2: #E8EFE8;       --accent-3: #EFEDF4;
  --text: #2d2a26;        --text-muted: #8a8070;
  --font-display: 'Playfair Display', serif;
  --font-body: 'Figtree', sans-serif;
  --radius: 20px;         --radius-lg: 32px;
}
```

```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Figtree:wght@400;500;600&display=swap" rel="stylesheet">
```

**Signature effects**: grain overlay at 3%, floating organic blob shapes via `border-radius: 60% 40% 70% 30%`, soft scroll reveals (long `duration: 1.2`, low `y: 20`), pastel `conic-gradient` backgrounds

---

## DevTools Chrome

*Browser extensions, developer platforms, utilities, "system"*

```css
:root {
  --bg: #f8f9fa;          --surface: #ffffff;        --surface-2: #f1f3f4;
  --border: #dadce0;      --accent: #06B6D4;         --accent-2: #0ea5e9;
  --text: #202124;        --text-muted: #5f6368;
  --font-display: 'DM Sans', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --radius: 4px;          --radius-lg: 8px;
}
```

```html
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

**Signature effects**: monospace for ALL data/numbers, Chrome DevTools panel layout, high density with 8px grid, cyan accent on interactive elements only

---

## Maximalist Chaos

*Creative agencies, art projects, "wild", experimental*

```css
:root {
  --bg: #0d0d0d;          --surface: #1a1a1a;
  --accent: #ff2d55;      --accent-2: #00ff88;       --accent-3: #ffdc00;
  --text: #ffffff;        --text-muted: #aaa;
  --font-display: 'Bebas Neue', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --radius: 0px;
}
```

```html
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
```

**Signature effects**: overlapping absolutely-positioned elements, mixed `font-size` from 12px to 200px, `mix-blend-mode: difference`, collision layouts, cursor trails

---

## Refined Minimal

*Luxury brands, high-end portfolios, "refined", "minimal"*

```css
:root {
  --bg: #fafafa;          --surface: #ffffff;        --surface-2: #f4f4f4;
  --border: #e5e5e5;      --accent: #111;            --accent-2: #666;
  --text: #111;           --text-muted: #777;        --text-subtle: #bbb;
  --font-display: 'Cormorant Garamond', serif;
  --font-body: 'Figtree', sans-serif;
  --radius: 2px;          --radius-lg: 4px;
}
```

```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Figtree:wght@400;500;600&display=swap" rel="stylesheet">
```

**Signature effects**: generous whitespace, hairline `0.5px` rules, single color accent used sparingly, hover animations that move `≤4px`, micro-interactions that feel inevitable not surprising

---

## Retro-Futuristic

*Music, gaming, nostalgia, "retro", 80s/90s*

```css
:root {
  --bg: #0a0a1a;          --surface: #111128;        --crt-green: #00ff41;
  --accent: #ff6b35;      --accent-2: #ffe66d;
  --text: #e8e8e8;        --text-muted: #666;
  --font-display: 'Orbitron', sans-serif;
  --font-body: 'Space Grotesk', sans-serif;
  --font-mono: 'Share Tech Mono', monospace;
  --radius: 0px;          --radius-lg: 2px;
}
```

```html
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Space+Grotesk:wght@400;500;600&family=Share+Tech+Mono&display=swap" rel="stylesheet">
```

**Signature effects**: CRT scanlines via `repeating-linear-gradient(transparent, transparent 2px, rgba(0,0,0,0.15) 2px, rgba(0,0,0,0.15) 4px)`, phosphor glow via `text-shadow: 0 0 8px var(--crt-green)`, glitch via `clip-path` keyframe jumps

---

## Fontshare — Premium Free Fonts (NOT on Google Fonts)

When you want more distinctive typography, use these instead:

```html
<!-- Satoshi — geometric modernist, great all-rounder -->
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&display=swap" rel="stylesheet">

<!-- Cabinet Grotesk — editorial grotesque with personality -->
<link href="https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@400,500,700,800&display=swap" rel="stylesheet">

<!-- Clash Display — striking, opinionated, great for big headlines -->
<link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&display=swap" rel="stylesheet">

<!-- General Sans — clean, versatile workhorse -->
<link href="https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600&display=swap" rel="stylesheet">
```

**NEVER use as primary display font**: Inter, Roboto, Arial, system-ui. They signal zero creative effort.

---

## Glassmorphism Card (CSS)

```css
.glass {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: var(--radius-lg);
}
.glass:hover { border-color: rgba(255,255,255,0.2); }
```
