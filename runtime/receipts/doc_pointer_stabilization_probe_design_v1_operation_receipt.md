# operation receipt / doc_pointer_stabilization_probe_design_v1

## 1. Source
- doc_id: `doc_pointer_stabilization_probe_design_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/pointer_stabilization_probe_design_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_pointer_stabilization_probe_design_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_191914_941199_7806504a_45a03f`
- idempotency_key: `6a738f9c85209f11`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_pointer_stabilization_probe_design_v1_label_packet.json` [evt_20260328_191915_ed8405e0]
- `doc_registered` -> `docs/reports/pointer_stabilization_probe_design_v1.md` [evt_20260328_191915_fd0daf4d]
- `routing_normalized` -> `docs/reports/pointer_stabilization_probe_design_v1.md` [evt_20260328_191915_50cff4b9]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_pointer_stabilization_probe_design_v1_20260328_191915.md` [evt_20260328_191916_705107d3]
- `file_created` -> `runtime/manifests/origin_maps/doc_pointer_stabilization_probe_design_v1_receipt_seed_origin_map.json` [evt_20260328_191916_fa03a243]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_pointer_stabilization_probe_design_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_pointer_stabilization_probe_design_v1_20260328_191915.json`
- `app/work/observer_ingest_min/generated/split_units_pointer_stabilization_probe_design_v1_20260328_191915.json`
- `app/work/observer_ingest_min/generated/processing_trace_pointer_stabilization_probe_design_v1_20260328_191915.json`
- `app/work/observer_ingest_min/generated/readable_input_board_pointer_stabilization_probe_design_v1_20260328_191915.md`
- `app/work/observer_ingest_min/generated/operator_summary_pointer_stabilization_probe_design_v1_20260328_191915.md`
- `runtime/manifests/origin_maps/doc_pointer_stabilization_probe_design_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_191914_941199_7806504a_45a03f.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/pointer_stabilization_probe_design_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/pointer_stabilization_probe_design_v1.md --label pointer_stabilization_probe_design_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T19:19:16+09:00`
- summary: `document routed, registered, recorded, and receipt written`
