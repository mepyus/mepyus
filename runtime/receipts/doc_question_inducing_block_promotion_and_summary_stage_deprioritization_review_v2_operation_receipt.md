# operation receipt / doc_question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2

## 1. Source
- doc_id: `doc_question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2.md`

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
- label_packet: `runtime/manifests/label_packets/doc_question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_183204_540630_0456f6fd_fcabb9`
- idempotency_key: `dc7dce07ac786669`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2_label_packet.json` [evt_20260328_183204_36c66feb]
- `doc_registered` -> `docs/reports/question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2.md` [evt_20260328_183204_e19f6251]
- `routing_normalized` -> `docs/reports/question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2.md` [evt_20260328_183204_8f963255]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2_20260328_183204.md` [evt_20260328_183205_14970241]
- `file_created` -> `runtime/manifests/origin_maps/doc_question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2_receipt_seed_origin_map.json` [evt_20260328_183205_8b0e477a]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2_20260328_183204.json`
- `app/work/observer_ingest_min/generated/split_units_question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2_20260328_183204.json`
- `app/work/observer_ingest_min/generated/processing_trace_question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2_20260328_183204.json`
- `app/work/observer_ingest_min/generated/readable_input_board_question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2_20260328_183204.md`
- `app/work/observer_ingest_min/generated/operator_summary_question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2_20260328_183204.md`
- `runtime/manifests/origin_maps/doc_question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_183204_540630_0456f6fd_fcabb9.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2.md --label question_inducing_block_promotion_and_summary_stage_deprioritization_review_v2 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T18:32:05+09:00`
- summary: `document routed, registered, recorded, and receipt written`
