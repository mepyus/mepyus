[[A]] [[OBJ:doc_process_console_history_drilldown_v1_operation_receipt]] [[SEM:receipt_for_process_console_history_lineage_surface]]

# doc_process_console_history_drilldown_v1_operation_receipt

- timestamp_utc: `2026-03-28T14:05:09Z`
- operation:
  - added asset-level history drill-down lineage surface to process console
- added_assets:
  - `docs/specs/process_console_history_drilldown_v1.md`
  - `docs/reports/process_console_history_drilldown_v1_report.md`
  - `app/runtime/process_console_history_loader.py`
  - `app/runtime/process_console_history_selectors.py`
- updated_assets:
  - `app/runtime/process_console_view/builder.py`
  - `app/runtime/process_console_view/render.py`
  - `runtime/views/repo_delta_log_latest_v1.md`
  - `runtime/logs/repo_delta_log.jsonl`
- lineage_locks:
  - `latest_first_history_drilldown_second`
  - `history_as_lineage_surface`
  - `provenance_first_reading`
  - `canonical_experimental_separation_kept`
  - `provenance_only_vs_canonical_change_split`
- verification:
  - `python3 -m py_compile app/runtime/process_console_history_loader.py app/runtime/process_console_history_selectors.py app/runtime/process_console_view/builder.py app/runtime/process_console_view/render.py app/core/runtime/viewer_server.py`
  - `python3 - <<'PY' ... build_process_console_view_data(runtime_root, asset_id=...) ... representative 4 + missing_asset ... PY`
- representative_check:
  - `youtube_03_22 -> loaded / runtime_evidence / provenance_only`
  - `openai_02_11 -> loaded / runtime_evidence / provenance_only`
  - `knowledge_editing_youtube -> loaded / runtime_evidence / provenance_only`
  - `gary_tan_brain -> loaded / runtime_evidence / provenance_only`
  - `missing_asset -> state_unavailable / history_unavailable`
- one_line_read:
  - 이번 작업으로 process console은 latest canonical state를 현재값으로만 보여주지 않고, 그 상태가 어떤 trigger와 evidence와 changed field 경로를 거쳐 형성됐는지 lineage로 다시 읽게 됐다.
