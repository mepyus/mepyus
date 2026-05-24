# QMD Dry Output Contract Trial Sample Return v0

## Status

```yaml
status: synthetic_sample_return
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
runtime_qmd_executed: false
qmd_installed: false
vectorfl_indexed: false
purpose: dry_contract_shape_test
```

## Boundary

This is not actual QMD output.

It is a synthetic sample shaped from:

```text
app/work/space-skill-sandbox/outputs/qmd_vectorfl_retrieval_output_contract_candidate_v0.md
app/work/space-skill-sandbox/outputs/qmd_direct_source_inspection_report_v0.md
```

Use it only to test whether Codex recovery can keep QMD-like retrieval metadata as raw trace.

## QMD_RETRIEVAL_RETURN_CARD

```yaml
source_tool: qmd
delivery_surface: cli_json
qmd_command_or_tool: qmd query --json --explain -n 3 --min-score 0.35
query_mode: query
query_text_or_document: "VectorFL external execution anchor request return-to-space movement record"
intent: "Find candidate internal evidence pointers about space-aware external execution loops, anchor packets, and Movement Record closeout."
collection_scope:
  - vectorfl_docs
limit: 3
min_score: 0.35
rerank_used: true
explain_requested: true
result_count: 3
raw_trace_boundary: true
recovery_required: true
```

## Result Items

### Item 1

```yaml
docid: "#a1b2c3"
file_or_uri: "qmd://vectorfl_docs/app/work/space-skill-sandbox/outputs/space_aware_external_execution_loop_two_test_candidate_operating_note_v0.md"
title: "Space-Aware External Execution Loop Two-Test Candidate Operating Note v0"
score: 0.91
context: "candidate operating notes for external execution loop testing"
line: 31
snippet: |
  31: User Purpose
  32: -> External Tool Interpretation
  33: -> Anchor Request
  34: -> Codex Anchor Packet
  35: -> External Execution
explain:
  retrieval_note: "High lexical and semantic match to Anchor Request / Anchor Packet loop."
```

### Item 2

```yaml
docid: "#d4e5f6"
file_or_uri: "qmd://vectorfl_docs/app/work/space-skill-sandbox/outputs/movement_record_space_loop_test_002_qmd_attachability_v0.md"
title: "Movement Record - Space Loop Test 002 QMD Attachability v0"
score: 0.84
context: "movement records for retrieval-side attachability tests"
line: 133
snippet: |
  133: A candidate non-implementation QMD-like attachability trial:
  134: ask retrieval sidecar to return bounded evidence pointers/snippets as raw trace,
  135: then test whether VectorFL retains interpretation, judgment, and memory recovery.
explain:
  retrieval_note: "Relevant to QMD-like raw trace boundary and recovery."
```

### Item 3

```yaml
docid: "#9f8e7d"
file_or_uri: "qmd://vectorfl_docs/docs/specs/movement_record_template_v0.md"
title: "Movement Record Template v0"
score: 0.62
context: "template candidates for movement records"
line: 12
snippet: |
  12: Movement Record is a lightweight markdown record.
  13: It is not a database schema and not an automatic writer target.
explain:
  retrieval_note: "Relevant as return shape guard, but not specific to QMD."
```

## Not Inspected Scope

```text
No actual QMD command was run.
No actual QMD index was queried.
No actual score, docid, line, snippet, or explain trace was produced by QMD.
No VectorFL corpus was indexed.
No file existence under qmd:// was verified by QMD.
```

## Watch Items

```text
synthetic_trace_confusion_watch
score_authority_watch
context_metadata_authority_watch
qmd_uri_memory_promotion_watch
snippet_truth_watch
```

`STATUS: QMD_DRY_OUTPUT_CONTRACT_TRIAL_SAMPLE_RETURN_PREPARED`
