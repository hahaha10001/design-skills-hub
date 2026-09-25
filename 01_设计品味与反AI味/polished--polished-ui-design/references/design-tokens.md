# Design Tokens: Giving the Agent Constraints

Without a design system, AI generates from training-data defaults. Structured
tokens give it a vocabulary and constraints, so it produces consistent,
professional output instead of a patchwork of invented values.

## The three-tier architecture

Build tokens in three tiers, each building on the last. This tells the model not
just *what* value to use, but *why*.

### Tier 1 — Primitives (raw values)

The building blocks. Never referenced directly in components.

```css
/* primitives */
--gray-50: 0 0% 98%;
--gray-900: 0 0% 9%;
--brand-500: 24 95% 53%;
```

```ts
// non-color primitives
export const spacingPrimitives = { scale: [0, 4, 8, 12, 16, 24, 32, 48, 64] } as const;
export const motionPrimitives = {
  ease: [0.16, 1, 0.3, 1] as const,
  duration: { instant: 0.2, short: 0.4, base: 0.6, long: 0.8 },
} as const;
```

### Tier 2 — Semantic (assign purpose)

Give primitives meaning. The model understands intent, not just values. Semantic
names stay the same across light/dark; only the values swap.

```css
:root {
  --background: var(--gray-50);
  --foreground: var(--gray-900);
  --primary:    var(--brand-500);
}
.dark {
  --background: var(--gray-900);
  --foreground: var(--gray-50);
  /* --primary stays the same */
}
```

### Tier 3 — Component (specific contexts, optional)

Add only when a component needs explicit guidance. Don't over-engineer this tier.

```css
--button-primary-bg:   var(--primary);
--button-primary-text: white;
```

## Tailwind + shadcn/ui: the AI-friendly stack

Tailwind classes are self-documenting (`p-4 bg-card border-border`), and
shadcn/ui components are readable TypeScript that live in your repo, so the agent
has full visibility. Map CSS variables to utilities in the config:

```ts
// tailwind.config.ts
export default {
  theme: { extend: { colors: {
    background: 'hsl(var(--background))',
    foreground: 'hsl(var(--foreground))',
    primary: {
      DEFAULT: 'hsl(var(--primary))',
      foreground: 'hsl(var(--primary-foreground))',
    },
  } } },
}
```

Now the agent writes `bg-background text-foreground` once and it works in both
modes — no scattered `dark:` prefixes. If you find yourself writing `dark:` a lot,
your semantic layer is incomplete; add a semantic token instead.

Avoid CSS-in-JS / styled-components with AI where possible: they hide styling
behind JS, making it harder for the model to know which classes to apply.

## Guardrails (so quality holds at scale)

AI generates fast and regresses faster. Automate enforcement:

1. **Lint arbitrary values** — flag `text-[#ff0000]`, `p-[13px]`, etc.
   ```json
   { "rules": { "tailwindcss/no-arbitrary-value": "warn" } }
   ```
2. **Pre-commit checks** — `lint && type-check` before every commit.
3. **Visual regression** (optional) — Chromatic / Percy / screenshot diffs.

## AI-facing docs

Keep a short, scannable design-system doc with copy-pastable examples in the
repo (the model mirrors example structure better than it interprets prose). Keep
rationale out — the model needs constraints and examples, not essays.
