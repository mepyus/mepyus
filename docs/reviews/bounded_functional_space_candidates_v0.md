# Bounded Functional Space Candidates v0

## 목적

이 문서는 현재 메인 공간 안에서
`bounded functional space` 후보를 1차로 뽑는다.

기준은 단순 폴더 묶음이 아니다.

후보가 되려면 최소 아래를 가져야 한다.

- 비교적 분명한 `space_purpose`
- 다루는 `scope_objects`
- 현재 상태를 읽을 수 있는 `state_surface`
- 어떤 root issue가 들어오는지에 대한 `root_entry_conditions`
- family가 자랄 수 있는 `family_domains`
- route가 나뉠 수 있는 `route_modes`
- 사람이 보거나 시스템이 실행할 `action_surface`

즉 이 목록은 “폴더 inventory”가 아니라
현재 공간 안에서 실질 bounded space로 숙성시킬 만한 구역을 추린 것이다.

## 판단 규칙

### 포함

- 현재 runtime/work/docs 근거가 함께 있다
- 단일 helper보다 도메인성 있는 작업 구역으로 읽힌다
- route / action / residue를 붙일 수 있다

### 제외

- baseline-memory 자체
- archive_review family
- 단순 generated accumulation belt
- purely infrastructural inventory folder

## 1차 후보 요약

### 강한 후보

- `input_ingest_space`
- `external_input_preprocess_space`
- `transition_validation_space`
- `operating_readout_space`

### 중간 후보

- `dialogue_validation_space`
- `internal_observer_compare_space`
- `corridor_stage_space`

### 아직 상위 family 또는 support로 보는 편이 맞는 것

- `baseline_memory_space`
- `archive_review families`
- `references comparison cohort`

## 후보 상세

## 1. input_ingest_space

### status

강한 후보

### 대표 근거

- [observer_ingest_min_spec.md](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/observer_ingest_min_spec.md)
- [app/input_layer](/Users/sungsookim/universe/vectorfl_replica/app/input_layer)
- [runtime/manifests/origin_maps](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/origin_maps)
- [app/work/observer_ingest_min/generated](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/generated)

### space_purpose

입력을 쉽게 넣고, 어떻게 나뉘었는지 바로 보고,
최소 trace와 readable board를 남기는 intake/ingest 공간

### scope_objects

- raw input documents
- registry-fed inputs
- split units
- processing trace
- readable board
- operator summary

### state_surface

- `source_manifest_*`
- `split_units_*`
- `processing_trace_*`
- `readable_input_board_*`
- `operator_summary_*`

### root_entry_conditions

- direct mode input
- registry mode ingest
- structured doc routing target 발생

### family_domains

- input routing family
- source registration family
- readable ingest family

### route_modes

- direct ingest
- registry ingest
- split-first review
- readable-board review

### action_surface

- input file ingest
- split mode 확인
- trace 확인
- operator summary 확인

### boundary note

이 공간은 deep linkage engine이 아니라
`easy ingest + visible split + readable trace`에 강하게 bounded 되어 있다.

## 2. external_input_preprocess_space

### status

강한 후보

### 대표 근거

- [README.md](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/README.md)
- [builder_choi_interview_transcript_preprocess_comparison.json](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json)
- `scripts/run_transcript_preprocess_comparison.py`
- `scripts/run_transcript_aware_regroup.py`
- `scripts/run_post_preprocess_first_pass_probe.py`

### space_purpose

외부 transcript를 코어로 넣기 전,
비교 / regroup / post-preprocess pass를 읽는 preprocess shaping 공간

### scope_objects

- external transcript
- preprocess comparison result
- regroup result
- post-preprocess first-pass probe

### state_surface

- preprocess comparison JSON
- regroup outputs
- post-preprocess probe outputs

### root_entry_conditions

- transcript input이 raw ingest에 비해 너무 거칠 때
- preprocess 필요 여부를 먼저 판정해야 할 때

### family_domains

- transcript preprocess family
- raw-return preservation family
- input-to-reading family

### route_modes

- compare-first
- regroup-first
- post-preprocess probe

### action_surface

- preprocess necessity 판정
- regroup 시도
- first-pass probe 재실행

### boundary note

raw cache가 아니라 emergent line belt로 읽는 것이 맞다.

## 3. transition_validation_space

### status

강한 후보

### 대표 근거

- [runtime/manifests/line_registry.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/line_registry.json)
- [runtime/manifests/phase_decision_log.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/phase_decision_log.jsonl)
- [runtime/logs/reread_observation_log.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/logs/reread_observation_log.jsonl)
- [app/work/mixed_reentry_probe_stage1](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_reentry_probe_stage1)
- [app/work/mixed_reentry_observer_stage2](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_reentry_observer_stage2)

### space_purpose

transition / reentry / thickening 관련 line을 실제 runtime evidence와 stage corridor로 검증하는 공간

### scope_objects

- transition_over_surface lines
- pre-read and raw-return latent lines
- reread decisions
- stage corridor outputs

### state_surface

- line registry
- phase decision log
- reread observation log
- stage generated reports

### root_entry_conditions

- 전환이 왜 막혔는지 설명해야 할 때
- 현재 line이 thickening인지 closure인지 다시 봐야 할 때
- stage corridor에서 다음 경계를 정해야 할 때

### family_domains

- transition_over_surface family
- pre_read_eye family
- raw_return_preservation family

### route_modes

- preflight reread
- stage corridor probe
- residue robustness validation

### action_surface

- next check trigger 확인
- reread 재실행
- corridor probe 실행
- closure review 보류/승격 판단

### boundary note

이 공간은 단순 report belt가 아니라
`line activation + reread + stage validation`이 묶인 기능 공간으로 읽는 편이 맞다.

## 4. operating_readout_space

### status

강한 후보

### 대표 근거

- [app/work/operating_ui/operating_ui_payload_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/operating_ui_payload_adapter.py)
- [runtime/views/engine_state_latest](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_state_latest)
- [runtime/views/engine_state_update_events](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_state_update_events)
- [runtime/views/reconstruction_supervisor](/Users/sungsookim/universe/vectorfl_replica/runtime/views/reconstruction_supervisor)

### space_purpose

process/state payload를 operator-facing UI와 readout surface로 번역하는 operating readout 공간

### scope_objects

- engine state latest
- update event summaries
- reconstruction supervisor views
- UI adapter payloads
- readonly board components

### state_surface

- `runtime/views/engine_state_latest/*.json`
- `runtime/views/engine_state_update_events/*.json`
- reconstruction supervisor views
- operating UI demo outputs

### root_entry_conditions

- 현재 상태를 사람에게 읽히게 보여줘야 할 때
- process console payload를 operating UI model로 바꿔야 할 때
- selected asset detail이나 activity를 요약해야 할 때

### family_domains

- operating state/history family
- readout family
- selected detail summary family

### route_modes

- readonly board
- activity panel
- selected detail summary
- internal search

### action_surface

- state board 렌더
- selected detail 요약
- activity 비교
- internal search 진입

### boundary note

아직 설명 문서는 얇지만,
실제 구조상 `상태면 -> UI adapter -> operator readout` 경계가 분명하다.

## 5. dialogue_validation_space

### status

중간 후보

### 대표 근거

- [README.md](/Users/sungsookim/universe/vectorfl_replica/app/work/dialogue_loop_test/README.md)
- [app/work/dialogue_loop_test/generated](/Users/sungsookim/universe/vectorfl_replica/app/work/dialogue_loop_test/generated)
- `docs/reports/*engine_purpose_validation*`
- `docs/reports/*multi_pass_validation*`

### space_purpose

dialogue asset을 여러 단계로 reread하면서
context unit, purpose synthesis, question block, multi-pass interpretation을 검증하는 공간

### 왜 중간 후보인가

validation belt로는 강하지만,
현재 action surface가 operator action보다 validation reread에 치우쳐 있다.

즉 bounded space로 성숙할 가능성은 높지만,
아직은 validation-centered emergent belt에 가깝다.

## 6. internal_observer_compare_space

### status

중간 후보

### 대표 근거

- [root_retention_note_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/root_retention_note_v1.md)
- [app/work/processor_compare/observer_engine](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/observer_engine)
- [app/work/processor_compare/reports](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports)

### space_purpose

observer / anchor / processor outputs를 비교하고
runtime sidecar에 필요한 비교 엔진을 제공하는 공간

### 왜 중간 후보인가

현재 runtime sidecar의 실행 기반으로 중요하지만,
도메인 bounded space라기보다 internal compare engine 성격이 강하다.

즉 `space`라기보다 `cross-space infrastructure`에 더 가깝다.

## 7. corridor_stage_space

### status

중간 후보

### 대표 근거

- [work_maturity_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/app/work/work_maturity_map_v0.md)
- `mixed_reentry_probe_stage1`
- `mixed_reentry_observer_stage2`
- `mixed_corridor_boundary_probe_stage3`
- `mixed_corridor_format_disentangle_stage4`
- `technical_business_corridor_decompose_stage5`

### space_purpose

하나의 corridor나 boundary를 stage lineage로 좁혀 가는 probe/observer 공간

### 왜 중간 후보인가

lineage는 강하지만,
지금은 bounded operational space라기보다
숙성 corridor 자체를 실험하는 meta-space 성격이 있다.

## 제외 또는 보류

### baseline_memory_space

- 중요하지만 functional space라기보다 전체 공간의 기준면이다

### archive_review families

- line residue / support cluster belt이지 active bounded space가 아니다

### references cohort

- 비교/참고 자산이며 메인 bounded space로 바로 읽지 않는다

## 현재 1차 결론

지금 메인 공간에서 가장 먼저 bounded functional space로 잠글 만한 후보는 아래 넷이다.

1. `input_ingest_space`
2. `external_input_preprocess_space`
3. `transition_validation_space`
4. `operating_readout_space`

그 다음 숙성 후보는 아래 셋이다.

1. `dialogue_validation_space`
2. `internal_observer_compare_space`
3. `corridor_stage_space`

## 다음 단계

이 문서 다음으로 자연스러운 일은 아래 둘 중 하나다.

1. 위 네 개 강한 후보에 대해 `bounded functional space schema v0` 형태로 실제 필드를 채운다
2. 그 전에 `upper family layer`가 이 공간들 위에서 무엇을 관리하는지 먼저 정의한다

현재로서는 1번이 먼저다.
