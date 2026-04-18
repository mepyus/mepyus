# operation receipt / doc_thin_operation_rules_lock_v1

## 1. Source
- doc_id: `doc_thin_operation_rules_lock_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/thin_operation_rules_lock_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_thin_operation_rules_lock_v1_label_packet.json`

## 5. Ticket
- ticket_id: `tkt_process_thin_operation_rules_lock_v1`
- ticket_created: `yes`

## 5A. Run Identity
- run_id: `run_20260326_200826_545413_4494c97e_344ad5`
- idempotency_key: `99574b65505fc5eb`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_thin_operation_rules_lock_v1_label_packet.json` [evt_20260326_200826_204dd916]
- `doc_registered` -> `thin_operation_rules_lock_v1.md` [evt_20260326_200826_528588ef]
- `routing_normalized` -> `thin_operation_rules_lock_v1.md` [evt_20260326_200826_be750074]
- `ticket_created` -> `runtime/manifests/ticket_registry_v1.json` [evt_20260326_200826_21f98c9c]
- `execution_started` -> `thin_operation_rules_lock_v1.md` [evt_20260326_200826_ef337a27]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_thin_operation_rules_lock_v1_20260326_200826.md` [evt_20260326_200826_574be212]
- `file_created` -> `runtime/manifests/origin_maps/doc_thin_operation_rules_lock_v1_receipt_seed_origin_map.json` [evt_20260326_200826_d0448a84]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_thin_operation_rules_lock_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_thin_operation_rules_lock_v1_20260326_200826.json`
- `app/work/observer_ingest_min/generated/split_units_thin_operation_rules_lock_v1_20260326_200826.json`
- `app/work/observer_ingest_min/generated/processing_trace_thin_operation_rules_lock_v1_20260326_200826.json`
- `app/work/observer_ingest_min/generated/readable_input_board_thin_operation_rules_lock_v1_20260326_200826.md`
- `app/work/observer_ingest_min/generated/operator_summary_thin_operation_rules_lock_v1_20260326_200826.md`
- `runtime/manifests/origin_maps/doc_thin_operation_rules_lock_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260326_200826_545413_4494c97e_344ad5.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc thin_operation_rules_lock_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/thin_operation_rules_lock_v1.md --label thin_operation_rules_lock_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-26T20:08:26+09:00`
- summary: `document routed, registered, recorded, and receipt written`
