# folder_status / scripts

## 1. Folder Identity
- path: `scripts`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `86`
- file_types: `.py` x 82, `.sh` x 4

## 3. Child Folders
- none

## 4. Markdown Files
- none

## 5. Code / Data Files
- python: `apply_anchor_engine_to_processor_docs.py`, `apply_internal_observer.py`, `backfill_engine_state_v1.py`, `backfill_live_input_bridges.py`, `backfill_possibility_bridges.py`, `build_dust_field_view.py`, `build_measurement_view.py`, `build_reconstruction_supervisor_surface.py`, `build_source_view.py`, `build_space_graph_view.py`, `commonize_runtime_observer_baseline.py`, `create_exploration_observation_stub.py`, `extract_explore_candidates.py`, `extract_segment_source_context.py`, `folder_status_sync.py`, `import_processor_compare_docs.py`, `ingest_fragments.py`, `process_structured_doc_with_routing.py`, `record_observer_samples.py`, `record_observer_template.py`
- other: `run_reconstruction_supervisor_advanced_cycle.sh`, `run_reconstruction_supervisor_batch.sh`, `run_reconstruction_supervisor_cycle.sh`, `run_youtube_03_22_dialogue_loop_test.sh`

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `scripts`
- inventory_manifest: `runtime/manifests/folder_inventory/scripts.json`
- parent_folder: `.`
- related_status_files: `scripts/folder_status.md`
- last_updated: `2026-04-06T20:09:30+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
