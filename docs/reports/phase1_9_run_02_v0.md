# Phase 1.9 Run 02 v0

## Scenario

generated artifact version shift

## Execution

Command:

```bash
python3 scripts/cli/run_phase1_space_query.py 'Compare generated artifact version shift from phase1_7 to phase1_8 and explain salient delta paths.' --mode comparison --stem phase1_9_run_02
```

Artifacts:

- `runtime/query_packets/phase1_9_run_02_question_packet.json`
- `runtime/exploration_results/phase1_9_run_02_exploration_result.json`
- `runtime/merge_diff_reports/phase1_9_run_02_merge_diff_report.json`
- `runtime/reingress_records/phase1_9_run_02_reingress_record.json`

## Interpretation

The run demonstrates version-shift reading across generated reports. The comparison does not stop at shape; it records changed fields such as evidence-depth and structured evidence summary.

## Validation

- chosen_mode: `diff`
- salient_diff: 16
- added paths: 11
- evidence_depth_change paths: 3
- trivial_diff: 0

Verdict: `PASS`
