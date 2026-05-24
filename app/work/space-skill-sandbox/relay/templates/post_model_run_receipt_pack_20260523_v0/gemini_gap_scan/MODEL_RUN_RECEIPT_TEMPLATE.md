# MODEL_RUN_RECEIPT_TEMPLATE

status: MODEL_RUN_RECEIPT_TEMPLATE_WITH_HOLD

## Required Fields

model_lane:
approval_phrase:
approval_scope:
started_at:
finished_at:
command_run:
input_packet:
raw_output_path:
lite_summary_path:
receipt_path:
hold_review_path:
reentry_path:
user_surface_card_path:
classification:
state_mutations_observed:
WATCH:
HOLD:


## Validator Expectations

- raw output exists
- lite summary exists
- HOLD review exists
- re-entry compression exists
- no authority/promotion language drift
- no repo/schema/registry/baseline mutation unless separately approved

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

