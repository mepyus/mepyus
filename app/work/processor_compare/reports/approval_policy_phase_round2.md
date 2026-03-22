# approval policy phase round2

## 1. current diagnosis

- round1에서 approval grammar의 gate/readiness/decision은 분리했지만, `canonical_anchor_gate` 자체는 아직 live_input_space builder 안에서 직접 계산되고 있었다.
- 이 상태로는 direct canonical overlap 승인 Phase를 더 밀수록 핵심 승인 규칙이 다시 executor 쪽으로 역류할 위험이 있었다.

## 2. exact changes

- [approval_policy_types.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/approval_policy_types.py)
  - `CanonicalAnchorApprovalContext`
  - `CanonicalAnchorApprovalResult`
  추가
- [approval_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/approval_policies.py)
  - `evaluate_canonical_anchor_approval_policy(...)` 추가
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)
  - `_build_anchor_review(...)` 안의 canonical anchor approval 결정 로직을 새 approval policy 호출로 대체

## 3. verification

- compile 통과
- fixture runner 유지
- `probe -> doc_006`
  - `possibility_candidate / candidate`
  - `promotion_readiness_class = anchor_alignment_pending`
  - `promotion_decision = review_canonical_anchor_alignment`
  - `space_entry_state = structural_led_space_pre_entry`
- `probe -> doc_005`
  - `none / translation_missing`

## 4. current reading

- approval policy phase는 이제 `gate/readiness/decision`뿐 아니라 `canonical_anchor_gate` 축까지 분리되기 시작했다.
- 아직 threshold를 바꾸지 않았고 behavior도 유지된다.
- 현재 상태는 `canonical anchor approval boundary introduced, behavior preserved` 로 읽을 수 있다.

## 5. next recommendation

1. 다음은 `cross-path corroboration + direct overlap + canonicalization`을 묶는 최상위 canonical approval decision policy로 올리기
2. threshold/rule 변경은 그 다음
