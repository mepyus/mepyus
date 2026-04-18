# operation receipt / doc_external_case_first_pass_saltlux_raw_transcript_input_v2

## 1. Source
- doc_id: `doc_external_case_first_pass_saltlux_raw_transcript_input_v2`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_saltlux_raw_transcript_input_v2.md`

## 2. Raw Routing Markers
- DOCROLE: `directive`
- RUNMODE: `ingest_then_execute`
- PRIORITY: `high`

## 3. Normalized Routing
- docrole: `directive`
- runmode: `ingest_then_execute`
- priority: `high`

## 4. Registration
- input_class: `structured_internal_doc`
- processing_profile: `execution_coupled`
- material_grade: `grade_a`
- role: `directive`
- execution_linkable: `true`
- label_packet: `runtime/manifests/label_packets/doc_external_case_first_pass_saltlux_raw_transcript_input_v2_label_packet.json`

## 5. Ticket
- ticket_id: `tkt_process_external_case_first_pass_saltlux_raw_transcript_input_v2`
- ticket_created: `yes`

## 5A. Run Identity
- run_id: `run_20260326_203800_729630_9ca8594f_fcf5e1`
- idempotency_key: `c9da8bf76e18a316`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_external_case_first_pass_saltlux_raw_transcript_input_v2_label_packet.json` [evt_20260326_203800_661c3ea9]
- `doc_registered` -> `external_case_first_pass_saltlux_raw_transcript_input_v2.md` [evt_20260326_203800_373ff64b]
- `routing_normalized` -> `external_case_first_pass_saltlux_raw_transcript_input_v2.md` [evt_20260326_203800_3a50ae3d]
- `ticket_created` -> `runtime/manifests/ticket_registry_v1.json` [evt_20260326_203800_395d74b6]
- `execution_started` -> `external_case_first_pass_saltlux_raw_transcript_input_v2.md` [evt_20260326_203800_cf586ae0]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_external_case_first_pass_saltlux_raw_transcript_input_v2_20260326_203800.md` [evt_20260326_203800_2a288d2e]
- `file_created` -> `runtime/manifests/origin_maps/doc_external_case_first_pass_saltlux_raw_transcript_input_v2_receipt_seed_origin_map.json` [evt_20260326_203800_635705ac]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_external_case_first_pass_saltlux_raw_transcript_input_v2_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_external_case_first_pass_saltlux_raw_transcript_input_v2_20260326_203800.json`
- `app/work/observer_ingest_min/generated/split_units_external_case_first_pass_saltlux_raw_transcript_input_v2_20260326_203800.json`
- `app/work/observer_ingest_min/generated/processing_trace_external_case_first_pass_saltlux_raw_transcript_input_v2_20260326_203800.json`
- `app/work/observer_ingest_min/generated/readable_input_board_external_case_first_pass_saltlux_raw_transcript_input_v2_20260326_203800.md`
- `app/work/observer_ingest_min/generated/operator_summary_external_case_first_pass_saltlux_raw_transcript_input_v2_20260326_203800.md`
- `runtime/manifests/origin_maps/doc_external_case_first_pass_saltlux_raw_transcript_input_v2_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260326_203800_729630_9ca8594f_fcf5e1.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc external_case_first_pass_saltlux_raw_transcript_input_v2.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_saltlux_raw_transcript_input_v2.md --label external_case_first_pass_saltlux_raw_transcript_input_v2 --profile auto`

## 9. Final Status
- processed_at: `2026-03-26T20:38:00+09:00`
- summary: `document routed, registered, recorded, and receipt written`
