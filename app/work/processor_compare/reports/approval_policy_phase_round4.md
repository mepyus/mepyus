# approval policy phase round4

## 1. current diagnosis

- round3까지는 bridge mode, grammar, canonical anchor approval이 분리됐지만, 최종 `next_review_blocker`와 `promotion_decision`은 여전히 review flow 안에서 암묵적으로 조합되고 있었다.
- approval phase를 더 밀려면 cross-path / threshold / direct overlap 중 무엇이 현재 canonical review의 실제 포커스인지 별도 decision unit으로 읽혀야 했다.

## 2. exact changes

- [approval_policy_types.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/approval_policy_types.py)
  - `CanonicalReviewDecisionContext`
  - `CanonicalReviewDecisionResult`
  추가
- [approval_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/approval_policies.py)
  - `evaluate_canonical_review_decision_policy(...)` 추가
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)
  - final `next_review_blocker`와 `promotion_decision`을 새 approval decision policy 결과로 조립
  - review surface에 `canonical_review_focus_class` additive 추가

## 3. verification

- compile 통과
- fixture runner 유지
- `probe -> doc_006`
  - `possibility_candidate / candidate`
  - `promotion_decision = review_canonical_anchor_alignment`
  - `canonical_review_focus_class = cross_path_corroboration`
- `probe -> doc_005`
  - `none / translation_missing`

## 4. current reading

- approval phase는 이제
  - bridge mode
  - approval grammar
  - canonical anchor approval
  - canonical review decision
  까지 별도 policy 경계를 가진다.
- behavior는 유지됐고, approval focus도 출력으로 읽히기 시작했다.
- 현재 상태는 `canonical review decision boundary introduced, behavior preserved` 로 읽을 수 있다.

## 5. next recommendation

1. 이제야 실제 `canonical approval policy` 자체를 정교화할 준비가 됐다
2. 다음은 threshold/rule refinement를 하더라도 approval policy unit 안에서만 진행
