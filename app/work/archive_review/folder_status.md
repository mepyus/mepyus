# folder_status / app/work/archive_review

## 1. Folder Identity
- path: `app/work/archive_review`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `7`
- immediate_child_files: `0`
- file_types: none

## 3. Child Folders
- `evaluations` -> `app/work/archive_review/evaluations/folder_status.md`
- `experiments` -> `app/work/archive_review/experiments/folder_status.md`
- `external_case_support` -> `app/work/archive_review/external_case_support/folder_status.md`
- `interview_support`
- `probe_support` -> `app/work/archive_review/probe_support/folder_status.md`
- `prompts` -> `app/work/archive_review/prompts/folder_status.md`
- `transition_support` -> `app/work/archive_review/transition_support/folder_status.md`

## 4. Markdown Files
- none

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `app.work.archive_review`
- inventory_manifest: `runtime/manifests/folder_inventory/app.work.archive_review.json`
- parent_folder: `app/work`
- related_status_files: `app/work/archive_review/folder_status.md`
- last_updated: `2026-04-05T10:11:16+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
