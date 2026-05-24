# QMD VectorFL Retrieval Output Contract Candidate v0

## Status

```yaml
status: contract_candidate
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
implementation: false
source_basis: qmd_direct_source_inspection
```

## Purpose

Define the minimum candidate output shape for receiving QMD-like retrieval results into VectorFL without treating them as memory, truth, or implementation authority.

This is a candidate contract note, not a parser schema or ingestion automation.

## Supported Delivery Surfaces

Candidate delivery surfaces from direct source inspection:

```text
cli_json
cli_files
cli_md
cli_csv
cli_xml
mcp_query
mcp_get
mcp_multi_get
sdk_search
sdk_get
sdk_multi_get
```

Preferred first surfaces:

```text
cli_json
cli_files
mcp_query
mcp_get
mcp_multi_get
```

Reason:

```text
They return structured or compact evidence pointers suitable for agent/space recovery.
```

## Minimum Retrieval Return Card

Each QMD retrieval run should be wrapped before entering VectorFL:

```text
QMD_RETRIEVAL_RETURN_CARD

source_tool:
delivery_surface:
qmd_command_or_tool:
query_mode:
query_text_or_document:
intent:
collection_scope:
limit:
min_score:
rerank_used:
explain_requested:
result_count:
result_items:
not_inspected_scope:
raw_trace_boundary: true
recovery_required: true
watch_items:
```

## Result Item Candidate Fields

For search-like results:

```text
docid:
file_or_uri:
title:
score:
context:
line:
snippet:
explain:
```

For get-like results:

```text
file_or_uri:
title:
context:
from_line:
max_lines:
line_numbers:
body_or_text:
```

For multi-get-like results:

```text
file_or_uri:
title:
context:
skipped:
skip_reason:
body_or_text:
```

## VectorFL Recovery Rule

QMD output may enter VectorFL only as:

```text
raw retrieval trace
evidence pointer
candidate source bundle
watch item
future bounded-read target
```

QMD output may not enter as:

```text
VectorFL memory by itself
truth
baseline
current-position update
source-of-truth replacement
lower input organ replacement
integrated-engine replacement
automatic memory promotion
storage writer
schema
registry
```

## Required Codex Packaging

Codex recovery should produce:

```text
source trace
query / command trace
result summary
evidence pointers accepted
evidence pointers held
not-inspected scope
metadata caution
Return-to-Space Value
Movement Record if reusable judgment exists
```

## Metadata Caution

Treat the following as retrieval metadata, not interpreted VectorFL judgment:

```text
score
context
title
snippet
line
docid
qmd:// uri
explain trace
rerank result
collection name
```

## First Trial Candidate

A safe non-implementation trial can ask QMD-like retrieval to answer:

```text
Find 3-5 candidate evidence pointers for a bounded VectorFL question.
Return docid, qmd path, title, score, context, line, snippet.
Do not summarize as truth.
Do not decide promotion.
Do not write memory.
```

Expected Codex recovery:

```text
which pointers are useful
which pointers are thin or mismatched
what should be read next
what watch items appeared
what Return-to-Space Value exists
```

## Stop Conditions

Return HOLD if:

```text
QMD needs installation or model download
indexing VectorFL corpus is required
MCP server setup is required
storage destination must be chosen
schema/parser/automation is needed
retrieval output claims final judgment
score is being treated as truth
```

## Do Not

```text
do not implement
do not install
do not index
do not start MCP
do not create storage/schema/registry
do not promote this contract candidate
do not update current position
```

`STATUS: QMD_VECTORFL_RETRIEVAL_OUTPUT_CONTRACT_CANDIDATE_PREPARED`
