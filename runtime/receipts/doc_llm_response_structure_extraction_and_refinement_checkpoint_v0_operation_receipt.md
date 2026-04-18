# operation receipt / doc_llm_response_structure_extraction_and_refinement_checkpoint_v0

## 1. Source
- doc_id: `doc_llm_response_structure_extraction_and_refinement_checkpoint_v0`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/llm_response_structure_extraction_and_refinement_checkpoint_v0.md`

## 2. Raw Routing Markers
- DOCROLE: `directive`
- RUNMODE: `ingest_then_execute`
- PRIORITY: `high`

## 3. Normalized Routing
- docrole: `directive`
- runmode: `ingest_then_execute`
- priority: `high`

## 4. Registration
- input_class: `structured_internal_doc`
- processing_profile: `execution_coupled`
- material_grade: `grade_a`
- role: `directive`
- execution_linkable: `true`
- label_packet: `runtime/manifests/label_packets/doc_llm_response_structure_extraction_and_refinement_checkpoint_v0_label_packet.json`

## 5. Ticket
- ticket_id: `tkt_process_llm_response_structure_extraction_and_refinement_checkpoint_v0`
- ticket_created: `yes`

## 5A. Run Identity
- run_id: `run_20260326_185718_981304_eacd374e_db43d9`
- idempotency_key: `0f9d647097ab8e66`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_llm_response_structure_extraction_and_refinement_checkpoint_v0_label_packet.json` [evt_20260326_185718_47645df1]
- `doc_registered` -> `llm_response_structure_extraction_and_refinement_checkpoint_v0.md` [evt_20260326_185719_f3ca1661]
- `routing_normalized` -> `llm_response_structure_extraction_and_refinement_checkpoint_v0.md` [evt_20260326_185719_d3f2f66e]
- `ticket_created` -> `runtime/manifests/ticket_registry_v1.json` [evt_20260326_185719_81fe2b09]
- `execution_started` -> `llm_response_structure_extraction_and_refinement_checkpoint_v0.md` [evt_20260326_185719_8a1393da]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_llm_response_structure_extraction_and_refinement_checkpoint_v0_20260326_185719.md` [evt_20260326_185719_c15a0aa3]
- `file_created` -> `runtime/manifests/origin_maps/doc_llm_response_structure_extraction_and_refinement_checkpoint_v0_receipt_seed_origin_map.json` [evt_20260326_185719_52e81999]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_llm_response_structure_extraction_and_refinement_checkpoint_v0_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_llm_response_structure_extraction_and_refinement_checkpoint_v0_20260326_185719.json`
- `app/work/observer_ingest_min/generated/split_units_llm_response_structure_extraction_and_refinement_checkpoint_v0_20260326_185719.json`
- `app/work/observer_ingest_min/generated/processing_trace_llm_response_structure_extraction_and_refinement_checkpoint_v0_20260326_185719.json`
- `app/work/observer_ingest_min/generated/readable_input_board_llm_response_structure_extraction_and_refinement_checkpoint_v0_20260326_185719.md`
- `app/work/observer_ingest_min/generated/operator_summary_llm_response_structure_extraction_and_refinement_checkpoint_v0_20260326_185719.md`
- `runtime/manifests/origin_maps/doc_llm_response_structure_extraction_and_refinement_checkpoint_v0_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260326_185718_981304_eacd374e_db43d9.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc llm_response_structure_extraction_and_refinement_checkpoint_v0.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/llm_response_structure_extraction_and_refinement_checkpoint_v0.md --label llm_response_structure_extraction_and_refinement_checkpoint_v0 --profile auto`

## 9. Final Status
- processed_at: `2026-03-26T18:57:19+09:00`
- summary: `document routed, registered, recorded, and receipt written`
