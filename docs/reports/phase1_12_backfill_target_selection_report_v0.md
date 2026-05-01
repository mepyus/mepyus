# Phase 1.12 Backfill Target Selection Report v0

## Verdict

`PASS_WITH_NOTE`

Four legacy families are selected for bounded identity backfill. Broad archive and promotion-sensitive report families are intentionally excluded.

## Selected Families

| chosen family | chosen reason | backfill mode | expected confidence ceiling | why not broader | risk note |
| --- | --- | --- | --- | --- | --- |
| `runtime_contract_v_series` | contracts are frequently compared across v0-v5 and are JSON-readable | `mapping_table_family_backfill` | `plausible_identity` | only Phase 1 space/exploration/merge/reingress contracts are targeted, not every runtime contract | contract identity must not become baseline lock |
| `phase1_5_to_1_10_runtime_run_artifacts` | old four-artifact runs are compared with Phase 1.11 new identity artifacts | `mapping_table_family_backfill` | `plausible_identity` | only representative high-use old run artifacts are mapped first | backfill must not imply old artifacts were emitted with self-identity |
| `external_preprocess_comparison_artifacts` | lower bridge depends on these gate/checkpoint artifacts | `sidecar_identity_note` plus `mapping_table_family_backfill` | `plausible_identity` | only three current transcript comparison JSONs are targeted | packet-candidate admission still requires bridge checklist |
| `observer_raw_intake_generated_bundle` | bridge examples and lower rediscovery repeatedly cite source/split/trace/GMD raw-intake artifacts | `mapping_table_family_backfill` | `plausible_identity` | only raw-intake gap analysis family is mapped; broad observer archive is held | source/split artifacts remain evidence-ready, not packet-candidate |

## Excluded For Now

| excluded family | reason |
| --- | --- |
| broad observer generated archive | too large and uneven for bounded backfill |
| line/axis/camera review reports | promotion-sensitive; identity could be confused with readiness |
| receipts and event ledgers | residue-only; bridge says reject for upper |
| all runtime contracts outside Phase 1 spine | useful later, but not central to Phase 1.12 old/new mixed comparison |

## Interpretation

This scope is bounded because it targets the small set of legacy families that current runs actually touch. The selected families improve old/new comparison without requiring a repository-wide migration.

Excluded families can wait because they either have lower operational value for the current CLI spine or carry higher admission-inflation risk.

## Validation

- Scope is 4 family groups, not repository-wide: `PASS`.
- High-use comparison and bridge families are prioritized: `PASS`.
- Promotion-sensitive material is held: `PASS`.
- Bridge minimum remains intact: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created/updated: `docs/reports/phase1_12_backfill_target_selection_report_v0.md`
3. What was backfilled: not yet; targets selected.
4. What remains unresolved: execute companion map and helper binding.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended next move: create companion legacy identity map and execution report.
