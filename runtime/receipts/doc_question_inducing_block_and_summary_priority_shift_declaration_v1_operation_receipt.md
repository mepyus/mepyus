# operation receipt / doc_question_inducing_block_and_summary_priority_shift_declaration_v1

## 1. Source
- doc_id: `doc_question_inducing_block_and_summary_priority_shift_declaration_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/source_assets/declarations/question_inducing_block_and_summary_priority_shift_declaration_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_question_inducing_block_and_summary_priority_shift_declaration_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_161310_289372_a223c5ab_35c91b`
- idempotency_key: `5355282871fa112c`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_question_inducing_block_and_summary_priority_shift_declaration_v1_label_packet.json` [evt_20260328_161310_1698885b]
- `doc_registered` -> `source_assets/declarations/question_inducing_block_and_summary_priority_shift_declaration_v1.md` [evt_20260328_161310_f1519c75]
- `routing_normalized` -> `source_assets/declarations/question_inducing_block_and_summary_priority_shift_declaration_v1.md` [evt_20260328_161310_2302a240]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_question_inducing_block_and_summary_priority_shift_declaration_v1_20260328_161310.md` [evt_20260328_161310_4ded263d]
- `file_created` -> `runtime/manifests/origin_maps/doc_question_inducing_block_and_summary_priority_shift_declaration_v1_receipt_seed_origin_map.json` [evt_20260328_161310_a2310e55]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_question_inducing_block_and_summary_priority_shift_declaration_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_question_inducing_block_and_summary_priority_shift_declaration_v1_20260328_161310.json`
- `app/work/observer_ingest_min/generated/split_units_question_inducing_block_and_summary_priority_shift_declaration_v1_20260328_161310.json`
- `app/work/observer_ingest_min/generated/processing_trace_question_inducing_block_and_summary_priority_shift_declaration_v1_20260328_161310.json`
- `app/work/observer_ingest_min/generated/readable_input_board_question_inducing_block_and_summary_priority_shift_declaration_v1_20260328_161310.md`
- `app/work/observer_ingest_min/generated/operator_summary_question_inducing_block_and_summary_priority_shift_declaration_v1_20260328_161310.md`
- `runtime/manifests/origin_maps/doc_question_inducing_block_and_summary_priority_shift_declaration_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_161310_289372_a223c5ab_35c91b.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc source_assets/declarations/question_inducing_block_and_summary_priority_shift_declaration_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/source_assets/declarations/question_inducing_block_and_summary_priority_shift_declaration_v1.md --label question_inducing_block_and_summary_priority_shift_declaration_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T16:13:10+09:00`
- summary: `document routed, registered, recorded, and receipt written`
