# folder_status / docs

## 1. Folder Identity
- path: `docs`
- role_guess: Documentation operating memory containing contracts, policies, reports, guides, prompts, and templates.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `14`
- immediate_child_files: `1`
- file_types: `<no_ext>` x 1

## 3. Child Folders
- `architecture` -> `docs/architecture/folder_status.md`
- `baselines`
- `contracts` -> `docs/contracts/folder_status.md`
- `evaluations` -> `docs/evaluations/folder_status.md`
- `examples` -> `docs/examples/folder_status.md`
- `guides` -> `docs/guides/folder_status.md`
- `notes` -> `docs/notes/folder_status.md`
- `policies` -> `docs/policies/folder_status.md`
- `prompts` -> `docs/prompts/folder_status.md`
- `proposals`
- `reports` -> `docs/reports/folder_status.md`
- `reviews` -> `docs/reviews/folder_status.md`
- `specs` -> `docs/specs/folder_status.md`
- `templates` -> `docs/templates/folder_status.md`

## 4. Markdown Files
- none

## 5. Code / Data Files
- other: `.DS_Store`

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `docs`
- inventory_manifest: `runtime/manifests/folder_inventory/docs.json`
- parent_folder: `.`
- related_status_files: `docs/folder_status.md`
- last_updated: `2026-04-09T18:45:29+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
