# folder_status / runtime/manifests

## 1. Folder Identity
- path: `runtime/manifests`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `12`
- immediate_child_files: `30`
- file_types: `.json` x 24, `.jsonl` x 3, `.lock` x 3

## 3. Child Folders
- `bridges` -> `runtime/manifests/bridges/folder_status.md`
- `folder_changes` -> `runtime/manifests/folder_changes/folder_status.md`
- `folder_inventory` -> `runtime/manifests/folder_inventory/folder_status.md`
- `label_packets` -> `runtime/manifests/label_packets/folder_status.md`
- `measurement_views` -> `runtime/manifests/measurement_views/folder_status.md`
- `operating_ui_phase1` -> `runtime/manifests/operating_ui_phase1/folder_status.md`
- `origin_maps` -> `runtime/manifests/origin_maps/folder_status.md`
- `provenance_compaction` -> `runtime/manifests/provenance_compaction/folder_status.md`
- `reactive_cells` -> `runtime/manifests/reactive_cells/folder_status.md`
- `reactive_spaces` -> `runtime/manifests/reactive_spaces/folder_status.md`
- `source_views` -> `runtime/manifests/source_views/folder_status.md`
- `user_pages` -> `runtime/manifests/user_pages/folder_status.md`

## 4. Markdown Files
- none

## 5. Code / Data Files
- json: `auto_hint_generation_rules_v0.json`, `document_routing_alias_map_v1.json`, `entry_prebias_examples_v0.json`, `executable_capability_registry_v0.json`, `issue_root_classifier_v0.json`, `latent_line_registry_v1.json`, `line_guided_work_packets.json`, `line_registry.json`, `pipeline_candidate_scope_summary.json`, `projection_registry_v0.json`, `provenance_link_index_v1.json`, `reference_intake_memory_v0.json`, `residue_reentry_rules_v0.json`, `route_registry_v0.json`, `second_candidate_watch_rules.json`, `signal_generation_sources_v0.json`, `signal_kind_taxonomy_v0.json`, `source_to_family_hints_v0.json`, `structured_internal_docs_registry_v1.json`, `ticket_registry_v1.json`
- other: `execution_trace_log_v0.jsonl`, `phase_decision_log.jsonl`, `pipeline_observation_registry.jsonl`, `provenance_link_index_v1.json.lock`, `structured_internal_docs_registry_v1.json.lock`, `ticket_registry_v1.json.lock`

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `runtime.manifests`
- inventory_manifest: `runtime/manifests/folder_inventory/runtime.manifests.json`
- parent_folder: `runtime`
- related_status_files: `runtime/manifests/folder_status.md`
- last_updated: `2026-04-09T18:45:30+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
