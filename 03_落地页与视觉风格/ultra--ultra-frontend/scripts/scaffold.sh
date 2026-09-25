#!/bin/bash
# ultra-frontend scaffold
# Usage: bash scripts/scaffold.sh <project-name> <stack>
# Stacks: html | react | next | vue | svelte

NAME=${1:-"my-project"}
STACK=${2:-"html"}

echo "🚀 ultra-frontend scaffold: $NAME ($STACK)"

case $STACK in
  html)
    mkdir -p "$NAME"
    cat > "$NAME/index.html" << 'HTMLEOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PROJECT_NAME</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.14/dist/ScrollTrigger.min.js"></script>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --bg: #0a0a0f; --surface: #12121a; --surface-2: #1a1a26;
      --border: rgba(255,255,255,0.08); --border-hover: rgba(255,255,255,0.15);
      --accent: #39ff14; --accent-2: #7b2fff; --accent-glow: rgba(57,255,20,0.25);
      --text: #e8e8f0; --text-muted: #6b6b80;
      --font: 'Plus Jakarta Sans', sans-serif;
      --mono: 'JetBrains Mono', monospace;
      --radius: 8px; --radius-lg: 16px;
    }
    body { background: var(--bg); color: var(--text); font-family: var(--font); line-height: 1.6; overflow-x: hidden; }
    h1 { font-size: clamp(2.5rem, 8vw, 7rem); line-height: .9; letter-spacing: -.02em; }
    h2 { font-size: clamp(1.75rem, 5vw, 3.5rem); line-height: 1.05; }
    p  { font-size: clamp(1rem, 2vw, 1.125rem); }
    .container { max-width: min(1200px, 90vw); margin-inline: auto; }
    .section { padding-block: clamp(4rem, 10vw, 10rem); }
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; }
    }
  </style>
</head>
<body>
<svg style="position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:9997;opacity:0.04" xmlns="http://www.w3.org/2000/svg">
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
  <rect width="100%" height="100%" filter="url(#grain)"/>
</svg>

<nav id="nav" style="position:fixed;inset:0 0 auto;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:1.5rem 2rem;transition:padding .3s,background .3s,transform .3s;">
  <div style="font-weight:700;font-size:1.1rem;">PROJECT_NAME</div>
  <div style="display:flex;gap:2rem;">
    <a href="#features" style="color:var(--text-muted);text-decoration:none;">Features</a>
    <a href="#about" style="color:var(--text-muted);text-decoration:none;">About</a>
  </div>
</nav>

<main>
  <section class="section container" style="min-height:100vh;display:flex;flex-direction:column;justify-content:center;">
    <p class="reveal" style="color:var(--accent);font-size:.875rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;margin-bottom:1.5rem;">Your tagline here</p>
    <h1 class="reveal">Your Headline<br><span style="color:var(--text-muted);">That Ships</span></h1>
    <p class="reveal" style="color:var(--text-muted);max-width:520px;margin-top:1.5rem;">
      Supporting copy that sells the vision clearly.
    </p>
    <div class="reveal" style="margin-top:2.5rem;display:flex;gap:1rem;">
      <button class="mag-btn" style="padding:.875rem 2rem;background:var(--accent);color:#0a0a0f;border:none;border-radius:var(--radius);font-weight:600;font-size:1rem;cursor:pointer;">
        Get started →
      </button>
      <button style="padding:.875rem 2rem;background:transparent;color:var(--text);border:1px solid var(--border);border-radius:var(--radius);font-weight:500;font-size:1rem;cursor:pointer;">
        Learn more
      </button>
    </div>
  </section>
</main>

<script>
gsap.registerPlugin(ScrollTrigger);
gsap.utils.toArray('.reveal').forEach(el => gsap.from(el, { scrollTrigger:{trigger:el,start:'top 88%'}, y:40, opacity:0, duration:.75, ease:'power3.out' }));
gsap.utils.toArray('.stagger').forEach(p => gsap.from(p.children, { scrollTrigger:{trigger:p,start:'top 85%'}, y:30, opacity:0, duration:.6, stagger:.1, ease:'power3.out' }));
document.querySelectorAll('.mag-btn').forEach(btn => {
  btn.addEventListener('mousemove', e => {
    const r = btn.getBoundingClientRect();
    gsap.to(btn, { x:(e.clientX-r.left-r.width/2)*.35, y:(e.clientY-r.top-r.height/2)*.35, duration:.4, ease:'power3.out' });
  });
  btn.addEventListener('mouseleave', () => gsap.to(btn, { x:0, y:0, duration:.7, ease:'elastic.out(1,.5)' }));
});
let lastY=0;
window.addEventListener('scroll',()=>{
  const nav=document.getElementById('nav'),y=window.scrollY;
  nav.style.transform=y>lastY&&y>200?'translateY(-100%)':'translateY(0)';
  nav.style.background=y>80?'rgba(10,10,15,.9)':'transparent';
  nav.style.backdropFilter=y>80?'blur(20px)':'none';
  nav.style.padding=y>80?'.75rem 2rem':'1.5rem 2rem';
  lastY=y;
},{passive:true});
</script>
</body>
</html>
HTMLEOF
    sed -i "s/PROJECT_NAME/$NAME/g" "$NAME/index.html"
    echo "✅ HTML project scaffolded: $NAME/"
    echo "   Open $NAME/index.html to start"
    ;;

  react)
    echo "Running: npm create vite@latest $NAME -- --template react"
    npm create vite@latest "$NAME" -- --template react 2>/dev/null || echo "(run npm create vite manually if npm not available)"
    echo ""
    echo "Next steps:"
    echo "  cd $NAME"
    echo "  npm install"
    echo "  npm install framer-motion gsap @gsap/react lucide-react"
    echo "  npx shadcn@latest init"
    echo "  npm run dev"
    ;;

  next)
    echo "Running: npx create-next-app@latest $NAME --tailwind --app --src-dir"
    echo ""
    echo "Then install:"
    echo "  npm install framer-motion gsap @gsap/react lucide-react"
    echo "  npx shadcn@latest init"
    ;;

  vue)
    echo "Running: npm create vue@latest $NAME"
    echo ""
    echo "Then install:"
    echo "  npm install @vueuse/motion gsap"
    ;;

  svelte)
    echo "Running: npm create svelte@latest $NAME"
    echo ""
    echo "Then install:"
    echo "  npm install gsap"
    ;;

  *)
    echo "Unknown stack: $STACK"
    echo "Available: html | react | next | vue | svelte"
    exit 1
    ;;
esac

echo ""
echo "📁 ultra-frontend skill active. Reference files:"
echo "   references/aesthetics.md     — design tokens, fonts"
echo "   references/gsap.md           — GSAP plugin cookbook"
echo "   references/components.md     — React + framer-motion patterns"
echo "   references/uiux-rules.md     — UX rules + accessibility"
echo "   references/component-library.md — 21st.dev components"
