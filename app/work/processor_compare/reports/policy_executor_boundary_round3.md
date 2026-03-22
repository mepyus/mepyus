# policy executor boundary round3

## 1. current diagnosis
- round1은 `promotion review` 정책 분리
- round2는 `cross_path overlap` 정책 분리
- 이번 round3은 `direct overlap / family rule refinement` 분리다
- 이유:
  - 앞으로 structural/object canonicalization rule 이 실제로 증식할 곳이 바로 이 축이기 때문이다
  - token-supported candidate, pair overlap, live anchor form, family rule state 는 전형적인 policy 영역이다

## 2. exact changes

### 새 타입
- [review_policy_types.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policy_types.py)
  - `DirectOverlapFamilyPolicyContext`
  - `DirectOverlapFamilyPolicyResult`
  - `DirectOverlapAggregatePolicyContext`
  - `DirectOverlapAggregatePolicyResult`

### 새 policy 함수
- [review_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policies.py)
  - `evaluate_direct_overlap_family_policy`
  - `evaluate_direct_overlap_aggregate_policy`

### live_input_space.py 에서 줄인 책임
- `_build_direct_overlap_review` 는 이제
  - family별 pair evidence 수집
  - family policy 호출
  - aggregate policy 호출
  - evidence surface 조립
순서로 바뀌었다

즉 direct overlap 분기 자체는 코어에서 빠지기 시작했다.

## 3. verification

### compile
- `python3 -m py_compile` 통과

### canonical fixture
- `doc_004 -> doc_005`: `canonical`
- `doc_005 -> doc_006`: `canonical`
- `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`: `canonical`

### review candidate
- `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode = possibility_candidate`
  - `review_state = candidate`
  - `direct_overlap_gap_class = token_pair_exists_but_alignment_rule_not_satisfied`
  - `direct_overlap_candidate_lead_family = structural`
  - `space_entry_state = structural_led_space_pre_entry`

### control
- `engine_phase1_observer_probe_20260321 -> doc_005`
  - `bridge_mode = none`
  - `review_state = translation_missing`
- `engine_phase1_observer_probe_20260321 -> doc_004`
  - `bridge_mode = none`
  - `review_state = translation_missing`

## 4. current reading
- `direct overlap promotion policy separated, executor still dominant`
- `promotion / cross_path / direct_overlap now all have callable policy boundaries`
- `family canonicalization rule is not yet fully externalized, but the main split line now exists`

## 5. what not changed
- canonical 기준 안 바꿈
- translation 범위 안 넓힘
- processing refinement 안 건드림
- viewer 수정 안 함
- lifecycle 구현 안 시작함
- family canonicalization rule 자체는 재설계 안 함

## 6. next recommendation
1. 다음 분리 1순위는 `cross_path canonicalization policy`
2. 그다음 `space entry policy`
3. 그 다음 `fixture manifest`

## 7. final sentence
- round3까지 오면서 [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py) 는 여전히 크지만,
  `promotion review`, `cross_path overlap`, `direct overlap` 의 핵심 policy 분기는 외부 callable unit 으로 분리되기 시작했다
