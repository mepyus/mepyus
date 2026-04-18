# operation receipt / doc_negative_control_file_selection_check_v1

## 1. Source
- doc_id: `doc_negative_control_file_selection_check_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/negative_control_file_selection_check_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_negative_control_file_selection_check_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_063612_877530_fc108a3c_445a43`
- idempotency_key: `6b8d3f0c3cc07947`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_negative_control_file_selection_check_v1_label_packet.json` [evt_20260328_063612_c488a77f]
- `doc_registered` -> `docs/reports/negative_control_file_selection_check_v1.md` [evt_20260328_063612_62b166b1]
- `routing_normalized` -> `docs/reports/negative_control_file_selection_check_v1.md` [evt_20260328_063612_e07cecf3]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_negative_control_file_selection_check_v1_20260328_063612.md` [evt_20260328_063613_885eb902]
- `file_created` -> `runtime/manifests/origin_maps/doc_negative_control_file_selection_check_v1_receipt_seed_origin_map.json` [evt_20260328_063613_852dcb4e]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_negative_control_file_selection_check_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_negative_control_file_selection_check_v1_20260328_063612.json`
- `app/work/observer_ingest_min/generated/split_units_negative_control_file_selection_check_v1_20260328_063612.json`
- `app/work/observer_ingest_min/generated/processing_trace_negative_control_file_selection_check_v1_20260328_063612.json`
- `app/work/observer_ingest_min/generated/readable_input_board_negative_control_file_selection_check_v1_20260328_063612.md`
- `app/work/observer_ingest_min/generated/operator_summary_negative_control_file_selection_check_v1_20260328_063612.md`
- `runtime/manifests/origin_maps/doc_negative_control_file_selection_check_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_063612_877530_fc108a3c_445a43.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/negative_control_file_selection_check_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/negative_control_file_selection_check_v1.md --label negative_control_file_selection_check_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T06:36:13+09:00`
- summary: `document routed, registered, recorded, and receipt written`
