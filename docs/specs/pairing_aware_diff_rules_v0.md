# Pairing-Aware Diff Rules v0

## Rules

- `weak_pair` diff evidence may support a cautious diff or hold note, but should not produce a strong comparison claim by itself.
- `plausible_pair` diff evidence can support ordinary diff claims when changed paths are salient.
- `strong_pair` plus salient changed paths can support stronger diff claims.
- Family mismatch is not automatically an authority conflict, but it is a meaningful comparison risk.
- Rejected pair candidates must be preserved when they affect comparison confidence.

## Interpretation

Diff salience and pair confidence are separate layers. Diff salience asks whether a changed path matters. Pair confidence asks whether the artifacts form a valid before/after comparison.

A good diff on a weak pair should remain cautious. Conversely, a strong pair with only trivial deltas should not force a strong diff.

## Validation

- Merge should not rely on top-level similarity alone.
- Diff should not rely on weak-pair salience without a risk note.
- Hold should remain narrow and tied to stop conditions or severe uncertainty.
