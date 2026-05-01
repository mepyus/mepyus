# Phase 1.25 Flow-Aware Reader / Operator Index v0

## Family Mode Index

| Family | Base mode | Operating note |
| --- | --- | --- |
| `route_selection` | bounded flow-aware allowed | use only when reread focus becomes narrower than default |
| `operating_cell` | bounded flow-aware allowed | same rule as `route_selection` |
| `preprocess_builder` | flow-aware blocked | stay on default bounded reread |
| `preprocess_jung` | flow-aware blocked | stay on default bounded reread |
| `compact_title_only` | flow-aware blocked | treat as bounded emptiness trace |
| `raw_intake_gap` | keep default | boundary remains the honest reread surface |
| `input_layer_wrapper` | protect as default | flow exists, but tuning is not justified |
| `general_line_vs_flow` | default + unresolved pressure | keep default; do not treat thin flow as tuning permission |

## Carry-Forward Handle Meaning

### actual reroute handle

- can support bounded flow-aware use
- means rerouting can reach a better local slice

### stable but low-value handle

- real ref
- not enough to justify tuning by itself

### mostly formal ref

- bookkeeping ref
- not a flow-aware justification

## Default-Sufficient Warning

Do not read all default-sufficient families with the same weight.

- `raw_intake_gap`
  - keep default
- `input_layer_wrapper`
  - protect as default
- `general_line_vs_flow`
  - default plus unresolved pressure

## Do

- keep global default as the baseline
- use allow-list only where already proven
- check carry-forward class before considering flow-aware use
- keep protected default separate from ordinary default
- keep unresolved items on current placement unless a trigger appears

## Don’t

- do not treat `flow exists` as `flow-aware eligible`
- do not treat thin flow as reroute permission
- do not use filename intuition as evidence
- do not flatten all default-sufficient families into one class
- do not use unresolved pressure as permission for broad tuning
