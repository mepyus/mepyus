# policy executor boundary round1

## 1. current diagnosis
- 이번 1차 코드화는 [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py) 전체를 뜯지 않았다
- 대신 가장 먼저 늘어날 위험이 큰 `promotion review` 축을 잘랐다
- 이유:
  - translation / processing / observer / readiness / decision 이 계속 규칙화될 가능성이 높고
  - outward review surface 도 이미 매우 크기 때문이다

## 2. exact changes

### 새 파일
- [review_policy_types.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policy_types.py)
  - `PromotionPolicyContext`
  - `PromotionPolicyResult`
  - `PromotionReviewAssembly`
- [review_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policies.py)
  - `evaluate_promotion_review_policy`
- [review_output_surface.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_output_surface.py)
  - `assemble_promotion_review_surface`

### live_input_space.py 에서 줄인 책임
- promotion review 의
  - translation coverage 판단
  - processing residual 판단
  - review state / recommendation / readiness / decision
  를 직접 계산하지 않고 policy 호출로 바꿈
- giant dict 조립을 output surface 호출로 넘김

### 남겨둔 것
- anchor review
- threshold review
- cross-path review
- canonicalization review
- direct overlap review
- space entry review

즉 지금은 `promotion review axis` 만 얇게 분리했다.

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
  - `space_entry_state = structural_led_space_pre_entry`
  - `translation_gate = true`
  - `processing_gate = true`
  - `observer_gate = true`
  - `canonical_anchor_gate = false`
  - `direct_overlap_candidate_families = [object, structural]`

### control
- `engine_phase1_observer_probe_20260321 -> doc_005`
  - `bridge_mode = none`
  - `review_state = translation_missing`
- `engine_phase1_observer_probe_20260321 -> doc_004`
  - `bridge_mode = none`
  - `review_state = translation_missing`

## 4. current reading
- `policy interface introduced, executor still dominant`
- `first review policy separated, behavior preserved`
- `output surface partially separated, next split ready`

## 5. what not changed
- canonical 기준 안 바꿈
- translation 범위 안 넓힘
- processing refinement 안 건드림
- viewer 수정 안 함
- lifecycle/pruning 구현 안 시작함
- family rule 재설계 안 함

## 6. next recommendation
1. 다음 분리 1순위는 `cross_path overlap policy`
2. 그다음 `family canonicalization policy`
3. fixture manifest 는 이 뒤에 바로 붙일 수 있다
4. lifecycle tag 는 policy 분리가 한 단계 더 된 뒤 붙이는 게 좋다

## 7. final sentence
- 이번 턴은 큰 리팩터링이 아니라 접합부 생성이다
- 이제 [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py) 는 review 정책을 외부 callable unit 으로 호출하기 시작했고, 다음 단계의 policy 분리를 위한 첫 경계선이 생겼다
