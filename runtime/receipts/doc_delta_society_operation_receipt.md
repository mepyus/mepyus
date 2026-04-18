# operation receipt / doc_delta_society

## 1. Source
- doc_id: `doc_delta_society`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/delta_society.md`

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
- label_packet: `runtime/manifests/label_packets/doc_delta_society_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260402_215911_804274_51d403a8_6d88d7`
- idempotency_key: `d6163dc3779eed72`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_delta_society_label_packet.json` [evt_20260402_215911_10e40644]
- `doc_registered` -> `inputs/external_cases/delta_society.md` [evt_20260402_215911_75c8f489]
- `routing_normalized` -> `inputs/external_cases/delta_society.md` [evt_20260402_215911_f64ff6ed]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_delta_society_20260402_215911.md` [evt_20260402_215912_d1e12a73]
- `file_created` -> `runtime/manifests/origin_maps/doc_delta_society_receipt_seed_origin_map.json` [evt_20260402_215912_fc1689d3]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_delta_society_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_delta_society_20260402_215911.json`
- `app/work/observer_ingest_min/generated/split_units_delta_society_20260402_215911.json`
- `app/work/observer_ingest_min/generated/processing_trace_delta_society_20260402_215911.json`
- `app/work/observer_ingest_min/generated/readable_input_board_delta_society_20260402_215911.md`
- `app/work/observer_ingest_min/generated/operator_summary_delta_society_20260402_215911.md`
- `runtime/manifests/origin_maps/doc_delta_society_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260402_215911_804274_51d403a8_6d88d7.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc inputs/external_cases/delta_society.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/delta_society.md --label delta_society --profile auto`

## 9. Final Status
- processed_at: `2026-04-02T21:59:12+09:00`
- summary: `document routed, registered, recorded, and receipt written`
