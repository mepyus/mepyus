# Run 248 - QMD Get / Multi-Get Surface Observation

## Status

```yaml
status: closed
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
qmd_get_executed: true
qmd_multi_get_json_executed: true
qmd_embed_executed: false
qmd_mcp_executed: false
verdict: PASS_WITH_WATCH_AS_BOUNDED_FOLLOW_UP_READ_TRIAL
```

## Purpose

Check whether QMD search pointers can be followed into bounded body reads in the same isolated fixture.

## Work Performed

1. Ran `qmd get` against the accepted anchor-loop pointer with `--json`.
2. Observed markdown body output rather than JSON.
3. Ran `qmd multi-get "*.md" --json`.
4. Observed JSON body bundle output.
5. Captured the surface mismatch and updated the recoverable operating judgment.

## Created Files

```text
app/work/space-skill-sandbox/outputs/qmd_get_multi_get_surface_observation_v0.md
app/work/space-skill-sandbox/outputs/movement_record_qmd_get_multi_get_surface_observation_v0.md
app/work/space-skill-sandbox/runs/run_248_qmd_get_multi_get_surface_observation.md
```

## Verdict

```text
PASS_WITH_WATCH_AS_BOUNDED_FOLLOW_UP_READ_TRIAL
```

Meaning:

```text
QMD can support a two-step fixture pattern:
search --json for candidate pointers
multi-get --json for bounded body bundles
```

Watch:

```text
get --json did not return JSON in this trial.
```

## Return-to-Space Value

```text
Search JSON plus multi-get JSON is now the strongest fixture-level candidate pattern for QMD as an evidence access carrier.
```

`STATUS: RUN_248_QMD_GET_MULTI_GET_SURFACE_OBSERVATION_CLOSED`
