---
name: polished-ui-design
description: >-
  Guides an agent to generate polished, professional web UI that avoids the
  generic "AI slop" / "vibe coded" look. Use when building, reviewing, or
  refining any frontend interface, landing page, dashboard, or component —
  especially when the goal is a distinctive, brand-appropriate design rather
  than a generic template. Covers a design-system-first workflow, concrete
  anti-patterns to avoid, and an effective prompting loop.
---

# Polished UI Design

A workflow for producing web interfaces that look intentionally designed rather
than machine-generated. The core idea: AI defaults to the statistical average of
its training data (purple gradients, Inter, glowing cards). Good design is the
opposite of average — it makes specific, constrained choices. This skill gives
the agent the constraints and judgment to get there.

## When to use this skill

Activate this skill whenever you are:

- Building a new frontend (landing page, dashboard, app screen, marketing site)
- Creating or refactoring UI components
- Reviewing existing UI for quality issues
- Refining a design that "feels off" or generic

## The core principle

> Vibe-coded UI looks like *everything* because it was trained on everything.
> It has no point of view. Good design makes deliberate choices about what to
> emphasize and what to leave out.

Every visual decision should trace back to **the product, the user, and the
brand** — not to "what modern UI looks like."

## Workflow

Follow these steps in order. Do not skip step 1.

### 1. Establish constraints BEFORE generating (design-system-first)

Never prompt from zero. Before writing any component, define the minimum design
context. If the project has no design system, create one first. The minimum is:

1. **Color palette** — one dominant color, one accent, one neutral scale.
   Derived from brand/product, not a default gradient.
2. **Spacing scale** — a fixed scale (e.g. 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64).
   No arbitrary values.
3. **Type scale** — a limited set of sizes/weights, and a deliberate font choice
   (not reflexively Inter).
4. **One reference component** that uses these tokens correctly.

Encode these as tokens (CSS variables + a tokens file). See
`references/design-tokens.md` for a concrete three-tier token architecture.

### 2. Generate against the constraints

When generating UI, always supply: the tokens, the relevant framework config,
and a visual reference (screenshot/link) if one exists. Use the prompt template
in `references/prompting.md`. Be specific about what "good" means for *this*
product; "make it look modern" reverts the model to training-data defaults.

### 3. Critique against the anti-pattern checklist

After generating, review the output against `references/anti-patterns.md`. If any
of the tells are present, fix them — do not ship the first output. This critique
step is what separates designed UI from vibe-coded UI.

### 4. Add guardrails so quality holds

For ongoing projects, add automated guardrails (lint rules against arbitrary
values, pre-commit checks) so the 10th component stays as consistent as the
first. See `references/design-tokens.md`.

## Quick self-check before shipping

- [ ] Is there ONE clear dominant color, not 5 competing neon accents?
- [ ] Does every color/effect communicate hierarchy or state — nothing purely decorative?
- [ ] Are cards reserved for genuinely independent/interactive blocks, not everything?
- [ ] Is spacing from the scale (no `p-[13px]`)?
- [ ] Are icons a consistent set (not random emojis as UI chrome)?
- [ ] Do status dots / badges map to a defined, labeled state?
- [ ] Would this look at home for *this* brand, or could it be any AI product?

## Reference files

- `references/anti-patterns.md` — the specific visual tells of AI-generated UI and how to fix each.
- `references/design-tokens.md` — three-tier token architecture (primitives → semantic → component), Tailwind + shadcn/ui integration, and guardrails.
- `references/prompting.md` — an effective, iterative prompting loop and a reusable prompt template.

## Sources

This skill synthesizes guidance from:

- Google / Firebase Studio effective prompting docs — <https://firebase.google.com/docs/studio/prompting>
- Google Stitch AI UI design — <https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/>
- "7 Signs a UI Has Been Vibe Coded" (The Fountain Institute) — <https://www.thefountaininstitute.com/blog/signs-vibe-coded-ui>
- "Design Systems for AI Coding: Stop Getting Purple Gradients" (BrainGrid) — <https://www.braingrid.ai/blog/design-system-optimized-for-ai-coding>

Content from these sources was rephrased for compliance with licensing restrictions.
