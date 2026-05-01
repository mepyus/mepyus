# Formation-Movement Interface Weak-Signal Stress Test v0

Date: 2026-04-24

## 1. overall verdict

`PASS_WITH_NOTE`

Reason:

The package survives weak-signal and ambiguous cases without collapsing into automatic promotion. It consistently allows `unclassified` seed capture, delays `object_type` commitment, blocks promotion under weak evidence, and uses `reread_priority`, `hold`, `refine`, and `archive_as_residue` as natural non-promotion branches. The note is that some thresholds remain soft enough that a permissive operator could still over-read weak signals unless more examples are added.

## 2. generated file path

`docs/reports/formation_movement_interface_weak_signal_stress_test_v0.md`

## 3. tested weak-signal cases

- Case A. Weak B-adjacent external reference
- Case B. Too-smooth user surface explanation
- Case C. Ambiguous Codex request without boundary
- Case D. A/C/T/X/R/L overlap case

## 4. case-by-case stress test

### Case A. weak B-adjacent external reference

#### 1. case setup

Situation:

An external reference says only that good agent systems should have clear roles.

Why weak-signal:

- it touches B, but only at a generic level
- it does not directly explain internal records
- it does not show relocation force
- it can easily be over-read as B evidence

Promotion risk:

- high, because the wording is intuitively close to B
- weak, because actual explanatory force is not shown

#### 2. seed sidecar

```text
current_purpose: check whether a generic role-clarity reference meaningfully helps B candidate reading
source_trace: weak_b_adjacent_external_reference_sample
initial_boundary: no B evidence claim, no promotion, no operating-rule use
object_type: unclassified
```

#### 3. formed sidecar

```text
object_type: reread_priority
provisional_status: hold_for_role_clarification
boundary: generic external support only; no B confirmation; no rule elevation
next_allowed_move draft: reread_only / compare_later
needed_reread_question: Is this actual B support, or only vague role-discipline language with no internal explanatory force?
source_trace: weak_b_adjacent_external_reference_sample
```

Judgment:

- `framing_candidate` is too early here
- `reread_priority` is healthier because the signal is generic and under-differentiated

#### 4. surface-specific visibility

User Surface judgment card:

```text
현재 판정: 이 reference는 B와 닿아 보이지만 아직 약한 일반론입니다.
이유: 역할 명확성은 말하지만 내부 장면 설명력이나 재배치력은 아직 없습니다.
다음 이동: 우선 reread 대상으로 보관하고, 나중에 내부 기록과 비교합니다.
금지선: B 증거, 축 확정, operating rule 승격은 금지입니다.
```

VectorFL Surface view:

```text
object_type: reread_priority
provisional_status: hold_for_role_clarification
boundary: generic support only; no B confirmation
needed_reread_question: Is this more than generic role-discipline advice?
instability_reason: direct evidence / defensive logic / comparison frame distinction is too weak
source_trace: weak_b_adjacent_external_reference_sample
next_allowed_move draft: reread_only / compare_later
```

Return / Validation view:

```text
observed_result: Weak B-adjacent reference did not force framing or promotion.
reread_trigger: compare against real internal B-adjacent scenes before any stronger classification.
next_recommended_state: keep as reread_priority or archive_as_residue if no internal explanatory match appears
```

#### 5. transition check

| transition | verdict | reason |
| --- | --- | --- |
| seed -> formed | PASS | unclassified seed safely moved into reread_priority. |
| formed -> reread_priority / framing_candidate / bounded_action_candidate | PASS | reread_priority was chosen instead of permissive framing. |
| allowed_to_prepare 여부 | HOLD | no action question or return form is strong enough yet. |
| allowed_to_execute 여부 | FAIL-safe / disallowed | nothing close to execution exists here. |
| short validation return sufficient? | PASS | low-risk, no action, no promotion, no schema change. |
| full validation return needed? | HOLD | only if later comparison tries to make it B evidence. |
| final branch | PASS | hold or archive_as_residue both remain natural. |

#### 6. operator cost check

- user-filled fields: 3
- user chose `object_type`: no
- full Core 7 required: no
- User Surface only 3-4 line card: yes
- judgment burden moved to VectorFL: yes

#### 7. promotion risk check

- over-promotion occurred: no
- promotion treated as default: no
- non-promotion branches worked: yes, strongly

#### 8. verdict

`PASS`

Reason:

The package correctly refuses to turn a weak generic reference into B evidence.

### Case B. too-smooth user surface explanation

#### 1. case setup

Situation:

The explanation is: "통합엔진은 네 생각을 정리하고 AI 작업을 도와주는 시스템이야."

Why weak-signal:

- it is easy to understand
- it feels successful on first read
- but it removes most structural residue

Promotion risk:

- high, because friendly phrasing can be reused as final wording too early

#### 2. seed sidecar

```text
current_purpose: test whether a very smooth user explanation is acceptable or flattening
source_trace: too_smooth_user_surface_explanation_sample
initial_boundary: no final definition, no baseline wording, draft only
object_type: unclassified
```

#### 3. formed sidecar

```text
object_type: bounded_action_candidate
provisional_status: explanation_draft_under_review
boundary: user-surface draft only; no baseline wording; no final definition
next_allowed_move draft: validate_draft_quality
needed_reread_question: Is this acceptable simplification or R-loss/flattening?
source_trace: too_smooth_user_surface_explanation_sample
```

#### 4. surface-specific visibility

User Surface judgment card:

```text
현재 판정: 설명은 부드럽지만 그대로 쓰기엔 너무 납작합니다.
이유: 이해는 쉽지만 중간 구조와 reread의 결이 거의 사라졌습니다.
다음 이동: 이 설명은 refine 대상으로 두고 더 균형 잡힌 draft를 찾습니다.
금지선: final definition이나 baseline wording으로 쓰지 않습니다.
```

VectorFL Surface view:

```text
object_type: bounded_action_candidate
provisional_status: explanation_draft_under_review
boundary: draft only; no canonical wording
needed_reread_question: Is this acceptable simplification or R-loss?
instability_reason: high flattening risk; user-fit is good but residue retention is weak
source_trace: too_smooth_user_surface_explanation_sample
next_allowed_move draft: refine
```

Return / Validation view:

```text
observed_result: The explanation is understandable but too smooth; it loses too much residue.
reread_trigger: compare against a more balanced explanation before reuse.
next_recommended_state: refine; keep as draft, not final wording
```

#### 5. transition check

| transition | verdict | reason |
| --- | --- | --- |
| seed -> formed | PASS | unclassified seed safely became explanation draft under review. |
| formed -> reread_priority / framing_candidate / bounded_action_candidate | PASS_WITH_NOTE | bounded draft is valid, but the content quality is weak. |
| allowed_to_prepare 여부 | PASS | a draft can be prepared and reviewed. |
| allowed_to_execute 여부 | HOLD | explanation reuse is blocked from canonical promotion. |
| short validation return sufficient? | PASS_WITH_NOTE | okay for draft-level review, but edge risk exists. |
| full validation return needed? | HOLD | needed if this starts to look like reusable canonical wording. |
| final branch | PASS | refine is natural; promote is correctly blocked. |

#### 6. operator cost check

- user-filled fields: 3
- user chose `object_type`: no
- full Core 7 required: no
- User Surface only 3-4 line card: yes
- judgment burden moved to VectorFL: yes

#### 7. promotion risk check

- over-promotion occurred: no
- promotion treated as default: no
- non-promotion branches worked: yes, through refine

#### 8. verdict

`PASS_WITH_NOTE`

Reason:

The package catches flattening and blocks promotion, but the threshold between acceptable simplification and R loss remains soft.

### Case C. ambiguous Codex request without boundary

#### 1. case setup

Situation:

The user says only: "이거 Codex에게 시켜서 정리해줘."

Why weak-signal:

- purpose exists only at a vague level
- no boundary
- no expected return form
- no guardrail

Promotion risk:

- medium-high, because vague urgency can push premature packetization

#### 2. seed sidecar

```text
current_purpose: determine whether the vague Codex request is even ready for preparation
source_trace: ambiguous_codex_request_sample
initial_boundary: no execution, no one-shot drafting until scope and return shape are clarified
object_type: unclassified
```

#### 3. formed sidecar

```text
object_type: reread_priority
provisional_status: missing_boundary_and_return_shape
boundary: clarification-first; no packet preparation; no execution
next_allowed_move draft: reread_only / clarify_scope
needed_reread_question: What exactly is "이거", what boundary applies, and what return form is expected?
source_trace: ambiguous_codex_request_sample
```

Missing conditions:

- boundary
- expected_return_form
- guardrail
- reread_return_hook

#### 4. surface-specific visibility

User Surface judgment card:

```text
현재 판정: 아직 Codex에 넘길 준비가 안 됐습니다.
이유: 범위, 반환 형식, guardrail이 빠져 있어 지금 넘기면 과해석 위험이 큽니다.
다음 이동: 먼저 무엇을 어디까지 정리할지 다시 잡습니다.
금지선: 지금 바로 one-shot 작성이나 실행으로 넘어가지 않습니다.
```

VectorFL Surface view:

```text
object_type: reread_priority
provisional_status: missing_boundary_and_return_shape
boundary: clarification-first only
needed_reread_question: What is the actual object, boundary, and return expectation?
instability_reason: request is too underspecified for preparation
source_trace: ambiguous_codex_request_sample
next_allowed_move draft: reread_only / clarify_scope
```

Engine Surface view:

```text
action_shape: not_attached_yet
execution_constraint: not_executable_yet
guardrail: no packetization, no execution
expected_return_form: missing
fallback_policy: required later
trust_scope: required later
reread_return_hook: missing
```

#### 5. transition check

| transition | verdict | reason |
| --- | --- | --- |
| seed -> formed | PASS | unclassified seed safely moved into reread_priority. |
| formed -> reread_priority / framing_candidate / bounded_action_candidate | PASS | reread_priority is the correct stop. |
| allowed_to_prepare 여부 | HOLD | not enough boundary or return shape to prepare packet. |
| allowed_to_execute 여부 | FAIL-safe / disallowed | execution is clearly blocked. |
| short validation return sufficient? | PASS | low-risk clarification stop. |
| full validation return needed? | HOLD | only if someone tries to force action despite missing prerequisites. |
| final branch | PASS | hold and reread are natural here. |

#### 6. operator cost check

- user-filled fields: 3
- user chose `object_type`: no
- full Core 7 required: no
- User Surface only 3-4 line card: yes
- judgment burden moved to VectorFL: yes

#### 7. promotion risk check

- over-promotion occurred: no
- promotion treated as default: no
- non-promotion branches worked: yes, strongly

#### 8. verdict

`PASS`

Reason:

The package correctly stops a boundary-less Codex request before it becomes preparation or execution.

### Case D. A/C/T/X/R/L overlap case

#### 1. case setup

Situation:

A discussion looks like:

- A: structure must come first
- T: concept is not yet mature
- C: hold after validation
- X/L/R: it is hard to translate to user explanation without flattening or lens mismatch

Why weak-signal:

- multiple strong lenses overlap
- any single-axis reading would over-compress the case

Promotion risk:

- high, because a decisive reader may force it into A-only or T-only too early

#### 2. seed sidecar

```text
current_purpose: determine whether a multi-overlap discussion can be safely classified without premature axis collapse
source_trace: overlap_case_sample
initial_boundary: no axis lock, no promotion, no baseline wording, reread-first
object_type: unclassified
```

#### 3. formed sidecar

```text
object_type: reread_priority
provisional_status: overlap_hold
boundary: overlap reading only; no axis conclusion; no candidate promotion
next_allowed_move draft: reread_against_A_C_T_X_R_L / compare_only
needed_reread_question: Which lens is actually central, and which are secondary effects?
source_trace: overlap_case_sample
```

Why not `framing_candidate` yet:

- overlap is too strong
- center is not yet clear
- any single promotion would absorb neighboring candidates

#### 4. surface-specific visibility

User Surface judgment card:

```text
현재 판정: 아직 하나의 원리로 정리하기 이릅니다.
이유: 구조, 성숙도, 보류, 번역, 렌즈 문제가 동시에 겹쳐 중심이 불명확합니다.
다음 이동: A/C/T/X/R/L을 나눠 다시 읽고 hold 상태를 유지합니다.
금지선: 지금 하나의 축으로 잠그거나 승격하지 않습니다.
```

VectorFL Surface view:

```text
object_type: reread_priority
provisional_status: overlap_hold
boundary: overlap reading only; no lock
needed_reread_question: Which signal is primary and which are secondary?
instability_reason: A/C/T/X/R/L overlap is too strong for clean framing
source_trace: overlap_case_sample
next_allowed_move draft: reread_against_A_C_T_X_R_L / compare_only
```

Return / Validation view:

```text
observed_result: Strong overlap prevents stable single-axis classification.
reread_trigger: compare against at least two scenes before any central-candidate claim.
next_recommended_state: hold / reread_priority
```

#### 5. transition check

| transition | verdict | reason |
| --- | --- | --- |
| seed -> formed | PASS | unclassified seed safely moved into reread_priority. |
| formed -> reread_priority / framing_candidate / bounded_action_candidate | PASS | reread_priority is the safer result under overlap. |
| allowed_to_prepare 여부 | HOLD | no stable action shape should be prepared yet. |
| allowed_to_execute 여부 | FAIL-safe / disallowed | execution is clearly inappropriate. |
| short validation return sufficient? | HOLD | likely not enough if this case starts driving axis decisions. |
| full validation return needed? | PASS_WITH_NOTE | likely needed once overlap begins affecting candidate hierarchy judgment. |
| final branch | PASS | hold is natural and should remain available. |

#### 6. operator cost check

- user-filled fields: 3
- user chose `object_type`: no
- full Core 7 required: no
- User Surface only 3-4 line card: yes
- judgment burden moved to VectorFL: yes

#### 7. promotion risk check

- over-promotion occurred: no
- promotion treated as default: no
- non-promotion branches worked: yes, via hold / reread_priority

#### 8. verdict

`PASS_WITH_NOTE`

Reason:

The package correctly resists single-axis collapse, but this is the clearest case where full validation return may become necessary once overlap starts affecting hierarchy claims.

## 5. case verdict summary

| case | verdict | healthy branch |
| --- | --- | --- |
| A. weak B-adjacent external reference | PASS | `reread_priority -> hold / compare_later / archive_as_residue` |
| B. too-smooth user surface explanation | PASS_WITH_NOTE | `bounded_action_candidate -> refine` |
| C. ambiguous Codex request without boundary | PASS | `reread_priority -> hold / clarify_scope` |
| D. A/C/T/X/R/L overlap case | PASS_WITH_NOTE | `reread_priority -> hold / reread_against_overlap` |

## 6. operator cost result

Overall operator-cost verdict:

`PASS`

Shared results across cases:

- user-filled fields stayed near three
- user never chose `object_type`
- full Core 7 was never required
- User Surface stayed to 3-4 line judgment cards
- judgment burden shifted to VectorFL surface

Interpretation:

The package is not turning weak cases into user-operated forms.

## 7. promotion risk result

Overall promotion-risk verdict:

`PASS`

Observed behavior:

- weak references were not promoted to evidence
- too-smooth explanation was not promoted to final definition
- ambiguous Codex request was not promoted to preparation or execution
- overlap case was not absorbed into a single axis

Interpretation:

Non-promotion branches are available and usable. This is the main sign that the package is not too permissive.

## 8. short/full validation return judgment

Short validation return was sufficient for:

- Case A
- Case B at draft-review level
- Case C

Short validation return becomes questionable or insufficient when:

- weak signal begins affecting hierarchy or trust scope
- overlap starts driving axis-level interpretation
- explanation begins to resemble reusable wording

Full validation return is most likely needed for:

- Case D, if overlap starts influencing hierarchy claims
- Case B, if the smooth explanation starts being reused as canonical wording
- Case A, if someone tries to elevate generic role talk into B evidence

## 9. what held under weak signal

- unclassified seed capture held
- object_type assignment remained delayed
- reread_priority remained available and useful
- hold remained a natural branch
- refine remained natural for explanation quality problems
- archive_as_residue remained plausible for weak generic signals
- prepare and execute stayed separate
- short/full validation return distinction remained meaningful

## 10. what became ambiguous

- acceptable simplification vs R loss
- when generic B-adjacent talk is strong enough to become framing
- when weak comparison should move from reread to bounded preparation
- when overlap is strong enough that full validation return becomes required
- how much explanation smoothness is acceptable before canonical-use risk appears

## 11. what should not be patched yet

- do not expand Core 7
- do not add new object families
- do not add weak-signal-specific state names
- do not enforce schema
- do not add structure first and evidence later

## 12. what may need future examples

- acceptable simplification vs R loss
- direct evidence / defensive logic / comparison frame
- `allowed_to_prepare` HOLD conditions
- A/C/T/X/R/L overlap hold conditions

## 13. recommended next move

Recommended direction:

`clarification patch needed`, but only after a few more weak cases or example bundles are collected.

Working recommendation:

- hold further structural expansion
- collect more weak cases
- prefer examples over new state names or field expansion

## 14. recommended future patch 여부

There may be future clarification patches, but none should expand Core 7 or object family.

Best patch candidates later:

- acceptable simplification vs R loss examples
- direct evidence / defensive logic / comparison frame examples
- ambiguous prepare HOLD examples
- overlap-hold examples

## 15. intentionally not changed

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- `docs/reports/formation_movement_interface_validation_work_package_v0.md`
- `docs/reports/formation_movement_interface_validation_work_package_audit_v0.md`
- `docs/reports/formation_movement_interface_round1_closeout_v0.md`
- no baseline lock
- no schema enforcement
- no implementation
- no runtime manifest
- no validator or script
- no Core 7 expansion
- no object family expansion

## 16. unresolved questions

- When does generic B-adjacent language become strong enough for framing rather than reread?
- Where exactly is the line between acceptable simplification and flattening?
- How many weak-signal examples are needed before clarification patches become more useful than more reports?
- When should overlap cases default to full validation return rather than short return?
- Is the package slightly too permissive around bounded_action_candidate for explanation drafts, or is that still acceptable?
