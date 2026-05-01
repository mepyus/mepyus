# Phase 1.23 Flow-Aware Operating Map v0

## Global Default Rule

Keep reader-side selection on global default.

Do not introduce a global flow-aware default.
Do not treat mere flow presence as flow-aware eligibility.

## Family-Level Operating Map

| Family | Default mode | Flow-aware stance | Reason |
| --- | --- | --- | --- |
| `route_selection` | default first | bounded flow-aware allowed | default can miss a better flow-bearing local slice |
| `operating_cell` | default first | bounded flow-aware allowed | same family shape as `route_selection` |
| `input_layer_wrapper` | default | do not tune; protect default | flow exists, but default is already sufficient |
| `raw_intake_gap` | default | do not tune for now | boundary remains the honest reread handle |
| `general_line_vs_flow` | default | do not tune for now; keep under unresolved pressure | thin flow survives, but no mode change is justified yet |
| `preprocess_builder` | default | flow-aware blocked | tuning adds bias, not value |
| `preprocess_jung` | default | flow-aware blocked | same as `preprocess_builder` |
| `compact_title_only` | default | flow-aware blocked | no useful survival beyond emptiness trace |

## Allow Rule

Bounded flow-aware selection may be used only when all of the following are true.

1. the family is on the provisional allow-list
2. `flow_support` survives independently enough to narrow reread focus
3. carry-forward behaves as an `actual reroute handle`
4. the new local slice is materially narrower or more useful than default

Current allow-list:

- `route_selection`
- `operating_cell`

## Block Rule

Do not use flow-aware selection when one of the following is true.

- the family is on the provisional block-list
- carry-forward remains `mostly formal ref`
- default already exposes the useful reread surface and flow-aware adds no narrowing
- the only reason for switching is filename intuition or generic flow wording

Current block-list:

- `preprocess_builder`
- `preprocess_jung`
- `compact_title_only`

## Default-Sufficient Rule

Default-sufficient does not mean flow is absent.
It means bounded flow-aware selection does not improve reread enough to justify a mode change.

That distinction matters for:

- `raw_intake_gap`
- `general_line_vs_flow`
- `input_layer_wrapper`

## Protected Default-Sufficient Rule

Protected default-sufficient is stronger than ordinary default-sufficient.

Meaning:

- flow is visibly present
- default already lands on the useful slice
- future tuning must not treat this as hidden allow-list pressure

Current protected default-sufficient family:

- `input_layer_wrapper`

## Carry-Forward Handle Operating Meaning

### actual reroute handle

- may justify bounded flow-aware selection
- means selection change can move reread to a better local slice

### stable but low-value handle

- may indicate real flow presence
- does not by itself justify tuning
- default may remain the correct operating choice

### mostly formal ref

- do not use as flow-aware justification
- treat as bookkeeping rather than reread improvement signal

## Why Default-Sufficient Must Not Be Flattened

Do not read all default-sufficient families as the same thing.

- `raw_intake_gap`
  - weak default-sufficient
- `general_line_vs_flow`
  - default-sufficient with unresolved pressure
- `input_layer_wrapper`
  - protected default-sufficient

That difference is part of the operating rule.
