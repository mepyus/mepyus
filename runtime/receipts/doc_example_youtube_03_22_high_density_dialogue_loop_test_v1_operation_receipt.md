# operation receipt / doc_example_youtube_03_22_high_density_dialogue_loop_test_v1

## 1. Source
- doc_id: `doc_example_youtube_03_22_high_density_dialogue_loop_test_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/examples/example_youtube_03_22_high_density_dialogue_loop_test_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_example_youtube_03_22_high_density_dialogue_loop_test_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_152138_347216_b8eb9feb_75d79e`
- idempotency_key: `164a88af494599c4`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_example_youtube_03_22_high_density_dialogue_loop_test_v1_label_packet.json` [evt_20260328_152138_0b6756bf]
- `doc_registered` -> `docs/examples/example_youtube_03_22_high_density_dialogue_loop_test_v1.md` [evt_20260328_152138_968f7396]
- `routing_normalized` -> `docs/examples/example_youtube_03_22_high_density_dialogue_loop_test_v1.md` [evt_20260328_152138_b53dc3f5]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_example_youtube_03_22_high_density_dialogue_loop_test_v1_20260328_152138.md` [evt_20260328_152139_c0bc545c]
- `file_created` -> `runtime/manifests/origin_maps/doc_example_youtube_03_22_high_density_dialogue_loop_test_v1_receipt_seed_origin_map.json` [evt_20260328_152139_b60bb22c]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_example_youtube_03_22_high_density_dialogue_loop_test_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_example_youtube_03_22_high_density_dialogue_loop_test_v1_20260328_152138.json`
- `app/work/observer_ingest_min/generated/split_units_example_youtube_03_22_high_density_dialogue_loop_test_v1_20260328_152138.json`
- `app/work/observer_ingest_min/generated/processing_trace_example_youtube_03_22_high_density_dialogue_loop_test_v1_20260328_152138.json`
- `app/work/observer_ingest_min/generated/readable_input_board_example_youtube_03_22_high_density_dialogue_loop_test_v1_20260328_152138.md`
- `app/work/observer_ingest_min/generated/operator_summary_example_youtube_03_22_high_density_dialogue_loop_test_v1_20260328_152138.md`
- `runtime/manifests/origin_maps/doc_example_youtube_03_22_high_density_dialogue_loop_test_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_152138_347216_b8eb9feb_75d79e.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/examples/example_youtube_03_22_high_density_dialogue_loop_test_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/examples/example_youtube_03_22_high_density_dialogue_loop_test_v1.md --label example_youtube_03_22_high_density_dialogue_loop_test_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T15:21:39+09:00`
- summary: `document routed, registered, recorded, and receipt written`
