[[A]] [[OBJ:doc_state_change_diff_surface_v1_operation_receipt]] [[SEM:receipt_for_adjacent_canonical_state_diff_surface]]

# doc_state_change_diff_surface_v1_operation_receipt

- timestamp_utc: `2026-03-28T14:12:59Z`
- operation:
  - added adjacent canonical-state diff surface to process console
- added_assets:
  - `docs/specs/state_change_diff_surface_v1.md`
  - `docs/reports/state_change_diff_surface_v1_report.md`
  - `app/runtime/state_change_diff_loader.py`
  - `app/runtime/state_change_diff_selectors.py`
- updated_assets:
  - `app/runtime/process_console_view/builder.py`
  - `app/runtime/process_console_view/render.py`
  - `app/core/runtime/viewer_server.py`
  - `runtime/views/repo_delta_log_latest_v1.md`
  - `runtime/logs/repo_delta_log.jsonl`
- diff_locks:
  - `canonical_first_diff`
  - `adjacent_pair_compare`
  - `provenance_only_split`
  - `array_set_like_diff`
  - `experimental_hidden_by_default`
- verification:
  - `python3 -m py_compile app/runtime/state_change_diff_loader.py app/runtime/state_change_diff_selectors.py app/runtime/process_console_view/builder.py app/runtime/process_console_view/render.py app/core/runtime/viewer_server.py`
  - `python3 - <<'PY' ... latest vs previous diff for representative 4 assets ... PY`
  - `python3 - <<'PY' ... oldest record no_previous_state fallback ... PY`
- representative_check:
  - `youtube_03_22 -> loaded / provenance_only / changed_fields=[]`
  - `openai_02_11 -> loaded / provenance_only / changed_fields=[]`
  - `knowledge_editing_youtube -> loaded / provenance_only / changed_fields=[]`
  - `gary_tan_brain -> loaded / provenance_only / changed_fields=[]`
  - `knowledge_editing_youtube oldest -> no_previous_state`
  - `gary_tan_brain oldest -> no_previous_state`
- one_line_read:
  - 이번 작업으로 process console은 lineage를 넘어 adjacent canonical state 사이에서 실제 변화와 무변화를 빠르게 읽는 diff surface를 갖추게 됐고, current representative latest run은 canonical drift 없이 provenance-only update로 읽히도록 잠겼다.
