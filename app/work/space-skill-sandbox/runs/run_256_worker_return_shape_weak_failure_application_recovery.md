# Run 256 - Worker Return Shape Weak Failure Application Recovery

## Status

```yaml
status: closed
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
verdict: HOLD_WITH_RECOVERABLE_FAILURE_SIGNAL
```

## Purpose

Recover Gemini's application of the worker-return candidate shape to one weak/failed external result.

## Work Performed

1. Accepted Gemini result as candidate material.
2. Checked presence of target, diagnosis, and raw-result pointer.
3. Downshifted over-strong failure language.
4. Captured HOLD behavior for empty worker returns.
5. Updated compact candidate setting with success and HOLD modes.
6. Wrote one package-level Movement Record.

## Created Files

```text
app/work/space-skill-sandbox/outputs/gemini_weak_partial_worker_return_shape_application_packaging_v0.md
app/work/space-skill-sandbox/outputs/worker_return_packaging_candidate_setting_success_and_hold_v0.md
app/work/space-skill-sandbox/outputs/movement_record_worker_return_shape_weak_failure_application_recovery_v0.md
app/work/space-skill-sandbox/runs/run_256_worker_return_shape_weak_failure_application_recovery.md
```

## Verdict

```text
HOLD_WITH_RECOVERABLE_FAILURE_SIGNAL
```

## Return-to-Space Value

```text
The worker-return shape now has one success-case application and one empty-failure HOLD application. This supports package-level triage without Codex micro-runs, while keeping the shape candidate-only.
```

## Watch Items

```text
empty_return_hold
missing_anchor_usage_hold
missing_return_to_space_value_hold
failure_diagnosis_raw_trace_watch
response_bundle_strategy_promotion_watch
micro_run_proliferation_watch
```

`STATUS: RUN_256_WORKER_RETURN_SHAPE_WEAK_FAILURE_APPLICATION_RECOVERY_CLOSED`
