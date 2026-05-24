# HOLD Review State Module Candidate Contract

status: MODULE_CANDIDATE_CONTRACT_WITH_HOLD
created_at: 2026-05-23 08:12:54 KST

## Candidate

candidate_id: M-CAND-05
function_pattern: HOLD Review State

## Input Boundary

A localized/receipted candidate item with claim language and approval state.

## Output Boundary

A review record with:

```text
review_state
reason
valid_for
not_valid_for
blocked_claims when applicable
recovery_class
HOLD tokens
```

## Guard Behavior

- candidate-only language -> CANDIDATE_MATERIAL_WITH_HOLD
- fake promotion/approval collapse -> STOP
- soft approval language -> HOLD_STOP_REVIEW

## Boundary

promotion_status: HOLD
program_alpha_status: NOT_READY
vectorfl_authority_mutation: no
model_execution: no
real_gemini_execution: no
real_codex_execution: no
approval_applied: no
live_db_mutation: no
schema_mutation: no
snapshot_mutation: no
router_runner_claim: no

