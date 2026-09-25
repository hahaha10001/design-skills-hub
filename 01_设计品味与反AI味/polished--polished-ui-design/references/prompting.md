# Effective Prompting for UI Generation

How you prompt determines what you get. Vague prompts ("make it modern") revert
the model to training-data defaults. Structured, constrained prompts produce
on-brand results on the first try.

## Principles

- **Be specific.** Define features, interactions, and data. Name technologies
  where it helps (e.g. "use three.js for the 3D element").
- **Provide context.** State the product's purpose, audience, and the experience
  you want.
- **Use examples & references.** A screenshot or reference URL constrains the
  output far more than adjectives.
- **Iterate.** Start basic, test, refine, then add the next feature — one change
  per request. Don't ask for ten things at once.
- **Ask the model to reason** when stuck: "Think step by step..."
- **Use domain keywords** the model associates with the output you want (e.g.
  "Material Design" for Google design standards) — but only when they match the
  brand you actually want.

## The prompt template

Supply all three inputs — tokens, config, and a visual reference. Skipping any
sends the model back to guessing.

```
## Context
- Design system tokens: [paste tokens or link to file]
- Framework config:      [paste relevant Tailwind/theme config]
- Visual reference:      [screenshot or link]

## Task
Build a [component/screen] that:
- Uses only colors from our token palette
- Follows our spacing scale (4 / 8 / 16 / 24 / 32)
- Matches the visual reference layout

## Constraints
- No arbitrary values (no text-[#hex] or p-[13px])
- Use semantic tokens (text-foreground, not text-gray-900)
- Follow existing component patterns in /components/ui
- Apply the polished-ui-design anti-pattern checklist

## Output
Single file with the component, including all imports.
```

## Refining when the result is off

- **Add constraints** on UI, data model, or layout.
- **Add counter-examples** if the model is making a wrong assumption.
- **Ask for one specific change at a time** rather than "improve it."
- **Reset context** (new session) if the model is stuck in a loop or carrying a
  bad assumption.

## Debugging generated code

- Describe the observed behavior *and* the error, clearly and concisely.
- Ask direct, specific questions ("What could cause this null reference here?").
- Break complex issues into smaller parts and solve them separately.
- Rephrase the prompt if the model loops; provide additional context.
