# QMD Isolated Fixture Trial Execution Return v0

## Status

```yaml
status: execution_return
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
qmd_collection_add_executed: true
qmd_search_json_executed: true
qmd_status_executed: true
qmd_embed_executed: false
qmd_query_executed: false
qmd_vsearch_executed: false
qmd_mcp_executed: false
verdict: PASS_AS_ISOLATED_FIXTURE_RETRIEVAL_RETURN_WITH_WATCH
```

## Purpose

Run the first real QMD retrieval trial against a tiny isolated fixture, not against the VectorFL corpus, to verify whether QMD can produce a recoverable retrieval return card.

## Runtime Boundary

Execution route:

```text
npx with explicit temporary npm cache
XDG_CACHE_HOME=/private/tmp/vectorfl-qmd-xdg-cache
QMD_CONFIG_DIR=/private/tmp/vectorfl-qmd-config
```

Isolation:

```text
fixture corpus only
no VectorFL corpus indexing
no embed
no query/rerank
no vsearch
no MCP
no daemon
no parser/schema/automation
```

Fixture files:

```text
app/work/space-skill-sandbox/tmp/qmd_fixture_001/anchor_loop_note.md
app/work/space-skill-sandbox/tmp/qmd_fixture_001/lacl_layer_note.md
app/work/space-skill-sandbox/tmp/qmd_fixture_001/qmd_boundary_note.md
```

## Command Trace

Collection add:

```text
env XDG_CACHE_HOME=/private/tmp/vectorfl-qmd-xdg-cache QMD_CONFIG_DIR=/private/tmp/vectorfl-qmd-config npx --cache /private/tmp/vectorfl-qmd-npm-cache @tobilu/qmd collection add app/work/space-skill-sandbox/tmp/qmd_fixture_001 --name fixture001
```

Result:

```text
Indexed: 3 new, 0 updated, 0 unchanged, 0 removed
Collection 'fixture001' created successfully
```

Search:

```text
env XDG_CACHE_HOME=/private/tmp/vectorfl-qmd-xdg-cache QMD_CONFIG_DIR=/private/tmp/vectorfl-qmd-config npx --cache /private/tmp/vectorfl-qmd-npm-cache @tobilu/qmd search "Return-to-Space Value" --json -n 5 -c fixture001
```

Status:

```text
env XDG_CACHE_HOME=/private/tmp/vectorfl-qmd-xdg-cache QMD_CONFIG_DIR=/private/tmp/vectorfl-qmd-config npx --cache /private/tmp/vectorfl-qmd-npm-cache @tobilu/qmd status
```

Status summary:

```text
Index: /private/tmp/vectorfl-qmd-xdg-cache/qmd/index.sqlite
Documents: 3 files indexed
Vectors: 0 embedded
Pending: 3 need embedding
Collection: fixture001
GPU: none
```

## Raw Search JSON

```json
[
  {
    "docid": "#1aeaf8",
    "score": 0,
    "file": "qmd://fixture001/anchor-loop-note.md",
    "title": "Anchor Loop Note",
    "snippet": "@@ -10,4 @@ (9 before, 5 after)\nexecution return\nReturn-to-Space Value\nMovement Record\nfuture reuse"
  },
  {
    "docid": "#bfa19a",
    "score": 0,
    "file": "qmd://fixture001/qmd-boundary-note.md",
    "title": "QMD Boundary Note",
    "snippet": "@@ -6,4 @@ (5 before, 0 after)\n\nCodex recovery must classify accepted pointers, held metadata, not-inspected scope, watch items, and Return-to-Space Value before anything enters VectorFL memory.\n\n"
  }
]
```

## QMD_RETRIEVAL_RETURN_CARD

```text
source_tool: qmd
delivery_surface: cli_json
runtime_route: npx_temporary_cache
qmd_command_or_tool: search
query_mode: bm25_full_text
query_text_or_document: Return-to-Space Value
intent: find candidate evidence pointers in isolated fixture for Return-to-Space loop recovery
collection_scope: fixture001
limit: 5
min_score: not_set
rerank_used: false
explain_requested: false
result_count: 2
raw_trace_boundary: true
recovery_required: true
```

Result items:

```text
1.
  docid: #1aeaf8
  file_or_uri: qmd://fixture001/anchor-loop-note.md
  title: Anchor Loop Note
  score: 0
  snippet: execution return / Return-to-Space Value / Movement Record / future reuse

2.
  docid: #bfa19a
  file_or_uri: qmd://fixture001/qmd-boundary-note.md
  title: QMD Boundary Note
  score: 0
  snippet: Codex recovery must classify accepted pointers, held metadata, not-inspected scope, watch items, and Return-to-Space Value
```

Not inspected scope:

```text
live get output
live multi-get output
live --files output
live --explain output
live query/rerank output
live vsearch/vector output
MCP output
SDK output
VectorFL corpus output
```

Watch items:

```text
score_zero_but_semantically_matched_watch
qmd_uri_filename_normalization_watch
snippet_as_pointer_not_truth_watch
default_models_list_status_not_download_watch
embedding_pending_not_required_for_bm25_watch
fixture_scope_only_watch
```

## Anchor Usage Trace

The QMD output contract candidate correctly predicted a recoverable search JSON surface carrying:

```text
docid
score
file/qmd uri
title
snippet
```

The runtime preflight guard correctly prevented:

```text
VectorFL corpus indexing
embedding/model download
MCP startup
schema/parser creation
baseline promotion
```

## Execution Verdict

```text
PASS_AS_ISOLATED_FIXTURE_RETRIEVAL_RETURN_WITH_WATCH
```

Meaning:

```text
QMD produced real CLI JSON retrieval output from an isolated fixture and the output can be wrapped as a VectorFL retrieval return card.
```

Limit:

```text
This does not validate QMD on the VectorFL corpus, MCP, SDK, embeddings, reranking, or automated memory ingestion.
```

`STATUS: QMD_ISOLATED_FIXTURE_TRIAL_EXECUTION_RETURN_PREPARED`
