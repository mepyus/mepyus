# operation receipt / doc_token_efficiency_claude_codex_stdy_note_v0

## 1. Source
- doc_id: `doc_token_efficiency_claude_codex_stdy_note_v0`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/token_efficiency_claude_codex_stdy_note_v0.md`

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
- label_packet: `runtime/manifests/label_packets/doc_token_efficiency_claude_codex_stdy_note_v0_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260423_212807_596984_6ec386c9_97551d`
- idempotency_key: `95d25bed68e20231`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_token_efficiency_claude_codex_stdy_note_v0_label_packet.json` [evt_20260423_212807_4ff016be]
- `doc_registered` -> `inputs/external_cases/token_efficiency_claude_codex_stdy_note_v0.md` [evt_20260423_212807_3353aec4]
- `routing_normalized` -> `inputs/external_cases/token_efficiency_claude_codex_stdy_note_v0.md` [evt_20260423_212807_0dff86e6]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.md` [evt_20260423_212808_e010b493]
- `gmd_native_read_written` -> `app/work/observer_ingest_min/generated/gmd_native_read_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.json` [evt_20260423_212808_4c2fb0c8]
- `output_generated` -> `runtime/views/multi_lens_document_reading/doc_token_efficiency_claude_codex_stdy_note_v0_multi_lens_readout_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.json` [evt_20260423_212808_00881c1f]
- `output_generated` -> `runtime/views/multi_lens_document_reading/doc_token_efficiency_claude_codex_stdy_note_v0_multi_lens_supervisor_surface_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.json` [evt_20260423_212808_19eeb7e9]
- `file_created` -> `runtime/manifests/origin_maps/doc_token_efficiency_claude_codex_stdy_note_v0_receipt_seed_origin_map.json` [evt_20260423_212808_89d00627]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_token_efficiency_claude_codex_stdy_note_v0_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.json`
- `app/work/observer_ingest_min/generated/split_units_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.json`
- `app/work/observer_ingest_min/generated/processing_trace_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.json`
- `app/work/observer_ingest_min/generated/readable_input_board_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.md`
- `app/work/observer_ingest_min/generated/operator_summary_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.md`
- `app/work/observer_ingest_min/generated/content_role_tags_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.json`
- `app/work/observer_ingest_min/generated/line_seed_bundles_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.json`
- `app/work/observer_ingest_min/generated/camera_support_bundles_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.json`
- `app/work/observer_ingest_min/generated/gmd_native_read_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.json`
- `runtime/views/multi_lens_document_reading/doc_token_efficiency_claude_codex_stdy_note_v0_multi_lens_readout_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.json`
- `runtime/views/multi_lens_document_reading/doc_token_efficiency_claude_codex_stdy_note_v0_multi_lens_supervisor_surface_token_efficiency_claude_codex_stdy_note_v0_20260423_212807.json`
- `runtime/manifests/origin_maps/doc_token_efficiency_claude_codex_stdy_note_v0_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260423_212807_596984_6ec386c9_97551d.md`

## 7A. GMD Native Read
- segmentation_basis: `{"split_mode_used": "heading", "dominant_unit_type": "heading_block", "unit_type_distribution": {"heading_block": 13}}`
- ordering_basis: `progressive_document_order`
- grouping_logic: `adjacent_units_in_native_document_order`
- role_hint_count: `13`
- relation_clue_count: `12`
- unresolved_count: `0`

## 7B. Semantic Commentary
- source_summary: `token_efficiency_claude_codex_stdy_note_v0 is being preserved as a structured source before VectorFL-specific line completion.`
- structure_summary: `The document currently reads as progressive_document_order with 13 units, dominated by heading_block.`
- why_this_structure_matters: `This native read keeps segmentation basis, role hints, and relation clues available before line translation and internal recall.`

## 7C. Translation-Ready Material
- source_block: `{"source_type": "mixed", "source_name": "token_efficiency_claude_codex_stdy_note_v0", "source_unit": "heading_block", "source_context": "note", "why_this_unit_matters": "It preserves native document structure before VectorFL mapping."}`
- provisional_line_block_count: `8`
- uncertainty_block_count: `0`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc inputs/external_cases/token_efficiency_claude_codex_stdy_note_v0.md --record-line-thickening`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/token_efficiency_claude_codex_stdy_note_v0.md --label token_efficiency_claude_codex_stdy_note_v0 --profile auto`

## 9. Final Status
- processed_at: `2026-04-23T21:28:08+09:00`
- summary: `document routed, registered, recorded, and receipt written`
