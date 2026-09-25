# Components Reference

React boilerplate, Motion patterns, Three.js, and 21st.dev-style components.

---

## React / JSX Artifact — Full Boilerplate

```jsx
import { useState, useEffect, useRef } from "react"
import { motion, AnimatePresence, useScroll, useTransform, useSpring, useMotionValue, useInView } from "framer-motion"

// ─── REUSABLE VARIANTS ───────────────────────────────────────────────────────

const fadeUp = {
  hidden: { opacity: 0, y: 24 },
  show:   { opacity: 1, y: 0, transition: { duration: 0.6, ease: [0.25, 0.46, 0.45, 0.94] } }
}
const stagger = {
  hidden: {},
  show:   { transition: { staggerChildren: 0.1, delayChildren: 0.1 } }
}

// ─── COMPONENTS ──────────────────────────────────────────────────────────────

// Scroll-reveal wrapper — wrap every major section with this
function Section({ children, className = "" }) {
  return (
    <motion.section
      variants={stagger} initial="hidden" whileInView="show"
      viewport={{ once: true, margin: "-80px" }}
      className={className}
    >
      {children}
    </motion.section>
  )
}

// Magnetic button with spring physics
function MagButton({ children, className = "", ...props }) {
  const ref = useRef(null)
  const x = useMotionValue(0)
  const y = useMotionValue(0)
  const sx = useSpring(x, { stiffness: 200, damping: 20 })
  const sy = useSpring(y, { stiffness: 200, damping: 20 })

  return (
    <motion.button
      ref={ref}
      style={{ x: sx, y: sy }}
      className={className}
      onMouseMove={e => {
        const r = ref.current.getBoundingClientRect()
        x.set((e.clientX - r.left - r.width  / 2) * 0.35)
        y.set((e.clientY - r.top  - r.height / 2) * 0.35)
      }}
      onMouseLeave={() => { x.set(0); y.set(0) }}
      whileTap={{ scale: 0.97 }}
      {...props}
    >
      {children}
    </motion.button>
  )
}

// Glow card — radial gradient follows cursor
function GlowCard({ children, style = {} }) {
  const mx = useMotionValue(0)
  const my = useMotionValue(0)

  return (
    <motion.div
      style={{ position: "relative", overflow: "hidden", ...style }}
      onMouseMove={e => {
        const r = e.currentTarget.getBoundingClientRect()
        mx.set(e.clientX - r.left)
        my.set(e.clientY - r.top)
      }}
    >
      <motion.div
        style={{
          position: "absolute", inset: 0, pointerEvents: "none",
          // motion values used directly in style — no hook-in-render violation
          background: "transparent"
        }}
        // Use inline dynamic style via useTransform instead
      />
      {/* Glow handled by CSS on hover for simplicity in static contexts */}
      {children}
    </motion.div>
  )
}

// Number counter that animates up on scroll — CORRECTLY structured (no hook in render)
function Counter({ value, suffix = "", duration = 2 }) {
  const ref = useRef(null)
  const inView = useInView(ref, { once: true })
  const motionValue = useMotionValue(0)
  const spring = useSpring(motionValue, { duration: duration * 1000, bounce: 0 })
  const [display, setDisplay] = useState(0)

  useEffect(() => {
    if (inView) motionValue.set(value)
  }, [inView, value, motionValue])

  useEffect(() => {
    return spring.on("change", v => setDisplay(Math.floor(v)))
  }, [spring])

  return <span ref={ref}>{display.toLocaleString()}{suffix}</span>
}

// ─── MAIN COMPONENT ──────────────────────────────────────────────────────────

export default function App() {
  return (
    <div style={{
      background: "#0a0a0f", color: "#e8e8f0", minHeight: "100vh",
      fontFamily: "'Plus Jakarta Sans', sans-serif"
    }}>
      <Section style={{ padding: "10rem 2rem", maxWidth: 1200, margin: "0 auto" }}>
        <motion.h1
          variants={fadeUp}
          style={{ fontSize: "clamp(2.5rem, 8vw, 6rem)", lineHeight: 0.95, letterSpacing: "-0.02em" }}
        >
          Your Headline
        </motion.h1>
        <motion.p
          variants={fadeUp}
          style={{ color: "#6b6b80", maxWidth: 520, marginTop: "1.5rem" }}
        >
          Supporting copy that sells the vision.
        </motion.p>
        <motion.div variants={fadeUp} style={{ marginTop: "2.5rem" }}>
          <MagButton
            style={{
              padding: "0.875rem 2rem", background: "#39ff14", color: "#0a0a0f",
              border: "none", borderRadius: 8, fontWeight: 600, fontSize: "1rem", cursor: "pointer"
            }}
          >
            Get started →
          </MagButton>
        </motion.div>
      </Section>
    </div>
  )
}
```

---

## Available Libraries in Claude React Artifacts

```js
// Animation
import { motion, AnimatePresence, useScroll, useTransform, useSpring,
         useMotionValue, useInView, useDragControls } from "framer-motion"

// React
import { useState, useEffect, useRef, useCallback, useMemo, useReducer, useId } from "react"

// Data viz
import { LineChart, BarChart, PieChart, AreaChart, ScatterChart,
         XAxis, YAxis, CartesianGrid, Tooltip, Legend, Line, Bar, Area,
         Scatter, ResponsiveContainer, Cell } from "recharts"

// 3D
import * as THREE from "three"   // r128 — no OrbitControls on CDN

// Utilities
import _ from "lodash"
import * as math from "mathjs"
import * as d3 from "d3"

// Icons
import { ArrowRight, Zap, Star, ChevronDown, Menu, X, Check,
         Github, Twitter, Linkedin, Moon, Sun, Search } from "lucide-react"
```

---

## Motion Patterns

### Scroll-Driven Parallax

```jsx
function Parallax({ children, speed = 0.2 }) {
  const ref = useRef(null)
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start end", "end start"] })
  const y = useTransform(scrollYProgress, [0, 1], [`${-speed * 100}%`, `${speed * 100}%`])
  return <motion.div ref={ref} style={{ y }}>{children}</motion.div>
}
```

### AnimatePresence — Tab / Modal Switching

```jsx
<AnimatePresence mode="wait">
  {activeTab === "features" && (
    <motion.div
      key="features"
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -12 }}
      transition={{ duration: 0.25, ease: [0.25, 0.46, 0.45, 0.94] }}
    >
      {/* tab content */}
    </motion.div>
  )}
</AnimatePresence>
```

### Shared Element / Layout Animation

```jsx
// Items that move between positions animate automatically
<motion.div layout layoutId="active-pill" />

// Smooth list reorder
{items.map(item => (
  <motion.li key={item.id} layout>
    {item.name}
  </motion.li>
))}
```

### Drag with Constraints

```jsx
function DraggableCard() {
  const constraintsRef = useRef(null)
  return (
    <div ref={constraintsRef} style={{ position: "relative", height: 400 }}>
      <motion.div
        drag
        dragConstraints={constraintsRef}
        dragElastic={0.1}
        whileDrag={{ scale: 1.05, rotate: 3, zIndex: 10 }}
        style={{ width: 200, height: 120, background: "#12121a", borderRadius: 12, cursor: "grab" }}
      />
    </div>
  )
}
```

### Stagger Children on Hover

```jsx
const container = {
  rest: {},
  hover: { transition: { staggerChildren: 0.05 } }
}
const child = {
  rest:  { x: 0 },
  hover: { x: 8, transition: { duration: 0.2 } }
}

<motion.div variants={container} initial="rest" whileHover="hover">
  {items.map(item => (
    <motion.div key={item} variants={child}>{item}</motion.div>
  ))}
</motion.div>
```

---

## Three.js — Verified r128 Scene

```jsx
// In a React JSX artifact:
import * as THREE from "three"  // r128 — no OrbitControls available from CDN
import { useEffect, useRef } from "react"

function ThreeScene() {
  const mountRef = useRef(null)

  useEffect(() => {
    const el = mountRef.current
    const W = el.clientWidth, H = el.clientHeight

    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true })
    renderer.setSize(W, H)
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
    el.appendChild(renderer.domElement)

    const scene  = new THREE.Scene()
    const camera = new THREE.PerspectiveCamera(60, W / H, 0.1, 100)
    camera.position.z = 4

    const mesh = new THREE.Mesh(
      new THREE.IcosahedronGeometry(1.2, 1),
      new THREE.MeshStandardMaterial({ color: 0x39ff14, wireframe: true,
        emissive: 0x39ff14, emissiveIntensity: 0.3 })
    )
    scene.add(mesh)
    scene.add(new THREE.AmbientLight(0xffffff, 0.5))
    scene.add(new THREE.DirectionalLight(0xffffff, 1))

    let mx = 0, my = 0
    const onMouse = e => {
      mx = (e.clientX / window.innerWidth  - 0.5) * 2
      my = (e.clientY / window.innerHeight - 0.5) * 2
    }
    window.addEventListener('mousemove', onMouse)

    let frameId
    const animate = () => {
      frameId = requestAnimationFrame(animate)
      mesh.rotation.y += 0.005 + mx * 0.02
      mesh.rotation.x += 0.002 + my * 0.01
      renderer.render(scene, camera)
    }
    animate()

    return () => {
      cancelAnimationFrame(frameId)
      window.removeEventListener('mousemove', onMouse)
      renderer.dispose()
      el.removeChild(renderer.domElement)
    }
  }, [])

  return <div ref={mountRef} style={{ width: "100%", height: 400 }} />
}
```

**Plain HTML version** (for single-file builds):
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<canvas id="gl" style="position:fixed;inset:0;z-index:-1;pointer-events:none"></canvas>
<script>
const W = innerWidth, H = innerHeight;
const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('gl'), antialias: true, alpha: true });
renderer.setSize(W, H);
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(60, W/H, 0.1, 100);
camera.position.z = 4;
const mesh = new THREE.Mesh(
  new THREE.IcosahedronGeometry(1.2, 1),
  new THREE.MeshStandardMaterial({ color: 0x39ff14, wireframe: true, emissive: 0x39ff14, emissiveIntensity: 0.3 })
);
scene.add(mesh, new THREE.AmbientLight(0xffffff, 0.5), new THREE.DirectionalLight(0xffffff, 1));
let mx=0, my=0;
document.addEventListener('mousemove', e => { mx=(e.clientX/W-.5)*2; my=(e.clientY/H-.5)*2; });
(function animate() {
  requestAnimationFrame(animate);
  mesh.rotation.y += 0.005 + mx*0.02;
  mesh.rotation.x += 0.002 + my*0.01;
  renderer.render(scene, camera);
})();
window.addEventListener('resize', () => {
  renderer.setSize(innerWidth, innerHeight);
  camera.aspect = innerWidth/innerHeight;
  camera.updateProjectionMatrix();
});
</script>
```

---

## 21st.dev Component Patterns

### Gradient Border Card

```css
.glow-card { position:relative; border-radius:16px; padding:1px; }
.glow-card::before {
  content:''; position:absolute; inset:0; border-radius:inherit;
  background: linear-gradient(135deg, var(--accent), transparent 50%, var(--accent-2));
  opacity:0; transition:opacity 0.3s;
}
.glow-card:hover::before { opacity:1; }
.glow-card-inner { background:var(--surface); border-radius:15px; padding:1.5rem; }
```

### Animated Tab Indicator (CSS-only)

```html
<div class="tabs" style="position:relative;display:flex;gap:4px;">
  <button class="tab active">Features</button>
  <button class="tab">Pricing</button>
  <button class="tab">Docs</button>
</div>
<style>
.tabs { background: var(--surface); border-radius: 8px; padding: 4px; }
.tab {
  padding: 0.5rem 1.25rem; border: none; background: transparent;
  border-radius: 6px; cursor: pointer; color: var(--text-muted);
  transition: color 0.2s;
  position: relative; z-index: 1;
}
.tab.active { color: var(--text); }
/* Sliding pill via sibling CSS — or use Flip plugin for animated version */
</style>
```

### Hero Patterns Quick Reference

| Pattern | Key technique |
|---|---|
| Oversized type + gradient mesh | `clamp()` type + layered `radial-gradient` |
| Full-viewport 3D canvas | Three.js canvas `position:fixed;z-index:-1` |
| Split screen text/visual | CSS Grid `3fr 2fr` + scroll parallax |
| Particle field | p5.js `noise()` flow field |
| Video background | `<video autoplay muted loop playsinline>` |
| Terminal / typewriter | `setInterval` + character append |
| Full-bleed image + grain | `object-fit:cover` + grain SVG overlay |
