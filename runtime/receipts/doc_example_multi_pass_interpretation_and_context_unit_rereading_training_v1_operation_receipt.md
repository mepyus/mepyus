# operation receipt / doc_example_multi_pass_interpretation_and_context_unit_rereading_training_v1

## 1. Source
- doc_id: `doc_example_multi_pass_interpretation_and_context_unit_rereading_training_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/examples/example_multi_pass_interpretation_and_context_unit_rereading_training_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_example_multi_pass_interpretation_and_context_unit_rereading_training_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_161515_563510_1ff6f441_ef0efe`
- idempotency_key: `a83d3e801f0cde16`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_example_multi_pass_interpretation_and_context_unit_rereading_training_v1_label_packet.json` [evt_20260328_161515_41410a1d]
- `doc_registered` -> `docs/examples/example_multi_pass_interpretation_and_context_unit_rereading_training_v1.md` [evt_20260328_161515_abbd5493]
- `routing_normalized` -> `docs/examples/example_multi_pass_interpretation_and_context_unit_rereading_training_v1.md` [evt_20260328_161515_86706b99]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_example_multi_pass_interpretation_and_context_unit_rereading_training_v1_20260328_161515.md` [evt_20260328_161515_8df415c4]
- `file_created` -> `runtime/manifests/origin_maps/doc_example_multi_pass_interpretation_and_context_unit_rereading_training_v1_receipt_seed_origin_map.json` [evt_20260328_161515_4f1a8d8a]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_example_multi_pass_interpretation_and_context_unit_rereading_training_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_example_multi_pass_interpretation_and_context_unit_rereading_training_v1_20260328_161515.json`
- `app/work/observer_ingest_min/generated/split_units_example_multi_pass_interpretation_and_context_unit_rereading_training_v1_20260328_161515.json`
- `app/work/observer_ingest_min/generated/processing_trace_example_multi_pass_interpretation_and_context_unit_rereading_training_v1_20260328_161515.json`
- `app/work/observer_ingest_min/generated/readable_input_board_example_multi_pass_interpretation_and_context_unit_rereading_training_v1_20260328_161515.md`
- `app/work/observer_ingest_min/generated/operator_summary_example_multi_pass_interpretation_and_context_unit_rereading_training_v1_20260328_161515.md`
- `runtime/manifests/origin_maps/doc_example_multi_pass_interpretation_and_context_unit_rereading_training_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_161515_563510_1ff6f441_ef0efe.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/examples/example_multi_pass_interpretation_and_context_unit_rereading_training_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/examples/example_multi_pass_interpretation_and_context_unit_rereading_training_v1.md --label example_multi_pass_interpretation_and_context_unit_rereading_training_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T16:15:15+09:00`
- summary: `document routed, registered, recorded, and receipt written`
