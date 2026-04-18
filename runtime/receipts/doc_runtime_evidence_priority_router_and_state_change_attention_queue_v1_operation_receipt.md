# doc_runtime_evidence_priority_router_and_state_change_attention_queue_v1_operation_receipt.md

- operation_date: 2026-03-28
- operation_scope: runtime evidence priority routing + state change attention queue wiring
- prepared_by: Codex

## changed assets

- `docs/specs/runtime_evidence_priority_router_v1.md`
- `docs/reports/runtime_evidence_priority_router_v1_report.md`
- `docs/specs/state_change_attention_queue_v1.md`
- `docs/reports/state_change_attention_queue_v1_report.md`
- `app/runtime/runtime_evidence_priority_router.py`
- `app/runtime/state_change_attention_queue.py`
- `app/runtime/process_console_view/builder.py`
- `app/runtime/process_console_view/render.py`
- `app/runtime/engine_state_runtime_update_bridge.py`
- `runtime/views/state_change_attention_queue/index.json`

## validation

- `python3 -m py_compile app/runtime/runtime_evidence_priority_router.py app/runtime/state_change_attention_queue.py app/runtime/process_console_view/builder.py app/runtime/process_console_view/render.py app/runtime/engine_state_runtime_update_bridge.py`
- rebuilt queue surface from current runtime state
- representative assets resolved into background provenance summaries without canonical drift inflation

## result

- process console now reads an added attention layer on top of latest/history/diff
- provenance-only runtime adoption runs stay suppressed from active queue
- queue remains derived; canonical history and latest surfaces remain authoritative
