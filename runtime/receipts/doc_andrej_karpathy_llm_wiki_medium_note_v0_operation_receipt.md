# operation receipt / doc_andrej_karpathy_llm_wiki_medium_note_v0

## 1. Source
- doc_id: `doc_andrej_karpathy_llm_wiki_medium_note_v0`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/andrej_karpathy_llm_wiki_medium_note_v0.md`

## 2. Raw Routing Markers
- DOCROLE: `memo`
- RUNMODE: `ingest_only`
- PRIORITY: `normal`

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
- label_packet: `runtime/manifests/label_packets/doc_andrej_karpathy_llm_wiki_medium_note_v0_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260423_144304_407287_10b488e0_452b7b`
- idempotency_key: `e1f7fed1c1321c10`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_andrej_karpathy_llm_wiki_medium_note_v0_label_packet.json` [evt_20260423_144304_b5d04eac]
- `doc_registered` -> `inputs/external_cases/andrej_karpathy_llm_wiki_medium_note_v0.md` [evt_20260423_144304_d5bbafa5]
- `routing_normalized` -> `inputs/external_cases/andrej_karpathy_llm_wiki_medium_note_v0.md` [evt_20260423_144304_dc3388b9]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.md` [evt_20260423_144304_d98c3c91]
- `gmd_native_read_written` -> `app/work/observer_ingest_min/generated/gmd_native_read_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.json` [evt_20260423_144304_3bc74795]
- `output_generated` -> `runtime/views/multi_lens_document_reading/doc_andrej_karpathy_llm_wiki_medium_note_v0_multi_lens_readout_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.json` [evt_20260423_144304_e6bd9201]
- `output_generated` -> `runtime/views/multi_lens_document_reading/doc_andrej_karpathy_llm_wiki_medium_note_v0_multi_lens_supervisor_surface_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.json` [evt_20260423_144304_cda5d8e6]
- `file_created` -> `runtime/manifests/origin_maps/doc_andrej_karpathy_llm_wiki_medium_note_v0_receipt_seed_origin_map.json` [evt_20260423_144305_98eba7cd]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_andrej_karpathy_llm_wiki_medium_note_v0_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.json`
- `app/work/observer_ingest_min/generated/split_units_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.json`
- `app/work/observer_ingest_min/generated/processing_trace_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.json`
- `app/work/observer_ingest_min/generated/readable_input_board_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.md`
- `app/work/observer_ingest_min/generated/operator_summary_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.md`
- `app/work/observer_ingest_min/generated/content_role_tags_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.json`
- `app/work/observer_ingest_min/generated/line_seed_bundles_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.json`
- `app/work/observer_ingest_min/generated/camera_support_bundles_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.json`
- `app/work/observer_ingest_min/generated/gmd_native_read_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.json`
- `runtime/views/multi_lens_document_reading/doc_andrej_karpathy_llm_wiki_medium_note_v0_multi_lens_readout_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.json`
- `runtime/views/multi_lens_document_reading/doc_andrej_karpathy_llm_wiki_medium_note_v0_multi_lens_supervisor_surface_andrej_karpathy_llm_wiki_medium_note_v0_20260423_144304.json`
- `runtime/manifests/origin_maps/doc_andrej_karpathy_llm_wiki_medium_note_v0_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260423_144304_407287_10b488e0_452b7b.md`

## 7A. GMD Native Read
- segmentation_basis: `{"split_mode_used": "heading", "dominant_unit_type": "heading_block", "unit_type_distribution": {"heading_block": 16}}`
- ordering_basis: `progressive_document_order`
- grouping_logic: `adjacent_units_in_native_document_order`
- role_hint_count: `16`
- relation_clue_count: `15`
- unresolved_count: `0`

## 7B. Semantic Commentary
- source_summary: `andrej_karpathy_llm_wiki_medium_note_v0 is being preserved as a structured source before VectorFL-specific line completion.`
- structure_summary: `The document currently reads as progressive_document_order with 16 units, dominated by heading_block.`
- why_this_structure_matters: `This native read keeps segmentation basis, role hints, and relation clues available before line translation and internal recall.`

## 7C. Translation-Ready Material
- source_block: `{"source_type": "mixed", "source_name": "andrej_karpathy_llm_wiki_medium_note_v0", "source_unit": "heading_block", "source_context": "note", "why_this_unit_matters": "It preserves native document structure before VectorFL mapping."}`
- provisional_line_block_count: `8`
- uncertainty_block_count: `0`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc inputs/external_cases/andrej_karpathy_llm_wiki_medium_note_v0.md --record-line-thickening`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/andrej_karpathy_llm_wiki_medium_note_v0.md --label andrej_karpathy_llm_wiki_medium_note_v0 --profile auto`

## 9. Final Status
- processed_at: `2026-04-23T14:43:05+09:00`
- summary: `document routed, registered, recorded, and receipt written`
