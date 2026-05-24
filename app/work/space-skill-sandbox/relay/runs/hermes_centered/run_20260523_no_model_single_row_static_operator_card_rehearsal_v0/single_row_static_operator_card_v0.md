# Single-row static operator card

card_id: static_operator_card:single_row:phase1_stable_cycle:v0
card_status: SINGLE_ROW_STATIC_OPERATOR_CARD_REHEARSAL_WITH_HOLD

## Phase 1 deterministic stable cycle

verdict: PASS_WITH_HOLD
guard_badge: HOLD

Stable local replay evidence exists for the Phase 1 deterministic cycle, but it remains candidate evidence under HOLD.

## Evidence links

trace_ref: `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_no_model_surface_to_evidence_trace_rehearsal_v0/program_spine_phase1_stable_cycle_surface_to_evidence_trace_v0.json`
evidence_receipt_ref: `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_no_model_evidence_layer_field_fill_rehearsal_v0/phase1_deterministic_stable_cycle_evidence_layer_receipt_filled_v0.json`

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

## Forbidden actions

- treat as Program Alpha evidence
- promote module/component/M3/M4
- mutate authority
- create schema registry
- create or refresh baseline snapshot
- execute model lane from this receipt
- activate live DB intake
- write UI mutation
- bulk trace conversion
- automatic enforcement claim
- router/runner promotion

## Render policy

static_only: true
no_network: true
no_api_call: true
no_local_server_start: true
no_subprocess_runner: true

## Boundary

promotion: HOLD
program_alpha_status: NOT_READY
authority_mutation: NO
model_execution: NO
schema_registry_mutation: NO
dashboard_registry_mutation: NO
api_call: NO
api_direct: NO
live_connector: NO
