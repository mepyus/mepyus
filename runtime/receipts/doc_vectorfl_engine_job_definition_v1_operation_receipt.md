# operation receipt / doc_vectorfl_engine_job_definition_v1

## 1. Source
- doc_id: `doc_vectorfl_engine_job_definition_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/vectorfl_engine_job_definition_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_vectorfl_engine_job_definition_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_145209_233497_a664c364_c8b314`
- idempotency_key: `4094c8959c3e30cf`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_vectorfl_engine_job_definition_v1_label_packet.json` [evt_20260328_145209_57fb47f7]
- `doc_registered` -> `source_assets/baselines/vectorfl_engine_job_definition_v1.md` [evt_20260328_145209_08f6984c]
- `routing_normalized` -> `source_assets/baselines/vectorfl_engine_job_definition_v1.md` [evt_20260328_145209_3bef8a56]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_vectorfl_engine_job_definition_v1_20260328_145209.md` [evt_20260328_145209_87a89b8e]
- `file_created` -> `runtime/manifests/origin_maps/doc_vectorfl_engine_job_definition_v1_receipt_seed_origin_map.json` [evt_20260328_145209_73a23561]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_vectorfl_engine_job_definition_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_vectorfl_engine_job_definition_v1_20260328_145209.json`
- `app/work/observer_ingest_min/generated/split_units_vectorfl_engine_job_definition_v1_20260328_145209.json`
- `app/work/observer_ingest_min/generated/processing_trace_vectorfl_engine_job_definition_v1_20260328_145209.json`
- `app/work/observer_ingest_min/generated/readable_input_board_vectorfl_engine_job_definition_v1_20260328_145209.md`
- `app/work/observer_ingest_min/generated/operator_summary_vectorfl_engine_job_definition_v1_20260328_145209.md`
- `runtime/manifests/origin_maps/doc_vectorfl_engine_job_definition_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_145209_233497_a664c364_c8b314.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc source_assets/baselines/vectorfl_engine_job_definition_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/vectorfl_engine_job_definition_v1.md --label vectorfl_engine_job_definition_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T14:52:09+09:00`
- summary: `document routed, registered, recorded, and receipt written`
