# folder_status / docs/reports/latent_line

## 1. Folder Identity
- path: `docs/reports/latent_line`
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
  title: Latent Line Family
  summary: 이 폴더는 아직 문서를 이동하지 않고, `latent_line_*` belt의 의미를 먼저 묶어 읽기 위한 index 면이다.

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `docs.reports.latent_line`
- inventory_manifest: `runtime/manifests/folder_inventory/docs.reports.latent_line.json`
- parent_folder: `docs/reports`
- related_status_files: `docs/reports/latent_line/folder_status.md`
- last_updated: `2026-04-05T09:59:06+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
