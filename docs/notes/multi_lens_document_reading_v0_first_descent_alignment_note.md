# multi_lens_document_reading_v0 first descent alignment note

## verdict

- first descent package alignment is applied
- this turn does not refine heuristics or introduce maturity logic
- current code now exposes line definition access, reading execution, and readout surface more explicitly

## what was aligned

### line definition access

- line registry access is now formalized through `LineDefinition`
- primary stable/thick lenses and secondary candidate/thin lenses are separated as explicit definition objects
- parked state is made explicit at line-definition level for `line_transition_over_surface`

### reading execution

- `MultiLensDocumentReader.read()` remains the execution entrypoint
- execution still produces `SegmentLineReading` and `DocumentLineLensingResult`
- execution does not assign promotions, reopen states, or maturity outcomes

### result surface

- `MultiLensReadoutFormatter` is introduced as a readout adapter layer
- surfaced output now carries `operating_state` and `is_primary_lens`
- parked-axis visibility is explicit in surfaced output without changing runtime decision scope

### operating decision boundary

- operating state is visible in code and readout, but runtime does not infer decisions from reading result
- parked output is allowed to appear without being treated as failure
- runtime still stops at readout/handoff boundary

## concrete code locations

- line definition access
  - `app/core/runtime/multi_lens_document_reading.py`
  - `LineDefinition`
  - `_load_line_definitions()`
  - `_line_definition_from_registry()`

- reading execution
  - `app/core/runtime/multi_lens_document_reading.py`
  - `MultiLensDocumentReader.read()`
  - `_apply_lens()`
  - `_apply_transition_over_surface_lens()`

- result surface
  - `app/core/runtime/multi_lens_document_reading.py`
  - `SurfacedLineReadout`
  - `SurfacedDocumentReadout`
  - `MultiLensReadoutFormatter`
  - `surface_readout()`

## what was not changed

- no heuristic refinement
- no scoring layer
- no candidate promotion
- no auto state transition
- no maturity judgment
- no reopen automation

## remaining blend check

- `multi_lens_document_reading.py` still contains line-definition access, execution, and readout classes in one file
- however, responsibilities are now named and separated by object/method boundary
- current file does not perform operating decision logic
- current scripts are still operator-facing utilities, not decision layers

## next step

- if later needed, line-definition access and readout formatter can be moved into separate modules without changing current boundaries
