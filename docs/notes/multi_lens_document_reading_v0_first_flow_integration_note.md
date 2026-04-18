# multi_lens_document_reading_v0 first flow integration note

## verdict

- first thin runtime invocation is connected
- `multi_lens_document_reading_v0` is now called from the broader structured-doc flow
- runtime still stops at readout/handoff boundary

## concrete invocation placement

- call site:
  - `scripts/process_structured_doc_with_routing.py`
- placement:
  - after observer ingest output exists
  - after split units are converted into `Segment`
  - after `context_linked_segmentation_v0` runs inside the integration helper
  - before any supervisor-side interpretation

## actual flow in code

1. structured-doc routing runs observer ingest
2. split units path is resolved
3. `build_multi_lens_observation_payload()` is called
4. helper performs:
   - split-unit to `Segment` conversion
   - `ContextLinkedSegmenter.link()`
   - `MultiLensDocumentReader.read()`
   - `surface_readout()`
5. runtime writes one observation artifact
6. handoff boundary is recorded in payload and event note

## handoff boundary

- raw reading result and surfaced readout are produced
- parked axis is visible in surfaced output
- runtime does not promote state, reopen axis, or make maturity decisions
- next owner is supervisor/docs/operating loop

## behavior scope

- no heuristic change
- no scoring
- no candidate promotion
- no auto state transition
- no maturity judgment
- no hidden decision logic
