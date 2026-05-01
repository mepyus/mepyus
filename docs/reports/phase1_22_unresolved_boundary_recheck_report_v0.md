# Phase 1.22 Unresolved Boundary Recheck Report v0

## Verdict

PASS_WITH_NOTE

## Scope

This round rechecked unresolved boundaries only.

Included:

- `raw_intake_gap`
- `general_line_vs_flow`
- `input_layer_wrapper`
- `conditional-only` bucket itself

Excluded on purpose:

- allow-list expansion
- block-list expansion
- emitter tuning
- broad family sweep

## Unresolved Family A/B Comparison

### 1. raw_intake_gap

- A: current default
  - `boundary`
  - flow judgment: `no clear added value`
- B: bounded flow-aware
  - same practical outcome
  - flow judgment: `no clear added value`

Recheck result:

- current status stays closer to `keep default-sufficient`
- no new evidence pushes this family toward `conditional-only`
- it does not yet justify `move toward block-list`, but it stays weak

Carry-forward:

- still closest to `mostly formal ref`

### 2. general_line_vs_flow

- A: current default
  - `boundary + flow`
  - flow judgment: `independent value`
- B: bounded flow-aware
  - materially same practical outcome
  - flow judgment: `independent value`

Recheck result:

- this still does **not** justify turning on a separate flow-aware mode
- default already lands on the useful local slice
- the family remains closest to `keep default-sufficient`
- but it still keeps the strongest unresolved pressure toward a future `conditional-only` bucket

Carry-forward:

- still closest to `stable but low-value handle`

### 3. input_layer_wrapper

- A: current default
  - `flow`
  - flow judgment: `independent value`
- B: bounded flow-aware
  - same practical outcome
  - flow judgment: `independent value`

Recheck result:

- this should remain `protect as default-sufficient`
- not because flow is weak
- but because tuning buys almost nothing while increasing the chance of misclassification later

Carry-forward:

- still useful, but the family does not need flow-aware rerouting to expose the useful slice
- operationally it stays closest to `stable but low-value handle`, with occasional reroute usefulness

## raw_intake_gap Decision

Current closest category:

- `keep default-sufficient`

Why:

- default continues to preserve the only clearly useful reread surface: boundary
- flow-aware does not help
- current evidence still does not show enough overreach risk to force a move toward block-list

What changed from prior round:

- nothing materially changed
- that stability itself is evidence that this family should remain default-first for now

## general_line_vs_flow Decision

Current closest category:

- `conditional-only candidate` pressure exists
- but final current placement remains `keep default-sufficient`

Why:

- flow survives independently
- but default already exposes that survival
- bounded flow-aware does not produce a better reread than default

So:

- this family is the strongest unresolved middle case
- but not strong enough yet to justify opening the conditional-only bucket

## input_layer_wrapper Protection Rule

Current closest category:

- `protect as default-sufficient`

Why:

- flow already survives in default
- future tuning could wrongly read this as an allow-list case simply because flow exists
- that would be a mistake because the real gain from tuning is too small

Protection rule:

- do not promote this family into flow-aware allow-list unless a future round shows default actually missing a better local slice

## Conditional-Only Bucket: Current Interpretation

Current best reading:

- **provisionally empty but structurally keep open**

Why not “truly empty”:

- `general_line_vs_flow` still leans toward a middle case

Why not “already populated”:

- no current family needs conditional gating more than it needs either default or allow-list treatment

So the bucket should stay:

- empty in current operating rule
- open in conceptual structure

## Carry-Forward Recheck

### actual reroute handle

No unresolved family moved up into this class.

### stable but low-value handle

- `general_line_vs_flow`
- `input_layer_wrapper` operationally stays closest to this class in current rule

### mostly formal ref

- `raw_intake_gap`

## What Can Now Be Locked More Confidently

- `input_layer_wrapper` as `protect as default-sufficient`
- `raw_intake_gap` as current `keep default-sufficient`
- `conditional-only` as structurally open but currently empty

## What Still Cannot Be Fully Locked

- `general_line_vs_flow` final placement
  - it still sits on the edge between default-sufficient and a possible future conditional-only bucket

## Broad-Tuning Guard

This round did not reopen broad tuning.

- only unresolved families were rechecked
- existing allow-list and block-list were not rewritten
- no lower or schema work was reintroduced

