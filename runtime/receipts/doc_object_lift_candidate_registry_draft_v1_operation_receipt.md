# operation receipt / doc_object_lift_candidate_registry_draft_v1

## 1. Source
- doc_id: `doc_object_lift_candidate_registry_draft_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/object_lift_candidate_registry_draft_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_object_lift_candidate_registry_draft_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_193340_145725_5ba6c6d9_b98529`
- idempotency_key: `4eb92263aee2e9fb`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_object_lift_candidate_registry_draft_v1_label_packet.json` [evt_20260328_193340_5156d688]
- `doc_registered` -> `docs/reports/object_lift_candidate_registry_draft_v1.md` [evt_20260328_193340_7eabefc6]
- `routing_normalized` -> `docs/reports/object_lift_candidate_registry_draft_v1.md` [evt_20260328_193340_ca8af34f]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_object_lift_candidate_registry_draft_v1_20260328_193341.md` [evt_20260328_193342_511f773b]
- `file_created` -> `runtime/manifests/origin_maps/doc_object_lift_candidate_registry_draft_v1_receipt_seed_origin_map.json` [evt_20260328_193343_bfe3e3c7]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_object_lift_candidate_registry_draft_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_object_lift_candidate_registry_draft_v1_20260328_193341.json`
- `app/work/observer_ingest_min/generated/split_units_object_lift_candidate_registry_draft_v1_20260328_193341.json`
- `app/work/observer_ingest_min/generated/processing_trace_object_lift_candidate_registry_draft_v1_20260328_193341.json`
- `app/work/observer_ingest_min/generated/readable_input_board_object_lift_candidate_registry_draft_v1_20260328_193341.md`
- `app/work/observer_ingest_min/generated/operator_summary_object_lift_candidate_registry_draft_v1_20260328_193341.md`
- `runtime/manifests/origin_maps/doc_object_lift_candidate_registry_draft_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_193340_145725_5ba6c6d9_b98529.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/object_lift_candidate_registry_draft_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/object_lift_candidate_registry_draft_v1.md --label object_lift_candidate_registry_draft_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T19:33:43+09:00`
- summary: `document routed, registered, recorded, and receipt written`
