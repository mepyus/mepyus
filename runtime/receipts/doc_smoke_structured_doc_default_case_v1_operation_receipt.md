# operation receipt / doc_smoke_structured_doc_default_case_v1

## 1. Source
- doc_id: `doc_smoke_structured_doc_default_case_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/smoke_structured_doc_default_case_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_smoke_structured_doc_default_case_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260403_164618_369270_d5b5d2ba_6bc045`
- idempotency_key: `43d9e268337ea2a0`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_smoke_structured_doc_default_case_v1_label_packet.json` [evt_20260403_164618_a5e6e020]
- `doc_registered` -> `docs/reports/smoke_structured_doc_default_case_v1.md` [evt_20260403_164618_b13c1172]
- `routing_normalized` -> `docs/reports/smoke_structured_doc_default_case_v1.md` [evt_20260403_164618_87c75de4]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_smoke_structured_doc_default_case_v1_20260403_164618.md` [evt_20260403_164618_add52e8d]
- `output_generated` -> `runtime/views/multi_lens_document_reading/doc_smoke_structured_doc_default_case_v1_multi_lens_readout_smoke_structured_doc_default_case_v1_20260403_164618.json` [evt_20260403_164618_eb76213f]
- `output_generated` -> `runtime/views/multi_lens_document_reading/doc_smoke_structured_doc_default_case_v1_multi_lens_supervisor_surface_smoke_structured_doc_default_case_v1_20260403_164618.json` [evt_20260403_164618_09195f56]
- `file_created` -> `runtime/manifests/origin_maps/doc_smoke_structured_doc_default_case_v1_receipt_seed_origin_map.json` [evt_20260403_164618_74e274d4]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_smoke_structured_doc_default_case_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_smoke_structured_doc_default_case_v1_20260403_164618.json`
- `app/work/observer_ingest_min/generated/split_units_smoke_structured_doc_default_case_v1_20260403_164618.json`
- `app/work/observer_ingest_min/generated/processing_trace_smoke_structured_doc_default_case_v1_20260403_164618.json`
- `app/work/observer_ingest_min/generated/readable_input_board_smoke_structured_doc_default_case_v1_20260403_164618.md`
- `app/work/observer_ingest_min/generated/operator_summary_smoke_structured_doc_default_case_v1_20260403_164618.md`
- `runtime/views/multi_lens_document_reading/doc_smoke_structured_doc_default_case_v1_multi_lens_readout_smoke_structured_doc_default_case_v1_20260403_164618.json`
- `runtime/views/multi_lens_document_reading/doc_smoke_structured_doc_default_case_v1_multi_lens_supervisor_surface_smoke_structured_doc_default_case_v1_20260403_164618.json`
- `runtime/manifests/origin_maps/doc_smoke_structured_doc_default_case_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260403_164618_369270_d5b5d2ba_6bc045.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/smoke_structured_doc_default_case_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/smoke_structured_doc_default_case_v1.md --label smoke_structured_doc_default_case_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-04-03T16:46:18+09:00`
- summary: `document routed, registered, recorded, and receipt written`
