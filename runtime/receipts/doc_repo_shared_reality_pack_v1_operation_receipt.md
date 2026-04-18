# operation receipt / doc_repo_shared_reality_pack_v1

## 1. Source
- doc_id: `doc_repo_shared_reality_pack_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/repo_shared_reality_pack_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_repo_shared_reality_pack_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260327_214437_083830_00c05ed1_152fce`
- idempotency_key: `6399e2c3da314f4f`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_repo_shared_reality_pack_v1_label_packet.json` [evt_20260327_214437_637981f9]
- `doc_registered` -> `source_assets/baselines/repo_shared_reality_pack_v1.md` [evt_20260327_214437_fe6fc621]
- `routing_normalized` -> `source_assets/baselines/repo_shared_reality_pack_v1.md` [evt_20260327_214437_b7d86f15]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_repo_shared_reality_pack_v1_20260327_214437.md` [evt_20260327_214437_b91e99c1]
- `file_created` -> `runtime/manifests/origin_maps/doc_repo_shared_reality_pack_v1_receipt_seed_origin_map.json` [evt_20260327_214437_c00a323a]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_repo_shared_reality_pack_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_repo_shared_reality_pack_v1_20260327_214437.json`
- `app/work/observer_ingest_min/generated/split_units_repo_shared_reality_pack_v1_20260327_214437.json`
- `app/work/observer_ingest_min/generated/processing_trace_repo_shared_reality_pack_v1_20260327_214437.json`
- `app/work/observer_ingest_min/generated/readable_input_board_repo_shared_reality_pack_v1_20260327_214437.md`
- `app/work/observer_ingest_min/generated/operator_summary_repo_shared_reality_pack_v1_20260327_214437.md`
- `runtime/manifests/origin_maps/doc_repo_shared_reality_pack_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260327_214437_083830_00c05ed1_152fce.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc source_assets/baselines/repo_shared_reality_pack_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/repo_shared_reality_pack_v1.md --label repo_shared_reality_pack_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-27T21:44:37+09:00`
- summary: `document routed, registered, recorded, and receipt written`
