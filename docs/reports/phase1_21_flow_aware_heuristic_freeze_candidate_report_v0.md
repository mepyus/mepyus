# Phase 1.21 Flow-Aware Heuristic Freeze Candidate Report v0

## Verdict

PASS_WITH_NOTE

## Current Phase Summary

Phase 1.17 to 1.20 established four stable observations.

1. `boundary` and `change + boundary` are already real reread handles.
2. `flow` is not globally weak, but it is not globally useful either.
3. the main bottleneck is reader-side selection pressure plus family distribution, not a broad emitter failure.
4. flow-aware selection can now be discussed as a bounded operating rule, not a universal mode.

This report does not freeze the whole heuristic system.
It separates:

- what can be frozen provisionally now
- what should remain unresolved

## Provisional Allow-List

- `route_selection`
- `operating_cell`

### Why

- both showed `selection-dependent independent` flow survival
- both passed stricter gated flow-aware selection
- both used carry-forward as an actual reroute handle
- in both, flow-aware selection changed reread focus materially rather than merely rephrasing the same local read

## Provisional Block-List

- `preprocess_builder`
- `preprocess_jung`
- `compact_title_only`

### Why

- flow-aware selection added no practical reread value
- carry-forward remained mostly formal
- default already preserved the most honest bounded reread
- bias risk outweighed gain

## Provisional Default-Sufficient List

- `input_layer_wrapper`
- `raw_intake_gap`
- `general_line_vs_flow`

### Why

- `input_layer_wrapper`
  - flow already survives in default
  - tuning adds little beyond what is already selected
- `raw_intake_gap`
  - default preserves the actually useful boundary reread
  - flow-aware does not materially improve focus
- `general_line_vs_flow`
  - flow survives only thinly
  - tuning does not currently buy enough extra value

## Unresolved List

- `raw_intake_gap`
- `general_line_vs_flow`
- `conditional-only` bucket itself

### Why These Stay Unresolved

- `raw_intake_gap`
  - looks default-sufficient now
  - but could still drift toward block-list if later rounds show that flow-aware mainly adds noise
- `general_line_vs_flow`
  - looks default-sufficient now
  - but thin flow survival leaves open whether this should later split into a conditional-only case
- `conditional-only`
  - currently cleanly empty
  - but likely empty because the sample set does not yet force a middle bucket strongly enough

## Family-by-Family Short Basis

### route_selection

- current status: `allow-list`
- short basis:
  - default misses the flow-bearing local slice
  - flow-aware reroutes successfully

### operating_cell

- current status: `allow-list`
- short basis:
  - same pattern as route_selection
  - actual flow survival appears only when selection pressure is changed

### input_layer_wrapper

- current status: `default-sufficient`
- short basis:
  - flow already survives in default
  - tuning is unnecessary

### general_line_vs_flow

- current status: `default-sufficient`, but unresolved boundary remains
- short basis:
  - thin flow survives
  - tuning does not materially improve the read

### raw_intake_gap

- current status: `default-sufficient`, but unresolved boundary remains
- short basis:
  - boundary remains the honest useful signal
  - flow-aware does not help enough yet

### preprocess_builder / preprocess_jung

- current status: `block-list`
- short basis:
  - current value stays in `change + boundary`
  - flow-aware adds no survival

### compact_title_only

- current status: `block-list`
- short basis:
  - remains traceable emptiness in all modes

## What Can Be Frozen Now

### Can be provisionally frozen now

- allow-list:
  - `route_selection`
  - `operating_cell`
- block-list:
  - `preprocess_builder`
  - `preprocess_jung`
  - `compact_title_only`
- carry-forward handle classes:
  - `actual reroute handle`
  - `stable but low-value handle`
  - `mostly formal ref`

### Should not be frozen yet

- `raw_intake_gap` exact placement
- `general_line_vs_flow` exact placement
- whether `conditional-only` should remain empty

