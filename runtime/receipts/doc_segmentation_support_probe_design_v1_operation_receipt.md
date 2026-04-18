# operation receipt / doc_segmentation_support_probe_design_v1

## 1. Source
- doc_id: `doc_segmentation_support_probe_design_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/segmentation_support_probe_design_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_segmentation_support_probe_design_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_191115_121997_771ac54c_157f36`
- idempotency_key: `5a083cbb5fa9a45d`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_segmentation_support_probe_design_v1_label_packet.json` [evt_20260328_191115_4b85ce11]
- `doc_registered` -> `docs/reports/segmentation_support_probe_design_v1.md` [evt_20260328_191115_59fbdca9]
- `routing_normalized` -> `docs/reports/segmentation_support_probe_design_v1.md` [evt_20260328_191115_adff67a5]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_segmentation_support_probe_design_v1_20260328_191115.md` [evt_20260328_191116_d64ca4b7]
- `file_created` -> `runtime/manifests/origin_maps/doc_segmentation_support_probe_design_v1_receipt_seed_origin_map.json` [evt_20260328_191117_502b520b]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_segmentation_support_probe_design_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_segmentation_support_probe_design_v1_20260328_191115.json`
- `app/work/observer_ingest_min/generated/split_units_segmentation_support_probe_design_v1_20260328_191115.json`
- `app/work/observer_ingest_min/generated/processing_trace_segmentation_support_probe_design_v1_20260328_191115.json`
- `app/work/observer_ingest_min/generated/readable_input_board_segmentation_support_probe_design_v1_20260328_191115.md`
- `app/work/observer_ingest_min/generated/operator_summary_segmentation_support_probe_design_v1_20260328_191115.md`
- `runtime/manifests/origin_maps/doc_segmentation_support_probe_design_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_191115_121997_771ac54c_157f36.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/segmentation_support_probe_design_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/segmentation_support_probe_design_v1.md --label segmentation_support_probe_design_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T19:11:17+09:00`
- summary: `document routed, registered, recorded, and receipt written`
