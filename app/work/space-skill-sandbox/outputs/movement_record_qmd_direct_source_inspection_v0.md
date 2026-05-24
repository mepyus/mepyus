# Movement Record - QMD Direct Source Inspection v0

## Status

```yaml
status: movement_record_candidate
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
verdict: PASS_WITH_WATCH
```

## Input Purpose

Continue from the two-test candidate operating note into bounded direct source inspection of `qmd-main`.

Goal:

```text
Inspect qmd-main directly enough to determine whether its retrieval output surfaces can support a future VectorFL-facing evidence-output contract candidate.
```

## Activated Space Memory / Anchors

```text
Plan from Space / Feature-Level External Retrieval Attachability
QMD as bounded retrieval-side candidate
PV_RAW_TRACE_BOUNDARY
PV_NON_INSPECTED_DISCLOSURE
PV_RETURN_TO_SPACE_CLOSEOUT
feature-level attach vs repo-level import
retrieval sidecar support vs VectorFL source-of-truth replacement
```

## Space Assets Consulted

```text
app/work/space-skill-sandbox/outputs/space_aware_external_execution_loop_two_test_candidate_operating_note_v0.md
app/work/space-skill-sandbox/outputs/movement_record_space_loop_test_002_qmd_attachability_v0.md
docs/reports/space_external_tool_repo_attach_inventory_report_v0.md
docs/reports/space_external_tool_repo_attach_feasibility_report_v0.md
docs/guides/space_asset_retrieval_manual_v0.md
docs/reports/space_cli_memory_card_retrieval_minimum_v0.md
```

## External Tool / Source Role

```text
source_material: references/git_search/qmd-main
role: imported external retrieval tool source
execution_role: source inspection only
authority_state: external_reference_raw_trace
```

## Tool Output Summary

No external execution carrier was run in this step.

Codex directly inspected bounded QMD source surfaces and created:

```text
app/work/space-skill-sandbox/outputs/qmd_direct_source_inspection_report_v0.md
app/work/space-skill-sandbox/outputs/qmd_vectorfl_retrieval_output_contract_candidate_v0.md
```

## Anchor Usage Trace

The inspection stayed focused on:

```text
retrieval output surfaces
agent-facing output formats
MCP tool return shapes
SDK surface
context/collection metadata
raw trace boundary
```

It did not move into:

```text
installing QMD
running QMD
indexing VectorFL
choosing storage
starting MCP
creating schema
creating automation
approving import
```

## Evidence / Not Inspected / Gap

Evidence:

```text
references/git_search/qmd-main/README.md
references/git_search/qmd-main/package.json
references/git_search/qmd-main/src/cli/qmd.ts
references/git_search/qmd-main/src/cli/formatter.ts
references/git_search/qmd-main/src/mcp/server.ts
references/git_search/qmd-main/src/index.ts
references/git_search/qmd-main/src/collections.ts
references/git_search/qmd-main/test/cli.test.ts
references/git_search/qmd-main/test/mcp.test.ts
references/git_search/qmd-main/test/formatter.test.ts
```

Not inspected:

```text
full QMD store internals
full benchmark/eval harness
runtime model behavior
actual command execution
real VectorFL corpus indexing
current upstream QMD state beyond local imported repo
```

Gap:

```text
The contract candidate is source-backed but not runtime-tested.
No actual QMD output was produced against VectorFL files.
```

## Issue / Watch Item

```text
retrieval_score_authority_watch
context_metadata_authority_watch
qmd_uri_memory_promotion_watch
model_download_runtime_cost_watch
mcp_setup_overpromotion_watch
storage_schema_pressure_watch
```

## User Decision Point

The user remains direction judge.

Decision now available:

```text
Proceed to a dry output-contract trial using synthetic/sample QMD return shape, or require actual QMD installation/indexing approval before runtime testing.
```

## Return-to-Space Value

Recoverable material:

```text
QMD has concrete output surfaces that can support a VectorFL-facing retrieval-output contract candidate.
```

Reusable judgment:

```text
The safest next attach step is not implementation. It is contract-level validation of QMD retrieval returns as raw evidence pointers.
```

Issue / watch:

```text
QMD scores, contexts, snippets, docids, and qmd:// URIs must not be promoted to VectorFL memory without Codex/space recovery.
```

Future reuse note:

```text
Use the contract candidate before any runtime QMD package. It should define what Codex expects to receive and what must remain raw trace.
```

## Next Re-Entry Trigger

```text
When preparing a QMD dry output-contract trial.
When considering QMD installation or indexing.
When receiving retrieval output from any QMD-like sidecar.
```

## Do Not

```text
do not promote to baseline
do not create automation
do not create schema/registry/storage
do not call QMD ready
do not claim runtime validation
do not update current position
```

`STATUS: MOVEMENT_RECORD_QMD_DIRECT_SOURCE_INSPECTION_PREPARED`
