# Phase 1.21 Flow-Aware Operating Rule Note v0

## Purpose

This note fixes a provisional operating rule for reader-side flow-aware selection without turning it into a global default.

## Flow-Aware Selection Allow Rule

Flow-aware selection may be allowed only when all of the following are true.

1. the family is on the provisional allow-list
2. `flow_support` survives independently enough to change reread focus
3. carry-forward behaves as an actual reroute handle
4. the new local slice is narrower and more useful than default reread focus

Current allow-list:

- `route_selection`
- `operating_cell`

## Flow-Aware Selection Deny Rule

Do not allow flow-aware selection when:

- the family is compact/title-only
- the family is preprocess comparison
- flow-aware does not change reread focus materially
- carry-forward remains mostly formal
- the only justification is that the document or filename “looks like” flow

## Default Maintain Rule

Keep default selection when one of the following is true.

1. flow already survives in default and tuning adds little
2. boundary/change remain the stronger and more honest reread handle
3. flow-aware adds branching without practical narrowing

Current default-sufficient candidates:

- `input_layer_wrapper`
- `raw_intake_gap`
- `general_line_vs_flow`

## Carry-Forward Handle Operating Attitude

### actual reroute handle

Meaning:

- selection change moves reread to a better local slice
- flow-aware may be allowed if the other gates also pass

### stable but low-value handle

Meaning:

- the ref is real and bounded
- but tuning does not buy enough extra value
- keep default unless future evidence changes this

### mostly formal ref

Meaning:

- the ref exists only as bookkeeping
- do not use it as justification for flow-aware selection

## How To Read Family-Local Only

`family-local only` does not mean flow is weak.

It means:

- the family already carries usable flow
- default selection already lands there
- tuning is not needed to expose it

So `family-local only` should not be read as an allow-list entry.
It is closer to “default is already sufficient.”

## Why Default-Sufficient Must Not Be Misread

`default-sufficient` does not mean:

- flow is absent
- flow is weak everywhere

It means:

- current bounded tuning does not improve the reread enough to justify a mode change

That distinction matters most for:

- `input_layer_wrapper`
- `general_line_vs_flow`

## Current Carry-Forward Table

| Family | Carry-forward class | Operating stance |
| --- | --- | --- |
| route_selection | actual reroute handle | flow-aware eligible |
| operating_cell | actual reroute handle | flow-aware eligible |
| input_layer_wrapper | stable but low-value handle | keep default |
| general_line_vs_flow | stable but low-value handle | keep default |
| raw_intake_gap | mostly formal ref | keep default |
| preprocess_builder | mostly formal ref | block flow-aware |
| preprocess_jung | mostly formal ref | block flow-aware |
| compact_title_only | mostly formal ref | block flow-aware |

