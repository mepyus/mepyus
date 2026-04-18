# operating ui legacy wording reconciliation v1

## 1. purpose

이 문서는 과거 operating UI report/spec에 남아 있는 이전 wording을
현재 canonical 기준선에서 어떻게 읽어야 하는지 정리하는 reconciliation 문서다.

목적:
- 과거 문서를 전면 rewrite하지 않는다
- 현재 canonical과 legacy wording을 분리한다
- 이후 독자가 오래된 표현을 현재 기준으로 오해하지 않게 한다

## 2. canonical references

현재 operating UI의 canonical reference는 아래 두 문서다.

1. [operating_ui_vocabulary_lock_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/operating_ui_vocabulary_lock_v1.md)
2. [operating_ui_state_axis_stabilization_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_state_axis_stabilization_v1.md)

보조 참조:
- [operating_ui_fallback_semantics_and_messaging_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_fallback_semantics_and_messaging_v1.md)

원칙:
- 과거 문서는 history record로 유지한다
- 현재 해석은 위 canonical references 기준으로 한다

## 3. legacy wording examples

### A. `current selected asset`

과거 예:
- [operating_ui_fallback_semantics_and_messaging_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_fallback_semantics_and_messaging_v1.md)
  - `current selected asset`
- [operating_ui_live_control_bar_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_live_control_bar_v1.md)
  - `current selected`

현재 해석:
- query 설명면에서는 `current shown asset`
- strip/detail/activity 일반 설명에서는 `selected asset`

즉:
- control bar 문맥이면 `current shown asset`
- read surface 문맥이면 `selected asset`

### B. `showing requested asset`

과거 예:
- [operating_ui_fallback_surface_polish_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_fallback_surface_polish_v1.md)
  - `showing requested asset '<id>'`
- [operating_ui_fallback_semantics_and_messaging_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_fallback_semantics_and_messaging_v1.md)
  - `showing requested asset '<id>'`

현재 해석:
- canonical wording은 `requested asset '<id>' shown`

주의:
- 의미 차이는 작지만, 앞으로는 `requested asset`를 문두에 두는 형태를 우선한다

### C. `fallback selection`

과거 예:
- [operating_ui_fallback_semantics_and_messaging_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_fallback_semantics_and_messaging_v1.md)
  - `showing fallback selection '<id>'`

현재 해석:
- canonical wording은 두 층으로 분리한다
  - control bar: `current shown asset '<id>' / fallback applied`
  - detail: `fallback-selected asset` badge

주의:
- 앞으로 `fallback selection`이라는 덩어리 표현은 새 문서에서 쓰지 않는다

### D. `query_unresolved_live_unavailable`

과거 예:
- [operating_ui_live_unavailable_path_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_live_unavailable_path_v1.md)

현재 해석:
- legacy only
- 더 이상 current state axis에 포함되지 않는다
- canonical reading:
  - `selection_query_state=no_selected_asset`
  - `live_availability=live_unavailable`
  - query 설명은 `selection_notice`

### E. `no canonical state yet`

과거 예:
- [operating_ui_selected_detail_summary_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_selected_detail_summary_v1.md)
- [operating_ui_readonly_components_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_readonly_components_v1.md)
- [operating_ui_empty_and_fallback_rules_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/operating_ui_empty_and_fallback_rules_v1.md)

현재 해석:
- detail helper 문맥에서는
  - `selected asset has no canonical state yet`
- strip fallback 문맥에서는
  - `select an asset to inspect state`
  또는
  - `compare to previous unavailable`

주의:
- `no canonical state yet` 단독 문구는 현재 기준에선 context가 부족한 legacy wording으로 본다

## 4. do not use in new docs

아래 표현은 새 문서에서 더 이상 canonical wording으로 쓰지 않는다.

- `current selected asset`
- `showing requested asset`
- `showing fallback selection`
- `query_unresolved_live_unavailable`
- context 없이 단독으로 쓰는 `no canonical state yet`

## 5. preferred replacements

| legacy wording | canonical replacement |
| --- | --- |
| `current selected asset` | `current shown asset` or `selected asset` |
| `showing requested asset '<id>'` | `requested asset '<id>' shown` |
| `showing fallback selection '<id>'` | `current shown asset '<id>' / fallback applied` |
| `query_unresolved_live_unavailable` | `selection_query_state=no_selected_asset` + `live_availability=live_unavailable` + `selection_notice` |
| `no canonical state yet` | `selected asset has no canonical state yet` |

## 6. reconciliation principle

원칙:
- 과거 문서는 historical record다
- historical wording이 남아 있어도 삭제/전면 rewrite하지 않는다
- 현재 해석과 구현 판단은 항상 canonical references 기준으로 한다

즉:
- **old report wording is reference-only**
- **current spec wording is decision-bearing**

## 7. checked legacy anchors

이번 reconciliation에서 실제 확인한 대표 문서:
- [operating_ui_fallback_semantics_and_messaging_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_fallback_semantics_and_messaging_v1.md)
- [operating_ui_live_unavailable_path_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_live_unavailable_path_v1.md)
- [operating_ui_live_control_bar_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_live_control_bar_v1.md)
- [operating_ui_selected_detail_summary_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_selected_detail_summary_v1.md)
- [operating_ui_layout_refinement_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/operating_ui_layout_refinement_v1.md)

## 8. limitation

- 과거 report 전부를 line-by-line canonical wording으로 갱신하지는 않았다.
- 이번 문서는 reading contract를 잠그는 reconciliation layer다.
