# operation receipt / doc_graphrag_neosh_negative_control_pass_v1

## 1. Source
- doc_id: `doc_graphrag_neosh_negative_control_pass_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/examples/graphrag_neosh_negative_control_pass_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_graphrag_neosh_negative_control_pass_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_063949_367899_4990d18a_4ab03e`
- idempotency_key: `116d2846aba7bedf`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_graphrag_neosh_negative_control_pass_v1_label_packet.json` [evt_20260328_063949_dad62276]
- `doc_registered` -> `docs/examples/graphrag_neosh_negative_control_pass_v1.md` [evt_20260328_063949_43d93296]
- `routing_normalized` -> `docs/examples/graphrag_neosh_negative_control_pass_v1.md` [evt_20260328_063949_ff80a364]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_graphrag_neosh_negative_control_pass_v1_20260328_063949.md` [evt_20260328_063949_58677da8]
- `file_created` -> `runtime/manifests/origin_maps/doc_graphrag_neosh_negative_control_pass_v1_receipt_seed_origin_map.json` [evt_20260328_063949_a9f3b6b3]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_graphrag_neosh_negative_control_pass_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_graphrag_neosh_negative_control_pass_v1_20260328_063949.json`
- `app/work/observer_ingest_min/generated/split_units_graphrag_neosh_negative_control_pass_v1_20260328_063949.json`
- `app/work/observer_ingest_min/generated/processing_trace_graphrag_neosh_negative_control_pass_v1_20260328_063949.json`
- `app/work/observer_ingest_min/generated/readable_input_board_graphrag_neosh_negative_control_pass_v1_20260328_063949.md`
- `app/work/observer_ingest_min/generated/operator_summary_graphrag_neosh_negative_control_pass_v1_20260328_063949.md`
- `runtime/manifests/origin_maps/doc_graphrag_neosh_negative_control_pass_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_063949_367899_4990d18a_4ab03e.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/examples/graphrag_neosh_negative_control_pass_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/examples/graphrag_neosh_negative_control_pass_v1.md --label graphrag_neosh_negative_control_pass_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T06:39:49+09:00`
- summary: `document routed, registered, recorded, and receipt written`
