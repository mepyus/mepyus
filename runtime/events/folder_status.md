# folder_status / runtime/events

## 1. Folder Identity
- path: `runtime/events`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `1`
- immediate_child_files: `4`
- file_types: `.jsonl` x 2, `.lock` x 1, `.md` x 1

## 3. Child Folders
- `folder_activity`

## 4. Markdown Files
- `event_schema_v1.md`
  title: event_schema_v1
  summary: 이 문서는 `vectorfl_replica` 의 append-only 운영 기록을 위한 최소 이벤트 스키마를 고정한다.

## 5. Code / Data Files
- other: `engine_event_ledger.jsonl`, `engine_event_ledger.jsonl.lock`, `formation_events.jsonl`

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `runtime.events`
- inventory_manifest: `runtime/manifests/folder_inventory/runtime.events.json`
- parent_folder: `runtime`
- related_status_files: `runtime/events/folder_status.md`
- last_updated: `2026-04-05T16:50:15+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
