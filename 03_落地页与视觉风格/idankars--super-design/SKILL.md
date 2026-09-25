---
name: super-design
description: Master entry point for ALL UI, UX, visual-design, motion, and frontend-polish work. Knows 65+ design skills and a local reference library (component libraries, real product screens, brand DESIGN.md files, animation kits), picks the right ones, runs them in order, and proves the result in a browser. Use when the user says "super design", or asks to build/redesign/polish/critique a screen, page, dashboard, component, or flow; make something look better, premium, or less AI-generated; add or fix animation; pick a UI library or pattern; or find a real-world example of a good screen. Not for backend or non-UI work.
version: 1.0.0
license: MIT
user-invocable: true
argument-hint: "[build|polish|critique|animate|mobile|refs|verify|find] [target]"
---

# Super Design

You conduct every design skill and the whole `~/Design/` library. Never
freestyle a pattern that a skill or a reference already covers.

## 0. Before anything

1. Read `house-rules.md` next to this file. It outranks every skill below.
2. Read the project's own guide if one exists (`DESIGN.md`, `PRODUCT.md`, a brand guide).
3. Say in one line which skill(s) and which reference(s) you picked, and why.
4. If a skill named below isn't installed, say so and point to
   `https://github.com/idankars/super-design` (`./install.sh`). Never pretend it ran.

Plugin skills show up as `<plugin>:<skill>` (e.g. `accesslint:accessibility-audit`).

## 1. Pick the lane

| The ask | Lane | Start with |
|---|---|---|
| Existing product surface: polish, critique, simplify, harden | System | `impeccable` |
| App screen / dashboard / admin / tool, new | Product UI | `interface-design` + a **screen reference** (§4) |
| Marketing page from nothing | Taste | `design-taste-frontend` (one direction skill only) |
| Motion: add, review, audit | Motion | `animate` / `review-animations` / `improve-animations` |
| Component craft, "why does this feel off" | Craft | `emil-design-eng` |
| Mobile web / native feel | Mobile | `mobile-native` → `apple-design` |
| Comps or brand boards before code | Imagegen | `imagegen-frontend-web` / `brandkit` |
| "Which library?" | Library | `pick-ui-library` + §4 table |
| "Show me a good example of X" | Find | §4, then `rg` in `~/Design/references` |
| Does it work / look right? | Verify | §6, always last |

Chains are fine (Taste → Motion → Verify). Two skills in the same lane never run together.

## 2. Full skill roster

### Direction and taste (pick exactly ONE per surface)
| Skill | When |
|---|---|
| `impeccable` | Default for anything existing. `/impeccable critique`, `audit`, `polish`, `distill`, `clarify`, `typeset`, `layout`, `colorize`, `bolder`, `quieter`, `delight`, `harden`, `optimize`, `live`, `init`, `document`, `extract`. Its hook scans every UI edit: fix findings, never silence them. |
| `design-taste-frontend` | Greenfield marketing: landing, portfolio. Infers direction from brief. |
| `high-end-visual-design` | Explicit "expensive / agency-grade". |
| `minimalist-ui` | Editorial, calm, warm monochrome. |
| `industrial-brutalist-ui` | Brutalist, terminal, blueprint. |
| `gpt-taste` | Only on explicit ask for heavy GSAP scroll choreography. |
| `redesign-existing-projects` | Upgrading a site with no Impeccable context. |
| `stitch-design-taste` | Writing a `DESIGN.md` for Google Stitch. |
| `frontend-design` | Distinctive aesthetic direction and typography choices. |
| `bencium-innovative-ux-designer:bencium-innovative-ux-designer` | Creative, non-templated components. |
| `design-taste-frontend-v1` | Only for backward compatibility. |

### Product UI and systems
| Skill | When |
|---|---|
| `interface-design` | Dashboards, admin panels, apps, tools. Not marketing. |
| `ui-ux-pro-max` | Lookup DB: 67 styles, 96 palettes, 57 font pairs, per-stack rules (`data/stacks/`). Use for palette / font / chart choice. |
| `ui-refactor` | Tactical fixes: spacing, color, hierarchy, "make this look better". |
| `design:design-system` | Audit, document, or extend a design system. |
| `design:design-handoff` | Dev handoff specs: tokens, props, states, breakpoints. |
| `design:ux-copy` | Microcopy, errors, empty states, CTAs. |
| `design:design-critique` | Structured critique of a mockup or screenshot. |
| `theme-factory` | Apply or generate a theme for an artifact, slides, or doc. |
| `artifact-design` / `dataviz` | Claude app only (built in, not installable): Artifact pages, charts. Use when present. |
| `design-system` | Three-layer tokens (primitive → semantic → component), component specs, token validators. |
| `ui-styling` | shadcn + Tailwind implementation: add components, generate Tailwind config, dark mode. |
| `slides` | HTML decks with Chart.js and tokens. |

### Motion and craft (additive: layers on any direction)
`emil-design-eng` (component craft) · `animate` (build web motion) ·
`animate-expo` (React Native / Reanimated) · `review-animations` (critique a diff) ·
`improve-animations` (codebase audit, read-only) · `find-animation-opportunities`
(what should move, read-only) · `animation-vocabulary` (name a vague effect) ·
`vercel-react-view-transitions` (page/route transitions) · `apple-design` (springs,
gestures, sheets) · `mobile-native` (installed-app feel) · `ask-sonner` (toasts) ·
`prototype` (several variants, flip between them) · `pick-ui-library`.

### Imagegen and brand (needs an image model; if none, say so and go to code)
`imagegen-frontend-web` (one comp per section) · `imagegen-frontend-mobile` ·
`image-to-code` (comp then build to match) · `brandkit` · `ad-creator` ·
`canvas-design` (posters, static art) · `algorithmic-art` (p5.js) · `hdr-glow:hdr-glow` (logos that glow on HDR screens) ·
`design` (logos, CIP, icons, social images; needs GEMINI / ATLASCLOUD / MUAPI key) ·
`banner-design` (social, ads, hero, print banners) · `ad-creator` (9:16 social ads, non-English text done right) · `brand` (voice, identity,
`docs/brand-guidelines.md` → tokens sync).

### Conversion flows
`landing-page-optimizer` · `cro` · `signup` · `onboarding`.

### Implementation
`vercel-react-best-practices` · `vercel-composition-patterns` · `vercel-react-native-skills` ·
`web-artifacts-builder` · `write-swift` · `full-output-enforcement` (only when
complete untruncated code is required).

### Review, accessibility, verification
`web-design-guidelines` · `design:accessibility-review` · `accesslint:accessibility-audit` ·
`accesslint:accessibility-scan` · `accesslint:accessibility-diff` (new violations only) ·
`accesslint:accessibility-fix` · `verify-ui-actions` (does the click DO something) · `webapp-testing`.

### Research
`design:user-research` · `design:research-synthesis`.

## 3. Precedence

- One direction skill per surface. Name the one you picked and what you rejected.
- Existing product beats generic taste: repo has a `DESIGN.md`, brand guide, or component library → `impeccable`, and build with what's installed.
- Motion is additive, never competing.
- Read-only first on existing surfaces: `critique` / `audit` / `improve-animations` before editing.
- House rules and project guide break every tie.

## 4. Reference library

Location: `$SUPER_DESIGN_REFS`, else `~/.super-design/references` (or `~/Design/references`
if that exists). Local copies of the best UI repos: read them instead of guessing, and
`rg` across them for any pattern. Every folder has a `SOURCE.md`. Missing? Run
`scripts/fetch-references.sh` from the super-design repo.

**License rule: study, don't paste.** `coss/`, `midday/`, `twenty/` are AGPL (or AGPL-style);
`tailwind/`, `motion/`, `react-bits/` have no or custom terms. Learn the
pattern from them and write your own code. Copy code only from MIT/Apache references:
shadcn, base-ui, radix, react-aria, mantine, mui, heroui, magicui, motion-primitives, sonner, vaul, cmdk, lucide, vercel-chatbot, design-md.


**How a component must behave (headless, a11y)**
| Folder | Use for |
|---|---|
| `base-ui/` | shadcn's default backend; prop contracts, handbook |
| `react-aria/` | deepest interaction/a11y source: selection, dnd, i18n |
| `radix/` | primitives + themes + the 12-step color scale |

**Built component libraries**
| Folder | Use for |
|---|---|
| `shadcn/` | default choice, all 3 backends |
| `coss/` | Cal.com's system: `docs/`, `registry/` (580 real components), `skills/` |
| `mantine/` | fullest feature set: forms, dates, tables, hooks |
| `heroui/` | polished-by-default look (v3) |
| `mui/` | Material UI docs for enterprise patterns |
| `material-web/` | why token systems are shaped the way they are |
| `tailwind/` | v4 utilities and `@theme` tokens |

**Real product screens (study before building an app screen)**
| Folder | Screens |
|---|---|
| `twenty/` | CRM at Linear level: `twenty-ui/` components, `design-tokens/`, `ui-docs/` |
| `midday/` | finance app: `dashboard/` (521 screen components: tables, settings, bulk actions, skeletons), `ui/` |
| `shadcn-admin/` | clean admin: `features/` (users, tasks, settings, auth), layout shell |
| `vercel-chatbot/` | AI chat UI: messages, streaming, artifacts, sidebar |

**Brand design systems as DESIGN.md**
`design-md/<brand>/DESIGN.md`: 74 brands (linear.app, stripe, vercel, notion,
raycast, superhuman, apple, airbnb, figma, cursor, claude, resend, supabase...).
Use to pin a direction ("Linear-like") or feed a `DESIGN.md`.

**Motion and wow**
| Folder | Use for |
|---|---|
| `motion/` | Motion (Framer Motion) official skill + `llms.txt` |
| `motion-primitives/` | `components/` 33 motion components + `docs/` usage |
| `magicui/` | `components/` 79 animated components, `docs/`, `skill/` |
| `react-bits/` | 200+ animated text/background/component effects (TS + Tailwind) |

**Small parts that make it feel finished**
`sonner/` toasts · `vaul/` mobile drawers · `cmdk/` ⌘K menu (+ `ARCHITECTURE.md`) · `lucide/` icons.

**Skill sources and lists**
`taste-skill-research/` (why AI output
turns lazy) · `awesome-lists/` (design resources, 200+ design systems, shadcn ecosystem).

Search examples:
```bash
R=${SUPER_DESIGN_REFS:-~/.super-design/references}
rg -l "DataTable" $R/{midday,twenty,shadcn-admin}
rg -il "empty state" $R
cat $R/design-md/linear.app/DESIGN.md
```

## 5. Standard pipelines

**New app screen**: house rules → `interface-design` → read 1-2 screen references
(§4) for the same screen type → build with the project's components → `impeccable audit` → Verify.

**New marketing page**: `design-taste-frontend` (or named direction) → optional
`design-md/<brand>` as anchor → build → `animate` for the 2-3 moments that earn it
→ `impeccable audit` → Verify.

**Existing surface feels off**: `impeccable critique` → `impeccable polish` →
`review-animations` if motion is involved → Verify.

**"Looks AI-generated"**: `npx impeccable detect <paths>` → `impeccable quieter`
or `distill` → direction skill only if the whole direction is wrong.

**Motion audit**: `improve-animations` → execute with `animate` → `review-animations`.

**Mobile web wrong**: `mobile-native` → `apple-design` → Verify at 375px.

**Brand-new product**: `brandkit` or `imagegen-frontend-web` → build →
`impeccable init` + `document`.

## 6. Verify (mandatory, last)

1. A real browser: Claude's built-in browser, Playwright MCP, or `webapp-testing`.
2. `127.0.0.1`, not `localhost`. Focused tab only (UI won't hydrate in background).
3. Click every control (`verify-ui-actions`). Check 375px, dark mode, empty/error/loading.
4. `accesslint:accessibility-scan` or `design:accessibility-review` for a11y.
5. Attach screenshot / snapshot / console output. "I changed X" is not "X works".
