# operation receipt / doc_domain_specific_vs_reusable_split_note_v1

## 1. Source
- doc_id: `doc_domain_specific_vs_reusable_split_note_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/domain_specific_vs_reusable_split_note_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_domain_specific_vs_reusable_split_note_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_193340_064045_9e758c05_c00500`
- idempotency_key: `d3b5b9b32a60325f`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_domain_specific_vs_reusable_split_note_v1_label_packet.json` [evt_20260328_193340_0cd657af]
- `doc_registered` -> `docs/reports/domain_specific_vs_reusable_split_note_v1.md` [evt_20260328_193340_5bf44832]
- `routing_normalized` -> `docs/reports/domain_specific_vs_reusable_split_note_v1.md` [evt_20260328_193340_d80c487e]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_domain_specific_vs_reusable_split_note_v1_20260328_193340.md` [evt_20260328_193342_40b2be5a]
- `file_created` -> `runtime/manifests/origin_maps/doc_domain_specific_vs_reusable_split_note_v1_receipt_seed_origin_map.json` [evt_20260328_193343_d007d217]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_domain_specific_vs_reusable_split_note_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_domain_specific_vs_reusable_split_note_v1_20260328_193340.json`
- `app/work/observer_ingest_min/generated/split_units_domain_specific_vs_reusable_split_note_v1_20260328_193340.json`
- `app/work/observer_ingest_min/generated/processing_trace_domain_specific_vs_reusable_split_note_v1_20260328_193340.json`
- `app/work/observer_ingest_min/generated/readable_input_board_domain_specific_vs_reusable_split_note_v1_20260328_193340.md`
- `app/work/observer_ingest_min/generated/operator_summary_domain_specific_vs_reusable_split_note_v1_20260328_193340.md`
- `runtime/manifests/origin_maps/doc_domain_specific_vs_reusable_split_note_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_193340_064045_9e758c05_c00500.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/domain_specific_vs_reusable_split_note_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/domain_specific_vs_reusable_split_note_v1.md --label domain_specific_vs_reusable_split_note_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T19:33:43+09:00`
- summary: `document routed, registered, recorded, and receipt written`
