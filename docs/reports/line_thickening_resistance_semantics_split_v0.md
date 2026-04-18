# line thickening resistance semantics split v0

## Verdict

PASS

## What changed

`line_thickening` now separates:

- `weakness_points`
- `caution_points`
- `contradiction_points`

The registry keeps compatibility with `resistance_count`, but the derived state is now based on `contradiction_count` as the only true opposing pressure.

## Verification path

The same grounded path was re-run with a bounded cohort:

- `frag_ytex_001`
- `frag_ytex_001` again
- `frag_ytex_002`
- `frag_ytex_003`
- `frag_basic_003`

Run:

```bash
python3 scripts/apply_internal_observer.py runtime frag_ytex_001 frag_ytex_001 frag_ytex_002 frag_ytex_003 frag_basic_003 --record-line-thickening --bounded-recurrence-validation
```

Observed behavior:

- the replayed second `frag_ytex_001` was still suppressed as an exact duplicate
- the distinct fragments appended direct-span observations
- the new packets carried `caution_points` for insufficient-repeatability language
- `contradiction_points` stayed empty for the validation cohort
- the registry accumulated support without turning all thinness into opposing pressure

## Promotion effect

The evaluator now treats:

- `contradiction` as actual counterevidence
- `weakness` as incompleteness
- `caution` as delay pressure

This means recurrence can now add support without being canceled by mere insufficiency.

## Current state

`input_to_reading_organ` remains conservative, but it is no longer structurally frozen by caution accumulation alone.

## Next boundary

The next step should only happen if a later grounded run produces real contradiction points or enough recurrence to justify a medium gate. No widening is needed yet.
