# line_thickening forward persistence confirmation note v0

## Why this check exists

`persistent_decay` should not remain a one-shot read. After the first persistence probe, the next question is whether that read still holds when a small amount of new primary-only support is appended.

## What this check does

- keeps the route surface fixed
- keeps breadth expansion out of scope
- adds only a tiny forward refresh for `transition_over_surface`
- reads whether `recent_decay_streak` and `last_derived_support_offset` continue to support `persistent_decay`

## Reading rule

- `decaying` = the recent window is clean
- `persistent_decay` = the clean direction keeps holding after additional primary-only refresh
- `reappearing` = derived support comes back into the recent window
- `stable_mixed` = there is no derived history to decay from, or the mixed state is currently flat rather than cleaning

## Guardrail

This is a direction check only. It does not change promotion scope, thickness, or route structure.
