# folder_status / docs/contracts

## 1. Folder Identity
- path: `docs/contracts`
- role_guess: Contract layer containing hard boundaries and structural guarantees.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `14`
- file_types: `.md` x 14

## 3. Child Folders
- none

## 4. Markdown Files
- `code_reference_asset_schema_v1.md`
  title: code_reference_asset_schema_v1
  summary: 이 계약은 코드/패치/설계 초안이 공간 안에서 단순 파일이 아니라 reference asset 으로 읽히도록 최소 필드를 고정한다.
- `exploration_observation_layer_v1.md`
  title: exploration_observation_layer_v1
  summary: 탐색 결과를 읽었음 수준으로 흘려보내지 않고, session / run 기준으로 얇게 반복 기록할 수 있는 runtime observer sidecar 층을 고정한다.
- `external_case_relation_reading_contract_v1.md`
  title: external_case_relation_reading_contract_v1
  summary: 외부 기술 사례가 공간에 들어왔을 때 단순 참고자료가 아니라 비교축 / 구조 차용 재료 / 분리 유지 판단 재료로 읽히도록 최소 판독 필드를 고정한다.
- `folder_status_render_contract_v1.md`
  title: folder_status_render_contract_v1
  summary: `folder_status.md`를 원장이 아니라 읽기면으로 고정한다.
- `input_layer_wrapper_core_link_note_v1.md`
  title: input_layer_wrapper_core_link_note_v1
  summary: 이 문서는 structured doc intake 에서 wrapper 와 core input-layer labeler 의 책임 경계를 잠그는 최소 연결 노트다.
- `label_family_separation_contract_v1.md`
  title: label_family_separation_contract_v1
  summary: 이 문서는 `vectorfl_replica` 전반에 이미 분산되어 존재하는 labeling 을 family 단위로 다시 구획하고, `core input-layer labeler` 가 어디까지를 맡는지 잠그기 위한 최소 계약 문서다.
- `observation_probe_contract_v1.md`
  title: observation_probe_contract_v1
  summary: 이 계약은 관측기/응결핵/탐색기를 공간 본체가 아닌 detachable read-only 부품으로 고정한다.
- `operation_surface_data_requirements_v1.md`
  title: operation_surface_data_requirements_v1
  summary: - `source_doc_ref` - `doc_id` - `run_id` - `ticket_id` - `started_at` - `status` - `expected_scenario` - `generated_files` - `receipt_ref` - `observation_refs` - `reference_refs` - `next_actions`
- `operation_surface_min_spec_v1.md`
  title: operation_surface_min_spec_v1
  summary: 이 문서는 전체 공간 뷰어 대신 먼저 필요한 read-only operation surface 의 최소 스펙을 잠근다.
- `operation_surface_pointer_spec_v1.md`
  title: operation_surface_pointer_spec_v1
  summary: This contract defines how latest operation surfaces should behave as pointer surfaces instead of content-heavy summary copies.
- `origin_map_minimum_fields_v1.md`
  title: origin_map_minimum_fields_v1
  summary: This contract fixes the minimum origin map fields used to return from a derived artifact back to its source document location.
- `provenance_compacted_surface_spec_v1.md`
  title: provenance_compacted_surface_spec_v1
  summary: `provenance_compacted_latest.md` is a readability surface summarizing duplicate-noise patterns without replacing the raw provenance index.
- `refinement_checkpoint_contract_v1.md`
  title: refinement_checkpoint_contract_v1
  summary: 엔진이 풍부해지더라도 코어가 비대해지지 않도록 주기적 정련 패스에서 무엇을 점검해야 하는지 고정한다.
- `stage1_exploration_result_minimum_fields_contract_v1.md`
  title: stage1_exploration_result_minimum_fields_contract_v1
  summary: 새 입력 1건을 응결핵처럼 넣었을 때 현재 엔진이 탐색 결과로 최소 무엇을 반환해야 하는지 고정한다.

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `docs.contracts`
- inventory_manifest: `runtime/manifests/folder_inventory/docs.contracts.json`
- parent_folder: `docs`
- related_status_files: `docs/contracts/folder_status.md`
- last_updated: `2026-03-26T20:09:05+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
