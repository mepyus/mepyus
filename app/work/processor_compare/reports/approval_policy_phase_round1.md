# approval policy phase round1

## 1. current diagnosis

- 다음 병목은 `운영 자동화`가 아니라 `approval grammar` 자체다.
- 특히 promotion review 안의 gate/readiness/decision 계산은 approval policy의 핵심인데, 아직 review policy 파일 내부 helper로 묶여 있었다.
- 이 상태로 다음 phase를 밀면 승인 문법이 점점 review flow 내부 구현으로 굳어질 위험이 있었다.

## 2. exact changes

- [approval_policy_types.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/approval_policy_types.py)
  - `ApprovalGrammarContext`
  - `ApprovalGrammarResult`
  추가
- [approval_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/approval_policies.py)
  - `evaluate_approval_grammar_policy(...)` 추가
  - gate vector / readiness / decision 계산을 approval policy unit으로 분리
- [review_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policies.py)
  - `evaluate_promotion_review_policy(...)` 가 새 approval policy를 호출하도록 변경
  - 기존 private helper `_build_promotion_gate_vector`, `_promotion_readiness_class`, `_promotion_decision` 제거

## 3. verification

- behavior 변경 없음
- compile 통과
- canonical fixture 유지
- `probe -> doc_006`
  - `possibility_candidate / candidate`
  - `space_entry_state = structural_led_space_pre_entry`
- `probe -> doc_005`, `probe -> doc_004`
  - `none / translation_missing`

## 4. current reading

- approval policy phase가 실제로 시작됐다.
- 아직 direct canonical overlap 규칙을 바꾼 건 아니고, 현재 승인 문법의 핵심 축을 별도 policy unit으로 꺼냈다.
- 즉 현재 상태는 `approval grammar boundary introduced, behavior preserved` 로 읽을 수 있다.

## 5. next recommendation

1. 다음은 cross-path / direct overlap / canonicalization 결과를 받아 `canonical approval decision`까지 별도 approval policy로 올리기
2. threshold 변경은 그 다음
3. 지금은 rule change보다 grammar extraction을 한 단계 더 미는 게 안전
