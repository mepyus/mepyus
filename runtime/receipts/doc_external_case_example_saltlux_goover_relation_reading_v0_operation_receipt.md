# operation receipt / doc_external_case_example_saltlux_goover_relation_reading_v0

## 1. Source
- doc_id: `doc_external_case_example_saltlux_goover_relation_reading_v0`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/external_case_example_saltlux_goover_relation_reading_v0.md`

## 2. Raw Routing Markers
- DOCROLE: `reference`
- RUNMODE: `ingest_only`
- PRIORITY: `high`

## 3. Normalized Routing
- docrole: `reference`
- runmode: `ingest_only`
- priority: `high`

## 4. Registration
- input_class: `structured_internal_doc`
- processing_profile: `minimal_preprocess`
- material_grade: `grade_a`
- role: `reference`
- execution_linkable: `false`
- label_packet: `runtime/manifests/label_packets/doc_external_case_example_saltlux_goover_relation_reading_v0_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260326_182344_695359_db0c11d0_f07e79`
- idempotency_key: `2337f18b0ee27979`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_external_case_example_saltlux_goover_relation_reading_v0_label_packet.json` [evt_20260326_182344_a317fe6c]
- `doc_registered` -> `external_case_example_saltlux_goover_relation_reading_v0.md` [evt_20260326_182344_8fc20813]
- `routing_normalized` -> `external_case_example_saltlux_goover_relation_reading_v0.md` [evt_20260326_182344_d0931207]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_external_case_example_saltlux_goover_relation_reading_v0_20260326_182344.md` [evt_20260326_182344_de21f3ba]
- `file_created` -> `runtime/manifests/origin_maps/doc_external_case_example_saltlux_goover_relation_reading_v0_receipt_seed_origin_map.json` [evt_20260326_182344_5c78048f]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_external_case_example_saltlux_goover_relation_reading_v0_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_external_case_example_saltlux_goover_relation_reading_v0_20260326_182344.json`
- `app/work/observer_ingest_min/generated/split_units_external_case_example_saltlux_goover_relation_reading_v0_20260326_182344.json`
- `app/work/observer_ingest_min/generated/processing_trace_external_case_example_saltlux_goover_relation_reading_v0_20260326_182344.json`
- `app/work/observer_ingest_min/generated/readable_input_board_external_case_example_saltlux_goover_relation_reading_v0_20260326_182344.md`
- `app/work/observer_ingest_min/generated/operator_summary_external_case_example_saltlux_goover_relation_reading_v0_20260326_182344.md`
- `runtime/manifests/origin_maps/doc_external_case_example_saltlux_goover_relation_reading_v0_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260326_182344_695359_db0c11d0_f07e79.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc external_case_example_saltlux_goover_relation_reading_v0.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/external_case_example_saltlux_goover_relation_reading_v0.md --label external_case_example_saltlux_goover_relation_reading_v0 --profile auto`

## 9. Final Status
- processed_at: `2026-03-26T18:23:44+09:00`
- summary: `document routed, registered, recorded, and receipt written`
