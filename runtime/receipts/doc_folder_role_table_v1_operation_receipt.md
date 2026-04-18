# operation receipt / doc_folder_role_table_v1

## 1. Source
- doc_id: `doc_folder_role_table_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/specs/folder_role_table_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_folder_role_table_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260327_224319_351259_f8af4425_e17c2a`
- idempotency_key: `b5f9cf5ce4500429`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_folder_role_table_v1_label_packet.json` [evt_20260327_224319_93a0ebed]
- `doc_registered` -> `docs/specs/folder_role_table_v1.md` [evt_20260327_224319_708f855c]
- `routing_normalized` -> `docs/specs/folder_role_table_v1.md` [evt_20260327_224319_d283fece]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_folder_role_table_v1_20260327_224319.md` [evt_20260327_224319_0b269b7b]
- `file_created` -> `runtime/manifests/origin_maps/doc_folder_role_table_v1_receipt_seed_origin_map.json` [evt_20260327_224319_293041a6]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_folder_role_table_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_folder_role_table_v1_20260327_224319.json`
- `app/work/observer_ingest_min/generated/split_units_folder_role_table_v1_20260327_224319.json`
- `app/work/observer_ingest_min/generated/processing_trace_folder_role_table_v1_20260327_224319.json`
- `app/work/observer_ingest_min/generated/readable_input_board_folder_role_table_v1_20260327_224319.md`
- `app/work/observer_ingest_min/generated/operator_summary_folder_role_table_v1_20260327_224319.md`
- `runtime/manifests/origin_maps/doc_folder_role_table_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260327_224319_351259_f8af4425_e17c2a.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/specs/folder_role_table_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/specs/folder_role_table_v1.md --label folder_role_table_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-27T22:43:19+09:00`
- summary: `document routed, registered, recorded, and receipt written`
