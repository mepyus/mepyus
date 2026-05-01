# Phase 1.12 Legacy Family Candidate Audit Report v0

## Verdict

`PASS_WITH_NOTE`

The highest-value legacy families are not all old artifacts. They are the families repeatedly touched by the current CLI spine: runtime contract versions, pre-identity Phase 1 runtime run artifacts, lower preprocess comparison artifacts, and observer ingest generated bundles. Line/axis/camera review reports are important but too promotion-sensitive for this bounded identity backfill.

## Candidate Family Table

| family name | representative artifact paths | current usage context | why it matters now | current identity quality | backfill suitability | readiness risk |
| --- | --- | --- | --- | --- | --- | --- |
| `runtime_contract_v_series` | `runtime/contracts/space_exploration_result_v0.json`, `runtime/contracts/space_exploration_result_v5.json`, `runtime/contracts/merge_diff_report_v0.json`, `runtime/contracts/space_reingress_record_v5.json` | structured/diff/pairing comparison and contract reading | v0-v5 contracts are compared across phases and act as old/new schema-like references | plausible from path/version; some v5 templates have inline identity but older versions do not | `mapping_table_family_backfill` | low; runtime contracts remain contract artifacts, not packet candidates |
| `phase1_5_to_1_10_runtime_run_artifacts` | `runtime/query_packets/phase1_5_run_01_question_packet.json`, `runtime/exploration_results/phase1_8_run_03_exploration_result.json`, `runtime/merge_diff_reports/phase1_10_run_03_merge_diff_report.json`, `runtime/reingress_records/phase1_9_run_05_reingress_record.json` | four-artifact spine history and old/new mixed comparison | these artifacts are repeatedly compared against Phase 1.11 self-identifying outputs | plausible from path/stem/run markers; weak internal identity before Phase 1.11 | `mapping_table_family_backfill` | medium; identity must not imply readiness promotion |
| `external_preprocess_comparison_artifacts` | `app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json`, `builder_jang_interview_transcript_preprocess_comparison.json`, `codex_ambassader_jung_transcript_preprocess_comparison.json` | lower input readiness, preprocess gate, packet-candidate examples | these are bridge-heavy lower artifacts with gate decisions and checkpoints | plausible from filename and embedded paths; no consistent artifact identity | `sidecar_identity_note` plus map entry | medium; packet-candidate only after bridge checklist, not by identity alone |
| `observer_raw_intake_generated_bundle` | `source_manifest_raw_intake_gap_analysis_before_middle_layer_fix_v1_*.json`, `split_units_raw_intake_gap_analysis_before_middle_layer_fix_v1_*.json`, `processing_trace_*`, `gmd_native_read_*` | lower material intake evidence, source/split/trace relation, bridge examples | these artifacts demonstrate lower readiness separation and are often referenced in Pre-1.12 reports | plausible family from shared stem and generated folder; role varies by prefix | `mapping_table_family_backfill` with role-specific entries | medium-high; source/split artifacts are evidence-ready, not packet-candidate by default |
| `line_axis_camera_review_reports` | `docs/reports/*line*`, `app/work/observer_ingest_min/generated/operator_summary_line_thickening_promotion_scope_*` | future promotion-sensitive review material | line/axis/camera materials are semantically important but can trigger over-promotion risk | weak/plausible from title only | `do_not_backfill_yet` | high; identity backfill may be mistaken as promotion readiness |
| `broad_observer_ingest_generated_archive` | many `app/work/observer_ingest_min/generated/source_manifest_*`, `processing_trace_*`, `operator_summary_*` | broad lower archive | too broad for current spine and too uneven in usage | mixed | `do_not_backfill_yet` except selected raw-intake bundle | high due to scale and uneven readiness |

## Priority

1. `phase1_5_to_1_10_runtime_run_artifacts`
2. `runtime_contract_v_series`
3. `external_preprocess_comparison_artifacts`
4. `observer_raw_intake_generated_bundle`
5. Hold line/axis/camera and broad archive families.

## Interpretation

These families come first because the current spine actually uses them for comparison, diff, identity, and bridge guardrail checks. Backfilling them improves operational comparison honesty without widening the repository surface.

All legacy artifacts should not be backfilled at once because the old archive is uneven. Some artifacts are receipts, traces, or promotion-sensitive reports. Giving them identity too broadly could make weak evidence look admission-ready.

The highest operational value is in families that help old/new mixed comparison: pre-identity runtime run artifacts and runtime contract versions. Lower preprocess and observer ingest families matter because they test the Pre-1.12B bridge guardrail.

## Validation

- Family selection is tied to actual current run and bridge usage: `PASS`.
- Scope is limited to high-value families: `PASS`.
- Line/axis promotion-sensitive material is held back: `PASS`.
- Bridge guardrail is preserved: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created/updated: `docs/reports/phase1_12_legacy_family_candidate_audit_report_v0.md`
3. What was backfilled: nothing yet; candidate families were audited.
4. What remains unresolved: backfill mode contract and target selection.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended next move: create bounded legacy identity backfill contract.
