---
name: ultra-frontend
description: |
  Master frontend skill for Claude Code. Synthesizes ultra-frontend design system, uiuxpromax design intelligence, superdesign.dev aesthetics, framer-motion + GSAP full plugin ecosystem, 21st.dev component patterns, Three.js 3D, shadcn/ui, and production-grade architecture. Invoke for ANY visual web task: landing pages, portfolios, dashboards, SaaS apps, React components, interactive experiences, scroll animations, 3D scenes, design systems, component libraries, "make it look sick", "world-class UI", or any frontend build across HTML, React, Next.js, Vue, Svelte, or mobile stacks.
---

# ultra-frontend — Claude Code Edition

The definitive frontend skill. Synthesizes what would take 6 separate skills to cover:
- **ultra-frontend** — design system, animations, GSAP, Three.js
- **uiuxpromax** — 50+ styles, UX rules, accessibility, chart types, multi-stack
- **superdesign.dev** — aesthetic archetypes, design tokens, signature effects
- **frontend-design** — anti-slop philosophy, bold direction, typography
- **framer-motion** — full React animation cookbook
- **21st.dev patterns** — shadcn/ui component library patterns

**Reference files** (Claude Code reads these on demand):
- `references/aesthetics.md` — 10 archetypes, CSS tokens, font loading, superdesign.dev system
- `references/gsap.md` — full GSAP plugin cookbook (SplitText, Flip, ScrollSmoother, DrawSVG, MorphSVG, Observer, ScrambleText, CustomEase, matchMedia)
- `references/components.md` — React/JSX boilerplate, framer-motion patterns, Three.js, 21st.dev components
- `references/uiux-rules.md` — uiuxpromax: 10-priority UX rules, accessibility, multi-stack guidelines
- `references/component-library.md` — 21st.dev deep library: dock, command menu, spotlight, marquee, timeline, accordion

**Scripts** (executable — run via bash):
- `scripts/scaffold.sh <name> <stack>` — scaffold a new project (html/react/next/vue)
- `scripts/design-system.py <keywords>` — generate a complete design system from keywords
- `scripts/audit.py <file>` — audit HTML/JSX for UX, a11y, and performance issues

---

## STEP 0 — Before writing any code

1. **Read context → choose aesthetic** (table below, full tokens in `references/aesthetics.md`)
2. **Choose stack** (html / react / next / vue / svelte)
3. **Run scaffold** if starting a new project: `bash scripts/scaffold.sh <project-name> <stack>`
4. **Generate design system** if complex: `python3 scripts/design-system.py "<keywords>"`
5. **Pick the signature moment** (Section 5) — the one thing people will remember

---

## 1. Aesthetic → Context Mapping

| Context | Aesthetic |
|---|---|
| AI tool, fintech, dev tool, startup, "futuristic" | **Futurist Dark** |
| Agency, portfolio, "editorial", "bold", architecture | **Brutalist Editorial** |
| Luxury, invite-only, fashion, premium | **Cinematic Luxury** |
| B2B SaaS, infrastructure, "technical" | **Technical Blueprint** |
| AI startup, premium SaaS, "glassmorphism" | **Glassmorphic SaaS** |
| Wellness, lifestyle, "soft", journal | **Soft Gen-Z** |
| Developer tool, extension, "system" | **DevTools Chrome** |
| Creative agency, art, "wild" | **Maximalist Chaos** |
| Luxury brand, minimal portfolio | **Refined Minimal** |
| Music, gaming, "retro", 80s/90s | **Retro-Futuristic** |

**Default when uncertain**: Futurist Dark.

Read `references/aesthetics.md` for full CSS token sets, Google Fonts + Fontshare links, and signature effects per archetype.

---

## 2. Stack Selection

```
HTML artifact (Claude Code / claude.ai)  → GSAP + vanilla JS + Three.js
React / JSX artifact                      → framer-motion + shadcn/ui + recharts
Next.js project                           → framer-motion + GSAP + shadcn/ui + next/image
Vue / Nuxt                                → vue-motion + GSAP + VueUse
Svelte / SvelteKit                        → svelte-motion + GSAP
Mobile (React Native)                     → react-native-reanimated
Mobile (Flutter)                          → Flutter animations + custom painters
Mobile (SwiftUI)                          → SwiftUI animations + Lottie
```

---

## 3. Canonical CDN URLs (HTML builds)

```html
<!-- GSAP — jsDelivr ONLY (cdnjs missing all bonus plugins) -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/ScrollTrigger.min.js"></script>
<!-- Bonus plugins (load only what you use): -->
<!-- SplitText:      cdn.jsdelivr.net/npm/gsap@3.14/dist/SplitText.min.js         -->
<!-- ScrollSmoother: cdn.jsdelivr.net/npm/gsap@3.14/dist/ScrollSmoother.min.js    -->
<!-- Flip:           cdn.jsdelivr.net/npm/gsap@3.14/dist/Flip.min.js              -->
<!-- DrawSVGPlugin:  cdn.jsdelivr.net/npm/gsap@3.14/dist/DrawSVGPlugin.min.js     -->
<!-- MorphSVGPlugin: cdn.jsdelivr.net/npm/gsap@3.14/dist/MorphSVGPlugin.min.js    -->
<!-- CustomEase:     cdn.jsdelivr.net/npm/gsap@3.14/dist/CustomEase.min.js        -->
<!-- Observer:       cdn.jsdelivr.net/npm/gsap@3.14/dist/Observer.min.js          -->
<!-- ScrollToPlugin: cdn.jsdelivr.net/npm/gsap@3.14/dist/ScrollToPlugin.min.js    -->
<!-- ScrambleText:   cdn.jsdelivr.net/npm/gsap@3.14/dist/ScrambleTextPlugin.min.js -->

<!-- Three.js r128 (cdnjs — no OrbitControls on CDN) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<!-- p5.js (generative art / particles) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js"></script>

<!-- Lenis smooth scroll -->
<script src="https://unpkg.com/lenis@1.1.14/dist/lenis.min.js"></script>
```

> All GSAP plugins are 100% free as of 2025 (Webflow deal). Never load from cdnjs for plugins.

---

## 4. HTML Boilerplate (copy-paste and go)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Site Title</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/ScrollTrigger.min.js"></script>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --bg: #0a0a0f;     --surface: #12121a;   --surface-2: #1a1a26;
      --border: rgba(255,255,255,0.08);
      --accent: #39ff14; --accent-2: #7b2fff;
      --text: #e8e8f0;   --text-muted: #6b6b80;
      --font: 'Plus Jakarta Sans', sans-serif;
      --mono: 'JetBrains Mono', monospace;
      --radius: 8px;     --radius-lg: 16px;
    }
    body { background:var(--bg); color:var(--text); font-family:var(--font); line-height:1.6; overflow-x:hidden; }
    h1 { font-size:clamp(2.5rem,8vw,7rem); line-height:.9; letter-spacing:-.02em; }
    h2 { font-size:clamp(1.75rem,5vw,3.5rem); line-height:1.05; }
    .container { max-width:min(1200px,90vw); margin-inline:auto; }
    .section   { padding-block:clamp(4rem,10vw,10rem); }
    @media (prefers-reduced-motion:reduce) { *,*::before,*::after { animation-duration:.01ms!important; transition-duration:.01ms!important; } }
  </style>
</head>
<body>
<!-- GRAIN OVERLAY -->
<svg style="position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:9997;opacity:0.04" xmlns="http://www.w3.org/2000/svg">
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
  <rect width="100%" height="100%" filter="url(#grain)"/>
</svg>
<!-- CONTENT -->
<script>
gsap.registerPlugin(ScrollTrigger);
gsap.utils.toArray('.reveal').forEach(el => gsap.from(el, { scrollTrigger:{trigger:el,start:'top 88%'}, y:40, opacity:0, duration:.75, ease:'power3.out' }));
gsap.utils.toArray('.stagger').forEach(p => gsap.from(p.children, { scrollTrigger:{trigger:p,start:'top 85%'}, y:30, opacity:0, duration:.6, stagger:.1, ease:'power3.out' }));
</script>
</body>
</html>
```

---

## 5. The Signature Moment

**Pick ONE. Make it extraordinary. Everything else can be clean.**

| Effect | Where to find it |
|---|---|
| Word-by-word headline reveal | `references/gsap.md` → SplitText |
| 3D object rotating with cursor | `references/components.md` → Three.js |
| Cards unstack on scroll | `references/gsap.md` → pin + scrub |
| Spring-lag cursor trail | Section 4 patterns below |
| Text scrambles to reveal | `references/gsap.md` → ScrambleText |
| SVG path draws in | `references/gsap.md` → DrawSVG |
| Icon morphs on click | `references/gsap.md` → MorphSVG |
| Chars explode off screen | `references/gsap.md` → SplitText + Physics2D |
| Filter grid animates | `references/gsap.md` → Flip |
| Particle field reacts to mouse | `references/components.md` → p5.js |
| Horizontal scroll narrative | `references/gsap.md` → horizontal scroll |
| Dock magnification (macOS) | `references/component-library.md` → Dock |
| Command palette (Cmd+K) | `references/component-library.md` → CommandMenu |
| Animated counters | `references/components.md` → Counter |
| Magnetic button | patterns below |

---

## 6. Core Patterns

### Magnetic Button
```javascript
document.querySelectorAll('.mag-btn').forEach(btn => {
  btn.addEventListener('mousemove', e => {
    const r = btn.getBoundingClientRect();
    gsap.to(btn, { x:(e.clientX-r.left-r.width/2)*.35, y:(e.clientY-r.top-r.height/2)*.35, duration:.4, ease:'power3.out' });
  });
  btn.addEventListener('mouseleave', () => gsap.to(btn, { x:0, y:0, duration:.7, ease:'elastic.out(1,.5)' }));
});
```

### Custom Cursor
```html
<div id="cur" style="position:fixed;width:10px;height:10px;background:var(--accent);border-radius:50%;pointer-events:none;z-index:9999;transform:translate(-50%,-50%);mix-blend-mode:difference"></div>
<div id="ring" style="position:fixed;width:36px;height:36px;border:1px solid var(--accent);border-radius:50%;pointer-events:none;z-index:9998;transform:translate(-50%,-50%);opacity:.5"></div>
<script>
let mx=0,my=0,rx=0,ry=0;
const cur=document.getElementById('cur'),ring=document.getElementById('ring');
document.addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY;});
(function l(){gsap.set(cur,{x:mx,y:my});rx+=(mx-rx)*.12;ry+=(my-ry)*.12;gsap.set(ring,{x:rx,y:ry});requestAnimationFrame(l);})();
document.querySelectorAll('a,button').forEach(el=>{
  el.addEventListener('mouseenter',()=>gsap.to(cur,{scale:3,duration:.3}));
  el.addEventListener('mouseleave',()=>gsap.to(cur,{scale:1,duration:.3}));
});
</script>
```

### Sticky Nav
```javascript
let lastY=0;
window.addEventListener('scroll',()=>{
  const nav=document.querySelector('nav'),y=window.scrollY;
  nav.style.transform=y>lastY&&y>200?'translateY(-100%)':'translateY(0)';
  nav.style.background=y>80?'rgba(10,10,15,.9)':'transparent';
  nav.style.backdropFilter=y>80?'blur(20px)':'none';
  lastY=y;
},{passive:true});
```

### gsap.matchMedia() — Responsive + Reduced Motion
```javascript
gsap.matchMedia().add({
  isDesktop:'(min-width:768px)',
  reduceMotion:'(prefers-reduced-motion:reduce)'
},({conditions:{isDesktop,reduceMotion}})=>{
  if(reduceMotion) return;
  gsap.from('.hero',{y:60,opacity:0,duration:1,ease:'power3.out'});
  if(isDesktop) ScrollTrigger.create({trigger:'.features',pin:true,end:'+=1000',scrub:1});
});
```

---

## 7. UX Rules (Priority Order)

Full rules with anti-patterns in `references/uiux-rules.md`. Quick reference:

| Priority | Rule | Must Have | Never |
|---|---|---|---|
| 1 | Accessibility | 4.5:1 contrast, keyboard nav, aria | No focus rings |
| 2 | Touch targets | 44×44px min, 8px spacing | Hover-only interactions |
| 3 | Performance | WebP/AVIF, lazy load, CLS <0.1 | Layout thrashing |
| 4 | Style | Match product type, consistent | Emoji as icons |
| 5 | Layout | Mobile-first, no horizontal scroll | Fixed px widths |
| 6 | Typography | 16px base, 1.5 line-height | <12px body text |
| 7 | Animation | 150–300ms, conveys meaning | Width/height animation |
| 8 | Forms | Visible labels, inline errors | Placeholder-only labels |

---

## 8. Modern CSS (Use These — AI Usually Doesn't)

```css
/* Scroll-driven animations — zero JS */
.fade-in { animation:fade-up linear both; animation-timeline:view(); animation-range:entry 0% entry 35%; }
@keyframes fade-up { from{opacity:0;transform:translateY(40px)} to{opacity:1;transform:translateY(0)} }

/* Container queries */
.wrap { container-type:inline-size; }
@container (min-width:400px) { .card { flex-direction:row; } }

/* :has() — parent styling without JS */
.card:has(img) { padding-top:0; }
body:has(#menu:checked) .nav-links { display:flex; }

/* Fluid everything */
h1 { font-size:clamp(2.5rem,8vw,7rem); }
.section { padding-block:clamp(4rem,10vw,10rem); }
.container { max-width:min(1200px,90vw); margin-inline:auto; }

/* Bento grid */
.bento { display:grid; grid-template-columns:repeat(12,1fr); grid-auto-rows:minmax(80px,auto); gap:12px; }
.cell-hero { grid-column:span 8; grid-row:span 4; }
.cell-tall { grid-column:span 4; grid-row:span 6; }
@media(max-width:768px){.bento>*{grid-column:1/-1!important;}}

/* Popover API — native modal */
/* <button popovertarget="m">Open</button><div id="m" popover>...</div> */

/* View Transitions */
/* document.startViewTransition(()=>render()) */
/* ::view-transition-old(root){animation:slide-out .3s} */
```

---

## 9. Component Patterns

### Gradient Border Card
```css
.glow-card{position:relative;border-radius:var(--radius-lg);padding:1px;}
.glow-card::before{content:'';position:absolute;inset:0;border-radius:inherit;background:linear-gradient(135deg,var(--accent),transparent 50%,var(--accent-2));opacity:0;transition:opacity .3s;}
.glow-card:hover::before{opacity:1;}
.glow-card-inner{background:var(--surface);border-radius:calc(var(--radius-lg) - 1px);padding:1.5rem;}
```

### Shimmer Skeleton
```css
.skeleton{background:linear-gradient(90deg,var(--surface) 25%,rgba(255,255,255,.06) 50%,var(--surface) 75%);background-size:200% 100%;animation:shimmer 1.5s ease-in-out infinite;border-radius:var(--radius);}
@keyframes shimmer{from{background-position:200% 0}to{background-position:-200% 0}}
```

### Dark/Light Toggle
```javascript
document.documentElement.setAttribute('data-theme',localStorage.getItem('theme')||'dark');
document.getElementById('theme-toggle').addEventListener('click',()=>{
  const n=document.documentElement.getAttribute('data-theme')==='dark'?'light':'dark';
  document.documentElement.setAttribute('data-theme',n);
  localStorage.setItem('theme',n);
});
```
```css
[data-theme="light"]{--bg:#f5f5f5;--text:#111;--surface:#fff;}
[data-theme="dark"]{--bg:#0a0a0f;--text:#e8e8f0;--surface:#12121a;}
```

---

## 10. Performance Rules

| DO | NEVER |
|---|---|
| `transform` + `opacity` only in animations | `width`, `height`, `top`, `left`, `margin` |
| `will-change:transform` on animated elements only | `will-change` on everything |
| `{passive:true}` on scroll/touch listeners | Unpassive scroll listeners doing layout |
| `loading="lazy"` on below-fold images | Missing lazy loading |
| `font-display:swap` on all fonts | Blocking font load |
| `clamp()` for all type + spacing | Fixed `px` everywhere |
| `aspect-ratio` on all media | Missing dimensions (CLS) |

---

## 11. Production Checklist

- [ ] Semantic HTML — `header`, `main`, `nav`, `section`, `footer`
- [ ] All colors via CSS variables — zero hardcoded hex in components
- [ ] Tested: 375px, 768px, 1280px, 1440px
- [ ] `prefers-reduced-motion` block + `gsap.matchMedia()`
- [ ] 4.5:1 contrast, focus rings visible, alt text on images
- [ ] `aspect-ratio` on all images
- [ ] `font-display:swap` on external fonts
- [ ] `loading="lazy"` on below-fold images
- [ ] Audit: `python3 scripts/audit.py <file>`

---

## 12. Multi-Stack Quick Start

### React / Next.js
```bash
npx create-next-app@latest my-site --tailwind --app
npm install framer-motion gsap @gsap/react lucide-react
npx shadcn@latest init
```

### Vue / Nuxt
```bash
npx nuxi init my-site
npm install @vueuse/motion gsap
```

### Plain HTML
Use the boilerplate in Section 4 directly. No build step.

---

For deep dives, read the reference files:
- Animation patterns → `references/gsap.md`
- React + framer-motion → `references/components.md`
- Design tokens → `references/aesthetics.md`
- Full UX rules → `references/uiux-rules.md`
- 21st.dev components → `references/component-library.md`
