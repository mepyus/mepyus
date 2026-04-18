# operation receipt / doc_second_order_readable_condition_table_draft_v1

## 1. Source
- doc_id: `doc_second_order_readable_condition_table_draft_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/specs/second_order_readable_condition_table_draft_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_second_order_readable_condition_table_draft_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_193340_019237_90a3066a_c2f5a0`
- idempotency_key: `4eefa9ce6b72da09`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_second_order_readable_condition_table_draft_v1_label_packet.json` [evt_20260328_193340_86e81b2d]
- `doc_registered` -> `docs/specs/second_order_readable_condition_table_draft_v1.md` [evt_20260328_193340_0e5b0e99]
- `routing_normalized` -> `docs/specs/second_order_readable_condition_table_draft_v1.md` [evt_20260328_193340_dffd24dd]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_second_order_readable_condition_table_draft_v1_20260328_193340.md` [evt_20260328_193342_eb5c4ffa]
- `file_created` -> `runtime/manifests/origin_maps/doc_second_order_readable_condition_table_draft_v1_receipt_seed_origin_map.json` [evt_20260328_193342_733a25cd]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_second_order_readable_condition_table_draft_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_second_order_readable_condition_table_draft_v1_20260328_193340.json`
- `app/work/observer_ingest_min/generated/split_units_second_order_readable_condition_table_draft_v1_20260328_193340.json`
- `app/work/observer_ingest_min/generated/processing_trace_second_order_readable_condition_table_draft_v1_20260328_193340.json`
- `app/work/observer_ingest_min/generated/readable_input_board_second_order_readable_condition_table_draft_v1_20260328_193340.md`
- `app/work/observer_ingest_min/generated/operator_summary_second_order_readable_condition_table_draft_v1_20260328_193340.md`
- `runtime/manifests/origin_maps/doc_second_order_readable_condition_table_draft_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_193340_019237_90a3066a_c2f5a0.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/specs/second_order_readable_condition_table_draft_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/specs/second_order_readable_condition_table_draft_v1.md --label second_order_readable_condition_table_draft_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T19:33:42+09:00`
- summary: `document routed, registered, recorded, and receipt written`
