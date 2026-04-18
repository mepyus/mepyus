# folder_status / runtime/observer

## 1. Folder Identity
- path: `runtime/observer`
- role_guess: Observer-facing output or review folder.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `2`
- immediate_child_files: `0`
- file_types: none

## 3. Child Folders
- `exploration` -> `runtime/observer/exploration/folder_status.md`
- `gemini` -> `runtime/observer/gemini/folder_status.md`

## 4. Markdown Files
- none

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `runtime.observer`
- inventory_manifest: `runtime/manifests/folder_inventory/runtime.observer.json`
- parent_folder: `runtime`
- related_status_files: `runtime/observer/folder_status.md`
- last_updated: `2026-04-05T16:50:15+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
