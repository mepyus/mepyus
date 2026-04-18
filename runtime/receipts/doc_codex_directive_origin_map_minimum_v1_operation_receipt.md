# operation receipt / doc_codex_directive_origin_map_minimum_v1

## 1. Source
- doc_id: `doc_codex_directive_origin_map_minimum_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/codex_directive_origin_map_minimum_v1.md`

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
- execution_linkable: `true`

## 5. Ticket
- ticket_id: `tkt_process_codex_directive_origin_map_minimum_v1`
- ticket_created: `yes`

## 6. Events
- `doc_registered` -> `codex_directive_origin_map_minimum_v1.md` [evt_20260324_203621_21a4e2d0]
- `routing_normalized` -> `codex_directive_origin_map_minimum_v1.md` [evt_20260324_203621_87c946fc]
- `ticket_created` -> `runtime/manifests/ticket_registry_v1.json` [evt_20260324_203621_04a1e8e5]
- `execution_started` -> `codex_directive_origin_map_minimum_v1.md` [evt_20260324_203621_a76d453a]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_codex_directive_origin_map_minimum_v1_20260324_203621.md` [evt_20260324_203621_fd9652bb]
- `file_created` -> `runtime/manifests/origin_maps/doc_codex_directive_origin_map_minimum_v1_receipt_seed_origin_map.json` [evt_20260324_203621_fab11340]

## 7. Generated / Updated Files
- `app/work/observer_ingest_min/generated/source_manifest_codex_directive_origin_map_minimum_v1_20260324_203621.json`
- `app/work/observer_ingest_min/generated/split_units_codex_directive_origin_map_minimum_v1_20260324_203621.json`
- `app/work/observer_ingest_min/generated/processing_trace_codex_directive_origin_map_minimum_v1_20260324_203621.json`
- `app/work/observer_ingest_min/generated/readable_input_board_codex_directive_origin_map_minimum_v1_20260324_203621.md`
- `app/work/observer_ingest_min/generated/operator_summary_codex_directive_origin_map_minimum_v1_20260324_203621.md`
- `runtime/manifests/origin_maps/doc_codex_directive_origin_map_minimum_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc codex_directive_origin_map_minimum_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/codex_directive_origin_map_minimum_v1.md --label codex_directive_origin_map_minimum_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-24T20:36:21+09:00`
- summary: `document routed, registered, recorded, and receipt written`
