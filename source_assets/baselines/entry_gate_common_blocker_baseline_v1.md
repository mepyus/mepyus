[[A]] [[OBJ:entry_gate_common_blocker_baseline_v1]] [[SEM:entry_gate_not_passed_as_repeated_blocker_bundle_not_vague_hold]]

# entry gate common blocker baseline v1

## 1. purpose

- 이 baseline의 목적은 `ENTRY_GATE_NOT_PASSED`를 막연한 보류가 아니라 반복 검증된 공통 blocker 묶음으로 다시 잠그는 것이다.

## 2. current read

- 여러 비교 자산에서 reusable attitude는 반복될 수 있다.
- 하지만 그 자체가 next loop gate를 여는 근거는 아니다.
- gate를 실제로 막는 것은 개별 자산의 우연한 실패가 아니라, 여러 자산에서 반복되는 공통 blocker 묶음이다.

## 3. common blockers

- `question_inducing_candidate_absence`
- `fallback_grounding_dominance`
- `weak_role_like_only`
- `pivot_compression_non_recurrence`
- `scaffold_carryover_risk`

## 4. operating implication

- 다음 판단은 “무슨 실험을 더 할까”보다 “어떤 blocker가 실제로 약해졌는가”를 먼저 본다.
- attitude survival과 institution recovery를 혼동하지 않는다.
- weak / fallback / partial 회복은 hold 해제 근거가 아니라 hold 이유를 더 구조화하는 재료다.

## 5. one-line lock

> 현재 `ENTRY_GATE_NOT_PASSED`는 소극적 보류가 아니라, 여러 자산에서 반복 검증된 공통 blocker 묶음에 근거한 구조 판정이다.
