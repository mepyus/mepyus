# Cross-tool Re-entry Synthetic Candidate Contract

status: MODULE_CANDIDATE_CONTRACT_WITH_HOLD
created_at: 2026-05-23 08:45:28 KST

## Candidate

candidate_id: M-CAND-09
function_pattern: Cross-tool Re-entry

## Required Lanes

```text
raw
lite
receipt
compressed_reentry
guard_review
```

## Guard Behavior

- declared synthetic Gemini/Codex output with raw/lite/receipt split -> CANDIDATE_MATERIAL_WITH_HOLD
- hidden transport -> STOP
- authority inheritance -> STOP
- role blur / soft approval -> HOLD_STOP_REVIEW

## Boundary

promotion_status: HOLD
program_alpha_status: NOT_READY
vectorfl_authority_mutation: no
model_execution: no
real_gemini_execution: no
real_codex_execution: no
synthetic_tool_output: yes
approval_applied: no
live_db_mutation: no
schema_mutation: no
snapshot_mutation: no
router_runner_claim: no
write_ui: no
authority_database: no
shared_db_mutation: no
v1_snapshot_creation: no
m4_reusable_module: no
module_promotion: no
program_alpha_ready: no
hidden_transport: no
authority_inheritance: no

