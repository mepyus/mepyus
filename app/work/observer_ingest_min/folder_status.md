# folder_status / app/work/observer_ingest_min

## 1. Folder Identity
- path: `app/work/observer_ingest_min`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `3`
- immediate_child_files: `3`
- file_types: `.md` x 2, `.py` x 1

## 3. Child Folders
- `contracts`
- `examples`
- `generated` -> `app/work/observer_ingest_min/generated/folder_status.md`

## 4. Markdown Files
- `observer_ingest_min_spec.md`
  title: observer_ingest_min spec
  summary: - 입력을 쉽게 넣고 - 어떻게 나뉘었는지 바로 보고 - 처리 흔적을 최소 trace로 남기고 - 사람이 md 한 장으로 빠르게 확인할 수 있게 한다.
- `observer_ingest_min_terminal_usage.md`
  title: observer_ingest_min terminal usage
  summary: 이 문서는 `observer_ingest_min` 실행기를 터미널에서 바로 사용하는 방법만 정리한다.

## 5. Code / Data Files
- python: `run_observer_ingest_min.py`

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `app.work.observer_ingest_min`
- inventory_manifest: `runtime/manifests/folder_inventory/app.work.observer_ingest_min.json`
- parent_folder: `app/work`
- related_status_files: `app/work/observer_ingest_min/folder_status.md`
- last_updated: `2026-04-23T21:43:10+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
