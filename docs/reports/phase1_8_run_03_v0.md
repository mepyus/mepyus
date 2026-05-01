# Phase 1.8 Run 03 v0

## Scenario

diff-heavy structured case

## Execution

Command:

```bash
python3 scripts/cli/run_phase1_space_query.py 'Compare structured evidence summaries across exploration, merge, and reingress contracts and preserve salient path diff.' --mode comparison --stem phase1_8_run_03
```

Artifacts:

- `runtime/query_packets/phase1_8_run_03_question_packet.json`
- `runtime/exploration_results/phase1_8_run_03_exploration_result.json`
- `runtime/merge_diff_reports/phase1_8_run_03_merge_diff_report.json`
- `runtime/reingress_records/phase1_8_run_03_reingress_record.json`

## Interpretation

The run remains `diff` because the question is comparative. Structured evidence now carries salient JSON paths into the diff report, so the diff is not based only on prose or contract identity.

## Validation

- chosen_mode: `diff`
- salient_path evidence: 18
- salient_paths in merge report: present
- identity_only: 0
- shape_only: 0

Verdict: `PASS`
