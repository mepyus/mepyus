# operation receipt / doc_youtube_03_22_engine_purpose_reset_reading_v1

## 1. Source
- doc_id: `doc_youtube_03_22_engine_purpose_reset_reading_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/youtube_03_22_engine_purpose_reset_reading_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_youtube_03_22_engine_purpose_reset_reading_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_155012_437820_dc7ca192_8c4dfa`
- idempotency_key: `14cb9a611fe6d7a5`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_youtube_03_22_engine_purpose_reset_reading_v1_label_packet.json` [evt_20260328_155012_7f02cc36]
- `doc_registered` -> `docs/reports/youtube_03_22_engine_purpose_reset_reading_v1.md` [evt_20260328_155012_6e0c2250]
- `routing_normalized` -> `docs/reports/youtube_03_22_engine_purpose_reset_reading_v1.md` [evt_20260328_155012_eee53910]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_youtube_03_22_engine_purpose_reset_reading_v1_20260328_155012.md` [evt_20260328_155012_2eb544a2]
- `file_created` -> `runtime/manifests/origin_maps/doc_youtube_03_22_engine_purpose_reset_reading_v1_receipt_seed_origin_map.json` [evt_20260328_155012_c82e9c53]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_youtube_03_22_engine_purpose_reset_reading_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_youtube_03_22_engine_purpose_reset_reading_v1_20260328_155012.json`
- `app/work/observer_ingest_min/generated/split_units_youtube_03_22_engine_purpose_reset_reading_v1_20260328_155012.json`
- `app/work/observer_ingest_min/generated/processing_trace_youtube_03_22_engine_purpose_reset_reading_v1_20260328_155012.json`
- `app/work/observer_ingest_min/generated/readable_input_board_youtube_03_22_engine_purpose_reset_reading_v1_20260328_155012.md`
- `app/work/observer_ingest_min/generated/operator_summary_youtube_03_22_engine_purpose_reset_reading_v1_20260328_155012.md`
- `runtime/manifests/origin_maps/doc_youtube_03_22_engine_purpose_reset_reading_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_155012_437820_dc7ca192_8c4dfa.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/youtube_03_22_engine_purpose_reset_reading_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/youtube_03_22_engine_purpose_reset_reading_v1.md --label youtube_03_22_engine_purpose_reset_reading_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T15:50:12+09:00`
- summary: `document routed, registered, recorded, and receipt written`
