# Phase 1.10 Run 02 v0

## Scenario

Generated artifact version lineage comparison.

Command:

`python3 scripts/cli/run_phase1_space_query.py 'Compare generated artifact version lineage between phase1_8 and phase1_9 runtime reports and explain why the before after pair belongs to the same family.' --mode comparison --stem phase1_10_run_02`

## Artifacts

- `runtime/query_packets/phase1_10_run_02_question_packet.json`
- `runtime/exploration_results/phase1_10_run_02_exploration_result.json`
- `runtime/merge_diff_reports/phase1_10_run_02_merge_diff_report.json`
- `runtime/reingress_records/phase1_10_run_02_reingress_record.json`

## Execution

The loop created all four artifacts and selected the same phase1_8 -> phase1_9 run 03 family pair.

## Interpretation

This run confirms that version/phase lineage is treated as pair evidence before diff salience is read. It keeps timestamp or discovery order from becoming the hidden pairing reason.

## Validation

- chosen mode: `diff`
- pair confidence: `strong_pair`
- pairing basis: `shared_run_stem`
- rejected pair candidates recorded: 1
- salient diff units: 8
- comparison fallback: 0
- reingress pairing fields present: PASS
