# operation receipt / doc_example_connection_translation_first_refinement_v1

## 1. Source
- doc_id: `doc_example_connection_translation_first_refinement_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/examples/example_connection_translation_first_refinement_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_example_connection_translation_first_refinement_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_095420_815011_59f6c352_60e70b`
- idempotency_key: `f95ef4de9bc24273`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_example_connection_translation_first_refinement_v1_label_packet.json` [evt_20260328_095420_6128750f]
- `doc_registered` -> `docs/examples/example_connection_translation_first_refinement_v1.md` [evt_20260328_095420_18960cc4]
- `routing_normalized` -> `docs/examples/example_connection_translation_first_refinement_v1.md` [evt_20260328_095420_24b16e87]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_example_connection_translation_first_refinement_v1_20260328_095420.md` [evt_20260328_095421_537853b8]
- `file_created` -> `runtime/manifests/origin_maps/doc_example_connection_translation_first_refinement_v1_receipt_seed_origin_map.json` [evt_20260328_095421_ff7d5510]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_example_connection_translation_first_refinement_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_example_connection_translation_first_refinement_v1_20260328_095420.json`
- `app/work/observer_ingest_min/generated/split_units_example_connection_translation_first_refinement_v1_20260328_095420.json`
- `app/work/observer_ingest_min/generated/processing_trace_example_connection_translation_first_refinement_v1_20260328_095420.json`
- `app/work/observer_ingest_min/generated/readable_input_board_example_connection_translation_first_refinement_v1_20260328_095420.md`
- `app/work/observer_ingest_min/generated/operator_summary_example_connection_translation_first_refinement_v1_20260328_095420.md`
- `runtime/manifests/origin_maps/doc_example_connection_translation_first_refinement_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_095420_815011_59f6c352_60e70b.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/examples/example_connection_translation_first_refinement_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/examples/example_connection_translation_first_refinement_v1.md --label example_connection_translation_first_refinement_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T09:54:21+09:00`
- summary: `document routed, registered, recorded, and receipt written`
