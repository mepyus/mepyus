# Diff Mode Selection Rules v0

## Execution

Bounded diff extraction rules:

- Compare selected JSON artifacts in stable pairs.
- Prefer same family before/after pairs when names suggest sequence or phase.
- Compare common paths first.
- Separate `added`, `removed`, and `modified`.
- Rank mode/status/evidence_depth/quality/validation changes above identity/timestamp changes.
- Keep only salient changed paths.
- If comparison fails, record shape-only or pointer-only fallback.

## Interpretation

Whole-object diff dumps are too noisy for this spine. The useful unit is a changed path with before/after values and a reason.

## Validation

- Changed paths are bounded.
- Trivial diffs are counted but not over-promoted.
- Fallback is explicit.
