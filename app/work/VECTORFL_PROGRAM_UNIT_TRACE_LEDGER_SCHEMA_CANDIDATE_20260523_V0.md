# VECTORFL_PROGRAM_UNIT_TRACE_LEDGER_SCHEMA_CANDIDATE_20260523_V0

status: TRACE_LEDGER_SCHEMA_CANDIDATE_WITH_HOLD
created_at: 2026-05-23 10:00:06 KST

## 0. Purpose

This is a candidate trace ledger schema for the program-unit internal structure.

It connects:

```text
input_layer
-> evidence_layer
-> review_guard_layer
-> surface_layer
-> tool_reentry_layer
-> operator_recovery_layer
```

It is not a database schema mutation, not a registry, not authority, not baseline, not workflow schema, and not promotion.

## 1. Why this exists

The structure gap review identified the biggest gap as cross-layer traceability.

This candidate gives every future artifact a row shape so we can ask:

```text
Where did this come from?
Which layer owns it?
Which receipt supports it?
Which guard label controls it?
What can the user see?
Does it mutate authority? no.
Does it promote? no.
```

## 2. Candidate ledger row fields

| field | type | requirement | meaning | boundary |
|---|---|---|---|---|
| trace_id | string | required | stable local identifier for one candidate trace row | not authority id |
| created_at | datetime/string | required | creation timestamp for evidence row | not baseline timestamp |
| source_layer | enum | required | input_layer/evidence_layer/review_guard_layer/surface_layer/tool_reentry_layer/operator_recovery_layer | must be one of six layers |
| source_artifact | path/string | required | local artifact that produced or justified row | local path only |
| input_ref | path/string/null | optional | declared input fixture/source reference | no secret/live connector |
| output_ref | path/string/null | optional | declared output artifact reference | local artifact only |
| receipt_ref | path/string | required | receipt evidence path | receipt is not authority |
| guard_status | enum | required | PASS_WITH_HOLD/WATCH/HOLD_STOP_REVIEW/STOP/HOLD_UNTIL_APPROVED_MODEL_OUTPUT | no APPROVED/PROMOTED |
| surface_label | string | required | user-facing status label coupled to guard_status | must not soften STOP/HOLD |
| reentry_ref | path/string/null | optional | raw/lite/receipt/re-entry reference if tool/model output exists | only after approved lane or synthetic fixture |
| authority_effect | enum | required | NO_AUTHORITY_MUTATION | single allowed value for now |
| promotion_status | enum | required | HOLD | single allowed value for now |
| next_action | string | required | next smallest bounded action | must preserve HOLD |
| watch_notes | list/string | optional | risks or interpretation notes | candidate evidence only |

## 3. Allowed enum candidates

### source_layer

```text
input_layer
evidence_layer
review_guard_layer
surface_layer
tool_reentry_layer
operator_recovery_layer
```

### guard_status

```text
PASS_WITH_HOLD
WATCH
HOLD_STOP_REVIEW
STOP
HOLD_UNTIL_APPROVED_MODEL_OUTPUT
```

Forbidden for now:

```text
APPROVED
PROMOTED
READY
AUTHORITY_ACCEPTED
M4_CONFIRMED
PROGRAM_ALPHA_READY
```

### authority_effect

```text
NO_AUTHORITY_MUTATION
```

### promotion_status

```text
HOLD
```

## 4. Minimal row shape

```yaml
trace_id: TRACE-YYYYMMDD-0001
created_at: 2026-05-23 00:00:00 KST
source_layer: input_layer
source_artifact: app/work/example.md
input_ref: app/work/fixtures/example_input.md
output_ref: app/work/example_output.md
receipt_ref: app/work/space-skill-sandbox/relay/runs/example/receipt.md
guard_status: PASS_WITH_HOLD
surface_label: candidate evidence with HOLD
reentry_ref: null
authority_effect: NO_AUTHORITY_MUTATION
promotion_status: HOLD
next_action: continue no-model validation
watch_notes:
  - candidate material only
```

## 5. Cross-layer trace use

A program-unit work item should be traceable as:

```text
input_ref
-> output_ref
-> receipt_ref
-> guard_status
-> surface_label
-> reentry_ref if any
-> next_action
```

This creates traceability without creating authority.

## 6. Validation rules candidate

```text
1. Every row must have trace_id, source_layer, source_artifact, receipt_ref, guard_status, authority_effect, promotion_status.
2. source_layer must be one of six internal layers.
3. guard_status must be one of PASS_WITH_HOLD/WATCH/HOLD_STOP_REVIEW/STOP/HOLD_UNTIL_APPROVED_MODEL_OUTPUT.
4. authority_effect must be NO_AUTHORITY_MUTATION.
5. promotion_status must be HOLD.
6. surface_label must not soften STOP/HOLD_STOP_REVIEW.
7. reentry_ref cannot claim real model execution unless approved raw/lite/receipt exists.
8. input_ref/output_ref must be local artifacts or null.
```

## 7. Example next use

Next no-model artifact can use this schema to create a synthetic trace ledger with rows for the six layers.

Recommended next file:

```text
VECTORFL_PROGRAM_UNIT_TRACE_LEDGER_FIXTURE_REHEARSAL_20260523_V0.md
```

## 8. HOLD

promotion_status: HOLD
program_alpha_status: NOT_READY
vectorfl_authority_mutation: no
model_execution: no
real_gemini_execution: no
real_codex_execution: no
approval_applied: no
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
