# Phase 1.8 Run 01 v0

## Scenario

runtime contract reading

## Execution

Command:

```bash
python3 scripts/cli/run_phase1_space_query.py 'Read the runtime contract fields for exploration result v2 and identify salient JSON paths, not just contract identity.' --mode verification --stem phase1_8_run_01
```

Artifacts:

- `runtime/query_packets/phase1_8_run_01_question_packet.json`
- `runtime/exploration_results/phase1_8_run_01_exploration_result.json`
- `runtime/merge_diff_reports/phase1_8_run_01_merge_diff_report.json`
- `runtime/reingress_records/phase1_8_run_01_reingress_record.json`

## Interpretation

The run selected runtime contract JSON and extracted path-level structured evidence such as evidence depth and grounding paths. This moves beyond top-level contract identity.

## Validation

- chosen_mode: `merge`
- structured contract: `space_exploration_result_v2`
- salient_path evidence: 18
- identity_only: 0
- shape_only: 0
- salient paths carried into merge/reingress: yes

Verdict: `PASS`
