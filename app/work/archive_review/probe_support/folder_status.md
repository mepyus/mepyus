# folder_status / app/work/archive_review/probe_support

## 1. Folder Identity
- path: `app/work/archive_review/probe_support`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `2`
- immediate_child_files: `1`
- file_types: `.md` x 1

## 3. Child Folders
- `concept_segment_probe`
- `future_segment_probe`

## 4. Markdown Files
- `README.md`
  title: Probe Support Family
  summary: 이 폴더는 bounded probe 산출을 남기는 support cluster를 묶는다.

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `app.work.archive_review.probe_support`
- inventory_manifest: `runtime/manifests/folder_inventory/app.work.archive_review.probe_support.json`
- parent_folder: `app/work/archive_review`
- related_status_files: `app/work/archive_review/probe_support/folder_status.md`
- last_updated: `2026-04-05T10:06:46+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
