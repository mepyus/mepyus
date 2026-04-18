# operation receipt / doc_codex_baseline_session_id_and_gemini_log_link_contract_v1

## 1. Source
- doc_id: `doc_codex_baseline_session_id_and_gemini_log_link_contract_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/codex_baseline_session_id_and_gemini_log_link_contract_v1.md`

## 2. Raw Routing Markers
- DOCROLE: `baseline`
- RUNMODE: `ingest_only`
- PRIORITY: `high`

## 3. Normalized Routing
- docrole: `baseline`
- runmode: `ingest_only`
- priority: `high`

## 4. Registration
- input_class: `structured_internal_doc`
- processing_profile: `minimal_preprocess`
- material_grade: `grade_a`
- role: `baseline`
- execution_linkable: `false`
- label_packet: `runtime/manifests/label_packets/doc_codex_baseline_session_id_and_gemini_log_link_contract_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260325_205719_377039_26781df0_60eb15`
- idempotency_key: `94cb21aca61cfe7d`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_codex_baseline_session_id_and_gemini_log_link_contract_v1_label_packet.json` [evt_20260325_205719_6030e746]
- `doc_registered` -> `codex_baseline_session_id_and_gemini_log_link_contract_v1.md` [evt_20260325_205719_c8c4ead2]
- `routing_normalized` -> `codex_baseline_session_id_and_gemini_log_link_contract_v1.md` [evt_20260325_205719_f9c760be]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_codex_baseline_session_id_and_gemini_log_link_contract_v1_20260325_205719.md` [evt_20260325_205719_89e1d071]
- `file_created` -> `runtime/manifests/origin_maps/doc_codex_baseline_session_id_and_gemini_log_link_contract_v1_receipt_seed_origin_map.json` [evt_20260325_205719_b0f075aa]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_codex_baseline_session_id_and_gemini_log_link_contract_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_codex_baseline_session_id_and_gemini_log_link_contract_v1_20260325_205719.json`
- `app/work/observer_ingest_min/generated/split_units_codex_baseline_session_id_and_gemini_log_link_contract_v1_20260325_205719.json`
- `app/work/observer_ingest_min/generated/processing_trace_codex_baseline_session_id_and_gemini_log_link_contract_v1_20260325_205719.json`
- `app/work/observer_ingest_min/generated/readable_input_board_codex_baseline_session_id_and_gemini_log_link_contract_v1_20260325_205719.md`
- `app/work/observer_ingest_min/generated/operator_summary_codex_baseline_session_id_and_gemini_log_link_contract_v1_20260325_205719.md`
- `runtime/manifests/origin_maps/doc_codex_baseline_session_id_and_gemini_log_link_contract_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260325_205719_377039_26781df0_60eb15.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc codex_baseline_session_id_and_gemini_log_link_contract_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/codex_baseline_session_id_and_gemini_log_link_contract_v1.md --label codex_baseline_session_id_and_gemini_log_link_contract_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-25T20:57:19+09:00`
- summary: `document routed, registered, recorded, and receipt written`
