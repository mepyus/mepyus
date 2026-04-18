# folder_status / inputs

## 1. Folder Identity
- path: `inputs`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `3`
- immediate_child_files: `2`
- file_types: `.md` x 1, `<no_ext>` x 1

## 3. Child Folders
- `external_cases` -> `inputs/external_cases/folder_status.md`
- `internal_notes` -> `inputs/internal_notes/folder_status.md`
- `reference_docs` -> `inputs/reference_docs/folder_status.md`

## 4. Markdown Files
- `README.md`
  title: inputs
  summary: 이 폴더는 사람이 넣는 입력 재료의 기본 드롭존이다.

## 5. Code / Data Files
- other: `.DS_Store`

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `inputs`
- inventory_manifest: `runtime/manifests/folder_inventory/inputs.json`
- parent_folder: `.`
- related_status_files: `inputs/folder_status.md`
- last_updated: `2026-04-02T21:59:12+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
