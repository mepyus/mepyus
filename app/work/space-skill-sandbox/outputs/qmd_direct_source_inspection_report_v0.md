# QMD Direct Source Inspection Report v0

## Status

```yaml
status: bounded_source_inspection_report
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
implementation: false
source_target: references/git_search/qmd-main
verdict: PASS_AS_BOUNDED_RETRIEVAL_OUTPUT_SURFACE_INSPECTION_WITH_WATCH
```

## Purpose

Inspect `qmd-main` directly enough to determine whether a QMD-like retrieval sidecar has concrete output surfaces that could support a future VectorFL evidence-output contract candidate.

This report does not approve import, implementation, storage, MCP setup, runtime attach, or readiness.

## Source Files Inspected

```text
references/git_search/qmd-main/README.md
references/git_search/qmd-main/package.json
references/git_search/qmd-main/src/cli/qmd.ts
references/git_search/qmd-main/src/cli/formatter.ts
references/git_search/qmd-main/src/mcp/server.ts
references/git_search/qmd-main/src/index.ts
references/git_search/qmd-main/src/collections.ts
references/git_search/qmd-main/skills/qmd/SKILL.md
references/git_search/qmd-main/docs/SYNTAX.md
references/git_search/qmd-main/test/cli.test.ts
references/git_search/qmd-main/test/mcp.test.ts
references/git_search/qmd-main/test/formatter.test.ts
```

## What QMD Is

QMD describes itself as an on-device search engine for markdown notes, transcripts, documentation, and knowledge bases.

Source pointers:

```text
references/git_search/qmd-main/README.md:3
references/git_search/qmd-main/README.md:5
references/git_search/qmd-main/package.json:2
references/git_search/qmd-main/package.json:4
```

It combines:

```text
BM25 full-text search
vector semantic search
LLM reranking
local node-llama-cpp / GGUF model usage
```

VectorFL read:

```text
QMD is a retrieval / evidence access candidate, not a VectorFL memory replacement.
```

## Concrete User-Facing Surfaces

QMD exposes:

```text
CLI command: qmd
SDK/library export: @tobilu/qmd
MCP server: stdio and HTTP
HTTP endpoints: /mcp and /query or /search
```

Source pointers:

```text
references/git_search/qmd-main/package.json:14
references/git_search/qmd-main/README.md:57
references/git_search/qmd-main/README.md:72
references/git_search/qmd-main/README.md:115
references/git_search/qmd-main/src/index.ts:210
references/git_search/qmd-main/src/mcp/server.ts:241
references/git_search/qmd-main/src/mcp/server.ts:368
references/git_search/qmd-main/src/mcp/server.ts:433
```

## Retrieval Modes

CLI modes:

```text
qmd search   = BM25 full-text search
qmd vsearch  = vector semantic search
qmd query    = hybrid search with query expansion and reranking
qmd get      = single document by path or docid
qmd multi-get = batch document retrieval by glob or comma-separated list
```

Source pointers:

```text
references/git_search/qmd-main/README.md:36
references/git_search/qmd-main/README.md:41
references/git_search/qmd-main/README.md:47
references/git_search/qmd-main/README.md:620
references/git_search/qmd-main/README.md:624
references/git_search/qmd-main/src/cli/qmd.ts:3141
references/git_search/qmd-main/src/cli/qmd.ts:3149
references/git_search/qmd-main/src/cli/qmd.ts:3162
```

MCP modes:

```text
query
get
multi_get
status
```

Source pointers:

```text
references/git_search/qmd-main/README.md:76
references/git_search/qmd-main/src/mcp/server.ts:241
references/git_search/qmd-main/src/mcp/server.ts:368
references/git_search/qmd-main/src/mcp/server.ts:433
references/git_search/qmd-main/src/mcp/server.ts:506
```

## Output Surfaces

QMD explicitly supports agent-oriented output formats:

```text
--json
--files
--csv
--md
--xml
default CLI text
```

Source pointers:

```text
references/git_search/qmd-main/README.md:57
references/git_search/qmd-main/README.md:648
references/git_search/qmd-main/src/cli/qmd.ts:1956
references/git_search/qmd-main/src/cli/qmd.ts:1980
references/git_search/qmd-main/src/cli/qmd.ts:1987
references/git_search/qmd-main/src/cli/qmd.ts:1934
references/git_search/qmd-main/src/cli/formatter.ts:97
references/git_search/qmd-main/src/cli/formatter.ts:132
references/git_search/qmd-main/src/cli/formatter.ts:161
references/git_search/qmd-main/src/cli/formatter.ts:171
```

Search JSON output carries:

```text
docid
score
file
line
title
context
body or snippet
optional explain
```

Source pointers:

```text
references/git_search/qmd-main/src/cli/qmd.ts:1967
references/git_search/qmd-main/src/cli/formatter.ts:115
```

Files output carries:

```text
docid, score, qmd path, optional context
```

Source pointers:

```text
references/git_search/qmd-main/README.md:648
references/git_search/qmd-main/src/cli/qmd.ts:1980
references/git_search/qmd-main/src/cli/formatter.ts:159
```

MCP `query` returns:

```text
content text summary
structuredContent.results
```

Each result includes:

```text
docid
file
title
score
context
snippet with line numbers
```

Source pointers:

```text
references/git_search/qmd-main/src/mcp/server.ts:345
references/git_search/qmd-main/src/mcp/server.ts:357
```

MCP `get` and `multi_get` return resource objects:

```text
uri
name
title
mimeType
text
```

Source pointers:

```text
references/git_search/qmd-main/src/mcp/server.ts:414
references/git_search/qmd-main/src/mcp/server.ts:486
```

## Context And Collection Model

QMD lets users define collections and contextual metadata.

Collection config fields include:

```text
path
pattern
ignore
context
update
includeByDefault
```

Source pointers:

```text
references/git_search/qmd-main/src/collections.ts:24
references/git_search/qmd-main/src/collections.ts:48
references/git_search/qmd-main/example-index.yml:1
references/git_search/qmd-main/README.md:28
```

VectorFL read:

```text
QMD context can help retrieval, but should remain retrieval metadata until VectorFL recovery interprets it.
```

## Fit For VectorFL

Strong fit:

```text
read-only evidence pointer return
docid/path-based follow-up retrieval
bounded collection filters
score and min-score filtering
context metadata for retrieval disambiguation
snippet and line-number support
JSON/files/markdown outputs useful for worker packets
MCP structuredContent useful for external carriers
```

Fit reason:

```text
The output surfaces can return evidence pointers without needing QMD to become VectorFL memory.
```

## Contract-Relevant Candidate Fields

A future VectorFL-facing retrieval-output contract can likely require:

```text
source_tool: qmd
delivery_surface: cli_json | cli_files | cli_md | mcp_query | mcp_get | mcp_multi_get | sdk
query_mode: search | vsearch | query | get | multi_get
query_text_or_document
collection_scope
intent
min_score
limit
result_items:
  - docid
  - file_or_uri
  - title
  - score
  - context
  - line
  - snippet
  - body_if_explicit_full_or_get
  - explain_if_requested
not_inspected_scope
raw_trace_boundary
recovery_required
```

This is a candidate contract shape, not a schema.

## Boundary / Watch

```text
QMD output can look highly authoritative because it includes scores, snippets, context, and reranking.
Do not treat score as truth.
Do not treat context metadata as VectorFL interpretation.
Do not treat qmd:// path or docid as memory promotion.
Do not enable automatic storage, schema, MCP, or ingestion from this inspection.
Do not import the repo wholesale.
Do not treat SDK availability as implementation approval.
```

## What Was Not Done

```text
QMD was not installed.
QMD was not run.
No index was created.
No VectorFL corpus was indexed.
No MCP server was started.
No HTTP server was started.
No qmd-main tests were run.
No code was modified.
No storage destination was chosen.
No schema was created.
```

## Return-to-Space Value

Recoverable material:

```text
QMD has concrete output surfaces that can support a future VectorFL retrieval-output contract candidate.
```

Reusable judgment:

```text
The safest first attach path is output-contract design around `--json`, `--files`, MCP `query`, MCP `get`, and MCP `multi_get`, not repo import or runtime integration.
```

Issue / watch:

```text
QMD score/context/snippet metadata must remain raw retrieval trace until Codex/VectorFL recovery interprets it.
```

Future reuse note:

```text
Use this report to draft a VectorFL-facing retrieval-output contract candidate before any qmd installation or indexing trial.
```

`STATUS: QMD_DIRECT_SOURCE_INSPECTION_REPORT_PREPARED`
