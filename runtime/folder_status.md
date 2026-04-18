# folder_status / runtime

## 1. Folder Identity
- path: `runtime`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `26`
- immediate_child_files: `4`
- file_types: `.json` x 2, `.jsonl` x 1, `<no_ext>` x 1

## 3. Child Folders
- `assistant_profile` -> `runtime/assistant_profile/folder_status.md`
- `commands` -> `runtime/commands/folder_status.md`
- `config` -> `runtime/config/folder_status.md`
- `contracts` -> `runtime/contracts/folder_status.md`
- `core` -> `runtime/core/folder_status.md`
- `decision_lineage` -> `runtime/decision_lineage/folder_status.md`
- `events` -> `runtime/events/folder_status.md`
- `fragments` -> `runtime/fragments/folder_status.md`
- `interpretation_packets` -> `runtime/interpretation_packets/folder_status.md`
- `line_thickening_demo` -> `runtime/line_thickening_demo/folder_status.md`
- `line_thickening_demo_v2` -> `runtime/line_thickening_demo_v2/folder_status.md`
- `logs` -> `runtime/logs/folder_status.md`
- `manifests` -> `runtime/manifests/folder_status.md`
- `measurements` -> `runtime/measurements/folder_status.md`
- `memory` -> `runtime/memory/folder_status.md`
- `multi_lens_views` -> `runtime/multi_lens_views/folder_status.md`
- `observer` -> `runtime/observer/folder_status.md`
- `receipts` -> `runtime/receipts/folder_status.md`
- `reports` -> `runtime/reports/folder_status.md`
- `review_ledgers` -> `runtime/review_ledgers/folder_status.md`
- `sandboxes` -> `runtime/sandboxes/folder_status.md`
- `source_documents` -> `runtime/source_documents/folder_status.md`
- `state` -> `runtime/state/folder_status.md`
- `tmp` -> `runtime/tmp/folder_status.md`
- `validation` -> `runtime/validation/folder_status.md`
- `views` -> `runtime/views/folder_status.md`

## 4. Markdown Files
- none

## 5. Code / Data Files
- json: `current_phase.json`, `preflight_last_decision.json`
- other: `.DS_Store`, `breadcrumbs.jsonl`

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `runtime`
- inventory_manifest: `runtime/manifests/folder_inventory/runtime.json`
- parent_folder: `.`
- related_status_files: `runtime/folder_status.md`
- last_updated: `2026-04-09T18:45:29+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
