# operation receipt / doc_line_thickening_promotion_scope_v0

## 1. Source
- doc_id: `doc_line_thickening_promotion_scope_v0`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/line_thickening_promotion_scope_v0.md`

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
- label_packet: `runtime/manifests/label_packets/doc_line_thickening_promotion_scope_v0_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260402_192503_145573_d5ad9b3b_42e4e6`
- idempotency_key: `98d8bb38733f4ce0`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_line_thickening_promotion_scope_v0_label_packet.json` [evt_20260402_192503_f1b15222]
- `doc_registered` -> `docs/reports/line_thickening_promotion_scope_v0.md` [evt_20260402_192503_c367f850]
- `routing_normalized` -> `docs/reports/line_thickening_promotion_scope_v0.md` [evt_20260402_192503_8fd34f7e]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_line_thickening_promotion_scope_v0_20260402_192503.md` [evt_20260402_192503_e5338f6e]
- `file_created` -> `runtime/manifests/origin_maps/doc_line_thickening_promotion_scope_v0_receipt_seed_origin_map.json` [evt_20260402_192503_2a5ac5df]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_line_thickening_promotion_scope_v0_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_line_thickening_promotion_scope_v0_20260402_192503.json`
- `app/work/observer_ingest_min/generated/split_units_line_thickening_promotion_scope_v0_20260402_192503.json`
- `app/work/observer_ingest_min/generated/processing_trace_line_thickening_promotion_scope_v0_20260402_192503.json`
- `app/work/observer_ingest_min/generated/readable_input_board_line_thickening_promotion_scope_v0_20260402_192503.md`
- `app/work/observer_ingest_min/generated/operator_summary_line_thickening_promotion_scope_v0_20260402_192503.md`
- `runtime/manifests/origin_maps/doc_line_thickening_promotion_scope_v0_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260402_192503_145573_d5ad9b3b_42e4e6.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/line_thickening_promotion_scope_v0.md --record-line-thickening`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/line_thickening_promotion_scope_v0.md --label line_thickening_promotion_scope_v0 --profile auto`

## 9. Final Status
- processed_at: `2026-04-02T19:25:03+09:00`
- summary: `document routed, registered, recorded, and receipt written`
