# folder_status / app/core/runtime

## 1. Folder Identity
- path: `app/core/runtime`
- role_guess: Runtime artifact or runtime-facing support folder.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `56`
- file_types: `.py` x 56

## 3. Child Folders
- none

## 4. Markdown Files
- none

## 5. Code / Data Files
- python: `__init__.py`, `approval_policies.py`, `approval_policy_types.py`, `auto_hint_generation.py`, `bootstrap.py`, `classifier_adapter.py`, `connection_engine.py`, `context_linked_segmentation.py`, `dust_field.py`, `execution_trace.py`, `external_input_comparison.py`, `external_input_gate.py`, `external_transcript_preprocess.py`, `file_store.py`, `flow_candidate_detection.py`, `graph_view.py`, `imported_material_contract.py`, `imported_material_probe.py`, `inputter.py`, `labeler.py`

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `app.core.runtime`
- inventory_manifest: `runtime/manifests/folder_inventory/app.core.runtime.json`
- parent_folder: `app/core`
- related_status_files: `app/core/runtime/folder_status.md`
- last_updated: `2026-04-06T20:09:30+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
