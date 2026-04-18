# reconstruction_supervisor_operating_pattern_v1

## purpose

- 이 문서는 reconstruction family를 repo 안에서 어떤 작업 패턴으로 써야 하는지 잠그는 operating pattern note다.

## core rule

- reconstruction family는 read-only reconstruction surface다.
- receipt / views / sidecar를 다시 묶어 supervisor-facing packet을 만들지만, decision logic이나 governing behavior는 열지 않는다.

## operating modes

### 1. single cycle

- 사용:
  - bounded scope가 있고 matching receipt가 자동으로 잡힐 때
- 명령:
  - `bash scripts/run_reconstruction_supervisor_cycle.sh`
  - `bash scripts/run_reconstruction_supervisor_cycle.sh tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md`

### 2. advanced cycle

- 사용:
  - explicit receipt
  - explicit supervisor view
  - explicit sidecar
  - explicit engine state/event
  - custom reconstruction id
  - selective check skip
  가 필요할 때
- 명령 예시:
  - `bash scripts/run_reconstruction_supervisor_advanced_cycle.sh --scope-ref openai_02_11 --receipt runtime/receipts/doc_process_console_state_wiring_v1_operation_receipt.md --engine-state runtime/views/engine_state_latest/openai_02_11.json --engine-event runtime/views/engine_state_update_events/openai_02_11.json`

### 3. batch cycle

- 사용:
  - 여러 bounded scope를 순차 처리할 때
- 명령:
  - `bash scripts/run_reconstruction_supervisor_batch.sh`
  - `bash scripts/run_reconstruction_supervisor_batch.sh tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md`

### 4. sync only

- 사용:
  - existing packet은 유지하고 navigation surface만 다시 맞출 때
- 명령:
  - `python3 scripts/sync_reconstruction_supervisor_surfaces.py`

## read order

- `runtime/views/reconstruction_supervisor_latest.json` 또는 `.md`
- `runtime/views/reconstruction_supervisor/index.json` 또는 `.md`
- target reconstruction packet `json`
- 필요할 때만 companion `md`

## guard

- matching receipt가 없는 scope를 latest pointer fallback으로 억지로 섞지 않는다.
- state-like scope는 explicit receipt/state/event 조합이나 dedicated fixture check를 쓴다.
- latest와 index는 navigation surface일 뿐 authoritative source가 아니다.

## current entrypoints

- builder:
  - `scripts/build_reconstruction_supervisor_surface.py`
- sync:
  - `scripts/sync_reconstruction_supervisor_surfaces.py`
- single cycle:
  - `scripts/run_reconstruction_supervisor_cycle.sh`
- advanced cycle:
  - `scripts/run_reconstruction_supervisor_advanced_cycle.sh`
- batch:
  - `scripts/run_reconstruction_supervisor_batch.sh`
- bounded fixture:
  - `scripts/run_reconstruction_supervisor_fixture_check.py`
- state-backed fixture:
  - `scripts/run_reconstruction_supervisor_state_fixture_check.py`
