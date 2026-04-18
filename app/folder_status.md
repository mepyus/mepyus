# folder_status / app

## 1. Folder Identity
- path: `app`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `8`
- immediate_child_files: `2`
- file_types: `.py` x 1, `<no_ext>` x 1

## 3. Child Folders
- `core` -> `app/core/folder_status.md`
- `events` -> `app/events/folder_status.md`
- `fragment` -> `app/fragment/folder_status.md`
- `input_layer` -> `app/input_layer/folder_status.md`
- `measurement` -> `app/measurement/folder_status.md`
- `models` -> `app/models/folder_status.md`
- `runtime` -> `app/runtime/folder_status.md`
- `work` -> `app/work/folder_status.md`

## 4. Markdown Files
- none

## 5. Code / Data Files
- python: `generate_folder_status.py`
- other: `.DS_Store`

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `app`
- inventory_manifest: `runtime/manifests/folder_inventory/app.json`
- parent_folder: `.`
- related_status_files: `app/folder_status.md`
- last_updated: `2026-04-09T18:45:29+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
