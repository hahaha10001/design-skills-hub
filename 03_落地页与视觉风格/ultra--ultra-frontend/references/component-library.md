# 21st.dev Component Library

Production-ready React + Tailwind components. Copy-paste, customize tokens, ship.
All components use shadcn/ui primitives + framer-motion where noted.

---

## Dock (macOS-style magnification)

```jsx
import { motion, useMotionValue, useTransform, useSpring } from "framer-motion"
import { useRef } from "react"

function DockItem({ icon, label, mouseX }) {
  const ref = useRef(null)
  const distance = useTransform(mouseX, v => {
    const bounds = ref.current?.getBoundingClientRect() ?? { x: 0, width: 0 }
    return v - bounds.x - bounds.width / 2
  })
  const size = useTransform(distance, [-120, 0, 120], [40, 72, 40])
  const sizeSpring = useSpring(size, { stiffness: 300, damping: 25 })

  return (
    <motion.div ref={ref} style={{ width: sizeSpring, height: sizeSpring }}
      className="flex items-end justify-center cursor-pointer relative group"
      whileTap={{ scale: 0.9 }}>
      <motion.div className="absolute -top-10 opacity-0 group-hover:opacity-100
        bg-black/80 text-white text-xs px-2 py-1 rounded-md whitespace-nowrap transition-opacity">
        {label}
      </motion.div>
      <div className="w-full h-full rounded-2xl bg-white/10 backdrop-blur-sm
        border border-white/20 flex items-center justify-center text-2xl">
        {icon}
      </div>
    </motion.div>
  )
}

export function Dock({ items }) {
  const mouseX = useMotionValue(Infinity)
  return (
    <motion.div
      onMouseMove={e => mouseX.set(e.pageX)}
      onMouseLeave={() => mouseX.set(Infinity)}
      className="fixed bottom-6 left-1/2 -translate-x-1/2 flex items-end gap-2
        bg-white/10 backdrop-blur-xl border border-white/20 rounded-2xl px-4 pb-3 pt-4">
      {items.map(item => <DockItem key={item.label} mouseX={mouseX} {...item} />)}
    </motion.div>
  )
}

// Usage: <Dock items={[{ icon: "🏠", label: "Home" }, { icon: "⚡", label: "Dashboard" }]} />
```

---

## Command Menu (Cmd+K Palette)

```jsx
import { useState, useEffect, useRef } from "react"
import { motion, AnimatePresence } from "framer-motion"

export function CommandMenu({ commands }) {
  const [open, setOpen] = useState(false)
  const [query, setQuery] = useState("")
  const inputRef = useRef(null)

  useEffect(() => {
    const handler = e => {
      if ((e.metaKey || e.ctrlKey) && e.key === "k") {
        e.preventDefault()
        setOpen(o => !o)
      }
      if (e.key === "Escape") setOpen(false)
    }
    window.addEventListener("keydown", handler)
    return () => window.removeEventListener("keydown", handler)
  }, [])

  useEffect(() => { if (open) setTimeout(() => inputRef.current?.focus(), 50) }, [open])

  const filtered = commands.filter(c =>
    c.label.toLowerCase().includes(query.toLowerCase()))

  return (
    <AnimatePresence>
      {open && (
        <motion.div className="fixed inset-0 z-50 flex items-start justify-center pt-[20vh]"
          initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
          <div className="absolute inset-0 bg-black/60 backdrop-blur-sm" onClick={() => setOpen(false)} />
          <motion.div className="relative w-full max-w-xl bg-zinc-900 border border-white/10
            rounded-2xl shadow-2xl overflow-hidden"
            initial={{ scale: 0.95, y: -10 }} animate={{ scale: 1, y: 0 }} exit={{ scale: 0.95, y: -10 }}
            transition={{ duration: 0.15, ease: [0.25, 0.46, 0.45, 0.94] }}>
            <div className="flex items-center gap-3 px-4 py-3 border-b border-white/10">
              <svg className="w-4 h-4 text-zinc-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
              <input ref={inputRef} value={query} onChange={e => setQuery(e.target.value)}
                placeholder="Type a command..." className="flex-1 bg-transparent text-white
                placeholder:text-zinc-500 outline-none text-sm" />
              <kbd className="text-xs text-zinc-500 bg-zinc-800 px-1.5 py-0.5 rounded">esc</kbd>
            </div>
            <ul className="max-h-72 overflow-y-auto p-2">
              {filtered.map(cmd => (
                <li key={cmd.label}>
                  <button onClick={() => { cmd.action(); setOpen(false); }}
                    className="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-sm
                    text-zinc-300 hover:bg-white/10 hover:text-white transition-colors text-left">
                    {cmd.icon && <span className="text-base">{cmd.icon}</span>}
                    <span>{cmd.label}</span>
                    {cmd.shortcut && <kbd className="ml-auto text-xs text-zinc-500">{cmd.shortcut}</kbd>}
                  </button>
                </li>
              ))}
              {filtered.length === 0 && (
                <li className="px-3 py-8 text-center text-sm text-zinc-500">No results found</li>
              )}
            </ul>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  )
}
```

---

## Spotlight Card (cursor glow effect)

```jsx
import { useRef, useState } from "react"

export function SpotlightCard({ children, className = "" }) {
  const divRef = useRef(null)
  const [pos, setPos] = useState({ x: 0, y: 0 })
  const [opacity, setOpacity] = useState(0)

  const handleMouseMove = e => {
    const rect = divRef.current?.getBoundingClientRect()
    if (!rect) return
    setPos({ x: e.clientX - rect.left, y: e.clientY - rect.top })
  }

  return (
    <div ref={divRef} onMouseMove={handleMouseMove}
      onMouseEnter={() => setOpacity(1)} onMouseLeave={() => setOpacity(0)}
      className={`relative overflow-hidden rounded-xl border border-white/10
        bg-white/5 p-6 ${className}`}>
      <div className="pointer-events-none absolute inset-0 transition-opacity duration-300"
        style={{
          opacity,
          background: `radial-gradient(400px circle at ${pos.x}px ${pos.y}px,
            rgba(99,102,241,0.12), transparent 60%)`
        }} />
      {children}
    </div>
  )
}
```

---

## Infinite Marquee

```jsx
import { motion } from "framer-motion"

export function Marquee({ items, speed = 30, direction = "left", pauseOnHover = true }) {
  const duration = items.length * speed

  return (
    <div className="overflow-hidden" style={{ maskImage: "linear-gradient(to right, transparent, black 10%, black 90%, transparent)" }}>
      <motion.div
        className="flex gap-6 w-max"
        animate={{ x: direction === "left" ? ["0%", "-50%"] : ["-50%", "0%"] }}
        transition={{ duration, repeat: Infinity, ease: "linear" }}
        whileHover={pauseOnHover ? { animationPlayState: "paused" } : undefined}>
        {/* Double for seamless loop */}
        {[...items, ...items].map((item, i) => (
          <div key={i} className="flex-shrink-0 px-6 py-3 rounded-full border border-white/10
            bg-white/5 text-sm text-zinc-300 whitespace-nowrap">
            {item}
          </div>
        ))}
      </motion.div>
    </div>
  )
}
```

---

## Animated Accordion

```jsx
import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"

function AccordionItem({ title, content, isOpen, onToggle }) {
  return (
    <div className="border-b border-white/10">
      <button onClick={onToggle}
        className="w-full flex items-center justify-between py-5 text-left
          text-white font-medium hover:text-zinc-300 transition-colors">
        {title}
        <motion.svg animate={{ rotate: isOpen ? 180 : 0 }} transition={{ duration: 0.2 }}
          className="w-4 h-4 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </motion.svg>
      </button>
      <AnimatePresence initial={false}>
        {isOpen && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.25, ease: [0.25, 0.46, 0.45, 0.94] }}>
            <div className="pb-5 text-zinc-400 text-sm leading-relaxed">{content}</div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}

export function Accordion({ items }) {
  const [openIndex, setOpenIndex] = useState(null)
  return (
    <div className="divide-y divide-white/10">
      {items.map((item, i) => (
        <AccordionItem key={i} {...item}
          isOpen={openIndex === i}
          onToggle={() => setOpenIndex(openIndex === i ? null : i)} />
      ))}
    </div>
  )
}
```

---

## Animated Timeline

```jsx
import { useRef } from "react"
import { motion, useInView } from "framer-motion"

function TimelineItem({ event, index }) {
  const ref = useRef(null)
  const inView = useInView(ref, { once: true, margin: "-50px" })

  return (
    <motion.div ref={ref}
      initial={{ opacity: 0, x: index % 2 === 0 ? -30 : 30 }}
      animate={inView ? { opacity: 1, x: 0 } : {}}
      transition={{ duration: 0.5, delay: 0.1, ease: [0.25, 0.46, 0.45, 0.94] }}
      className={`flex gap-8 items-start ${index % 2 === 0 ? "flex-row" : "flex-row-reverse"}`}>
      <div className="flex-1 pb-8">
        <div className="bg-white/5 border border-white/10 rounded-xl p-5">
          <p className="text-xs text-zinc-500 mb-1">{event.date}</p>
          <h3 className="font-medium text-white mb-2">{event.title}</h3>
          <p className="text-sm text-zinc-400">{event.description}</p>
        </div>
      </div>
      <div className="flex flex-col items-center pt-5">
        <div className="w-3 h-3 rounded-full bg-indigo-500 ring-4 ring-indigo-500/20" />
        <div className="w-px flex-1 bg-white/10 mt-2" />
      </div>
      <div className="flex-1" />
    </motion.div>
  )
}

export function Timeline({ events }) {
  return (
    <div className="relative">
      {events.map((event, i) => <TimelineItem key={i} event={event} index={i} />)}
    </div>
  )
}
```

---

## Animated Tabs with Shared Layout

```jsx
import { useState } from "react"
import { motion } from "framer-motion"

export function AnimatedTabs({ tabs }) {
  const [active, setActive] = useState(tabs[0].id)

  return (
    <div>
      <div className="flex gap-1 bg-zinc-900 p-1 rounded-xl w-fit">
        {tabs.map(tab => (
          <button key={tab.id} onClick={() => setActive(tab.id)}
            className={`relative px-4 py-2 text-sm font-medium rounded-lg transition-colors
              ${active === tab.id ? "text-white" : "text-zinc-400 hover:text-zinc-300"}`}>
            {active === tab.id && (
              <motion.div layoutId="active-tab"
                className="absolute inset-0 bg-white/10 rounded-lg"
                transition={{ duration: 0.2, ease: [0.25, 0.46, 0.45, 0.94] }} />
            )}
            <span className="relative z-10">{tab.label}</span>
          </button>
        ))}
      </div>
      <div className="mt-6">
        {tabs.map(tab => active === tab.id && (
          <motion.div key={tab.id}
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            transition={{ duration: 0.2 }}>
            {tab.content}
          </motion.div>
        ))}
      </div>
    </div>
  )
}
```

---

## Glowing Button

```jsx
import { motion } from "framer-motion"

export function GlowButton({ children, onClick, color = "#39ff14" }) {
  return (
    <motion.button onClick={onClick}
      className="relative px-6 py-3 font-semibold text-sm rounded-lg overflow-hidden"
      style={{ background: color, color: "#000" }}
      whileHover={{ scale: 1.02 }}
      whileTap={{ scale: 0.97 }}>
      <motion.div
        className="absolute inset-0 rounded-lg"
        style={{ background: color, filter: "blur(12px)", opacity: 0.5 }}
        animate={{ opacity: [0.4, 0.7, 0.4] }}
        transition={{ duration: 2, repeat: Infinity }} />
      <span className="relative z-10">{children}</span>
    </motion.button>
  )
}
```

---

## Number Counter (on scroll)

```jsx
import { useEffect, useRef, useState } from "react"
import { useInView, useMotionValue, useSpring } from "framer-motion"

export function Counter({ value, suffix = "", prefix = "", duration = 2 }) {
  const ref = useRef(null)
  const inView = useInView(ref, { once: true })
  const mv = useMotionValue(0)
  const spring = useSpring(mv, { duration: duration * 1000, bounce: 0 })
  const [display, setDisplay] = useState(0)

  useEffect(() => { if (inView) mv.set(value) }, [inView, value, mv])
  useEffect(() => spring.on("change", v => setDisplay(Math.floor(v))), [spring])

  return (
    <span ref={ref}>{prefix}{display.toLocaleString()}{suffix}</span>
  )
}

// Usage: <Counter value={12500} prefix="$" suffix="+" />
```

---

## Gradient Text

```jsx
export function GradientText({ children, from = "#39ff14", to = "#7b2fff", className = "" }) {
  return (
    <span className={`bg-clip-text text-transparent ${className}`}
      style={{ backgroundImage: `linear-gradient(135deg, ${from}, ${to})` }}>
      {children}
    </span>
  )
}
```

---

## Card Grid (Bento)

```jsx
export function BentoGrid({ children }) {
  return (
    <div className="grid grid-cols-12 auto-rows-[80px] gap-3">
      {children}
    </div>
  )
}

export function BentoCell({ children, className = "", colSpan = 4, rowSpan = 2 }) {
  return (
    <div className={`col-span-${colSpan} row-span-${rowSpan} bg-white/5 border
      border-white/10 rounded-xl p-5 overflow-hidden ${className}`}>
      {children}
    </div>
  )
}

// Usage:
// <BentoGrid>
//   <BentoCell colSpan={8} rowSpan={4}>Hero cell</BentoCell>
//   <BentoCell colSpan={4} rowSpan={6}>Tall cell</BentoCell>
//   <BentoCell colSpan={4} rowSpan={2}>Small</BentoCell>
// </BentoGrid>
```

---

## Toast Notification

```jsx
import { useState, useEffect } from "react"
import { motion, AnimatePresence } from "framer-motion"

export function Toast({ message, type = "success", duration = 3000, onDismiss }) {
  const colors = { success: "bg-green-500", error: "bg-red-500", info: "bg-blue-500" }

  useEffect(() => {
    const t = setTimeout(onDismiss, duration)
    return () => clearTimeout(t)
  }, [duration, onDismiss])

  return (
    <motion.div
      initial={{ opacity: 0, y: 50, scale: 0.9 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      exit={{ opacity: 0, y: 20, scale: 0.9 }}
      className={`${colors[type]} text-white text-sm font-medium
        px-4 py-3 rounded-xl shadow-lg flex items-center gap-3 min-w-[200px]`}>
      <span>{message}</span>
      <button onClick={onDismiss} className="ml-auto opacity-70 hover:opacity-100">✕</button>
    </motion.div>
  )
}
```
