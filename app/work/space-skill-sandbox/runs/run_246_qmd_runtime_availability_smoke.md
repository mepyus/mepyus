# Run 246 - QMD Runtime Availability Smoke

## Status

```yaml
status: closed
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
qmd_help_executed: true
qmd_search_executed: false
qmd_indexing_executed: false
qmd_mcp_executed: false
verdict: PASS_WITH_WATCH_AS_CLI_ENTRY_SMOKE
```

## Purpose

Move one step beyond QMD preflight by checking only whether the QMD CLI can be invoked, while preserving the approval boundary around indexing, search, and MCP.

## Space Basis

```text
Plan from Space, not from Model Default.
```

Activated anchors:

```text
qmd_runtime_preflight_package_v0
movement_record_qmd_runtime_preflight_v0
qmd_direct_source_inspection_report_v0
qmd_vectorfl_retrieval_output_contract_candidate_v0
```

## Work Performed

1. Attempted `npx @tobilu/qmd --help`.
2. Classified npm home-cache EACCES as a local runtime route issue.
3. Re-ran with an explicit temporary npm cache.
4. Confirmed QMD help output returned successfully.
5. Captured the result as CLI-entry smoke only.

## Created Files

```text
app/work/space-skill-sandbox/outputs/qmd_runtime_availability_smoke_return_v0.md
app/work/space-skill-sandbox/outputs/movement_record_qmd_runtime_availability_smoke_v0.md
app/work/space-skill-sandbox/runs/run_246_qmd_runtime_availability_smoke.md
```

## Verdict

```text
PASS_WITH_WATCH_AS_CLI_ENTRY_SMOKE
```

Meaning:

```text
QMD can be fetched and invoked through a temporary npx cache on this machine.
This is not retrieval validation, indexing validation, MCP validation, or VectorFL attachability completion.
```

## Return-to-Space Value

```text
Use an explicit temporary npm cache for future QMD npx trials unless the user's home npm cache is repaired.
Keep the next trial isolated from the default QMD index path.
```

## Next Boundary

```text
An isolated fixture indexing/search trial is the next meaningful runtime step.
It must control storage path and avoid indexing VectorFL.
```

`STATUS: RUN_246_QMD_RUNTIME_AVAILABILITY_SMOKE_CLOSED`
