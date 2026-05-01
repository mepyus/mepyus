# Formation-Movement Interface Codex One-Shot Validation Case v0

Date: 2026-04-24

## 1. status

- `validation_case`
- `dry_run_only`
- `no package modification`
- `no implementation`
- `no schema enforcement`
- `no baseline lock`

Source package:

- `docs/reports/formation_movement_interface_package_draft_v0.md`

Validation target:

- Whether the package, including the addendum, can handle a Codex one-shot preparation case without becoming too heavy.
- Whether sidecar maturity, operational minimum, surface-specific visibility, prepare/execute separation, and short validation return work in practice.

## 2. case setup

Scenario:

- The user wants to pass a specific task to Codex.
- The task is not ready for direct execution.
- The correct current move is to prepare a Codex one-shot packet.
- The one-shot packet should later return as validation material, not as final truth.

Purpose:

Prepare a Codex one-shot instruction draft and recover the result as a `validation_return`.

Boundary:

- No actual Codex execution in this dry-run.
- No package document modification.
- No schema lock.
- No baseline lock.
- No runtime manifest or validator generation.

## 3. seed sidecar application

Operational minimum only:

```text
current_purpose: prepare a Codex one-shot instruction draft for a bounded task
source_trace: user request + formation_movement_interface_package_draft_v0 addendum
initial_boundary: preparation only; no execution; no baseline/schema/package modification
```

Seed-stage rule check:

- `object_type` is not forced at seed stage.
- `object_type` may remain omitted or `unclassified`.
- Core 7 is not required at creation time.

Validation note:

This keeps the first capture lightweight. The user only contributes purpose and boundary context; VectorFL later performs object typing.

## 4. formed sidecar application

After VectorFL reread, the object can be typed.

```text
object_type: bounded_action_candidate
provisional_status: PASS_WITH_NOTE-ready
boundary: prepare a one-shot instruction draft only; do not execute; do not mutate package docs; do not lock schema
next_allowed_move: prepare_worker_packet
needed_reread_question: Is the requested Codex handoff bounded enough to become a one-shot packet without becoming execution?
candidate_role: Codex one-shot preparation object
source_trace: user request + package draft sections 0-20 + addendum sections 21-22
```

Validation point:

- PASS: `object_type` was attached at the formed sidecar stage, not at seed.
- PASS_WITH_NOTE: `object_type` is usable but still revisable. If the handoff scope widens or lacks expected return form, this object should downgrade to `framing_candidate` or return to reread.

## 5. motion sidecar application

The object can move into preparation, not execution.

```text
object_type: bounded_action_candidate
provisional_status: prepare_ready
next_allowed_move: prepare_worker_packet
action_shape: draft a Codex one-shot instruction packet
guardrail: preparation only; no execution; no package modification; no schema lock; no baseline lock
expected_return_form: one-shot instruction draft + explicit boundary + expected output + no-execute note + unresolved questions
reread_return_hook: VectorFL rereads the draft as validation_return before any execution decision
```

Prepare/execute distinction:

```text
allowed_to_prepare: yes
allowed_to_execute: no
```

Reason:

- `prepare_worker_packet` is a preparation move.
- Execution still requires `execution_constraint`, `guardrail`, `fallback_policy`, and `trust_scope`.
- This dry-run has a guardrail and expected return form, but does not yet define a full execution constraint, fallback policy, and trust scope sufficient for actual execution.

Execution requirements before later movement:

```text
execution_constraint: required before execution
guardrail: required before execution
fallback_policy: required before execution
trust_scope: required before execution
```

Validation point:

- PASS: the package prevents `prepare_worker_packet` from being misread as execute permission.

## 6. surface-specific visibility application

### A. User Surface judgment card

```text
현재 판정: 아직 실행이 아니라 Codex one-shot 준비 단계입니다.
이유: 목적과 경계는 보이지만 실행 constraint / fallback / trust scope가 충분하지 않습니다.
다음 이동: one-shot packet 초안을 준비하고 VectorFL면에서 다시 읽습니다.
금지선: 지금 바로 Codex 실행, baseline lock, schema 강제, package 문서 수정은 금지입니다.
```

Check:

- PASS: user-facing surface stays to 4 lines.
- PASS: User Surface is not asked to fill Core 7.

### B. VectorFL Surface view

```text
object_type: bounded_action_candidate
provisional_status: prepare_ready / PASS_WITH_NOTE-ready
boundary: one-shot packet preparation only; no execution; no package modification; no lock
needed_reread_question: Is this handoff bounded enough to remain preparation and not slip into execution?
candidate_role: Codex one-shot preparation object
promotion_barrier: cannot become guarded_execution until execution_constraint, fallback_policy, and trust_scope are explicit
source_trace: user request + formation_movement_interface_package_draft_v0
next_allowed_move draft: prepare_worker_packet
```

Check:

- PASS: VectorFL sees the full formation sidecar.
- PASS_WITH_NOTE: `promotion_barrier` is doing real work by blocking premature execution.

### C. Engine Surface view

```text
action_shape: draft Codex one-shot instruction packet
execution_constraint 여부: not ready / required before execution
guardrail: preparation only; no execution; no mutation; no schema/baseline lock
expected_return_form: one-shot draft + boundary + expected output + unresolved questions
fallback_policy 필요 여부: yes, required before execution
trust_scope 필요 여부: yes, required before execution
reread_return_hook: return draft to VectorFL for validation before execution
```

Check:

- PASS: Engine Surface receives movement-relevant fields only.
- PASS: missing execution fields are visible as blockers, not hidden assumptions.

### D. Return / Validation Surface view

Dry-run assumed observed result:

```text
observed_result: The one-shot preparation object can be represented without requiring full Core 7 from the user.
reread_trigger: Confirm whether prepared packet has enough execution_constraint / fallback_policy / trust_scope before any execution.
recommended_branch: refine
next_recommended_state: remain bounded_action_candidate; prepare packet draft; do not promote to guarded_execution yet
```

Check:

- PASS: Return view focuses on branch and next state, not full result prose.
- PASS_WITH_NOTE: if the actual one-shot draft later changes trust scope or creates promotion risk, this must become full validation return.

## 7. short validation return application

Short validation return for this dry-run:

```text
observed_result: Addendum reduced operator burden and prevented prepare/execute confusion in the Codex one-shot preparation case.
reread_trigger: Recheck before actual execution whether execution_constraint, fallback_policy, and trust_scope are explicit.
next_recommended_state: bounded_action_candidate / prepare_ready; not guarded_execution yet
```

Why short is enough here:

- No real execution happened.
- No baseline or schema changed.
- The dry-run only tested preparation semantics and visibility projection.
- Deviation analysis is not yet worth full validation cost.

Upgrade to full validation return if:

- promotion risk appears
- schema risk appears
- baseline risk appears
- worker or Codex crosses the boundary
- expected return form differs substantially from actual output
- object type or trust scope changes

## 8. transition check

| transition | verdict | reason |
| --- | --- | --- |
| seed sidecar -> formed sidecar | PASS | Seed used only operational minimum; VectorFL later attached object identity. |
| formed sidecar -> motion sidecar | PASS | Action shape, guardrail, expected return form, and reread return hook were enough for preparation. |
| allowed_to_prepare -> allowed_to_execute | HOLD | Preparation is allowed, but execution lacks explicit execution constraint, fallback policy, and trust scope. |
| motion sidecar -> return sidecar | PASS_WITH_NOTE | Dry-run return can be short because no execution occurred; full return needed if actual worker output changes scope. |
| return sidecar -> refined sidecar / hold / downgrade / archive_as_residue | PASS_WITH_NOTE | Recommended branch is refine: keep as bounded action candidate and add execution blockers before any guarded execution. |

## 9. operator cost check

Required questions:

- User-filled fields: 3 fields at seed stage: `current_purpose`, `source_trace`, and `initial_boundary` / `why_now`.
- User Surface exposure: yes, only a 4-line judgment card.
- Core 7 demanded from user: no.
- `object_type` selection delegated to user: no.
- Prepare and execute separated: yes.

Cost verdict:

`PASS`

Reason:

The addendum materially reduces operator burden. The user does not fill a schema, does not select `object_type`, and does not need to reason about execution readiness beyond seeing the guardrail card.

## 10. verdict

`PASS_WITH_NOTE`

Reason:

The package works for a Codex one-shot preparation case without becoming too heavy. The addendum successfully prevents three major failures:

- Core 7 being treated as a creation-time form
- `prepare_worker_packet` being treated as execution permission
- every validation return becoming a full report

The remaining note is that actual execution still needs a sharper conversion from `bounded_action_candidate` to `guarded_execution`.

## 11. findings

### What worked

- Operational minimum was enough at seed stage.
- `object_type` could be delayed until VectorFL reread.
- Surface-specific visibility kept User Surface light while preserving full VectorFL detail.
- `allowed_to_prepare` vs `allowed_to_execute` blocked premature execution.
- Short validation return was sufficient for a no-execution dry-run.

### What was too heavy

- Full VectorFL sidecar is too heavy for User Surface, but the addendum already prevents this exposure.
- Requiring `promotion_barrier` for every formed object may be heavy in small cases; it is useful here because execution drift is plausible.

### What remained ambiguous

- Whether `allowed_to_prepare` and `allowed_to_execute` should become explicit fields or inferred states.
- When exactly a prepared one-shot draft becomes `guarded_execution`.
- Whether `trust_scope` belongs in preparation preview or only in execution readiness.

### What should not be changed yet

- Do not change Core 7.
- Do not add a formal schema.
- Do not modify the package draft based on one dry-run.
- Do not turn short validation return into another mandatory template.

### What may need a later package patch

- Add a small note clarifying when `bounded_action_candidate` becomes `guarded_execution`.
- Add an example of `unclassified` seed sidecar.
- Add a lightweight rule for when short validation return must be upgraded to full validation return.

## 12. no-change rule

This report does not modify the package document.

Recommended future patches are listed only as future candidates. They are not applied here.

## 13. intentionally not changed

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- Package status: `package_candidate` / `PASS_WITH_NOTE-ready`
- No baseline lock
- No schema enforcement
- No implementation
- No runtime manifest
- No validator/script

## 14. unresolved questions

- Should `allowed_to_prepare` and `allowed_to_execute` be explicit fields?
- What is the exact readiness threshold from `bounded_action_candidate` to `guarded_execution`?
- Should `trust_scope` be drafted during preparation or only required at execution readiness?
- What is the minimum `unclassified` seed sidecar syntax?
- What concrete event auto-upgrades short validation return to full validation return?
