# QMD Dry Output Contract Trial Codex Recovery v0

## Status

```yaml
status: dry_contract_recovery
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
runtime_qmd_executed: false
verdict: PASS_WITH_WATCH_AS_DRY_OUTPUT_CONTRACT_TRIAL
```

## Source Trace

Synthetic sample:

```text
app/work/space-skill-sandbox/outputs/qmd_dry_output_contract_trial_sample_return_v0.md
```

Contract candidate:

```text
app/work/space-skill-sandbox/outputs/qmd_vectorfl_retrieval_output_contract_candidate_v0.md
```

Source inspection:

```text
app/work/space-skill-sandbox/outputs/qmd_direct_source_inspection_report_v0.md
```

## Trial Purpose

Test whether a QMD-like retrieval return can be received as raw trace and recovered without:

```text
treating scores as truth
treating context metadata as VectorFL interpretation
treating qmd:// URI or docid as memory promotion
creating schema/parser/automation
approving QMD installation or indexing
```

## Contract Shape Check

| field / rule | pass / watch | note |
| --- | --- | --- |
| source tool stated | pass | `source_tool: qmd` |
| delivery surface stated | pass | `cli_json` |
| command/tool trace stated | pass | command-like string provided, marked synthetic |
| query mode stated | pass | `query` |
| intent stated | pass | disambiguation intent included |
| collection scope stated | pass_with_watch | synthetic collection only |
| limit/min_score stated | pass | values present |
| rerank/explain flags stated | pass | values present |
| result_count stated | pass | 3 |
| result item fields present | pass | docid, uri, title, score, context, line, snippet, explain |
| not-inspected scope present | pass | explicit no-runtime boundary |
| raw_trace_boundary present | pass | true |
| recovery_required present | pass | true |
| watch items present | pass | synthetic/metadata authority watches included |

## Codex Recovery

### Evidence Pointers Accepted

Accepted only as candidate pointers:

```text
qmd://vectorfl_docs/app/work/space-skill-sandbox/outputs/space_aware_external_execution_loop_two_test_candidate_operating_note_v0.md
qmd://vectorfl_docs/app/work/space-skill-sandbox/outputs/movement_record_space_loop_test_002_qmd_attachability_v0.md
qmd://vectorfl_docs/docs/specs/movement_record_template_v0.md
```

Acceptance meaning:

```text
These are plausible follow-up read targets for a future real retrieval test.
They are not confirmed QMD results.
They are not memory promotion.
```

### Evidence Pointers Held

Held as synthetic:

```text
docid values
score values
line values
explain traces
collection name
```

Reason:

```text
They were fabricated for contract-shape testing and cannot support evidence claims.
```

## Metadata Caution

The dry trial confirms the need for an explicit metadata caution layer.

Treat as retrieval metadata only:

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

Codex interpretation must happen after retrieval, not inside retrieval output.

## What The Dry Trial Validated

```text
The candidate QMD return card is sufficient for Codex to separate raw trace from recoverable material.
The contract shape carries enough fields for source trace, result summary, metadata caution, and Movement Record recovery.
The dry sample exposes the main risk: retrieval metadata looks like evidence unless explicitly downshifted.
```

## What The Dry Trial Did Not Validate

```text
actual QMD command behavior
actual qmd:// URI resolution
actual score quality
actual line/snippet accuracy
actual VectorFL indexing
MCP transport
SDK behavior
runtime cost
installation feasibility
```

## Return-to-Space Value

Recoverable material:

```text
The QMD retrieval return card shape is usable for dry Codex recovery.
```

Reusable judgment:

```text
A QMD-like retrieval sidecar should return a card, not a conclusion.
Codex should then classify candidate pointers, held metadata, not-inspected scope, and watch items.
```

Issue / watch:

```text
Synthetic or real retrieval metadata can be mistaken for verified evidence.
The contract should always force not-inspected scope and recovery_required.
```

Future reuse note:

```text
Before runtime testing, reuse this dry recovery shape as the expected packaging target for a real QMD output.
```

## Packaging Decision

```text
PASS_WITH_WATCH_AS_DRY_OUTPUT_CONTRACT_TRIAL
```

## Do Not

```text
do not promote to baseline
do not create parser/schema
do not create automation
do not treat synthetic values as evidence
do not approve QMD installation
do not approve VectorFL indexing
do not update current position
```

`STATUS: QMD_DRY_OUTPUT_CONTRACT_TRIAL_CODEX_RECOVERY_COMPLETE`
