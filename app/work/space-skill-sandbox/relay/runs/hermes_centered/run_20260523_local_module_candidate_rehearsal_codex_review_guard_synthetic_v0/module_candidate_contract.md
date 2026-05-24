# Codex Review Guard Synthetic Candidate Contract

status: MODULE_CANDIDATE_CONTRACT_WITH_HOLD
created_at: 2026-05-23 08:41:52 KST

## Candidate

candidate_id: M-CAND-10
function_pattern: Codex Review Guard

## Input Boundary

Synthetic Codex-like review output over the eight-candidate chain.

## Output Boundary

Guard classification:

```text
ACCEPT_REVIEW_ONLY_WITH_HOLD
STOP_CODEX_PROMOTION_OVERCLAIM
STOP_CODEX_AUTHORITY_MUTATION_OVERCLAIM
HOLD_STOP_REVIEW_SOFT_MODULE_LANGUAGE
STOP_CODEX_EDIT_COMMAND_DRIFT
```

## Guard Behavior

- review-only with HOLD -> CANDIDATE_MATERIAL_WITH_HOLD
- promotion/M4 claim -> STOP
- authority mutation claim -> STOP
- almost reusable language -> HOLD_STOP_REVIEW
- edit/patch command from review-only lane -> STOP

## Boundary

promotion_status: HOLD
program_alpha_status: NOT_READY
vectorfl_authority_mutation: no
model_execution: no
real_gemini_execution: no
real_codex_execution: no
synthetic_codex_output: yes
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

