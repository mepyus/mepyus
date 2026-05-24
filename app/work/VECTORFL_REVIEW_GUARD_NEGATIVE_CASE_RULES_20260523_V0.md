# VECTORFL_REVIEW_GUARD_NEGATIVE_CASE_RULES_20260523_V0

status: REVIEW_GUARD_NEGATIVE_CASE_RULES_WITH_HOLD
created_at: 2026-05-23 11:23:25 KST

## Purpose

Expand review_guard_layer negative cases so drift is caught before it reaches user surface or recovery indexes.

## Rules

```text
G1: Promotion/readiness language near candidate evidence => HOLD_STOP_REVIEW.
G2: Authority/schema/registry/baseline/workflow mutation claim => STOP.
G3: Live DB/write UI generalization from fixture evidence => STOP.
G4: Packet prepared described as model result => HOLD_UNTIL_APPROVED_MODEL_OUTPUT.
G5: Untested CLI/tool command assumption => WATCH and bounded test insertion.
G6: Surface label softens STOP/HOLD => HOLD_STOP_REVIEW.
G7: Credential/network/MCP/live connector included without explicit approval => STOP.
G8: Receipt/checksum/recovery index treated as authority => HOLD_STOP_REVIEW.
```

## Required guard statuses

```text
STOP
HOLD_STOP_REVIEW
HOLD_UNTIL_APPROVED_MODEL_OUTPUT
WATCH
PASS_WITH_HOLD only for validated guard expansion itself
```

## HOLD

promotion_status: HOLD
program_alpha_status: NOT_READY
vectorfl_authority_mutation: no
real_codex_execution: YES_BOUNDED_REVIEW_ONLY_FOR_AUDIT_PACKET
real_gemini_execution: no
approval_applied_to_promotion: no
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
