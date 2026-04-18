# reconstruction_supervisor_operator_usage_note_v1

## purpose

- 이 메모는 reconstruction family를 operator가 어떤 순서로 쓰는지 빠르게 보여주는 usage note다.

## single scope cycle

- 명령:
  - `bash scripts/run_reconstruction_supervisor_cycle.sh`
- 특정 scope 지정:
  - `bash scripts/run_reconstruction_supervisor_cycle.sh tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md`

주의:

- single scope cycle은 matching receipt가 잡히는 bounded scope에서만 쓴다.
- receipt가 자동으로 안 잡히는 state-like scope는 cycle 대신 fixture check나 explicit receipt 입력 경로를 쓴다.

## batch cycle

- 기본 batch:
  - `bash scripts/run_reconstruction_supervisor_batch.sh`
- 임의 scope 나열:
  - `bash scripts/run_reconstruction_supervisor_batch.sh tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md`

## read order

- 먼저 `runtime/views/reconstruction_supervisor_latest.json` 또는 `.md`
- 필요하면 `runtime/views/reconstruction_supervisor/index.json` 또는 `.md`
- 그 다음 target reconstruction packet `json`
- 사람이 다시 읽을 때만 companion `md`

## note

- 이 family는 read-only reconstruction surface다.
- decision logic, governing behavior, state mutation은 여기서 열지 않는다.
