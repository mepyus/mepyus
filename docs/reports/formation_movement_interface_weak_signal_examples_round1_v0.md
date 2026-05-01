# Formation-Movement Interface Weak-Signal Examples Round 1 v0

## 1. status

```yaml
status: case_example_report
verdict: PASS_WITH_NOTE
purpose: collect additional weak-signal examples as threshold material without changing package structure
baseline_lock: no
schema_enforcement: no
implementation: no
runtime_manifest: no
validator_or_script: no
core7_expansion: no
object_family_expansion: no
```

## 2. source note

This report was written from:

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- `docs/reports/formation_movement_interface_validation_work_package_v0.md`
- `docs/reports/formation_movement_interface_weak_signal_stress_test_v0.md`

The requested library seed file `docs/reports/formation_movement_interface_weak_signal_case_library_seed_v0.md` was not present in the workspace at the time of writing. The family structure below follows the requested family layout and the weak-signal stress-test findings.

## 3. included families

- acceptable simplification vs R loss
- direct evidence vs defensive logic vs comparison frame
- ambiguous prepare HOLD cases
- A/C/T/X/R/L overlap hold cases

## 4. examples

### Example ID: WS-R1-01

- Family: acceptable simplification vs R loss
- Situation:
  A user asks, "내가 만드는 공간이 뭐야?" and the explanation offered is:
  "네가 모은 생각과 자료를 연결해서 나중에 다시 보기 쉽게 만드는 공간이야."
- Why it is weak / ambiguous:
  It is understandable and not wrong, but it strips out staged reread, provisionality, and movement qualification.
- Initial safe object_type:
  `bounded_action_candidate`

User Surface judgment card:

```text
현재 판정: 설명은 이해되지만 그대로 쓰기엔 너무 얇습니다.
이유: 연결성과 다시 보기만 남고, 잠정성이나 단계적 이동의 결이 거의 사라졌습니다.
다음 이동: 더 균형 잡힌 설명과 비교해 refine합니다.
금지선: final definition, baseline wording으로 쓰지 않습니다.
```

VectorFL reading:

- relevant lenses: `R`, `L`, `X`
- instability reason: user fit is decent, but residue and intermediate-layer trace are too thin
- promotion barrier: cannot be reused as canonical space wording before stronger residue-preserving draft exists

- Recommended next_allowed_move:
  `refine`
- Short vs full validation return:
  short is enough at draft-review level; full is needed if this wording starts circulating as canonical wording
- Healthy branch:
  `refine`
- What not to do:
  do not treat this as acceptable just because it is easy to understand; do not promote it into product slogan or baseline wording

### Example ID: WS-R1-02

- Family: direct evidence vs defensive logic vs comparison frame
- Situation:
  An external reference says:
  "A reliable team needs explicit review checkpoints, otherwise the whole system drifts."
- Why it is weak / ambiguous:
  It sounds relevant to C, maybe B, and maybe validation grammar, but it does not directly map to repeated internal structures yet.
- Initial safe object_type:
  `reread_priority`

User Surface judgment card:

```text
현재 판정: 유용해 보이지만 아직 어떤 역할인지 불분명합니다.
이유: 검토 checkpoint 이야기는 맞지만, 내부 구조를 직접 보강하는지 아직 확인되지 않았습니다.
다음 이동: direct evidence인지 defensive logic인지 comparison frame인지 먼저 구분합니다.
금지선: 지금 evidence나 rule로 승격하지 않습니다.
```

VectorFL reading:

- relevant lenses: `C`, `B`, `T`
- instability reason: may be defensive logic for governance rather than direct evidence; could also be a comparison frame
- promotion barrier: no internal repeated explanatory force has been shown

- Recommended next_allowed_move:
  `reread_only`
- Short vs full validation return:
  short is enough until internal reread begins; full is needed if someone uses it to alter C/B trust scope
- Healthy branch:
  `hold`
- What not to do:
  do not read review-checkpoint language as direct C evidence without internal reread; do not elevate it into governance rule

### Example ID: WS-R1-03

- Family: ambiguous prepare HOLD cases
- Situation:
  A user says:
  "이 자료들 보고 정리될 만한 것만 Codex로 묶어봐."
- Why it is weak / ambiguous:
  There is some task intent, but no clear boundary, no return shape, no guardrail, and no reread return expectation.
- Initial safe object_type:
  `reread_priority`

User Surface judgment card:

```text
현재 판정: 아직 Codex 준비 단계로 올리기 이릅니다.
이유: 무엇을 어디까지 묶는지와 어떤 형태로 돌려받을지가 비어 있습니다.
다음 이동: 먼저 범위와 기대 반환 형식을 다시 잡습니다.
금지선: 지금 packet 준비나 실행으로 넘기지 않습니다.
```

VectorFL reading:

- relevant lenses: `B`, `X`
- instability reason: request has purpose but lacks packet-shaping structure
- promotion barrier: no stable boundary, no expected_return_form, no reread_return_hook

- Recommended next_allowed_move:
  `reread_only`
- Short vs full validation return:
  short is enough because this is still a clarification stop; full is needed only if someone overrides the stop and tries to packetize
- Healthy branch:
  `hold`
- What not to do:
  do not convert vague task intent into `prepare_worker_packet`; do not assume VectorFL should invent missing return structure without bounded context

### Example ID: WS-R1-04

- Family: A/C/T/X/R/L overlap hold cases
- Situation:
  A note says:
  "이건 먼저 구조를 세워야 하는데 아직 익지 않았고, 지금 설명하면 다 뭉개질 것 같으니 당장은 보류하자."
- Why it is weak / ambiguous:
  A, C, T, X, and R are all active at once; almost any single-axis reading would absorb the others.
- Initial safe object_type:
  `reread_priority`

User Surface judgment card:

```text
현재 판정: 아직 하나의 원리로 묶기보다 보류가 안전합니다.
이유: 구조 선행, 미성숙, 번역 어려움, 손실 위험이 동시에 강합니다.
다음 이동: A/C/T/X/R 쪽을 나눠 reread하고 중심을 다시 봅니다.
금지선: 지금 한 축으로 잠그거나 승격하지 않습니다.
```

VectorFL reading:

- relevant lenses: `A`, `C`, `T`, `X`, `R`
- instability reason: no clear central lens yet; each lens explains part of the same phrase
- promotion barrier: any single-axis framing would absorb the others too early

- Recommended next_allowed_move:
  `reread_against_A_C_T_X_R`
- Short vs full validation return:
  full is likely needed earlier than usual if this note begins to influence hierarchy judgment, because overlap ambiguity is itself the main result
- Healthy branch:
  `hold`
- What not to do:
  do not reduce the note to A-only or T-only; do not issue a clean framing candidate unless the central lens becomes clearer through comparison

## 5. example summary

| example | family | quick reading | healthy branch |
| --- | --- | --- | --- |
| `WS-R1-01` | acceptable simplification vs R loss | user explanation is readable but too thin | `refine` |
| `WS-R1-02` | direct evidence / defensive logic / comparison frame | governance-like external note is role-unclear | `hold` |
| `WS-R1-03` | ambiguous prepare HOLD | Codex request has intent but missing packet boundary | `hold` |
| `WS-R1-04` | overlap hold | one note activates multiple lenses at once | `hold` |

## 6. thresholds that became slightly clearer

- not every user-friendly explanation is acceptable simplification; some are clearly R-loss even when they are readable
- generic governance or review language should default to reread before evidence
- task intent alone is not enough for `allowed_to_prepare`
- strong multi-lens overlap is a legitimate reason to stay in hold/reread rather than force framing

## 7. thresholds still ambiguous

- where acceptable simplification ends and R-loss begins
- when external governance language becomes direct evidence instead of defensive logic
- how much missing structure VectorFL should infer before `allowed_to_prepare` becomes valid
- when overlap ambiguity alone is enough to demand full validation return

## 8. do-not-change guardrails

- This report does not expand Core 7.
- This report does not add object families.
- This report does not add weak-signal-specific state names.
- These examples are not rules.
- These examples are evidence material for future clarification only.
- Repeated `PASS_WITH_NOTE` does not auto-trigger a patch.
- Any future patch should happen only after repeated evidence accumulates in a separate bounded action.

## 9. recommended next move

- collect 3-5 more weak examples, preferably at least one more per family
- then compare repetition across examples before drafting any clarification patch
- keep package structure fixed for now
- prioritize example accumulation over structure expansion
