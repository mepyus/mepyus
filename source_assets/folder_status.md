# folder_status / source_assets

## 1. Folder Identity
- path: `source_assets`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `7`
- immediate_child_files: `1`
- file_types: `.md` x 1

## 3. Child Folders
- `baselines` -> `source_assets/baselines/folder_status.md`
- `declarations` -> `source_assets/declarations/folder_status.md`
- `directives` -> `source_assets/directives/folder_status.md`
- `external_case_inputs` -> `source_assets/external_case_inputs/folder_status.md`
- `handoffs` -> `source_assets/handoffs/folder_status.md`
- `legacy_misc` -> `source_assets/legacy_misc/folder_status.md`
- `session_notes` -> `source_assets/session_notes/folder_status.md`

## 4. Markdown Files
- `README.md`
  title: source_assets
  summary: 이 폴더는 루트에 섞이기 쉬운 source asset 계열 md를 앞으로 분리해서 넣기 위한 상위 정리 폴더다.

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `source_assets`
- inventory_manifest: `runtime/manifests/folder_inventory/source_assets.json`
- parent_folder: `.`
- related_status_files: `source_assets/folder_status.md`
- last_updated: `2026-04-03T16:19:12+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
