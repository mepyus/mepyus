# Integrated Engine Translation Bridge Lexicon v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This is a provisional bridge working lexicon.

It is not:

- final glossary
- UI copy
- wording patch source
- baseline term replacement
- external translation rule
- scaffold or manifest contract

Use it to preserve internal meaning when explaining integrated-engine language to humans. Do not use it to overwrite the internal terms.

## 1. scope

This lexicon is built from:

- internal grammar candidates
- human bridge seed list
- real handoff grammar classification
- real handoff human explanation trial
- real handoff retention check
- language amplification harvest
- translation friction log
- current use-state and hold/watch records

Each entry records:

- what the internal term does in the system
- what must survive in human explanation
- where easy explanation tends to flatten it
- what boundary must be repeated

## 2. entries

### 2.1 `workspace ownership`

- internal term: `workspace ownership`
- internal role or meaning: Authority / boundary term. It marks which actor may write or treat material as proposal, canonical report, scaffold, manifest, or status material.
- why it matters in the integrated engine: Without workspace ownership, Gemini proposal material can look like canonical material, or Codex documentation can look like implementation authority.
- what must be preserved: file location as authority, provenance, write permission, and collision prevention.
- flattening risk: reduced to "folder assignment" or "who owns which directory."
- boundary reminder: `gemini/` may hold proposal material; `docs/reports/` may hold Codex canonical reports when scoped; scaffold/manifest work remains closed unless explicitly opened.
- provisional human bridge note: Explain it as the rule that keeps proposal material, canonical reports, and implementation spaces from collapsing into one another. The folder is not just storage; it marks what kind of authority the material currently has.
- do-not-reduce-to: folder 담당, file organization, convenience path.
- scenario scope: handoff / cross-scenario.
- confidence level: high, with flattening risk.
- evidence source(s): `integrated_engine_real_handoff_retention_check_v0.md`, `integrated_engine_real_handoff_human_explanation_trial_v0.md`, `integrated_engine_human_bridge_seed_list_v0.md`, `integrated_engine_translation_friction_log_v0.md`.

### 2.2 `needs Codex translation`

- internal term: `needs Codex translation`
- internal role or meaning: Authority / validation term. It means material must be filtered through the current baseline before any core use.
- why it matters in the integrated engine: It prevents Gemini output, mock material, or easy explanation from bypassing route, authority, state, and boundary checks.
- what must be preserved: structural filtering, conflict detection, hold/carry-forward classification, and baseline fit judgment.
- flattening risk: reduced to "Codex reviews," "Codex summarizes," or "Codex passes it along."
- boundary reminder: translation is not forwarding. It decides what is usable now, needs translation, carry-forward, reject/conflict, or needs user decision.
- provisional human bridge note: Explain it as the step where Codex checks whether the material can safely enter the current engine language. It is closer to baseline filtering than ordinary translation.
- do-not-reduce-to: simple 전달, summary, wording cleanup.
- scenario scope: handoff / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_real_handoff_grammar_classification_v0.md`, `integrated_engine_real_handoff_retention_check_v0.md`, `integrated_engine_internal_language_grammar_candidate_v0.md`.

### 2.3 `proposal-only`

- internal term: `proposal-only`
- internal role or meaning: Authority / state term. It marks material as idea or design clay that has not entered baseline.
- why it matters in the integrated engine: It allows Gemini or other sources to expand possibility without granting implementation or canonical status.
- what must be preserved: non-canonical status, no direct core entry, needs translation before use.
- flattening risk: reduced to "rough draft," "weak output," or "almost approved."
- boundary reminder: proposal-only material may be valuable, but it cannot become scaffold, manifest, baseline, or final wording by itself.
- provisional human bridge note: Explain it as material that is allowed to be considered but not allowed to act yet. Its value is preserved while its authority is limited.
- do-not-reduce-to: draft, low-quality idea, pending approval by default.
- scenario scope: handoff.
- confidence level: high.
- evidence source(s): `integrated_engine_real_gemini_handoff_artifact_v0.md`, `integrated_engine_real_handoff_retention_check_v0.md`, `integrated_engine_translation_friction_log_v0.md`.

### 2.4 `collision stop condition`

- internal term: `collision stop condition`
- internal role or meaning: Boundary / validation brake. It stops a route when material would force core drift, unauthorized edits, runtime truth, read-map change, or authority mixing.
- why it matters in the integrated engine: It prevents simultaneous or proposal-driven work from crossing into core without baseline translation and user scope.
- what must be preserved: stop as baseline-protection brake, not generic error.
- flattening risk: reduced to "error handling," "problem," or "blocked task."
- boundary reminder: a collision stop can preserve future value as carry-forward; it does not mean every part of the source material failed.
- provisional human bridge note: Explain it as the point where the engine says "this would damage the current boundary if we force it in now." It protects the route rather than punishing the idea.
- do-not-reduce-to: bug, failure, tool crash, simple stop-if-problem.
- scenario scope: handoff / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_real_handoff_grammar_classification_v0.md`, `integrated_engine_real_handoff_retention_check_v0.md`, `integrated_engine_translation_friction_log_v0.md`.

### 2.5 `hold`

- internal term: `hold`
- internal role or meaning: State / boundary term. It keeps material outside current core or current package without deleting its future value.
- why it matters in the integrated engine: It lets the system preserve future axes while keeping current baseline stable.
- what must be preserved: visible but not core now; no build or promotion opened.
- flattening risk: reduced to "discarded," "ignored," or "not used."
- boundary reminder: hold is an active boundary state. It needs a later gate or package before promotion.
- provisional human bridge note: Explain hold as "kept out of the current body for now, but still visible as material." Avoid making it sound like rejection.
- do-not-reduce-to: 버림, unused, backlog.
- scenario scope: handoff / cross-scenario.
- confidence level: medium-high.
- evidence source(s): `integrated_engine_internal_language_grammar_candidate_v0.md`, `integrated_engine_real_handoff_retention_check_v0.md`, `integrated_engine_current_hold_and_watch_registry_v0.md`.

### 2.6 `carry-forward`

- internal term: `carry-forward`
- internal role or meaning: State / future-material term. It preserves material for later consideration without making it core now.
- why it matters in the integrated engine: It prevents premature extension promotion while avoiding loss of useful design or structural material.
- what must be preserved: future value, no current implementation, no automatic promotion.
- flattening risk: reduced to "approved later," "backlog item," or "unused idea."
- boundary reminder: carry-forward is not approval. It still needs promotion gate or user-scoped package later.
- provisional human bridge note: Explain it as material that stays in the space for future reread. It has value, but not current authority.
- do-not-reduce-to: later approved, task backlog, deferred feature.
- scenario scope: handoff / cross-scenario.
- confidence level: medium-high.
- evidence source(s): `integrated_engine_real_gemini_handoff_artifact_v0.md`, `integrated_engine_real_handoff_retention_check_v0.md`, `integrated_engine_internal_language_pattern_inventory_v0.md`.

### 2.7 `reject / conflict`

- internal term: `reject / conflict`
- internal role or meaning: Validation / boundary result. It marks material that conflicts with current baseline guardrails.
- why it matters in the integrated engine: It keeps incompatible material from entering core while allowing the reason to be recorded.
- what must be preserved: conflict with current baseline, not universal badness.
- flattening risk: reduced to "bad idea," "wrong," or "not useful."
- boundary reminder: reject/conflict is scoped to the current baseline and package. Some ideas may be valid elsewhere or later, but not here.
- provisional human bridge note: Explain it as "this does not fit the current engine boundary." Keep the reason attached.
- do-not-reduce-to: bad, useless, impossible.
- scenario scope: handoff / cross-scenario.
- confidence level: medium-high.
- evidence source(s): `integrated_engine_real_handoff_grammar_classification_v0.md`, `integrated_engine_real_gemini_handoff_artifact_v0.md`.

### 2.8 `not promoted`

- internal term: `not promoted`
- internal role or meaning: State / gate term. It means a candidate has not moved into patch planning, core, or extension status.
- why it matters in the integrated engine: It prevents watch items from becoming automatic work.
- what must be preserved: visible candidate, no promotion, no patch planning.
- flattening risk: reduced to "rejected" or "ignored."
- boundary reminder: not promoted can coexist with watch keep or carry-forward.
- provisional human bridge note: Explain it as "kept visible, but not raised to the next operating level." It is a gate state.
- do-not-reduce-to: rejected, closed forever, forgotten.
- scenario scope: S2 / use observation / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_current_use_state_refresh_v0.md`, `integrated_engine_current_hold_and_watch_registry_v0.md`, `integrated_engine_internal_language_grammar_candidate_v0.md`.

### 2.9 `watch keep`

- internal term: `watch keep`
- internal role or meaning: State / observation term. It means a candidate remains under use observation without opening patch planning.
- why it matters in the integrated engine: It lets recoverable ambiguity stay visible while stopping premature wording changes.
- what must be preserved: observe during use, no immediate action, re-entry only on official conditions.
- flattening risk: reduced to "bug watch," "patch queue," or "low-priority task."
- boundary reminder: watch keep is not enough to reopen a gate. Cross-scenario or natural-use recurrence is needed.
- provisional human bridge note: Explain it as continued observation, not implementation. It keeps the signal alive without moving it into build mode.
- do-not-reduce-to: TODO, bug, patch candidate.
- scenario scope: S2 / use observation / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_current_use_state_refresh_v0.md`, `integrated_engine_current_hold_and_watch_registry_v0.md`, `integrated_engine_internal_language_grammar_candidate_v0.md`.

### 2.10 `user decision / package opening authority`

- internal term: `user decision / package opening authority`
- internal role or meaning: Authority / route-opening term. It marks that the user decides whether a direction becomes an actual package, promotion, implementation, or external harvest.
- why it matters in the integrated engine: It prevents Codex translation or Gemini proposal material from becoming autonomous promotion.
- what must be preserved: user opens scope; action does not start from proposal or classification alone.
- flattening risk: reduced to "approval" or "permission."
- boundary reminder: user decision is route control. It determines which mode opens and which remains closed.
- provisional human bridge note: Explain it as the point where the user chooses whether the next operational route exists at all. It is stronger than simple approval.
- do-not-reduce-to: approval click, permission, sign-off.
- scenario scope: handoff / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_real_handoff_human_explanation_trial_v0.md`, `integrated_engine_real_handoff_grammar_classification_v0.md`, `integrated_engine_internal_language_grammar_candidate_v0.md`.

### 2.11 `return validation`

- internal term: `return validation`
- internal role or meaning: Route / validation term. Engine output returns to VectorFL-side validation before user decision, reflux, or reprocess.
- why it matters in the integrated engine: It keeps engine output from being mistaken for final completion or final meaning.
- what must be preserved: validation ownership, route selector role, separation from execution.
- flattening risk: reduced to "checking the result" or engine self-validation.
- boundary reminder: engine produces return material; VectorFL validates route/fit before next movement.
- provisional human bridge note: Explain it as the step where returned material is checked for route fit before it can close, reprocess, or become maturation input.
- do-not-reduce-to: engine check, result done, QA only.
- scenario scope: S1 / S2 / S3 / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_internal_language_grammar_candidate_v0.md`, `integrated_engine_translation_friction_log_v0.md`, `integrated_engine_language_amplification_harvest_v0.md`.

### 2.12 `anchor drift`

- internal term: `anchor drift`
- internal role or meaning: Boundary / validation brake. It indicates mismatch against anchor criteria that can stop route progression and trigger reprocess.
- why it matters in the integrated engine: It proves anchor is not just explanation; it can operate as a brake.
- what must be preserved: operational stop/reprocess force, anchor-fit comparison, not passive warning.
- flattening risk: reduced to "mismatch," "reference issue," or "warning."
- boundary reminder: anchor drift can keep the loop open and prevent user decision until recheck or reprocess.
- provisional human bridge note: Explain it as a reference-fit break that can stop the flow. It is not merely a note that something looks off.
- do-not-reduce-to: warning, mismatch label, advisory note.
- scenario scope: S3 / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_translation_friction_log_v0.md`, `integrated_engine_internal_language_grammar_candidate_v0.md`, `integrated_engine_language_amplification_harvest_v0.md`.

### 2.13 `reflux`

- internal term: `reflux`
- internal role or meaning: Route / maturation preservation term. It carries maturation-worthy material back toward space for reread and line/axis growth.
- why it matters in the integrated engine: It separates future maturation value from return completion or rollback.
- what must be preserved: route and reason for preserving material, not failure.
- flattening risk: reduced to "save for later," "archive," "rollback," or "residue."
- boundary reminder: reflux is a packet route with maturation value, not passive storage.
- provisional human bridge note: Explain it as material returning to the space because it still has growth value. Keep the route/reason visible.
- do-not-reduce-to: archive, rollback, leftover, 저장.
- scenario scope: S1 / S3 / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_translation_friction_log_v0.md`, `integrated_engine_human_bridge_seed_list_v0.md`, `integrated_engine_language_amplification_harvest_v0.md`.

### 2.14 `current_loop_state`

- internal term: `current_loop_state`
- internal role or meaning: State / position term. It shows the active loop's current position, not the complete history.
- why it matters in the integrated engine: It lets the operator locate the loop without turning state into a full event timeline.
- what must be preserved: minimum current-position state plus need for connection records when reconstructing route history.
- flattening risk: reduced to "workflow history" or "timeline."
- boundary reminder: current loop state is enough for current position; panel connection records are needed for movement reconstruction.
- provisional human bridge note: Explain it as where the loop is now. If someone needs how it got there, they must read supporting packets and connection records.
- do-not-reduce-to: full history, event log, trace UI.
- scenario scope: S1 / S2 / S3 / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_internal_language_grammar_candidate_v0.md`, `integrated_engine_translation_friction_log_v0.md`, `integrated_engine_language_amplification_harvest_v0.md`.

### 2.15 `support reread recovery`

- internal term: `support reread recovery`
- internal role or meaning: Reread / support term. It means first-pass thinness can recover when central panel, packet/object, support panels, and connection records are read in order.
- why it matters in the integrated engine: It keeps recoverable ambiguity from becoming premature patch or feature pressure.
- what must be preserved: recovery path, reading order, no structure change if meaning recovers.
- flattening risk: reduced to "read more docs" or "extra explanation."
- boundary reminder: support reread recovery is not selected-object behavior, trace UI, or runtime binding.
- provisional human bridge note: Explain it as the current way the operator restores intended meaning from existing support records. It is a use-mode mechanism, not a new UI feature.
- do-not-reduce-to: documentation workaround, trace UI need, selected object drilldown.
- scenario scope: S2 / S3 / handoff / cross-scenario.
- confidence level: medium-high.
- evidence source(s): `integrated_engine_real_handoff_retention_check_v0.md`, `integrated_engine_translation_friction_log_v0.md`, `integrated_engine_internal_language_grammar_candidate_v0.md`.

## 3. closeout

This lexicon is deliberately provisional.

Its strongest entries are authority and route terms that have been tested across scenario and handoff records.

Its highest-risk entries are state/boundary terms that ordinary language tends to flatten:

- `workspace ownership`
- `hold`
- `carry-forward`
- `reject / conflict`
- `needs Codex translation`
- `collision stop condition`

Use this document as a bridge-preservation reference, not as a replacement vocabulary.
