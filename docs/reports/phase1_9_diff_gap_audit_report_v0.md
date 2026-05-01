# Phase 1.9 Diff Gap Audit Report v0

## Verdict

`PASS_WITH_NOTE`

Phase 1.8 can read structured paths, but comparison is still not a true before/after diff. It surfaces salient paths from individual JSON assets, not changed paths between two generated/runtime artifacts.

## Execution

Audited:

- `docs/reports/phase1_8_structured_asset_validation_report_v0.md`
- `docs/specs/structured_evidence_contract_v0.md`
- `docs/specs/structured_merge_diff_rules_v0.md`
- `scripts/cli/structured_helpers.py`
- `scripts/cli/explore_space.py`
- `scripts/cli/merge_or_diff.py`
- Phase 1.8 run artifacts
- `runtime/contracts/*.json`
- generated-like runtime run artifacts

## Gap Types

- `change_detected_but_not_ranked`: not yet applicable because changed paths are not computed.
- `path_detected_but_not_explained`: Phase 1.8 paths have salience reasons, but not before/after meaning.
- `before_after_missing`: main gap; evidence units do not include before/after values.
- `nested_delta_blindness`: nested JSON changes are not compared across records.
- `noisy_delta_dump`: future risk if full object diffs are dumped.
- `diff_without_salience`: current diff mode can be task-based even when no changed path evidence exists.
- `fallback_overuse_on_comparison`: not observed yet, but needed for unparseable or unmatched comparison pairs.

## Interpretation

Structured reading naturally leads to diff salience. Once JSON paths are visible, the next question is whether those paths changed between two artifacts and whether that change matters. A changed path without before/after values is hard to judge. A before/after value without salience can become noise.

Diff reading matters most for:

- runtime contract version shifts;
- generated run records;
- comparison-heavy questions;
- evidence-depth and quality changes across phases;
- hold-trigger comparisons where a state or mode shift might matter.

## Validation

- Diff gap is separate from structured single-asset reading: PASS.
- Next contract target is clear: before/after changed path evidence.
- Existing spine can be preserved with additive v3 fields.
