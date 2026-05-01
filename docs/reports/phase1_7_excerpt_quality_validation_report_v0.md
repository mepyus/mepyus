# Phase 1.7 Excerpt Quality Validation Report v0

## Overall Verdict

`PASS_WITH_NOTE`

Phase 1.7 improved excerpt quality without breaking the Phase 1.5/1.6 spine. Title-only capture was reduced in bounded runs, quality fields are now populated, and merge/reingress artifacts preserve excerpt quality summaries.

The note is that generated/runtime JSON excerpts are readable but still shallow, and the quality labels remain heuristic.

## Files Created/Updated

Created:

- `docs/reports/phase1_7_excerpt_failure_shape_audit_report_v0.md`
- `docs/specs/excerpt_quality_contract_v0.md`
- `docs/guides/excerpt_quality_examples_v0.md`
- `docs/specs/excerpt_mode_selection_rules_v0.md`
- `docs/specs/excerpt_retry_and_fallback_policy_v0.md`
- `docs/reports/phase1_7_run_01_v0.md`
- `docs/reports/phase1_7_run_02_v0.md`
- `docs/reports/phase1_7_run_03_v0.md`
- `docs/reports/phase1_7_run_04_v0.md`
- `docs/reports/phase1_7_run_05_v0.md`
- `docs/reports/phase1_7_provisional_lock_candidates_v0.md`

Updated:

- `scripts/cli/excerpt_helpers.py`
- `scripts/cli/explore_space.py`
- `scripts/cli/merge_or_diff.py`
- `scripts/cli/write_reingress_record.py`
- `scripts/cli/build_question_packet.py`

Runtime artifacts:

- `runtime/query_packets/phase1_7_run_01_question_packet.json` through `phase1_7_run_05_question_packet.json`
- `runtime/exploration_results/phase1_7_run_01_exploration_result.json` through `phase1_7_run_05_exploration_result.json`
- `runtime/merge_diff_reports/phase1_7_run_01_merge_diff_report.json` through `phase1_7_run_05_merge_diff_report.json`
- `runtime/reingress_records/phase1_7_run_01_reingress_record.json` through `phase1_7_run_05_reingress_record.json`

## What Improved From Phase 1.6

- Excerpts now carry `excerpt_quality`.
- Poor recoverable excerpts can retry/widen before being accepted.
- Title-only and metadata-only excerpts are detected.
- Exploration result includes `excerpt_quality_summary`.
- Merge report carries `excerpt_quality_summary` and can record merge risk when poor excerpts remain.
- Reingress record preserves excerpt quality summary for the next run.
- Runtime/generated JSON targets can be added for stress runs.

## Bounded Run Summary

- run 01: space-first exploration, `merge`, title-only reduced to 0.
- run 02: mixed Codex + space, `merge`, quality summary present.
- run 03: diff-heavy, `diff`, quality diff preserved.
- run 04: hold-trigger, `hold`, final-lock protection preserved.
- run 05: runtime/generated JSON stress, `merge`, readable but shallow JSON excerpts.

Observed quality:

- run 01: poor 0, usable 2, strong 4, retried 2.
- run 02: poor 0, usable 2, strong 4, retried 2.
- run 03: poor 0, usable 3, strong 3, retried 2.
- run 04: poor 0, usable 4, strong 3, retried 2.
- run 05: poor 0, usable 3, strong 6, retried 2.

## Operationally Improved

- Grounded evidence is more readable.
- Title-only evidence is no longer silently treated as sufficient.
- Retry/widen is bounded and visible.
- Quality summaries make manual review easier.
- Pointer fallback remains available.

## Still Heuristic-Bound

- Quality labels are rule-based, not semantic entailment.
- JSON contract excerpts are top-level and may be shallow.
- Cross-supported status can still be generous when the excerpt is only usable.
- Larger generated documents need more stress cases.

## Safe To Provisionally Reuse

- `excerpt_quality`
- `excerpt_retry_count`
- `fallback_reason`
- `tuning_note`
- bounded heading/block widening
- quality summary propagation

## Not Ready To Lock

- final taxonomy names;
- thresholds for usable vs strong;
- scoring for generated JSON;
- baseline promotion of the quality contract.

## Validation

- CLI compile: PASS.
- All Phase 1.7 runtime artifacts parse as JSON: PASS.
- Four-artifact spine preserved for all five runs: PASS.
- `excerpt_quality` field present in evidence units: PASS.
- quality summary present in exploration/merge/reingress: PASS.
- title_only/metadata_only issue count reduced to 0 in bounded runs: PASS.
- hold discipline preserved: PASS.
- baseline promotion avoided: PASS.
- final naming lock avoided: PASS.

## Whether User Decision Is Required

No immediate user decision is required.

No grounded contract meaning was changed. No artifact path was moved. No final naming lock was made.

## Recommended Next Move

Continue using Phase 1.7 on real questions. The next practical improvement should be stress-testing more diverse documents and tuning JSON/generated excerpt scoring, still without UI, vector retrieval, or baseline promotion.
