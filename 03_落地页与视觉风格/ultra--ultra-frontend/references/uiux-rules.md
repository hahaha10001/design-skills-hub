# UX Rules Reference (uiuxpromax)

10 priority categories. Always apply in order 1→10. Anti-patterns are equally important.

---

## Priority 1 — Accessibility (CRITICAL)

**Must have:**
- Color contrast ≥ 4.5:1 for body text, ≥ 3:1 for large text (18px+ bold / 24px+)
- All interactive elements keyboard-navigable (Tab, Enter, Space, Arrow keys)
- `aria-label` on icon-only buttons: `<button aria-label="Close menu">`
- `alt` text on all images (empty `alt=""` for decorative)
- Focus rings always visible — never `outline: none` without a custom replacement
- `role`, `aria-expanded`, `aria-controls` on custom components (dropdowns, accordions)
- Skip-to-main link: `<a href="#main" class="sr-only focus:not-sr-only">Skip to content</a>`

**Anti-patterns:**
- `outline: none` or `outline: 0` with no replacement
- Icon-only buttons without `aria-label`
- Color as the only way to convey information (use shape/text too)
- Missing `lang` attribute on `<html>`
- Form inputs without associated `<label>`

**Tools:** axe DevTools, Lighthouse, WAVE, VoiceOver/NVDA testing

---

## Priority 2 — Touch & Interaction (CRITICAL)

**Must have:**
- Minimum touch target: 44×44px (iOS HIG) — applies to buttons, links, checkboxes
- 8px minimum spacing between adjacent touch targets
- Loading feedback within 100ms of any interaction
- Disabled state visually distinct (opacity 0.4 + `cursor: not-allowed`)
- Hover + focus + active + disabled states for every interactive element
- Press states: `scale(0.97)` or `background-color` shift on `:active`

**Anti-patterns:**
- Hover-only interactions (breaks touch devices)
- Instant state changes (0ms) — always transition ≥150ms
- Touch targets < 44px (especially on mobile nav)
- No loading indicator on async actions
- `pointer-events: none` blocking expected interactions

---

## Priority 3 — Performance

**Must have:**
- Images: WebP or AVIF format, `srcset` for responsive sizes
- `loading="lazy"` on all below-fold images
- `width` + `height` on images to reserve space (prevents CLS)
- CLS (Cumulative Layout Shift) < 0.1
- Fonts: `font-display: swap`, preconnect to font CDN
- CSS: only animate `transform` and `opacity` (GPU-composited)
- JS: defer non-critical scripts, code-split where possible

**Anti-patterns:**
- Animating `width`, `height`, `top`, `left`, `margin` (causes reflow)
- Images without dimensions (layout shift)
- Render-blocking scripts in `<head>` without `defer`/`async`
- Loading all 14 GSAP plugins when you need 2
- Unpassive scroll listeners: always `{ passive: true }`

---

## Priority 4 — Style Selection

**Match product type to aesthetic:**

| Product | Recommended styles |
|---|---|
| SaaS / B2B | Glassmorphic, Technical Blueprint, Futurist Dark |
| E-commerce | Clean minimal, editorial, brand-led |
| Portfolio | Brutalist Editorial, Cinematic Luxury, Refined Minimal |
| Wellness / Lifestyle | Soft Gen-Z, organic, pastel |
| Developer tool | DevTools Chrome, Technical Blueprint |
| Gaming / Music | Retro-Futuristic, Maximalist Chaos |
| Fintech | Futurist Dark, Technical Blueprint |
| Agency | Brutalist Editorial, Maximalist Chaos |

**Must have:**
- One clear aesthetic direction — commit fully
- Consistent icon set (Lucide, Heroicons, or Phosphor — never mix)
- SVG icons only — never emoji as UI icons

**Anti-patterns:**
- Mixing flat and skeuomorphic randomly
- Emoji as interface icons
- Purple gradient on white (the most overused AI-generated pattern)
- Inter + card grid + purple gradient = instant AI slop
- Inconsistent border-radius (some 4px, some 20px, some 0)

---

## Priority 5 — Layout & Responsive

**Must have:**
- Mobile-first: write base styles for 375px, enhance with min-width breakpoints
- Standard breakpoints: 375 / 768 / 1024 / 1280 / 1440
- No horizontal scroll on any viewport
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- Fluid sizing: `clamp()` for type, `min()` for containers, `%` + `vw` for layout

**Anti-patterns:**
- `overflow: hidden` on `<body>` hiding scroll issues instead of fixing them
- Fixed pixel container widths without max-width
- `user-scalable=no` in viewport (accessibility violation)
- Horizontal scroll on mobile
- Desktop-only layouts that break below 768px

**Breakpoint system:**
```css
/* Mobile first */
.component { /* 375px base */ }
@media (min-width: 768px)  { /* tablet  */ }
@media (min-width: 1024px) { /* desktop */ }
@media (min-width: 1280px) { /* wide    */ }
```

---

## Priority 6 — Typography & Color

**Typography:**
- Base body: 16px minimum (never below 14px for body, 12px for labels)
- Line-height: 1.5–1.7 for body, 0.9–1.1 for display
- Letter-spacing: -0.02em to -0.04em for large display type, 0.05em+ for small caps
- Font scale: use `clamp()` — `clamp(1rem, 2vw, 1.125rem)` for body
- Max line length: 65–75ch for body text
- Semantic color tokens in CSS variables — never raw hex in components

**Color:**
- 60/30/10 rule: 60% background, 30% surface/secondary, 10% accent
- Dominant + secondary + sharp accent only
- Always `prefers-color-scheme` if doing dark mode
- Check contrast with browser devtools or Polypane

**Anti-patterns:**
- Body text below 14px
- Gray text on gray background (fails contrast)
- More than 3 font families
- Hardcoded colors in components: `color: #39ff14` → `color: var(--accent)`
- All-caps body text (hurts readability)

---

## Priority 7 — Animation

**Rules:**
- Entrance animations: 150–400ms
- Page transitions: 200–350ms
- Micro-interactions: 100–200ms
- Scroll-scrubbed animations: no duration limit (tied to scroll)
- Motion should convey meaning — entrance from direction of origin, exit to destination
- Spatial continuity: elements that move should maintain physical logic
- `prefers-reduced-motion`: always respect

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

**Anti-patterns:**
- Decorative-only animations that add no meaning
- Animating `width`, `height` (reflow)
- Animations over 600ms for simple state changes
- No `prefers-reduced-motion` support
- Infinite spinning loaders with no progress indication

---

## Priority 8 — Forms & Feedback

**Must have:**
- Visible `<label>` for every input (not placeholder-only)
- Error messages directly below the field that errored (not just at top)
- Helper text before interaction (not only on error)
- Progressive disclosure: show advanced options only when needed
- Success state confirmation after submit
- Disabled submit button while loading (with spinner)

**Anti-patterns:**
- Placeholder as the only label (disappears on focus)
- Errors only at top of form
- No success feedback after form submission
- Required fields indicated only by color
- Password fields without show/hide toggle

---

## Priority 9 — Navigation

**Must have:**
- Predictable back behavior (browser back always works)
- Bottom navigation on mobile: max 5 items
- Active state clearly visible on current page/section
- Deep linking: URLs reflect app state
- Breadcrumbs for pages > 2 levels deep

**Anti-patterns:**
- Overloaded navigation (> 7 top-level items)
- Breaking browser back button
- No visual indication of current location
- Mobile navigation that requires horizontal scroll
- Hamburger menu with no close affordance

---

## Priority 10 — Charts & Data

**Must have:**
- Legend explaining every data series
- Tooltips on hover/focus with exact values
- Color-blind safe palettes (avoid red/green pairs alone)
- Accessible: data tables as alternative to charts
- Labels on chart axes
- Clear chart title

**Anti-patterns:**
- Color as the only differentiator between data series
- No labels on axes
- Pie charts with > 5 segments (use bar instead)
- 3D charts (distorts perception)
- Missing null/zero state design

**Color-blind safe chart colors:**
```
Blue:   #1f77b4
Orange: #ff7f0e
Green:  #2ca02c  (use texture too)
Purple: #9467bd
Brown:  #8c564b
Pink:   #e377c2
```

---

## Multi-Stack Guidelines

### React / Next.js
- Components: shadcn/ui base + custom layer
- Animation: framer-motion for component-level, GSAP for scroll/page
- State: Zustand or Jotai for global, React Query for server
- Icons: Lucide React

### Vue / Nuxt
- Components: Nuxt UI or PrimeVue
- Animation: @vueuse/motion + GSAP
- State: Pinia

### Svelte / SvelteKit
- Animation: Svelte built-in transitions + GSAP for scroll
- CSS: Tailwind or UnoCSS

### HTML / Tailwind (no framework)
- Animation: GSAP only (no framer-motion in vanilla)
- Interactivity: Alpine.js for lightweight reactivity

### React Native
- Animation: react-native-reanimated (not Animated API)
- Navigation: Expo Router
- UI: NativeWind (Tailwind for RN)

### Flutter
- Animation: AnimationController + Curves
- State: Riverpod or Bloc
- UI: Material 3 or custom theme

### SwiftUI
- Animation: `.animation()` modifier + `withAnimation {}`
- Use `matchedGeometryEffect` for shared element transitions
