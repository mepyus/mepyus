# operating ui state axis stabilization v1

## 1. verdict

완료.

이번 슬라이스는 새 UI 기능 추가가 아니라,
`selection_query_state`와 `live_availability`를 더 orthogonal하게 유지하도록
상태 축을 정리하는 작업이다.

핵심 결과:
- `query_unresolved_live_unavailable` 제거
- query 해석 축은 query 결과만 표현
- unavailable 설명은 `live_availability=live_unavailable` + control bar notice에서 담당

## 2. state axis result

### selection_query_state

의미:
- query input이 어떻게 해석됐는지
- fallback-selected가 되었는지
- selected asset이 생겼는지

현재 사용 상태:
- `default_selected`
- `valid_asset_id`
- `invalid_selected_asset_query`
- `no_selected_asset`
- `empty_assets`

### live_availability

의미:
- live source/readiness와 현재 읽기 가능성

현재 사용 상태:
- `live_ready`
- `no_selected_asset`
- `empty_board`
- `state_unavailable`
- `live_unavailable`

## 3. why the composite state was removed

제거한 상태:
- `query_unresolved_live_unavailable`

제거 이유:
- query 축에 live source unavailable을 섞는 복합 상태였기 때문이다.
- requested asset이 있었더라도, live source가 unavailable이면 query를 검증할 수 없다는 사실은
  `selection_notice`와 `live_availability=live_unavailable`로 충분히 설명 가능하다.
- selection 축은 이 경우 그냥 `no_selected_asset`으로 두는 편이 더 안정적이다.

즉:
- requested asset 존재 여부는 `requested_asset_id`
- query 상세 설명은 `selection_notice`
- source 상태는 `live_availability`
- selection 축은 `no_selected_asset`

이렇게 나누는 편이 상태 과증식을 막는다.

## 4. modified files

- [app/runtime/operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)

## 5. case matrix

| case | selection_query_state | live_availability | current shown asset | control bar responsibility | page fallback | strip/detail/activity |
| --- | --- | --- | --- | --- | --- | --- |
| `/operating-ui-live` | `default_selected` | `live_ready` | yes | default selection 설명 | none | selected asset 기준 loaded |
| `/operating-ui-live?asset_id=turboquant_youtube` | `valid_asset_id` | `live_ready` | yes | requested asset 설명 | none | selected asset 기준 loaded |
| `/operating-ui-live?asset_id=missing_asset` | `invalid_selected_asset_query` | `live_ready` | yes, fallback-selected | invalid query + fallback applied 설명 | none | fallback-selected asset 기준 loaded |
| `/operating-ui-live?live_mode=unavailable` | `no_selected_asset` | `live_unavailable` | no | live source unavailable 설명 | yes | asset를 읽는 척하지 않음 |
| `/operating-ui-live?asset_id=turboquant_youtube&live_mode=unavailable` | `no_selected_asset` | `live_unavailable` | no | requested asset could not be checked 설명 | yes | asset를 읽는 척하지 않음 |

## 6. allowed and avoid combinations

### allowed

- `default_selected + live_ready`
- `valid_asset_id + live_ready`
- `invalid_selected_asset_query + live_ready`
- `no_selected_asset + live_unavailable`
- `empty_assets + empty_board`

### avoid

- `selection_query_state` 안에 live source unavailable 의미를 다시 넣는 것
- `invalid_selected_asset_query + live_unavailable`
  - 이 경우 invalid를 실제 검증한 게 아니므로 부정확하다
- `valid_asset_id + live_unavailable`
  - live unavailable이면 requested asset를 검증했다고 보면 안 된다

## 7. verification

확인 케이스:
- `/operating-ui-live`
- `/operating-ui-live?asset_id=<valid>`
- `/operating-ui-live?asset_id=missing_asset`
- `/operating-ui-live?live_mode=unavailable`
- `/operating-ui-live?asset_id=<valid>&live_mode=unavailable`

확인 결과:
- default / valid / invalid semantics 유지
- controlled unavailable path 유지
- invalid query + fallback-selected semantics 유지
- `query_unresolved_live_unavailable` 제거 후에도 control bar notice로 의미 손실 없음

syntax:
- `python3 -m py_compile app/runtime/operating_ui_live.py`

## 8. remaining limitations

- `selection_query_state=no_selected_asset`는 unavailable path에서 이유를 전부 담지 않는다.
  - 이 정보는 `selection_notice`가 보완한다.
- `empty_assets`는 현재 live unavailable path에서는 직접 쓰이지 않고, empty board 상황의 별도 조합으로 남아 있다.
