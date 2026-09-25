# House rules

Applies to every UI shipped with super-design. These override any default a skill or framework suggests.

## Density

- Show the thing, don't describe the thing. No sentence explaining what the next screen does.
- No helper text that restates the label. "Duration" doesn't need "how long the interview runs".
- One line per idea. Word > phrase > sentence. Cut every "you can", "this lets you", "please note".
- No state chatter. Don't narrate counts, selections, or obvious defaults ("0 selected").
- Split, don't stack. Many controls → tabs or progressive disclosure, one group on screen at a time.
- Advanced settings collapse by default.
- Explanations live in tooltips, never in visible helper paragraphs.
- Density benchmark: Google Calendar's quick-event dialog.

## Type

- **Never below `text-sm` (14px).** No `text-xs`, no `text-[11px]`, no uppercase micro-headers.
- If it only fits at a tiny size, there's too much text — cut the text, don't shrink it.

## Assets

- Real names, real logos, real app icons from the repo. Never invent placeholders.
- Don't HTML-escape campaign copy.

## Verification

- A control that renders is not a control that works. Prove the click does something (`verify-ui-actions`).
- Verify in a **focused** browser tab — client UI doesn't hydrate in a background tab.
- Use `127.0.0.1`, not `localhost`, for Playwright/preview in the sandbox.

## Why these exist

A real card once stacked a micro-header, a why-line, a setup paragraph and consent legalese at 11–12px. The verdict: too small, too much text. It should have been one button with a tooltip.

Edit this file to make the rules your own. super-design reads it before every UI task.
