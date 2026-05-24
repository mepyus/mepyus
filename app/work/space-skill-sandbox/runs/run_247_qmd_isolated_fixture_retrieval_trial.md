# Run 247 - QMD Isolated Fixture Retrieval Trial

## Status

```yaml
status: closed
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
qmd_collection_add_executed: true
qmd_search_json_executed: true
qmd_status_executed: true
qmd_embed_executed: false
qmd_mcp_executed: false
verdict: PASS_WITH_WATCH_AS_FIRST_REAL_QMD_RETRIEVAL_RETURN
```

## Purpose

Test whether a real external retrieval carrier can read a bounded fixture, return candidate evidence pointers, and be recovered back into VectorFL space without becoming authority.

## Space Basis

```text
Plan from Space, not from Model Default.
```

Activated anchors:

```text
qmd_runtime_preflight_package_v0
qmd_runtime_availability_smoke_return_v0
qmd_vectorfl_retrieval_output_contract_candidate_v0
qmd_direct_source_inspection_report_v0
```

## Work Performed

1. Created a tiny three-file fixture under `app/work/space-skill-sandbox/tmp/qmd_fixture_001`.
2. Ran QMD collection add with temporary npm cache, XDG cache, and QMD config paths.
3. Ran QMD `search --json` against only `fixture001`.
4. Ran QMD `status` to confirm the isolated index path and no embedded vectors.
5. Wrapped the output as a retrieval return card.
6. Recovered the result through Codex into candidate pointers, held metadata, watch items, and Return-to-Space Value.
7. Wrote a Movement Record.

## Created Files

```text
app/work/space-skill-sandbox/tmp/qmd_fixture_001/anchor_loop_note.md
app/work/space-skill-sandbox/tmp/qmd_fixture_001/lacl_layer_note.md
app/work/space-skill-sandbox/tmp/qmd_fixture_001/qmd_boundary_note.md
app/work/space-skill-sandbox/outputs/qmd_isolated_fixture_trial_execution_return_v0.md
app/work/space-skill-sandbox/outputs/qmd_isolated_fixture_trial_codex_recovery_v0.md
app/work/space-skill-sandbox/outputs/movement_record_qmd_isolated_fixture_trial_v0.md
app/work/space-skill-sandbox/runs/run_247_qmd_isolated_fixture_retrieval_trial.md
```

## Verdict

```text
PASS_WITH_WATCH_AS_FIRST_REAL_QMD_RETRIEVAL_RETURN
```

Meaning:

```text
QMD successfully returned CLI JSON evidence pointers from an isolated fixture.
Codex recovered the result without treating it as VectorFL memory, baseline, schema, or authority.
```

## Return-to-Space Value

```text
The first real external retrieval carrier loop succeeded at the evidence-pointer layer:
space anchor -> isolated QMD execution -> JSON return -> Codex recovery -> Movement Record.
```

## Watch Items

```text
score_zero_but_semantically_matched_watch
metadata_authority_watch
fixture_success_overclaim_watch
qmd_uri_filename_normalization_watch
temporary_index_cleanup_watch
```

## Next Re-Entry

```text
Test qmd get / multi-get on the same fixture before considering any VectorFL subset.
```

`STATUS: RUN_247_QMD_ISOLATED_FIXTURE_RETRIEVAL_TRIAL_CLOSED`
