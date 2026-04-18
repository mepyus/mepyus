# operation receipt / doc_smoke_structured_doc_reference_case_v1

## 1. Source
- doc_id: `doc_smoke_structured_doc_reference_case_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/smoke_structured_doc_reference_case_v1.md`

## 2. Raw Routing Markers
- DOCROLE: `reference`
- RUNMODE: `reference_only`
- PRIORITY: `low`

## 3. Normalized Routing
- docrole: `reference`
- runmode: `reference_only`
- priority: `low`

## 4. Registration
- input_class: `structured_internal_doc`
- processing_profile: `reference_only`
- material_grade: `grade_a`
- role: `reference`
- execution_linkable: `false`
- label_packet: `runtime/manifests/label_packets/doc_smoke_structured_doc_reference_case_v1_label_packet.json`

## 5. Ticket
- ticket_id: `not_created`
- ticket_created: `no`

## 6. Events
- `file_created` -> `runtime/manifests/label_packets/doc_smoke_structured_doc_reference_case_v1_label_packet.json` [evt_20260324_213932_43b7662c]
- `doc_registered` -> `docs/reports/smoke_structured_doc_reference_case_v1.md` [evt_20260324_213932_97e6bceb]
- `routing_normalized` -> `docs/reports/smoke_structured_doc_reference_case_v1.md` [evt_20260324_213932_2d0da70e]
- `file_created` -> `runtime/manifests/origin_maps/doc_smoke_structured_doc_reference_case_v1_receipt_seed_origin_map.json` [evt_20260324_213932_ef564c7f]

## 7. Generated / Updated Files
- `runtime/manifests/label_packets/doc_smoke_structured_doc_reference_case_v1_label_packet.json`
- `runtime/manifests/origin_maps/doc_smoke_structured_doc_reference_case_v1_receipt_seed_origin_map.json`
- `runtime/commands/structured_doc_routing_commands_v1.md`

## 8. Commands
- `/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 scripts/process_structured_doc_with_routing.py --doc docs/reports/smoke_structured_doc_reference_case_v1.md`

## 9. Final Status
- processed_at: `2026-03-24T21:39:32+09:00`
- summary: `document routed, registered, recorded, and receipt written`
