# folder_status / runtime/manifests/folder_inventory

## 1. Folder Identity
- path: `runtime/manifests/folder_inventory`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `98`
- file_types: `.json` x 98

## 3. Child Folders
- none

## 4. Markdown Files
- none

## 5. Code / Data Files
- json: `app.core.json`, `app.core.runtime.__pycache__.json`, `app.core.runtime.json`, `app.json`, `app.work.archive_review.evaluations.json`, `app.work.archive_review.experiments.json`, `app.work.archive_review.external_case_support.json`, `app.work.archive_review.interview_support.json`, `app.work.archive_review.json`, `app.work.archive_review.probe_support.json`, `app.work.archive_review.prompts.json`, `app.work.archive_review.transition_support.json`, `app.work.dialogue_loop_test.generated.json`, `app.work.dialogue_loop_test.json`, `app.work.external_input_preprocess.generated.json`, `app.work.external_input_preprocess.json`, `app.work.input_layer.json`, `app.work.json`, `app.work.middle_layer_experiments.generated.json`, `app.work.middle_layer_experiments.json`

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `runtime.manifests.folder_inventory`
- inventory_manifest: `runtime/manifests/folder_inventory/runtime.manifests.folder_inventory.json`
- parent_folder: `runtime/manifests`
- related_status_files: `runtime/manifests/folder_inventory/folder_status.md`
- last_updated: `2026-04-06T20:09:30+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
