# line_thickening transition_over_surface sentinel loop close-out note v0

## Purpose

This note closes the current sentinel-loop check for `transition_over_surface`.

The goal is not to widen the system further.
The goal is to lock what is currently proven, what is not proven, and how the line should be read now.

## Current Closed Points

- the main runtime currently reads `transition_over_surface` as:
  - `validation_profile=mixed_derived_supported`
  - `primary_only_validation_profile=balanced_broadening_candidate`
  - `derived_residue_trend=decaying`
  - `derived_residue_persistence=persistent_decay`
  - `derived_residue_robustness=robust_decay`
  - `derived_reintroduction_status=observed_but_outside_window`
- a sandbox-only derived re-entry can flip the sentinel to `observed_recently`
- a bounded primary-only sandbox refresh can push that same derived row back outside the recent window
- the main runtime stayed untouched during the trip and recovery checks

## Current Official Reading Of transition_over_surface

`transition_over_surface` is currently:

- overall `mixed_derived_supported`
- primary-only `balanced_broadening_candidate`
- trending toward cleaner primary support in the recent window
- still not a clean-balanced or global line

More specifically:

- the overall ecology is still mixed because derived/self-referential support remains in history
- the primary-only side is already materially broader and stronger than before
- the residue trend is decaying in the main runtime
- that decay is persistent under the current recent-window read
- the multi-window direction is robust enough to read as `robust_decay`

## Sentinel Loop Meaning

The sentinel is not static metadata.

It behaves like a monitoring loop:

- if derived residue re-enters the active recent window, it can flip to `observed_recently`
- if later primary-only refresh pushes that residue back outside the window, it can return to `observed_but_outside_window`

This means the sentinel is behaving as a live guard on recent derived re-entry, not as a frozen historical tag.

## before / trip / recovery Reading

- before
  - `observed_but_outside_window`
  - derived residue exists in history, but not inside the active recent window
- trip
  - `observed_recently`
  - a fresh sandbox-only derived row brings the residue back into the active recent window
- recovery
  - `observed_but_outside_window`
  - later bounded primary-only refresh pushes that derived row back out again

## What This Does NOT Prove

This does not prove:

- global validation
- clean-balanced promotion
- a full causality model for why derived rows appear
- a main-runtime state change
- production-scale recovery behavior

The recovery check used bounded clone-style rows inside a sandbox runtime.
That proves loop behavior.
It does not prove full production causality.

## Why Main Runtime Must Remain Untouched

The trip and recovery both require temporary re-entry of derived residue into the recent window.

Doing that in the main runtime would contaminate the current append-only history and would blur the official reading.
So this test must stay sandbox-only.

## Reopen Conditions

Reopen this note if any of the following happens:

- a real derived refresh re-enters the recent window in the main runtime
- the current `robust_decay` weakens or becomes window-sensitive
- primary-only refresh no longer pushes derived residue back outside the active window
- a genuinely independent new primary path changes the overall balance materially
- the line moves from mixed overall toward a truly clean-balanced state
