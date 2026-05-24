# QMD Runtime Preflight Package v0

## Status

```yaml
status: runtime_preflight_package
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
runtime_qmd_executed: false
verdict: HOLD_FOR_USER_APPROVAL_BEFORE_INSTALL_INDEX_OR_MCP
```

## Purpose

Lower the QMD attachability work from dry contract validation toward actual runtime entry, without installing, indexing, starting MCP, downloading models, or promoting any contract to baseline.

This package records what is already known, what was checked locally, and where the next approval boundary sits.

## Activated Space Memory

Line:

```text
Plan from Space / Feature-Level External Retrieval Attachability
```

Axis:

```text
retrieval sidecar output vs VectorFL interpreted memory
dry contract validation vs actual runtime execution
local environment fact vs implementation readiness
approval boundary vs silent automation drift
```

Camera:

```text
runtime preflight
environment boundary
provenance integrity
user approval boundary
Return-to-Space recovery
```

Lens:

```text
raw trace boundary
not-inspected disclosure
metadata caution
Movement Record closeout
installation/indexing stop condition
```

Candidate PV signals:

```text
PV_PLAN_BASIS_GATE
PV_NON_INSPECTED_DISCLOSURE
PV_RAW_TRACE_BOUNDARY
PV_RETURN_TO_SPACE_CLOSEOUT
PV_LINE_MATURITY_CAUTION
PV_BROAD_BOUNDED_PACKAGE
```

## Activated Material Families

```text
Run Records
Package Folders
Worker Return / Packaging Records
Current Position / Re-Entry Notes
Task-Mode Gate Specs
External Material Intake Records
Integrated Engine / Operating Surface Records
```

## Bounded Anchors Consulted

```text
app/work/space-skill-sandbox/outputs/qmd_direct_source_inspection_report_v0.md
app/work/space-skill-sandbox/outputs/qmd_vectorfl_retrieval_output_contract_candidate_v0.md
app/work/space-skill-sandbox/outputs/qmd_dry_output_contract_trial_codex_recovery_v0.md
app/work/space-skill-sandbox/outputs/movement_record_qmd_dry_output_contract_trial_v0.md
references/git_search/qmd-main/README.md
references/git_search/qmd-main/package.json
```

## Local Environment Check

Observed facts:

```text
qmd command: absent from PATH
node: v24.13.0
npm: /usr/local/bin/npm
npm version: 11.6.2
bun command: absent from PATH
references/git_search/qmd-main/node_modules: absent
references/git_search/qmd-main/dist: absent
```

Source-side compatibility note:

```text
references/git_search/qmd-main/package.json declares node >=22.0.0.
Current local node version is v24.13.0.
```

This means the environment has a compatible Node runtime and npm available, but no installed QMD CLI and no ready local built QMD checkout.

## Runtime Entry Boundary

The next actual QMD runtime trial would require at least one of the following:

```text
global install route: npm install -g @tobilu/qmd
direct package route: npx @tobilu/qmd ...
local checkout route: install dependencies in references/git_search/qmd-main, then run/build the CLI
```

Each route crosses a user approval boundary because it may involve package download, native dependencies, model-related dependencies, local binary build steps, or persistent installation state.

## Stop Conditions

Do not proceed silently if the next step requires:

```text
npm install
npm install -g
npx package fetch
bun install
bunx package fetch
qmd collection add
qmd embed
qmd mcp
qmd mcp --http
QMD model download or model initialization
indexing a VectorFL corpus
choosing a persistent storage path
writing parser/schema/automation
promoting the QMD contract to baseline
updating current position
```

## Safe Next Trial Shape After Approval

If runtime approval is granted, the smallest useful trial is:

```text
create an isolated temporary markdown fixture
install or run QMD by an approved route
create a tiny isolated collection or index for only that fixture
run one search-like command with JSON output
wrap output as QMD_RETRIEVAL_RETURN_CARD
recover through Codex into candidate pointers / held metadata / watch items
write a Movement Record
```

Preferred retrieval command shape after runtime availability:

```text
qmd search "space anchor return value" --json -n 5
```

Only use this against an isolated fixture until the runtime behavior and output shape are confirmed.

## Expected Execution Return Shape

The external retrieval carrier should return:

```text
source_tool:
delivery_surface:
runtime_route:
command_trace:
collection_scope:
query_text:
result_count:
result_items:
not_inspected_scope:
raw_trace_boundary: true
anchor_usage_trace:
watch_items:
```

Codex recovery should then produce:

```text
accepted candidate evidence pointers
held or mismatched pointers
metadata treated as metadata
not-inspected/gap disclosure
Return-to-Space Value
Movement Record
```

## Current Verdict

```text
HOLD_FOR_USER_APPROVAL_BEFORE_INSTALL_INDEX_OR_MCP
```

Reason:

```text
The next meaningful step is no longer more design. It is actual runtime installation/execution, and that crosses package download or environment mutation boundaries.
```

## Do Not

```text
do not treat this as QMD runtime success
do not treat QMD as installed
do not treat the dry contract as a schema
do not treat retrieval scores or snippets as VectorFL memory
do not index the VectorFL corpus without explicit approval
do not start MCP without explicit approval
do not update current position from this preflight alone
```

`STATUS: QMD_RUNTIME_PREFLIGHT_PACKAGE_PREPARED_WITH_HOLD`
