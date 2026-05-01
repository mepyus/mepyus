# Evidence Confidence Taxonomy v0

## Status

- phase: `phase1_6_evidence_grounding_hardening`
- authority: `working_spec`
- final naming lock: no

## Execution

Confidence labels:

- `low`: pointer-only, unreadable, missing excerpt, or weak relation.
- `medium`: bounded excerpt exists but support is contextual or not cross-supported.
- `high`: direct grounded excerpt or cross-supported evidence with no strong contradiction.

Grounding and confidence relationship:

- `pointer_only` usually maps to `low`.
- `weak_grounded` usually maps to `medium`.
- `direct_grounded` usually maps to `high` for local support.
- `cross_supported` usually maps to `high`, but authority conflicts can still force hold.

Confidence is not authority. A high-confidence excerpt from a report can still lose to a locked baseline in authority resolution.

## Interpretation

The taxonomy is intentionally small. Phase 1.6 needs better discipline, not a full semantic scoring engine. Confidence should prevent careless merge when evidence is thin and should explain why a diff/hold is more honest.

## Validation

- Labels are coarse enough for manual review.
- Labels do not replace authority ladder.
- Pointer-only fallback remains visible.
