# folder_status / source_assets/handoffs

## 1. Folder Identity
- path: `source_assets/handoffs`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `1`
- file_types: `.md` x 1

## 3. Child Folders
- none

## 4. Markdown Files
- `codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md`
  title: CODEX HANDOFF — STRUCTURED DOC ROUTING STABILITY BASELINE LOCK + NEXT STEP DIRECTIVE
  summary: [[DOCROLE:directive]] [[RUNMODE:ingest_only]] [[PRIORITY:high]]

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `source_assets.handoffs`
- inventory_manifest: `runtime/manifests/folder_inventory/source_assets.handoffs.json`
- parent_folder: `source_assets`
- related_status_files: `source_assets/handoffs/folder_status.md`
- last_updated: `2026-03-26T21:43:41+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
