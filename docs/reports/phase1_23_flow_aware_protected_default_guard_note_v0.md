# Phase 1.23 Flow-Aware Protected Default Guard Note v0

## Purpose

This note fixes the protection rule for families where flow is real but bounded tuning should still not be turned on.

## Protected Default-Sufficient Family

- `input_layer_wrapper`

## Why `input_layer_wrapper` Stays Protected

`input_layer_wrapper` is not weak.
Flow survives in the family.
The issue is different:

- default already exposes the useful local slice
- bounded flow-aware selection adds little
- future tuning could misread “flow exists” as “flow-aware eligible”

That move would be incorrect.

## Guard Wording

Use the following operating attitude.

- keep default selection
- do not promote this family into the allow-list unless default begins missing a better local slice
- do not treat stable carry-forward as reroute permission by itself
- do not read independent flow survival as a tuning requirement

## Why This Is Different From `general_line_vs_flow`

`general_line_vs_flow` still carries unresolved middle pressure.

`input_layer_wrapper` does not.

The difference is:

- `general_line_vs_flow`
  - thin flow survival keeps open a future `conditional-only` question
- `input_layer_wrapper`
  - flow is already surfaced well enough by default
  - the main risk is over-tuning, not under-reading

## Stable But Low-Value Handle: Misread Guard

`stable but low-value handle` does not mean:

- hidden allow-list pressure
- pending reroute opportunity
- tuning should be tried just because the ref is usable

It means:

- the handle is real
- the handle is bounded
- the handle does not buy enough extra reread value to justify mode change

This is the correct reading for `input_layer_wrapper`.

## Future Tuning Guard

Do not reopen this family just because:

- flow survives in default
- carry-forward exists
- the family looks structurally flow-shaped

Reopen only if future evidence shows:

- default repeatedly misses a better local slice, and
- bounded flow-aware selection adds material narrowing beyond current default behavior
