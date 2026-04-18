# Signal Generation Sources v0

## 목적

이 문서는 어떤 runtime/work artifact와 surface가
어떤 `signal_kind` 를 생성하거나 강하게 시사하는지 연결한다.

지금까지는 다음이 이미 있다.

- signal taxonomy
- issue-root classifier
- classifier priority policy

하지만 아직 비어 있던 것은
실제 공간의 어느 evidence가 어떤 signal을 낳는가였다.

이 문서는 그 연결층이다.

## 핵심 원칙

### 1. signal은 허공에서 오지 않는다

signal은 실제 artifact, surface, log, board, query에서 나온다.

### 2. source는 family보다 아래, classifier보다 위에 있다

즉 순서는 아래다.

- artifact/source
- signal_kind
- classifier
- family / projection / route

### 3. source는 단일 파일일 수도 있고 surface 패턴일 수도 있다

예:

- 특정 JSON field
- 특정 board file family
- query text 존재 여부
- phase decision payload

## source schema v0

최소 필드:

- `source_id`
- `source_kind`
- `source_ref`
- `emitted_signal_kind`
- `evidence_pattern`
- `confidence`
- `family_hint`
- `notes`

`source_kind` 예:

- `artifact_file`
- `artifact_family`
- `surface_field`
- `operator_input`
- `runtime_view`

`confidence` 예:

- `low`
- `medium`
- `high`

## signal source map

## 1. raw_input

대표 source:

- raw transcript/note/memo/article input file
- input registry entry

강한 근거:

- input file exists
- readable entry output not yet stabilized

예시 source:

- `inputs/external_cases/*`
- `app/work/observer_ingest_min/contracts/input_registry_contract_v1.md`

## 2. preprocess_ambiguity

대표 source:

- preprocess comparison result
- uncertain-needs-probe verdict
- noisy transcript comparison output

강한 근거:

- `preprocess_required`
- `uncertain_needs_probe`
- regroup/probe branch still open

예시 source:

- [builder_choi_interview_transcript_preprocess_comparison.json](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json)

## 3. transition_blockage

대표 source:

- phase decision log
- active latent lines
- reread observation log

강한 근거:

- `active_latent_lines`
- `decision=thickening`
- blockage explanation request

예시 source:

- [phase_decision_log.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/phase_decision_log.jsonl)

## 4. boundary_ambiguity

대표 source:

- stage corridor outputs
- corridor boundary notes
- survivor/nonreinforced cards

강한 근거:

- stage lineage exists
- boundary note still open
- narrowing remains necessary

예시 source:

- [mixed_reentry_observer_stage2/generated](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_reentry_observer_stage2/generated)
- staged corridor folders in [app/work](/Users/sungsookim/universe/vectorfl_replica/app/work)

## 5. operator_overview_request

대표 source:

- engine state latest surface
- update event summary
- broad board request

강한 근거:

- latest state object exists
- no narrow query yet
- overview/readout intent is explicit

예시 source:

- [runtime/views/engine_state_latest](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_state_latest)
- [runtime/views/engine_state_update_events](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_state_update_events)

## 6. operator_search_query

대표 source:

- operator query text
- internal search panel input
- selected result context

강한 근거:

- explicit query exists
- internal search surface is available

예시 source:

- [internal_search_panel.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/components/internal_search_panel.py)
- [internal_search_panel_demo_20260402T212134Z.json](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/generated/internal_search_panel_demo_20260402T212134Z.json)

## 해석 규칙

### rule 1. 한 source가 여러 signal을 시사할 수 있다

예:

- raw transcript는 `raw_input`
- 동시에 noisy transcript이면 `preprocess_ambiguity`

이 경우 classifier priority policy가 뒤에서 정리한다.

### rule 2. field-level evidence가 있으면 file-level evidence보다 강할 수 있다

예:

- 단순 phase log 존재보다 `active_latent_lines` field 존재가 더 강한 signal

### rule 3. query 존재는 readout family에서 narrow signal로 취급한다

단순 overview보다 explicit query가 더 좁고 강하다.

## 현재 결론

이 문서가 들어오면서
지금 구조는 아래로 더 닫힌다.

- artifact/source
- signal_kind
- classifier
- family
- projection
- route

즉 classifier 입력이 실제 공간 근거와 더 직접 연결된다.
