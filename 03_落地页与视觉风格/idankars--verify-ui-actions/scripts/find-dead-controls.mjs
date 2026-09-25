#!/usr/bin/env node
/**
 * find-dead-controls — static scan for "dead" action buttons.
 *
 * The bug this exists to prevent: a `<button>` renders with an action label
 * (Reject, Advance, Save, Schedule, …) but has NO `onClick` (and isn't a form
 * submit) — so clicking it does nothing. This passes ESLint, `tsc`, unit tests,
 * AND a 200/render smoke-check, because the page renders fine — the control is
 * just inert. That is exactly how the review-workspace "Reject" button shipped
 * broken ("I clicked Reject and nothing happened"). A render/HTTP check can't
 * catch it; a handler-presence check can.
 *
 * Heuristic + advisory by default. Run `--strict` to exit non-zero (for CI/QA).
 *
 *   node scripts/find-dead-controls.mjs [dir]            # report, exit 0
 *   node scripts/find-dead-controls.mjs [dir] --strict   # exit 1 if any found
 *
 * A button is considered WIRED (not flagged) when its opening tag has any of:
 *   onClick= · onMouseDown= · onPointerDown= · type="submit" · disabled ·
 *   form= · a prop spread {...} (handler forwarded by a parent).
 * It is flagged only when it ALSO has an action-y text label or an aria-label,
 * so decorative/icon-only chrome doesn't create noise.
 */

import { readFileSync, readdirSync, statSync } from "node:fs";
import { join } from "node:path";

const ROOT = process.argv.find((a) => !a.startsWith("-") && a !== process.argv[0] && a !== process.argv[1]) || "src";
const STRICT = process.argv.includes("--strict");

const ACTION_WORDS =
  /\b(reject|advance|schedule|message|approve|decline|send|save|delete|remove|archive|withdraw|move|submit|create|add|invite|publish|confirm|assign|download|export|import|upload|retry|resend|apply|enroll|book|email|call|sync|connect|disconnect|enable|disable|hire|reopen|restore|duplicate|edit|update|generate|run|copy|share|merge|unmerge|snooze|advance stage)\b/i;

function* walk(dir) {
  let entries;
  try {
    entries = readdirSync(dir);
  } catch {
    return;
  }
  for (const name of entries) {
    if (name === "node_modules" || name === ".next" || name.startsWith(".")) continue;
    const p = join(dir, name);
    const s = statSync(p);
    if (s.isDirectory()) yield* walk(p);
    else if (name.endsWith(".tsx")) yield p;
  }
}

/** Index of the `>` that closes the opening tag, tracking brace depth so the
 *  `>` inside `onClick={() => …}` (an arrow fn) is not mistaken for the end. */
function tagEnd(src, start) {
  let depth = 0;
  for (let i = start; i < src.length; i++) {
    const c = src[i];
    if (c === "{") depth++;
    else if (c === "}") depth--;
    else if (c === ">" && depth === 0) return i;
  }
  return -1;
}

/** Blank out /* … *​/ and {/* … *​/} comments, preserving offsets + newlines so
 *  reported line numbers stay accurate and a `<button>` mentioned in a JSDoc
 *  block isn't mistaken for real markup. */
function blankBlockComments(s) {
  return s.replace(/\/\*[\s\S]*?\*\//g, (m) => m.replace(/[^\n]/g, " "));
}

const findings = [];
for (const file of walk(ROOT)) {
  const raw = readFileSync(file, "utf8");
  const src = blankBlockComments(raw);
  const lines = raw.split("\n");
  let idx = 0;
  while ((idx = src.indexOf("<button", idx)) !== -1) {
    const after = src[idx + 7];
    if (after && !/[\s>/]/.test(after)) {
      idx += 7;
      continue;
    }
    const end = tagEnd(src, idx);
    if (end === -1) {
      idx += 7;
      continue;
    }
    const openTag = src.slice(idx, end + 1);
    const wired =
      /\bon(Click|MouseDown|PointerDown|KeyDown)\s*=/.test(openTag) ||
      /\btype\s*=\s*["'`]submit["'`]/.test(openTag) ||
      /\bdisabled\b/.test(openTag) ||
      /\bform\s*=/.test(openTag) ||
      /\{\.\.\./.test(openTag);
    const closeIdx = src.indexOf("</button>", end);
    const inner = closeIdx === -1 ? "" : src.slice(end + 1, closeIdx);
    const text = inner
      .replace(/<[^>]*>/g, " ")
      .replace(/\{[^}]*\}/g, " ")
      .replace(/\s+/g, " ")
      .trim();
    const hasActionLabel = ACTION_WORDS.test(text) || /\baria-label\s*=/.test(openTag);
    if (!wired && hasActionLabel && text.length > 0) {
      const line = src.slice(0, idx).split("\n").length;
      // Opt-out for intentionally-inert chrome (e.g. a preview mockup of the
      // public career card): put `find-dead-controls-ignore` on the tag's line
      // or the line above it.
      const ctx = `${lines[line - 1] ?? ""} ${lines[line - 2] ?? ""}`;
      if (!/find-dead-controls-ignore/.test(ctx)) {
        findings.push({ file, line, text: text.slice(0, 48) });
      }
    }
    idx = end + 1;
  }
}

if (findings.length === 0) {
  console.log("✓ find-dead-controls: no dead action buttons found.");
  process.exit(0);
}

console.log(`✗ find-dead-controls: ${findings.length} potential dead action button(s) — render fine but have no handler:\n`);
for (const f of findings) {
  console.log(`  ${f.file}:${f.line}  "${f.text}"`);
}
console.log(
  "\nEach needs one of: an onClick handler, type=\"submit\" inside a <form>, a forwarded handler prop, or removal.\n" +
    "False positive? The button forwards a handler some other way — add it to the wired heuristic or refactor to make intent explicit.",
);
process.exit(STRICT ? 1 : 0);
