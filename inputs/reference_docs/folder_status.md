# folder_status / inputs/reference_docs

## 1. Folder Identity
- path: `inputs/reference_docs`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `1`
- file_types: `.md` x 1

## 3. Child Folders
- none

## 4. Markdown Files
- `README.md`
  title: reference_docs
  summary: 구조화된 참고 문서를 넣는 위치다.

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `inputs.reference_docs`
- inventory_manifest: `runtime/manifests/folder_inventory/inputs.reference_docs.json`
- parent_folder: `inputs`
- related_status_files: `inputs/reference_docs/folder_status.md`
- last_updated: `2026-03-26T21:12:29+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
