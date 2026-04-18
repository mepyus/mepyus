# operation receipt / doc_multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1

## 1. Source
- doc_id: `doc_multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/source_assets/directives/multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_161905_035683_cc40ec4d_2689a8`
- idempotency_key: `aaa5a1f97a52dcaa`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1_label_packet.json` [evt_20260328_161905_c0854f79]
- `doc_registered` -> `source_assets/directives/multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1.md` [evt_20260328_161905_368a19b2]
- `routing_normalized` -> `source_assets/directives/multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1.md` [evt_20260328_161905_3c98ba2e]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1_20260328_161905.md` [evt_20260328_161905_0968e2ff]
- `file_created` -> `runtime/manifests/origin_maps/doc_multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1_receipt_seed_origin_map.json` [evt_20260328_161905_1d4bd16c]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1_20260328_161905.json`
- `app/work/observer_ingest_min/generated/split_units_multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1_20260328_161905.json`
- `app/work/observer_ingest_min/generated/processing_trace_multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1_20260328_161905.json`
- `app/work/observer_ingest_min/generated/readable_input_board_multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1_20260328_161905.md`
- `app/work/observer_ingest_min/generated/operator_summary_multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1_20260328_161905.md`
- `runtime/manifests/origin_maps/doc_multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_161905_035683_cc40ec4d_2689a8.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc source_assets/directives/multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/source_assets/directives/multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1.md --label multi_pass_interpretation_and_context_unit_rereading_training_instruction_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T16:19:05+09:00`
- summary: `document routed, registered, recorded, and receipt written`
