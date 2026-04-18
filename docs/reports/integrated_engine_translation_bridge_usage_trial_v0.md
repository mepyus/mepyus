# Integrated Engine Translation Bridge Usage Trial v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This document applies `integrated_engine_translation_bridge_lexicon_v1_candidate.md` to one realistic explanation context.

It does not create final glossary entries, UI copy, wording patches, scaffold edits, manifest changes, read-map changes, external style harvest, selected-object behavior, trace UI, runtime binding, or extension promotion.

## 1. chosen explanation context

Chosen context:

- explaining the current integrated-engine operating mode to a human collaborator before any new build work is opened

Why this context was chosen:

- It naturally includes multiple high-risk entries:
  - `workspace ownership`
  - `hold`
  - `carry-forward`
  - `reject / conflict`
  - `collision stop condition`
  - `watch keep`
  - `not promoted`
  - `user decision / package opening authority`
- It is close to current real use because the engine is already in stop-and-use / use observation mode.
- It tests whether bridge language can explain status without turning status into project-management shorthand.

## 2. internal reading summary

Current operating status:

- The integrated engine is in `stop-and-use / use observation` mode.
- Build mode, patch planning, patch application, scaffold modification, manifest/read-map changes, and extension promotion are closed.
- S1/S2/S3 are manually usable under the current baseline.
- S2 wording candidates are `not promoted / watch keep`.

Authority / ownership boundary:

- User opens or does not open future packages.
- Codex writes canonical reports or patches only when scoped.
- Gemini proposal material remains proposal-side unless Codex translates/classifies it and the user opens a path.
- Workspace ownership is an authority boundary, not just folder assignment.

What remains closed:

- scaffold edits
- `runtime/views/*` changes
- manifest shape changes
- `PANEL_MANIFEST_READ_MAP` changes
- wording patch planning/application
- selected-object behavior
- trace UI
- runtime binding
- extension promotion
- external translation harvest

Possible re-entry or decision condition:

- wording gate may reopen only if cross-scenario or natural-use recurrence appears, supported reread weakens, or scenario reading is actually blocked.
- build or patch packages may open only by user decision and scoped package.
- held features can move only through a future promotion gate or explicit scoped work.

What must not be inferred:

- `watch keep` does not mean patch queue.
- `hold` does not mean discarded.
- `carry-forward` does not mean approved later.
- `reject / conflict` does not mean globally bad.
- `collision stop condition` does not mean error.
- `workspace ownership` does not mean simple folder owner.

## 3. bridge lexicon applied explanation draft

This is a trial explanation, not final wording:

The current operating status is stop-and-use / use observation. That means the baseline can be used manually now, but build mode, patch planning, scaffold edits, manifest/read-map changes, runtime binding, trace UI, selected-object behavior, and extension promotion remain closed.

The important authority boundary is that no material moves into core just because it exists or looks useful. Gemini material stays proposal-side unless Codex translates it against the baseline, and even Codex translation does not by itself open implementation. The user has the package-opening authority: a new patch, external harvest, or promotion path starts only if the user opens that route.

Workspace ownership should be read as authority and provenance. `gemini/` material can be proposal material. `docs/reports/` can hold Codex canonical reports when the task is scoped. `runtime/views` and `runtime/manifests` remain closed in this mode. This is not just folder responsibility; it tells us what the artifact is allowed to do.

Current watch items remain `not promoted / watch keep`. They are visible because they may matter during use, but they do not open wording patch planning. The gate reopens only if similar ambiguity appears across S1/S3 or natural use, if supported reread weakens, or if scenario reading is actually blocked.

Held items remain held. Selected-object behavior, trace UI, runtime binding, manifest/read-map changes, extension promotion, and wording patch application are outside the current mode. Hold means these are kept outside the current core/package; it does not mean the ideas have no future value.

Carry-forward material can remain useful for later reread, but it has no current operating authority. Reject/conflict material is different: it conflicts with the current baseline or package boundary. That does not make it universally bad, but it means it cannot enter core under the current rules.

If a proposed route would require unauthorized core drift, runtime truth, read-map changes, new authority, or direct Gemini-to-core movement, that is a collision stop condition. It is not an error message. It is a brake that protects the current baseline and tells us to classify the material as hold, carry-forward, reject/conflict, or needs user decision.

## 4. lexicon entries used

Actually used in this explanation:

- `workspace ownership`
- `needs Codex translation`
- `proposal-only`
- `collision stop condition`
- `hold`
- `carry-forward`
- `reject / conflict`
- `not promoted`
- `watch keep`
- `user decision / package opening authority`
- `support reread recovery`

Not central in this usage context:

- `return validation`
- `anchor drift`
- `reflux`
- `current_loop_state`

Reason:

- This context is current operating mode / handoff boundary, not S1/S3 route explanation.

## 5. required separation check

### current operating status

Preserved:

- stop-and-use / use observation
- build and patch paths closed
- S1/S2/S3 usable

Risk:

- could sound like project pause if not paired with "manual use possible."

### authority / ownership boundary

Preserved:

- User opens packages.
- Codex translates and records when scoped.
- Gemini material stays proposal-side unless translated.
- workspace path indicates artifact authority.

Risk:

- could still sound like a maker/reviewer/approver chain if shortened too much.

### what remains closed

Preserved:

- scaffold, manifest/read-map, selected-object, trace UI, runtime binding, extension promotion, external harvest, wording patch all stay closed.

Risk:

- closed items can sound rejected if hold/carry-forward distinction is omitted.

### possible re-entry or decision condition

Preserved:

- wording gate reopens only through cross-scenario/natural-use recurrence, weak recovery, or use-blocking confusion.
- implementation or promotion opens only by user-scoped package.

Risk:

- "future condition" can sound like scheduled work unless no-current-authority is repeated.

### what must not be inferred

Preserved:

- watch keep is not patch queue.
- hold is not discarded.
- carry-forward is not approved later.
- reject/conflict is not universal failure.
- collision stop is not error.
- workspace ownership is not folder owner.

Risk:

- this section remains necessary; without it, high-risk terms flatten quickly.

## 6. trial note

The explanation is readable enough, but it works because it is explicit and somewhat procedural.

If shortened into smoother user-facing copy, the first losses would likely be:

- workspace ownership as authority
- watch keep as observation-only
- carry-forward as non-commitment
- collision stop as route brake

Therefore this remains an explanation trial, not final copy.
