# operation receipt / doc_external_case_first_pass_andrewng_stanford_input_v1

## 1. Source
- doc_id: `doc_external_case_first_pass_andrewng_stanford_input_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/source_assets/external_case_inputs/external_case_first_pass_andrewng_stanford_input_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_external_case_first_pass_andrewng_stanford_input_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260326_215042_199261_1fc7f36d_b484b4`
- idempotency_key: `6017dcf5aff61e59`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_external_case_first_pass_andrewng_stanford_input_v1_label_packet.json` [evt_20260326_215042_390926aa]
- `doc_registered` -> `source_assets/external_case_inputs/external_case_first_pass_andrewng_stanford_input_v1.md` [evt_20260326_215042_7b105ff9]
- `routing_normalized` -> `source_assets/external_case_inputs/external_case_first_pass_andrewng_stanford_input_v1.md` [evt_20260326_215042_814d6b0e]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_external_case_first_pass_andrewng_stanford_input_v1_20260326_215042.md` [evt_20260326_215042_8c24e7b6]
- `file_created` -> `runtime/manifests/origin_maps/doc_external_case_first_pass_andrewng_stanford_input_v1_receipt_seed_origin_map.json` [evt_20260326_215042_e1a14896]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_external_case_first_pass_andrewng_stanford_input_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_external_case_first_pass_andrewng_stanford_input_v1_20260326_215042.json`
- `app/work/observer_ingest_min/generated/split_units_external_case_first_pass_andrewng_stanford_input_v1_20260326_215042.json`
- `app/work/observer_ingest_min/generated/processing_trace_external_case_first_pass_andrewng_stanford_input_v1_20260326_215042.json`
- `app/work/observer_ingest_min/generated/readable_input_board_external_case_first_pass_andrewng_stanford_input_v1_20260326_215042.md`
- `app/work/observer_ingest_min/generated/operator_summary_external_case_first_pass_andrewng_stanford_input_v1_20260326_215042.md`
- `runtime/manifests/origin_maps/doc_external_case_first_pass_andrewng_stanford_input_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260326_215042_199261_1fc7f36d_b484b4.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc source_assets/external_case_inputs/external_case_first_pass_andrewng_stanford_input_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/source_assets/external_case_inputs/external_case_first_pass_andrewng_stanford_input_v1.md --label external_case_first_pass_andrewng_stanford_input_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-26T21:50:42+09:00`
- summary: `document routed, registered, recorded, and receipt written`
