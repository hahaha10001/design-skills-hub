---
name: verify-ui-actions
description: Verify that interactive UI actions actually DO something - not just that the page renders. Use this whenever you add or fix a button, form, menu item, drag action, or any control that triggers a write/navigation/state change; whenever a user reports "I clicked X and nothing happened" / "it's not working" / "didn't save"; and as the UI layer of any QA pass. Guards against shipping controls that render fine but are inert (no handler), or handlers that swallow failures.
---

# Verify UI actions actually work

## The trap this prevents

**"Renders" is not "works."** An HTTP 200, a passing build, green unit tests, an accessibility snapshot, and even a screenshot all prove the page *loaded*. None of them prove a button *does anything*. A `<button>` with no `onClick` renders pixel-perfect and is completely dead.

Canonical failure: a review workspace shipped a **Reject** button — plus Advance / Schedule / Message — as `<button type="button">` with **no handler at all**. Clicking did nothing. It passed ESLint, `tsc`, the unit suite, and a 200 smoke-check, because the *page* was fine. A change that added an "Archive" tab + counts was even built on top of reject "working" and declared done — verified by fetching route HTML (200) and never once clicking the button. The user's report: *"the user rejected someone and nothing happened."*

The lesson: **if a turn's deliverable is a user action, the verification must exercise that action and assert the resulting state change.** If you literally cannot, you must say so out loud instead of implying it works.

## Do this — every time you touch an interactive control

### 1. Static check: no dead controls
Run the scanner (it flags `<button>`s with an action label but no `onClick` / `type="submit"` / forwarded handler):

```
node scripts/find-dead-controls.mjs src --strict
```

If the repo has no `scripts/find-dead-controls.mjs`, use the copy bundled with this skill:

```
node ~/.claude/skills/verify-ui-actions/scripts/find-dead-controls.mjs src --strict
```

It must exit 0. A real, intentionally-inert control (e.g. a preview mockup) is opted out with a `find-dead-controls-ignore` comment on/above the tag - use that sparingly and only when the inertness is the point.

### 2. Behavioral check: exercise the action, assert the STATE CHANGE
Prove the effect, not the render. For each action, confirm the thing it's supposed to change actually changed:
- **reject/withdraw/move/advance** → the application's `status`/`current_stage` changed; the candidate left the active list and the count dropped; it appears where it should (Archive / Disqualified).
- **save/edit** → re-read the row and confirm the new value persisted (see the Save Standard below).
- **navigation/tab** → the destination/tab actually changed.

Ways to exercise, best first:
- **Click it for real** in a hydrated browser (preview/PR-preview/staging) and observe the result + the network call + the DB/read-back.
- If the headless preview won't hydrate (some app shells render but never attaches handlers - clicks no-op for *every* button, including pre-existing ones), drive the **exact endpoint the handler calls** and read the state back. Note this proves the data flow, not the literal click binding - call that out.
- Where a non-prod DB is available, mutate + restore. **Do not write to production data without explicit user authorization** (the sandbox blocks it by default, and you should respect that).

### 3. Client writes go through the Save Standard
Never hand-roll `fetch(...).then(r => { if (r.ok) ... })` for a write - that's how "said saved, didn't save" ships. Use a wrapper that fails loudly (or the project's equivalent). It should throw on any non-2xx or network failure, so a failed action can't masquerade as success. Surface the error and keep the user's input; only say "done/saved" after a confirmed 2xx.

## When you CANNOT fully verify - say so, don't imply

If hydration, missing test infra (e.g. no React Testing Library in the repo), or a production-write block prevents you from exercising the action in the sandbox, your report MUST distinguish what you verified from what you didn't. Use plain language:

> Verified: handler is wired (code), lint/tsc clean, the endpoint + `saveResource` are tested, the data flow works via direct API call.
> NOT verified: the literal in-browser click→effect (headless preview doesn't hydrate here). Please click it on the PR preview / staging, or authorize a non-prod test.

Never write "verified working" / "QA'd" / "done" for an action whose effect you never observed. Offer the user a concrete way to close the gap (PR preview, staging, granting write access).

## Quick checklist
- [ ] `node scripts/find-dead-controls.mjs src --strict` exits 0
- [ ] Every new/changed control has a handler (or is a real form submit)
- [ ] Writes go through a throw-on-failure save wrapper; failure surfaces + input preserved
- [ ] The action's STATE CHANGE was observed (clicked, or endpoint-driven + read back) — or the gap is explicitly reported
- [ ] Terminal/disabled states handled (don't offer Reject on an already-rejected row, etc.)
