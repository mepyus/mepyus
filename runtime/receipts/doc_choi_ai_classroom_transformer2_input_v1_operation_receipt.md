# operation receipt / doc_choi_ai_classroom_transformer2_input_v1

## 1. Source
- doc_id: `doc_choi_ai_classroom_transformer2_input_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/source_assets/external_case_inputs/choi_ai_classroom_transformer2_input_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_choi_ai_classroom_transformer2_input_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_061757_848596_6aeb60c3_73099d`
- idempotency_key: `89832a12c5c8f492`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_choi_ai_classroom_transformer2_input_v1_label_packet.json` [evt_20260328_061757_2d588626]
- `doc_registered` -> `source_assets/external_case_inputs/choi_ai_classroom_transformer2_input_v1.md` [evt_20260328_061757_92f00507]
- `routing_normalized` -> `source_assets/external_case_inputs/choi_ai_classroom_transformer2_input_v1.md` [evt_20260328_061757_5bb117cc]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_choi_ai_classroom_transformer2_input_v1_20260328_061758.md` [evt_20260328_061758_06df401f]
- `file_created` -> `runtime/manifests/origin_maps/doc_choi_ai_classroom_transformer2_input_v1_receipt_seed_origin_map.json` [evt_20260328_061758_2bca8bfd]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_choi_ai_classroom_transformer2_input_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_choi_ai_classroom_transformer2_input_v1_20260328_061758.json`
- `app/work/observer_ingest_min/generated/split_units_choi_ai_classroom_transformer2_input_v1_20260328_061758.json`
- `app/work/observer_ingest_min/generated/processing_trace_choi_ai_classroom_transformer2_input_v1_20260328_061758.json`
- `app/work/observer_ingest_min/generated/readable_input_board_choi_ai_classroom_transformer2_input_v1_20260328_061758.md`
- `app/work/observer_ingest_min/generated/operator_summary_choi_ai_classroom_transformer2_input_v1_20260328_061758.md`
- `runtime/manifests/origin_maps/doc_choi_ai_classroom_transformer2_input_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_061757_848596_6aeb60c3_73099d.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc source_assets/external_case_inputs/choi_ai_classroom_transformer2_input_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/source_assets/external_case_inputs/choi_ai_classroom_transformer2_input_v1.md --label choi_ai_classroom_transformer2_input_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T06:17:58+09:00`
- summary: `document routed, registered, recorded, and receipt written`
