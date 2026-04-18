# multi_lens_document_reading_v0 integrated flow cohort observation report

## verdict

- integrated `multi_lens_document_reading_v0` flow was observed across a small structured-doc cohort
- current artifacts showed stable shape and stable handoff semantics
- this report records observational behavior only and does not introduce decision logic

## cohort inputs used

- `docs/reports/smoke_structured_doc_default_case_v1.md`
- `docs/reports/smoke_structured_doc_summary_case_v1.md`
- `source_assets/directives/codex_directive_document_routing_markers_and_operation_receipt_v1.md`
- `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md`

## what was compared

- field presence and top-level artifact stability
- active vs parked surfaced semantics
- raw vs surfaced readout shape
- handoff boundary consistency

## stable patterns

### artifact shape stability

모든 cohort artifact에서 아래 top-level fields가 동일하게 유지됐다.

- `kind`
- `source_id`
- `observer_run_id`
- `split_units_path`
- `invocation_stage`
- `linked_segments`
- `raw_reading_result`
- `surfaced_readout`
- `parked_axes`
- `handoff_boundary`

추가로 아래도 cohort 전반에서 안정적이었다.

- `raw_reading_result` key shape
  - `source_id`
  - `readings`
  - `lens_ids_used`
  - `is_stable_lens_only`
- `surfaced_readout` key shape
  - `source_id`
  - `lens_ids_used`
  - `is_stable_lens_only`
  - `line_states`
  - `readings`

### active vs parked surfaced semantics

모든 cohort case에서 surfaced semantics는 동일했다.

- `line_input_to_reading_organ -> active`
- `line_transition_over_surface -> parked`
- `parked_axes = [line_transition_over_surface]`

즉 parked axis 표시는 케이스 크기와 무관하게 artifact 안에서 안정적으로 유지됐다.

### raw vs surfaced readout shape

모든 cohort case에서 raw reading count와 surfaced reading count가 일치했다.

- default smoke: `2 -> 2`
- summary smoke: `4 -> 4`
- routing directive: `68 -> 68`
- engine lock preset directive: `110 -> 110`

의미:

- surfaced readout은 현재 raw result 위의 얕은 surface adapter로 동작하고 있다
- shape drift나 hidden post-processing은 관찰되지 않았다

### handoff boundary consistency

모든 cohort artifact에서 handoff boundary는 동일했다.

- `runtime_stops_after = surfaced_readout`
- `next_owner = supervisor_docs_operating_loop`
- `decision_logic_in_runtime = false`

즉 integrated flow는 실제 호출 뒤에도 readout/handoff boundary에서 멈췄다.

## sparse / weak areas

- current stable/thick actual lens는 두 개뿐이다
- `line_transition_over_surface`는 cohort 전반에서 parked axis로만 나타났고, surfaced output에서도 parked 해석 범위를 벗어나지 않았다
- `line_input_to_reading_organ`는 active axis이지만 current basis는 자주 `low linkage_confidence` 또는 partial match 수준에 머문다
- 현재 artifact는 observation trace로는 충분하지만, maturity-level reading이나 document-level conclusion을 지지하는 재료는 아니다

## overclaim risks

- `active`를 maturity state로 읽는 위험
- `weak`를 곧 promotion candidate처럼 읽는 위험
- `parked` axis의 `absent`를 runtime failure로 읽는 위험
- raw와 surfaced가 둘 다 저장된다는 이유로 decision legitimacy가 생긴다고 읽는 위험
- larger directive case에서 row 수가 많아졌다고 판단 권한까지 확장된 것처럼 읽는 위험

현재 contract 기준으로 위 해석은 모두 금지다.

## artifact-shape drift check

- 이번 cohort에서는 artifact-shape drift가 관찰되지 않았다
- top-level field set, raw/surfaced key set, parked-axis marker, handoff boundary가 모두 안정적이었다

## case spread note

- smoke case 두 개는 small payload에서 shape와 boundary를 확인하는 데 유효했다
- directive case 두 개는 larger payload에서도 같은 구조가 유지되는지 확인하는 데 유효했다
- 즉 current v0는 small-case와 larger-case 모두에서 artifact contract를 유지했다

## technical summary

- integrated multi-lens flow는 `segmentation -> raw reading result -> surfaced readout -> handoff` 구조를 cohort 전반에서 유지했다
- active/parked semantics와 handoff boundary는 stable했다
- weak area는 heuristic richness가 아니라 interpretive ceiling 쪽에 있다
- current artifacts는 observation runtime output으로는 읽을 수 있지만 decision or maturity surface로 읽으면 안 된다

## user-language summary

- 지금 multi-lens는 여러 문서에서 실제로 돌고 있고, 결과 파일 모양도 안정적으로 유지됐다
- `input_to_reading_organ`은 active 축으로 보이고, `transition_over_surface`는 parked 축으로 계속 분리돼 보인다
- 하지만 이 결과는 어디까지나 "이번에 어떻게 읽혔는가" 기록일 뿐이고, "그래서 이 line을 올린다" 같은 판단 기록은 아니다
- 지금 단계에서 가장 중요한 건 잘 읽혔는지보다, 결과가 같은 규칙으로 안정적으로 남고 과장 해석을 막고 있는지인데, 그 점은 cohort 기준으로 유지됐다

## close-out

- future supervisor는 이 report만 보고 current integrated `multi_lens_document_reading_v0`가 several structured-doc cases에서 어떻게 보이는지 빠르게 파악할 수 있다
- stable pattern과 weak observational ceiling은 여기서 고정한다
- 새로운 decision logic은 이번 report에 없다
