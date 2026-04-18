# operation receipt / doc_codex_directive_program_level_upgrade_delta_based_program_operation_v1

## 1. Source
- doc_id: `doc_codex_directive_program_level_upgrade_delta_based_program_operation_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/codex_directive_program_level_upgrade_delta_based_program_operation_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_codex_directive_program_level_upgrade_delta_based_program_operation_v1_label_packet.json`

## 5. Ticket
- ticket_id: `tkt_process_codex_directive_program_level_upgrade_delta_based_program_operation_v1`
- ticket_created: `yes`

## 5A. Run Identity
- run_id: `run_20260325_210935_640396_59f2fb6b_75de11`
- idempotency_key: `ce09a84621b417c7`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_codex_directive_program_level_upgrade_delta_based_program_operation_v1_label_packet.json` [evt_20260325_210935_4bb01c32]
- `doc_registered` -> `codex_directive_program_level_upgrade_delta_based_program_operation_v1.md` [evt_20260325_210935_03fc9929]
- `routing_normalized` -> `codex_directive_program_level_upgrade_delta_based_program_operation_v1.md` [evt_20260325_210935_28f804de]
- `ticket_created` -> `runtime/manifests/ticket_registry_v1.json` [evt_20260325_210935_d564729e]
- `execution_started` -> `codex_directive_program_level_upgrade_delta_based_program_operation_v1.md` [evt_20260325_210935_da68c5a0]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_codex_directive_program_level_upgrade_delta_based_program_operation_v1_20260325_210935.md` [evt_20260325_210935_1cd7ec16]
- `file_created` -> `runtime/manifests/origin_maps/doc_codex_directive_program_level_upgrade_delta_based_program_operation_v1_receipt_seed_origin_map.json` [evt_20260325_210935_1f054cf4]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_codex_directive_program_level_upgrade_delta_based_program_operation_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_codex_directive_program_level_upgrade_delta_based_program_operation_v1_20260325_210935.json`
- `app/work/observer_ingest_min/generated/split_units_codex_directive_program_level_upgrade_delta_based_program_operation_v1_20260325_210935.json`
- `app/work/observer_ingest_min/generated/processing_trace_codex_directive_program_level_upgrade_delta_based_program_operation_v1_20260325_210935.json`
- `app/work/observer_ingest_min/generated/readable_input_board_codex_directive_program_level_upgrade_delta_based_program_operation_v1_20260325_210935.md`
- `app/work/observer_ingest_min/generated/operator_summary_codex_directive_program_level_upgrade_delta_based_program_operation_v1_20260325_210935.md`
- `runtime/manifests/origin_maps/doc_codex_directive_program_level_upgrade_delta_based_program_operation_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260325_210935_640396_59f2fb6b_75de11.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc codex_directive_program_level_upgrade_delta_based_program_operation_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/codex_directive_program_level_upgrade_delta_based_program_operation_v1.md --label codex_directive_program_level_upgrade_delta_based_program_operation_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-25T21:09:35+09:00`
- summary: `document routed, registered, recorded, and receipt written`
