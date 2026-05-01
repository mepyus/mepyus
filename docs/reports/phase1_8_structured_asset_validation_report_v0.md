# Phase 1.8 Structured Asset Validation Report v0

## Overall Verdict

`PASS_WITH_NOTE`

Phase 1.8 improved structured asset reading by adding bounded JSON/path-aware evidence. Runtime contracts are no longer read only as top-level identity; exploration now emits structured evidence units with path refs, shape summaries, value excerpts, salience reasons, and comparison hints.

The note is that generated/large artifact reading remains shallow when the selected targets are contract templates rather than changing runtime instances. Salience scoring is useful but still heuristic.

## Files Created/Updated

Created:

- `docs/reports/phase1_8_structured_asset_gap_audit_report_v0.md`
- `docs/specs/structured_evidence_contract_v0.md`
- `docs/guides/structured_evidence_examples_v0.md`
- `runtime/contracts/space_exploration_result_v2.json`
- `docs/specs/structured_mode_selection_rules_v0.md`
- `scripts/cli/structured_helpers.py`
- `docs/specs/structured_merge_diff_rules_v0.md`
- `runtime/contracts/merge_diff_report_v2.json`
- `docs/specs/structured_reingress_learning_fields_v0.md`
- `runtime/contracts/space_reingress_record_v2.json`
- `docs/reports/phase1_8_run_01_v0.md`
- `docs/reports/phase1_8_run_02_v0.md`
- `docs/reports/phase1_8_run_03_v0.md`
- `docs/reports/phase1_8_run_04_v0.md`
- `docs/reports/phase1_8_run_05_v0.md`
- `docs/reports/phase1_8_provisional_lock_candidates_v0.md`

Updated:

- `scripts/cli/build_question_packet.py`
- `scripts/cli/explore_space.py`
- `scripts/cli/merge_or_diff.py`
- `scripts/cli/write_reingress_record.py`

Runtime artifacts:

- `runtime/query_packets/phase1_8_run_01_question_packet.json` through `phase1_8_run_05_question_packet.json`
- `runtime/exploration_results/phase1_8_run_01_exploration_result.json` through `phase1_8_run_05_exploration_result.json`
- `runtime/merge_diff_reports/phase1_8_run_01_merge_diff_report.json` through `phase1_8_run_05_merge_diff_report.json`
- `runtime/reingress_records/phase1_8_run_01_reingress_record.json` through `phase1_8_run_05_reingress_record.json`

## What Improved From Phase 1.7

- JSON/runtime assets are traversed as structured data, not only line excerpts.
- Exploration result now uses `space_exploration_result_v2`.
- Structured units include `path_ref`, `node_kind`, `shape_summary`, `value_excerpt`, `salience_reason`, and `comparison_hint`.
- Merge report now uses `merge_diff_report_v2` and carries salient paths plus structured merge risk notes.
- Reingress now uses `space_reingress_record_v2` and records structured learning fields.

## Bounded Run Summary

- run 01: runtime contract reading, `merge`, salient_path 18.
- run 02: generated/runtime interpretation, `merge`, salient_path 18.
- run 03: diff-heavy structured comparison, `diff`, salient_path 18.
- run 04: hold-trigger structured conflict, `hold`, stop discipline preserved.
- run 05: mixed prose + structured, `merge`, structured paths re-entered.

Observed structured quality:

- identity_only: 0 in all five bounded runs.
- shape_only: 0 in all five bounded runs.
- salient_path: 18 in all five bounded runs.
- structured_fallback: 0 in all five bounded runs.

## Operationally Improved

- Structured evidence now points to fields like `$.evidence_units[0].grounding_status`, `$.chosen_mode`, and `$.evidence_depth_summary.total`.
- Merge/diff can see whether structured support is path-salient or only shape-level.
- Reingress can preserve salient paths and reusable structured assets.
- Existing prose evidence and excerpt quality fields remain intact.

## Still Shallow

- Salience scoring is term-based, not semantic.
- Contract templates are easier than large generated runtime instances.
- Diff-heavy structured comparison does not yet compute actual before/after node diffs.
- Arrays are bounded to representative early items.

## Safe To Provisionally Reuse

- structured evidence units;
- JSON path refs;
- structured evidence summary;
- salient path propagation into merge/reingress;
- bounded JSON traversal.

## Not Ready To Lock

- structured taxonomy names;
- salience scoring weights;
- final v2 contract naming;
- generated artifact diff rules;
- baseline promotion.

## Validation

- CLI compile: PASS.
- Phase 1.8 runtime artifacts parse as JSON: PASS.
- Four-artifact spine preserved for all five runs: PASS.
- structured evidence fields present: PASS.
- merge report considers structured evidence: PASS.
- reingress structured learning fields present: PASS.
- hold discipline preserved: PASS.
- baseline promotion avoided: PASS.
- canonical path migration avoided: PASS.
- final naming lock avoided: PASS.

## Whether User Decision Is Required

No immediate user decision is required.

No source authority ladder was changed. No runtime path was moved. No final structured taxonomy lock was made.

## Recommended Next Move

Continue using Phase 1.8 on structured-heavy real questions. The next useful improvement is generated artifact diff salience: comparing two runtime records and surfacing changed paths, still without vector retrieval, UI, or baseline promotion.
