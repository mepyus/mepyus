# folder_status / docs/policies

## 1. Folder Identity
- path: `docs/policies`
- role_guess: Policy layer containing operating rules and governance notes.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `16`
- file_types: `.md` x 16

## 3. Child Folders
- none

## 4. Markdown Files
- `AMBIGUITY_REVIEW_POLICY.md`
  title: Ambiguity Review Policy
  summary: When a value or judgment is visibly ambiguous, the workflow should not jump directly to silent internal resolution.
- `ANCHOR_V1.md`
  title: Anchor V1
  summary: Anchor is not a simple tag.
- `code_reference_ingest_policy_v1.md`
  title: code_reference_ingest_policy_v1
  summary: 이 정책은 코드/설계 초안/패치 결과를 reference_memory 로 재투입할 때의 최소 intake 기준을 정한다.
- `codex_baseline_program_grade_workspace_upgrade_v1.md`
  title: codex_baseline_program_grade_workspace_upgrade_v1
  summary: 이 문서는 현재 엔진 작업공간을 “몇 개의 스크립트와 파이프라인이 돌아가는 상태”에서 **입력·기록·판독·실행·조회가 역할별로 정돈된 프로그램급 작업공간**으로 승격시키기 위한 기준문이다.
- `CODEX_LEARNING_ITEMS_V0_1.md`
  title: Codex 추가 학습 항목 v0.1
  summary: [[A]] [[OBJ:codex_learning_items]] [[ROLE:engine]]
- `codex_material_and_operation_docs_index_v1.md`
  title: codex_material_and_operation_docs_index_v1
  summary: 이 문서는 `vectorfl_replica` 의 문서형 운영 재료 중 현재 최상위 3종 세트를 한 번에 가리키는 index 이다.
- `company_space_boundary_policy_v1.md`
  title: company_space_boundary_policy_v1
  summary: 이 정책은 새 회사 시나리오에서 회사 raw, 개인 장기 공간, 외부 LLM 전송 가능 범위를 섞지 않기 위한 최소 경계 슬롯을 정의한다.
- `core_promotion_checklist_v1.md`
  title: core_promotion_checklist_v1
  summary: 외부 사례 / 예시문 / 관측 결과 / 탐색 판독이 쌓일 때 무엇을 코어 후보로 읽고, 무엇을 외곽 후보로 남기며, 무엇을 보류해야 하는지 반복 가능한 체크리스트로 고정한다.
- `document_routing_markers_policy_v1.md`
  title: document_routing_markers_policy_v1
  summary: This policy fixes the lightweight routing markers used at the top of structured documents in `vectorfl_replica`.
- `engine_input_lane_baseline_v1.md`
  title: engine_input_lane_baseline_v1
  summary: 이 문서는 엔진으로 들어오는 입력의 종류가 늘어나더라도 입력 혼잡과 중심 오염을 막기 위해 사용하는 **단일 intake 기준문(SSOT)** 이다.
- `input_calibration_reference_policy_v1.md`
  title: input_calibration_reference_policy_v1
  summary: 이 정책은 raw input 자유를 막지 않으면서 입력기 흔들림 점검용 calibration reference set 을 별도로 유지하는 기준을 고정한다.
- `MEASUREMENT_RETENTION_POLICY.md`
  title: Measurement Retention Policy
  summary: The replica must preserve ambiguous measurements, tentative judgments, and intermediate outputs instead of discarding them.
- `OBSERVER_LAYER_GUIDE.md`
  title: Observer Layer Guide
  summary: 이 문서는 `vectorfl_replica`에서 observer layer를 어떻게 써야 하는지 정리한 짧은 운영 가이드다.
- `provenance_dedupe_compaction_policy_v1.md`
  title: provenance_dedupe_compaction_policy_v1
  summary: This policy defines how provenance duplicate noise should be reviewed and compacted without destroying raw trace evidence.
- `refinement_trigger_rules_v1.md`
  title: refinement_trigger_rules_v1
  summary: 정련(refinement)을 언젠가 필요하면이 아니라 개시 조건이 명시된 운영 트리거로 고정한다.
- `REPLICA_METHOD_SPEC_V0_1.md`
  title: VECTORFL Replica — 운영 방법 규약 v0.1
  summary: [[A]] [[OBJ:replica_method_spec]] [[ROLE:engine]]

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `docs.policies`
- inventory_manifest: `runtime/manifests/folder_inventory/docs.policies.json`
- parent_folder: `docs`
- related_status_files: `docs/policies/folder_status.md`
- last_updated: `2026-04-05T09:56:49+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
