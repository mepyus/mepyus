# operation receipt / doc_smoke_structured_doc_summary_case_v1

## 1. Source
- doc_id: `doc_smoke_structured_doc_summary_case_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/smoke_structured_doc_summary_case_v1.md`

## 2. Raw Routing Markers
- DOCROLE: `summary`
- RUNMODE: `ingest_only`
- PRIORITY: `normal`

## 3. Normalized Routing
- docrole: `summary`
- runmode: `ingest_only`
- priority: `normal`

## 4. Registration
- input_class: `structured_internal_doc`
- processing_profile: `minimal_preprocess`
- material_grade: `grade_a`
- role: `summary`
- execution_linkable: `false`
- label_packet: `runtime/manifests/label_packets/doc_smoke_structured_doc_summary_case_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260403_161910_474452_edd20131_2c516d`
- idempotency_key: `72871a970663efdc`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_smoke_structured_doc_summary_case_v1_label_packet.json` [evt_20260403_161910_61194589]
- `doc_registered` -> `docs/reports/smoke_structured_doc_summary_case_v1.md` [evt_20260403_161910_2316e44b]
- `routing_normalized` -> `docs/reports/smoke_structured_doc_summary_case_v1.md` [evt_20260403_161910_079d6fa5]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_smoke_structured_doc_summary_case_v1_20260403_161910.md` [evt_20260403_161910_5fb9b9e5]
- `output_generated` -> `runtime/views/multi_lens_document_reading/doc_smoke_structured_doc_summary_case_v1_multi_lens_readout_smoke_structured_doc_summary_case_v1_20260403_161910.json` [evt_20260403_161910_6686cb48]
- `file_created` -> `runtime/manifests/origin_maps/doc_smoke_structured_doc_summary_case_v1_receipt_seed_origin_map.json` [evt_20260403_161910_30d38647]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_smoke_structured_doc_summary_case_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_smoke_structured_doc_summary_case_v1_20260403_161910.json`
- `app/work/observer_ingest_min/generated/split_units_smoke_structured_doc_summary_case_v1_20260403_161910.json`
- `app/work/observer_ingest_min/generated/processing_trace_smoke_structured_doc_summary_case_v1_20260403_161910.json`
- `app/work/observer_ingest_min/generated/readable_input_board_smoke_structured_doc_summary_case_v1_20260403_161910.md`
- `app/work/observer_ingest_min/generated/operator_summary_smoke_structured_doc_summary_case_v1_20260403_161910.md`
- `runtime/views/multi_lens_document_reading/doc_smoke_structured_doc_summary_case_v1_multi_lens_readout_smoke_structured_doc_summary_case_v1_20260403_161910.json`
- `runtime/manifests/origin_maps/doc_smoke_structured_doc_summary_case_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260403_161910_474452_edd20131_2c516d.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/smoke_structured_doc_summary_case_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/smoke_structured_doc_summary_case_v1.md --label smoke_structured_doc_summary_case_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-04-03T16:19:10+09:00`
- summary: `document routed, registered, recorded, and receipt written`
