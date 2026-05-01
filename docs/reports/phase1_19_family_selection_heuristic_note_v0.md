# Phase 1.19 Family Selection Heuristic Note v0

## Provisional Family Selection Defaults

### Keep default selection

- `raw_intake_gap`
- `preprocess_builder`
- `preprocess_jung`
- `compact_title_only`

Reason:

- flow-aware selection did not improve reread focus
- default already preserves the actually useful signal

### Allow bounded flow-aware selection

- `route_selection`
- `operating_cell`

Reason:

- default missed a flow-bearing local slice
- flow-aware selection surfaced independent reread value
- carry-forward refs helped reroute the local slice

### Default is already sufficient; no immediate tuning value

- `input_layer_wrapper`
- `general_line_vs_flow`

Reason:

- flow already survives in default
- flow-aware selection does not materially improve the reread

## Flow-Aware Allow Conditions

All should remain bounded.

1. `flow_support` must be `has_signal` or at least meaningful `thin`
2. flow-aware selection must narrow reread focus beyond default
3. carry-forward refs must help reroute or stabilize the new local slice
4. family must show either:
   - repeated flow-bearing local slices, or
   - a demonstrated miss under default selection

## Flow-Aware Disallow Conditions

- compact/title-only family
- preprocess family without explicit new flow survival
- raw_intake_gap family in current state
- any case where flow-aware does not change reread focus
- any case where carry-forward remains mostly formal
- any case justified only by filename/family intuition

## Families That Still Need Recheck

- `general_line_vs_flow`
  - flow survives, but only thinly
  - needs another pass to see if this should stay default-stable rather than flow-oriented
- `input_layer_wrapper`
  - default already does well
  - recheck only if future selection tuning starts to disturb stable default behavior

## Practical Bounded Rule

Current small rule:

- keep `default` as the global baseline
- open `flow-aware` only for families that have already shown `selection-dependent independent` behavior
- do not expand the allow-list until another bounded reread round confirms it

