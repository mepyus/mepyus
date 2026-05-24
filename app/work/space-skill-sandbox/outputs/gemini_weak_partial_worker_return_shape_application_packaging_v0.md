# Gemini Weak / Partial Worker Return Shape Application Packaging v0

## Status

```yaml
status: gemini_return_packaging
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
current_position_update: false
source_return: user_pasted_gemini_result
verdict: HOLD_WITH_RECOVERABLE_FAILURE_SIGNAL
```

## Source

Gemini applied the candidate worker-return shape to:

```text
app/work/space-skill-sandbox/relay/outbox/run_032_gemini_outbox_20260429_181647.md
```

Related diagnosis:

```text
app/work/space-skill-sandbox/runs/run_033_diagnose_run_032_runner_failure.md
```

Codex checked file presence only in this recovery pass:

```text
target_result: present
run_033_diagnosis: present
raw_result_pointer: present
```

## Accepted Values

Accepted as candidate material:

```text
The 10-field worker-return shape can classify an empty/silent external return as HOLD without requiring more micro-runs.
The first failing fields are anchors_used, how_anchors_changed_behavior, tool_output_summary, and return_to_space_value_candidate.
The target return itself is not recoverable as memory.
The failure signal can be recovered only as diagnostic residue / watch material.
```

## Downshift Corrections

Gemini wording:

```text
catastrophic failure
```

Downshift:

```text
non-recoverable empty return / HOLD case
```

Gemini wording:

```text
matures the runner's Failure Guide
```

Downshift:

```text
may inform failure-guide candidate material if separately reviewed; this pass does not update a guide.
```

Gemini wording:

```text
correctly triggers HOLD
```

Downshift:

```text
supports HOLD classification for this target.
```

## HOLD Classification

```yaml
classification: HOLD
hold_reason:
  - anchors_used missing
  - behavior_change missing
  - tool_output_summary missing
  - return_to_space_value_candidate missing
  - no recoverable material in target result body
watch_material:
  - failure diagnosis may be useful as diagnostic residue
  - stderr/raw logs should remain raw trace until separately reviewed
```

## Raw Trace Boundary

Remain raw trace:

```text
packet path
run_id
timestamp
empty Result section
0-byte raw result pointer
associated diagnosis claims
stderr/log references
```

Do not promote:

```text
empty return
failure diagnosis
response-bundle workaround
```

without separate recovery.

## Candidate Setting Update

The worker-return candidate setting now has two observed application modes:

```text
success_case:
  shape maps fields and supports package-level recovery with watch.

empty_failure_case:
  shape fails early and supports HOLD without extra micro-runs.
```

This is still not a schema, parser, automation, or baseline.

## Return-to-Space Value

Recoverable material:

```text
The worker-return shape can quickly reject an empty external return as non-recoverable while preserving failure signal as diagnostic residue.
```

Reusable judgment:

```text
If anchors_used and return_to_space_value_candidate are missing, classify as HOLD unless a separate diagnostic record supplies recoverable failure material.
```

Operational correction:

```text
Do not spend Codex tokens trying to infer meaning from an empty worker return. Move to diagnostic residue or rerun strategy only if needed.
```

Future reuse note:

```text
Use this as the weak/empty return application record alongside the prior success-case application record.
```

## Do Not

```text
do not promote Run 032 to recovered memory
do not update current position
do not create schema/parser/automation
do not treat failure guide maturation as completed
do not turn response-bundle strategy into default automation from this pass
```

`STATUS: GEMINI_WEAK_PARTIAL_WORKER_RETURN_SHAPE_APPLICATION_PACKAGED_WITH_HOLD`
