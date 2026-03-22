# approval policy phase round3

## 1. current diagnosis

- round2까지는 promotion decision과 canonical anchor approval이 분리됐지만, top-level `bridge_mode` 결정은 아직 `live_input_space.py` 안에 남아 있었다.
- 즉 approval phase를 계속 민다면 coarse bridge approval도 policy unit으로 끌어올려야 했다.

## 2. exact changes

- [approval_policy_types.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/approval_policy_types.py)
  - `BridgeModeApprovalContext`
  - `BridgeModeApprovalResult`
  추가
- [approval_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/approval_policies.py)
  - `evaluate_bridge_mode_approval_policy(...)` 추가
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)
  - top-level `bridge_mode` 결정 로직을 새 approval policy 호출로 대체

## 3. verification

- compile 통과
- fixture runner 유지
- canonical fixture 유지
- `probe -> doc_006`
  - `bridge_mode = possibility_candidate`
  - `promotion_decision = review_canonical_anchor_alignment`
- `probe -> doc_005`
  - `bridge_mode = none`
  - `review_state = translation_missing`

## 4. current reading

- approval phase는 이제
  - top-level bridge mode
  - approval grammar
  - canonical anchor approval
  까지 별도 policy 경계를 갖는다.
- behavior는 그대로 유지됐다.
- 현재 상태는 `coarse bridge approval boundary introduced, behavior preserved` 로 읽을 수 있다.

## 5. next recommendation

1. 다음은 cross-path corroboration + direct overlap + canonicalization을 묶는 `canonical approval decision policy`
2. 그 다음에야 실제 threshold/rule refinement
