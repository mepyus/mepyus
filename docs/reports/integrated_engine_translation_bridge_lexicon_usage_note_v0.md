# Integrated Engine Translation Bridge Lexicon Usage Note v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

The translation bridge lexicon can be used as a provisional explanation aid, but it must not be used as final UI wording, final glossary, or wording patch source.

## 1. purpose

The bridge lexicon exists to keep internal integrated-engine terms from being flattened when they are explained to humans.

It supports explanation, not replacement.

## 2. allowed uses

Allowed:

- human explanation draft
- Gemini/Codex handoff explanation
- internal-to-human bridge note
- future translation rule harvest input
- future real-use explanation trial support
- checking whether a proposed explanation preserves route, authority, state, and boundary

Allowed example of use:

- When explaining `proposal-only`, consult the lexicon to preserve non-canonical authority status before writing any smoother human explanation.

## 3. prohibited uses

Not allowed:

- UI final label replacement
- glossary lock
- wording patch direct source
- baseline term overwrite
- scaffold text replacement
- manifest/read-map contract change
- final public terminology
- external translation style claim
- extension promotion support

Do not copy `provisional human bridge note` into UI copy.

Those notes are explanation direction, not product language.

## 4. required reading order

Before using a bridge entry, check four things:

1. route
   - What moves, from where, to where, and why?
2. authority
   - Who can propose, translate, record, decide, or promote?
3. state
   - Is the item active, held, watched, not promoted, carry-forward, rejected/conflict, or closed?
4. boundary
   - What must not be reopened: scaffold, manifest, read map, runtime binding, selected-object behavior, trace UI, extension promotion, or final wording?

If the explanation does not preserve these four axes, do not use it.

## 5. bridge entry interpretation rules

### Do not replace the internal term first

Start from the internal term and its operating role.

Only after preserving role and boundary should a human explanation be attempted.

### Do not make smoothness the goal

The goal is not the smoothest sentence.

The goal is to prevent loss of:

- route reason
- authority ownership
- active hold/watch state
- validation brake
- support-reread recovery
- user package-opening authority

### Do not collapse states

Keep these separate:

- `hold`
- `watch keep`
- `not promoted`
- `carry-forward`
- `reject / conflict`
- `needs user decision`

These terms are not synonyms for "not used."

### Do not collapse authority

Keep these separate:

- Gemini proposal material
- Codex baseline translation
- Codex canonical report writing under scoped package
- User promotion / package opening

These are not a simple maker-reviewer-approver chain.

## 6. when to use extra caution

Use extra caution for:

- `workspace ownership`
- `needs Codex translation`
- `hold`
- `carry-forward`
- `reject / conflict`
- `collision stop condition`

Reason:

- these entries weakened first in the real handoff explanation trial.
- they can become ordinary process language unless authority and boundary are repeated.

## 7. relation to current mode

Current operating mode remains:

- stop-and-use / use observation
- build mode closed
- patch planning closed
- patch application closed
- selected-object / trace UI / runtime binding / extension promotion held

The bridge lexicon does not reopen any of those.

## 8. relation to future external harvest

This lexicon can feed a future external translation rule harvest, but external harvest is not opened by this document.

Before external harvest, any candidate external phrasing must be checked against:

- proposal-only authority
- workspace ownership
- hold/watch separation
- collision stop as brake
- request / return / reflux route separation

## 9. closeout sentence

Use this lexicon as a boundary-preserving bridge aid. Do not use it as a final glossary, UI copy source, or shortcut around integrated-engine grammar.
