# operation receipt / doc_program_grade_workspace_surface_maintenance_directive_v1

## 1. Source
- doc_id: `doc_program_grade_workspace_surface_maintenance_directive_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/source_assets/directives/program_grade_workspace_surface_maintenance_directive_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_program_grade_workspace_surface_maintenance_directive_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260327_222351_792080_a9c64e77_b7a8a2`
- idempotency_key: `c125369220061758`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_program_grade_workspace_surface_maintenance_directive_v1_label_packet.json` [evt_20260327_222351_1044b1b2]
- `doc_registered` -> `source_assets/directives/program_grade_workspace_surface_maintenance_directive_v1.md` [evt_20260327_222351_db686049]
- `routing_normalized` -> `source_assets/directives/program_grade_workspace_surface_maintenance_directive_v1.md` [evt_20260327_222351_b2c3a0d3]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_program_grade_workspace_surface_maintenance_directive_v1_20260327_222351.md` [evt_20260327_222351_76635b91]
- `file_created` -> `runtime/manifests/origin_maps/doc_program_grade_workspace_surface_maintenance_directive_v1_receipt_seed_origin_map.json` [evt_20260327_222351_6d171730]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_program_grade_workspace_surface_maintenance_directive_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_program_grade_workspace_surface_maintenance_directive_v1_20260327_222351.json`
- `app/work/observer_ingest_min/generated/split_units_program_grade_workspace_surface_maintenance_directive_v1_20260327_222351.json`
- `app/work/observer_ingest_min/generated/processing_trace_program_grade_workspace_surface_maintenance_directive_v1_20260327_222351.json`
- `app/work/observer_ingest_min/generated/readable_input_board_program_grade_workspace_surface_maintenance_directive_v1_20260327_222351.md`
- `app/work/observer_ingest_min/generated/operator_summary_program_grade_workspace_surface_maintenance_directive_v1_20260327_222351.md`
- `runtime/manifests/origin_maps/doc_program_grade_workspace_surface_maintenance_directive_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260327_222351_792080_a9c64e77_b7a8a2.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc source_assets/directives/program_grade_workspace_surface_maintenance_directive_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/source_assets/directives/program_grade_workspace_surface_maintenance_directive_v1.md --label program_grade_workspace_surface_maintenance_directive_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-27T22:23:51+09:00`
- summary: `document routed, registered, recorded, and receipt written`
