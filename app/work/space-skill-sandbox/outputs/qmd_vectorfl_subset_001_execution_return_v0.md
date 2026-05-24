# QMD VectorFL Subset 001 Execution Return v0

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
verdict: PASS_AS_BOUNDED_VECTORFL_SUBSET_RETRIEVAL_RETURN_WITH_WATCH
```

## Purpose

Test QMD against a tiny real VectorFL subset, while preserving the operating rule that retrieval output is evidence-pointer material, not VectorFL memory or authority.

## Activated Anchor Packet

```text
app/work/space-skill-sandbox/outputs/qmd_vectorfl_subset_001_anchor_packet_v0.md
```

## Bounded Subset

Subset directory:

```text
app/work/space-skill-sandbox/tmp/qmd_vectorfl_subset_001
```

Subset files:

```text
next_chat_reentry_summary_after_space_aware_external_execution_loop_v0.md
qmd_vectorfl_retrieval_output_contract_candidate_v0.md
qmd_isolated_fixture_trial_codex_recovery_v0.md
movement_record_qmd_get_multi_get_surface_observation_v0.md
run_248_qmd_get_multi_get_surface_observation.md
movement_record_template_v0.md
```

## Runtime Boundary

Execution route:

```text
npx with explicit temporary npm cache
XDG_CACHE_HOME=/private/tmp/vectorfl-qmd-subset001-xdg-cache
QMD_CONFIG_DIR=/private/tmp/vectorfl-qmd-subset001-config
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
env XDG_CACHE_HOME=/private/tmp/vectorfl-qmd-subset001-xdg-cache QMD_CONFIG_DIR=/private/tmp/vectorfl-qmd-subset001-config npx --cache /private/tmp/vectorfl-qmd-npm-cache @tobilu/qmd collection add app/work/space-skill-sandbox/tmp/qmd_vectorfl_subset_001 --name vectorfl_subset001
```

Result:

```text
Indexed: 6 new, 0 updated, 0 unchanged, 0 removed
Collection 'vectorfl_subset001' created successfully
```

Search:

```text
env XDG_CACHE_HOME=/private/tmp/vectorfl-qmd-subset001-xdg-cache QMD_CONFIG_DIR=/private/tmp/vectorfl-qmd-subset001-config npx --cache /private/tmp/vectorfl-qmd-npm-cache @tobilu/qmd search "Plan from Space Return-to-Space Movement Record" --json -n 5 -c vectorfl_subset001
```

First multi-get attempt:

```text
qmd multi-get "*movement-record*.md,*next-chat*.md" --json --max-bytes 20000
```

Result:

```text
No files matched pattern
```

Correction:

```text
qmd ls vectorfl_subset001
```

Then multi-get by exact qmd URI list:

```text
qmd multi-get "qmd://vectorfl_subset001/movement-record-qmd-get-multi-get-surface-observation-v0.md,qmd://vectorfl_subset001/next-chat-reentry-summary-after-space-aware-external-execution-loop-v0.md" --json --max-bytes 20000
```

Status:

```text
qmd status
```

Status summary:

```text
Index: /private/tmp/vectorfl-qmd-subset001-xdg-cache/qmd/index.sqlite
Documents: 6 files indexed
Vectors: 0 embedded
Pending: 6 need embedding
Collection: vectorfl_subset001
```

## Raw Search JSON

```json
[
  {
    "docid": "#76eba9",
    "score": 0,
    "file": "qmd://vectorfl_subset001/next-chat-reentry-summary-after-space-aware-external-execution-loop-v0.md",
    "title": "Next Chat Re-entry Summary After Space-Aware External Execution Loop v0",
    "snippet": "@@ -235,4 @@ (234 before, 95 after)\n7. Codex recovers and downshifts\n8. VectorFL matures from Return-to-Space Value / Movement Record\n9. User judges direction\n```"
  },
  {
    "docid": "#8f2a66",
    "score": 0,
    "file": "qmd://vectorfl_subset001/movement-record-template-v0.md",
    "title": "Movement Record Template v0",
    "snippet": "@@ -82,4 @@ (81 before, 2 after)\n\nThis template extends the spirit of `docs/reports/space_feedback_loop_return_to_space_record_minimum_v0.md` for external-tool movement.\n\nKeep it lighter than a package sidecar. If it becomes heavy, preserve pointers and compress the judgment."
  },
  {
    "docid": "#9b333a",
    "score": 0,
    "file": "qmd://vectorfl_subset001/movement-record-qmd-get-multi-get-surface-observation-v0.md",
    "title": "Movement Record - QMD Get / Multi-Get Surface Observation v0",
    "snippet": "@@ -27,4 @@ (26 before, 137 after)\n```text\nPlan from Space / Feature-Level External Retrieval Attachability\n```\n"
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
query_text_or_document: Plan from Space Return-to-Space Movement Record
intent: find candidate evidence pointers for the current space-aware external execution loop
collection_scope: vectorfl_subset001
limit: 5
min_score: not_set
rerank_used: false
explain_requested: false
result_count: 3
raw_trace_boundary: true
recovery_required: true
```

Result items:

```text
1.
  docid: #76eba9
  file_or_uri: qmd://vectorfl_subset001/next-chat-reentry-summary-after-space-aware-external-execution-loop-v0.md
  title: Next Chat Re-entry Summary After Space-Aware External Execution Loop v0
  score: 0
  snippet: VectorFL matures from Return-to-Space Value / Movement Record

2.
  docid: #8f2a66
  file_or_uri: qmd://vectorfl_subset001/movement-record-template-v0.md
  title: Movement Record Template v0
  score: 0
  snippet: template extends return-to-space record minimum; keep it lighter than a package sidecar

3.
  docid: #9b333a
  file_or_uri: qmd://vectorfl_subset001/movement-record-qmd-get-multi-get-surface-observation-v0.md
  title: Movement Record - QMD Get / Multi-Get Surface Observation v0
  score: 0
  snippet: Plan from Space / Feature-Level External Retrieval Attachability
```

## Multi-Get Body Bundle Observation

Exact qmd URI list returned JSON body bundle for:

```text
qmd://vectorfl_subset001/movement-record-qmd-get-multi-get-surface-observation-v0.md
qmd://vectorfl_subset001/next-chat-reentry-summary-after-space-aware-external-execution-loop-v0.md
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
VectorFL source references outside subset
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
subset_copy_context_loss_watch
multi_get_glob_pattern_mismatch_watch
qmd_uri_exact_list_more_reliable_watch
body_bundle_memory_promotion_watch
subset_success_overclaim_watch
```

## Execution Verdict

```text
PASS_AS_BOUNDED_VECTORFL_SUBSET_RETRIEVAL_RETURN_WITH_WATCH
```

Meaning:

```text
QMD can retrieve candidate evidence pointers and bounded body bundles from a tiny real VectorFL subset under temporary isolated runtime paths.
```

Limit:

```text
This is not full-corpus integration, not MCP integration, not schema creation, and not memory promotion.
```

`STATUS: QMD_VECTORFL_SUBSET_001_EXECUTION_RETURN_PREPARED`
