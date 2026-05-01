# Legacy Identity Backfill Examples v0

## Purpose

This guide gives concrete examples for applying `legacy_artifact_identity_backfill_contract_v0.md` without rewriting the old archive.

## Examples

| artifact family | example path | recommended mode | confidence ceiling | reason |
| --- | --- | --- | --- | --- |
| runtime contract v-series | `runtime/contracts/merge_diff_report_v0.json` | `mapping_table_family_backfill` | `plausible_identity` | contract role and version family are clear from path, but identity is not embedded |
| old runtime run artifact | `runtime/merge_diff_reports/phase1_8_run_03_merge_diff_report.json` | `mapping_table_family_backfill` | `plausible_identity` | phase/run/role are clear and used in old/new comparison |
| new runtime run artifact | `runtime/merge_diff_reports/phase1_11_run_03_merge_diff_report.json` | no legacy backfill; use embedded identity | `strong_identity` when emitted inline | current artifact already self-describes |
| external preprocess comparison | `app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json` | `sidecar_identity_note` plus map entry | `plausible_identity` | lower gate/checkpoint artifact can seed upper only after bridge checklist |
| observer raw-intake source manifest | `app/work/observer_ingest_min/generated/source_manifest_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json` | `mapping_table_family_backfill` | `plausible_identity` | family and role are clear, but readiness remains evidence-only |
| line/axis promotion report | `app/work/observer_ingest_min/generated/operator_summary_line_thickening_promotion_scope_v0_20260402_192503.md` | `do_not_backfill_yet` | `weak_identity` | promotion-sensitive; identity could be misread as admission readiness |

## Operator Rule

When in doubt, choose the lower confidence and lower admission. A sidecar identity note can improve comparison honesty while still keeping the artifact at `evidence_only` or `ingest_ready`.

## Validation

- Examples cover inline, sidecar, mapping table, and hold modes: `PASS`.
- Readiness inflation is explicitly blocked: `PASS`.
