# approval policy phase round5

## 1. current diagnosis

- round4까지는 canonical review decision focus가 분리됐지만, 현재 후보가 canonical approval 관점에서 얼마나 준비됐는지는 별도 approval status로 읽히지 않았다.
- threshold를 실제로 바꾸기 전에, 지금 신호들이 canonical approval 쪽에서 어떤 readiness를 의미하는지 approval policy에서 먼저 계산할 필요가 있었다.

## 2. exact changes

- [approval_policy_types.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/approval_policy_types.py)
  - `CanonicalApprovalStatusContext`
  - `CanonicalApprovalStatusResult`
  추가
- [approval_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/approval_policies.py)
  - `evaluate_canonical_approval_status_policy(...)` 추가
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)
  - review surface에
    - `canonical_approval_readiness_class`
    - `canonical_approval_next_step`
    - `canonical_approval_vector`
  추가

## 3. verification

- compile 통과
- fixture runner 유지
- `probe -> doc_006`
  - `canonical_review_focus_class = cross_path_corroboration`
  - `canonical_approval_readiness_class = cross_path_corroboration_pending`
- `probe -> doc_005`
  - `none / translation_missing`

## 4. current reading

- 이제 approval phase는 “왜 아직 canonical이 아닌가”를 focus뿐 아니라 readiness class로도 읽을 수 있다.
- threshold는 아직 안 바꿨고 behavior도 유지된다.
- 현재 상태는 `canonical approval status boundary introduced, behavior preserved` 로 읽을 수 있다.

## 5. next recommendation

1. 이제부터의 실제 threshold/rule 조정은 `approval_policies.py` 안에서만 진행
2. 특히 `cross_path_corroboration_pending`을 어떤 승인 조건으로 넘길지 정하는 턴이 다음이다
