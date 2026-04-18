# operation receipt / doc_interview_summary_stage_deprioritization_candidate_review_v1

## 1. Source
- doc_id: `doc_interview_summary_stage_deprioritization_candidate_review_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/interview_summary_stage_deprioritization_candidate_review_v1.md`

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
- label_packet: `runtime/manifests/label_packets/doc_interview_summary_stage_deprioritization_candidate_review_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 5A. Run Identity
- run_id: `run_20260328_095420_807177_96366b62_d4854c`
- idempotency_key: `816bb8c544f6c410`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_interview_summary_stage_deprioritization_candidate_review_v1_label_packet.json` [evt_20260328_095420_5f60fa20]
- `doc_registered` -> `docs/reports/interview_summary_stage_deprioritization_candidate_review_v1.md` [evt_20260328_095420_2925de35]
- `routing_normalized` -> `docs/reports/interview_summary_stage_deprioritization_candidate_review_v1.md` [evt_20260328_095420_2710c93a]
- `output_generated` -> `app/work/observer_ingest_min/generated/operator_summary_interview_summary_stage_deprioritization_candidate_review_v1_20260328_095420.md` [evt_20260328_095421_f2c433f5]
- `file_created` -> `runtime/manifests/origin_maps/doc_interview_summary_stage_deprioritization_candidate_review_v1_receipt_seed_origin_map.json` [evt_20260328_095421_8878dc5f]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_interview_summary_stage_deprioritization_candidate_review_v1_label_packet.json`
- `app/work/observer_ingest_min/generated/source_manifest_interview_summary_stage_deprioritization_candidate_review_v1_20260328_095420.json`
- `app/work/observer_ingest_min/generated/split_units_interview_summary_stage_deprioritization_candidate_review_v1_20260328_095420.json`
- `app/work/observer_ingest_min/generated/processing_trace_interview_summary_stage_deprioritization_candidate_review_v1_20260328_095420.json`
- `app/work/observer_ingest_min/generated/readable_input_board_interview_summary_stage_deprioritization_candidate_review_v1_20260328_095420.md`
- `app/work/observer_ingest_min/generated/operator_summary_interview_summary_stage_deprioritization_candidate_review_v1_20260328_095420.md`
- `runtime/manifests/origin_maps/doc_interview_summary_stage_deprioritization_candidate_review_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`
- `runtime/commands/structured_doc_routing_commands_run_20260328_095420_807177_96366b62_d4854c.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/interview_summary_stage_deprioritization_candidate_review_v1.md`
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 /Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py --input /Users/sungsookim/universe/vectorfl_replica/docs/reports/interview_summary_stage_deprioritization_candidate_review_v1.md --label interview_summary_stage_deprioritization_candidate_review_v1 --profile auto`

## 9. Final Status
- processed_at: `2026-03-28T09:54:21+09:00`
- summary: `document routed, registered, recorded, and receipt written`
