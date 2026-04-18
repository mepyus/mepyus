# line_thickening_third_primary_route_survey_note_v0

## purpose

- 이번 note의 목적은 existing route 중 genuinely separate third primary route 후보가 있는지 짧게 선별하는 것이다.
- 조건은 `existing route + pointer-bearing + primary_raw or primary_structured + observer route와 path-wise distinct + bounded sink 가능`이다.

## survey

### candidate 1. `scripts/run_external_case_raw_intake_probe.py`

- validation_path_id candidate: `external_case_raw_intake_probe`
- pointer-bearing: 약함
- expected evidence origin: `primary_raw`
- expected independence class: `primary`
- observer route와의 차이: 있음
- verdict: `invalid`
- 이유:
  - raw intake 자체는 primary지만 output이 aggregate summary 중심이다.
  - row/span/section/key pointer가 안정적으로 남지 않아 line_thickening sink를 정직하게 꽂기 어렵다.

### candidate 2. `scripts/run_middle_layer_interview_probe.py`

- validation_path_id candidate: `middle_layer_interview_probe`
- pointer-bearing: 약함
- expected evidence origin: `derived_report` 또는 `primary_structured` 혼합
- expected independence class: `mixed`
- observer route와의 차이: 있음
- verdict: `invalid`
- 이유:
  - normalized block 분석 경로이지만 generated interpretation packet이 중심이다.
  - concrete source span/row pointer보다 role-summary output이 앞선다.

### candidate 3. `scripts/run_concept_segment_probe.py`

- validation_path_id candidate: `concept_segment_probe`
- pointer-bearing: 약함
- expected evidence origin: `derived_report`
- expected independence class: `derived`
- observer route와의 차이: 있음
- verdict: `invalid`
- 이유:
  - segment probe는 useful하지만 probe summary가 본체다.
  - primary pointer-bearing validation route로 쓰기엔 output anchor가 너무 얇다.

### candidate 4. `scripts/build_source_view.py`

- validation_path_id candidate: `source_fragment_view`
- pointer-bearing: 있음
- expected evidence origin: `primary_structured`
- expected independence class: `primary`
- observer route와의 차이: 있음
- verdict: `valid`
- 이유:
  - `FragmentStore`와 `MeasurementStore`를 직접 읽는다.
  - row마다 `fragment_id`, `source_range`, `paragraph_index`, `source_path`가 유지된다.
  - generated report를 읽는 것이 아니라 stored fragment row를 source-sorted validation surface로 다시 읽는다.
  - bounded sink를 script-level opt-in으로 붙일 수 있다.

## selection rule

- 이번 턴의 third route는 `scripts/build_source_view.py`만 valid로 본다.
- 이유는 existing route이면서, observer route와 genuinely different 하고, primary-structured pointer-bearing output을 이미 가지고 있기 때문이다.

## reading rule

- 이 route는 `primary_structured`이지 `primary_raw`는 아니다.
- 즉 raw span을 직접 다시 계산하는 route는 아니지만, stored fragment row와 source pointer를 보존한 primary validation route다.
- 그래서 independent path로는 인정하되, raw-only corroboration처럼 과장하지 않는다.
