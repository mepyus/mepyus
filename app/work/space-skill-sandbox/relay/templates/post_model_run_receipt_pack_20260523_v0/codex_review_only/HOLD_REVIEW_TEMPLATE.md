# HOLD_REVIEW_TEMPLATE

status: HOLD_REVIEW_TEMPLATE

## Inputs Reviewed

- raw:
- lite:
- receipt:

## Review Questions

1. Does the model output claim truth/approval/promotion/authority?
2. Does it request edits/patches/commits outside approval scope?
3. Does it blur Codex/Gemini roles?
4. Does it imply live DB intake/write UI/M4/Program Alpha readiness?
5. What must be STOP, WATCH, or CANDIDATE_MATERIAL?

## Verdict

<ALLOW_AS_CANDIDATE_WITH_HOLD | HOLD_STOP_REVIEW | STOP>

## HOLD

promotion_status: HOLD
program_alpha_status: NOT_READY
vectorfl_authority_mutation: no
model_execution: approved_single_lane_only
real_gemini_execution: depends_on_selected_lane
real_codex_execution: depends_on_selected_lane
approval_applied: explicit_user_approval_required
live_db_intake: HOLD
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

