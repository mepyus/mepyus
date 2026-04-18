# operation receipt / doc_claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1

## 1. Source
- doc_id: `doc_claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1.md`

## 2. Raw Routing Markers
- DOCROLE: ``
- RUNMODE: ``
- PRIORITY: ``

## 3. Normalized Routing
- docrole: `memo`
- runmode: `ingest_only`
- priority: `normal`

## 4. Registration
- input_class: `structured_internal_doc`
- processing_profile: `minimal_preprocess`
- material_grade: `grade_a`
- role: `memo`
- execution_linkable: `false`
- label_packet: `runtime/manifests/label_packets/doc_claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_191115_137437_c47eb567_0e313a`
- idempotency_key: `30bae434ba2cbcdd`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1_label_packet.json` [evt_20260328_191115_ca314215]
- `doc_registered` -> `docs/reports/claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1.md` [evt_20260328_191115_c6ee2a08]
- `routing_normalized` -> `docs/reports/claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1.md` [evt_20260328_191115_11594df4]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1_20260328_191115.md` [evt_20260328_191117_0b2aedee]
- `file_created` -> `runtime/manifests/origin_maps/doc_claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1_receipt_seed_origin_map.json` [evt_20260328_191117_acb4b460]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1_20260328_191115.json`
- `app/work/observer_ingest_min/generated/split_units_claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1_20260328_191115.json`
- `app/work/observer_ingest_min/generated/processing_trace_claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1_20260328_191115.json`
- `app/work/observer_ingest_min/generated/readable_input_board_claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1_20260328_191115.md`
- `app/work/observer_ingest_min/generated/operator_summary_claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1_20260328_191115.md`
- `runtime/manifests/origin_maps/doc_claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_191115_137437_c47eb567_0e313a.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1.md --label claude_code_index_engine_purpose_reset_reading_segmentation_probe_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T19:11:17+09:00`
- summary: `document routed, registered, recorded, and receipt written`
