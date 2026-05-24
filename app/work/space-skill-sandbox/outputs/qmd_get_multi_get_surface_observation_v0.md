# QMD Get / Multi-Get Surface Observation v0

## Status

```yaml
status: runtime_surface_observation
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
qmd_get_executed: true
qmd_multi_get_json_executed: true
qmd_embed_executed: false
qmd_mcp_executed: false
verdict: PASS_WITH_WATCH_AS_FOLLOW_UP_READ_SURFACE_OBSERVATION
```

## Purpose

Test whether candidate pointers returned by QMD search can support bounded follow-up reads in the same isolated fixture.

## Runtime Scope

```text
same fixture001 collection
same temporary npx cache
same temporary XDG cache and QMD config
no VectorFL corpus
no embedding
no MCP
no schema/parser/automation
```

## Command Trace

Get command:

```text
env XDG_CACHE_HOME=/private/tmp/vectorfl-qmd-xdg-cache QMD_CONFIG_DIR=/private/tmp/vectorfl-qmd-config npx --cache /private/tmp/vectorfl-qmd-npm-cache @tobilu/qmd get qmd://fixture001/anchor-loop-note.md --json
```

Observed output:

```text
exit_code: 0
returned markdown body, not JSON
```

Multi-get command:

```text
env XDG_CACHE_HOME=/private/tmp/vectorfl-qmd-xdg-cache QMD_CONFIG_DIR=/private/tmp/vectorfl-qmd-config npx --cache /private/tmp/vectorfl-qmd-npm-cache @tobilu/qmd multi-get "*.md" --json
```

Observed output:

```text
exit_code: 0
returned JSON array with file, title, body fields
```

## Live Surface Findings

Search JSON:

```text
best current surface for evidence pointers
fields observed: docid, score, file, title, snippet
```

Get:

```text
useful for direct body retrieval
but live `get --json` returned markdown body in this trial
do not assume get JSON structure without further source/runtime review
```

Multi-get JSON:

```text
useful for bounded body bundle retrieval
fields observed: file, title, body
```

## Multi-Get JSON Shape Observed

```text
[
  {
    file:
    title:
    body:
  }
]
```

Observed fixture body results:

```text
anchor-loop-note.md
lacl-layer-note.md
qmd-boundary-note.md
```

## Contract Downshift

Previous candidate expectation:

```text
get-like and multi-get-like results can be wrapped as structured follow-up read surfaces.
```

Runtime correction:

```text
multi-get --json is currently supported as a structured body bundle in this trial.
get --json was not observed as JSON in this trial; treat it as raw body text unless separately confirmed.
```

## Return-to-Space Value

Recoverable material:

```text
QMD search JSON pointers can be followed by QMD multi-get JSON body retrieval in an isolated fixture.
```

Reusable judgment:

```text
Use search --json for candidate pointer discovery and multi-get --json for bounded body bundle recovery. Do not assume get --json emits JSON from this trial.
```

Issue / watch:

```text
get_json_surface_mismatch_watch
multi_get_body_bundle_surface_candidate
body_text_not_interpreted_memory_watch
fixture_scope_only_watch
```

## Do Not

```text
do not update the candidate contract as baseline
do not build parser/schema from this single observation
do not treat body bundle as memory
do not index VectorFL corpus
do not start MCP
```

`STATUS: QMD_GET_MULTI_GET_SURFACE_OBSERVATION_PREPARED`
