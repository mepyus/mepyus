# operation receipt / doc_repeated_second_order_pattern_table_draft_v1

## 1. Source
- doc_id: `doc_repeated_second_order_pattern_table_draft_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/specs/repeated_second_order_pattern_table_draft_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_repeated_second_order_pattern_table_draft_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_185930_348103_e534616b_008f80`
- idempotency_key: `18ca8b639dffef77`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_repeated_second_order_pattern_table_draft_v1_label_packet.json` [evt_20260328_185930_fdb3d779]
- `doc_registered` -> `docs/specs/repeated_second_order_pattern_table_draft_v1.md` [evt_20260328_185930_db9625d5]
- `routing_normalized` -> `docs/specs/repeated_second_order_pattern_table_draft_v1.md` [evt_20260328_185930_c94ef44a]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_repeated_second_order_pattern_table_draft_v1_20260328_185930.md` [evt_20260328_185931_0e47ad63]
- `file_created` -> `runtime/manifests/origin_maps/doc_repeated_second_order_pattern_table_draft_v1_receipt_seed_origin_map.json` [evt_20260328_185931_12d46910]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_repeated_second_order_pattern_table_draft_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_repeated_second_order_pattern_table_draft_v1_20260328_185930.json`
- `app/work/observer_ingest_min/generated/split_units_repeated_second_order_pattern_table_draft_v1_20260328_185930.json`
- `app/work/observer_ingest_min/generated/processing_trace_repeated_second_order_pattern_table_draft_v1_20260328_185930.json`
- `app/work/observer_ingest_min/generated/readable_input_board_repeated_second_order_pattern_table_draft_v1_20260328_185930.md`
- `app/work/observer_ingest_min/generated/operator_summary_repeated_second_order_pattern_table_draft_v1_20260328_185930.md`
- `runtime/manifests/origin_maps/doc_repeated_second_order_pattern_table_draft_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_185930_348103_e534616b_008f80.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/specs/repeated_second_order_pattern_table_draft_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/specs/repeated_second_order_pattern_table_draft_v1.md --label repeated_second_order_pattern_table_draft_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T18:59:31+09:00`
- summary: `document routed, registered, recorded, and receipt written`
