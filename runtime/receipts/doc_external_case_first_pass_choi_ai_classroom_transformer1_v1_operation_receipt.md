# operation receipt / doc_external_case_first_pass_choi_ai_classroom_transformer1_v1

## 1. Source
- doc_id: `doc_external_case_first_pass_choi_ai_classroom_transformer1_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/examples/external_case_first_pass_choi_ai_classroom_transformer1_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_external_case_first_pass_choi_ai_classroom_transformer1_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_061757_837390_437d491c_8d3b77`
- idempotency_key: `be90d6a173abbede`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_external_case_first_pass_choi_ai_classroom_transformer1_v1_label_packet.json` [evt_20260328_061757_016d31c9]
- `doc_registered` -> `docs/examples/external_case_first_pass_choi_ai_classroom_transformer1_v1.md` [evt_20260328_061757_22447c23]
- `routing_normalized` -> `docs/examples/external_case_first_pass_choi_ai_classroom_transformer1_v1.md` [evt_20260328_061757_2a8867d6]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_external_case_first_pass_choi_ai_classroom_transformer1_v1_20260328_061757.md` [evt_20260328_061758_ba90b666]
- `file_created` -> `runtime/manifests/origin_maps/doc_external_case_first_pass_choi_ai_classroom_transformer1_v1_receipt_seed_origin_map.json` [evt_20260328_061758_c7d9522f]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_external_case_first_pass_choi_ai_classroom_transformer1_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_external_case_first_pass_choi_ai_classroom_transformer1_v1_20260328_061757.json`
- `app/work/observer_ingest_min/generated/split_units_external_case_first_pass_choi_ai_classroom_transformer1_v1_20260328_061757.json`
- `app/work/observer_ingest_min/generated/processing_trace_external_case_first_pass_choi_ai_classroom_transformer1_v1_20260328_061757.json`
- `app/work/observer_ingest_min/generated/readable_input_board_external_case_first_pass_choi_ai_classroom_transformer1_v1_20260328_061757.md`
- `app/work/observer_ingest_min/generated/operator_summary_external_case_first_pass_choi_ai_classroom_transformer1_v1_20260328_061757.md`
- `runtime/manifests/origin_maps/doc_external_case_first_pass_choi_ai_classroom_transformer1_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_061757_837390_437d491c_8d3b77.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/examples/external_case_first_pass_choi_ai_classroom_transformer1_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/examples/external_case_first_pass_choi_ai_classroom_transformer1_v1.md --label external_case_first_pass_choi_ai_classroom_transformer1_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T06:17:58+09:00`
- summary: `document routed, registered, recorded, and receipt written`
