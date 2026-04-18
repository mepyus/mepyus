# operation receipt / doc_external_case_first_pass_saltlux_ai_v1

## 1. Source
- doc_id: `doc_external_case_first_pass_saltlux_ai_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/examples/external_case_first_pass_saltlux_ai_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_external_case_first_pass_saltlux_ai_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260327_225142_082988_aef2648f_31b806`
- idempotency_key: `72133f5e40e92483`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_external_case_first_pass_saltlux_ai_v1_label_packet.json` [evt_20260327_225142_775af93f]
- `doc_registered` -> `docs/examples/external_case_first_pass_saltlux_ai_v1.md` [evt_20260327_225142_6f4ed96f]
- `routing_normalized` -> `docs/examples/external_case_first_pass_saltlux_ai_v1.md` [evt_20260327_225142_cdb845cb]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_external_case_first_pass_saltlux_ai_v1_20260327_225142.md` [evt_20260327_225142_c0344966]
- `file_created` -> `runtime/manifests/origin_maps/doc_external_case_first_pass_saltlux_ai_v1_receipt_seed_origin_map.json` [evt_20260327_225142_5a5aed40]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_external_case_first_pass_saltlux_ai_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_external_case_first_pass_saltlux_ai_v1_20260327_225142.json`
- `app/work/observer_ingest_min/generated/split_units_external_case_first_pass_saltlux_ai_v1_20260327_225142.json`
- `app/work/observer_ingest_min/generated/processing_trace_external_case_first_pass_saltlux_ai_v1_20260327_225142.json`
- `app/work/observer_ingest_min/generated/readable_input_board_external_case_first_pass_saltlux_ai_v1_20260327_225142.md`
- `app/work/observer_ingest_min/generated/operator_summary_external_case_first_pass_saltlux_ai_v1_20260327_225142.md`
- `runtime/manifests/origin_maps/doc_external_case_first_pass_saltlux_ai_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260327_225142_082988_aef2648f_31b806.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/examples/external_case_first_pass_saltlux_ai_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/examples/external_case_first_pass_saltlux_ai_v1.md --label external_case_first_pass_saltlux_ai_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-27T22:51:42+09:00`
- summary: `document routed, registered, recorded, and receipt written`
