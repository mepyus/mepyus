# operating ui live unavailable path v1

## 1. verdict

완료.

이번 작업은 새 기능 확장이 아니라, 문서로만 정의돼 있던 `live_unavailable`를
실제로 재현 가능한 검증 경로로 승격하는 작업이다.

일반 live path는 유지했고,
의도적으로만 진입 가능한 controlled path를 추가했다.

## 2. modified files

- [app/runtime/operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)
- [app/core/runtime/viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)

## 3. live_unavailable reproduction

재현 방식:
- `/operating-ui-live?live_mode=unavailable`
- `/operating-ui-live?asset_id=turboquant_youtube&live_mode=unavailable`
- `/api/operating-ui-live?live_mode=unavailable`

설계 이유:
- 실제 failing source를 억지로 만들지 않고
- viewer/live composition 안에서 안전하게 unavailable path를 검증할 수 있게 하려는 controlled path다.
- 일반 live route는 오염시키지 않는다.

## 4. behavior

### normal live path

- `live_mode`가 없으면 기존 동작 유지
- invalid query + fallback-selected semantics도 그대로 유지

### controlled live_unavailable path

- `state=live_unavailable`
- `live_availability=live_unavailable`
- `selected_asset_id=None`
- `available_assets=[]`
- control bar는 계속 보이되:
  - current 없음
  - requested asset 여부
  - query state
  - live unavailable notice
  를 보여준다
- page fallback panel이 `live source unavailable`를 주 설명으로 노출한다
- strip/detail/activity는 실제 asset를 읽는 척하지 않는다

## 5. selection_query_state and live_availability combinations

| case | selection_query_state | live_availability | note |
| --- | --- | --- | --- |
| `/operating-ui-live` | `default_selected` | `live_ready` | 기본 selected asset |
| `/operating-ui-live?asset_id=turboquant_youtube` | `valid_asset_id` | `live_ready` | requested asset loaded |
| `/operating-ui-live?asset_id=missing_asset` | `invalid_selected_asset_query` | `live_ready` | fallback-selected asset loaded |
| `/operating-ui-live?live_mode=unavailable` | `no_selected_asset` | `live_unavailable` | default selection 자체를 못 읽음 |
| `/operating-ui-live?asset_id=turboquant_youtube&live_mode=unavailable` | `query_unresolved_live_unavailable` | `live_unavailable` | requested asset를 확인할 수 없음 |

주의:
- `invalid_selected_asset_query`와 `live_ready` 동시 가능 규칙은 그대로 유지된다.
- `live_unavailable`는 query 문제와 별개다.
- controlled unavailable path에서만 `query_unresolved_live_unavailable`를 사용해
  “query가 틀렸다”가 아니라 “live source unavailable이라 query를 확인할 수 없다”를 구분했다.

## 6. surface responsibility preservation

- `Live Control Bar`
  - query 상태와 live unavailable 설명의 주 표면
- `Live Page Fallback`
  - page-level unavailable 설명
- `Derived State Strip`
  - unavailable path에서는 data reading surface로 사용하지 않음
- `Selected Detail Summary`
  - unavailable path에서는 selected asset를 읽는 척하지 않음
- `Activity Panel`
  - unavailable path에서는 history reading 의미를 확장하지 않음

## 7. run/check result

확인 케이스:
- `/operating-ui-live`
- `/operating-ui-live?asset_id=turboquant_youtube`
- `/operating-ui-live?asset_id=missing_asset`
- `/operating-ui-live?live_mode=unavailable`
- `/operating-ui-live?asset_id=turboquant_youtube&live_mode=unavailable`

확인 결과:
- 일반 경로:
  - 기존 selection / fallback semantics 유지
- unavailable 경로:
  - control bar 존재
  - page fallback 존재
  - selected asset를 읽는 척하지 않음
  - syntax check 통과

## 8. remaining limitations

- 실제 runtime failure를 재현하는 것은 아니고, controlled unavailable path다.
- unavailable path용 별도 visual polish는 아직 없다.
