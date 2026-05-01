# Phase 1.18 Selection Pressure Validation Report v0

## Verdict

PASS_WITH_NOTE

## Scope

This package validated selection pressure only.

- no emitter change
- no schema change
- no classifier change
- no lens naming
- no axis naming

The question was whether default selection was hiding flow-rich local slices.

## Trial Modes

- A: `default selection`
- B: `flow-preferred selection`
- optional support check:
  - explicit seed selection was already used in Phase 1.17 to verify local flow-rich slices

Mode B still used the same lower artifacts. It only changed which seed/camera pair the bounded reread note consumed first.

## Artifact Set

Base set:

1. observer/review: `route_selection_policy_v0`
2. observer/report: `raw_intake_gap_analysis_before_middle_layer_fix_v1`
3. preprocess comparison: `builder_choi_interview`
4. preprocess comparison: `codex_ambassader_jung`
5. compact/title-only: `middle_layer_thickening_program_instruction_v1`

Route-selection-external families intentionally added:

6. `input_layer_wrapper_core_link_note_v1`
7. `general_line_vs_flow_candidate_v0`
8. `vectorfl_paper_operating_cell_schema_v0`

Also inspected but not used as a positive flow-rich case:

- `codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1`
  - flow survival did not surface in the emitted camera rows

## Selection Mode Comparison Table

| Artifact / family | Default selection | Flow-preferred selection | Family judgment |
| --- | --- | --- | --- |
| route_selection | boundary-led, flow absent | flow survives, reread narrows | selection-dependent independent |
| raw_intake_gap | boundary-led, flow absent | still no flow survival | no meaningful survival |
| builder preprocess | change+boundary, flow absent | still no flow survival | no meaningful survival |
| jung preprocess | change+boundary, flow absent | still no flow survival | no meaningful survival |
| compact/title-only | emptiness trace | emptiness trace | no meaningful survival |
| input_layer_wrapper | flow already survives in default | flow still survives | family-local only |
| general_line_vs_flow | thin flow already survives in default | same thin flow survival | family-local only |
| operating_cell_schema | default misses flow slice | flow-preferred finds independent flow | selection-dependent independent |

## Artifact / Family Comparison

### 1. route_selection_policy_v0

- default:
  - reread focus stayed on boundary-like local wording
  - flow judgment: no clear added value
- flow-preferred:
  - reread focus moved to local sequence / handoff wording
  - flow judgment: independent value
- family judgment:
  - `selection-dependent independent`

Read:
this was not just route_selection being flow-rich. It was route_selection default selection preferring a different local slice.

### 2. raw_intake_gap_analysis_before_middle_layer_fix_v1

- default:
  - boundary survives
- flow-preferred:
  - still no flow survival
- family judgment:
  - `no meaningful survival`

### 3. builder_choi_interview preprocess comparison

- default:
  - change + boundary survive
- flow-preferred:
  - no practical change
- family judgment:
  - `no meaningful survival`

### 4. codex_ambassader_jung preprocess comparison

- default:
  - change + boundary survive
- flow-preferred:
  - no practical change
- family judgment:
  - `no meaningful survival`

### 5. compact/title-only

- default:
  - traceable emptiness
- flow-preferred:
  - traceable emptiness
- family judgment:
  - `no meaningful survival`

### 6. input_layer_wrapper_core_link_note_v1

- default:
  - flow already survives as an independent reread cue
- flow-preferred:
  - same result, with a small carry-forward ref shift
- family judgment:
  - `family-local only`

Read:
here the family itself carries handoff/ordering language strongly enough that default selection already lands on a flow-bearing slice.

### 7. general_line_vs_flow_candidate_v0

- default:
  - flow survives only thinly
- flow-preferred:
  - materially similar result
- family judgment:
  - `family-local only`

Read:
flow is present, but only thinly. Selection pressure does not change the outcome much.

### 8. vectorfl_paper_operating_cell_schema_v0

- default:
  - change + boundary dominate
  - flow absent
- flow-preferred:
  - flow becomes independent and reread focus shifts to sequence/handoff wording
- family judgment:
  - `selection-dependent independent`

Read:
this is the strongest non-route-selection confirmation that selection pressure can hide a real flow cue.

## Route Selection Bias Check

Route selection was not the only positive case.

Non-route-selection evidence:

- `input_layer_wrapper_core_link_note_v1`
  - independent flow survives even in default mode
- `general_line_vs_flow_candidate_v0`
  - thin but real flow survives
- `vectorfl_paper_operating_cell_schema_v0`
  - flow becomes independent only when selection pressure is changed

So the current result is not “route_selection-only bias.”

The more honest reading is:

- some families are naturally flow-bearing
- some families contain flow-bearing local slices that default selection misses
- some families simply do not carry usable flow at this stage

## Carry-Forward Handle Check

### Useful cases

- route_selection flow-preferred
- input_layer_wrapper default / flow-preferred
- operating_cell flow-preferred

Why:

- carry-forward refs stayed bounded
- when selection changed, the carry-forward refs moved with the flow-bearing local slice
- this means the handle was not just formal metadata; it helped point the reread at the new local target

### Weak cases

- preprocess comparison
- compact/title-only
- raw_intake_gap

Why:

- refs stayed stable, but selection changes did not surface stronger flow-bearing local material

## Compact / Title-Only Observation

Compact/title-only remained traceable emptiness in both modes.

That is still the correct result.

Changing selection pressure should not invent flow where the lower artifact does not carry it.

## Current Bottleneck: Emitter or Selection?

Provisional answer:

- not emitter-only
- not family-bias-only
- mostly `selection pressure + family distribution`

Why:

- route_selection and operating_cell both showed flow that default selection missed
- input_layer_wrapper showed a family where flow already survives without special selection
- preprocess and compact families did not improve even under flow-preferred selection

So the present bottleneck is:

1. default selection often prefers non-flow local slices
2. some families truly have little flow to recover

## Why We Are Still Not Modifying the Emitter

If flow-preferred selection had failed everywhere, emitter change would be the next direct move.

That did not happen.

Instead:

- some families improved only when selection pressure changed
- some families already contained usable flow without emitter change

That means the next honest move is still selection-side validation or tuning, not immediate emitter rewriting.

