# Phase 1.9 Run 03 v0

## Scenario

diff-heavy structured case

## Execution

Command:

```bash
python3 scripts/cli/run_phase1_space_query.py 'Diff structured evidence summaries and preserve before after evidence for changed validation and quality paths.' --mode comparison --stem phase1_9_run_03
```

Artifacts:

- `runtime/query_packets/phase1_9_run_03_question_packet.json`
- `runtime/exploration_results/phase1_9_run_03_exploration_result.json`
- `runtime/merge_diff_reports/phase1_9_run_03_merge_diff_report.json`
- `runtime/reingress_records/phase1_9_run_03_reingress_record.json`

## Interpretation

This run checks whether diff evidence affects a structured comparison. The merge report includes `salient_diff_paths`, `strongest_diff_support_refs`, and `comparison_risk_note`.

## Validation

- chosen_mode: `diff`
- salient_diff: 8
- evidence_depth_change: 3
- comparison_risk_note: salient changed paths found
- before/after excerpts: present

Verdict: `PASS`
