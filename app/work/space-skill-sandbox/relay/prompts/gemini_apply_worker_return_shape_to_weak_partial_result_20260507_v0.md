# Gemini Instruction - Apply Worker Return Shape to Weak / Partial Result v0

## Mission

You are acting as an external execution carrier for VectorFL.

Run one broad-but-bounded pass applying the candidate Worker Return / Packaging shape to one weak, failed, partial, or non-space-grounded external result.

Do not create micro-runs.
Do not create schema, parser, automation, registry, baseline, or current-position update.

## Purpose

The worker-return shape worked on one successful external result.

Now test whether it can classify a weaker result into HOLD vs WATCH without forcing Codex into many tiny recovery runs.

## Candidate Worker Return Shape

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

This is packaging discipline, not schema.

## Target Selection

Select one target from available prior external returns or raw outputs that is weak, failed, partial, thin, or non-space-grounded.

Suggested target pools:

```text
app/work/space-skill-sandbox/relay/outbox/
app/work/space-skill-sandbox/outputs/gemini_raw_results/
app/work/space-skill-sandbox/runs/run_033_diagnose_run_032_runner_failure.md
app/work/space-skill-sandbox/runs/run_033_validate_run_032_and_prepare_next_packet.md
app/work/space-skill-sandbox/outputs/external_run_failure_signal_bundle_v0.md
```

If file access is unavailable, state `target_not_inspected` and perform a conceptual weak-return classification using the required shape.

Do not read the whole repository.
Select one target only.

## Space Anchors To Use

Use these anchors if available:

```text
app/work/space-skill-sandbox/outputs/worker_return_packaging_candidate_setting_compact_v0.md
app/work/space-skill-sandbox/outputs/movement_record_worker_return_packaging_setting_recovery_v0.md
app/work/space-skill-sandbox/outputs/movement_record_worker_return_shape_application_recovery_v0.md
docs/specs/external_tool_plan_return_review_template_v0.md
docs/specs/movement_record_template_v0.md
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
Weak worker output stands at raw/partial trace layer.
Recovery may produce watch or hold judgment.
It does not produce memory, baseline, schema, or automation.
```

## Required Output Shape

Return exactly:

```text
PLAN_BASIS
TARGET_SELECTION
WEAK_RETURN_SUMMARY
WORKER_RETURN_SHAPE_APPLICATION
HOLD_VS_WATCH_CLASSIFICATION
RAW_TRACE_BOUNDARY
RECOVERABLE_MATERIAL_IF_ANY
MICRO_RUN_PREVENTION_CHECK
RETURN_TO_SPACE_VALUE
MOVEMENT_RECORD_CANDIDATE
DO_NOT_PROMOTE
NEXT_USE
```

## Evaluation Rules

Classify as HOLD if:

```text
authority claim is present
baseline/schema/automation claim is present
Return-to-Space Value is absent and cannot be inferred
not-inspected scope hides a critical gap
the result asks user/Codex to do many tiny relay steps
```

Classify as WATCH if:

```text
anchor usage is thin but present
not-inspected scope is partial but disclosed
evidence pointers are weak but usable
return value is candidate-level only
wording overclaims but can be downshifted
```

## Required Focus

Answer:

```text
Can the candidate worker-return shape handle weak/partial returns?
What field fails first?
What should Codex hold?
What can continue with watch?
What Return-to-Space Value exists, if any?
Does this prevent micro-run proliferation?
```

## Hard Boundaries

Do not:

```text
do not create schema/parser/automation
do not promote the shape to baseline
do not update current position
do not request full corpus indexing
do not review multiple targets
do not create multiple Movement Records
```

## Style Constraints

Be concise.
Do not expand into broad philosophy.
Do not invent new PVs.
Do not call the result final.

`STATUS: GEMINI_APPLY_WORKER_RETURN_SHAPE_TO_WEAK_PARTIAL_RESULT_INSTRUCTION_PREPARED`
