# operation receipt / doc_multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1

## 1. Source
- doc_id: `doc_multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_163200_217583_4bdc8bb3_dfd115`
- idempotency_key: `a53fc5a91980ea51`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1_label_packet.json` [evt_20260328_163200_4f0accf0]
- `doc_registered` -> `source_assets/baselines/multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1.md` [evt_20260328_163200_2cba1fc8]
- `routing_normalized` -> `source_assets/baselines/multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1.md` [evt_20260328_163200_c30a1c7d]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1_20260328_163200.md` [evt_20260328_163200_6d6c6131]
- `file_created` -> `runtime/manifests/origin_maps/doc_multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1_receipt_seed_origin_map.json` [evt_20260328_163200_98a773d7]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1_20260328_163200.json`
- `app/work/observer_ingest_min/generated/split_units_multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1_20260328_163200.json`
- `app/work/observer_ingest_min/generated/processing_trace_multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1_20260328_163200.json`
- `app/work/observer_ingest_min/generated/readable_input_board_multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1_20260328_163200.md`
- `app/work/observer_ingest_min/generated/operator_summary_multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1_20260328_163200.md`
- `runtime/manifests/origin_maps/doc_multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_163200_217583_4bdc8bb3_dfd115.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc source_assets/baselines/multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1.md --label multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T16:32:00+09:00`
- summary: `document routed, registered, recorded, and receipt written`
