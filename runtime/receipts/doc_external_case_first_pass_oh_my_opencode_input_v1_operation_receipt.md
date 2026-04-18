# operation receipt / doc_external_case_first_pass_oh_my_opencode_input_v1

## 1. Source
- doc_id: `doc_external_case_first_pass_oh_my_opencode_input_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_oh_my_opencode_input_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_external_case_first_pass_oh_my_opencode_input_v1_label_packet.json`

## 5. Ticket
- ticket_id: `tkt_process_external_case_first_pass_oh_my_opencode_input_v1`
- ticket_created: `yes`

## 5A. Run Identity
- run_id: `run_20260326_205840_945224_1e530531_d583db`
- idempotency_key: `8164c252435028a1`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_external_case_first_pass_oh_my_opencode_input_v1_label_packet.json` [evt_20260326_205840_9828d92f]
- `doc_registered` -> `external_case_first_pass_oh_my_opencode_input_v1.md` [evt_20260326_205840_01ccad3f]
- `routing_normalized` -> `external_case_first_pass_oh_my_opencode_input_v1.md` [evt_20260326_205840_b8b27779]
- `ticket_created` -> `runtime/manifests/ticket_registry_v1.json` [evt_20260326_205841_d5f37d73]
- `execution_started` -> `external_case_first_pass_oh_my_opencode_input_v1.md` [evt_20260326_205841_dd9a67c4]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_external_case_first_pass_oh_my_opencode_input_v1_20260326_205841.md` [evt_20260326_205841_03c70e5e]
- `file_created` -> `runtime/manifests/origin_maps/doc_external_case_first_pass_oh_my_opencode_input_v1_receipt_seed_origin_map.json` [evt_20260326_205841_10b4b9aa]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_external_case_first_pass_oh_my_opencode_input_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_external_case_first_pass_oh_my_opencode_input_v1_20260326_205841.json`
- `app/work/observer_ingest_min/generated/split_units_external_case_first_pass_oh_my_opencode_input_v1_20260326_205841.json`
- `app/work/observer_ingest_min/generated/processing_trace_external_case_first_pass_oh_my_opencode_input_v1_20260326_205841.json`
- `app/work/observer_ingest_min/generated/readable_input_board_external_case_first_pass_oh_my_opencode_input_v1_20260326_205841.md`
- `app/work/observer_ingest_min/generated/operator_summary_external_case_first_pass_oh_my_opencode_input_v1_20260326_205841.md`
- `runtime/manifests/origin_maps/doc_external_case_first_pass_oh_my_opencode_input_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260326_205840_945224_1e530531_d583db.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc external_case_first_pass_oh_my_opencode_input_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_oh_my_opencode_input_v1.md --label external_case_first_pass_oh_my_opencode_input_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-26T20:58:41+09:00`
- summary: `document routed, registered, recorded, and receipt written`
