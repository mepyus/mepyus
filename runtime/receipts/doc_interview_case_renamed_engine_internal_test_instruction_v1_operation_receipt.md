# operation receipt / doc_interview_case_renamed_engine_internal_test_instruction_v1

## 1. Source
- doc_id: `doc_interview_case_renamed_engine_internal_test_instruction_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/source_assets/directives/interview_case_renamed_engine_internal_test_instruction_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_interview_case_renamed_engine_internal_test_instruction_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_081124_230270_8219f28c_863dd9`
- idempotency_key: `13ccc61cbb20ebce`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_interview_case_renamed_engine_internal_test_instruction_v1_label_packet.json` [evt_20260328_081124_6164f66e]
- `doc_registered` -> `source_assets/directives/interview_case_renamed_engine_internal_test_instruction_v1.md` [evt_20260328_081124_447ae7fe]
- `routing_normalized` -> `source_assets/directives/interview_case_renamed_engine_internal_test_instruction_v1.md` [evt_20260328_081124_eab14506]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_interview_case_renamed_engine_internal_test_instruction_v1_20260328_081124.md` [evt_20260328_081124_99011792]
- `file_created` -> `runtime/manifests/origin_maps/doc_interview_case_renamed_engine_internal_test_instruction_v1_receipt_seed_origin_map.json` [evt_20260328_081124_8d17f4c9]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_interview_case_renamed_engine_internal_test_instruction_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_interview_case_renamed_engine_internal_test_instruction_v1_20260328_081124.json`
- `app/work/observer_ingest_min/generated/split_units_interview_case_renamed_engine_internal_test_instruction_v1_20260328_081124.json`
- `app/work/observer_ingest_min/generated/processing_trace_interview_case_renamed_engine_internal_test_instruction_v1_20260328_081124.json`
- `app/work/observer_ingest_min/generated/readable_input_board_interview_case_renamed_engine_internal_test_instruction_v1_20260328_081124.md`
- `app/work/observer_ingest_min/generated/operator_summary_interview_case_renamed_engine_internal_test_instruction_v1_20260328_081124.md`
- `runtime/manifests/origin_maps/doc_interview_case_renamed_engine_internal_test_instruction_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_081124_230270_8219f28c_863dd9.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc source_assets/directives/interview_case_renamed_engine_internal_test_instruction_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/source_assets/directives/interview_case_renamed_engine_internal_test_instruction_v1.md --label interview_case_renamed_engine_internal_test_instruction_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T08:11:24+09:00`
- summary: `document routed, registered, recorded, and receipt written`
