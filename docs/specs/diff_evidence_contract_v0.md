# Diff Evidence Contract v0

## Status

- phase: `phase1_9_generated_artifact_diff_salience`
- authority: `working_spec`
- compatibility: additive to Phase 1.8 structured evidence

## Execution

Diff evidence unit fields:

- `source_ref_before`
- `source_ref_after`
- `asset_kind`
- `path_ref`
- `change_type`
- `before_excerpt`
- `after_excerpt`
- `delta_summary`
- `salience_reason`
- `why_it_matters`
- `relation_type`
- `grounding_status`
- `local_confidence`
- `comparison_hint`

Allowed `change_type` values:

- `added`
- `removed`
- `modified`
- `mode_shift`
- `count_change`
- `status_change`
- `evidence_depth_change`

## Interpretation

Changed path alone is not enough. A reader needs the before value, after value, and a delta summary to understand the difference. `salience_reason` explains why this change was selected instead of the many trivial changes that JSON records can contain.

Not every change is important. Timestamp, record id, or path string differences may be expected. Mode, status, validation, evidence depth, quality, and risk changes are usually more operationally salient.

## Validation

- Units stay bounded.
- Structured evidence remains compatible.
- Before/after values are visible.
- Fallback comparison remains allowed.
