# Merge Diff Hold Grounding Rules v0

## Status

- phase: `phase1_6_evidence_grounding_hardening`
- authority: `working_spec`

## Execution

Grounding-aware mode guidance:

- mostly `pointer_only`: avoid confident merge; choose `diff` unless the user only asked for path routing.
- `weak_grounded` plus mild support: choose cautious `merge` or `diff` depending on task mode.
- `direct_grounded`: merge is allowed when authority and task mode align.
- `cross_supported`: stronger merge basis when no contradiction exists.
- strong contradiction or tension: choose `diff`.
- authority conflict or stop condition: choose `hold`.

Merge report should include:

- `evidence_depth_summary`
- `strongest_support_refs`
- `strongest_tension_refs`
- `merge_risk_note`
- `hold_trigger_reason`
- `confidence_distribution`

## Interpretation

Merge cannot be based on alignment language alone. If evidence depth is thin, a merge can hide uncertainty. In that case, `diff` may be the more honest judgment because it preserves the gap. `hold` remains a protection device for authority and structural risks, not a generic failure state.

Authority ladder and grounding depth are different layers. Authority answers "which source has priority"; grounding answers "how much local text supports the use of that source." Both must be visible.

## Validation

- Over-merge risk is recorded.
- Hold remains tied to stop/authority conditions.
- Evidence insufficiency can become diff without pretending to be authority conflict.
