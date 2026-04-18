# folder_status / docs/templates

## 1. Folder Identity
- path: `docs/templates`
- role_guess: Template lane for reusable document headers, formats, and skeletons.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `2`
- file_types: `.md` x 2

## 3. Child Folders
- none

## 4. Markdown Files
- `stage1_exploration_observation_note_template_v1.md`
  title: stage1_exploration_observation_note_template_v1
  summary: - input_ref: - focus_anchor: - focus_labels: - related_run_ids: - related_session_ids: - evidence_refs: - recorded_at:
- `structured_doc_routing_header_template_v1.md`
  title: structured_doc_routing_header_template_v1
  summary: [[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]]

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `docs.templates`
- inventory_manifest: `runtime/manifests/folder_inventory/docs.templates.json`
- parent_folder: `docs`
- related_status_files: `docs/templates/folder_status.md`
- last_updated: `2026-03-26T18:46:00+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
