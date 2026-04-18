# operation receipt / doc_heading_independent_role_probe_claude_code_index_v1

## 1. Source
- doc_id: `doc_heading_independent_role_probe_claude_code_index_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/heading_independent_role_probe_claude_code_index_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_heading_independent_role_probe_claude_code_index_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_192636_363416_6706ecd5_e532b3`
- idempotency_key: `c63e945e43a8d88d`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_heading_independent_role_probe_claude_code_index_v1_label_packet.json` [evt_20260328_192636_4dfd322b]
- `doc_registered` -> `docs/reports/heading_independent_role_probe_claude_code_index_v1.md` [evt_20260328_192636_ae3b7415]
- `routing_normalized` -> `docs/reports/heading_independent_role_probe_claude_code_index_v1.md` [evt_20260328_192636_a7d50645]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_heading_independent_role_probe_claude_code_index_v1_20260328_192636.md` [evt_20260328_192636_ae9a2adb]
- `file_created` -> `runtime/manifests/origin_maps/doc_heading_independent_role_probe_claude_code_index_v1_receipt_seed_origin_map.json` [evt_20260328_192636_57caab05]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_heading_independent_role_probe_claude_code_index_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_heading_independent_role_probe_claude_code_index_v1_20260328_192636.json`
- `app/work/observer_ingest_min/generated/split_units_heading_independent_role_probe_claude_code_index_v1_20260328_192636.json`
- `app/work/observer_ingest_min/generated/processing_trace_heading_independent_role_probe_claude_code_index_v1_20260328_192636.json`
- `app/work/observer_ingest_min/generated/readable_input_board_heading_independent_role_probe_claude_code_index_v1_20260328_192636.md`
- `app/work/observer_ingest_min/generated/operator_summary_heading_independent_role_probe_claude_code_index_v1_20260328_192636.md`
- `runtime/manifests/origin_maps/doc_heading_independent_role_probe_claude_code_index_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_192636_363416_6706ecd5_e532b3.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/heading_independent_role_probe_claude_code_index_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/heading_independent_role_probe_claude_code_index_v1.md --label heading_independent_role_probe_claude_code_index_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T19:26:36+09:00`
- summary: `document routed, registered, recorded, and receipt written`
