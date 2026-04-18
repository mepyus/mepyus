# operation receipt / doc_heading_intervention_comparison_report_v1

## 1. Source
- doc_id: `doc_heading_intervention_comparison_report_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/heading_intervention_comparison_report_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_heading_intervention_comparison_report_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_192550_415286_31c8e0b5_6fb122`
- idempotency_key: `91d3b46d1a4c0536`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_heading_intervention_comparison_report_v1_label_packet.json` [evt_20260328_192550_3e98ba3b]
- `doc_registered` -> `docs/reports/heading_intervention_comparison_report_v1.md` [evt_20260328_192550_d5f951c2]
- `routing_normalized` -> `docs/reports/heading_intervention_comparison_report_v1.md` [evt_20260328_192550_0b58cac1]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_heading_intervention_comparison_report_v1_20260328_192550.md` [evt_20260328_192552_0fd00efb]
- `file_created` -> `runtime/manifests/origin_maps/doc_heading_intervention_comparison_report_v1_receipt_seed_origin_map.json` [evt_20260328_192552_1837772d]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_heading_intervention_comparison_report_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_heading_intervention_comparison_report_v1_20260328_192550.json`
- `app/work/observer_ingest_min/generated/split_units_heading_intervention_comparison_report_v1_20260328_192550.json`
- `app/work/observer_ingest_min/generated/processing_trace_heading_intervention_comparison_report_v1_20260328_192550.json`
- `app/work/observer_ingest_min/generated/readable_input_board_heading_intervention_comparison_report_v1_20260328_192550.md`
- `app/work/observer_ingest_min/generated/operator_summary_heading_intervention_comparison_report_v1_20260328_192550.md`
- `runtime/manifests/origin_maps/doc_heading_intervention_comparison_report_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_192550_415286_31c8e0b5_6fb122.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/heading_intervention_comparison_report_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/heading_intervention_comparison_report_v1.md --label heading_intervention_comparison_report_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T19:25:52+09:00`
- summary: `document routed, registered, recorded, and receipt written`
