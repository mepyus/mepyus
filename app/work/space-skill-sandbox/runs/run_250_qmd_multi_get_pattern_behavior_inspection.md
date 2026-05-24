# Run 250 - QMD Multi-Get Pattern Behavior Inspection

## Status

```yaml
status: closed
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
source_inspection_executed: true
runtime_execution_executed: false
verdict: PASS_WITH_WATCH_AS_PATTERN_MISMATCH_DOWNSHIFT
```

## Purpose

Inspect the multi-get pattern mismatch from run 249 and recover it as a precise watch item.

## Work Performed

1. Re-read run 249 Movement Record.
2. Inspected QMD CLI and store source around multi-get classification.
3. Compared source behavior with README examples.
4. Downshifted the mismatch from generic glob failure to comma-glob unsupported behavior.
5. Wrote source inspection and Movement Record.

## Created Files

```text
app/work/space-skill-sandbox/outputs/qmd_multi_get_pattern_behavior_source_inspection_v0.md
app/work/space-skill-sandbox/outputs/movement_record_qmd_multi_get_pattern_behavior_v0.md
app/work/space-skill-sandbox/runs/run_250_qmd_multi_get_pattern_behavior_inspection.md
```

## Verdict

```text
PASS_WITH_WATCH_AS_PATTERN_MISMATCH_DOWNSHIFT
```

## Return-to-Space Value

```text
QMD follow-up reads should use exact qmd URI lists after search pointer discovery, or one glob pattern at a time. Comma-separated glob groups are not the safe operating shape.
```

`STATUS: RUN_250_QMD_MULTI_GET_PATTERN_BEHAVIOR_INSPECTION_CLOSED`
