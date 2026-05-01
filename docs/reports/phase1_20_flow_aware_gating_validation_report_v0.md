# Phase 1.20 Flow-Aware Gating Validation Report v0

## Verdict

PASS_WITH_NOTE

## Scope

This package validated reader-side gating only.

- no lower emitter change
- no schema change
- no classifier change
- no lens / axis naming
- no promotion layer

The point was to test whether a stricter gated flow-aware mode can be stated provisionally.

## A / B / C Gating Modes

- A: `current default selection`
- B: `bounded flow-aware selection`
  - prefers flow-bearing local slices when asked
- C: `stricter gated flow-aware selection`
  - B is allowed only when all of the following hold:
    - flow survives independently
    - carry-forward behaves as a real reroute handle
    - reread focus is narrower than A
    - family is not already default-sufficient

If those conditions do not hold, C falls back to A.

## A / B / C Comparison Table

| Family | A | B | C | Provisional class |
| --- | --- | --- | --- | --- |
| route_selection | boundary-led | flow-led | flow-aware accepted | allow-list candidate |
| operating_cell | change+boundary-led | flow-led | flow-aware accepted | allow-list candidate |
| input_layer_wrapper | flow already alive | similar | default kept | default-sufficient |
| general_line_vs_flow | thin flow already alive | similar | default kept | default-sufficient |
| raw_intake_gap | boundary-led | no useful improvement | default kept | default-sufficient |
| preprocess_builder | change+boundary-led | no useful improvement | default kept | block-list candidate |
| preprocess_jung | change+boundary-led | no useful improvement | default kept | block-list candidate |
| compact_title_only | emptiness trace | emptiness trace | default kept | block-list candidate |

## Family-by-Family Provisional Judgment

### allow-list candidate

#### route_selection

- B improved focus from boundary wording to sequence / handoff wording
- carry-forward rerouted the local slice
- C accepted B

Minimum gating conditions observed:

- `flow_strength = has_signal`
- reread focus changed materially
- carry-forward was an actual reroute handle

#### operating_cell

- same pattern as route_selection
- default missed the flow-bearing local slice
- C accepted B

### default-sufficient

#### input_layer_wrapper

- flow already survives in A
- B does not buy enough extra value
- C correctly keeps default

Why not tune:
because tuning would add mode complexity without improving the reread.

#### general_line_vs_flow

- thin flow already survives in A
- B does not improve enough to justify a mode switch
- C correctly keeps default

Why not tune:
because this is “flow exists” rather than “flow-aware selection is needed.”

#### raw_intake_gap

- A keeps the useful boundary reread
- B does not surface meaningful flow
- C correctly keeps default

Why not block outright:
because this looks like a weak-flow family, not a misleading-flow family.

### block-list candidate

#### preprocess_builder

- current value stays in `change + boundary`
- B does not improve reread focus
- C should remain off

#### preprocess_jung

- same pattern as preprocess_builder
- C should remain off

#### compact_title_only

- remains traceable emptiness in all modes
- C should remain off

Why these should be blocked:

- flow-aware adds bias risk
- carry-forward stays mostly formal
- default already preserves the only boundedly honest reread

### conditional-only

No family is being promoted here as a clean conditional-only candidate.

Current reason:

- the families that improved did so strongly enough to sit in allow-list candidate
- the families with thin flow but no practical gain fit better under default-sufficient

## Selection-Dependent Independent Families: Minimum Gating Conditions

Current minimum conditions, based on route_selection and operating_cell:

1. `flow_support` is `has_signal`
2. default mode misses that slice
3. flow-aware mode changes reread focus materially
4. carry-forward reroutes to the new local slice
5. family is not one where default already preserves the best bounded reread

## Why Default-Sufficient Families Should Not Be Tuned

Two patterns showed up:

1. flow already survives in default
2. flow does not survive usefully even when preferred

In both cases, adding tuning produces more branching than value.

That is why:

- `input_layer_wrapper`
- `general_line_vs_flow`
- `raw_intake_gap`

should stay default-first for now.

## Why Block-List Candidates Should Be Blocked

The block-list candidates are not just “weak.”
They are families where flow-aware selection adds little while increasing the chance of reader-side overreach.

That is currently true for:

- preprocess family
- compact/title-only family

## Carry-Forward Handle Classification

### actual reroute handle

- `route_selection`
- `operating_cell`

Meaning:
selection mode changed, and carry-forward moved the reread to a more useful local slice.

### stable but low-value handle

- `input_layer_wrapper`
- `general_line_vs_flow`

Meaning:
the handle is real, but tuning is not needed because default already lands in a usable slice.

### mostly formal ref

- `raw_intake_gap`
- `preprocess_builder`
- `preprocess_jung`
- `compact_title_only`

Meaning:
the handle stays bounded, but it does not materially help reroute toward a stronger flow reread.

## Why We Are Still Not Modifying the Emitter

The gating result still does not support a broad emitter failure claim.

What it supports is narrower:

- some families need flow-aware selection
- some do not
- some should be blocked

That remains a reader-side control problem first.

## What Looks Freezable vs Not Yet Freezable

### Looks close to freeze candidate

- provisional allow-list candidates
- provisional block-list candidates

### Not yet safe to freeze

- whether `raw_intake_gap` should stay default-sufficient or degrade into block-list later
- whether `general_line_vs_flow` needs a conditional-only split instead of default-sufficient

