# Phase 1.6 Evidence Gap Audit Report v0

## Verdict

`PASS_WITH_NOTE`

Phase 1.5 spine is intact and repeatable. The gap is not structure absence; it is evidence depth. Current artifacts can say which files were selected and why, but they mostly cannot show what exact text was read, how strong that local grounding is, or how evidence depth affects merge/diff/hold.

## Execution

Audited:

- `docs/reports/phase1_5_usage_loop_binding_validation_report_v0.md`
- `docs/specs/space_exploration_contract_v0.md`
- `docs/specs/evidence_merge_diff_hold_contract_v0.md`
- `docs/specs/space_reingress_package_v0.md`
- `scripts/cli/run_phase1_space_query.py`
- `scripts/cli/explore_space.py`
- `scripts/cli/merge_or_diff.py`
- `scripts/cli/write_reingress_record.py`
- `runtime/contracts/space_exploration_result_v0.json`
- `runtime/contracts/merge_diff_report_v0.json`
- `runtime/contracts/space_reingress_record_v0.json`
- sample Phase 1.5 artifacts under `runtime/exploration_results`, `runtime/merge_diff_reports`, and `runtime/reingress_records`.

## Gap Categories

## Pointer-Only Evidence

Current evidence units contain:

- `source_ref`
- `excerpt_or_pointer`
- `why_it_matters`
- `relation_type`
- `confidence`

In Phase 1.5 runs, `excerpt_or_pointer` is usually just the path again. This is enough to prove that a path was selected, but not enough to prove what local text supports the claim.

## Weak Grounded Evidence Candidate

The selected asset reason is useful. It explains why the path was included, but it is still not grounded in source text. It can become weak grounded evidence when paired with a bounded excerpt window.

## Direct Grounded Evidence Candidate

Direct grounded evidence should include:

- path;
- line range or block pointer;
- small excerpt window;
- why the excerpt matters for the interpreted goal.

The current scripts do not extract this yet.

## Cross-Supported Candidate

Cross-support exists conceptually when multiple selected assets point in the same direction, for example goal/non-goal plus authority ladder plus reading order. Current artifacts list multiple paths but do not mark cross-support relationships.

## Excerpt Extraction Missing Zone

The missing zone is `explore_space.py`. It creates evidence units from selected assets without reading the selected files. This keeps the loop safe but leaves evidence thin.

## Confidence Missing Zone

`confidence: medium` is currently coarse. It does not distinguish:

- pointer-only confidence;
- excerpt-level local confidence;
- cross-supported confidence;
- authority confidence;
- contradiction/tension strength.

## Interpretation

The current loop is sufficient because it stabilizes the handoff sequence: one command creates packet, exploration, merge/diff/hold, and reingress. That is the spine. The next bottleneck is not more retrieval; it is grounding quality inside the evidence units.

Pointer-level evidence is especially weak for:

- baseline/current-working comparisons;
- diff-heavy questions;
- hold-trigger questions where authority conflict must be justified;
- reingress learning questions where the next run needs to know what actually worked.

For simple routing or path discovery, pointer-level may remain acceptable. For any claim that says "this supports", "this conflicts", or "this should merge", pointer-only is too thin.

## Validation

- Gap type is evidence depth, not missing spine: PASS.
- Current spine can be preserved: PASS.
- Contract targets are clear: evidence unit fields, excerpt modes, confidence/depth summary, reingress learning fields.
- No baseline meaning or canonical path change is required.

## Most Urgent Evidence Weakness

`explore_space.py` must read selected local markdown/json files and fill `excerpt_window`, `excerpt_mode`, `grounding_status`, and `local_confidence` while preserving `pointer_only` fallback.

## Entry Condition For Next Stage

Create a grounded evidence unit contract and a compatible v1 exploration result template without invalidating v0 artifacts.
