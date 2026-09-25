---
name: openai-image-gen
description: Batch-generate images via OpenAI Images API. Random prompt sampler + `index.html` gallery. 用 OpenAI 兼容 API 批量生图。触发词：生图、批量生图、generate images、openai image、gpt-image。Use when the user wants to render one or more images (game assets, concept art, stickers, posters) through the OpenAI Images API instead of hand-crafting each prompt.
---

# OpenAI Image Gen

Generate a handful of "random but structured" prompts and render them via OpenAI Images API.

## Script location

The generator script lives inside this skill's directory:

- opencode global install: `C:\Users\<user>\<opencode-skills>\openai-image-gen\scripts\gen.py`
- Cline install: `E:\Loser\<cline-skills>\openai-image-gen\scripts\gen.py`

If the path does not exist, locate it with Glob (`**/openai-image-gen/scripts/gen.py`) before running. Do not rely on a cwd-relative path.

## Setup

- Needs env: `OPENAI_API_KEY` (or pass `--api-key`)
- Custom relay (e.g. <your-relay-api>): set `OPENAI_BASE_URL` — the script appends `/v1/images/generations` automatically

## Run

```bash
python3 C:\Users\<user>\<opencode-skills>\openai-image-gen\scripts\gen.py
```

Useful flags:
```bash
python3 C:\Users\<user>\<opencode-skills>\openai-image-gen\scripts\gen.py --count 16 --model gpt-image-1.5
python3 C:\Users\<user>\<opencode-skills>\openai-image-gen\scripts\gen.py --prompt "ultra-detailed studio photo of a lobster astronaut" --count 4
python3 C:\Users\<user>\<opencode-skills>\openai-image-gen\scripts\gen.py --size 1536x1024 --quality high --out-dir ./out/images
```

Always run `--dry-run` first to preview the prompt list and output dir before spending API credits.

## Output

- `*.png` images
- `prompts.json` (prompt > file mapping)
- `index.html` (thumbnail gallery)
