# operation receipt / doc_same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1

## 1. Source
- doc_id: `doc_same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/examples/same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_062229_104206_f1405580_7fb5c6`
- idempotency_key: `bdff844893900cd3`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1_label_packet.json` [evt_20260328_062229_53676401]
- `doc_registered` -> `docs/examples/same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1.md` [evt_20260328_062229_43f75158]
- `routing_normalized` -> `docs/examples/same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1.md` [evt_20260328_062229_1d8d9a52]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1_20260328_062229.md` [evt_20260328_062229_c6534f86]
- `file_created` -> `runtime/manifests/origin_maps/doc_same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1_receipt_seed_origin_map.json` [evt_20260328_062229_028f8f3b]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1_20260328_062229.json`
- `app/work/observer_ingest_min/generated/split_units_same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1_20260328_062229.json`
- `app/work/observer_ingest_min/generated/processing_trace_same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1_20260328_062229.json`
- `app/work/observer_ingest_min/generated/readable_input_board_same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1_20260328_062229.md`
- `app/work/observer_ingest_min/generated/operator_summary_same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1_20260328_062229.md`
- `runtime/manifests/origin_maps/doc_same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_062229_104206_f1405580_7fb5c6.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/examples/same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/examples/same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1.md --label same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T06:22:29+09:00`
- summary: `document routed, registered, recorded, and receipt written`
