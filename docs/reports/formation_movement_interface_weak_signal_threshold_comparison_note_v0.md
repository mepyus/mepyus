# Formation-Movement Interface Weak-Signal Threshold Comparison Note v0

## 1. status

```yaml
status: threshold_comparison_note
based_on_round1_and_round2_weak_examples: true
package_candidate_support: true
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_core7_expansion: true
no_object_family_expansion: true
no_clarification_patch_yet: true
verdict: PASS_WITH_NOTE
```

## 2. source documents

- `docs/reports/formation_movement_interface_weak_signal_examples_round1_v0.md`
- `docs/reports/formation_movement_interface_weak_signal_examples_round2_v0.md`
- `docs/reports/formation_movement_interface_weak_signal_case_library_seed_v0.md`
- `docs/reports/formation_movement_interface_weak_signal_stress_test_v0.md`
- `docs/reports/formation_movement_interface_package_draft_v0.md`

## 3. comparison matrix

### Family A. acceptable simplification vs R loss

- round1 example summary:
  `WS-R1-01` explains the space as something that connects collected thoughts and materials for later reread. It is understandable, but staged reread, provisionality, and movement qualification become too thin.
- round2 example summary:
  `WS-R2-01` explains the integrated engine as a tool that pulls gathered material into current work and connects it to AI processing. It preserves slightly more movement sense, but residue is still thin.
- repeated pattern:
  readability alone is not enough; explanations can remain usable while still carrying significant flattening risk.
- difference:
  round1 is clearly thinner and closer to plain summary/storage language; round2 preserves current-work movement better, but still weakens reread and provisionality.
- threshold movement:
  `CLEARER`
- remaining ambiguity:
  how much residue hook is enough for a draft to cross from "less bad flattening" into acceptable simplification remains unclear.

### Family B. direct evidence vs defensive logic vs comparison frame

- round1 example summary:
  `WS-R1-02` uses review-checkpoint language that may touch C, B, or T, but still lacks internal repeated explanatory force.
- round2 example summary:
  `WS-R2-02` uses stronger role-boundary and checkpoint language. It touches B and C more explicitly, but still reads as disciplined-structure defense rather than direct evidence.
- repeated pattern:
  governance / checkpoint / role-boundary language keeps landing in reread/hold rather than direct evidence.
- difference:
  round2 is stronger and more specific than round1, which helps clarify defensive logic, but still does not cross into evidence.
- threshold movement:
  `CLEARER`
- remaining ambiguity:
  when repeated governance language becomes comparison frame strong enough to leave pure reread and when it begins to count as internal-evidence-adjacent remains unresolved.

### Family C. ambiguous prepare HOLD

- round1 example summary:
  `WS-R1-03` asks Codex to gather only what looks worth organizing, but lacks packet boundary, return shape, guardrail, and reread path.
- round2 example summary:
  `WS-R2-03` adds a style preference, "보기 좋게" and "너무 길지만 않게," but still lacks boundary, expected return form, guardrail, and reread return hook.
- repeated pattern:
  task intent alone does not open `allowed_to_prepare`; vague request plus style preference is still insufficient.
- difference:
  round2 clarifies that style and tone preference do not substitute for packet structure.
- threshold movement:
  `CLEARER`
- remaining ambiguity:
  how much missing structure VectorFL may safely infer before opening `allowed_to_prepare` is still unresolved.

### Family D. A/C/T/X/R/L overlap hold

- round1 example summary:
  `WS-R1-04` says structure should come first, things are not yet ripe, and explanation would flatten them; A/C/T/X/R are all active.
- round2 example summary:
  `WS-R2-04` adds explicit user-surface translation risk, bringing L in more strongly and making overlap itself part of the validation problem.
- repeated pattern:
  when multiple lenses stay strong at once, hold/reread is healthier than clean framing.
- difference:
  round2 makes L/X pressure more explicit and raises the likelihood that short return may be insufficient.
- threshold movement:
  `CLEARER`
- remaining ambiguity:
  whether overlap with strong user-surface translation risk should default to full validation return sooner than ordinary overlap cases is still unresolved.

## 4. repeated patterns

- 읽기 쉬움만으로는 acceptable simplification이 되지 않음.
- residue가 얇으면 R loss / flattening 위험이 계속 남음.
- generic governance / disciplined-structure language는 internal reread 없이 direct evidence가 되지 않음.
- governance/checkpoint/role-boundary language는 대체로 defensive logic 또는 reread_priority 쪽에 머묾.
- vague Codex request는 boundary / expected_return_form / guardrail 없이는 allowed_to_prepare도 HOLD.
- style preference는 packet 조건을 대체하지 못함.
- A/C/T/X/R/L overlap이 강하면 clean framing보다 hold/reread가 건강함.
- overlap에 user-surface translation risk가 붙으면 full validation return 필요성이 빨리 올라감.

## 5. threshold movement

| threshold item | judgment | note |
| --- | --- | --- |
| acceptable simplification vs R loss | `CLEARER` | easy readability is repeatedly shown to be insufficient, but the exact residue minimum is still unclear |
| direct evidence vs defensive logic | `CLEARER` | external governance language repeatedly fails to become direct evidence without internal reread |
| defensive logic vs comparison frame | `STILL_AMBIGUOUS` | examples suggest distinction, but not enough to draw a stable line |
| allowed_to_prepare HOLD 조건 | `CLEARER` | task intent and style preference both fail without boundary + expected return + guardrail |
| overlap hold 조건 | `CLEARER` | repeated support for hold/reread over clean framing |
| short vs full validation return trigger | `PATCH_CANDIDATE_LATER` | overlap + translation risk and canonical-wording risk are emerging but not fully stable |
| VectorFL inference 허용 폭 | `HOLD_MORE_EXAMPLES` | examples show risk of overreach, but safe inference boundary remains soft |

## 6. patch readiness check

| family | readiness | reason |
| --- | --- | --- |
| acceptable simplification vs R loss | `PATCH_CANDIDATE_AFTER_MORE_EXAMPLES` | repeated pattern exists, but threshold still risks over-hardening if patched too early |
| direct evidence vs defensive logic vs comparison frame | `EMERGING_PATTERN` | strong repetition around non-evidence status exists, but comparison-frame threshold is still thin |
| ambiguous prepare HOLD | `PATCH_CANDIDATE_AFTER_MORE_EXAMPLES` | repeated under-specification pattern is stable, but forcing wording too early may increase operator cost |
| A/C/T/X/R/L overlap hold | `EMERGING_PATTERN` | hold preference repeats, but full-return threshold and hierarchy effects need more evidence |

Readiness rule:

- no family is `READY_FOR_CLARIFICATION_PATCH` yet
- no family is structurally broken

## 7. candidate future clarifications

These are candidates only, not patches.

- acceptable simplification is not just readability; it should leave at least a minimal residue hook for deeper reread
- direct evidence should not be judged from an external reference alone; repeated internal reread support is needed
- `allowed_to_prepare` should not open on task intent alone; minimum packet-shaping conditions still matter
- overlap-heavy cases should default to hold/reread rather than single-axis cleanup
- overlap plus user-surface translation risk should raise the likelihood of full validation return

## 8. what should not be patched yet

- Core 7 expansion
- object family addition
- weak-signal-specific new `object_type`
- locking acceptable simplification as a premature rule
- numeric thresholds for direct-evidence judgment
- turning guarded-execution conditions into enforced schema at this stage
- using repeated `PASS_WITH_NOTE` as an automatic patch trigger

## 9. recommended next move

Global direction:

`hold_structure_expansion`

Family-level direction:

- acceptable simplification vs R loss:
  `collect_more_examples`
- direct evidence vs defensive logic vs comparison frame:
  `collect_more_examples`
- ambiguous prepare HOLD:
  `prepare_clarification_patch_candidate` only after one more targeted weak case
- overlap hold:
  `run_one_more_targeted_weak_case`

Compressed judgment:

- structure expansion should stay on hold
- examples are still more valuable than patching
- one targeted weak case on overlap/full-return and one on ambiguous prepare may be enough before candidate patch wording is drafted

## 10. overall verdict

`PASS_WITH_NOTE`

Reason:

- round1 and round2 together show real threshold movement
- repeated patterns are visible and non-random
- however, the current evidence is still better suited for comparison and future patch readiness judgment than for immediate clarification patching

## 11. unresolved questions

- what is the minimum residue hook that makes an explanation acceptably simplified rather than merely less flattened
- when does defensive logic become strong enough to count as comparison frame rather than just reread material
- how much packet structure can VectorFL safely infer before `allowed_to_prepare` becomes too permissive
- should overlap cases with explicit translation risk default to full validation return earlier than other overlap cases
- how many more weak examples are enough before `EMERGING_PATTERN` should become `PATCH_CANDIDATE_AFTER_MORE_EXAMPLES`
