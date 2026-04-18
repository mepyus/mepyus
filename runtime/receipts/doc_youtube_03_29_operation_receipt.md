# operation receipt / doc_youtube_03_29

## 1. Source
- doc_id: `doc_youtube_03_29`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/youtube_03_29.md`

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
- label_packet: `runtime/manifests/label_packets/doc_youtube_03_29_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260401_205101_123577_1cc992a0_4c6edd`
- idempotency_key: `8996f3895aee0fad`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_youtube_03_29_label_packet.json` [evt_20260401_205101_ebb06ab5]
- `doc_registered` -> `inputs/external_cases/youtube_03_29.md` [evt_20260401_205101_22d084fd]
- `routing_normalized` -> `inputs/external_cases/youtube_03_29.md` [evt_20260401_205101_f35295c6]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_youtube_03_29_20260401_205101.md` [evt_20260401_205101_bf4a293a]
- `file_created` -> `runtime/manifests/origin_maps/doc_youtube_03_29_receipt_seed_origin_map.json` [evt_20260401_205101_d4abd3b1]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_youtube_03_29_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_youtube_03_29_20260401_205101.json`
- `app/work/observer_ingest_min/generated/split_units_youtube_03_29_20260401_205101.json`
- `app/work/observer_ingest_min/generated/processing_trace_youtube_03_29_20260401_205101.json`
- `app/work/observer_ingest_min/generated/readable_input_board_youtube_03_29_20260401_205101.md`
- `app/work/observer_ingest_min/generated/operator_summary_youtube_03_29_20260401_205101.md`
- `runtime/manifests/origin_maps/doc_youtube_03_29_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260401_205101_123577_1cc992a0_4c6edd.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc inputs/external_cases/youtube_03_29.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/youtube_03_29.md --label youtube_03_29 --profile auto`

## 9. Final Status
- processed_at: `2026-04-01T20:51:01+09:00`
- summary: `document routed, registered, recorded, and receipt written`
