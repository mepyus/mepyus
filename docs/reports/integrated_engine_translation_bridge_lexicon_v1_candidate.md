# Integrated Engine Translation Bridge Lexicon v1 Candidate

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This is a provisional bridge lexicon v1 candidate.

It rereads v0 and strengthens preservation conditions for high-risk flattening entries. It is still not a final glossary, UI copy, wording patch source, baseline term replacement, external translation rule, scaffold contract, manifest contract, or promotion gate.

## 1. reread boundary

This candidate keeps the same 15 entries from v0.

The reread changed the emphasis:

- stronger distinction between state terms
- thicker authority boundary for Gemini/Codex/User handoff terms
- less UI-copy-like phrasing in bridge notes
- more explicit "what breaks if flattened" boundary reminders

Use this as a preservation aid only.

## 2. entries

### 2.1 `workspace ownership`

- internal term: `workspace ownership`
- internal role or meaning: Authority / boundary term. It binds workspace path, write permission, artifact status, and promotion path together.
- why it matters in the integrated engine: It prevents proposal material, canonical reports, scaffold files, manifests, and status documents from becoming interchangeable just because they are all in the same repo.
- what must be preserved: provenance, write authority, canonicalization boundary, and collision prevention.
- flattening risk: becomes folder assignment, owner label, repo hygiene, or "who works where."
- boundary reminder: a path is not only a location. In this context it signals whether material is proposal-only, canonical report, scaffold, manifest evidence, or closed scope.
- provisional human bridge note: When explaining this, start by saying what kind of authority the material has before saying where it lives. The important point is not the folder name; it is whether the material may act on core.
- do-not-reduce-to: folder 담당, owner field, file organization, convenience path.
- scenario scope: handoff / cross-scenario.
- confidence level: high, with high flattening risk.
- evidence source(s): `integrated_engine_real_handoff_retention_check_v0.md`, `integrated_engine_real_handoff_human_explanation_trial_v0.md`, `integrated_engine_human_bridge_seed_list_v0.md`, `integrated_engine_translation_friction_log_v0.md`.

### 2.2 `needs Codex translation`

- internal term: `needs Codex translation`
- internal role or meaning: Authority / validation term. It means material must be converted into baseline-safe form before any current-core use.
- why it matters in the integrated engine: It blocks direct Gemini-to-core movement and forces route, authority, state, boundary, and collision checks.
- what must be preserved: classification work, baseline fit check, conflict detection, hold/carry-forward distinction, and user-decision boundary.
- flattening risk: becomes review, summary, relay, wording cleanup, or "Codex makes it nicer."
- boundary reminder: translation changes operating status. It can produce usable-now, needs-translation, carry-forward, reject/conflict, or needs-user-decision outcomes.
- provisional human bridge note: Explain this as Codex deciding what status the material can safely have under the current baseline. Do not describe it as just rewriting or passing along.
- do-not-reduce-to: simple 전달, review, summary, cleanup.
- scenario scope: handoff / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_real_handoff_grammar_classification_v0.md`, `integrated_engine_real_handoff_retention_check_v0.md`, `integrated_engine_internal_language_grammar_candidate_v0.md`.

### 2.3 `proposal-only`

- internal term: `proposal-only`
- internal role or meaning: Authority / state term. It marks material as valuable possible input with no direct core authority.
- why it matters in the integrated engine: It lets Gemini or other support sources expand the possibility space without moving the baseline.
- what must be preserved: non-canonical status, no direct implementation, no automatic promotion, and required translation before use.
- flattening risk: becomes draft, weak output, almost-approved material, or pending work.
- boundary reminder: proposal-only material can be useful and still unable to act. Value and authority are separate.
- provisional human bridge note: Explain the material's status before explaining its content. It may be useful, but it has not earned baseline authority.
- do-not-reduce-to: draft, low-quality idea, pending approval, ready-to-use mock.
- scenario scope: handoff.
- confidence level: high.
- evidence source(s): `integrated_engine_real_gemini_handoff_artifact_v0.md`, `integrated_engine_real_handoff_retention_check_v0.md`, `integrated_engine_translation_friction_log_v0.md`.

### 2.4 `collision stop condition`

- internal term: `collision stop condition`
- internal role or meaning: Boundary / validation brake. It stops a handoff route when continuing would require unauthorized core drift or authority mixing.
- why it matters in the integrated engine: It protects the current baseline from being changed by visual appeal, agent confidence, runtime assumptions, or parallel writes.
- what must be preserved: route brake, baseline protection, explicit reason, and possible carry-forward of non-conflicting value.
- flattening risk: becomes error handling, blocked task, failure, tool problem, or "stop if something is wrong."
- boundary reminder: collision stop is not generic failure. It says the current route cannot safely continue under current scope.
- provisional human bridge note: State first which boundary would be crossed. Then state whether the material is reject/conflict, carry-forward, or needs user decision.
- do-not-reduce-to: bug, failure, simple stop, tool crash, generic blocker.
- scenario scope: handoff / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_real_handoff_grammar_classification_v0.md`, `integrated_engine_real_handoff_retention_check_v0.md`, `integrated_engine_translation_friction_log_v0.md`.

### 2.5 `hold`

- internal term: `hold`
- internal role or meaning: State / boundary term. It keeps material outside current core and current package while preserving it as readable future material.
- why it matters in the integrated engine: It supports expansion without letting expansion become implementation.
- what must be preserved: active boundary, current non-promotion, future readability, no build-mode entry.
- flattening risk: becomes discarded, ignored, unused, backlog, or "not important."
- boundary reminder: hold is not an outcome of low value. It is a current-scope decision.
- provisional human bridge note: Explain what remains closed and why it remains closed. Then say the material is still kept as space material for future reread.
- do-not-reduce-to: 버림, unused, backlog, no value.
- scenario scope: handoff / cross-scenario.
- confidence level: medium-high.
- evidence source(s): `integrated_engine_internal_language_grammar_candidate_v0.md`, `integrated_engine_real_handoff_retention_check_v0.md`, `integrated_engine_current_hold_and_watch_registry_v0.md`.

### 2.6 `carry-forward`

- internal term: `carry-forward`
- internal role or meaning: State / future-material term. It preserves material as future-readable without giving it current operating authority.
- why it matters in the integrated engine: It prevents loss of useful material while blocking premature extension promotion.
- what must be preserved: future value, no current implementation, no automatic promotion, later gate required.
- flattening risk: becomes approved later, backlog, deferred feature, or "we will do this."
- boundary reminder: carry-forward is preservation, not commitment.
- provisional human bridge note: Explain that the material remains available for future reread. Avoid implying that implementation is scheduled or already accepted.
- do-not-reduce-to: approved later, roadmap item, task backlog, deferred feature.
- scenario scope: handoff / cross-scenario.
- confidence level: medium-high.
- evidence source(s): `integrated_engine_real_gemini_handoff_artifact_v0.md`, `integrated_engine_real_handoff_retention_check_v0.md`, `integrated_engine_internal_language_pattern_inventory_v0.md`.

### 2.7 `reject / conflict`

- internal term: `reject / conflict`
- internal role or meaning: Validation / boundary result. It marks material that cannot enter current core because it conflicts with active baseline rules.
- why it matters in the integrated engine: It records why a route stops without reducing the material to universal failure.
- what must be preserved: scoped conflict reason, current-baseline context, and distinction from hold/carry-forward.
- flattening risk: becomes bad idea, wrong, impossible, or useless.
- boundary reminder: reject/conflict means "not compatible here under current rules." It does not decide all future contexts.
- provisional human bridge note: Name the boundary it conflicts with. Do not judge the idea globally.
- do-not-reduce-to: bad, useless, impossible, failed.
- scenario scope: handoff / cross-scenario.
- confidence level: medium-high.
- evidence source(s): `integrated_engine_real_handoff_grammar_classification_v0.md`, `integrated_engine_real_gemini_handoff_artifact_v0.md`.

### 2.8 `not promoted`

- internal term: `not promoted`
- internal role or meaning: State / gate term. It means the candidate has not crossed into patch planning, core status, or stable extension status.
- why it matters in the integrated engine: It keeps observed material visible without changing operating mode.
- what must be preserved: gate not crossed, no patch planning, no automatic rejection, candidate still readable.
- flattening risk: becomes rejected, ignored, closed forever, or "decided no."
- boundary reminder: not promoted can coexist with watch keep, hold, or carry-forward; it only says the promotion gate is not open.
- provisional human bridge note: Explain that the candidate remains below the promotion line. Avoid implying that it has been discarded.
- do-not-reduce-to: rejected, forgotten, closed forever.
- scenario scope: S2 / use observation / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_current_use_state_refresh_v0.md`, `integrated_engine_current_hold_and_watch_registry_v0.md`, `integrated_engine_internal_language_grammar_candidate_v0.md`.

### 2.9 `watch keep`

- internal term: `watch keep`
- internal role or meaning: State / observation term. It keeps a candidate under observation without opening patch planning or build mode.
- why it matters in the integrated engine: It prevents recoverable ambiguity from becoming premature wording or structure work.
- what must be preserved: active observation, no immediate action, official re-entry conditions, no patch queue.
- flattening risk: becomes TODO, bug watch, patch candidate, low-priority task, or backlog.
- boundary reminder: watch keep records evidence need. It does not authorize a change.
- provisional human bridge note: Explain what evidence would reopen the gate. If no re-entry condition is met, the item stays watched only.
- do-not-reduce-to: TODO, bug, patch candidate, backlog.
- scenario scope: S2 / use observation / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_current_use_state_refresh_v0.md`, `integrated_engine_current_hold_and_watch_registry_v0.md`, `integrated_engine_internal_language_grammar_candidate_v0.md`.

### 2.10 `user decision / package opening authority`

- internal term: `user decision / package opening authority`
- internal role or meaning: Authority / route-opening term. It marks that only the user can open the next operating package or promotion path.
- why it matters in the integrated engine: It prevents proposal, Codex classification, or bridge explanation from becoming autonomous action.
- what must be preserved: route-opening authority, package scope, mode transition, and closed-scope protection.
- flattening risk: becomes approval, permission, sign-off, or acceptance.
- boundary reminder: user decision does not merely approve content; it opens or keeps closed an operating route.
- provisional human bridge note: Explain which route the user is or is not opening. Avoid treating the decision as a generic approval stamp.
- do-not-reduce-to: approval click, permission, sign-off.
- scenario scope: handoff / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_real_handoff_human_explanation_trial_v0.md`, `integrated_engine_real_handoff_grammar_classification_v0.md`, `integrated_engine_internal_language_grammar_candidate_v0.md`.

### 2.11 `return validation`

- internal term: `return validation`
- internal role or meaning: Route / validation term. It names the point where engine return material is checked before user decision, reflux, or reprocess.
- why it matters in the integrated engine: It keeps engine output from becoming final completion or final authority.
- what must be preserved: VectorFL-side validation ownership, route selector role, separation from engine execution.
- flattening risk: becomes checking, QA, result review, or engine self-validation.
- boundary reminder: engine creates return material; validation decides next route.
- provisional human bridge note: Say what can happen after validation: user decision, reflux, or reprocess. This prevents "result done" reading.
- do-not-reduce-to: engine check, result done, QA only.
- scenario scope: S1 / S2 / S3 / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_internal_language_grammar_candidate_v0.md`, `integrated_engine_translation_friction_log_v0.md`, `integrated_engine_language_amplification_harvest_v0.md`.

### 2.12 `anchor drift`

- internal term: `anchor drift`
- internal role or meaning: Boundary / validation brake. It marks anchor-fit mismatch that can hold closure and trigger reprocess.
- why it matters in the integrated engine: It proves anchor criteria can change route behavior.
- what must be preserved: comparison against anchor, route brake, reprocess possibility, loop remaining open.
- flattening risk: becomes warning, mismatch label, reference issue, or advisory note.
- boundary reminder: anchor drift can stop progression; it is not just information beside the route.
- provisional human bridge note: Name the anchor-fit break and the route consequence together. Do not describe only the mismatch.
- do-not-reduce-to: warning, mismatch label, advisory note.
- scenario scope: S3 / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_translation_friction_log_v0.md`, `integrated_engine_internal_language_grammar_candidate_v0.md`, `integrated_engine_language_amplification_harvest_v0.md`.

### 2.13 `reflux`

- internal term: `reflux`
- internal role or meaning: Route / maturation preservation term. It routes maturation-worthy material back toward space with a reason for future reread.
- why it matters in the integrated engine: It separates maturation preservation from completion, archive, rollback, or residue.
- what must be preserved: route direction, preservation reason, future growth value, packet role.
- flattening risk: becomes archive, save for later, rollback, leftover, or storage.
- boundary reminder: reflux is active route material, not passive storage.
- provisional human bridge note: Keep both movement and reason visible: material returns to space because it still has maturation value.
- do-not-reduce-to: archive, rollback, leftover, 저장.
- scenario scope: S1 / S3 / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_translation_friction_log_v0.md`, `integrated_engine_human_bridge_seed_list_v0.md`, `integrated_engine_language_amplification_harvest_v0.md`.

### 2.14 `current_loop_state`

- internal term: `current_loop_state`
- internal role or meaning: State / current-position term. It locates the active loop without claiming to be the full movement history.
- why it matters in the integrated engine: It lets manual operation continue without turning state into trace UI or event timeline.
- what must be preserved: current position, minimal state, need for connection records to reconstruct movement.
- flattening risk: becomes full workflow history, timeline, event log, or runtime trace.
- boundary reminder: current loop state answers "where is the loop now?" not "everything that happened."
- provisional human bridge note: Explain the current position first. If route history is needed, point to packets and panel connection records.
- do-not-reduce-to: full history, event log, trace UI.
- scenario scope: S1 / S2 / S3 / cross-scenario.
- confidence level: high.
- evidence source(s): `integrated_engine_internal_language_grammar_candidate_v0.md`, `integrated_engine_translation_friction_log_v0.md`, `integrated_engine_language_amplification_harvest_v0.md`.

### 2.15 `support reread recovery`

- internal term: `support reread recovery`
- internal role or meaning: Reread / support term. It describes how intended meaning can recover through ordered reread without changing structure.
- why it matters in the integrated engine: It separates recoverable thinness from patch-worthy confusion or feature gap.
- what must be preserved: reading order, recovery condition, no automatic patch, no selected-object or trace UI implication.
- flattening risk: becomes "read more docs," documentation workaround, hidden complexity, or feature need.
- boundary reminder: recovery is valid only if support reread restores route/authority/state/boundary without structural change.
- provisional human bridge note: State what recovered and what support material made it recover. Do not turn recovery into a demand for new UI behavior.
- do-not-reduce-to: documentation workaround, trace UI need, selected-object drilldown.
- scenario scope: S2 / S3 / handoff / cross-scenario.
- confidence level: medium-high.
- evidence source(s): `integrated_engine_real_handoff_retention_check_v0.md`, `integrated_engine_translation_friction_log_v0.md`, `integrated_engine_internal_language_grammar_candidate_v0.md`.

## 3. v1 candidate closeout

This candidate remains provisional.

Compared with v0, the main improvement is that high-risk entries now lead with operating status and boundary consequence before explanation smoothness.

Still high-risk:

- `workspace ownership`
- `hold`
- `carry-forward`
- `reject / conflict`
- `collision stop condition`
- `watch keep`

The lexicon is now safer for a usage trial, but still not ready for final glossary or UI wording work.
