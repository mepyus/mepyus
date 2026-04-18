# Integrated Engine Real Handoff Grammar Classification v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This document classifies `integrated_engine_real_gemini_handoff_artifact_v0.md` through the six current internal grammar candidates.

It does not create final wording, patch wording, scaffold edits, manifest changes, read-map changes, runtime binding, selected-object behavior, trace UI, external translation rules, or extension promotion.

## 1. route grammar

Concrete evidence in artifact:

- source material is Gemini-side design clay and prior Codex analysis.
- proposal-only status is explicit.
- Codex translation is required before any core use.
- expected return from Codex is grammar classification, human explanation trial, retention check, and closeout.
- user decision is required before any later promotion or implementation.

What is preserved:

- the route is not `Gemini output -> core`.
- the route is:

```text
Gemini proposal material
-> formal handoff artifact
-> Codex grammar classification
-> human explanation trial
-> retention / closeout
-> future user decision if any next package opens
```

What is thin:

- the artifact is formalized by Codex from stored material; it is not a freshly generated Gemini CLI handoff file.
- still, it is formal enough for explanation trial because proposal-only, translation, ownership, and stop conditions are explicit.

What would break if flattened:

- calling it a "mock review" would erase route reason and handoff status.
- calling it a "design task" would hide the proposal -> translation -> decision route.

## 2. authority grammar

Concrete evidence in artifact:

- Gemini owns proposal workspace under `gemini/`.
- Codex owns canonical trial reports under `docs/reports/` for this package.
- scaffold and manifest workspaces are closed.
- user owns package opening and promotion decisions.
- proposal-only and needs Codex translation are explicit.

What is preserved:

- Gemini can propose but not canonicalize.
- Codex can translate and report but not promote without user scope.
- User decides future promotion or implementation.
- workspace ownership is tied to authority, not just location.

What is thin:

- because the artifact is written under `docs/reports`, readers may overread it as canonical acceptance of Gemini material.
- the artifact counters this by labeling itself documentation trial only.

What would break if flattened:

- `proposal-only` as "draft" would erase authority boundary.
- `needs Codex translation` as "handoff forwarding" would erase validation work.
- `workspace ownership` as "folder responsibility" would erase write authority and collision prevention.

## 3. hold / watch grammar

Concrete evidence in artifact:

- supervisor queue, watcher recommendation, bridge panel, line atlas as center, team/role console dominance, and control-room framing are classified as hold, support-only, extension later, or reject-conflict.
- held material is not deleted.
- usable material is scoped to reference or documentation trial.

What is preserved:

- hold means visible but not core now.
- carry-forward differs from reject/conflict.
- needs user decision differs from usable now.

What is thin:

- no new watch registry is opened for this handoff.
- hold/watch is used as classification, not repeated observation state.

What would break if flattened:

- hold could become "discarded."
- carry-forward could become "approved later."
- reject/conflict could become "bad idea" rather than baseline conflict.

## 4. validation grammar

Concrete evidence in artifact:

- Codex must classify handoff material before use.
- collision stop conditions are named.
- reject/conflict is assigned when material requires runtime binding, read-map changes, new authority, or core drift.
- expected Codex role is baseline translator and boundary checker.

What is preserved:

- validation is route selection, not taste judgment.
- stop/collision is a baseline-protection brake.
- reject/conflict and carry-forward are separate outcomes.

What is thin:

- validation here checks explanation and proposal boundaries, not a live engine return.
- that is acceptable because Gemini handoff material is listed as a validation starting point in the grammar candidate.

What would break if flattened:

- stop/collision as "error" would hide its brake function.
- validation as "review" would hide classification and authority control.

## 5. reread / support grammar

Concrete evidence in artifact:

- source material includes prior mock analysis and visual translation briefs.
- the artifact explicitly says source material cannot define baseline by itself.
- Codex must recover baseline fit through grammar classification and retention check.

What is preserved:

- first-pass mock usefulness is not enough.
- support reread through baseline and analysis reports is required before any core use.
- explanation trial is allowed only after the handoff status is clear.

What is thin:

- the artifact does not include a separate blind first-pass log.
- first-pass risk is inferred from prior structural analysis and known mock conflicts.

What would break if flattened:

- "read the mock and decide" would erase the support-reread sequence.
- "explain it simply" would skip the recovery check.

## 6. bridge-before-flatten grammar

Concrete evidence in artifact:

- final user-facing wording is prohibited.
- human explanation is allowed only as trial material.
- artifact requires proposal, translation, official recording, and user decision roles to remain separate.
- collision and workspace ownership must stay visible.

What is preserved:

- bridge explanation cannot become glossary or patch wording.
- simplification must preserve route, authority, state, and boundary.
- explanation is judged by retention, not smoothness.

What is thin:

- no external style or real user test is included.
- that is intentional for this package.

What would break if flattened:

- easy explanation could make proposal-only sound like draft.
- easy explanation could make Codex translation sound like relay.
- easy explanation could make user decision sound optional.

## 7. targeted checks

### proposal-only is not simple draft

Reason:

- proposal-only means material cannot enter core directly.
- it marks authority and route status.
- a draft can be copied or revised; proposal-only must be translated and classified first.

### needs Codex translation is not simple delivery

Reason:

- Codex translation includes baseline fit, conflict detection, hold/carry-forward classification, and authority check.
- forwarding would preserve content only; translation preserves boundary.

### workspace ownership is not simple responsibility

Reason:

- workspace ownership controls write authority.
- `gemini/` output provenance prevents direct core adoption.
- `docs/reports` canonical reporting is scoped to Codex documentation packages.

### collision stop is not simple error handling

Reason:

- collision stop means a route would damage baseline boundaries.
- it can classify material as reject/conflict or carry-forward without treating all source material as failed.

## 8. classification closeout

The formal artifact preserves all six grammar candidates well enough for human explanation trial.

Main thinness:

- the artifact is formalized from existing material rather than produced by a live Gemini CLI handoff.
- reread/support grammar is present but would be stronger with an explicit blind first-pass section.
