# operation receipt / doc_external_case_first_pass_andrej_karpathy_youtube_v1

## 1. Source
- doc_id: `doc_external_case_first_pass_andrej_karpathy_youtube_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/examples/external_case_first_pass_andrej_karpathy_youtube_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_external_case_first_pass_andrej_karpathy_youtube_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_065043_346762_14fec0f3_631758`
- idempotency_key: `816d5bee937578c5`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_external_case_first_pass_andrej_karpathy_youtube_v1_label_packet.json` [evt_20260328_065043_35fa212c]
- `doc_registered` -> `docs/examples/external_case_first_pass_andrej_karpathy_youtube_v1.md` [evt_20260328_065043_7365149b]
- `routing_normalized` -> `docs/examples/external_case_first_pass_andrej_karpathy_youtube_v1.md` [evt_20260328_065043_24dec7c4]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_external_case_first_pass_andrej_karpathy_youtube_v1_20260328_065043.md` [evt_20260328_065044_ba3aee0d]
- `file_created` -> `runtime/manifests/origin_maps/doc_external_case_first_pass_andrej_karpathy_youtube_v1_receipt_seed_origin_map.json` [evt_20260328_065044_c9f3f519]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_external_case_first_pass_andrej_karpathy_youtube_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_external_case_first_pass_andrej_karpathy_youtube_v1_20260328_065043.json`
- `app/work/observer_ingest_min/generated/split_units_external_case_first_pass_andrej_karpathy_youtube_v1_20260328_065043.json`
- `app/work/observer_ingest_min/generated/processing_trace_external_case_first_pass_andrej_karpathy_youtube_v1_20260328_065043.json`
- `app/work/observer_ingest_min/generated/readable_input_board_external_case_first_pass_andrej_karpathy_youtube_v1_20260328_065043.md`
- `app/work/observer_ingest_min/generated/operator_summary_external_case_first_pass_andrej_karpathy_youtube_v1_20260328_065043.md`
- `runtime/manifests/origin_maps/doc_external_case_first_pass_andrej_karpathy_youtube_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_065043_346762_14fec0f3_631758.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/examples/external_case_first_pass_andrej_karpathy_youtube_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/examples/external_case_first_pass_andrej_karpathy_youtube_v1.md --label external_case_first_pass_andrej_karpathy_youtube_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T06:50:44+09:00`
- summary: `document routed, registered, recorded, and receipt written`
