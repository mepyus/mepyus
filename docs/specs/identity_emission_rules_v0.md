# Identity Emission Rules v0

## Rules

- Every Phase 1.11-generated artifact should include `artifact_identity`.
- Identity is inline, not a canonical sidecar.
- Role is derived from the artifact lane and filename.
- Run stem and phase label are derived from the output stem when available.
- `generated_from_ref` records the immediate upstream artifact.
- `prior_artifact_ref` records the local handoff predecessor.
- Missing identity should be preserved as `weak_identity` or path-inferred `plausible_identity`.

## Interpretation

Bounded identity emission is more realistic than a full provenance graph for Phase 1.11. It gives pairing and diff enough self-description without creating a new authority layer.

Weak identity is better than silent guessing. If the loop must infer identity from a path, it should say so.

## Validation

- Identity fields must appear in generated artifacts.
- Artifact size should remain bounded.
- The four-artifact spine must remain unchanged.
