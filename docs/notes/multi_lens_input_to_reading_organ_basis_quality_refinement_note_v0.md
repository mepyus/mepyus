# multi_lens_input_to_reading_organ_basis_quality_refinement_note_v0

## verdict

- first bounded basis-quality refinement is applied for `input_to_reading_organ`
- this turn changes basis wording only
- this turn does not change operating state, architecture, or decision boundaries

## what changed

- `input_to_reading_organ` basis generation is now handled by a dedicated helper
- basis wording now distinguishes:
  - direct evidence
  - partial cue
  - low-confidence basis only
- weak explanations are more explicit about why they stayed weak

## what did not change

- no heuristic expansion
- no scoring
- no candidate promotion
- no auto state transition
- no maturity judgment
- `line_input_to_reading_organ` remains `active`
- `line_transition_over_surface` remains `parked`
- runtime still stops at readout/handoff boundary

## intent

- make operator-facing basis wording clearer
- improve evidence-description clarity without reopening promotion or maturity debate
