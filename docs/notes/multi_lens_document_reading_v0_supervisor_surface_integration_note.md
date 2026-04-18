# multi_lens_document_reading_v0_supervisor_surface_integration_note

## verdict

- supervisor-facing multi-lens surface is now exposed as a primary surfaced view
- raw observation artifact remains available as a secondary reference
- runtime still stops before any decision logic

## where this surface now appears

- runtime path:
  - `scripts/process_structured_doc_with_routing.py`
- generated view:
  - `runtime/views/multi_lens_document_reading/*_multi_lens_supervisor_surface_*.json`

## what the supervisor surface contains

- `primary_view = surfaced_readout`
- `line_states`
- `parked_axes`
- `handoff_boundary`
- `raw_output_reference`

## what remains secondary

- full observation artifact
- `linked_segments`
- `raw_reading_result`
- execution-trace internals

즉 supervisor first view는 surfaced readout 중심이고, raw artifact는 reference-only로 남는다.

## behavior boundary

- no decision surface
- no maturity surface
- no promotion signal
- no reopen trigger
- runtime still ends at readout/handoff boundary
