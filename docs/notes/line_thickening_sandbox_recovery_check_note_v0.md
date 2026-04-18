# line_thickening sandbox recovery check note v0

## Why recovery is needed

The sandbox trip already proved that the derived reintroduction sentinel can flip.

That is not enough by itself.
The sentinel should also be able to leave the tripped state when enough primary-only rows push the derived row back outside the active recent window.

## Recovery method

- keep the main runtime untouched
- keep the same sandbox style runtime copy
- reuse only existing primary routes
- append a small set of distinct primary `transition_over_surface` rows after the sandbox trip

## Expected loop

- before: `observed_but_outside_window`
- after trip: `observed_recently`
- after recovery: `observed_but_outside_window`

## Guardrail

The point is not promotion, route expansion, or breadth expansion.
The point is only to prove that the sentinel behaves like a looped monitoring device rather than a one-way flag.
