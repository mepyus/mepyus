# Worker Return Packaging Candidate Setting - Success and Hold v0

## Status

```yaml
status: candidate_operating_setting
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
current_position_update: false
```

## Candidate Shape

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

## Observed Modes

```text
success_case:
  if fields are present, Codex can recover candidate material with watch.

empty_failure_case:
  if anchors_used and return_to_space_value_candidate are missing, classify HOLD and do not infer recovery value from silence.
```

## HOLD

```text
authority claim
baseline/schema/automation claim
missing Return-to-Space Value
missing anchors_used
empty result body
critical not-inspected scope hidden
micro-relay burden pushed back to user
```

## WATCH

```text
thin but present anchor usage
partial but disclosed not-inspected scope
weak but usable evidence pointers
candidate-level return value
overclaim wording that can be downshifted
```

## Micro-Run Rule

```text
Do not create a micro-run to interpret an empty return.
Do not create separate records for each missing field.
Classify once at package level.
Use diagnostics only as separate raw trace / failure-residue material.
```

## Do Not Promote

```text
not schema
not parser
not automation
not baseline
not current-position update
not memory before Codex recovery
```

`STATUS: WORKER_RETURN_PACKAGING_CANDIDATE_SETTING_SUCCESS_AND_HOLD_PREPARED`
