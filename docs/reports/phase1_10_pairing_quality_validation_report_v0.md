# Phase 1.10 Pairing Quality Validation Report v0

## Overall Verdict

`PASS_WITH_NOTE`

Phase 1.10 added bounded artifact family pairing while preserving the Phase 1.5 through Phase 1.9 CLI spine. The loop now records why a generated/runtime before/after pair was selected before reading diff salience.

The note is that pairing remains heuristic. It is operationally stronger than selected-order pairing, but ambiguous generated/runtime families still need more real-use runs before any final lock.

## Files Created/Updated

Created:

- `docs/reports/phase1_10_pairing_gap_audit_report_v0.md`
- `docs/specs/artifact_family_pairing_contract_v0.md`
- `docs/guides/artifact_pairing_examples_v0.md`
- `runtime/contracts/space_exploration_result_v4.json`
- `docs/specs/pairing_mode_selection_rules_v0.md`
- `scripts/cli/pairing_helpers.py`
- `docs/specs/pairing_aware_diff_rules_v0.md`
- `runtime/contracts/merge_diff_report_v4.json`
- `docs/specs/pairing_reingress_learning_fields_v0.md`
- `runtime/contracts/space_reingress_record_v4.json`
- `docs/reports/phase1_10_run_01_v0.md`
- `docs/reports/phase1_10_run_02_v0.md`
- `docs/reports/phase1_10_run_03_v0.md`
- `docs/reports/phase1_10_run_04_v0.md`
- `docs/reports/phase1_10_run_05_v0.md`
- `docs/reports/phase1_10_provisional_lock_candidates_v0.md`

Updated:

- `scripts/cli/build_question_packet.py`
- `scripts/cli/diff_helpers.py`
- `scripts/cli/explore_space.py`
- `scripts/cli/merge_or_diff.py`
- `scripts/cli/write_reingress_record.py`

Runtime artifacts:

- `runtime/query_packets/phase1_10_run_01_question_packet.json` through `phase1_10_run_05_question_packet.json`
- `runtime/exploration_results/phase1_10_run_01_exploration_result.json` through `phase1_10_run_05_exploration_result.json`
- `runtime/merge_diff_reports/phase1_10_run_01_merge_diff_report.json` through `phase1_10_run_05_merge_diff_report.json`
- `runtime/reingress_records/phase1_10_run_01_reingress_record.json` through `phase1_10_run_05_reingress_record.json`

## What Improved From Phase 1.9

- Exploration result now uses `space_exploration_result_v4`.
- Pairing units include `family_key`, `lineage_hint`, `pairing_basis`, `pair_confidence`, `ordering_basis`, `why_this_pair`, rejected candidates, and ambiguity notes.
- Diff evidence units receive pair metadata from the selected pairing unit.
- Merge report now uses `merge_diff_report_v4`.
- Merge/diff/hold reports include pair confidence, family keys, pairing risk, strongest pair support refs, and rejected candidate summaries.
- Reingress now uses `space_reingress_record_v4`.
- Reingress records preserve useful pairing modes, reusable family groups, weak pair areas, rejected candidates, and next pairing probes.

## Bounded Run Summary

- run 01: same-family runtime before/after comparison, `diff`, `strong_pair`.
- run 02: generated artifact version lineage comparison, `diff`, `strong_pair`.
- run 03: ambiguous unrelated generated artifacts, `diff`, `weak_pair`.
- run 04: final taxonomy/path movement stop case, `hold`, `weak_pair`.
- run 05: mixed prose + structured comparison, `merge`, `strong_pair`.

Observed pairing quality:

- strong pair runs: 3.
- weak pair runs: 2.
- rejected pair candidates recorded in all five runs.
- comparison fallback count: 0.
- pairing learning fields present in all five reingress records.

## Operationally Improved

The loop no longer compares JSON artifacts only by selected order when a same-family path exists. It prefers shared run stems and phase/version ordering, records rejected candidates, and carries pair confidence into merge/diff/hold.

Weak-pair runs now remain honest: the diff can still be computed, but the merge report and reingress record state that the comparison rests on fallback pairing.

## Still Heuristic

- Family keys are normalized from path/stem/version markers.
- There is no full provenance graph.
- Content signature family matching is not implemented.
- Large generated artifacts may still need manual review when stems are ambiguous.

## Safe To Provisionally Reuse

- `pairing_units`
- `pairing_summary`
- `pair_confidence`
- `family_key`
- `pairing_basis`
- `rejected_pair_candidates`
- pairing-aware risk notes in merge/reingress

## Not Ready To Lock

- final family taxonomy;
- final pair confidence taxonomy;
- global artifact lineage model;
- baseline promotion;
- canonical path rules.

## Validation

- CLI compile: PASS.
- v4 runtime contracts parse as JSON: PASS.
- Phase 1.10 runtime artifacts parse as JSON: PASS.
- Four-artifact spine preserved for all five runs: PASS.
- pair fields present in exploration: PASS.
- merge reports consider pair confidence: PASS.
- reingress pairing learning fields present: PASS.
- hold discipline preserved: PASS.
- baseline promotion avoided: PASS.
- canonical path migration avoided: PASS.
- final naming lock avoided: PASS.

## Whether User Decision Is Required

No immediate user decision is required.

No authority ladder was changed. No canonical runtime path was moved. No final pairing taxonomy lock was made.

## Recommended Next Move

Continue using the Phase 1.10 loop on generated/runtime comparison questions. The next useful improvement is content-signature support for ambiguous family matching, still as a bounded heuristic rather than a full provenance engine.
