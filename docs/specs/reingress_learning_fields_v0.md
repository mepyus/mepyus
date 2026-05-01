# Reingress Learning Fields v0

## Status

- phase: `phase1_6_evidence_grounding_hardening`
- authority: `working_spec`

## Execution

Additional reingress learning fields:

- `evidence_depth_summary`
- `useful_excerpt_modes`
- `weak_grounding_areas`
- `next_probe_hint`
- `reuse_candidate_assets`
- `unresolved_grounding_note`
- `merge_risk_summary`
- `future_validation_hint`

## Interpretation

Reingress is not only a result archive. It should tell the next run what kind of grounding worked, where evidence remained thin, and which assets are worth reusing. Without this, every run starts from the same shallow state.

Unresolved notes are not clutter. They are maturation material. A run that says "pointer-only here" gives the next run a concrete probe target.

## Validation

- Reingress can guide the next probe.
- Weakness is preserved alongside result.
- Learning fields are additive to v0.
