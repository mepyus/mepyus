# operation receipt / doc_ai_future_segment_probe_v1

## 1. Source
- doc_id: `doc_ai_future_segment_probe_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/ai_future_segment_probe_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_ai_future_segment_probe_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_081912_197036_23bb2177_8e08ea`
- idempotency_key: `8d4b0a3973760b5f`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_ai_future_segment_probe_v1_label_packet.json` [evt_20260328_081912_973ec031]
- `doc_registered` -> `docs/reports/ai_future_segment_probe_v1.md` [evt_20260328_081912_3f1780e6]
- `routing_normalized` -> `docs/reports/ai_future_segment_probe_v1.md` [evt_20260328_081912_b02a381d]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_ai_future_segment_probe_v1_20260328_081912.md` [evt_20260328_081912_1c684d6a]
- `file_created` -> `runtime/manifests/origin_maps/doc_ai_future_segment_probe_v1_receipt_seed_origin_map.json` [evt_20260328_081912_ce49a051]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_ai_future_segment_probe_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_ai_future_segment_probe_v1_20260328_081912.json`
- `app/work/observer_ingest_min/generated/split_units_ai_future_segment_probe_v1_20260328_081912.json`
- `app/work/observer_ingest_min/generated/processing_trace_ai_future_segment_probe_v1_20260328_081912.json`
- `app/work/observer_ingest_min/generated/readable_input_board_ai_future_segment_probe_v1_20260328_081912.md`
- `app/work/observer_ingest_min/generated/operator_summary_ai_future_segment_probe_v1_20260328_081912.md`
- `runtime/manifests/origin_maps/doc_ai_future_segment_probe_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_081912_197036_23bb2177_8e08ea.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/ai_future_segment_probe_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/ai_future_segment_probe_v1.md --label ai_future_segment_probe_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T08:19:12+09:00`
- summary: `document routed, registered, recorded, and receipt written`
