# Input Localization Module Candidate Contract

status: MODULE_CANDIDATE_CONTRACT_WITH_HOLD
created_at: 2026-05-23 07:52:17 KST

## Candidate

candidate_id: M-CAND-01
function_pattern: Input Localization

## Input Boundary

A text input plus declared source_type/lens/boundary hints.

## Output Boundary

A localization record with:

```text
source_type
lens
boundary
authority_check
valid_for
not_valid_for
placement_candidate
receipt_seed
re_entry_compression
recovery_class
```

## Guard Behavior

- normal personal goal -> CANDIDATE_MATERIAL_WITH_HOLD
- authority mutation claim -> STOP
- router/runner ambiguity -> HOLD_STOP_REVIEW

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

