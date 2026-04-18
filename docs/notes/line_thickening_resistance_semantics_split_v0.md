# line thickening resistance semantics split note v0

## Purpose

This note hardens `line_thickening` so that not every non-promotion signal is treated as resistance.

The previous shape bundled too many cases into one pressure bucket. That made the line look structurally stuck: support could grow, but caution and weakness would keep accumulating as if they were direct counterevidence.

## Semantics split

- `support_points`
  - reasons the line is genuinely being read as present
- `weakness_points`
  - reasons the line is still thin or incomplete, but not contradicted
- `caution_points`
  - reasons to slow promotion without claiming a counterexample
- `contradiction_points`
  - actual evidence that pushes against the line

## Why this matters

The phrase "not enough yet" is not the same as "this line is wrong."

If those are merged, then recurrence validation can never escape thin mode because every cautious reread counts like a contradiction. The result is a false structural freeze.

## Registry discipline

The registry now treats `contradiction_count` as the real opposing pressure.
`weakness_count` and `caution_count` remain visible, but they are not symmetric with support.

## One-line lock

> Thinness from caution is not contradiction, and recurrence should be able to accumulate support without being canceled by mere insufficiency.
