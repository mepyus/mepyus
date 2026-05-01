# Phase 1.10 Run 05 v0

## Scenario

Mixed prose + structured comparison case.

Command:

`python3 scripts/cli/run_phase1_space_query.py 'Mix prose and structured comparison evidence while preserving reusable family groups and pairing risk in reingress.' --mode merge --stem phase1_10_run_05`

## Artifacts

- `runtime/query_packets/phase1_10_run_05_question_packet.json`
- `runtime/exploration_results/phase1_10_run_05_exploration_result.json`
- `runtime/merge_diff_reports/phase1_10_run_05_merge_diff_report.json`
- `runtime/reingress_records/phase1_10_run_05_reingress_record.json`

## Execution

The loop created all four artifacts. It selected the phase1_8 -> phase1_9 run 03 family pair and kept reusable family groups in reingress.

## Interpretation

This run checks that pairing metadata is not only useful in explicit diff mode. Even a merge-mode return can preserve family keys, rejected candidates, and pairing risk for later comparison questions.

## Validation

- chosen mode: `merge`
- pair confidence: `strong_pair`
- pairing basis: `shared_run_stem`
- rejected pair candidates recorded: 1
- salient diff units: 8
- reingress reusable family groups present: PASS
