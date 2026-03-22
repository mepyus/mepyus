# review timestamp round1

## 1. current diagnosis

- lifecycle grammar는 이미 `top-level`과 `promotion_review`에 붙어 있었지만, 언제 이 상태를 읽었는지와 어떤 상태 조합인지 남기는 운영 태그가 없었다.
- 따라서 fixture runner는 현재 판정은 검증할 수 있어도, 이후 automation에서 `same state / new read` 와 `state changed` 를 구분할 최소 서명이 없었다.

## 2. exact changes

- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)
  - top-level `evaluate_mixed_path_pair(...)` 반환값에 `evaluated_at`, `state_signature` 추가
  - promotion review surface에도 같은 필드 추가
  - `_build_review_timestamp(...)`, `_material_side_ref(...)` helper 추가
- [review_policy_types.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policy_types.py)
  - `ReviewTimestamp` dataclass 추가
- [review_output_surface.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_output_surface.py)
  - `assemble_promotion_review_surface(...)` 가 timestamp payload를 받도록 확장
- [run_review_fixture_check.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_review_fixture_check.py)
  - fixture check output에 `evaluated_at`, `state_signature` 추가

## 3. verification

- `python3 -m py_compile ...` 통과
- fixture runner 유지
  - immutable regression fixture: `3/3 pass`
  - mutable exploration control: `3/3 current match`
- sample pair
  - `probe -> doc_006`
    - `bridge_mode = possibility_candidate`
    - `review_state = candidate`
    - top-level / review surface 모두 timestamp 존재
  - `probe -> doc_005`
    - `bridge_mode = none`
    - `review_state = translation_missing`
    - top-level timestamp 존재, review surface timestamp 없음
  - `doc_004 -> doc_005`
    - `bridge_mode = canonical`
    - `review_state = not_applicable`
    - top-level timestamp 존재, review surface timestamp 없음

## 4. current reading

- lifecycle boundary 위에 최소 운영 태그가 추가됐다.
- 아직 persisted history나 change detection은 없지만, `read time`과 `state signature`를 남길 접합부는 생겼다.
- 즉 현재 상태는 `policy / fixture / surface / lifecycle / timestamp boundary introduced` 로 읽을 수 있다.

## 5. next recommendation

1. `state_signature`를 fixture runner diff의 기준으로 쓰기
2. 필요하면 `last_reviewed_at` 같은 persistence tag를 나중에 추가
3. 다음은 분리보다 `stabilization + lightweight automation` 쪽이 자연스럽다
