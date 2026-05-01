# Phase 1.30 Flow-Aware Map Recheck and Manualization Note v0

## Verdict

PASS_WITH_NOTE

The current flow-aware map is coherent enough to operate.

The main question is no longer structure formation.
It is whether each layer should now be treated as:

- operator manual
- reference index
- trigger-only guard
- still unresolved

## Current Map Recheck

### 1. Entry layer

Current documents:

- `phase1_25_flow_aware_operating_entrypoint_v0.md`
- `phase1_25_flow_aware_reader_operator_index_v0.md`
- `phase1_25_flow_aware_trigger_checklist_v0.md`

Status:

- coherent
- readable in sequence
- ready for manual-like use

Current role:

- tells reader/operator where to start
- tells them the current placement
- tells them when not to reopen

### 2. Rule layer

Current documents:

- `phase1_23_flow_aware_operating_map_v0.md`
- `phase1_23_flow_aware_protected_default_guard_note_v0.md`
- `phase1_23_flow_aware_unresolved_hold_note_v0.md`

Status:

- strong enough as reference rule set
- not ideal as first entry surface

Current role:

- detailed rule explanation
- placement nuance
- protected/default/unresolved separation

### 3. Reopen control layer

Current documents:

- `phase1_26_flow_aware_reopen_path_map_v0.md`
- `phase1_27_flow_aware_evidence_log_template_v0.md`
- `phase1_27_flow_aware_reopen_permission_boundary_v0.md`
- `runtime/reopen_evidence_logs/flow_aware/README.md`

Status:

- coherent
- strongly bounded
- ready for trigger-only use

Current role:

- blocks broad reopen
- routes bounded reopen
- fixes log shape and landing path

### 4. Index / integration layer

Current documents:

- `phase1_26_flow_aware_cross_reference_note_v0.md`
- `phase1_26_flow_aware_runtime_index_connection_v0.md`
- `phase1_27_flow_aware_master_index_integration_note_v0.md`
- `phase1_28_flow_aware_master_index_merge_note_v0.md`
- `docs/policies/codex_material_and_operation_docs_index_v1.md`

Status:

- enough for discovery
- slightly dense for day-to-day use

Current role:

- tells the system where the flow-aware set lives in the larger operating document tree

## What Is Manualizable Now

### A. Operator start manual

This can be manualized now.

Reason:

- entry sequence is already stable
- no unresolved nuance is needed for first read

Manual candidate:

- “open these three docs in order”
- entrypoint
- reader/operator index
- trigger checklist

### B. Family mode quick manual

This can be manualized now.

Reason:

- family placements are already frozen enough for operation

Manual candidate:

- allow-list families
- block-list families
- keep default
- protect default
- unresolved pressure family

### C. Trigger decision manual

This can be manualized now.

Reason:

- trigger checklist and permission boundary are already explicit

Manual candidate:

- no trigger -> stop
- trigger -> check path map
- bounded reopen only

### D. Evidence log writing manual

This can be manualized now.

Reason:

- storage path exists
- filename rule exists
- template exists
- dry-run already checked first-use friction

Manual candidate:

- when to write
- where to write
- how to name the file
- what fields must appear
- what must not appear

## What Should Stay Reference-Only

### A. Protected default nuance

Keep as reference-first, not operator-front manual.

Reason:

- `input_layer_wrapper` protection logic is stable
- but too much nuance for first-entry quick use

Best place:

- guard note
- linked from index, not frontloaded into a short manual

### B. Carry-forward classification explanation

Keep as compact reference, not long manual.

Reason:

- the 3-way split is stable
- but detailed interpretation belongs behind the quick manual

Best use:

- short table in manual
- full meaning in supporting reference

## What Should Not Be Manualized Yet

### A. `general_line_vs_flow` final handling

Do not over-manualize.

Reason:

- current position is operationally usable
- but still unresolved enough that a too-strong manual would overstate certainty

### B. `conditional-only` bucket usage

Do not manualize as if it were an active bucket.

Reason:

- structurally open
- operationally empty

### C. future reopen decision patterns

Do not manualize beyond bounded trigger procedure.

Reason:

- this would drift back into speculative design

## Recommended Manual Split

The map now supports three manual surfaces.

### 1. Start manual

Audience:

- operator
- Codex

Scope:

- where to begin
- what order to read

### 2. Family mode card

Audience:

- reader
- operator

Scope:

- which family gets which mode

### 3. Trigger-and-log card

Audience:

- operator
- Codex handling a possible reopen

Scope:

- trigger check
- reopen path
- evidence log creation

## Recommended Next Documentation Move

If manualization is wanted, do not create a new design package.

Create only:

1. a short operator start manual
2. a short family mode card
3. a short trigger-and-log card

Everything else should remain in reference notes.

## Current Judgment

The map itself does not need restructuring.

What it needs is selective manualization:

- front-surface operation steps
- family lookup
- trigger/log procedure

Not:

- unresolved nuance
- future tuning logic
- broad reopen reasoning
