# Phase 1.20 Flow-Aware Gating Freeze Candidate Note v0

## Provisional Allow-List

- `route_selection`
- `operating_cell`

Reason:

- both showed selection-dependent independent flow survival
- both passed the stricter gated mode
- both used carry-forward as an actual reroute handle

## Provisional Conditional-Only List

None cleanly promoted yet.

Reason:

- no family currently needs a true middle bucket more than it needs either allow-list or default-sufficient treatment

## Provisional Default-Sufficient List

- `input_layer_wrapper`
- `general_line_vs_flow`
- `raw_intake_gap`

Reason:

- either flow already survives in default
- or flow-aware selection adds no useful improvement

## Provisional Block-List

- `preprocess_builder`
- `preprocess_jung`
- `compact_title_only`

Reason:

- flow-aware adds little practical value
- default preserves the boundedly honest reread better
- bias risk is higher than gain

## Could Be Frozen Soon

- allow-list candidate:
  - `route_selection`
  - `operating_cell`
- block-list candidate:
  - preprocess family
  - compact/title-only

## Needs One More Round Before Freeze

- `raw_intake_gap`
  - still default-sufficient, but only weakly
- `general_line_vs_flow`
  - thin flow survives, but tuning does not help enough yet

## Practical Provisional Rule

1. keep global default
2. allow bounded flow-aware only on provisional allow-list
3. keep preprocess + compact families blocked
4. treat default-sufficient families as “do not tune unless a new round shows real gain”

