# multi_lens_document_reading_v0 second descent readout separation note

## verdict

- readout layer is separated at file level
- this turn does not change heuristic behavior or operating-state behavior
- separation was applied to make execution vs surface ownership visible before any further extension

## why readout was separated first

- readout is the safest layer to separate without reopening heuristic or governance questions
- execution and readout had already been separated by object boundary, but not yet by file boundary
- moving readout into its own module makes future supervision clearer while keeping runtime behavior unchanged

## what moved

- `SurfacedLineReadout`
- `SurfacedDocumentReadout`
- `MultiLensReadoutFormatter`
- `surface_readout()`

새 위치:

- `app/core/runtime/multi_lens_document_readout.py`

## what stayed

- line-definition access remains in `multi_lens_document_reading.py`
- reading execution remains in `multi_lens_document_reading.py`
- runtime still stops at readout/handoff boundary

## behavior check

- parked-axis surfaced semantics remain explicit
- active-axis surfaced semantics remain explicit
- current strength distribution is unchanged after extraction
