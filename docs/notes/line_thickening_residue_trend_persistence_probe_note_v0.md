# line_thickening residue trend persistence probe note v0

## Why this probe exists

`derived_residue_trend=decaying` is not enough by itself. It says the recent window is cleaner, but it does not say whether that cleaning persists when the current line keeps receiving primary-only observations.

## What we read

- `transition_over_surface` is the only line probed for persistence.
- `derived_residue_trend` reads short-window direction.
- `derived_residue_persistence` reads whether that direction is still holding under continued primary-only refresh.

## Persistence classes

- `unconfirmed_decay`: one clean recent window, but not enough history to call persistence.
- `persistent_decay`: repeated clean recent windows with no recent derived return.
- `stable_mixed`: no derived residue in the observed history, or a stable non-decay mixed shape.
- `reappearing`: derived residue returned in the recent window.
- `insufficient_history`: too little evidence to say anything stable.

## Reading rule

`decaying` is directional.
`persistent_decay` is directional plus retained across refresh.
They are not the same signal.

## Guardrail

This axis is interpretation only. It does not change status, scope, or promotion behavior.
