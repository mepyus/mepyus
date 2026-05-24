# Movement Record - QMD Runtime Availability Smoke v0

## Status

```yaml
status: movement_record_candidate
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

## Input Purpose

After the runtime preflight hold, perform only the smallest QMD CLI availability check that does not index, search, start MCP, or create a VectorFL ingestion path.

## Activated Space Memory / Anchors

Line:

```text
Plan from Space / Feature-Level External Retrieval Attachability
```

Axis:

```text
runtime entry evidence vs retrieval evidence
temporary execution route vs persistent install
default tool storage vs VectorFL-approved storage
```

Material families:

```text
Run Records
Worker Return / Packaging Records
External Material Intake Records
Task-Mode Gate Specs
Integrated Engine / Operating Surface Records
```

Files consulted or activated:

```text
app/work/space-skill-sandbox/outputs/qmd_runtime_preflight_package_v0.md
app/work/space-skill-sandbox/outputs/movement_record_qmd_runtime_preflight_v0.md
app/work/space-skill-sandbox/outputs/qmd_direct_source_inspection_report_v0.md
app/work/space-skill-sandbox/outputs/qmd_vectorfl_retrieval_output_contract_candidate_v0.md
```

## External Tool Role

```text
source_tool: QMD
delivery_route: npx temporary-cache CLI invocation
command: npx --cache /private/tmp/vectorfl-qmd-npm-cache @tobilu/qmd --help
authority_state: CLI entry smoke only
```

## Tool Output Summary

The first npx attempt failed because the user's home npm cache contains root-owned files.

The second npx attempt used an explicit temporary cache and returned QMD help successfully.

This validates:

```text
QMD package can be fetched by npx in this environment.
QMD CLI entry can start enough to print help.
The local Node runtime can execute the package at help level.
```

This does not validate:

```text
search
indexing
embedding
reranking
MCP
SDK
JSON output contract
VectorFL corpus attachability
```

## Anchor Usage Trace

The preflight package prevented accidental escalation from help smoke into indexing/search/MCP.

The direct source inspection gave a prior expected list of CLI commands and output formats; the live help output aligned with that list.

The QMD output contract candidate remains unvalidated at runtime because no live retrieval output was produced.

## Evidence / Not Inspected / Gap

Evidence:

```text
first command failed with npm EACCES on home cache
second command exited 0 using /private/tmp/vectorfl-qmd-npm-cache
QMD help output listed CLI commands and output formats
QMD help output displayed default index path /Users/sungsookim/.cache/qmd/index.sqlite
```

Not inspected:

```text
whether QMD can create an isolated index
whether QMD can search a fixture
whether QMD can emit JSON results matching the candidate return card
whether default index path can or should be used
whether model-related commands trigger downloads
whether MCP startup is stable
```

Gap:

```text
actual retrieval return evidence is still missing
```

## User Decision Point

The next user decision is whether to approve an isolated fixture trial.

Minimum next runtime trial:

```text
use temporary npm cache
use temporary QMD index/storage location if supported or confirmed
create a tiny markdown fixture
add only that fixture as a collection
run one --json search
wrap output in QMD_RETRIEVAL_RETURN_CARD
recover through Codex
write Movement Record
```

## Return-to-Space Value

Recoverable material:

```text
QMD is now confirmed as CLI-entry reachable through npx temporary cache, but not yet retrieval-validated.
```

Reusable judgment:

```text
Separate CLI availability smoke from retrieval contract validation. A successful help command must not be promoted into attachability proof.
```

Issue / watch:

```text
npm_home_cache_permission_watch
default_qmd_index_path_outside_workspace_watch
temporary_cache_route_watch
retrieval_not_yet_validated_watch
```

Future reuse note:

```text
Use the temporary-cache npx route for the next isolated QMD runtime trial unless a persistent install route is explicitly approved.
```

## Do Not

```text
do not promote to baseline
do not create parser/schema
do not create automation
do not claim retrieval validation
do not use the default home QMD index path without review
do not index VectorFL corpus
do not start MCP
do not update current position from this alone
```

`STATUS: MOVEMENT_RECORD_QMD_RUNTIME_AVAILABILITY_SMOKE_PREPARED`
