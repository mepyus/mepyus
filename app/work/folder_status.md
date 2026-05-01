# folder_status / app/work

## 1. Folder Identity
- path: `app/work`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `13`
- immediate_child_files: `1`
- file_types: `.md` x 1

## 3. Child Folders
- `archive_review` -> `app/work/archive_review/folder_status.md`
- `current_layer_baseline` -> `app/work/current_layer_baseline/folder_status.md`
- `dialogue_loop_test` -> `app/work/dialogue_loop_test/folder_status.md`
- `external_input_preprocess` -> `app/work/external_input_preprocess/folder_status.md`
- `input_layer` -> `app/work/input_layer/folder_status.md`
- `mixed_corridor_boundary_probe_stage3` -> `app/work/mixed_corridor_boundary_probe_stage3/folder_status.md`
- `mixed_corridor_format_disentangle_stage4` -> `app/work/mixed_corridor_format_disentangle_stage4/folder_status.md`
- `mixed_reentry_observer_stage2` -> `app/work/mixed_reentry_observer_stage2/folder_status.md`
- `mixed_reentry_probe_stage1` -> `app/work/mixed_reentry_probe_stage1/folder_status.md`
- `observer_ingest_min` -> `app/work/observer_ingest_min/folder_status.md`
- `operating_ui` -> `app/work/operating_ui/folder_status.md`
- `processor_compare` -> `app/work/processor_compare/folder_status.md`
- `technical_business_corridor_decompose_stage5` -> `app/work/technical_business_corridor_decompose_stage5/folder_status.md`

## 4. Markdown Files
- `work_maturity_map_v0.md`
  title: work maturity map v0
  summary: 이 문서는 `app/work/`를 한 덩어리 실험장으로 읽지 않도록 상위 maturity map을 제공하는 entrypoint다.

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `app.work`
- inventory_manifest: `runtime/manifests/folder_inventory/app.work.json`
- parent_folder: `app`
- related_status_files: `app/work/folder_status.md`
- last_updated: `2026-04-23T21:43:09+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
