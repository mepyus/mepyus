# Phase 1.6 Evidence Grounding Validation Report v0

## Overall Verdict

`PASS_WITH_NOTE`

Phase 1.6 improved the Phase 1.5 loop from pointer-level evidence toward grounded evidence. The spine remains intact:

`question packet -> exploration result -> merge/diff/hold report -> reingress record`

The note is that excerpt quality is bounded-useful, not semantically complete. Some excerpts are still title-level or locally thin, so manual support remains necessary for high-stakes interpretation.

## Files Created/Updated

Created:

- `docs/reports/phase1_6_evidence_gap_audit_report_v0.md`
- `docs/specs/evidence_unit_grounding_contract_v0.md`
- `runtime/contracts/space_exploration_result_v1.json`
- `docs/guides/evidence_unit_examples_v0.md`
- `docs/specs/excerpt_extraction_rules_v0.md`
- `docs/guides/excerpt_fallback_policy_v0.md`
- `scripts/cli/excerpt_helpers.py`
- `docs/specs/evidence_confidence_taxonomy_v0.md`
- `docs/specs/merge_diff_hold_grounding_rules_v0.md`
- `runtime/contracts/merge_diff_report_v1.json`
- `docs/specs/reingress_learning_fields_v0.md`
- `runtime/contracts/space_reingress_record_v1.json`
- `docs/guides/reingress_learning_examples_v0.md`
- `docs/reports/phase1_6_run_01_v0.md`
- `docs/reports/phase1_6_run_02_v0.md`
- `docs/reports/phase1_6_run_03_v0.md`
- `docs/reports/phase1_6_run_04_v0.md`
- `docs/reports/phase1_6_run_05_v0.md`
- `docs/reports/phase1_6_provisional_lock_candidates_v0.md`

Updated:

- `scripts/cli/build_question_packet.py`
- `scripts/cli/explore_space.py`
- `scripts/cli/merge_or_diff.py`
- `scripts/cli/write_reingress_record.py`

Runtime artifacts:

- `runtime/query_packets/phase1_6_run_01_question_packet.json` through `phase1_6_run_05_question_packet.json`
- `runtime/exploration_results/phase1_6_run_01_exploration_result.json` through `phase1_6_run_05_exploration_result.json`
- `runtime/merge_diff_reports/phase1_6_run_01_merge_diff_report.json` through `phase1_6_run_05_merge_diff_report.json`
- `runtime/reingress_records/phase1_6_run_01_reingress_record.json` through `phase1_6_run_05_reingress_record.json`

## What Improved From Phase 1.5

- exploration result now uses `space_exploration_result_v1`.
- evidence units include `pointer`, `excerpt_window`, `excerpt_mode`, `local_confidence`, `cross_support_refs`, `contradiction_note`, and `grounding_status`.
- bounded excerpt extraction reads local files and preserves line pointers.
- merge report now uses `merge_diff_report_v1`.
- merge/diff/hold includes `evidence_depth_summary`, `confidence_distribution`, `strongest_support_refs`, `merge_risk_note`, and `hold_trigger_reason`.
- reingress now uses `space_reingress_record_v1`.
- reingress includes learning fields such as `useful_excerpt_modes`, `weak_grounding_areas`, `reuse_candidate_assets`, and `future_validation_hint`.

## What Remains Thin

- Excerpt extraction is heuristic and sometimes returns only a heading or short metadata block.
- Cross-support is simple same-relation support, not semantic entailment.
- Confidence labels are coarse and not final taxonomy.
- JSON templates are still templates, not strict JSON Schema.
- Generated/large/unusual documents need more fallback testing.

## Operationally Stronger

- Codex can now show what local text was used as evidence.
- Merge reports can see whether evidence was pointer-only or grounded.
- Reingress tells the next run which excerpt modes and assets were useful.
- Stop discipline still works: run 04 remained `hold`.

## Still Manual-Support Dependent

- deciding whether an excerpt truly supports a nuanced claim;
- resolving implicit authority conflict;
- reviewing title-only excerpts;
- tuning excerpt selection per document shape.

## Not Yet Ready To Lock

- confidence taxonomy names;
- v1 runtime contract names as final;
- excerpt mode priority;
- cross-support scoring;
- baseline promotion.

## Promising Lock Candidates

- additive evidence unit fields;
- pointer-only fallback rule;
- evidence depth summary in merge reports;
- reingress learning fields.

## Validation

Checks performed:

- Python compile for all CLI scripts including `excerpt_helpers.py`: PASS.
- Five bounded Phase 1.6 runs completed: PASS.
- All runs produced four artifacts: PASS.
- Exploration artifacts contain grounded fields: PASS.
- Merge reports consider evidence depth: PASS.
- Reingress records contain learning fields: PASS.
- Stop/hold discipline preserved: PASS.
- Baseline promotion avoided: PASS.
- Canonical path migration avoided: PASS.

Observed run summary:

- run 01: space-first exploration, `merge`, grounded evidence present.
- run 02: mixed Codex + space, `merge`, grounded evidence present.
- run 03: diff-heavy, `diff`, evidence depth summary present.
- run 04: hold-trigger, `hold`, user decision flagged.
- run 05: reingress learning, `merge`, learning fields present.

## Whether User Decision Is Required

No immediate user decision is required.

No baseline meaning was changed. No canonical path was moved. No final naming lock was made. No large structural alternative was selected.

## Recommended Next Move

Continue using the Phase 1.6 loop on real questions and watch:

- title-only excerpt frequency;
- pointer-only fallback ratio;
- whether `cross_supported` is too generous;
- whether confidence labels need more granularity.

Do not promote to baseline yet. The next practical improvement should be excerpt quality tuning, not UI or vector retrieval.
