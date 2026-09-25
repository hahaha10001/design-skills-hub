# GSAP Reference

**All GSAP plugins are 100% free** as of 2025 (Webflow deal). No Club membership needed.

**Always load from jsDelivr** — cdnjs only has core up to 3.12.2 and is missing all bonus plugins.

```html
<!-- Core (always load first) -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/gsap.min.js"></script>

<!-- Load ONLY the plugins you actually use: -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/SplitText.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/ScrollSmoother.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/Flip.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/DrawSVGPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/MorphSVGPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/MotionPathPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/CustomEase.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/Draggable.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/Observer.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/ScrollToPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/Physics2DPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/ScrambleTextPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/TextPlugin.min.js"></script>

<!-- Register everything you loaded -->
<script>
gsap.registerPlugin(ScrollTrigger, SplitText, Flip, DrawSVGPlugin, CustomEase);
</script>
```

**npm** (for build-tool projects):
```js
import gsap from "gsap"
import { ScrollTrigger } from "gsap/ScrollTrigger"
import { SplitText } from "gsap/SplitText"
import { Flip } from "gsap/Flip"
import { DrawSVGPlugin } from "gsap/DrawSVGPlugin"
import { MorphSVGPlugin } from "gsap/MorphSVGPlugin"
import { CustomEase } from "gsap/CustomEase"
import { Observer } from "gsap/Observer"
import { ScrollToPlugin } from "gsap/ScrollToPlugin"
import { ScrambleTextPlugin } from "gsap/ScrambleTextPlugin"

gsap.registerPlugin(ScrollTrigger, SplitText, Flip, DrawSVGPlugin, Observer, ScrollToPlugin)
```

---

## Plugin Selection

| Need | Plugin |
|---|---|
| Text animated by char / word / line | SplitText |
| Buttery smooth scroll + zero-JS parallax | ScrollSmoother |
| Animate layout changes (sort, filter, tab) | Flip |
| Draw / erase SVG paths | DrawSVGPlugin |
| Morph between SVG shapes | MorphSVGPlugin |
| Custom easing curves | CustomEase |
| Swipe / gesture / wheel events | Observer |
| Programmatic scroll-to | ScrollToPlugin |
| Physics — gravity, throw, bounce | Draggable + InertiaPlugin |
| Responsive animations + reduced motion | gsap.matchMedia() |
| Element follows an SVG path | MotionPathPlugin |
| Matrix / glitch text scramble | ScrambleTextPlugin |
| Typewriter effect | TextPlugin |
| Characters explode off screen | SplitText + Physics2DPlugin |

---

## SplitText

```javascript
gsap.registerPlugin(ScrollTrigger, SplitText);

// Lines reveal upward — classic editorial
const split = new SplitText('.headline', {
  type: 'lines',
  mask: 'lines'  // wraps lines in overflow:hidden automatically
});

gsap.from(split.lines, {
  scrollTrigger: { trigger: '.headline', start: 'top 85%' },
  yPercent: 110, duration: 0.8, stagger: 0.12, ease: 'power4.out'
});

// Words scatter in
const words = new SplitText('.tagline', { type: 'words' });
gsap.from(words.words, {
  scrollTrigger: { trigger: '.tagline', start: 'top 85%' },
  opacity: 0, y: 20, rotation: 5,
  duration: 0.5, stagger: 0.07, ease: 'back.out(1.5)'
});

// autoSplit — re-splits on viewport resize (responsive)
new SplitText('.hero-title', {
  type: 'chars',
  autoSplit: true,
  onSplit(self) {
    // always create animations here, not outside onSplit
    gsap.from(self.chars, {
      opacity: 0, y: 40, duration: 0.4,
      stagger: 0.025, ease: 'power3.out'
    });
  }
});
```

---

## ScrollSmoother

> Requires wrapping your entire page in a two-div structure.

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/ScrollSmoother.min.js"></script>

<!-- Required HTML structure — ALL content goes inside smooth-content -->
<div id="smooth-wrapper">
  <div id="smooth-content">
    <!-- everything here -->
  </div>
</div>

<script>
gsap.registerPlugin(ScrollTrigger, ScrollSmoother);

const smoother = ScrollSmoother.create({
  wrapper: '#smooth-wrapper',
  content: '#smooth-content',
  smooth: 1.5,         // higher = more lag = more buttery
  effects: true,       // enables data-speed and data-lag HTML attributes
  smoothTouch: 0.1     // subtle smoothing on touch devices
});
</script>
```

**Zero-JS parallax via HTML attributes** (requires `effects: true`):
```html
<img src="bg.jpg" data-speed="0.6" alt="">      <!-- slower = parallax bg -->
<h1 data-speed="1.2">Moves faster</h1>
<div class="card" data-lag="0.3">Lags slightly</div>
```

**Programmatic scroll**:
```javascript
smoother.scrollTo('#section-3', true, 'top top');
```

> **Gotcha**: ScrollSmoother + pinned ScrollTrigger sections require `pinnedContainer` option or the pinned section offset will be wrong. Test with `markers: true` during development.

---

## Flip

The most underused powerful plugin. Captures DOM state before a change, then animates smoothly into the new state. Perfect for filter/sort grids, tab switching, adding/removing items.

```javascript
gsap.registerPlugin(Flip);

// Filter a portfolio grid
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const filter = btn.dataset.filter;

    // 1. Capture layout state BEFORE the DOM change
    const state = Flip.getState('.grid-item');

    // 2. Make the DOM change (show/hide items)
    document.querySelectorAll('.grid-item').forEach(item => {
      item.style.display =
        filter === 'all' || item.dataset.cat === filter ? 'block' : 'none';
    });

    // 3. Animate from old positions to new positions
    Flip.from(state, {
      duration: 0.5, ease: 'power2.inOut', stagger: 0.05, absolute: true,
      onEnter: els => gsap.from(els, { opacity: 0, scale: 0.8, duration: 0.3 }),
      onLeave: els => gsap.to(els, { opacity: 0, scale: 0.8, duration: 0.3 })
    });
  });
});

// Animated tab indicator (shared element)
function switchTab(newTabEl) {
  const state = Flip.getState('.tab-indicator');
  newTabEl.appendChild(document.querySelector('.tab-indicator'));
  Flip.from(state, { duration: 0.4, ease: 'power2.inOut' });
}
```

---

## DrawSVG

```javascript
gsap.registerPlugin(ScrollTrigger, DrawSVGPlugin);

// Path draws on scroll
gsap.from('.svg-path', {
  scrollTrigger: { trigger: '.svg-wrap', start: 'top 70%', end: 'bottom 30%', scrub: 1 },
  drawSVG: '0%'
});

// Hover underline (draw on enter, erase on leave)
document.querySelectorAll('.hover-line').forEach(el => {
  const path = el.querySelector('path');
  gsap.set(path, { drawSVG: '0%' });
  el.addEventListener('mouseenter', () =>
    gsap.to(path, { drawSVG: '100%', duration: 0.4, ease: 'power2.out' }));
  el.addEventListener('mouseleave', () =>
    gsap.to(path, { drawSVG: '0%', duration: 0.3, ease: 'power2.in' }));
});

// Partial draw (only middle segment)
gsap.to('.path', { drawSVG: '20% 80%', duration: 0.6 });
```

---

## MorphSVG

```javascript
gsap.registerPlugin(MorphSVGPlugin);

// Play/pause icon toggle
let playing = false;
const play  = 'M8 5v14l11-7z';
const pause = 'M6 19h4V5H6v14zm8-14v14h4V5h-4z';

document.getElementById('play-btn').addEventListener('click', () => {
  playing = !playing;
  gsap.to('#icon-path', {
    duration: 0.4,
    morphSVG: { shape: playing ? pause : play, type: 'rotational' },
    ease: 'power2.inOut'
  });
});

// Menu → Close icon
gsap.to('#menu-icon', {
  morphSVG: '#close-icon',
  duration: 0.5, ease: 'power3.inOut'
});
```

---

## CustomEase

```javascript
gsap.registerPlugin(CustomEase);

// Define once, reuse everywhere by name
CustomEase.create('premium',  'M0,0 C0.25,0.1 0.25,1 1,1');          // refined S-curve
CustomEase.create('snap',     'M0,0 C0.14,0 0.242,0.438 0.272,0.561 0.313,0.728 0.354,0.963 0.362,1 0.37,0.985 1,1 1,1');
CustomEase.create('rubber',   'M0,0 C0,0 0.056,0.442 0.175,0.442 0.294,0.442 0.332,0 0.397,0 0.461,0 0.491,1 0.599,1 0.668,1 0.702,0.963 0.732,0.963 0.763,0.963 0.786,1.041 0.819,1.041 0.862,1.041 1,1 1,1');

gsap.to('.nav', { y: 0, ease: 'premium', duration: 0.8 });
gsap.to('.btn', { scale: 1, ease: 'rubber', duration: 1 });

// Built-in eases worth memorising:
// 'expo.out'          — fast start, graceful landing     (navs, drawers)
// 'back.out(1.7)'     — slight overshoot                 (playful cards)
// 'elastic.out(1,.5)' — spring physics                   (magnetic release)
// 'power4.inOut'      — professional S-curve             (page transitions)
// 'none'              — linear (use ONLY with scrub)
```

---

## Observer (Fullscreen Section Snapping)

> Requires `ScrollToPlugin` loaded alongside `Observer` for the `gsap.to(window, { scrollTo })` call to work.

```javascript
// Load both:
// <script src="cdn.jsdelivr.net/npm/gsap@3.14/dist/Observer.min.js"></script>
// <script src="cdn.jsdelivr.net/npm/gsap@3.14/dist/ScrollToPlugin.min.js"></script>

gsap.registerPlugin(Observer, ScrollToPlugin);

const sections = gsap.utils.toArray('.section');
let current = 0, animating = false;

function goTo(index) {
  if (index < 0 || index >= sections.length || animating) return;
  animating = true;
  gsap.to(window, {
    scrollTo: { y: sections[index], autoKill: false },
    duration: 1, ease: 'power3.inOut',
    onComplete: () => { animating = false; }
  });
  current = index;
}

Observer.create({
  type: 'wheel,touch,pointer',
  wheelSpeed: -1,
  onDown: () => goTo(current - 1),
  onUp:   () => goTo(current + 1),
  tolerance: 10,
  preventDefault: true
});
```

---

## ScrambleText

```javascript
gsap.registerPlugin(ScrambleTextPlugin);

// Reveal with character scramble
gsap.to('.heading', {
  duration: 1.5,
  scrambleText: {
    text: 'FINAL TEXT HERE',
    chars: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    revealDelay: 0.4,
    speed: 0.5
  }
});

// Binary / code scramble
gsap.to('.code', {
  duration: 1,
  scrambleText: { text: 'initializing...', chars: '01', speed: 0.8 }
});

// Glitch on hover
el.addEventListener('mouseenter', () => {
  gsap.to(el, {
    duration: 0.6,
    scrambleText: { text: el.dataset.text || el.textContent, chars: '!@#$%^&*', speed: 1 }
  });
});
```

---

## Timeline Mastery

```javascript
// Staggered entrance with overlaps — this is what pro intros look like
const tl = gsap.timeline({ defaults: { ease: 'power3.out', duration: 0.8 } });

tl.from('.nav',        { y: -80, opacity: 0 })
  .from('.badge',      { scale: 0, opacity: 0 },  '-=0.4')  // starts 0.4s before prev ends
  .from('.headline',   { y: 60, opacity: 0 },     '-=0.3')
  .from('.subline',    { y: 40, opacity: 0 },     '-=0.4')
  .from('.cta',        { y: 30, opacity: 0 },     '-=0.4')
  .from('.hero-img',   { x: 80, opacity: 0 },     '<');     // same start time as previous

// toggleActions reference:
// 'play pause resume reverse' — onEnter onLeave onEnterBack onLeaveBack
// most useful: 'play none none reverse' or 'play none none none'
const st = gsap.timeline({
  scrollTrigger: { trigger: '.section', start: 'top 70%', toggleActions: 'play none none reverse' }
});

// Seek and control
tl.addLabel('act-2', '+=0');
document.getElementById('skip').onclick = () => tl.seek('act-2');
document.getElementById('pause').onclick = () => tl.paused() ? tl.play() : tl.pause();
```

---

## gsap.matchMedia() — Responsive + Reduced Motion

```javascript
const mm = gsap.matchMedia();

// Multi-condition — most useful pattern
mm.add({
  isDesktop:    '(min-width: 768px)',
  isMobile:     '(max-width: 767px)',
  reduceMotion: '(prefers-reduced-motion: reduce)'
}, ({ conditions: { isDesktop, reduceMotion } }) => {
  if (reduceMotion) return; // respect user preference — no animation

  // Always runs (both breakpoints, no reduced motion)
  gsap.from('.hero-text', { y: 60, opacity: 0, duration: 1, ease: 'power3.out' });

  if (isDesktop) {
    // Desktop-only complex animations
    ScrollTrigger.create({ trigger: '.features', pin: true, end: '+=1000', scrub: 1 });
    new SplitText('.headline', { type: 'lines', mask: 'lines' });
  }

  return () => {
    // Optional cleanup when query stops matching
    ScrollTrigger.getAll().forEach(t => t.kill());
  };
});
```
