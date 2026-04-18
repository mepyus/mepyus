# operation receipt / doc_codex_summary_today_session_close_v1

## 1. Source
- doc_id: `doc_codex_summary_today_session_close_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/codex_summary_today_session_close_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_codex_summary_today_session_close_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_codex_summary_today_session_close_v1_label_packet.json` [evt_20260324_214708_0004cd63]
- `doc_registered` -> `codex_summary_today_session_close_v1.md` [evt_20260324_214708_6a0027a6]
- `routing_normalized` -> `codex_summary_today_session_close_v1.md` [evt_20260324_214708_758c9234]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_codex_summary_today_session_close_v1_20260324_214709.md` [evt_20260324_214709_62c201fb]
- `file_created` -> `runtime/manifests/origin_maps/doc_codex_summary_today_session_close_v1_receipt_seed_origin_map.json` [evt_20260324_214709_611bc340]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_codex_summary_today_session_close_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_codex_summary_today_session_close_v1_20260324_214709.json`
- `app/work/observer_ingest_min/generated/split_units_codex_summary_today_session_close_v1_20260324_214709.json`
- `app/work/observer_ingest_min/generated/processing_trace_codex_summary_today_session_close_v1_20260324_214709.json`
- `app/work/observer_ingest_min/generated/readable_input_board_codex_summary_today_session_close_v1_20260324_214709.md`
- `app/work/observer_ingest_min/generated/operator_summary_codex_summary_today_session_close_v1_20260324_214709.md`
- `runtime/manifests/origin_maps/doc_codex_summary_today_session_close_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc codex_summary_today_session_close_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/codex_summary_today_session_close_v1.md --label codex_summary_today_session_close_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-24T21:47:09+09:00`
- summary: `document routed, registered, recorded, and receipt written`
