# operation receipt / doc_vectorfl_declaration_space_as_personal_technology_v1

## 1. Source
- doc_id: `doc_vectorfl_declaration_space_as_personal_technology_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/vectorfl_declaration_space_as_personal_technology_v1.md`

## 2. Raw Routing Markers
- DOCROLE: `declaration`
- RUNMODE: `ingest_only`
- PRIORITY: `high`

## 3. Normalized Routing
- docrole: `declaration`
- runmode: `ingest_only`
- priority: `high`

## 4. Registration
- input_class: `structured_internal_doc`
- processing_profile: `minimal_preprocess`
- material_grade: `grade_a`
- role: `declaration`
- execution_linkable: `false`
- label_packet: `runtime/manifests/label_packets/doc_vectorfl_declaration_space_as_personal_technology_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260326_182745_940837_65be4a78_9dab7f`
- idempotency_key: `bd831e89bf4269eb`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_vectorfl_declaration_space_as_personal_technology_v1_label_packet.json` [evt_20260326_182745_78fdc12e]
- `doc_registered` -> `vectorfl_declaration_space_as_personal_technology_v1.md` [evt_20260326_182745_6e796e14]
- `routing_normalized` -> `vectorfl_declaration_space_as_personal_technology_v1.md` [evt_20260326_182745_9a944945]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_vectorfl_declaration_space_as_personal_technology_v1_20260326_182746.md` [evt_20260326_182746_1bb0e1f0]
- `file_created` -> `runtime/manifests/origin_maps/doc_vectorfl_declaration_space_as_personal_technology_v1_receipt_seed_origin_map.json` [evt_20260326_182746_3e1b4249]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_vectorfl_declaration_space_as_personal_technology_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_vectorfl_declaration_space_as_personal_technology_v1_20260326_182746.json`
- `app/work/observer_ingest_min/generated/split_units_vectorfl_declaration_space_as_personal_technology_v1_20260326_182746.json`
- `app/work/observer_ingest_min/generated/processing_trace_vectorfl_declaration_space_as_personal_technology_v1_20260326_182746.json`
- `app/work/observer_ingest_min/generated/readable_input_board_vectorfl_declaration_space_as_personal_technology_v1_20260326_182746.md`
- `app/work/observer_ingest_min/generated/operator_summary_vectorfl_declaration_space_as_personal_technology_v1_20260326_182746.md`
- `runtime/manifests/origin_maps/doc_vectorfl_declaration_space_as_personal_technology_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260326_182745_940837_65be4a78_9dab7f.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc vectorfl_declaration_space_as_personal_technology_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/vectorfl_declaration_space_as_personal_technology_v1.md --label vectorfl_declaration_space_as_personal_technology_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-26T18:27:46+09:00`
- summary: `document routed, registered, recorded, and receipt written`
