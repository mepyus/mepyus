# Outputs Summary

verdict: PASS_HERMES_CENTERED_H1_H2_STAGE1_VERIFICATION_WITH_HOLD

## Created run folder

`app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_h1_h2_stage1_verification/`

## Required files

- `run_brief.md`
- `commands_run.md`
- `tool_calls.md`
- `outputs_summary.md`
- `receipt.md`

## H2 verification results

- personal_intake_min fixture tests: PASS
- Phase 1 deterministic stable cycle: PASS
- Phase 0.5 live-safety: PASS
- Phase 0.5 v1 preflight: PASS
- shared DB unchanged: PASS

## shared_db_before

```json
{
  "authority_mutations": 0,
  "executions": 3,
  "fail_events": 0,
  "guardrail_events": 25,
  "maturation_entries": 4,
  "non_hold_reviews": 0,
  "probe_requests": 6,
  "receipts": 5,
  "requests": 10,
  "reviews": 4
}
```

## shared_db_after

```json
{
  "authority_mutations": 0,
  "executions": 3,
  "fail_events": 0,
  "guardrail_events": 25,
  "maturation_entries": 4,
  "non_hold_reviews": 0,
  "probe_requests": 6,
  "receipts": 5,
  "requests": 10,
  "reviews": 4
}
```
