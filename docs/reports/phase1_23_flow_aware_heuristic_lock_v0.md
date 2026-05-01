# Phase 1.23 Flow-Aware Heuristic Lock v0

## Purpose

This note consolidates the current reader-side flow-aware selection rule into a provisional operating lock.

It does not reopen tuning.
It does not change schema, emitter wording, classifier behavior, or selection logic.

## Current Locked Boundary

### Provisional allow-list

- `route_selection`
- `operating_cell`

Short basis:

- both families showed repeatable `selection-dependent independent` flow survival
- bounded flow-aware selection narrowed reread focus beyond default
- carry-forward behaved as an `actual reroute handle`

### Provisional block-list

- `preprocess_builder`
- `preprocess_jung`
- `compact_title_only`

Short basis:

- flow-aware added no practical reread gain
- useful reread remained `change + boundary` or emptiness trace
- carry-forward stayed `mostly formal ref`
- flow-aware bias risk is higher than gain

### Provisional default-sufficient

- `raw_intake_gap`
- `general_line_vs_flow`

Short basis:

- `raw_intake_gap`
  - default preserves the honest boundary reread
  - flow-aware does not improve focus enough
- `general_line_vs_flow`
  - flow survives, but default already lands on the useful slice
  - tuning does not currently justify a mode change

### Protected default-sufficient

- `input_layer_wrapper`

Short basis:

- flow is real
- default already exposes the useful slice
- tuning adds little and risks misreading this family as allow-list eligible

### Unresolved hold

- `general_line_vs_flow` final placement
- `conditional-only` bucket itself
- `raw_intake_gap` long-term reclassification possibility

Short basis:

- `general_line_vs_flow` still carries middle-bucket pressure
- `conditional-only` is currently empty, but should stay structurally open
- `raw_intake_gap` is stable enough for current default use, but not strong enough for a hard final placement

## Family Basis Table

| Family | Current placement | Basis |
| --- | --- | --- |
| `route_selection` | allow-list | default misses the better flow-bearing slice; gated flow-aware improves reread focus |
| `operating_cell` | allow-list | same pattern as `route_selection`; flow-aware reroute adds real value |
| `preprocess_builder` | block-list | flow-aware adds no useful survival; `change + boundary` remains the honest reread |
| `preprocess_jung` | block-list | same as `preprocess_builder` |
| `compact_title_only` | block-list | remains traceable emptiness across modes |
| `raw_intake_gap` | default-sufficient | boundary stays useful; flow-aware adds no real gain |
| `general_line_vs_flow` | default-sufficient with unresolved pressure | flow survives, but default already captures it |
| `input_layer_wrapper` | protected default-sufficient | flow exists, but tuning is unnecessary and overreads the family |

## What Can Be Locked Now

- provisional allow-list
- provisional block-list
- protected default-sufficient rule for `input_layer_wrapper`
- carry-forward handle classes and their operating meaning
- global default-first stance

## What Is Intentionally Not Locked Now

- final placement of `general_line_vs_flow`
- permanent emptiness of `conditional-only`
- long-term final placement of `raw_intake_gap`

These remain open only as bounded unresolved hold items.
They are not grounds for broad heuristic reopening.
