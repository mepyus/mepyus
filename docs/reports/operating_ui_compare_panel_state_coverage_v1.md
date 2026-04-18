# operating ui compare panel state coverage v1

## 1. verdict

완료.

이번 작업은 compare candidate panel 기능 확장이 아니라,
**guarded extension panel의 integrated state coverage closure**다.

즉:
- compare panel scope는 그대로 유지
- 새 interaction 없음
- adapter contract touch 없음
- runtime live shell에서 각 상태를 재현 가능한 controlled path를 추가해
  검증 자산으로 닫았다

## 2. modified files

- [app/runtime/operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)
- [app/core/runtime/viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)

## 3. controlled path 방식

추가한 controlled path:
- `compare_mode=empty`
- `compare_mode=no_selected`
- `compare_mode=state_unavailable`

예:
- `/operating-ui-live?asset_id=turboquant_youtube&compare_mode=empty`
- `/operating-ui-live?asset_id=turboquant_youtube&compare_mode=no_selected`
- `/operating-ui-live?asset_id=turboquant_youtube&compare_mode=state_unavailable`

원칙:
- 일반 live 경로는 그대로 유지
- compare panel만 controlled override
- selection semantics / live availability / selected asset rule은 그대로 둔다

## 4. integrated state coverage result

| case | selection_query_state | live_availability | selected_asset_id | compare panel state | compare panel output |
| --- | --- | --- | --- | --- | --- |
| `/operating-ui-live` | `default_selected` | `live_ready` | yes | `loaded` | count + rows |
| `/operating-ui-live?asset_id=<valid>` | `valid_asset_id` | `live_ready` | yes | `loaded` | count + rows |
| `/operating-ui-live?asset_id=missing_asset` | `invalid_selected_asset_query` | `live_ready` | fallback-selected | `loaded` | fallback-selected asset 기준 rows |
| `/operating-ui-live?live_mode=unavailable` | `no_selected_asset` | `live_unavailable` | no | page fallback 우선 | compare panel meaning 확장 안 함 |
| `/operating-ui-live?asset_id=<valid>&compare_mode=empty` | `valid_asset_id` | `live_ready` | yes | `empty` | `no compare candidates` |
| `/operating-ui-live?asset_id=<valid>&compare_mode=no_selected` | `valid_asset_id` | `live_ready` | yes | `no_selected_asset` | `select an asset to inspect compare candidates` |
| `/operating-ui-live?asset_id=<valid>&compare_mode=state_unavailable` | `valid_asset_id` | `live_ready` | yes | `state_unavailable` | `compare candidates unavailable` |

## 5. wording / behavior check

검증 결과:
- `empty`
  - `no compare candidates`
- `no_selected_asset`
  - `select an asset to inspect compare candidates`
- `state_unavailable`
  - `compare candidates unavailable`
- `live_unavailable`
  - compare panel이 unavailable의 주 설명면이 되지 않음
  - control bar / page fallback이 주 설명면 유지

즉 compare panel은 계속:
- compare 후보 읽기 보조면
- unavailable 주 설명면 아님
- detail/activity 책임 침범 없음

## 6. boundary re-check

### detail summary

- selected asset 상태 설명 유지
- compare panel은 compare candidate만 담당

### activity panel

- history/activity fallback 유지
- compare panel은 activity vocabulary를 가져오지 않음

### control bar / page fallback

- query/live unavailable 설명의 주 표면 유지
- compare panel은 helper 수준만 유지

## 7. verification notes

실행 확인:
- default / valid / invalid / live unavailable
- compare_mode empty / no_selected / state_unavailable

syntax:
- `python3 -m py_compile app/runtime/operating_ui_live.py app/core/runtime/viewer_server.py app/work/operating_ui/components/compare_candidate_panel.py`

## 8. remaining limitations

- `live_unavailable`는 page fallback이 우선이라 compare panel 자체 상태를 page 안에서 독립적으로 보여주지는 않는다
- compare_mode는 panel validation용 controlled path이며, 일반 운용 query로 보지 않는다
