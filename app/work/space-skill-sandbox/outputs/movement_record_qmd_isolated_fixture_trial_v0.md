# Movement Record - QMD Isolated Fixture Retrieval Trial v0

## Status

```yaml
status: movement_record_candidate
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
qmd_collection_add_executed: true
qmd_search_json_executed: true
qmd_status_executed: true
qmd_embed_executed: false
qmd_mcp_executed: false
verdict: PASS_WITH_WATCH_AS_FIRST_REAL_QMD_RETRIEVAL_RETURN
```

## Input Purpose

Run one actual external retrieval carrier trial where QMD reads only a tiny fixture and returns JSON evidence pointers that Codex can recover into VectorFL space.

## Activated Space Memory / Anchors

Line:

```text
Plan from Space / Feature-Level External Retrieval Attachability
```

Axis:

```text
retrieval carrier execution vs VectorFL memory
fixture evidence pointer vs corpus integration
runtime output shape vs schema promotion
metadata caution vs authority drift
```

Material families:

```text
Run Records
Package Folders
Worker Return / Packaging Records
External Material Intake Records
Task-Mode Gate Specs
Integrated Engine / Operating Surface Records
```

Anchors:

```text
qmd_runtime_preflight_package_v0
qmd_runtime_availability_smoke_return_v0
qmd_vectorfl_retrieval_output_contract_candidate_v0
qmd_direct_source_inspection_report_v0
movement_record_qmd_runtime_availability_smoke_v0
```

## External Tool Role

```text
tool: QMD
role: retrieval sidecar candidate
execution_surface: CLI search JSON
carrier_scope: isolated fixture only
```

## Tool Output Summary

QMD indexed three fixture markdown files into an isolated temporary index:

```text
/private/tmp/vectorfl-qmd-xdg-cache/qmd/index.sqlite
```

QMD returned two JSON search results for:

```text
Return-to-Space Value
```

Returned candidate pointers:

```text
qmd://fixture001/anchor-loop-note.md
qmd://fixture001/qmd-boundary-note.md
```

## Anchor Usage Trace

The Anchor Packet / preflight boundary shaped execution behavior:

```text
use fixture, not VectorFL corpus
use BM25 search, not query/vsearch/embed
use CLI JSON, not MCP
use temporary cache/config/index paths
recover result as raw trace
```

The QMD retrieval output contract candidate shaped packaging behavior:

```text
wrap source_tool
wrap delivery_surface
record query mode and collection scope
record result count and result items
mark raw_trace_boundary
require Codex recovery
```

## Evidence / Not Inspected / Gap

Evidence:

```text
collection add succeeded for exactly 3 fixture markdown files
search --json returned 2 result items
status confirmed isolated index path under /private/tmp
status confirmed 0 embedded vectors and 3 pending embeddings
```

Not inspected:

```text
qmd get
qmd multi-get
qmd --files
qmd --explain
qmd query/rerank
qmd vsearch
qmd embed
qmd mcp
SDK usage
VectorFL corpus indexing
```

Gap:

```text
Only the CLI search JSON surface has first runtime evidence.
```

## User Decision Point

User remains direction judge.

Available next choices:

```text
same fixture follow-up read with qmd get / multi-get
larger bounded fixture trial
small VectorFL subset trial with explicit scope
hold QMD at fixture retrieval evidence level
```

## Return-to-Space Value

Recoverable material:

```text
QMD can act as an external retrieval carrier for candidate evidence pointers in an isolated fixture trial.
```

Reusable judgment:

```text
The safe first attach layer is evidence-pointer return, not memory writing or automated ingestion.
```

Issue / watch:

```text
score_zero_but_semantically_matched_watch
metadata_authority_watch
fixture_success_overclaim_watch
qmd_uri_filename_normalization_watch
temporary_index_cleanup_watch
```

Future reuse note:

```text
Use the same isolated fixture setup to test qmd get / multi-get before moving to any VectorFL subset.
```

## Do Not

```text
do not promote to baseline
do not update current position
do not create parser/schema/automation
do not index VectorFL corpus yet
do not start MCP yet
do not treat fixture success as integration
```

`STATUS: MOVEMENT_RECORD_QMD_ISOLATED_FIXTURE_TRIAL_PREPARED`
