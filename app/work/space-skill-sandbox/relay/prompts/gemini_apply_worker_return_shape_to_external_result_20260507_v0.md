# Gemini Instruction - Apply Worker Return Shape to One External Result v0

## Mission

You are acting as an external execution carrier for VectorFL.

Do not create multiple micro-runs.
Do not create a schema, parser, automation, registry, baseline, or current-position update.

Run one broad-but-bounded pass applying the candidate Worker Return / Packaging shape to one actual external result.

Return one packaged result that Codex can recover.

## Operating Principle

```text
Plan from Space, not from Model Default.
```

Worker output is raw/candidate trace until Codex recovery.
The goal is not to decide final truth.
The goal is to determine whether the external result is recoverable into VectorFL space.

## Current Candidate Setting

Use this worker-return candidate shape:

```yaml
worker_role:
input_purpose:
anchors_used:
how_anchors_changed_behavior:
tool_output_summary:
evidence_pointers:
not_inspected_scope:
issues_or_watch_items:
return_to_space_value_candidate:
do_not_promote:
```

This is not a schema.
It is a packaging discipline for recovery.

## Target External Result

Review one actual external result from the previous space-aware loop.

Preferred target:

```text
app/work/space-skill-sandbox/relay/outbox/space_loop_test_001_execute_with_anchor_packet_20260507_gemini_outbox_20260507_181109.md
```

Fallback target if unavailable:

```text
app/work/space-skill-sandbox/relay/outbox/space_loop_test_002_qmd_attach_execute_with_anchor_packet_20260507_gemini_outbox_20260507_181636.md
```

If neither is available, state `target_not_inspected` and perform a shape-level review only.

## Space Anchors To Use

If available, inspect these anchors:

```text
app/work/space-skill-sandbox/outputs/worker_return_packaging_candidate_setting_compact_v0.md
app/work/space-skill-sandbox/outputs/movement_record_worker_return_packaging_setting_recovery_v0.md
app/work/space-skill-sandbox/outputs/qmd_carrier_candidate_operating_setting_compact_v0.md
app/work/space-skill-sandbox/outputs/movement_record_qmd_carrier_broad_bounded_setting_recovery_v0.md
app/work/space-skill-sandbox/outputs/qmd_gate_anchor_application_to_gemini_anchor_request_review_v0.md
docs/specs/external_tool_plan_return_review_template_v0.md
docs/specs/movement_record_template_v0.md
```

Do not read the whole repository.
Do not index the whole space.

## Material Family

```text
Worker Return / Packaging Records
```

Related:

```text
Task-Mode Gate Specs
External Material Intake Records
Run Records
Maturation / Residue Policy
```

## Route / PV / LACL

Route:

```text
ROUTE_MANUAL_WORKER_RETURN_INTAKE
ROUTE_AUTHORITY_DOWNSHIFT
ROUTE_RETURN_TO_SPACE_CLOSEOUT
```

Canonical PVs:

```text
PV_RAW_TRACE_BOUNDARY
PV_RETURN_TO_SPACE_CLOSEOUT
PV_NON_INSPECTED_DISCLOSURE
PV_LINE_MATURITY_CAUTION
```

LACL:

```text
The reviewed external result stands at raw/candidate worker-return layer.
The review stands at candidate packaging-setting application layer.
It is not baseline, schema, automation, or memory promotion.
```

## What To Evaluate

Answer:

1. Does the external result contain enough fields to be recoverable?
2. Did anchors actually change worker behavior?
3. What remains raw trace?
4. What is accepted as candidate recoverable material?
5. What is not inspected?
6. What is HOLD vs WATCH?
7. What Return-to-Space Value exists?
8. Would this shape prevent micro-run proliferation next time?

## Required Output Shape

Return exactly:

```text
PLAN_BASIS
TARGET_RESULT_SUMMARY
WORKER_RETURN_SHAPE_APPLICATION
RAW_TRACE_BOUNDARY
RECOVERABLE_MATERIAL
HOLD_AND_WATCH
MICRO_RUN_PREVENTION_CHECK
RETURN_TO_SPACE_VALUE
MOVEMENT_RECORD_CANDIDATE
DO_NOT_PROMOTE
NEXT_USE
```

## Section Requirements

### PLAN_BASIS

Include:

```text
work_type
current_line
axis
camera
lens
route
canonical_PVs
space_assets_consulted
target_result
not_inspected_scope
package_sizing_judgment
```

### WORKER_RETURN_SHAPE_APPLICATION

Fill the candidate shape against the target result:

```yaml
worker_role:
input_purpose:
anchors_used:
how_anchors_changed_behavior:
tool_output_summary:
evidence_pointers:
not_inspected_scope:
issues_or_watch_items:
return_to_space_value_candidate:
do_not_promote:
```

If a field is missing, write `missing` and classify as HOLD or WATCH.

### RAW_TRACE_BOUNDARY

Must classify:

```text
worker prose
tool logs
model claims
QMD metadata if present
unread source claims
body/snippet text if present
```

### HOLD_AND_WATCH

Use:

```text
authority_claim_hold
schema_or_automation_hold
baseline_claim_hold
missing_not_inspected_scope_watch
thin_anchor_usage_trace_watch
micro_run_proliferation_watch
return_to_space_value_missing_hold
```

### MICRO_RUN_PREVENTION_CHECK

State whether this review can be handled as one package-level recovery, without more small runs.

### RETURN_TO_SPACE_VALUE

Give 3-7 bullets.

### MOVEMENT_RECORD_CANDIDATE

Return a compact candidate only.
Do not write a full long record.

## Hard Boundaries

Do not:

```text
do not call the target result authoritative
do not create schema/parser/automation
do not promote candidate setting to baseline
do not update current position
do not request full corpus indexing
do not ask for more micro-runs unless there is a real blocker
```

## Style Constraints

Be concise.
Do not expand into broad philosophy.
Do not invent new PVs.
Do not call the review final.

`STATUS: GEMINI_APPLY_WORKER_RETURN_SHAPE_TO_EXTERNAL_RESULT_INSTRUCTION_PREPARED`
