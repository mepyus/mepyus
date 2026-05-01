# Pairing Mode Selection Rules v0

## Rule Order

1. Prefer explicit before/after markers when present.
2. Prefer same phase/run stem or same contract version family.
3. Prefer same logical runtime slot over nearby files.
4. Use timestamp only as a tie-breaker inside an already plausible family.
5. Use selected-order fallback only when no same-family pair can be confirmed.

## Interpretation

Pair ranking is a bounded middle step, not a full provenance engine. It is enough for the current CLI spine because Phase 1.10 only needs to reduce wrong-pair comparisons, expose ambiguity, and avoid overconfident diff claims.

Shared stem is useful but insufficient by itself. It should be paired with ordering basis, asset kind, and rejected candidates.

## Validation

- Wrong-order pairing should decrease.
- Same-family pair confidence should be visible.
- Ambiguous pair selection should remain in the artifact instead of being hidden.
