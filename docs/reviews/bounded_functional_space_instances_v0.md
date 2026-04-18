# Bounded Functional Space Instances v0

## 목적

이 문서는 [bounded_functional_space_schema_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/bounded_functional_space_schema_v0.md)
를 기준으로 현재 가장 강한 후보 네 개를 실제 instance처럼 채운다.

현재 대상은 아래다.

- `input_ingest_space`
- `external_input_preprocess_space`
- `transition_validation_space`
- `operating_readout_space`

## 1. input_ingest_space

- `space_id`: `input_ingest_space`
- `space_name`: `Input Ingest Space`
- `space_status`: `active`
- `space_purpose`: 입력을 쉽게 넣고, 어떻게 나뉘었는지 바로 보고, 최소 trace와 readable board를 남기는 intake/ingest 공간
- `bounded_question`: 새 입력이 코어 해석 이전 단계에서 어떻게 읽기 가능한 형태로 들어오는가
- `scope_objects`:
  - raw input documents
  - registry-fed inputs
  - split units
  - processing trace
  - readable board
  - operator summary
- `excluded_scope`:
  - deep linkage inference
  - corridor/axis analysis
  - canonical/mixed 판독
- `state_surface`:
  - `source_manifest_*`
  - `split_units_*`
  - `processing_trace_*`
  - `readable_input_board_*`
  - `operator_summary_*`
- `action_surface`:
  - direct ingest
  - registry ingest
  - split mode 확인
  - readable board review
- `evidence_paths`:
  - [observer_ingest_min_spec.md](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/observer_ingest_min_spec.md)
  - [input_registry_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/contracts/input_registry_contract_v1.md)
  - [observer_output_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/contracts/observer_output_contract_v1.md)
  - [app/input_layer](/Users/sungsookim/universe/vectorfl_replica/app/input_layer)
  - [runtime/manifests/origin_maps](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/origin_maps)
- `root_entry_conditions`:
  - direct mode input arrives
  - registry mode ingest is requested
  - structured doc routing target is created
- `root_entry_examples`:
  - transcript input
  - memo input
  - note/article input
- `family_domains`:
  - input routing family
  - source registration family
  - readable ingest family
- `route_modes`:
  - direct ingest
  - registry ingest
  - split-first review
  - readable-board review
- `activation_signals`:
  - `input_kind` detected
  - `split_mode` resolved
  - readable board requested
- `boundary_rules`:
  - ingest visibility first
  - minimal trace only
  - no deep linkage inside this space
- `residue_policy`:
  - keep manifest/split/trace/board/summary as ingest residue
  - do not confuse ingest trace with higher-order interpretation residue
- `upper_family_links`:
  - input routing line
- `related_spaces`:
  - `external_input_preprocess_space`
  - `transition_validation_space`

## 2. external_input_preprocess_space

- `space_id`: `external_input_preprocess_space`
- `space_name`: `External Input Preprocess Space`
- `space_status`: `emergent`
- `space_purpose`: 외부 transcript를 코어로 넣기 전에 비교, regroup, post-preprocess pass를 읽는 preprocess shaping 공간
- `bounded_question`: raw transcript를 언제 어떻게 preprocess해야 input-to-reading line을 살리면서 진입시킬 수 있는가
- `scope_objects`:
  - external transcript
  - preprocess comparison result
  - regroup result
  - post-preprocess first-pass probe
- `excluded_scope`:
  - final canonical ingest
  - deep observer comparison
  - full runtime promotion decision
- `state_surface`:
  - preprocess comparison JSON
  - regroup outputs
  - post-preprocess probe outputs
- `action_surface`:
  - preprocess necessity 판정
  - regroup 시도
  - first-pass probe 재실행
- `evidence_paths`:
  - [README.md](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/README.md)
  - [builder_choi_interview_transcript_preprocess_comparison.json](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json)
  - [run_transcript_preprocess_comparison.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_transcript_preprocess_comparison.py)
  - [run_transcript_aware_regroup.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_transcript_aware_regroup.py)
  - [run_post_preprocess_first_pass_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_post_preprocess_first_pass_probe.py)
- `root_entry_conditions`:
  - transcript input feels too raw for direct ingest
  - preprocess requirement must be judged before ingest
- `root_entry_examples`:
  - builder interview transcript comparison
  - regroup-aware transcript pass
- `family_domains`:
  - transcript preprocess family
  - raw-return preservation family
  - input-to-reading family
- `route_modes`:
  - compare-first
  - regroup-first
  - post-preprocess probe
- `activation_signals`:
  - preprocess required verdict
  - uncertain-needs-probe verdict
  - regroup candidate detected
- `boundary_rules`:
  - shaping not compression
  - preserve raw-return sensitivity
  - keep this space before core ingest
- `residue_policy`:
  - keep comparison/probe outputs as preprocess residue
  - use representative-family condensation instead of raw deletion when outputs multiply
- `upper_family_links`:
  - transcript preprocess line
  - input routing line
- `related_spaces`:
  - `input_ingest_space`
  - `transition_validation_space`

## 3. transition_validation_space

- `space_id`: `transition_validation_space`
- `space_name`: `Transition Validation Space`
- `space_status`: `active`
- `space_purpose`: transition / reentry / thickening 관련 line을 runtime evidence와 stage corridor로 검증하는 공간
- `bounded_question`: 현재 line이 왜 막히고, 어디서 thickening 또는 closure 판단이 갈리는가
- `scope_objects`:
  - transition_over_surface lines
  - pre-read and raw-return latent lines
  - reread decisions
  - stage corridor outputs
- `excluded_scope`:
  - generic UI rendering
  - raw ingest splitting
  - broad policy drafting unrelated to active lines
- `state_surface`:
  - line registry
  - phase decision log
  - reread observation log
  - stage generated reports
- `action_surface`:
  - preflight reread
  - corridor probe 실행
  - closure review 보류/승격 판단
  - next check trigger 확인
- `evidence_paths`:
  - [line_registry.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/line_registry.json)
  - [phase_decision_log.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/phase_decision_log.jsonl)
  - [reread_observation_log.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/logs/reread_observation_log.jsonl)
  - [mixed_reentry_probe_stage1](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_reentry_probe_stage1)
  - [mixed_reentry_observer_stage2](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_reentry_observer_stage2)
- `root_entry_conditions`:
  - transition blockage explanation needed
  - active line needs thickening vs closure reread
  - corridor boundary must be narrowed
- `root_entry_examples`:
  - preflight reread on active latent lines
  - stage corridor validation run
  - residue robustness review
- `family_domains`:
  - transition_over_surface family
  - pre_read_eye family
  - raw_return_preservation family
- `route_modes`:
  - preflight reread
  - stage corridor probe
  - residue robustness validation
- `activation_signals`:
  - residue becomes high
  - same latent line repeats
  - sufficiency moves toward closure
- `boundary_rules`:
  - line activation and reread first
  - do not collapse validation surface into simple pass/fail
  - keep stage lineage visible
- `residue_policy`:
  - keep unresolved edges as residue candidates
  - promote only reread-surviving patterns
- `upper_family_links`:
  - observation and line-thickening line
  - promotion governance line
- `related_spaces`:
  - `operating_readout_space`
  - `input_ingest_space`

## 4. operating_readout_space

- `space_id`: `operating_readout_space`
- `space_name`: `Operating Readout Space`
- `space_status`: `active`
- `space_purpose`: process/state payload를 operator-facing UI와 readout surface로 번역하는 공간
- `bounded_question`: 현재 engine/process 상태를 operator가 어떤 readout route로 이해하고 조작할 수 있게 만들 것인가
- `scope_objects`:
  - engine state latest
  - engine state update events
  - reconstruction supervisor views
  - operating UI models
  - readonly/activity/detail/search surfaces
- `excluded_scope`:
  - deep ingest splitting
  - latent line thickening itself
  - policy authoring
- `state_surface`:
  - `runtime/views/engine_state_latest/*.json`
  - `runtime/views/engine_state_update_events/*.json`
  - `runtime/views/reconstruction_supervisor/*`
  - operating UI demo payloads
- `action_surface`:
  - readonly board
  - activity panel
  - selected detail summary
  - internal search
- `evidence_paths`:
  - [operating_ui_payload_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/operating_ui_payload_adapter.py)
  - [engine_operating_layer_manifest_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_operating_layer_manifest_v1.json)
  - [runtime/views/engine_state_latest](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_state_latest)
  - [runtime/views/engine_state_update_events](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_state_update_events)
  - [runtime/views/reconstruction_supervisor](/Users/sungsookim/universe/vectorfl_replica/runtime/views/reconstruction_supervisor)
- `root_entry_conditions`:
  - operator needs current state readout
  - process console payload must be adapted into UI model
  - selected asset/activity explanation is needed
- `root_entry_examples`:
  - process console board
  - selected asset detail
  - internal search review
- `family_domains`:
  - operating state/history family
  - readout family
  - selected detail summary family
- `route_modes`:
  - readonly board
  - activity panel
  - selected detail summary
  - internal search
- `activation_signals`:
  - engine state latest updated
  - update event summary emitted
  - operator selects asset or query
- `boundary_rules`:
  - latest is derived, history is authoritative
  - UI presentation must respect runtime evidence hierarchy
  - experimental naming stays outside authoritative layer
- `residue_policy`:
  - keep event/update surfaces as derived operating residue
  - do not treat presentation-only variations as canonical state
- `upper_family_links`:
  - surface and readout line
  - operating state/history emergent line
- `related_spaces`:
  - `transition_validation_space`
  - `dialogue_validation_space`

## 현재 판단

이 네 개는 지금 메인 공간에서
실제 bounded functional space로 가장 먼저 잠글 수 있는 후보다.

다만 아직 약한 필드도 있다.

- `upper_family_links` 는 현재 이름 수준에서만 붙어 있다
- `activation_signals` 는 일부 space에서 정량 규칙보다 해석 문장에 가깝다
- `related_spaces` 는 관계망 초안일 뿐 계층 구조가 아니다

즉 이 문서는 `final map` 이 아니라
`bounded space instantiation v0` 로 읽는 것이 맞다.

## 다음 단계

다음으로 자연스러운 일은 아래 둘이다.

1. `upper_family_layer_v0` 를 정의해서 이 네 space를 상위에서 어떻게 묶는지 정한다
2. 또는 각 space에 대해 `root family invariant` 와 `route signature` 를 실제로 붙인다

현재는 2번보다 1번이 먼저다.
