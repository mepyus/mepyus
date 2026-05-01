# Phase 1.19 Selection Tuning Small Package Report v0

## Verdict

PASS_WITH_NOTE

## Scope

This package tuned reader-side selection only.

- no lower emitter change
- no schema change
- no classifier change
- no lens / axis / promotion layer

The question was not “find more flow everywhere.”
The question was “when is flow-aware selection actually justified?”

## A/B Comparison Table

| Family | A: default | B: bounded flow-aware | Family verdict |
| --- | --- | --- | --- |
| route_selection | boundary-led reread | flow-led reread | selection-dependent independent |
| raw_intake_gap | boundary-led reread | no practical change | default-stable |
| preprocess_builder | change+boundary reread | no practical change | default-stable |
| preprocess_jung | change+boundary reread | no practical change | default-stable |
| compact_title_only | emptiness trace | emptiness trace | default-stable |
| input_layer_wrapper | flow already survives | same practical outcome | family-local only |
| general_line_vs_flow | thin flow already survives | same practical outcome | family-local only |
| operating_cell | change+boundary reread | flow-led reread | selection-dependent independent |

## Family-by-Family Judgment

### route_selection

- default:
  - `boundary`
  - flow absent
- flow-aware:
  - `flow`
  - focus moved from risk/limit wording to sequence/handoff wording
- verdict:
  - `selection-dependent independent`

### raw_intake_gap

- default:
  - `boundary`
- flow-aware:
  - same practical outcome
- verdict:
  - `default-stable`

### preprocess_builder

- default:
  - `change + boundary`
- flow-aware:
  - same practical outcome
- verdict:
  - `default-stable`

### preprocess_jung

- default:
  - `change + boundary`
- flow-aware:
  - same practical outcome
- verdict:
  - `default-stable`

### compact_title_only

- default:
  - no useful flow survival
- flow-aware:
  - no useful flow survival
- verdict:
  - `default-stable`

### input_layer_wrapper

- default:
  - flow already survives as independent reread cue
- flow-aware:
  - almost same outcome
- verdict:
  - `family-local only`

Interpretation:
This family does not need tuning first. Default already lands on a flow-bearing local slice.

### general_line_vs_flow

- default:
  - thin but independent flow survives
- flow-aware:
  - no material improvement
- verdict:
  - `family-local only`

Interpretation:
There is flow here, but tuning does not buy much right now.

### operating_cell

- default:
  - `change + boundary`
- flow-aware:
  - `flow`
  - focus moves from correction-like reread to sequence/handoff reread
- verdict:
  - `selection-dependent independent`

## Carry-Forward Handle

### Useful as a real reroute handle

- `route_selection`
- `operating_cell`
- `input_layer_wrapper`
- `general_line_vs_flow` (weaker, but still usable)

Observed behavior:

- when flow-aware selection was meaningful, carry-forward refs moved with the selected local slice
- when default already landed on the correct local slice, the handle stayed stable and still usable

### Mostly formal

- `raw_intake_gap`
- `preprocess_builder`
- `preprocess_jung`
- `compact_title_only`

Observed behavior:

- refs remained bounded
- but changing selection pressure did not surface stronger flow-bearing local material

## Why Compact / Title-Only and Preprocess Stay Default-First

### Compact / title-only

- flow-aware selection produces no practical improvement
- the family remains traceable emptiness
- forcing flow-aware here would be pure bias

### Preprocess family

- current reread value comes from `change + boundary`
- flow-aware selection adds no survival
- default is more honest because it preserves the actually useful signal

## Why We Are Still Not Modifying the Emitter

The package result does not support a broad emitter failure claim.

Instead it shows three different cases:

1. families where default already finds usable flow
2. families where flow exists but selection pressure misses it
3. families where flow simply does not survive right now

That is a selection/distribution problem before it is an emission problem.

## Why Selection Tuning Must Stay Bounded

If flow-aware selection becomes global, it will overfit to flow-bearing families and distort default reread behavior.

The current evidence supports only a narrow rule:

- allow flow-aware selection where local flow survival is demonstrated
- keep default elsewhere

That is why this package stays small and family-gated.

