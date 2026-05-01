# Phase 1.12 Run 01 v0

## Scenario

Old vs old same-family comparison.

Question: compare legacy Phase 1.8 and Phase 1.9 run 03 merge reports and check identity confidence without readiness promotion.

## Artifacts

- `runtime/query_packets/phase1_12_run_01_question_packet.json`
- `runtime/exploration_results/phase1_12_run_01_exploration_result.json`
- `runtime/merge_diff_reports/phase1_12_run_01_merge_diff_report.json`
- `runtime/reingress_records/phase1_12_run_01_reingress_record.json`

## Result

| check | observed |
| --- | --- |
| chosen mode | `diff` |
| identity summary | `strong_identity: 3`, `plausible_identity: 12`, `weak_identity: 0` |
| pair summary | `strong_pair: 3`, `weak_pair: 0`, `shared_family_confirmed: 3` |
| diff summary | `salient_diff: 24`, `comparison_fallback: 0`, `trivial: 0` |
| identity basis | embedded markers, mapping table backfill, sidecar note, path/role, phase/run marker |
| guardrail | identity backfill did not change readiness |

## Interpretation

The old artifacts are no longer treated as path-only identity. They read as `plausible_identity` through the legacy backfill map, while current generated artifacts remain `strong_identity`.

The run shows that old/old same-family comparison can use stronger pair selection without claiming old artifacts had native self-description.

## Validation

- Four-artifact spine preserved: `PASS`.
- Legacy identity reflected in exploration and reingress: `PASS`.
- No bridge admission inflation: `PASS`.

## Stage Closeout

1. Verdict: `PASS`
2. Files created/updated: this report plus four runtime artifacts.
3. What was backfilled: old run-family identity was used through companion map.
4. What remains unresolved: confidence remains plausible, not strong.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended next move: run old/new comparison.
