# Legacy Artifact Family Identity Map v0

## Purpose

This is the human-readable companion to `legacy_artifact_family_identity_map_v0.json`.

The map provides bounded identity anchors for selected legacy artifacts without rewriting those artifacts.

## Guardrail

Identity backfill does not change lower readiness or upper admission.

- `residue-only` remains `reject_for_upper`.
- `evidence-ready` remains `evidence_only`.
- `engine-ingest-ready` remains `ingest_ready`.
- `packet-candidate` remains `packet_candidate` only after checklist pass.

## Backfilled Families

| family | mode | confidence ceiling | notes |
| --- | --- | --- | --- |
| `runtime_contract_v_series` | `mapping_table_family_backfill` | `plausible_identity` | v0-v5 contract lineage can be compared without baseline promotion |
| `phase1_5_to_1_10_runtime_run_artifacts` | `mapping_table_family_backfill` | `plausible_identity` | old run artifacts gain role/family/run hints for old/new comparison |
| `external_preprocess_comparison_artifacts` | `sidecar_identity_note` + map | `plausible_identity` | lower packet-candidate remains checklist-bound |
| `observer_raw_intake_generated_bundle` | `mapping_table_family_backfill` | `plausible_identity` | source/split artifacts remain evidence-only unless paired with stronger support |

## Held Families

- line/axis/camera promotion-sensitive reports;
- broad observer generated archive;
- receipts and event ledgers;
- unrelated runtime contracts not used in the Phase 1.12 runs.

## Validation

- Machine-readable map exists: `docs/indexes/legacy_artifact_family_identity_map_v0.json`.
- Old artifacts are not rewritten.
- Confidence is capped at `plausible_identity`.
