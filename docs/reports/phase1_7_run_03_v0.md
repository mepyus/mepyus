# Phase 1.7 Run 03 v0

## Scenario

diff-heavy excerpt quality comparison

## Execution

Command:

```bash
python3 scripts/cli/run_phase1_space_query.py 'Compare poor excerpts with usable excerpts and preserve the quality diff in merge risk.' --mode comparison --stem phase1_7_run_03
```

Artifacts:

- `runtime/query_packets/phase1_7_run_03_question_packet.json`
- `runtime/exploration_results/phase1_7_run_03_exploration_result.json`
- `runtime/merge_diff_reports/phase1_7_run_03_merge_diff_report.json`
- `runtime/reingress_records/phase1_7_run_03_reingress_record.json`

## Interpretation

The run keeps comparison mode as `diff` while carrying excerpt quality into the merge report. This is the desired behavior: quality tuning improves evidence readability without forcing merge.

## Validation

- chosen_mode: `diff`
- title_only / metadata_only issues: 0
- poor excerpts: 0
- usable excerpts: 3
- strong excerpts: 3
- merge report includes `excerpt_quality_summary`

Verdict: `PASS`
