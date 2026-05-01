# Phase 1.31 Flow-Aware Family Mode Card v0

## Family Modes

| Family | Mode | Operator meaning |
| --- | --- | --- |
| `route_selection` | bounded flow-aware allowed | allow only when reread focus becomes narrower than default |
| `operating_cell` | bounded flow-aware allowed | same rule as `route_selection` |
| `preprocess_builder` | flow-aware blocked | stay on default reread |
| `preprocess_jung` | flow-aware blocked | stay on default reread |
| `compact_title_only` | flow-aware blocked | treat as bounded emptiness trace |
| `raw_intake_gap` | keep default | boundary remains the honest reread surface |
| `input_layer_wrapper` | protect as default | flow exists, but tuning is not justified |
| `general_line_vs_flow` | default + unresolved pressure | keep default; do not treat thin flow or unresolved pressure as reopen permission by itself |

## Carry-Forward Handle

### actual reroute handle

- may support bounded flow-aware use

### stable but low-value handle

- real handle
- not enough to justify tuning by itself

### mostly formal ref

- not a flow-aware justification

## Default Warning

Do not flatten all default-like families into one class.

- `raw_intake_gap`
  - keep default
- `input_layer_wrapper`
  - protect as default
- `general_line_vs_flow`
  - default plus unresolved pressure

## Quick Rule

- allow-list only where already proven
- block-list stays blocked
- protected default is not a hidden allow-list
- unresolved pressure is not permission to retune
- trigger candidate is not the same thing as actual reopen permission
