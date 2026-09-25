---
name: webapp-testing
description: Focused acceptance testing for local web UI changes, including responsive layout, interactions, accessibility basics, browser logs, and resource loading. Reuse project tests and available browser tools first.
license: Complete terms in LICENSE.txt
---

# Web Application Testing

Start with the project's existing test commands and already available browser tools. Use Python Playwright only when its runtime and browser are already installed and it is the best fit. Do not install dependencies or browser binaries automatically; report missing prerequisites and what can still be verified.

**Helper Scripts Available**:
- `scripts/with_server.py` - Starts servers, waits for their ports, runs a command, and attempts cleanup (supports multiple servers).

Run a helper with `--help` first. Inspect its source when platform behavior, readiness, or cleanup matters. Port availability does not establish application readiness; cleanup of child process trees is not guaranteed on every platform. Reuse an existing server when possible and stop only processes started for this task.

## Decision Tree: Choosing Your Approach

```
User task -> Run relevant existing project tests, if available
    -> Choose an already available browser tool or test runner
    -> Static HTML: open the file when supported; no server unless required
    -> Dynamic app: reuse its server, or start the existing project command
       (with_server.py is optional when Python is available)
    -> Inspect the rendered page and identify selectors
    -> Wait for the feature's ready element and required business state
    -> Exercise the changed behavior and verify the visible result
```

## Example: Using with_server.py

When the helper fits the platform and project, run `--help` first. The commands below are examples; use the project's actual package manager, commands, and free ports. Start multiple servers only when the tested flow requires them.

**Single server:**
```bash
python scripts/with_server.py --server "npm run dev" --port 5173 -- python your_automation.py
```

**Multiple servers (e.g., backend + frontend):**
```bash
python scripts/with_server.py \
  --server "cd backend && python server.py" --port 3000 \
  --server "cd frontend && npm run dev" --port 5173 \
  -- python your_automation.py
```

If Python Playwright and its browser are already available, a test can contain only browser logic. Run it against the chosen server:
```python
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    try:
        page = browser.new_page()
        page.goto('http://localhost:5173', wait_until='domcontentloaded')
        # Replace with the inspected feature's ready locator and business state.
        expect(page.get_by_role('main')).to_be_visible()
        # ... exercise the changed behavior and assert its result
    finally:
        browser.close()
```

## Reconnaissance-Then-Action Pattern

1. **Inspect rendered DOM**:
   ```python
   page.screenshot(path='inspect.png', full_page=True)
   content = page.content()
   page.locator('button').all()
   ```

2. **Identify selectors** from inspection results

3. **Execute actions** using discovered selectors

## Common Pitfall

Do not treat `networkidle` as proof that JavaScript, hydration, or business data is ready. Polling and persistent requests may also prevent it from completing. Inspect the page, then use bounded locator assertions or a task-specific data/response condition before the action that depends on it. Fixed sleeps are not readiness checks.

## Focused Acceptance

Scale checks to the change: a small fix needs the affected component or route and its immediate regression path, not a mandatory full-site suite.

- For layout or visual changes, inspect the affected view at one desktop and one phone viewport; check clipping, horizontal overflow, text, controls, and loaded assets. Include an affected breakpoint when relevant.
- Exercise the changed primary interaction and its relevant states, such as loading, empty, error, success, or disabled. Do not create unrelated fixtures or test flows.
- For interactive changes, check keyboard operation and visible focus; for dialogs, check opening, closing, and focus restoration. For motion changes, verify reduced-motion behavior and cleanup after navigation when applicable.
- Check browser console errors, failed requests, and missing fonts/images/scripts during the tested flow; distinguish existing or unrelated noise from regressions.
- Report the actual commands, browser/tool, viewports, and observed results. Name untested checks and blockers explicitly; static inspection or syntax checks are not browser acceptance.

## Best Practices

- Reuse existing project tests and helpers rather than adding a parallel test stack.
- Use `sync_playwright()` when writing an already-supported Python test.
- Close browser sessions you created; do not close the user's existing browser or server.
- Use descriptive selectors: `text=`, `role=`, CSS selectors, or IDs
- Prefer role/label locators and assertions tied to the required state, with bounded timeouts.

## Reference Files

- **examples/** - Optional starting points, not guaranteed ready-to-run tests for the current app. Adapt their URLs, paths, waits, and assertions to the workflow above; do not copy their `networkidle` or fixed sleeps as readiness gates:
  - `element_discovery.py` - Discovering buttons, links, and inputs on a page
  - `static_html_automation.py` - Using file:// URLs for local HTML
  - `console_logging.py` - Capturing console logs during automation
