# Identity-Aware Pairing Rules v0

## Rules

- Strong pair confidence should be treated cautiously when either artifact has weak identity.
- Embedded identity anchors can strengthen pairing when role, slot, and family align.
- Explicit `prior_artifact_ref` can support a stronger lineage link.
- Identity mismatch is not an authority conflict, but it is a comparison risk.
- Weak identity above a salient diff should produce a risk note rather than a silent merge or overconfident diff.

## Interpretation

Pair confidence and identity confidence answer different questions. Pair confidence asks whether two artifacts belong together. Identity confidence asks whether each artifact can describe itself well enough to support that relation.

Self-description improves comparison honesty because it lets the loop explain not only what changed, but what kind of artifacts were compared.

## Validation

- Identity confidence must be visible in pairing units.
- Merge/diff/hold must carry identity risk.
- Hold remains narrow and does not trigger solely because identity is path-inferred.
