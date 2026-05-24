# RAW_OUTPUT_TEMPLATE

status: RAW_CAPTURE_TEMPLATE_WITH_HOLD

Paste exact approved model output below this line.
Do not edit raw output except secret redaction if needed.

## Metadata

model_lane: gemini_gap_scan
approval_phrase: <exact user approval phrase>
command_run: <exact command>
captured_at: <timestamp>
raw_is_authority: no
raw_is_promotion: no

## RAW OUTPUT

```text
<PASTE_RAW_MODEL_OUTPUT_HERE>
```

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

