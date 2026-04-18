# operation receipt / doc_raw_intake_gap_analysis_before_middle_layer_fix_v1

## 1. Source
- doc_id: `doc_raw_intake_gap_analysis_before_middle_layer_fix_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/raw_intake_gap_analysis_before_middle_layer_fix_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_raw_intake_gap_analysis_before_middle_layer_fix_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260409_184529_282317_68d83e36_b9cec6`
- idempotency_key: `d13675decc9f80ba`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_raw_intake_gap_analysis_before_middle_layer_fix_v1_label_packet.json` [evt_20260409_184529_9aeecfe6]
- `doc_registered` -> `docs/reports/raw_intake_gap_analysis_before_middle_layer_fix_v1.md` [evt_20260409_184529_41c7e834]
- `routing_normalized` -> `docs/reports/raw_intake_gap_analysis_before_middle_layer_fix_v1.md` [evt_20260409_184529_f942a506]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.md` [evt_20260409_184529_4b88f923]
- `gmd_native_read_written` -> `app/work/observer_ingest_min/generated/gmd_native_read_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json` [evt_20260409_184529_ec4d158b]
- `output_generated` -> `runtime/views/multi_lens_document_reading/doc_raw_intake_gap_analysis_before_middle_layer_fix_v1_multi_lens_readout_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json` [evt_20260409_184529_35dd4018]
- `output_generated` -> `runtime/views/multi_lens_document_reading/doc_raw_intake_gap_analysis_before_middle_layer_fix_v1_multi_lens_supervisor_surface_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json` [evt_20260409_184529_a9302b86]
- `file_created` -> `runtime/manifests/origin_maps/doc_raw_intake_gap_analysis_before_middle_layer_fix_v1_receipt_seed_origin_map.json` [evt_20260409_184529_7083c2e7]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_raw_intake_gap_analysis_before_middle_layer_fix_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json`
- `app/work/observer_ingest_min/generated/split_units_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json`
- `app/work/observer_ingest_min/generated/processing_trace_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json`
- `app/work/observer_ingest_min/generated/readable_input_board_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.md`
- `app/work/observer_ingest_min/generated/operator_summary_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.md`
- `app/work/observer_ingest_min/generated/gmd_native_read_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json`
- `runtime/views/multi_lens_document_reading/doc_raw_intake_gap_analysis_before_middle_layer_fix_v1_multi_lens_readout_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json`
- `runtime/views/multi_lens_document_reading/doc_raw_intake_gap_analysis_before_middle_layer_fix_v1_multi_lens_supervisor_surface_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json`
- `runtime/manifests/origin_maps/doc_raw_intake_gap_analysis_before_middle_layer_fix_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260409_184529_282317_68d83e36_b9cec6.md`

## 7A. GMD Native Read
- segmentation_basis: `{"split_mode_used": "heading", "dominant_unit_type": "heading_block", "unit_type_distribution": {"heading_block": 15}}`
- ordering_basis: `input_to_processing_to_result`
- grouping_logic: `adjacent_units_in_native_document_order`
- role_hint_count: `15`
- relation_clue_count: `14`
- unresolved_count: `0`

## 7B. Semantic Commentary
- source_summary: `raw_intake_gap_analysis_before_middle_layer_fix_v1 is being preserved as a structured source before VectorFL-specific line completion.`
- structure_summary: `The document currently reads as input_to_processing_to_result with 15 units, dominated by heading_block.`
- why_this_structure_matters: `This native read keeps segmentation basis, role hints, and relation clues available before line translation and internal recall.`

## 7C. Translation-Ready Material
- source_block: `{"source_type": "mixed", "source_name": "raw_intake_gap_analysis_before_middle_layer_fix_v1", "source_unit": "heading_block", "source_context": "note", "why_this_unit_matters": "It preserves native document structure before VectorFL mapping."}`
- provisional_line_block_count: `8`
- uncertainty_block_count: `0`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/raw_intake_gap_analysis_before_middle_layer_fix_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/raw_intake_gap_analysis_before_middle_layer_fix_v1.md --label raw_intake_gap_analysis_before_middle_layer_fix_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-04-09T18:45:29+09:00`
- summary: `document routed, registered, recorded, and receipt written`
