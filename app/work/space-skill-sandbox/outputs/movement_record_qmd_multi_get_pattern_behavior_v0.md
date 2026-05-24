# Movement Record - QMD Multi-Get Pattern Behavior v0

## Status

```yaml
status: movement_record_candidate
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
source_inspection_executed: true
runtime_execution_executed: false
verdict: PASS_WITH_WATCH_AS_PATTERN_MISMATCH_DOWNSHIFT
```

## Input Purpose

Recover the QMD subset trial's multi-get pattern mismatch by inspecting source behavior and converting the confusion into a reusable operating watch.

## Activated Space Memory

Line:

```text
Plan from Space / Feature-Level External Retrieval Attachability
```

Axis:

```text
runtime mismatch vs source behavior
glob input expectation vs exact qmd URI list
confusion recovery vs failure overclaim
```

Camera:

```text
source-backed downshift
watch item precision
future retrieval carrier behavior
```

Lens:

```text
not-inspected disclosure
raw trace boundary
Return-to-Space recovery
```

## Space Assets Consulted

```text
app/work/space-skill-sandbox/outputs/movement_record_qmd_vectorfl_subset_001_trial_v0.md
app/work/space-skill-sandbox/outputs/qmd_vectorfl_subset_001_execution_return_v0.md
references/git_search/qmd-main/src/cli/qmd.ts
references/git_search/qmd-main/src/store.ts
references/git_search/qmd-main/README.md
```

## External Tool Role

```text
tool: QMD source
role: behavior clarification source
execution_boundary: no new QMD runtime execution
```

## Tool Output Summary

The source inspection showed that QMD treats comma-separated input as a list only when it contains no glob syntax.

Because the failed input contained both comma and `*`, it was treated as a single glob pattern, not as two globs.

## Read Trace / Evidence

```text
src/cli/qmd.ts:
  multiGet checks pattern.includes(',') and absence of *, ?, { before comma-list mode.

src/store.ts:
  findDocuments uses the same comma-list vs glob classification.

src/store.ts:
  matchFilesByGlob tests virtual path, document path, and collection/path against one pattern.

README.md:
  examples show one glob pattern or comma-separated exact docs/docids, not comma-separated glob groups.
```

## Issue / Watch Item

```text
multi_get_comma_glob_not_supported_watch
qmd_uri_exact_list_more_reliable_watch
```

## User Decision Point

No immediate user decision required.

This watch should reappear before any larger QMD follow-up read flow.

## Return-to-Space Value

Recoverable material:

```text
QMD's multi-get mismatch is now explained and downshifted: comma-glob input is not the safe shape.
```

Reusable judgment:

```text
After search pointer discovery, follow-up reads should use exact qmd URI lists or one glob call at a time.
```

Issue / watch:

```text
Do not use comma-separated glob groups for QMD multi-get until source behavior changes.
```

Future reuse note:

```text
The next QMD subset trial should build a qmd URI exact list from search results before multi-get.
```

## Next Re-Entry Trigger

```text
When repeating QMD on another material-family subset.
When designing QMD follow-up read packaging.
When a worker proposes comma-separated glob groups.
```

## Do Not

```text
do not promote to baseline
do not create schema/parser/automation
do not treat this as QMD failure
do not update current position
```

`STATUS: MOVEMENT_RECORD_QMD_MULTI_GET_PATTERN_BEHAVIOR_PREPARED`
