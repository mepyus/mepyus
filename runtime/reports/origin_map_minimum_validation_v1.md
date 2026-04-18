# origin_map_minimum_validation_v1

## 1. Test Document
- source_doc: `codex_directive_origin_map_minimum_v1.md`
- doc_id: `doc_codex_directive_origin_map_minimum_v1`
- normalized_route: `directive / ingest_then_execute / high`

## 2. Generated Origin Map
- file: `runtime/manifests/origin_maps/doc_codex_directive_origin_map_minimum_v1_receipt_seed_origin_map.json`
- derived_from_kind: `receipt_seed`
- source_locator.type: `char_span`
- heading_path:
  - `codex_directive_origin_map_minimum_v1`
  - `0. 목적`

## 3. Validation Read
- source_doc_id exists
- heading_path exists
- source_locator exists
- source_preview exists
- derived_at exists
- derived_from_kind exists

## 4. Event Trail
- `doc_registered`
- `routing_normalized`
- `ticket_created`
- `execution_started`
- `output_generated`
- `file_created` for origin map seed
- `receipt_written`
- `board_updated`

## 5. Current Judgment
- origin map v1 works as a lightweight source-return handle
- no additional user-side intake burden was added
- v1 is ready for receipt/board later reading
