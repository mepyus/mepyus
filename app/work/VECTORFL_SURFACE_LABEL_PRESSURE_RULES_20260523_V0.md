# VECTORFL_SURFACE_LABEL_PRESSURE_RULES_20260523_V0

status: SURFACE_LABEL_PRESSURE_RULES_WITH_HOLD
created_at: 2026-05-23 11:17:39 KST

## Purpose

Prevent user-facing status labels from softening HOLD/WATCH/STOP into approval/readiness/promotion.

## Rules

```text
R1: PASS_WITH_HOLD must include "not approval/promotion/readiness" when shown to user.
R2: WATCH must remain WATCH; it cannot become green/ready/safe-to-promote.
R3: HOLD_STOP_REVIEW must remain exact and visible; it cannot become minor warning.
R4: STOP must remain STOP and name the blocked action.
R5: HOLD_UNTIL_APPROVED_MODEL_OUTPUT must distinguish packet/template from real model output.
R6: Every surface label must preserve guard_status + forbidden_interpretation.
```

## Forbidden softening vocabulary

```text
READY
APPROVED
PROMOTED
Program Alpha ready
green
baseline frozen
ok to proceed
soft hold
available/enabled for live DB
model said as truth source
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
