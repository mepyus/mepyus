# QMD Multi-Get Pattern Behavior Source Inspection v0

## Status

```yaml
status: bounded_source_inspection
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
source_target: references/git_search/qmd-main
verdict: PASS_AS_WATCH_DOWNSHIFT_SOURCE_INSPECTION
```

## Purpose

Inspect the `multi-get` pattern mismatch that appeared in QMD VectorFL subset 001 and recover it as a clear watch item instead of treating it as a retrieval failure.

## Source Files Inspected

```text
references/git_search/qmd-main/src/cli/qmd.ts
references/git_search/qmd-main/src/store.ts
references/git_search/qmd-main/README.md
```

## Runtime Symptom

This failed:

```text
qmd multi-get "*movement-record*.md,*next-chat*.md" --json --max-bytes 20000
```

Observed:

```text
No files matched pattern
```

This succeeded:

```text
qmd multi-get "qmd://vectorfl_subset001/movement-record-qmd-get-multi-get-surface-observation-v0.md,qmd://vectorfl_subset001/next-chat-reentry-summary-after-space-aware-external-execution-loop-v0.md" --json --max-bytes 20000
```

## Source Explanation

The CLI classifies multi-get input as comma-separated only when the pattern contains a comma and does not contain glob syntax:

```text
pattern includes comma
and pattern does not include *
and pattern does not include ?
and pattern does not include {
```

Therefore:

```text
*movement-record*.md,*next-chat*.md
```

is not treated as two comma-separated globs. Because it contains `*`, it is treated as one glob pattern.

The glob matcher compares the single pattern against:

```text
qmd virtual path
relative document path
collection/path
```

That single comma-containing glob did not match the subset files.

## README Alignment

README examples separate:

```text
glob pattern: qmd multi-get "journals/2025-05*.md"
comma-separated list: qmd multi-get "doc1.md, doc2.md, #abc123"
```

It does not claim support for comma-separated glob patterns.

## Downshifted Watch

Old watch:

```text
multi_get_glob_pattern_mismatch_watch
```

More precise watch:

```text
multi_get_comma_glob_not_supported_watch
```

Operational note:

```text
Use one glob pattern at a time, or use comma-separated exact file/qmd URI/docid values.
```

## Return-to-Space Value

Recoverable material:

```text
The subset multi-get failure came from input classification behavior, not from QMD being unable to retrieve the files.
```

Reusable judgment:

```text
For QMD follow-up reads, use qmd URI exact lists after search pointer discovery. Do not use comma-separated glob patterns unless source behavior changes.
```

Issue / watch:

```text
multi_get_comma_glob_not_supported_watch
qmd_uri_exact_list_more_reliable_watch
```

Future reuse note:

```text
If multi-get must retrieve multiple glob groups, run separate glob calls or collect exact qmd URIs first.
```

## Do Not

```text
do not treat the failed comma-glob as retrieval failure
do not create parser/schema from this observation
do not promote to baseline
do not update current position
```

`STATUS: QMD_MULTI_GET_PATTERN_BEHAVIOR_SOURCE_INSPECTION_PREPARED`
