# operating ui vocabulary lock v1

## 1. purpose

이 문서는 operating UI에서 상태 축은 유지한 채,
상태명과 helper copy가 흔들리지 않도록 vocabulary를 잠그는 문서다.

이번 lock의 범위:
- `selection_query_state`
- `live_availability`
- control bar / selection notice / detail helper / activity fallback / page fallback에 쓰는 용어

## 2. canonical terms

| term | meaning | may appear | should not appear |
| --- | --- | --- | --- |
| `requested asset` | query param으로 요청한 asset | control bar, selection notice, report table | strip, detail canonical summary, activity item text |
| `current shown asset` | 현재 화면이 실제로 읽고 있는 asset | control bar, selection notice | strip/detail/activity 내부 상태명 |
| `fallback-selected asset` | invalid query 후 fallback으로 현재 보여주는 asset | detail badge, report text | control bar current field 이름, strip/activity helper |
| `selected asset` | strip/detail/activity가 실제로 읽고 있는 대상이라는 일반 표현 | strip subhead, detail helper, report prose | query 설명면의 주어 |
| `live source unavailable` | live source/readiness unavailable | control bar notice, page fallback | strip/detail/activity의 상태 설명 |
| `selected asset has no canonical state yet` | selected asset는 있으나 canonical state가 없음 | detail helper, diff fallback | control bar query 설명 |
| `no selected asset` | 현재 표시할 selected asset 자체가 없음 | strip helper, unavailable path state | invalid query fallback 설명 |
| `empty board` | selectable asset list가 비어 있음 | board empty state, report table | detail/activity helper |
| `history unavailable` | history/activity source unavailable | activity panel | control bar query 설명 |

## 3. state axis wording rules

### selection_query_state

이 축은 query 해석 결과만 말한다.

allowed wording:
- `default_selected`
- `valid_asset_id`
- `invalid_selected_asset_query`
- `no_selected_asset`
- `empty_assets`

forbidden:
- live source unavailable 의미를 selection state 이름에 다시 넣는 것

### live_availability

이 축은 live source/readiness만 말한다.

allowed wording:
- `live_ready`
- `no_selected_asset`
- `empty_board`
- `state_unavailable`
- `live_unavailable`

forbidden:
- requested asset validity를 availability 이름에 넣는 것

## 4. surface copy guidance

### Live Control Bar

표현 순서:
1. `current shown asset`
2. `source`
3. `live`
4. `requested asset`
5. `query_state`
6. `selection_notice`

selection notice 예시:
- default:
  - `no requested asset / current shown asset '<id>'`
- valid:
  - `requested asset '<id>' shown`
- invalid:
  - `requested asset '<id>' not found / current shown asset '<id>' / fallback applied`
- unavailable without request:
  - `live source unavailable / no current shown asset`
- unavailable with request:
  - `live source unavailable / requested asset '<id>' not checked`

### Derived State Strip

- `selected asset`의 state summary만 담당
- query 관련 단어는 넣지 않는다

### Selected Detail Summary

- `selected asset`의 richer summary만 담당
- invalid query 설명은 하지 않는다
- 단, `fallback-selected asset` badge는 허용한다

### Activity Panel

- `history unavailable`, `no recent activity`만 담당
- query / requested asset / fallback language를 넣지 않는다

### Page fallback

- `live source unavailable`를 가장 짧게 유지한다
- query 설명은 control bar가 우선 담당한다

## 5. checked wording results

현재 기준:
- default
  - `no requested asset / current shown asset '<id>'`
- valid
  - `requested asset '<id>' shown`
- invalid
  - `requested asset '<id>' not found / current shown asset '<id>' / fallback applied`
- live unavailable
  - `live source unavailable / no current shown asset`
- live unavailable with request
  - `live source unavailable / requested asset '<id>' not checked`

## 6. notes

- `fallback-selected asset`는 badge label로만 쓴다.
- `current shown asset`는 control bar/notice에서만 쓴다.
- `selected asset`는 strip/detail/activity 계열 설명에서만 쓴다.
