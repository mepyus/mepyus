# Formation-Movement Interface External Reference Ingest Validation Case v0

Date: 2026-04-24

## 1. status

- `validation_case`
- `dry_run_only`
- `no package modification`
- `no implementation`
- `no schema enforcement`
- `no baseline lock`
- `no external reference promotion`

Source package:

- `docs/reports/formation_movement_interface_package_draft_v0.md`

Validation target:

- Test whether an external reference can enter as an `unclassified` seed sidecar, then become a formed sidecar / framing candidate without increasing operator burden.
- Test whether promotion is blocked, prepare/execute remains separated, and User Surface stays light.

## 2. case setup

Sample reference:

> 멀티 에이전트나 외부 worker는 자유롭게 풀어두면 혼선이 생기므로, 각 worker에게 명확한 역할, 경계, 반환 형식을 주어야 한다.

Scenario:

- An external reference enters the space.
- The user wants to know whether it strengthens B, the boundary-surface / role-organization principle.
- Direct promotion, baseline reflection, and operating-rule elevation are forbidden.
- The purpose is to capture the reference as a provisional object and run it through the sidecar lifecycle without making the user do object classification work.

Boundary:

- No actual external reference file movement or modification.
- No direct B evidence promotion.
- No baseline or operating rule change.
- No execution or worker handoff.

## 3. seed sidecar application

Operational minimum only:

```text
current_purpose: 외부 reference가 B 후보를 보강하는지 확인
source_trace: external_reference_ingest_dry_run_sample
initial_boundary: promotion 금지, B 확정 금지, 역할/위치 판정만 허용
object_type: unclassified
```

Validation points:

- PASS: seed stage does not force final `object_type`.
- PASS: `object_type: unclassified` is only a temporary seed marker.
- PASS: the user is not asked to fill Core 7.
- PASS: user input stays at `current_purpose`, `source_trace`, and `initial_boundary` level.

Operator note:

The external reference is captured without asking the user whether it is B evidence, defensive logic, comparison material, or action input.

## 4. formed sidecar application

VectorFL rereads the reference and attaches provisional identity.

Candidate formed sidecar:

```text
object_type: framing_candidate
provisional_status: candidate_with_promotion_barrier
boundary: use only as comparison frame for B; no B lock; no axis promotion; no operating rule creation
next_allowed_move: compare_only
needed_reread_question: Is this direct evidence for B, or defensive logic that protects role-bound organization from agent freedom drift?
candidate_role: role-bound external worker comparison frame
source_trace: external_reference_ingest_dry_run_sample
```

Reread questions:

- Is this reference direct evidence for B?
- Or is it defensive logic that protects B from agent-freedom drift?
- Do A/C/T/X/R/L relations still need to be separated before any B claim?
- Can it become `framing_candidate` now, or should it remain `reread_priority`?

Dry-run judgment:

`PASS_WITH_NOTE`: The reference can become `framing_candidate` because the role-bound worker comparison is visible. However, it must retain a promotion barrier because the reference may also express A-like premature freedom suppression or X-like return-format translation logic.

## 5. framing candidate judgment

Transition condition check:

- repeated signal: PASS_WITH_NOTE. The signal matches existing CLI/external-worker boundary concerns, but this dry-run does not reread actual internal records.
- current purpose connection: PASS. It directly connects to B candidate evaluation.
- candidate_role: PASS. `role-bound external worker comparison frame`.
- promotion_barrier: PASS. Explicitly blocks B evidence promotion.

Framing sidecar:

```text
object_type: framing_candidate
provisional_status: PASS_WITH_NOTE
candidate_role: role-bound external worker comparison frame
promotion_barrier: 내부 CLI/외부도구 부착 기록에서 설명력과 재배치력을 확인하기 전까지 B 증거로 승격 불가
next_allowed_move: compare_only
reread_return_hook: compare against internal CLI/external tool attachment records before any B promotion claim
source_trace: external_reference_ingest_dry_run_sample
```

Judgment:

`PASS`: The object can be a framing candidate without becoming promoted evidence.

## 6. bounded action candidate possibility

Possible action question:

> 이 reference를 기준으로 내부 CLI/외부도구 부착 기록에서 B가 A에 흡수되는지, 독립 조직 축으로 남는지 비교하라.

Transition condition check:

- actionable_question: PASS
- boundary: PASS. Compare only; no B lock; no baseline or operating-rule update.
- expected_return_form: PASS_WITH_NOTE. A report shape can be drafted, but no worker packet is created in this dry-run.
- return_hook: PASS. Return should come back to VectorFL as validation material for B/A/C/T/X/R/L relation reread.

Bounded action candidate preview:

```text
object_type: bounded_action_candidate
provisional_status: prepare_possible
next_allowed_move: prepare_worker_packet
action_shape: comparative reread report draft
boundary: internal comparison only; no B promotion; no baseline update; no schema or rule creation
guardrail: report draft only; no execution in this dry-run
expected_return_form: verdict + compared internal scenes + B evidence candidate + A/C/T/X/R/L overlap + unresolved questions
reread_return_hook: return as validation_return before any promotion or rule decision
```

Prepare/execute note:

- This is `allowed_to_prepare`, not `allowed_to_execute`.
- No `guarded_execution` is created.
- A real Codex one-shot or worker handoff is outside this dry-run.

Judgment:

`PASS_WITH_NOTE`: The reference can support a bounded action candidate, but only as a future preparation step.

## 7. surface-specific visibility application

### A. User Surface judgment card

```text
현재 판정: 이 reference는 B 후보와 닿지만, 아직 B 증거로 승격하지 않습니다.
이유: role/boundary/return-format 신호는 강하지만 A/C/T/X/R/L 관계가 아직 분리되지 않았습니다.
다음 이동: VectorFL면에서 비교 frame으로 보존하고 내부 CLI/외부도구 기록과 대조합니다.
금지선: B 확정, baseline 반영, operating rule 승격, 실행 지시는 금지입니다.
```

Check:

- PASS: User Surface stays to 4 lines.
- PASS: User Surface does not expose full sidecar detail.

### B. VectorFL Surface view

```text
object_type: framing_candidate
provisional_status: PASS_WITH_NOTE
boundary: comparison frame only; no B lock; no axis promotion; no operating rule creation
needed_reread_question: Is this direct B evidence, B-protective defensive logic, or X-style return-format translation support?
candidate_role: role-bound external worker comparison frame
promotion_barrier: cannot promote to B evidence before internal CLI/external tool records show explanatory and relocation force
source_trace: external_reference_ingest_dry_run_sample
next_allowed_move draft: compare_only / prepare_worker_packet only if bounded comparison question is accepted
```

Check:

- PASS: VectorFL sees full formation sidecar.
- PASS_WITH_NOTE: VectorFL must preserve A/C/T/X/R/L overlap instead of collapsing the reference into B.

### C. Engine Surface view

No execution in this case.

```text
action_shape 후보: comparative reread report draft
execution_constraint: not_attached_yet / not_executable_yet
guardrail: no execution; no B promotion; no baseline update; report preview only
expected_return_form 후보: verdict + compared scenes + B/A/C/T/X/R/L overlap + unresolved questions
fallback_policy 필요 여부: yes, required before execution
trust_scope 필요 여부: yes, required before execution
reread_return_hook: return any future comparison as validation_return to VectorFL
```

Check:

- PASS: Engine Surface clearly shows not executable yet.
- PASS: preparation candidate does not become execution.

### D. Return / Validation Surface view

Short validation return for this dry-run:

```text
observed_result: External reference ingest can start as unclassified seed, become framing_candidate, and preview bounded_action_candidate without user-side object typing or promotion.
reread_trigger: Recheck against actual internal CLI/external tool attachment records before any B evidence claim.
next_recommended_state: keep as framing_candidate; optionally prepare bounded comparison packet later
```

Check:

- PASS: short validation return is enough because no execution, promotion, baseline, or schema change occurred.

## 8. prepare vs execute check

- PASS: formed sidecar is not execution permission.
- PASS: `framing_candidate` is not execution permission.
- PASS: `bounded_action_candidate` preview is `allowed_to_prepare`, not `allowed_to_execute`.
- PASS: `allowed_to_execute` would require `execution_constraint`, `guardrail`, `fallback_policy`, `trust_scope`, `expected_return_form`, and `reread_return_hook`.
- PASS: this dry-run does not promote the object to `guarded_execution`.

## 9. short validation return application

Short validation return:

```text
observed_result: The package handled external reference ingest without making the user classify the object or fill Core 7.
reread_trigger: Compare with real internal CLI/external tool scenes before any B promotion or bounded worker packet.
next_recommended_state: framing_candidate with optional future bounded_action_candidate preparation
```

Full validation return trigger check:

- B promotion risk: present but controlled by promotion barrier; no full return needed for this dry-run.
- baseline risk: not triggered.
- schema enforcement risk: not triggered.
- worker boundary drift: not triggered because no worker ran.
- expected-return deviation: not applicable because no worker output exists.
- User Surface flattening / R loss: not triggered; User Surface stayed compact.
- object type change / downgrade / hold: not required in this dry-run.

Judgment:

`PASS_WITH_NOTE`: short validation return is adequate, but actual comparison against internal records should likely use full validation if it changes B trust scope.

## 10. transition check

| transition | verdict | reason |
| --- | --- | --- |
| unclassified seed -> formed sidecar | PASS | Seed used only operational minimum; VectorFL assigned provisional identity. |
| formed sidecar -> reread_priority or framing_candidate | PASS_WITH_NOTE | `framing_candidate` is justified, but A/C/T/X/R/L overlap requires note. |
| reread_priority -> framing_candidate | PASS_WITH_NOTE | If the object had started as reread-only, the visible B relation and candidate role would allow framing; promotion barrier remains required. |
| framing_candidate -> bounded_action_candidate | PASS_WITH_NOTE | Actionable comparison question exists, but this dry-run only previews preparation. |
| bounded_action_candidate -> guarded_execution | HOLD | Execution constraints, fallback policy, and trust scope are not attached; no execution allowed. |
| short validation return -> full validation return needed? | PASS_WITH_NOTE | Short return is enough now; full return needed if actual internal comparison changes B trust scope or creates promotion risk. |

## 11. operator cost check

Required questions:

- User-filled fields: 3 fields at seed stage: `current_purpose`, `source_trace`, and `initial_boundary` / `why_now`.
- Did the user choose `object_type`? No.
- Was Core 7 required from the user? No.
- Did User Surface show only a 3-4 line judgment card? Yes.
- Was the reference directly promoted? No.
- Were `allowed_to_prepare` and `allowed_to_execute` confused? No.

Cost verdict:

`PASS`

Reason:

The package kept external reference ingest from becoming operator-heavy. The user provides purpose and boundary context, while VectorFL handles classification and promotion barrier management.

## 12. verdict

`PASS_WITH_NOTE`

Reason:

The package successfully handled the external reference as a provisional object without direct promotion, user-side object typing, or execution drift. The note is that `framing_candidate` was possible partly because the sample reference is already close to B; weaker references may need to remain `reread_priority` longer.

## 13. findings

### What worked

- `unclassified` seed sidecar was sufficient for first capture.
- User did not need to fill Core 7.
- VectorFL could assign `framing_candidate` after reread.
- Promotion barrier prevented direct B evidence elevation.
- Surface-specific visibility kept User Surface light.
- Prepare and execute remained separated.
- Short validation return was enough for a low-risk dry-run.

### What was too heavy

- Full A/C/T/X/R/L overlap language may be too dense for User Surface, but it stayed in VectorFL Surface.
- Promotion barrier wording is substantial, but necessary because this reference strongly tempts B promotion.

### What remained ambiguous

- Whether the reference should first remain `reread_priority` for one more pass before `framing_candidate`.
- Whether B relation is direct evidence, defensive logic, or X-style return-format support.
- Whether future internal comparison should be a small report or a fuller package validation.

### What should not be changed yet

- Do not change Core 7.
- Do not add new object families.
- Do not modify the package based on this single external-reference dry-run.
- Do not create an ingest schema or manifest from this case.
- Do not promote B based on this sample.

### What may need a later package patch

- Add a small rule for when an external reference should remain `reread_priority` instead of becoming `framing_candidate`.
- Add examples distinguishing direct evidence, defensive logic, and comparison frame.
- Add a trigger for when external-reference comparison should require full validation return.

## 14. no-change rule

This report does not modify the package document.

Recommended future patches are listed only as future candidates. They are not applied here.

## 15. intentionally not changed

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- No baseline lock
- No schema enforcement
- No implementation
- No runtime manifest
- No validator or script
- No external reference file movement or modification
- No B promotion

## 16. unresolved questions

- Is `unclassified` seed enough for weaker or noisier external references?
- Should B-adjacent references default to `reread_priority` before `framing_candidate` unless repeated internal scenes are already known?
- What is the boundary between B direct evidence and B-protective defensive logic?
- When should A/C/T/X/R/L overlap force a hold instead of a framing candidate?
- Should future bounded comparison use short validation unless B trust scope changes, or should B-adjacent comparison default to full validation?
