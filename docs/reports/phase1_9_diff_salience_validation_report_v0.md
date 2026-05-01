# Phase 1.9 Diff Salience Validation Report v0

## Overall Verdict

`PASS_WITH_NOTE`

Phase 1.9 added bounded generated/runtime diff salience while preserving the Phase 1.5/1.6/1.7/1.8 spine. The loop now emits before/after changed path evidence and carries salient deltas into merge and reingress records.

The note is that pairing and salience scoring are heuristic. Large/generated comparisons still need more diverse stress runs before any final lock.

## Files Created/Updated

Created:

- `docs/reports/phase1_9_diff_gap_audit_report_v0.md`
- `docs/specs/diff_evidence_contract_v0.md`
- `docs/guides/diff_evidence_examples_v0.md`
- `runtime/contracts/space_exploration_result_v3.json`
- `docs/specs/diff_mode_selection_rules_v0.md`
- `scripts/cli/diff_helpers.py`
- `docs/specs/diff_aware_merge_hold_rules_v0.md`
- `runtime/contracts/merge_diff_report_v3.json`
- `docs/specs/diff_reingress_learning_fields_v0.md`
- `runtime/contracts/space_reingress_record_v3.json`
- `docs/reports/phase1_9_run_01_v0.md`
- `docs/reports/phase1_9_run_02_v0.md`
- `docs/reports/phase1_9_run_03_v0.md`
- `docs/reports/phase1_9_run_04_v0.md`
- `docs/reports/phase1_9_run_05_v0.md`
- `docs/reports/phase1_9_provisional_lock_candidates_v0.md`

Updated:

- `scripts/cli/build_question_packet.py`
- `scripts/cli/explore_space.py`
- `scripts/cli/merge_or_diff.py`
- `scripts/cli/write_reingress_record.py`

Runtime artifacts:

- `runtime/query_packets/phase1_9_run_01_question_packet.json` through `phase1_9_run_05_question_packet.json`
- `runtime/exploration_results/phase1_9_run_01_exploration_result.json` through `phase1_9_run_05_exploration_result.json`
- `runtime/merge_diff_reports/phase1_9_run_01_merge_diff_report.json` through `phase1_9_run_05_merge_diff_report.json`
- `runtime/reingress_records/phase1_9_run_01_reingress_record.json` through `phase1_9_run_05_reingress_record.json`

## What Improved From Phase 1.8

- Exploration result now uses `space_exploration_result_v3`.
- Diff evidence units include before/after refs, changed path, change type, before/after excerpts, delta summary, and salience reason.
- Merge report now uses `merge_diff_report_v3`.
- Merge/diff reports include salient diff paths, strongest diff support refs, comparison risk notes, and mode/status change notes.
- Reingress now uses `space_reingress_record_v3`.
- Reingress records include useful diff modes, reusable comparison pairs, salient diff path summaries, and generated diff notes.

## Bounded Run Summary

- run 01: runtime before/after comparison, `diff`, salient_diff 16.
- run 02: generated artifact version shift, `diff`, salient_diff 16.
- run 03: diff-heavy structured case, `diff`, salient_diff 8.
- run 04: hold-trigger comparison conflict, `hold`, stop discipline preserved.
- run 05: mixed prose + structured comparison, `merge`, diff learning fields present.

Observed diff quality:

- salient_diff paths were generated in all five runs.
- trivial_diff count was 0 in bounded runs.
- comparison_fallback count was 0 in bounded runs.
- evidence_depth_change was surfaced in comparison runs.

## Operationally Improved

- The loop can now say what changed, not just that two JSON artifacts differ.
- Before/after values are visible in diff evidence units.
- Merge/diff/hold can see salient changed paths.
- Reingress can preserve reusable comparison pairs.

## Still Heuristic

- Pairing strategy is simple selected-JSON order.
- Salience scoring is term-based.
- No full AST diff or semantic diff engine exists.
- Large generated records may need stricter noise filtering.

## Safe To Provisionally Reuse

- diff evidence units;
- changed path summaries;
- before/after excerpts;
- salient diff path propagation;
- reusable comparison pairs.

## Not Ready To Lock

- final change type taxonomy;
- salience weights;
- pairing rules;
- final v3 contract naming;
- baseline promotion.

## Validation

- CLI compile: PASS.
- v3 runtime contracts parse as JSON: PASS.
- Phase 1.9 runtime artifacts parse as JSON: PASS.
- Four-artifact spine preserved for all five runs: PASS.
- diff evidence fields present: PASS.
- merge reports consider diff evidence: PASS.
- reingress diff learning fields present: PASS.
- hold discipline preserved: PASS.
- baseline promotion avoided: PASS.
- canonical path migration avoided: PASS.
- final naming lock avoided: PASS.

## Whether User Decision Is Required

No immediate user decision is required.

No authority ladder was changed. No runtime path was moved. No final diff taxonomy lock was made.

## Recommended Next Move

Continue using Phase 1.9 on generated/runtime comparison questions. The next useful improvement is pairing quality: selecting before/after artifacts from the same family more deliberately, still without UI, vector retrieval, or baseline promotion.
