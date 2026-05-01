# Phase 1.24 Flow-Aware Operator Quick Reference v0

## Default Rule

- keep global default selection
- do not turn on flow-aware selection broadly

## Where Flow-Aware Is Allowed

- `route_selection`
- `operating_cell`

Use bounded flow-aware only when:

- reread focus becomes narrower than default
- flow survives independently enough to matter
- carry-forward behaves like an actual reroute handle

## Where Flow-Aware Is Blocked

- `preprocess_builder`
- `preprocess_jung`
- `compact_title_only`

Operator stance:

- do not force flow-aware mode
- stay with default bounded reread

## Where Default Should Stay

- `raw_intake_gap`
- `general_line_vs_flow`

Operator stance:

- keep default
- do not read thin flow as tuning permission

## Protected Default

- `input_layer_wrapper`

Rule:

- `flow exists` does not mean `flow-aware eligible`
- do not move this family toward allow-list unless default begins missing a better slice

## Carry-Forward Handle Meaning

### actual reroute handle

- usable as flow-aware support

### stable but low-value handle

- real handle
- not enough to justify tuning by itself

### mostly formal ref

- bookkeeping only
- not a tuning signal

## Unresolved Operator Attitude

When a family is unresolved:

- keep current placement
- do not reopen broadly
- wait for explicit trigger evidence

## Do

- keep default as the baseline
- use allow-list only where already proven
- treat protected default separately from ordinary default-sufficient
- read carry-forward class before considering flow-aware use

## Don’t

- do not turn flow-aware into a global habit
- do not use filename intuition as evidence
- do not treat thin flow as reroute permission
- do not use unresolved hold as a reason to restart broad tuning
