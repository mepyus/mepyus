# folder_status / app/work/dialogue_loop_test

## 1. Folder Identity
- path: `app/work/dialogue_loop_test`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `1`
- immediate_child_files: `1`
- file_types: `.md` x 1

## 3. Child Folders
- `generated` -> `app/work/dialogue_loop_test/generated/folder_status.md`

## 4. Markdown Files
- `README.md`
  title: Dialogue Loop Test Family
  summary: 이 폴더는 지금 시점에서 `archive_review` 로 내리지 않는 살아있는 emergent line belt다.

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `app.work.dialogue_loop_test`
- inventory_manifest: `runtime/manifests/folder_inventory/app.work.dialogue_loop_test.json`
- parent_folder: `app/work`
- related_status_files: `app/work/dialogue_loop_test/folder_status.md`
- last_updated: `2026-04-05T10:32:21+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
