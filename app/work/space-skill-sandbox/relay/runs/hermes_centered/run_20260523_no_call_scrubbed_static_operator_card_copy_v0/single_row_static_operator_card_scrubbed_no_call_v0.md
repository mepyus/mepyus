# Scrubbed no-call static operator card copy

card_id: static_operator_card:single_row:phase1_stable_cycle:scrubbed_no_call:v0
card_status: SCRUBBED_STATIC_OPERATOR_CARD_COPY_WITH_HOLD

## Phase 1 deterministic stable cycle

verdict: PASS_WITH_HOLD
guard_badge: HOLD
source_reference_policy: SCRUBBED_DISPLAY_ONLY_NOT_ACTIVE_CALL

Archived no-call local evidence exists for the Phase 1 deterministic cycle, but it remains candidate evidence under HOLD.

operator_note: This card is a scrubbed copy. Legacy endpoint replay evidence is display-only archived evidence and must not be executed in no-call lanes.

## Evidence links

trace_ref: `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_no_model_surface_to_evidence_trace_rehearsal_v0/program_spine_phase1_stable_cycle_surface_to_evidence_trace_v0.json`
evidence_receipt_ref: `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_no_model_evidence_layer_field_fill_rehearsal_v0/phase1_deterministic_stable_cycle_evidence_layer_receipt_filled_v0.json`

## Scrub rules applied

- `api_contract_replay.py` -> `archived_local_endpoint_contract_replay_evidence` / DO_NOT_RUN_IN_NO_CALL_LANES
- `api_drift_replay_gate.py` -> `archived_local_endpoint_drift_replay_evidence` / DO_NOT_RUN_IN_NO_CALL_LANES
- `phase1_deterministic_stable_cycle.py` -> `archived_stable_cycle_receipt_source` / DO_NOT_RUN_IN_NO_CALL_LANES
- `/api/` -> `legacy_local_endpoint_path_label` / DISPLAY_ONLY_NOT_ACTIVE_CALL
- `API_CONTRACT_REPLAY_PASS` -> `archived_contract_replay_pass_label` / DISPLAY_ONLY_NOT_ACTIVE_CALL
- `PASS_API_DRIFT_REPLAY_MATCH` -> `archived_drift_replay_pass_label` / DISPLAY_ONLY_NOT_ACTIVE_CALL

## Not valid for

- Program Alpha
- authority mutation
- schema registry mutation
- baseline/snapshot creation
- promotion
- live DB intake
- model execution evidence
- write UI readiness

## HOLD boundaries

- promotion_status: HOLD
- program_alpha_status: NOT_READY
- authority_mutation: NO
- schema_registry_mutation: NO
- model_execution: NO
- live_db_intake: HOLD
- write_ui: NO
- snapshot_refresh: NO
- v1_checkpoint_creation: NO

## No-call boundary

api_call: NO
api_direct: NO
local_http_endpoint_replay: NO
local_server_start: NO
subprocess_runner: NO
model_execution: NO
authority_mutation: NO
promotion: HOLD
source_card_mutation: NO
registry_mutation: NO
