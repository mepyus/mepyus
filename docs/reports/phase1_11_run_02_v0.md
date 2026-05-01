# Phase 1.11 Run 02 v0

## Scenario

Generated artifact lineage comparison.

Command:

`python3 scripts/cli/run_phase1_space_query.py 'Compare generated artifact lineage with identity anchors between phase1_10 and phase1_11 reports and explain identity basis before pairing.' --mode comparison --stem phase1_11_run_02`

## Artifacts

- `runtime/query_packets/phase1_11_run_02_question_packet.json`
- `runtime/exploration_results/phase1_11_run_02_exploration_result.json`
- `runtime/merge_diff_reports/phase1_11_run_02_merge_diff_report.json`
- `runtime/reingress_records/phase1_11_run_02_reingress_record.json`

## Execution

The run generated v5 artifacts and read prior phase1_10 / phase1_11 comparison candidates.

## Interpretation

This is the lineage stress case. The loop can now distinguish embedded generated chain evidence from path-only inference through `identity_basis`.

## Validation

- chosen mode: `diff`
- artifact self identity: `strong_identity`
- identity basis includes `generated_from_chain`
- pair confidence: `strong_pair`
- identity risk note present and bounded
- reingress identity learning fields present: PASS
