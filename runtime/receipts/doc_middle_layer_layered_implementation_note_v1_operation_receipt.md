# operation receipt / doc_middle_layer_layered_implementation_note_v1

## 1. Source
- doc_id: `doc_middle_layer_layered_implementation_note_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/specs/middle_layer_layered_implementation_note_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_middle_layer_layered_implementation_note_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_073643_922576_61b78f2c_4d0461`
- idempotency_key: `48f1fdde0fa70658`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_middle_layer_layered_implementation_note_v1_label_packet.json` [evt_20260328_073643_f2c8e43f]
- `doc_registered` -> `docs/specs/middle_layer_layered_implementation_note_v1.md` [evt_20260328_073643_aaaf52d6]
- `routing_normalized` -> `docs/specs/middle_layer_layered_implementation_note_v1.md` [evt_20260328_073643_8d5c583c]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_middle_layer_layered_implementation_note_v1_20260328_073644.md` [evt_20260328_073644_1f797250]
- `file_created` -> `runtime/manifests/origin_maps/doc_middle_layer_layered_implementation_note_v1_receipt_seed_origin_map.json` [evt_20260328_073644_315aec5c]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_middle_layer_layered_implementation_note_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_middle_layer_layered_implementation_note_v1_20260328_073644.json`
- `app/work/observer_ingest_min/generated/split_units_middle_layer_layered_implementation_note_v1_20260328_073644.json`
- `app/work/observer_ingest_min/generated/processing_trace_middle_layer_layered_implementation_note_v1_20260328_073644.json`
- `app/work/observer_ingest_min/generated/readable_input_board_middle_layer_layered_implementation_note_v1_20260328_073644.md`
- `app/work/observer_ingest_min/generated/operator_summary_middle_layer_layered_implementation_note_v1_20260328_073644.md`
- `runtime/manifests/origin_maps/doc_middle_layer_layered_implementation_note_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_073643_922576_61b78f2c_4d0461.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/specs/middle_layer_layered_implementation_note_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/specs/middle_layer_layered_implementation_note_v1.md --label middle_layer_layered_implementation_note_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T07:36:44+09:00`
- summary: `document routed, registered, recorded, and receipt written`
