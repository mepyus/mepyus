# operating ui fallback semantics and messaging v1

## 1. purpose

이번 정리는 새 기능 추가가 아니라, 이미 동작하는 live operating UI에서
`requested asset`, `fallback-selected asset`, `live availability`, `panel fallback`
의 의미가 섞이지 않도록 정리하는 작업이다.

핵심 기준:
- invalid query는 기능적으로 fallback 되더라도 의미적으로는 숨기지 않는다.
- `selection_query_state`는 query 해석 결과다.
- `live_availability`는 live source와 현재 읽기 가능성 상태다.
- selection query 오류의 주 설명면은 `Live Control Bar`다.
- `Derived State Strip`, `Selected Detail Summary`, `Activity Panel`은 각각 자기 영역의 fallback만 설명한다.

## 2. semantic decisions

### invalid query semantics

- `asset_id` query가 invalid면:
  - requested asset은 찾지 못한 것으로 본다.
  - 화면은 fallback-selected asset으로 다시 구성한다.
  - 이 사실은 `Live Control Bar`에서 명시적으로 설명한다.
- 즉 invalid query 상황에서 현재 선택 대상은:
  - `requested asset`이 아니라
  - **fallback-selected asset**이다.

### selection_query_state vs live_availability

- `selection_query_state`
  - query input이 어떻게 해석됐는지 보여준다.
  - 예: `default_selected`, `valid_asset_id`, `invalid_selected_asset_query`
- `live_availability`
  - live source와 adapted selection이 읽기 가능한지 보여준다.
  - 예: `live_ready`, `no_selected_asset`, `empty_board`, `state_unavailable`, `live_unavailable`
- 따라서 invalid query 자체는 더 이상 `live_availability=state_unavailable`로 덮지 않는다.
  - invalid query + fallback-selected asset loaded
  - 이 경우는 `selection_query_state=invalid_selected_asset_query`, `live_availability=live_ready`

## 3. surface responsibility

### Live Control Bar

역할:
- current selected asset
- requested query asset
- query 해석 결과
- fallback applied 여부
- live source kind

메시지 책임:
- invalid query 설명의 주 표면
- default selection 설명의 주 표면
- empty assets / live unavailable의 1차 설명면

### Derived State Strip

역할:
- 현재 실제로 읽고 있는 selected asset의 핵심 상태 요약

메시지 책임:
- `no_previous_state`
- `no_active_attention`
- `insufficient_attention_history`
- `no_selected_asset`

제한:
- invalid query의 주 설명면이 되지 않는다.

### Selected Detail Summary

역할:
- 현재 실제로 읽고 있는 selected asset의 richer summary

메시지 책임:
- `state_unavailable`
- `no_selected_asset`
- selected asset의 비교/attention/memory helper

제한:
- query 오류의 주 설명면이 되지 않는다.
- fallback notice를 중복으로 길게 반복하지 않는다.

### Activity Panel

역할:
- recent lineage / activity hint

메시지 책임:
- `history_unavailable`
- `empty activity`
- lineage absent

제한:
- selection query 오류를 설명하지 않는다.

## 4. state code to user message map

| internal state code | 의미 | user-facing message | 표시 surface | tone | fallback implied |
| --- | --- | --- | --- | --- | --- |
| `default_selected` | query 없이 기본 선택 사용 | `no asset query provided; showing default selection '<id>'` | control bar | neutral | yes |
| `valid_asset_id` | 요청 자산 정상 선택 | `showing requested asset '<id>'` | control bar | neutral | no |
| `invalid_selected_asset_query` | 요청 자산 없음, fallback 적용 | `requested asset '<id>' was not found; showing fallback selection '<id>'` | control bar | informative | yes |
| `empty_assets` | live source에 selectable asset 없음 | `no selectable assets in live source` | control bar | neutral | no |
| `live_unavailable` | live source read 실패 | `live source unavailable` | control bar, page fallback | warning | no |
| `no_selected_asset` | 선택 대상 자체 없음 | `select an asset to inspect state` | strip | neutral | no |
| `state_unavailable` | 현재 selected asset에 canonical state 없음 | `selected asset has no canonical state yet` | detail summary | neutral | no |
| `no_previous_state` | 직전 state 없음 | `compare to previous unavailable` | strip, detail summary | neutral | no |
| `no_active_attention` | active attention 없음 | `no active attention` | strip, detail summary | neutral | no |
| `insufficient_attention_history` | memory용 attention history 부족 | `insufficient attention history` | strip, detail summary | neutral | no |
| `history_unavailable` | history source 없음/약함 | `history unavailable` | activity panel | neutral | no |
| `empty` | recent activity 없음 | `no recent activity` | activity panel | neutral | no |

## 5. before / after

### before

- invalid query 시:
  - board는 fallback-selected asset을 강조
  - strip/detail/activity는 `state_unavailable` 또는 `no_selected_asset`로 보여
  - requested asset과 displayed asset이 섞여 보일 수 있었다.

### after

- invalid query 시:
  - control bar가 `requested asset not found; fallback selection shown`을 설명
  - strip/detail/activity는 실제 fallback-selected asset 기준으로 정상 렌더
  - `selection_query_state`와 `live_availability`의 의미가 분리된다.

## 6. implementation notes

최소 반영:
- `app/runtime/operating_ui_live.py`
  - invalid query 감지 후 fallback-selected asset으로 process-console payload 재조회
  - `selection_notice` 생성
  - control bar에 selection notice 표면화
  - `live_availability`는 selected fallback loaded 여부 기준으로 재정리
- `app/work/operating_ui/components/derived_state_strip.py`
  - `no_selected_asset` 문구를 `select an asset to inspect state`로 정리
- `app/work/operating_ui/components/selected_asset_detail_summary.py`
  - `state_unavailable` 문구를 `selected asset has no canonical state yet`로 정리

## 7. run/check result

확인 경로:
- `/operating-ui-live`
- `/operating-ui-live?asset_id=turboquant_youtube`
- `/operating-ui-live?asset_id=missing_asset`
- runtime fallback 상태 확인은 `missing_asset` 경로로 대표 검증

확인 결과:
- default
  - `selection_query_state=default_selected`
  - `live_availability=live_ready`
- valid query
  - `selection_query_state=valid_asset_id`
  - selected asset 정상 반영
- invalid query
  - `selection_query_state=invalid_selected_asset_query`
  - `selection_notice=requested asset 'missing_asset' was not found; showing fallback selection 'choi_ai_classroom_vlm'`
  - `live_availability=live_ready`
  - strip/detail/activity는 fallback-selected asset 기준으로 loaded
- HTML에서도 selection notice와 detail section 존재 확인

## 8. remaining limitations

- `live_unavailable`를 실제 failing runtime source로 재현하는 별도 fixture는 아직 없다.
- control bar의 selection notice는 현재 한 줄 text helper다.
- invalid query 시 board first item fallback 정책 자체를 바꾸지는 않았다.

## 9. recommended next step

다음 구현 슬라이스는 `selected fallback badge + quiet status line polish` 정도의 미세 refinement다.

이유:
- 현재 의미 충돌은 정리됐고,
- 다음엔 정보를 늘리기보다 현재 read-only shell의 status hierarchy를 조금 더 매끄럽게 만드는 편이 맞다.
