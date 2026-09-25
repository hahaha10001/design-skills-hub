---
name: grok-cli
description: Run Grok CLI headless for real-time X/Twitter and news research. Use when the user says "use grok", "ask grok", "dig into twitter/x", "latest on...", or when fresh data past the training cutoff is needed.
license: Apache-2.0
---

# grok-cli — fresh info via the Grok CLI

`grok` is xAI's installed CLI (`~/.grok/bin/grok`, already authenticated). Use it as a sub-agent to fetch **real-time** info: X/Twitter chatter and news beyond this model's knowledge. It is slow but live.

## Do this immediately

When this skill triggers, **run the command right away.** Do not run `--help`, `--version`, `which grok`, or any discovery — it works, the recipe below is verified.

### The one command (copy, fill the prompt)

```bash
grok -p "<your question>" -m grok-build --yolo --max-turns 8 --disallowed-tools web_fetch --output-format json | jq -r '.text'
```

That is the whole interface. Only the `<your question>` changes.

- `-m grok-build` uses the Grok model (not the composer model).
- `--yolo` auto-approves grok's tools (required headless, or it hangs).
- `--disallowed-tools web_fetch` forces grok onto `web_search` (xAI live search). This is the key fix: with `web_fetch` enabled grok loops on X/news URLs and never returns.
- `--max-turns 8` caps it so it can't loop forever.
- `jq -r '.text'` returns just the answer. Drop `| jq ...` if `jq` is missing and read the JSON `text` field yourself.

### Timing (important)

A live search takes ~1–3 minutes. **Set the Bash timeout to 300000 ms (5 min)** and wait. Do not assume it failed. If you may keep working meanwhile, run it in the background and poll later.

## Prompt templates

**Dig deep into X/Twitter** — be explicit, ask for specifics:

```bash
grok -p "Search X/Twitter for the latest discussion about <TOPIC> (last 24-72h). Surface 5-8 specific posts: @handle, a one-line summary, and the post URL. Quote standout lines. Then give prevailing sentiment, the most influential accounts driving it, and any emerging angle. Be specific, no filler." \
  -m grok-build --yolo --max-turns 10 --disallowed-tools web_fetch --output-format json | jq -r '.text'
```

**News / live web research:**

```bash
grok -p "What's the latest on <TOPIC> as of this week? Give 3-5 key developments, each one line with a source link, then a 2-sentence takeaway." \
  -m grok-build --yolo --max-turns 8 --disallowed-tools web_fetch --output-format json | jq -r '.text'
```

## Good prompting

- Ask for **concrete output**: handles, URLs, quotes, dates, sentiment — not vague summaries.
- State the **time window** ("last 48h", "this week").
- One focused question per call. For a different angle, make a second call.
- Keep `<your question>` as a single double-quoted string; escape inner quotes or use single quotes inside.

## Follow-ups (same grok session)

Capture the session id, then continue for cheaper, context-aware follow-ups:

```bash
SID=$(grok -p "<first question>" -m grok-build --yolo --max-turns 8 --disallowed-tools web_fetch --output-format json | jq -r '.sessionId')
grok -p "<follow-up>" --resume "$SID" -m grok-build --yolo --max-turns 8 --disallowed-tools web_fetch --output-format json | jq -r '.text'
```

## After you get results

Treat grok's output as a fresh source: summarize it for the user and **keep the source links/@handles** so they can verify. Note it's live data (may be noisy or unverified). If it returns empty or errors, retry once with a tighter prompt or a longer timeout before giving up.

## Notes

- This skill uses `-m grok-build` (the Grok model). `grok-composer-2.5-fast` is the CLI default but the composer model is not what we want here.
- For richer general web research (not X-specific), prefer the existing Exa tooling per global rules; reach for `grok` when you specifically want X/Twitter or want xAI's live take.
- Requires the `grok` CLI installed and authenticated (`curl -fsSL https://x.ai/cli/install.sh | bash`, then `grok login`) and `jq` on PATH.
