# operation receipt / doc_codex_baseline_program_grade_workspace_upgrade_v1

## 1. Source
- doc_id: `doc_codex_baseline_program_grade_workspace_upgrade_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_codex_baseline_program_grade_workspace_upgrade_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260327_214720_354070_0665c714_bbf376`
- idempotency_key: `c2d2edf39c0640f7`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_codex_baseline_program_grade_workspace_upgrade_v1_label_packet.json` [evt_20260327_214720_a30a44cf]
- `doc_registered` -> `docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md` [evt_20260327_214720_d3a0b57f]
- `routing_normalized` -> `docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md` [evt_20260327_214720_48d16b69]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_codex_baseline_program_grade_workspace_upgrade_v1_20260327_214720.md` [evt_20260327_214720_e1f488ce]
- `file_created` -> `runtime/manifests/origin_maps/doc_codex_baseline_program_grade_workspace_upgrade_v1_receipt_seed_origin_map.json` [evt_20260327_214720_09651852]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_codex_baseline_program_grade_workspace_upgrade_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_codex_baseline_program_grade_workspace_upgrade_v1_20260327_214720.json`
- `app/work/observer_ingest_min/generated/split_units_codex_baseline_program_grade_workspace_upgrade_v1_20260327_214720.json`
- `app/work/observer_ingest_min/generated/processing_trace_codex_baseline_program_grade_workspace_upgrade_v1_20260327_214720.json`
- `app/work/observer_ingest_min/generated/readable_input_board_codex_baseline_program_grade_workspace_upgrade_v1_20260327_214720.md`
- `app/work/observer_ingest_min/generated/operator_summary_codex_baseline_program_grade_workspace_upgrade_v1_20260327_214720.md`
- `runtime/manifests/origin_maps/doc_codex_baseline_program_grade_workspace_upgrade_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260327_214720_354070_0665c714_bbf376.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md --label codex_baseline_program_grade_workspace_upgrade_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-27T21:47:20+09:00`
- summary: `document routed, registered, recorded, and receipt written`
