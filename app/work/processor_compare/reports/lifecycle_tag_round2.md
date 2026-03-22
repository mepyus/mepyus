# lifecycle tag round2

## 1. current diagnosis
- round1에서는 lifecycle tag를 `promotion_review` surface 안에만 붙였다
- 그래서 active review candidate는 temperature로 읽을 수 있었지만, canonical / none row는 top-level에서 같은 문법으로 읽기 어려웠다
- 이번 round2에서는 lifecycle surface를 top-level pair result까지 올렸다

## 2. exact changes

### 변경 파일
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)

### 적용 방식
- `evaluate_mixed_path_pair(...)` 반환값에 아래 필드 추가
  - `trace_temperature`
  - `lifecycle_stage`
  - `lifecycle_reason`
- lifecycle 판정은 기존 `evaluate_review_lifecycle_policy(...)`를 재사용했다
- 즉 canonical / none / possibility를 top-level에서 같은 lifecycle grammar로 읽을 수 있게 됐다

## 3. verification

### compile
- `python3 -m py_compile` 통과

### possibility review candidate
- `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode = possibility_candidate`
  - `trace_temperature = hot`
  - `lifecycle_stage = review_active`
  - `promotion_review.trace_temperature = hot`

### translation-missing control
- `engine_phase1_observer_probe_20260321 -> doc_005`
  - `bridge_mode = none`
  - `trace_temperature = warm`
  - `lifecycle_stage = blocked_waiting_revisit`

### canonical fixture
- `doc_004 -> doc_005`
  - `bridge_mode = canonical`
  - `trace_temperature = hot`
  - `lifecycle_stage = approved_active`

## 4. current reading
- lifecycle tag is now available at top-level pair surface
- canonical / none / possibility can be read with the same temperature grammar
- review-lane lifecycle and top-level lifecycle now coexist

## 5. what not changed
- storage layer 구현 안 함
- timestamp 저장 안 함
- pruning automation 안 함
- lifecycle transition history 안 만듦

## 6. next recommendation
1. 다음은 `review timestamps` 또는 lightweight runner 쪽으로 갈 수 있다
2. lifecycle은 지금 단계에서 접합부로는 충분하다
3. automation 전에 field naming을 잠그는 게 좋다

## 7. final sentence
- round2로 lifecycle grammar는 review lane 내부에만 머무르지 않고, 엔진 pair result 전체에 적용되기 시작했다
- 이제 canonical / possibility / blocked control을 한 문법으로 읽는 기반이 생겼다
