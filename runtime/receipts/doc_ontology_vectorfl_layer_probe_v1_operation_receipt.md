# operation receipt / doc_ontology_vectorfl_layer_probe_v1

## 1. Source
- doc_id: `doc_ontology_vectorfl_layer_probe_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/ontology_vectorfl_layer_probe_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_ontology_vectorfl_layer_probe_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_085136_210343_ccea8889_dd8a0c`
- idempotency_key: `bd30f0a599aa5bcd`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_ontology_vectorfl_layer_probe_v1_label_packet.json` [evt_20260328_085136_19fcd414]
- `doc_registered` -> `docs/reports/ontology_vectorfl_layer_probe_v1.md` [evt_20260328_085136_740fe83f]
- `routing_normalized` -> `docs/reports/ontology_vectorfl_layer_probe_v1.md` [evt_20260328_085136_f81f01d4]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_ontology_vectorfl_layer_probe_v1_20260328_085136.md` [evt_20260328_085136_8481f5a1]
- `file_created` -> `runtime/manifests/origin_maps/doc_ontology_vectorfl_layer_probe_v1_receipt_seed_origin_map.json` [evt_20260328_085136_484ae2c0]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_ontology_vectorfl_layer_probe_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_ontology_vectorfl_layer_probe_v1_20260328_085136.json`
- `app/work/observer_ingest_min/generated/split_units_ontology_vectorfl_layer_probe_v1_20260328_085136.json`
- `app/work/observer_ingest_min/generated/processing_trace_ontology_vectorfl_layer_probe_v1_20260328_085136.json`
- `app/work/observer_ingest_min/generated/readable_input_board_ontology_vectorfl_layer_probe_v1_20260328_085136.md`
- `app/work/observer_ingest_min/generated/operator_summary_ontology_vectorfl_layer_probe_v1_20260328_085136.md`
- `runtime/manifests/origin_maps/doc_ontology_vectorfl_layer_probe_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_085136_210343_ccea8889_dd8a0c.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/ontology_vectorfl_layer_probe_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/ontology_vectorfl_layer_probe_v1.md --label ontology_vectorfl_layer_probe_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T08:51:36+09:00`
- summary: `document routed, registered, recorded, and receipt written`
