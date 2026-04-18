# operation receipt / doc_multi_pass_interpretation_and_context_unit_rereading_training_v2

## 1. Source
- doc_id: `doc_multi_pass_interpretation_and_context_unit_rereading_training_v2`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/multi_pass_interpretation_and_context_unit_rereading_training_v2.md`

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
- label_packet: `runtime/manifests/label_packets/doc_multi_pass_interpretation_and_context_unit_rereading_training_v2_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_183204_567030_a4de9bed_cecee9`
- idempotency_key: `44e35d03ac3685bd`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_multi_pass_interpretation_and_context_unit_rereading_training_v2_label_packet.json` [evt_20260328_183204_98fe6d01]
- `doc_registered` -> `docs/reports/multi_pass_interpretation_and_context_unit_rereading_training_v2.md` [evt_20260328_183204_713504bd]
- `routing_normalized` -> `docs/reports/multi_pass_interpretation_and_context_unit_rereading_training_v2.md` [evt_20260328_183204_4334bcea]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_multi_pass_interpretation_and_context_unit_rereading_training_v2_20260328_183204.md` [evt_20260328_183205_66e9d324]
- `file_created` -> `runtime/manifests/origin_maps/doc_multi_pass_interpretation_and_context_unit_rereading_training_v2_receipt_seed_origin_map.json` [evt_20260328_183205_e71d55e1]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_multi_pass_interpretation_and_context_unit_rereading_training_v2_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_multi_pass_interpretation_and_context_unit_rereading_training_v2_20260328_183204.json`
- `app/work/observer_ingest_min/generated/split_units_multi_pass_interpretation_and_context_unit_rereading_training_v2_20260328_183204.json`
- `app/work/observer_ingest_min/generated/processing_trace_multi_pass_interpretation_and_context_unit_rereading_training_v2_20260328_183204.json`
- `app/work/observer_ingest_min/generated/readable_input_board_multi_pass_interpretation_and_context_unit_rereading_training_v2_20260328_183204.md`
- `app/work/observer_ingest_min/generated/operator_summary_multi_pass_interpretation_and_context_unit_rereading_training_v2_20260328_183204.md`
- `runtime/manifests/origin_maps/doc_multi_pass_interpretation_and_context_unit_rereading_training_v2_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_183204_567030_a4de9bed_cecee9.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/multi_pass_interpretation_and_context_unit_rereading_training_v2.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/multi_pass_interpretation_and_context_unit_rereading_training_v2.md --label multi_pass_interpretation_and_context_unit_rereading_training_v2 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T18:32:05+09:00`
- summary: `document routed, registered, recorded, and receipt written`
