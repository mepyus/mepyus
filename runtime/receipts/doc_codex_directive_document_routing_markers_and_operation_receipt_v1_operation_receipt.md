# operation receipt / doc_codex_directive_document_routing_markers_and_operation_receipt_v1

## 1. Source
- doc_id: `doc_codex_directive_document_routing_markers_and_operation_receipt_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/source_assets/directives/codex_directive_document_routing_markers_and_operation_receipt_v1.md`

## 2. Raw Routing Markers
- DOCROLE: `directive`
- RUNMODE: `ingest_then_execute`
- PRIORITY: `high`

## 3. Normalized Routing
- docrole: `directive`
- runmode: `ingest_then_execute`
- priority: `high`

## 4. Registration
- input_class: `structured_internal_doc`
- processing_profile: `execution_coupled`
- material_grade: `grade_a`
- role: `directive`
- execution_linkable: `true`
- label_packet: `runtime/manifests/label_packets/doc_codex_directive_document_routing_markers_and_operation_receipt_v1_label_packet.json`

## 5. Ticket
- ticket_id: `tkt_process_codex_directive_document_routing_markers_and_operation_receipt_v1`
- ticket_created: `yes`

## 5A. Run Identity
- run_id: `run_20260403_161911_449139_9df83980_b444fc`
- idempotency_key: `1a59559e909d860b`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_codex_directive_document_routing_markers_and_operation_receipt_v1_label_packet.json` [evt_20260403_161911_77724c0b]
- `doc_registered` -> `source_assets/directives/codex_directive_document_routing_markers_and_operation_receipt_v1.md` [evt_20260403_161911_933303d4]
- `routing_normalized` -> `source_assets/directives/codex_directive_document_routing_markers_and_operation_receipt_v1.md` [evt_20260403_161911_b3ddbc4b]
- `ticket_created` -> `runtime/manifests/ticket_registry_v1.json` [evt_20260403_161911_86ad639e]
- `execution_started` -> `source_assets/directives/codex_directive_document_routing_markers_and_operation_receipt_v1.md` [evt_20260403_161911_9d5830b3]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_codex_directive_document_routing_markers_and_operation_receipt_v1_20260403_161911.md` [evt_20260403_161911_5e2270bd]
- `output_generated` -> `runtime/views/multi_lens_document_reading/doc_codex_directive_document_routing_markers_and_operation_receipt_v1_multi_lens_readout_codex_directive_document_routing_markers_and_operation_receipt_v1_20260403_161911.json` [evt_20260403_161911_84d20dd5]
- `file_created` -> `runtime/manifests/origin_maps/doc_codex_directive_document_routing_markers_and_operation_receipt_v1_receipt_seed_origin_map.json` [evt_20260403_161911_3a6d7dc7]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_codex_directive_document_routing_markers_and_operation_receipt_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_codex_directive_document_routing_markers_and_operation_receipt_v1_20260403_161911.json`
- `app/work/observer_ingest_min/generated/split_units_codex_directive_document_routing_markers_and_operation_receipt_v1_20260403_161911.json`
- `app/work/observer_ingest_min/generated/processing_trace_codex_directive_document_routing_markers_and_operation_receipt_v1_20260403_161911.json`
- `app/work/observer_ingest_min/generated/readable_input_board_codex_directive_document_routing_markers_and_operation_receipt_v1_20260403_161911.md`
- `app/work/observer_ingest_min/generated/operator_summary_codex_directive_document_routing_markers_and_operation_receipt_v1_20260403_161911.md`
- `runtime/views/multi_lens_document_reading/doc_codex_directive_document_routing_markers_and_operation_receipt_v1_multi_lens_readout_codex_directive_document_routing_markers_and_operation_receipt_v1_20260403_161911.json`
- `runtime/manifests/origin_maps/doc_codex_directive_document_routing_markers_and_operation_receipt_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260403_161911_449139_9df83980_b444fc.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc source_assets/directives/codex_directive_document_routing_markers_and_operation_receipt_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/source_assets/directives/codex_directive_document_routing_markers_and_operation_receipt_v1.md --label codex_directive_document_routing_markers_and_operation_receipt_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-04-03T16:19:11+09:00`
- summary: `document routed, registered, recorded, and receipt written`
