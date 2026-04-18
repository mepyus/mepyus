# operation receipt / doc_codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1

## 1. Source
- doc_id: `doc_codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md`

## 2. Raw Routing Markers
- DOCROLE: `directive`
- RUNMODE: `ingest_only`
- PRIORITY: `high`

## 3. Normalized Routing
- docrole: `directive`
- runmode: `ingest_only`
- priority: `high`

## 4. Registration
- input_class: `structured_internal_doc`
- processing_profile: `minimal_preprocess`
- material_grade: `grade_a`
- role: `directive`
- execution_linkable: `false`
- label_packet: `runtime/manifests/label_packets/doc_codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260325_184602_703669_3e3bcb9c_679f44`
- idempotency_key: `dc2d6acd02593de7`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1_label_packet.json` [evt_20260325_184602_97cec1e8]
- `doc_registered` -> `codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md` [evt_20260325_184602_14332827]
- `routing_normalized` -> `codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md` [evt_20260325_184602_f818d587]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1_20260325_184602.md` [evt_20260325_184602_870718f6]
- `file_created` -> `runtime/manifests/origin_maps/doc_codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1_receipt_seed_origin_map.json` [evt_20260325_184602_6f2ee7a2]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1_20260325_184602.json`
- `app/work/observer_ingest_min/generated/split_units_codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1_20260325_184602.json`
- `app/work/observer_ingest_min/generated/processing_trace_codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1_20260325_184602.json`
- `app/work/observer_ingest_min/generated/readable_input_board_codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1_20260325_184602.md`
- `app/work/observer_ingest_min/generated/operator_summary_codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1_20260325_184602.md`
- `runtime/manifests/origin_maps/doc_codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260325_184602_703669_3e3bcb9c_679f44.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md --label codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-25T18:46:02+09:00`
- summary: `document routed, registered, recorded, and receipt written`
