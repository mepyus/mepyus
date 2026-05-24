# Gemini Instruction - Apply Worker Return Shape to Partial Non-Empty Result v0

## Mission

You are acting as an external execution carrier for VectorFL.

Run one broad-but-bounded pass applying the candidate Worker Return / Packaging shape to one partial-but-not-empty external result.

Do not create micro-runs.
Do not review multiple targets.
Do not create schema, parser, automation, registry, baseline, or current-position update.

## Purpose

The worker-return shape has now been tested on:

```text
success_case:
  recoverable with watch

empty_failure_case:
  HOLD, no inference, no micro-run
```

Now test a middle case:

```text
partial_nonempty_case:
  some content exists, but anchor usage / not-inspected scope / Return-to-Space may be thin or incomplete
```

The goal is to clarify HOLD vs WATCH behavior without creating micro-runs.

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

Select one target only.

Prefer a prior external return that has some text/content but is incomplete, thin, overclaiming, or weakly grounded.

Suggested target pools:

```text
app/work/space-skill-sandbox/relay/outbox/
app/work/space-skill-sandbox/outputs/gemini_raw_results/
app/work/space-skill-sandbox/runs/
app/work/space-skill-sandbox/outputs/*return*
app/work/space-skill-sandbox/outputs/*review*
```

Good target traits:

```text
has a result body
has some evidence or claims
missing or thin anchors_used
missing or vague not_inspected_scope
contains overclaim language
has possible Return-to-Space Value but needs downshift
```

Bad target traits:

```text
empty result
fully successful well-packaged result
requires reading the whole repository
requires multiple target comparisons
```

If file access is unavailable, state `target_not_inspected` and perform conceptual classification only.

## Space Anchors To Use

Use these anchors if available:

```text
app/work/space-skill-sandbox/outputs/worker_return_packaging_candidate_setting_success_and_hold_v0.md
app/work/space-skill-sandbox/outputs/movement_record_worker_return_shape_application_recovery_v0.md
app/work/space-skill-sandbox/outputs/movement_record_worker_return_shape_weak_failure_application_recovery_v0.md
app/work/space-skill-sandbox/outputs/worker_return_packaging_candidate_setting_compact_v0.md
docs/specs/external_tool_plan_return_review_template_v0.md
docs/specs/movement_record_template_v0.md
```

Do not read the whole repository.

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
Partial worker output stands at raw/partial candidate layer.
Recovery may produce WATCH or HOLD.
It does not produce memory, baseline, schema, or automation.
```

## Required Output Shape

Return exactly:

```text
PLAN_BASIS
TARGET_SELECTION
PARTIAL_RETURN_SUMMARY
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
authority claim is present and cannot be downshifted
baseline/schema/automation claim is present
Return-to-Space Value is absent and cannot be inferred
critical not-inspected scope is hidden
evidence pointers are absent and claims are unsupported
the result asks user/Codex to do many tiny relay steps
```

Classify as WATCH if:

```text
anchor usage is thin but present
not-inspected scope is partial but disclosed
evidence pointers are weak but usable
Return-to-Space Value is candidate-level and can be downshifted
overclaim wording can be corrected
body content exists and has some recoverable material
```

## Required Focus

Answer:

```text
Which field is weakest?
Is this HOLD or WATCH?
What can be recovered?
What remains raw trace?
What should Codex downshift?
Does one package-level recovery suffice?
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

`STATUS: GEMINI_APPLY_WORKER_RETURN_SHAPE_TO_PARTIAL_NONEMPTY_RESULT_INSTRUCTION_PREPARED`
