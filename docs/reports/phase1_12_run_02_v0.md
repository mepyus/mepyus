# Phase 1.12 Run 02 v0

## Scenario

Old vs new same-family comparison.

Question: compare Phase 1.10 pairing-era run 03 merge report with Phase 1.11 identity-era run 03 merge report and verify legacy backfill identity is read.

## Artifacts

- `runtime/query_packets/phase1_12_run_02_question_packet.json`
- `runtime/exploration_results/phase1_12_run_02_exploration_result.json`
- `runtime/merge_diff_reports/phase1_12_run_02_merge_diff_report.json`
- `runtime/reingress_records/phase1_12_run_02_reingress_record.json`

## Result

| check | observed |
| --- | --- |
| chosen mode | `diff` |
| identity summary | `strong_identity: 3`, `plausible_identity: 12`, `weak_identity: 0` |
| pair summary | `strong_pair: 3`, `shared_family_confirmed: 3` |
| useful identity modes | `mapping_table_family_backfill`, `generated_from_chain`, `path_plus_role`, `phase_run_marker` |
| merge identity risk | identity anchors present and usable |
| guardrail | old artifact identity stayed `plausible_identity` |

## Interpretation

The mixed comparison is more honest than Phase 1.11 alone: the new artifact can self-describe, while the old artifact receives only a companion identity. Pairing can still confirm same-family context, but the confidence distinction remains visible.

## Validation

- Old/new comparison works: `PASS`.
- Legacy confidence ceiling preserved: `PASS`.
- No readiness promotion: `PASS`.

## Stage Closeout

1. Verdict: `PASS`
2. Files created/updated: this report plus four runtime artifacts.
3. What was backfilled: Phase 1.10 legacy run artifact identity used in comparison.
4. What remains unresolved: broad old run families remain unmapped.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended next move: test ambiguous lower comparison artifacts.
