# Anti-Patterns: The Tells of Vibe-Coded UI

These are the recurring visual signatures of AI-generated interfaces. They aren't
bugs — they're the model reproducing the statistical average of its training
data. Each has a fix rooted in design intent. Check every UI against this list.

---

## 1. Neon palettes with no hierarchy

**Tell:** Five or six high-saturation colors (electric blue, hot pink, acid
green) all competing at once. Everything shouts at equal volume, so nothing reads
as important.

**Why it happens:** Neon-on-dark photographs well and dominated "modern SaaS"
content in training data.

**Fix:** One dominant color, one accent, one neutral. Hierarchy comes from
contrast and restraint, not from adding colors.

---

## 2. Decorative dark-mode glow effects

**Tell:** Aurora backgrounds, radial light bloom behind hero sections, glowing
text — effects that carry no meaning and respond to no interaction.

**Why it happens:** Gaming, crypto, and AI launch pages paired dark mode with
glow so heavily that the model learned "dark + glow = premium."

**Fix:** Dark mode earns depth through typography, contrast, and surface levels.
If an effect doesn't communicate state or hierarchy, remove it.

---

## 3. Emojis used as UI chrome

**Tell:** Emojis as navigation icons, section headers, bullet replacements, and
background decoration.

**Why it happens:** Onboarding/marketing copy uses emojis for cheap visual
rhythm; the model generalized it into a design move.

**Fix:** Interfaces need a consistent icon *system* (weight, meaning, sizing).
Emojis belong in communication/microcopy, not as structural iconography.

---

## 4. Purple/indigo gradient on everything

**Tell:** The purple-to-blue gradient applied to buttons, headers, and heroes —
"the Times New Roman of AI design."

**Why it happens:** Notion/Linear/Vercel and their imitators saturated the
training set. It was a trend, never a brand decision.

**Fix:** Derive color from what the product is and who it's for. Start from brand
values and work outward.

---

## 5. Cards for every block of info

**Tell:** Everything is a card. Cards nested in cards nested in cards. A filing
cabinet inside a filing cabinet.

**Why it happens:** The model knows content needs containers but has no cost
function for visual weight, so it wraps until nothing reads as more important.

**Fix:** Group with whitespace, proximity, and typography. Reserve cards for
things that are genuinely independent or interactive. Most content needs no box.

---

## 6. Multicolored side tabs on every block

**Tell:** A thin vertical accent bar on every content block, each a different
color, cycling through the palette with no logic.

**Why it happens:** The model knows accents signal active/selected states but
can't reason about the whole-page color budget.

**Fix:** Treat accent color as a shared, scarce resource. Define what gets an
accent and why, then hold the line. Emphasis needs something to contrast against.

---

## 7. Status dots that mean nothing

**Tell:** Small colored circles on nav items, headers, and labels, changing color
arbitrarily and communicating no actual state.

**Why it happens:** Learned from dashboards where dots genuinely indicate status;
applied globally and stripped of meaning.

**Fix:** Every indicator must map to a defined, communicated state. If a dot
needs explaining, use a text label. If nothing changes state, remove it.

---

## The common thread

All of these come from optimizing for *statistical association* instead of
*design intent*. The model gives you the average. Escape it by making specific
choices grounded in the product, the user, and the context.
