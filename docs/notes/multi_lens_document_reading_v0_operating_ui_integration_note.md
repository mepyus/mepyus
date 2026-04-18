# multi_lens_document_reading_v0_operating_ui_integration_note

## verdict

- multi-lens supervisor surface now appears in the phase1 operating UI observation area
- surfaced readout is the primary panel content
- raw output remains secondary/reference-only

## where the panel appears

- UI entry:
  - `operating-ui-phase1`
- location:
  - `Operating` surface
  - left stack observation area
  - after current run and selected asset/state summaries

## how it should be read

- first read `line_states`
- then read `parked_axes`
- then read surfaced per-reading rows and `reading_basis`
- confirm `handoff_boundary`
- open raw reference only if deeper audit is needed

## what remains secondary

- raw observation artifact path
- deeper artifact link/reference
- full execution-oriented payload

## boundary

- observational only
- not a decision panel
- not a maturity panel
- not a promotion signal
- not a reopen trigger
