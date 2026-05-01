# folder_status / runtime/manifests

## 1. Folder Identity
- path: `runtime/manifests`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `12`
- immediate_child_files: `116`
- file_types: `.json` x 106, `.jsonl` x 4, `.lock` x 3, `.md` x 3

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
- `vectorfl_paper_external_resource_cell_draft_v0.md`
  title: External Resource Draft
  summary: - source_contract: `docs/contracts/vectorfl_paper_external_resource_cell_v0.md` - purpose: 외부 비교 지시와 주입 기준을 바꾸기 전에 임시 draft로 검토하는 slot
- `vectorfl_paper_internal_read_cell_draft_v0.md`
  title: Internal Read Draft
  summary: - source_contract: `docs/contracts/vectorfl_paper_internal_read_cell_v0.md` - purpose: internal_read 셀 수정 실험을 본 계약과 분리해서 먼저 적어보는 draft slot
- `vectorfl_paper_synthesis_cell_draft_v0.md`
  title: Synthesis Draft
  summary: - source_contract: `docs/contracts/vectorfl_paper_synthesis_cell_v0.md` - purpose: 감독 보고 형식과 종합 규칙을 수정할 때 먼저 써 보는 slot

## 5. Code / Data Files
- json: `active_anchor_integrated_engine_3_surface.json`, `auto_hint_generation_rules_v0.json`, `current_loop_state_axis_drift_recheck_001.json`, `current_loop_state_axis_enrichment_001.json`, `document_routing_alias_map_v1.json`, `entry_prebias_examples_v0.json`, `executable_capability_registry_v0.json`, `issue_root_classifier_v0.json`, `latent_line_registry_v1.json`, `line_guided_work_packets.json`, `line_registry.json`, `maturation_object_axis_candidate_001.json`, `packet_reflux_axis_pattern_001.json`, `packet_request_axis_enrichment_001.json`, `packet_request_axis_followup_001.json`, `packet_request_axis_reprocess_001.json`, `packet_return_axis_enrichment_001.json`, `packet_return_axis_followup_001.json`, `panel_connection_record_axis_enrichment_001.json`, `panel_connection_record_engine_return_to_vectorfl_validation_001.json`
- other: `execution_trace_log_v0.jsonl`, `phase_decision_log.jsonl`, `pipeline_observation_registry.jsonl`, `provenance_link_index_v1.json.lock`, `structured_internal_docs_registry_v1.json.lock`, `ticket_registry_v1.json.lock`, `vectorfl_paper_weekend_live_execution_trace_log_v0.jsonl`

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `runtime.manifests`
- inventory_manifest: `runtime/manifests/folder_inventory/runtime.manifests.json`
- parent_folder: `runtime`
- related_status_files: `runtime/manifests/folder_status.md`
- last_updated: `2026-04-23T21:43:09+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
