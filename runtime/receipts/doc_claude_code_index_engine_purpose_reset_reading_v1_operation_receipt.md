# operation receipt / doc_claude_code_index_engine_purpose_reset_reading_v1

## 1. Source
- doc_id: `doc_claude_code_index_engine_purpose_reset_reading_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/claude_code_index_engine_purpose_reset_reading_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_claude_code_index_engine_purpose_reset_reading_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_184229_998675_d7dc70cc_a64e77`
- idempotency_key: `06ca16838780418a`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_claude_code_index_engine_purpose_reset_reading_v1_label_packet.json` [evt_20260328_184230_78e84058]
- `doc_registered` -> `docs/reports/claude_code_index_engine_purpose_reset_reading_v1.md` [evt_20260328_184230_9c7a8705]
- `routing_normalized` -> `docs/reports/claude_code_index_engine_purpose_reset_reading_v1.md` [evt_20260328_184230_d8f04c7e]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_claude_code_index_engine_purpose_reset_reading_v1_20260328_184230.md` [evt_20260328_184231_6d99c191]
- `file_created` -> `runtime/manifests/origin_maps/doc_claude_code_index_engine_purpose_reset_reading_v1_receipt_seed_origin_map.json` [evt_20260328_184231_340ebd3a]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_claude_code_index_engine_purpose_reset_reading_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_claude_code_index_engine_purpose_reset_reading_v1_20260328_184230.json`
- `app/work/observer_ingest_min/generated/split_units_claude_code_index_engine_purpose_reset_reading_v1_20260328_184230.json`
- `app/work/observer_ingest_min/generated/processing_trace_claude_code_index_engine_purpose_reset_reading_v1_20260328_184230.json`
- `app/work/observer_ingest_min/generated/readable_input_board_claude_code_index_engine_purpose_reset_reading_v1_20260328_184230.md`
- `app/work/observer_ingest_min/generated/operator_summary_claude_code_index_engine_purpose_reset_reading_v1_20260328_184230.md`
- `runtime/manifests/origin_maps/doc_claude_code_index_engine_purpose_reset_reading_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_184229_998675_d7dc70cc_a64e77.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/claude_code_index_engine_purpose_reset_reading_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/claude_code_index_engine_purpose_reset_reading_v1.md --label claude_code_index_engine_purpose_reset_reading_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T18:42:31+09:00`
- summary: `document routed, registered, recorded, and receipt written`
