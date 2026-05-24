# Worker Return Packaging Candidate Setting - Three Modes v0

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

## Intake Modes

```text
success_case:
  fields present
  anchor usage trace present
  Return-to-Space candidate present
  -> recover with watch

empty_failure_case:
  empty result body
  anchors_used missing
  Return-to-Space candidate missing
  -> HOLD; do not infer meaning from silence

partial_nonempty_case:
  result body exists
  usable candidate material exists
  anchor usage / behavior-change / not-inspected scope is thin or missing
  -> WATCH; downshift and disclose gaps
```

## HOLD

```text
authority claim that cannot be downshifted
baseline/schema/automation implementation claim
missing Return-to-Space Value
missing anchors_used with empty or unsupported result
empty result body
critical not-inspected scope hidden
micro-relay burden pushed back to user
```

## WATCH

```text
thin but present anchor usage
missing or partial not-inspected scope that recovery can disclose
weak but usable evidence pointers
candidate-level return value
overclaim wording that can be downshifted
body content exists and has recoverable candidate material
```

## Internal Convergence Gate

Before continuing, check:

```text
Is Codex about to create another tiny run instead of one package-level recovery?
Is Gemini being used for broad-bounded internal execution where possible?
Is the result being promoted beyond candidate setting?
Is a new instruction actually needed, or should the current material be compressed?
```

If yes to micro-run convergence, stop and compress.

## Micro-Run Rule

```text
Do not create a run for each missing field.
Do not create a run for each search/read/review step.
Classify once at package level.
Use Gemini instructions for broad-bounded internal execution.
Codex recovers only the packaged return.
```

## Do Not Promote

```text
not schema
not parser
not automation
not registry
not baseline
not current-position update
not memory before Codex recovery
```

`STATUS: WORKER_RETURN_PACKAGING_CANDIDATE_SETTING_THREE_MODES_PREPARED`
