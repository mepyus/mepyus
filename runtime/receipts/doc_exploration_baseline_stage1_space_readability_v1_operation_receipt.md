# operation receipt / doc_exploration_baseline_stage1_space_readability_v1

## 1. Source
- doc_id: `doc_exploration_baseline_stage1_space_readability_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/exploration_baseline_stage1_space_readability_v1.md`

## 2. Raw Routing Markers
- DOCROLE: `baseline`
- RUNMODE: `ingest_then_execute`
- PRIORITY: `high`

## 3. Normalized Routing
- docrole: `baseline`
- runmode: `ingest_then_execute`
- priority: `high`

## 4. Registration
- input_class: `structured_internal_doc`
- processing_profile: `execution_coupled`
- material_grade: `grade_a`
- role: `baseline`
- execution_linkable: `true`
- label_packet: `runtime/manifests/label_packets/doc_exploration_baseline_stage1_space_readability_v1_label_packet.json`

## 5. Ticket
- ticket_id: `tkt_process_exploration_baseline_stage1_space_readability_v1`
- ticket_created: `yes`

## 5A. Run Identity
- run_id: `run_20260326_184359_982086_4eb1be1e_23c26d`
- idempotency_key: `e9aea40c7296e470`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_exploration_baseline_stage1_space_readability_v1_label_packet.json` [evt_20260326_184359_d48bd56b]
- `doc_registered` -> `exploration_baseline_stage1_space_readability_v1.md` [evt_20260326_184359_a3a08aa3]
- `routing_normalized` -> `exploration_baseline_stage1_space_readability_v1.md` [evt_20260326_184359_0b11ce08]
- `ticket_created` -> `runtime/manifests/ticket_registry_v1.json` [evt_20260326_184400_020821f6]
- `execution_started` -> `exploration_baseline_stage1_space_readability_v1.md` [evt_20260326_184400_236fb43d]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_exploration_baseline_stage1_space_readability_v1_20260326_184400.md` [evt_20260326_184400_b1be3274]
- `file_created` -> `runtime/manifests/origin_maps/doc_exploration_baseline_stage1_space_readability_v1_receipt_seed_origin_map.json` [evt_20260326_184400_01c6344a]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_exploration_baseline_stage1_space_readability_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_exploration_baseline_stage1_space_readability_v1_20260326_184400.json`
- `app/work/observer_ingest_min/generated/split_units_exploration_baseline_stage1_space_readability_v1_20260326_184400.json`
- `app/work/observer_ingest_min/generated/processing_trace_exploration_baseline_stage1_space_readability_v1_20260326_184400.json`
- `app/work/observer_ingest_min/generated/readable_input_board_exploration_baseline_stage1_space_readability_v1_20260326_184400.md`
- `app/work/observer_ingest_min/generated/operator_summary_exploration_baseline_stage1_space_readability_v1_20260326_184400.md`
- `runtime/manifests/origin_maps/doc_exploration_baseline_stage1_space_readability_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260326_184359_982086_4eb1be1e_23c26d.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc exploration_baseline_stage1_space_readability_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/exploration_baseline_stage1_space_readability_v1.md --label exploration_baseline_stage1_space_readability_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-26T18:44:00+09:00`
- summary: `document routed, registered, recorded, and receipt written`
