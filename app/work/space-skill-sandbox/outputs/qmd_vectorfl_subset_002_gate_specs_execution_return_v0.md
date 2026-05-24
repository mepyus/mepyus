# QMD VectorFL Subset 002 Gate Specs Execution Return v0

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
qmd_multi_get_json_executed: true
qmd_status_executed: true
qmd_embed_executed: false
qmd_mcp_executed: false
verdict: PASS_AS_GATE_SPECS_SUBSET_RETRIEVAL_RETURN_WITH_WATCH
```

## Purpose

Run QMD against a second tiny VectorFL subset from the Task-Mode Gate Specs / Core Operating Anchors material family.

## Activated Anchor Packet

```text
app/work/space-skill-sandbox/outputs/qmd_vectorfl_subset_002_gate_specs_anchor_packet_v0.md
```

## Bounded Subset

Subset directory:

```text
app/work/space-skill-sandbox/tmp/qmd_vectorfl_subset_002_gate_specs
```

Subset files:

```text
anchor_stack_plan_mode_gate_sequence_v0.md
anchor_stack_gate_checklist_v0.md
small_anchor_generation_rule_v0.md
plan_basis_template_v0.md
external_tool_plan_prompt_wrapper_v0.md
external_tool_plan_return_review_template_v0.md
```

## Runtime Boundary

Execution route:

```text
npx with explicit temporary npm cache
XDG_CACHE_HOME=/private/tmp/vectorfl-qmd-subset002-xdg-cache
QMD_CONFIG_DIR=/private/tmp/vectorfl-qmd-subset002-config
```

Stop boundaries preserved:

```text
no VectorFL full corpus indexing
no embed
no query/rerank
no vsearch
no MCP
no daemon
no parser/schema/automation
no current-position update
```

## Command Trace

Collection add:

```text
env XDG_CACHE_HOME=/private/tmp/vectorfl-qmd-subset002-xdg-cache QMD_CONFIG_DIR=/private/tmp/vectorfl-qmd-subset002-config npx --cache /private/tmp/vectorfl-qmd-npm-cache @tobilu/qmd collection add app/work/space-skill-sandbox/tmp/qmd_vectorfl_subset_002_gate_specs --name vectorfl_subset002_gate_specs
```

Result:

```text
Indexed: 6 new, 0 updated, 0 unchanged, 0 removed
Collection 'vectorfl_subset002_gate_specs' created successfully
```

Search:

```text
env XDG_CACHE_HOME=/private/tmp/vectorfl-qmd-subset002-xdg-cache QMD_CONFIG_DIR=/private/tmp/vectorfl-qmd-subset002-config npx --cache /private/tmp/vectorfl-qmd-npm-cache @tobilu/qmd search "Plan Basis canonical Position IDs Return-to-Space" --json -n 6 -c vectorfl_subset002_gate_specs
```

Multi-get by exact qmd URI list:

```text
env XDG_CACHE_HOME=/private/tmp/vectorfl-qmd-subset002-xdg-cache QMD_CONFIG_DIR=/private/tmp/vectorfl-qmd-subset002-config npx --cache /private/tmp/vectorfl-qmd-npm-cache @tobilu/qmd multi-get "qmd://vectorfl_subset002_gate_specs/external-tool-plan-prompt-wrapper-v0.md,qmd://vectorfl_subset002_gate_specs/anchor-stack-gate-checklist-v0.md" --json --max-bytes 20000
```

Status:

```text
qmd status
```

Status summary:

```text
Index: /private/tmp/vectorfl-qmd-subset002-xdg-cache/qmd/index.sqlite
Documents: 6 files indexed
Vectors: 0 embedded
Pending: 6 need embedding
Collection: vectorfl_subset002_gate_specs
```

## Raw Search JSON

```json
[
  {
    "docid": "#2406f8",
    "score": 0,
    "file": "qmd://vectorfl_subset002_gate_specs/external-tool-plan-prompt-wrapper-v0.md",
    "title": "External Tool Plan Prompt Wrapper v0",
    "snippet": "@@ -64,4 @@ (63 before, 69 after)\n\nUse canonical Position IDs:\n\n```text"
  },
  {
    "docid": "#ca0818",
    "score": 0,
    "file": "qmd://vectorfl_subset002_gate_specs/anchor-stack-gate-checklist-v0.md",
    "title": "Anchor Stack Gate Checklist v0",
    "snippet": "@@ -19,4 @@ (18 before, 91 after)\n- selected route\n- canonical Position IDs\n- current line\n- at least one axis"
  }
]
```

## QMD_RETRIEVAL_RETURN_CARD

```text
source_tool: qmd
delivery_surface: cli_json
runtime_route: npx_temporary_cache_with_temp_xdg_and_config
qmd_command_or_tool: search
query_mode: bm25_full_text
query_text_or_document: Plan Basis canonical Position IDs Return-to-Space
intent: find task-mode gate anchors that change worker planning behavior
collection_scope: vectorfl_subset002_gate_specs
limit: 6
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
  docid: #2406f8
  file_or_uri: qmd://vectorfl_subset002_gate_specs/external-tool-plan-prompt-wrapper-v0.md
  title: External Tool Plan Prompt Wrapper v0
  score: 0
  snippet: Use canonical Position IDs

2.
  docid: #ca0818
  file_or_uri: qmd://vectorfl_subset002_gate_specs/anchor-stack-gate-checklist-v0.md
  title: Anchor Stack Gate Checklist v0
  score: 0
  snippet: selected route / canonical Position IDs / current line / axis
```

## Multi-Get Body Bundle Observation

Exact qmd URI list returned JSON body bundle for:

```text
qmd://vectorfl_subset002_gate_specs/external-tool-plan-prompt-wrapper-v0.md
qmd://vectorfl_subset002_gate_specs/anchor-stack-gate-checklist-v0.md
```

Observed multi-get fields:

```text
file
title
body
```

## Not Inspected

```text
whole VectorFL corpus
larger task-mode gate family
embed/vector search
query/rerank
MCP
SDK
parser/schema/automation
current-position update
```

## Watch Items

```text
score_zero_repeat_watch
score_authority_watch
gate_specs_subset_success_overclaim_watch
body_bundle_memory_promotion_watch
plan_basis_as_baseline_watch
```

## Execution Verdict

```text
PASS_AS_GATE_SPECS_SUBSET_RETRIEVAL_RETURN_WITH_WATCH
```

Meaning:

```text
QMD can retrieve gate-spec evidence pointers from a second bounded VectorFL subset, and exact qmd URI multi-get can recover the body bundle.
```

Limit:

```text
This confirms a bounded evidence-access pattern, not full integration or automation.
```

`STATUS: QMD_VECTORFL_SUBSET_002_GATE_SPECS_EXECUTION_RETURN_PREPARED`
