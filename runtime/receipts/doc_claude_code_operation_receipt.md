# operation receipt / doc_claude_code

## 1. Source
- doc_id: `doc_claude_code`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/claude_code.txt`

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
- label_packet: `runtime/manifests/label_packets/doc_claude_code_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260401_205101_080026_52496924_cbbe56`
- idempotency_key: `51526c24a31375f7`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_claude_code_label_packet.json` [evt_20260401_205101_bd3f1746]
- `doc_registered` -> `inputs/external_cases/claude_code.txt` [evt_20260401_205101_318f23ad]
- `routing_normalized` -> `inputs/external_cases/claude_code.txt` [evt_20260401_205101_4bd04918]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_claude_code_20260401_205101.md` [evt_20260401_205101_a770e468]
- `file_created` -> `runtime/manifests/origin_maps/doc_claude_code_receipt_seed_origin_map.json` [evt_20260401_205101_8c6fe3cf]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_claude_code_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_claude_code_20260401_205101.json`
- `app/work/observer_ingest_min/generated/split_units_claude_code_20260401_205101.json`
- `app/work/observer_ingest_min/generated/processing_trace_claude_code_20260401_205101.json`
- `app/work/observer_ingest_min/generated/readable_input_board_claude_code_20260401_205101.md`
- `app/work/observer_ingest_min/generated/operator_summary_claude_code_20260401_205101.md`
- `runtime/manifests/origin_maps/doc_claude_code_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260401_205101_080026_52496924_cbbe56.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc inputs/external_cases/claude_code.txt`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/claude_code.txt --label claude_code --profile auto`

## 9. Final Status
- processed_at: `2026-04-01T20:51:01+09:00`
- summary: `document routed, registered, recorded, and receipt written`
