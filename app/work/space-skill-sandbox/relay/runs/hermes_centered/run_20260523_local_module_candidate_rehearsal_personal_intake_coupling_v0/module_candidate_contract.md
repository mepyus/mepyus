# Personal Intake Coupling Candidate Contract

status: MODULE_CANDIDATE_CONTRACT_WITH_HOLD
created_at: 2026-05-23 09:04:47 KST

## Candidate

candidate_id: M-CAND-02
function_pattern: Personal Intake

## Required Behavior

- use temp/fixture SQLite DB only
- run `personal_intake_min.py` against `VECTORFL_PHASE0_DB`
- write local receipt
- preserve HOLD/NO authority in inserted rows
- expose read-only user-surface status

## Guard Behavior

- fixture-only intake -> INTAKE_CAPTURED_WITH_HOLD
- live DB intake claim -> STOP
- write UI claim -> STOP
- personal intake as authority/promotion -> STOP
- soft “ready for live intake” -> HOLD_STOP_REVIEW

## Boundary

promotion_status: HOLD
program_alpha_status: NOT_READY
vectorfl_authority_mutation: no
model_execution: no
real_gemini_execution: no
real_codex_execution: no
approval_applied: no
live_db_intake: HOLD
live_db_mutation: no
fixture_db_mutation: yes
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

