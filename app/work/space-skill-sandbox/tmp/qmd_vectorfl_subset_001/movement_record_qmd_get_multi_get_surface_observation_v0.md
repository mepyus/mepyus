# Movement Record - QMD Get / Multi-Get Surface Observation v0

## Status

```yaml
status: movement_record_candidate
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
qmd_get_executed: true
qmd_multi_get_json_executed: true
qmd_embed_executed: false
qmd_mcp_executed: false
verdict: PASS_WITH_WATCH_AS_BOUNDED_FOLLOW_UP_READ_TRIAL
```

## Input Purpose

Continue from the first QMD search JSON retrieval trial by testing whether returned pointers can support bounded follow-up reads without leaving fixture scope.

## Activated Space Memory / Anchors

Line:

```text
Plan from Space / Feature-Level External Retrieval Attachability
```

Axis:

```text
pointer discovery vs body retrieval
runtime observation vs contract assumption
body bundle vs interpreted memory
```

Material families:

```text
Run Records
Worker Return / Packaging Records
External Material Intake Records
Task-Mode Gate Specs
```

Anchors:

```text
qmd_isolated_fixture_trial_execution_return_v0
qmd_isolated_fixture_trial_codex_recovery_v0
movement_record_qmd_isolated_fixture_trial_v0
qmd_vectorfl_retrieval_output_contract_candidate_v0
```

## External Tool Role

```text
tool: QMD
role: follow-up read surface candidate
execution_surface: CLI get and CLI multi-get JSON
scope: isolated fixture001 only
```

## Tool Output Summary

`qmd get qmd://fixture001/anchor-loop-note.md --json` returned the markdown body, not a JSON object.

`qmd multi-get "*.md" --json` returned a JSON array with:

```text
file
title
body
```

## Anchor Usage Trace

The prior search trial produced pointer candidates.

The follow-up read trial tested whether those pointers can become bounded read targets.

Codex recovery downshifted the original contract expectation instead of forcing observed output into the expected shape.

## Evidence / Not Inspected / Gap

Evidence:

```text
get command returned body text successfully
multi-get command returned JSON body bundle successfully
fixture remained isolated
no embedding or MCP was executed
```

Not inspected:

```text
get output with different flag ordering
get output by docid
line-sliced get output
multi-get by qmd URI glob
multi-get with max lines or max bytes
MCP get/multi_get
SDK get/multiGet
```

Gap:

```text
get JSON support remains unresolved for this runtime route.
```

## User Decision Point

Possible next directions:

```text
stop with fixture-level search + multi-get evidence
test line-sliced get / docid get in fixture
test MCP only after separate approval
test a small VectorFL subset only after explicit scope selection
```

## Return-to-Space Value

Recoverable material:

```text
The safe QMD evidence access pattern is currently search --json for pointers and multi-get --json for bounded body bundles.
```

Reusable judgment:

```text
When runtime output differs from the candidate contract, downshift the contract and preserve the mismatch as a watch item instead of correcting the output by assumption.
```

Issue / watch:

```text
get_json_surface_mismatch_watch
multi_get_body_bundle_surface_candidate
body_bundle_memory_promotion_watch
fixture_scope_only_watch
```

Future reuse note:

```text
Use multi-get --json as the next candidate follow-up read surface before building any parser, automation, or VectorFL subset trial.
```

## Do Not

```text
do not promote to baseline
do not update current position
do not create parser/schema/automation
do not index VectorFL corpus
do not start MCP
do not treat body bundle as interpreted memory
```

`STATUS: MOVEMENT_RECORD_QMD_GET_MULTI_GET_SURFACE_OBSERVATION_PREPARED`
