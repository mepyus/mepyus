# folder_status / runtime/reports

## 1. Folder Identity
- path: `runtime/reports`
- role_guess: Report layer containing analysis, reviews, and result summaries.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `14`
- file_types: `.html` x 6, `.json` x 6, `.md` x 2

## 3. Child Folders
- none

## 4. Markdown Files
- `core_input_layer_labeler_stabilization_smoke_v1.md`
  title: core_input_layer_labeler_stabilization_smoke_v1
  summary: 이 문서는 `core input-layer labeler v1` 안정화 smoke 결과를 요약한 보고서다.
- `origin_map_minimum_validation_v1.md`
  title: origin_map_minimum_validation_v1
  summary: - source_doc: `codex_directive_origin_map_minimum_v1.md` - doc_id: `doc_codex_directive_origin_map_minimum_v1` - normalized_route: `directive / ingest_then_execute / high`

## 5. Code / Data Files
- json: `dust_field_view.json`, `measurement_view.json`, `region_atlas_view.json`, `source_fragment_view.json`, `space_graph_view.json`, `terrain_map_view.json`
- other: `dust_field_view.html`, `measurement_view.html`, `region_atlas_view.html`, `source_fragment_view.html`, `space_graph_view.html`, `terrain_map_view.html`

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `runtime.reports`
- inventory_manifest: `runtime/manifests/folder_inventory/runtime.reports.json`
- parent_folder: `runtime`
- related_status_files: `runtime/reports/folder_status.md`
- last_updated: `2026-04-05T16:50:15+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
