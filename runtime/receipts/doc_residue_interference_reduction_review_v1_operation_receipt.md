# operation receipt / doc_residue_interference_reduction_review_v1

## 1. Source
- doc_id: `doc_residue_interference_reduction_review_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/source_assets/directives/residue_interference_reduction_review_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_residue_interference_reduction_review_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_094939_534199_a9b3d5cf_996531`
- idempotency_key: `97c5988498e65897`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_residue_interference_reduction_review_v1_label_packet.json` [evt_20260328_094939_bc6f00f3]
- `doc_registered` -> `source_assets/directives/residue_interference_reduction_review_v1.md` [evt_20260328_094939_b3682644]
- `routing_normalized` -> `source_assets/directives/residue_interference_reduction_review_v1.md` [evt_20260328_094939_3bbbe5d5]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_residue_interference_reduction_review_v1_20260328_094939.md` [evt_20260328_094939_5b7247bc]
- `file_created` -> `runtime/manifests/origin_maps/doc_residue_interference_reduction_review_v1_receipt_seed_origin_map.json` [evt_20260328_094939_aa7a0d44]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_residue_interference_reduction_review_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_residue_interference_reduction_review_v1_20260328_094939.json`
- `app/work/observer_ingest_min/generated/split_units_residue_interference_reduction_review_v1_20260328_094939.json`
- `app/work/observer_ingest_min/generated/processing_trace_residue_interference_reduction_review_v1_20260328_094939.json`
- `app/work/observer_ingest_min/generated/readable_input_board_residue_interference_reduction_review_v1_20260328_094939.md`
- `app/work/observer_ingest_min/generated/operator_summary_residue_interference_reduction_review_v1_20260328_094939.md`
- `runtime/manifests/origin_maps/doc_residue_interference_reduction_review_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_094939_534199_a9b3d5cf_996531.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc source_assets/directives/residue_interference_reduction_review_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/source_assets/directives/residue_interference_reduction_review_v1.md --label residue_interference_reduction_review_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T09:49:39+09:00`
- summary: `document routed, registered, recorded, and receipt written`
