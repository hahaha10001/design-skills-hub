---
name: ad-creator
description: Generate static social-media ad images (Reels/TikTok/Instagram 9:16) for a brand using OpenAI gpt-image-1 or Gemini 2.5 Flash Image. Handles English and non-English ad copy correctly — knows which model wins for which script, how to phrase prompts, when to retry, and when to fall back to PIL text compositing. Trigger with "create an ad", "generate ad images", "design a social ad", or any request for static social-media ad creative.
---

# ad-creator — static social ad image generator

You generate **finished, ship-ready vertical 9:16 social ads** as PNGs. The user gives you a concept (or asks you to invent one); you produce the image, open it, and grade it.

## The two models — and when to use which

| Model | Strength | Weakness |
|---|---|---|
| **OpenAI `gpt-image-1`** | Renders **non-Latin scripts** (Hebrew, Arabic) far better than Gemini. ~30–60s per image. ~$0.20 each at high quality. | Slower. Stochastic on RTL text — needs 2–3 retries. Bills against OpenAI hard limit. |
| **Gemini `gemini-2.5-flash-image`** | Fast (~7s). Cheap. Excellent on **Latin-script** languages (English, French, Spanish, German). | **Scrambles Hebrew, Arabic, and other complex scripts** every single time. Even renders Italian with typos sometimes. |

**Rule:** Latin script → Gemini. Non-Latin script → OpenAI (with retries). When in doubt, OpenAI.

## The recipe that wins for non-English ads

1. **Prompt entirely in the target language.** Don't write the prompt in English with Hebrew strings embedded — you get gibberish. Write the whole prompt in Hebrew/Arabic/French/etc., including all instructions to the model. This was the single biggest accuracy unlock in testing.
2. **Keep target-language text SHORT.** A 3-word headline succeeds first try. A 6-word headline with subline often scrambles letters. Each extra word multiplies failure odds. Trim ruthlessly.
3. **Render numerals and brand name in Latin.** "$3,000", "ב-90 שניות", "{brand}" — Latin digits and Latin wordmarks render perfectly even in RTL ads. Don't translate "{brand}" or numbers.
4. **Generate 2–3 attempts in parallel** for non-Latin (it's stochastic). Use `concurrent.futures.ThreadPoolExecutor`. Pick the cleanest after.
5. **Add a "do not invent letters / do not duplicate" instruction** in the target language. Helps a little, not a lot.
6. **If accuracy is critical** (paid media, client deliverable): use the **PIL fallback** — generate a text-free scene via Gemini, composite Hebrew/Arabic/etc. typography with Pillow + the brand font (Heebo for HE, Cairo for AR, Inter for Latin). 100% accurate text every time. See the fallback section below.

## Empirical accuracy (tested 2026-04-30, 9-language matrix)

| Language | Script | Best model | First-try result | Notes |
|---|---|---|---|---|
| English | Latin | Gemini | ✅ Perfect | Default winner |
| German | Latin (umlauts, ß) | Gemini | ✅ Perfect | "Gratis-Video" rendered cleanly |
| Portuguese | Latin (accents, ç) | Gemini | ✅ Perfect | All diacritics correct |
| French | Latin (accents) | Gemini | ✅ Perfect | All accents correct |
| Russian | **Cyrillic** | Gemini | ✅ Mostly correct | Headline+CTA perfect; minor case-ending grammar error in subline. Cyrillic works on Gemini. |
| Spanish | Latin (accents, ñ) | Gemini | ⚠️ Headline typo | "SECUNDOS" instead of "SEGUNDOS" — retry usually fixes |
| Italian | Latin (accents) | Gemini | ⚠️ Two typos | "pubblicà" / "seconid" — Gemini struggles with Italian word endings; retry or PIL |
| Hebrew | **RTL non-Latin** | **OpenAI** | ⚠️ ~30% / attempt | Gemini scrambles every attempt. OpenAI works with 2-3 parallel retries. Shorter text → much higher hit rate. |
| Arabic | **RTL non-Latin** | **OpenAI (predicted)** | ❌ on Gemini | Gemini scrambles 100%. Same RTL non-Latin failure mode as Hebrew — OpenAI expected to work (untested due to billing cap during matrix run). |
| Chinese (Simplified) | **CJK** | **OpenAI** | ✅ Perfect first try | Gemini gibberish; OpenAI nailed headline + subline + CTA. |
| Japanese | **CJK + kana** | **OpenAI** | ✅ Perfect first try | Gemini broken; OpenAI rendered kanji + hiragana + katakana correctly. |
| Korean | **Hangul** | **OpenAI** | ✅ Perfect first try | Gemini scrambled headlines; OpenAI clean. |
| Hindi | **Devanagari** | **OpenAI** | ✅ Perfect first try | Gemini scrambled every word; OpenAI rendered conjuncts and matras correctly. |
| Spanish | Latin | **OpenAI** (or Gemini + retry) | ✅ OpenAI perfect first try | Gemini typo'd "SEGUNDOS" → "SECUNDOS". OpenAI fixed it. |

**Updated decision rule (2026-04-30, after building production composer):**

- **English** → Gemini renders text directly. Single-shot, ~7s.
- **Every other language** → **PIL composite is the default.** Gemini generates a text-free scene; Pillow draws the typography with the right Noto/Heebo font. **100% accurate text every time, no retries.** This eliminates the stochastic failure mode that plagued OpenAI on RTL/CJK.

The legacy "let the AI render the text" approach (OpenAI for non-Latin / Gemini for Latin) still works and is faster on the EN side, but for **any non-English deliverable shipped to a customer** prefer the PIL composite path below.

**Why PIL won decisively:**
- OpenAI scrambled Hebrew headlines ~70% of attempts even with explicit instructions.
- Gemini scrambled Italian and Spanish word endings even though they're Latin.
- Hindi conjuncts and Arabic letter-joining cannot be guaranteed via any image model.
- PIL + the right font + bidi/reshaper + raqm = perfect text every time.

## Standard ad anatomy (9:16, what every ad must have)

```
┌─────────────────────────┐
│   HEADLINE              │  ← top, white, large, bold, 1 line
│   subline (optional)    │  ← muted gray, 1 line
│                         │
│      [phone mockup or   │  ← center hero — generated content lives here
│       hero composition] │
│                         │
│                         │
│   ┌─────────────────┐   │  ← gradient pill CTA, single action
│   │  Get free video │   │
│   └─────────────────┘   │
│       {brand}           │  ← lowercase wordmark, gradient text
└─────────────────────────┘
```

Single CTA. Single concept. Sentence case (never Title Case). Numbers as digits. Lowercase wordmark.

## Workflow

1. **Confirm** target language(s), concept(s), output count. Don't ask if obvious — make assumptions and proceed in auto mode.
2. **Pick the model** by language (table above).
3. **Write prompts** following the recipe. For non-Latin, prompt fully in target language.
4. **Run in parallel** via `ThreadPoolExecutor` — for non-Latin, 2–3 attempts each.
5. **Save to** `marketing/ad_drafts/` (create if missing), with descriptive names like `final_he_01_realestate.png`.
6. **Open in Preview** (`open path1 path2 ...`) so the user can see them.
7. **Grade each one in your reply.** Be honest about scrambled text, typos, weak composition. Mark which are ship-ready (✅) vs need regen (⚠️) vs unusable (❌). Don't make the user squint.
8. **Offer a clear next step** — regen the broken ones, ship the good ones, move to video, etc.

## Code template — the parallel generator

```python
import os, pathlib, base64, time
from concurrent.futures import ThreadPoolExecutor

# Load API keys from .env.local in project root (walk up from script)
env_path = pathlib.Path(__file__).resolve().parents[2] / ".env.local"
for line in env_path.read_text().splitlines():
    if line.startswith("OPENAI_API_KEY="):
        os.environ["OPENAI_API_KEY"] = line.split("=", 1)[1].strip().strip('"')
    elif line.startswith("GEMINI_API_KEY="):
        os.environ["GEMINI_API_KEY"] = line.split("=", 1)[1].strip().strip('"')

# OpenAI — for non-Latin scripts (Hebrew, Arabic, CJK)
from openai import OpenAI
oai = OpenAI()

def oai_gen(name, prompt, out_dir):
    r = oai.images.generate(
        model="gpt-image-1", prompt=prompt,
        size="1024x1536",  # vertical 2:3, close to 9:16
        quality="high", n=1,
    )
    p = out_dir / f"{name}.png"
    p.write_bytes(base64.b64decode(r.data[0].b64_json))
    return p

# Gemini — for Latin scripts
from google import genai
from google.genai import types
gem = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def gem_gen(name, prompt, out_dir):
    r = gem.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(aspect_ratio="9:16"),
        ),
    )
    for part in r.candidates[0].content.parts:
        if part.inline_data and part.inline_data.data:
            p = out_dir / f"{name}.png"
            p.write_bytes(part.inline_data.data)
            return p
    raise RuntimeError("no image in response")

# Run in parallel
JOBS = [
    # (name, "oai" | "gem", prompt)
]

def run(job):
    name, kind, prompt = job
    t0 = time.time()
    try:
        fn = oai_gen if kind == "oai" else gem_gen
        p = fn(name, prompt, OUT_DIR)
        print(f"[{name}] {time.time()-t0:.1f}s -> {p}")
    except Exception as e:
        print(f"[{name}] FAILED: {e}")

with ThreadPoolExecutor(max_workers=4) as ex:
    list(ex.map(run, JOBS))
```

## Prompt template — Hebrew (winning recipe, OpenAI)

```
מודעה ורטיקלית 9:16 ל[פלטפורמה], פלט סופי.

רקע שחור עמוק. במרכז: [תיאור הסצנה הקולנועית — סמארטפון, מוצר, פנים מסעדה וכו']. מאחורי המוצר זוהר רך בסגול-ורוד.

טיפוגרפיה: גופן Heebo בולד. עברית מימין לשמאל.

כותרת בראש הפריים, אותיות לבנות גדולות:
[כותרת קצרה — 2-4 מילים]

כפתור CTA בתחתית, גרדיאנט סגול-ורוד-כתום, אותיות לבנות:
קבלו סרטון חינם

מתחת לכפתור: {brand} באותיות לטיניות קטנות בגרדיאנט.

קריטי: רנדר את האותיות העבריות בדיוק. אל תכפיל מילים. אל תוסיף טקסט אחר. פלט סופי גמור.
```

## Prompt template — French (Latin, Gemini)

```
Annonce verticale 9:16 [plateforme], version finale.
Fond noir profond. Au centre : [description de la scène cinématographique]. Halo doux violet-rose derrière.
Typographie : Inter Bold.
Titre en haut, lettres blanches grandes : [titre — 3-5 mots max]
Sous-titre gris clair (optionnel) : [sous-titre court]
Bouton CTA en bas, dégradé violet-rose-orange, texte blanc : Obtenez votre vidéo gratuite
Sous le bouton : {brand} en minuscules avec dégradé.
Critique : rendre le français exactement, sans fautes, sans répétitions. Version finale.
```

## Prompt template — English (Latin, Gemini)

```
Vertical 9:16 social ad, [platform], finished output.
Deep black #09090B background. Center: [cinematic scene description]. Soft purple-pink glow behind.
Typography: Inter Bold, sentence case, tracking-tight.
Top headline, large white letters: [headline — 3-5 words]
Subline (optional) in muted gray: [subline]
Bottom: rounded pill button filled with brand gradient (purple #6C5CE7 → pink #FF4FD8 → orange #FF9A3C), white text reading exactly: Get your free video
Below the button: lowercase "{brand}" wordmark in gradient.
Render English text exactly. No typos. Finished output, not a sketch.
```

## PIL composite — the production path for non-English

This is the **default** for non-English ads now. Covers 12 languages (FR, DE, PT, RU, ES, IT, HE, AR, ZH, JA, KO, HI).

### Pipeline
1. **Scene-only generation via Gemini.** Prompt: `NO TEXT, NO LETTERS, NO LOGOS, NO WORDS, NO NUMBERS, NO HEX CODES, NO TAGS anywhere in the image.` Strict instruction is required because Gemini will otherwise leak hex codes (`#0909B`), prompt fragments, or hashtags into the rendered image. Describe the scene with traits (woman, setting, lighting, vibe) but never include color hex codes in the prompt — describe colors by name.
2. **PIL overlay** with auto-fit headline, subline, gradient pill CTA, glow halo, and gradient-masked `{brand}` wordmark.

### Required dependencies
```bash
pip install Pillow python-bidi arabic-reshaper
brew install libraqm                       # macOS, for Devanagari/Arabic shaping
pip install --no-binary Pillow Pillow      # rebuild Pillow against libraqm
```
Verify: `python -c "from PIL import features; print(features.check('raqm'))"` should print `True`. Without raqm, Devanagari conjuncts and pre-base matras (e.g. ि in विज्ञापन) render incorrectly.

### Font matrix
Download once into `marketing/ad_drafts/fonts/`:
- **Heebo-Bold.ttf** — Hebrew
- **NotoSansArabic-Bold.ttf** — Arabic
- **NotoSansSC-Bold.otf** — Chinese (Simplified)
- **NotoSansJP-Bold.otf** — Japanese
- **NotoSansKR-Bold.otf** — Korean
- **NotoSansDevanagari-Bold.ttf** — Hindi
- **NotoSans-Bold.ttf** — Latin + Cyrillic (FR, DE, PT, RU, ES, IT, EN)

### Text shaping per language
```python
import arabic_reshaper
from bidi.algorithm import get_display

def shape(text, rtl, lang=None):
    if not rtl: return text
    if lang == "ar":
        text = arabic_reshaper.reshape(text)   # connect Arabic letters
    return get_display(text)                   # bidi reorder for RTL
```
- **Hebrew:** `get_display(text)` only — no shaper needed (Hebrew letters don't connect).
- **Arabic:** `arabic_reshaper.reshape()` THEN `get_display()` — without the reshaper letters appear isolated/disconnected.
- **CJK / Devanagari / Latin / Cyrillic:** no preprocessing, but Devanagari requires Pillow built with libraqm.

### Auto-fit headline
Long German/Russian headlines overflow at 100pt. Iterate down by 4pt until the rendered bbox fits within `W - 2*PAD`:
```python
def fit_font(font_path, text, max_w, max_size, min_size=40):
    for size in range(max_size, min_size - 1, -4):
        f = ImageFont.truetype(font_path, size)
        if (f.getbbox(text)[2] - f.getbbox(text)[0]) <= max_w:
            return f
    return ImageFont.truetype(font_path, min_size)
```

### Composition primitives
- **Top + bottom dark gradient overlays** (~700px / 500px) for headline legibility on top of any scene.
- **Gradient pill** drawn pixel-by-pixel (purple→pink→orange) with rounded-rectangle alpha mask.
- **Soft purple glow** behind the CTA — `Image.new` ellipse + Gaussian blur 60px + 0.5 alpha.
- **Gradient-masked wordmark** — render text into an L-mode mask, paste a horizontal gradient through it.

Full code in `gen_all_pil.py` — copy-modify rather than rewrite from scratch.

## After generating — always

- Open all images: `open path1 path2 path3 …` (macOS).
- Grade each one in your reply. Use ✅ / ⚠️ / ❌ markers. Be specific about what's wrong: scrambled letter, missing word, weak composition, wrong CTA copy.
- For non-Latin ads, **read the rendered text yourself** and verify it matches what was requested. Don't assume the model got it right because the image looks pretty.
- Offer one clear next step.

## Anti-patterns — don't do these

- ❌ Embedding non-Latin text inside an English prompt (e.g. "render the Hebrew word חינם here") — you get gibberish.
- ❌ Long headlines + subline + CTA + tagline + disclaimer — too much text in one image guarantees errors. Pick one or two text elements max.
- ❌ Title Case headlines — brand voice is sentence case.
- ❌ Mentioning credit counts, prices, or limited-time urgency in CTAs unless the user asks. Default to a plain benefit CTA with no numbers.
- ❌ Stock-photo-y compositions. Hero imagery should be generated content, never stock.
- ❌ Single attempt on a non-Latin ad. Always run 2–3 in parallel.
- ❌ Reporting "the ad is ready" without actually reading the rendered text.
- ❌ Using `#DA7756` as the CTA button fill on cream/white backgrounds — use `#C4642D` (WCAG-safe). `#DA7756` fails contrast on cream.
