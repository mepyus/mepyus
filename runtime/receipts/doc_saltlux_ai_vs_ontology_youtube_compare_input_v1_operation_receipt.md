# operation receipt / doc_saltlux_ai_vs_ontology_youtube_compare_input_v1

## 1. Source
- doc_id: `doc_saltlux_ai_vs_ontology_youtube_compare_input_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/source_assets/external_case_inputs/saltlux_ai_vs_ontology_youtube_compare_input_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_saltlux_ai_vs_ontology_youtube_compare_input_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_054427_875875_60ceddac_59c391`
- idempotency_key: `5f5f9be99bc113a6`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_saltlux_ai_vs_ontology_youtube_compare_input_v1_label_packet.json` [evt_20260328_054427_92a5b51f]
- `doc_registered` -> `source_assets/external_case_inputs/saltlux_ai_vs_ontology_youtube_compare_input_v1.md` [evt_20260328_054427_2df57115]
- `routing_normalized` -> `source_assets/external_case_inputs/saltlux_ai_vs_ontology_youtube_compare_input_v1.md` [evt_20260328_054427_bbb25b0d]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_saltlux_ai_vs_ontology_youtube_compare_input_v1_20260328_054427.md` [evt_20260328_054428_ad940a29]
- `file_created` -> `runtime/manifests/origin_maps/doc_saltlux_ai_vs_ontology_youtube_compare_input_v1_receipt_seed_origin_map.json` [evt_20260328_054428_b98c7316]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_saltlux_ai_vs_ontology_youtube_compare_input_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_saltlux_ai_vs_ontology_youtube_compare_input_v1_20260328_054427.json`
- `app/work/observer_ingest_min/generated/split_units_saltlux_ai_vs_ontology_youtube_compare_input_v1_20260328_054427.json`
- `app/work/observer_ingest_min/generated/processing_trace_saltlux_ai_vs_ontology_youtube_compare_input_v1_20260328_054427.json`
- `app/work/observer_ingest_min/generated/readable_input_board_saltlux_ai_vs_ontology_youtube_compare_input_v1_20260328_054427.md`
- `app/work/observer_ingest_min/generated/operator_summary_saltlux_ai_vs_ontology_youtube_compare_input_v1_20260328_054427.md`
- `runtime/manifests/origin_maps/doc_saltlux_ai_vs_ontology_youtube_compare_input_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_054427_875875_60ceddac_59c391.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc source_assets/external_case_inputs/saltlux_ai_vs_ontology_youtube_compare_input_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/source_assets/external_case_inputs/saltlux_ai_vs_ontology_youtube_compare_input_v1.md --label saltlux_ai_vs_ontology_youtube_compare_input_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T05:44:28+09:00`
- summary: `document routed, registered, recorded, and receipt written`
