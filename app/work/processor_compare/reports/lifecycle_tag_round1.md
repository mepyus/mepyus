# lifecycle tag round1

## 1. current diagnosis
- policy boundary와 fixture boundary 다음으로 필요한 것은 lifecycle 접합부였다
- 이번 round1에서는 storage 구현 없이, current review result가 `hot / warm / cold` 관점으로 읽힐 수 있는 최소 lifecycle tag만 붙였다
- 목적은 pruning 을 시작하는 것이 아니라 다음 phase의 lifecycle 정책이 걸릴 자리를 먼저 만드는 것이다

## 2. exact changes

### 새 타입
- [review_policy_types.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policy_types.py)
  - `LifecyclePolicyContext`
  - `LifecyclePolicyResult`

### 새 policy 함수
- [review_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policies.py)
  - `evaluate_review_lifecycle_policy`

### output surface 추가 필드
- [review_output_surface.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_output_surface.py)
  - `trace_temperature`
  - `lifecycle_stage`
  - `lifecycle_reason`

### 적용 방식
- 이번 round에서는 lifecycle tag를 `promotion_review` surface에만 붙였다
- 즉 active review / possibility candidate 쪽 lifecycle 접합부만 먼저 만들었다

## 3. verification

### compile
- `python3 -m py_compile` 통과

### review candidate
- `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode = possibility_candidate`
  - `review_state = candidate`
  - `trace_temperature = hot`
  - `lifecycle_stage = review_active`
  - `space_entry_state = structural_led_space_pre_entry`

### control
- `engine_phase1_observer_probe_20260321 -> doc_005`
  - `bridge_mode = none`
  - `review_state = translation_missing`
  - lifecycle tag 없음

### canonical fixture
- `doc_004 -> doc_005`
  - `bridge_mode = canonical`
  - `review_state = not_applicable`
  - lifecycle tag 없음

## 4. current reading
- lifecycle policy is now callable
- current active review candidate can be temperature-tagged without storage redesign
- lifecycle is still partial and review-lane scoped

## 5. what not changed
- pruning 구현 안 함
- hot/warm/cold migration 안 함
- timestamp 저장 안 함
- canonical/not_applicable row 전체에 lifecycle field 안 붙임

## 6. next recommendation
1. 다음은 top-level pair result에도 lifecycle surface를 붙일 수 있다
2. 그 다음 `last_reviewed_at / last_state_change_at` 같은 최소 태그를 생각할 수 있다
3. lifecycle automation 은 그 뒤다

## 7. final sentence
- 이번 round1은 lifecycle 구현이 아니라 lifecycle 접합부 생성이다
- 이제 review candidate는 단순 상태뿐 아니라 temperature 관점으로도 읽을 수 있다
