# Phase 1.18 Selection Pressure Next Note v0

## What Became Clear

- `flow` is not globally weak.
- `default selection` can miss real flow-bearing local slices.
- `selection pressure` explains more of the current failure surface than emitter failure alone.

## What Also Became Clear

- some families are genuinely poor flow carriers right now
  - preprocess comparison
  - compact/title-only
  - raw intake gap report
- so selection is not a magic fix

## Recommended Next Move

Selection tuning is the more justified next move.

Narrow target:

- compare current default seed ranking against a slightly flow-aware ranking
- keep it bounded to reader-side selection
- do not touch lower emitter yet

## Why Not Emitter Tuning Yet

The current evidence does not support a broad emitter failure claim.

It supports this narrower claim:

- the emitter can produce useful flow support in some families
- the reader does not always pick those local slices first

That is a selection problem before it is an emission problem.

