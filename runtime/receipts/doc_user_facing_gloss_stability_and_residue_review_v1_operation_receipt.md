# operation receipt / doc_user_facing_gloss_stability_and_residue_review_v1

## 1. Source
- doc_id: `doc_user_facing_gloss_stability_and_residue_review_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/user_facing_gloss_stability_and_residue_review_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_user_facing_gloss_stability_and_residue_review_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_093849_235010_75c88fb0_0ba7aa`
- idempotency_key: `0099020c52c3ec8a`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_user_facing_gloss_stability_and_residue_review_v1_label_packet.json` [evt_20260328_093849_96f16b7a]
- `doc_registered` -> `docs/reports/user_facing_gloss_stability_and_residue_review_v1.md` [evt_20260328_093849_be6ca595]
- `routing_normalized` -> `docs/reports/user_facing_gloss_stability_and_residue_review_v1.md` [evt_20260328_093849_99b36059]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_user_facing_gloss_stability_and_residue_review_v1_20260328_093849.md` [evt_20260328_093849_f60a7aaa]
- `file_created` -> `runtime/manifests/origin_maps/doc_user_facing_gloss_stability_and_residue_review_v1_receipt_seed_origin_map.json` [evt_20260328_093849_491e2872]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_user_facing_gloss_stability_and_residue_review_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_user_facing_gloss_stability_and_residue_review_v1_20260328_093849.json`
- `app/work/observer_ingest_min/generated/split_units_user_facing_gloss_stability_and_residue_review_v1_20260328_093849.json`
- `app/work/observer_ingest_min/generated/processing_trace_user_facing_gloss_stability_and_residue_review_v1_20260328_093849.json`
- `app/work/observer_ingest_min/generated/readable_input_board_user_facing_gloss_stability_and_residue_review_v1_20260328_093849.md`
- `app/work/observer_ingest_min/generated/operator_summary_user_facing_gloss_stability_and_residue_review_v1_20260328_093849.md`
- `runtime/manifests/origin_maps/doc_user_facing_gloss_stability_and_residue_review_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_093849_235010_75c88fb0_0ba7aa.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/user_facing_gloss_stability_and_residue_review_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/user_facing_gloss_stability_and_residue_review_v1.md --label user_facing_gloss_stability_and_residue_review_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T09:38:49+09:00`
- summary: `document routed, registered, recorded, and receipt written`
