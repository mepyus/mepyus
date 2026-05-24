# Movement Record - QMD Runtime Preflight v0

## Status

```yaml
status: movement_record_candidate
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
runtime_qmd_executed: false
verdict: HOLD_FOR_USER_APPROVAL_BEFORE_RUNTIME_ENTRY
```

## Input Purpose

Continue the QMD attachability work while keeping the current task space-aware: inspect the relevant space anchors, check local runtime readiness, and identify the next boundary before actual QMD execution.

## Activated Space Memory / Anchors

Line:

```text
Plan from Space / Feature-Level External Retrieval Attachability
```

Axis:

```text
retrieval sidecar output vs VectorFL interpreted memory
dry contract validation vs runtime implementation
environment fact vs operational approval
```

Material families:

```text
Run Records
Package Folders
Worker Return / Packaging Records
External Material Intake Records
Integrated Engine / Operating Surface Records
Task-Mode Gate Specs
```

Files consulted:

```text
app/work/space-skill-sandbox/outputs/movement_record_qmd_dry_output_contract_trial_v0.md
app/work/space-skill-sandbox/outputs/qmd_vectorfl_retrieval_output_contract_candidate_v0.md
app/work/space-skill-sandbox/outputs/qmd_direct_source_inspection_report_v0.md
references/git_search/qmd-main/README.md
references/git_search/qmd-main/package.json
```

## External Tool Role

```text
tool_target: QMD
role: retrieval sidecar candidate
runtime_state: not installed / not executed
carrier_state: not attached
```

## Tool Output Summary

No QMD runtime output was produced.

Local preflight checks produced these facts:

```text
qmd command: absent from PATH
node: v24.13.0
npm: available at /usr/local/bin/npm
npm version: 11.6.2
bun command: absent from PATH
local qmd node_modules: absent
local qmd dist: absent
```

## Anchor Usage Trace

The dry output contract anchor shaped the expected return card and recovery boundary.

The direct source inspection anchor supplied the known QMD surfaces:

```text
CLI JSON/files/markdown/csv/xml output
MCP query/get/multi_get/status
SDK search/get/multiGet
```

The package source supplied the environment requirement:

```text
node >=22.0.0
```

The README supplied the install/runtime paths and MCP/indexing operations that must be treated as stop conditions before user approval.

## Evidence / Not Inspected / Gap

Evidence:

```text
command availability was checked locally
node/npm/bun availability was checked locally
local qmd dependency/build folders were checked locally
README and package.json were re-read
```

Not inspected:

```text
whether global QMD could be installed successfully
whether native dependencies compile on this machine
whether node-llama-cpp or sqlite native packages initialize correctly
whether QMD can index a real or fixture corpus
whether QMD JSON output matches the candidate wrapper in a live run
whether MCP startup works
```

Gap:

```text
actual runtime evidence is still missing
```

## User Decision Point

User judgment is required before crossing runtime boundary:

```text
approve an isolated QMD runtime trial
keep QMD at source-inspection / dry-contract level
choose another external retrieval carrier
```

## Return-to-Space Value

Recoverable material:

```text
QMD runtime entry is now blocked on approval, not on more design.
```

Reusable judgment:

```text
Before attaching a retrieval carrier, Codex should separate environment facts from runtime evidence and stop before install/index/MCP boundaries.
```

Issue / watch:

```text
install_boundary_watch
native_dependency_watch
model_download_watch
indexing_scope_watch
mcp_background_process_watch
retrieval_metadata_authority_watch
runtime_success_overclaim_watch
```

Future reuse note:

```text
Use qmd_runtime_preflight_package_v0.md as the approval gate before the first real QMD runtime trial.
```

## Do Not

```text
do not promote to baseline
do not create parser/schema
do not create automation
do not claim QMD runtime validation
do not index VectorFL corpus
do not start MCP
do not update current position from this alone
```

`STATUS: MOVEMENT_RECORD_QMD_RUNTIME_PREFLIGHT_PREPARED_WITH_HOLD`
