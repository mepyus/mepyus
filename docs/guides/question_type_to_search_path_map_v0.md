# Question Type To Search Path Map v0

## Purpose

사용자 질문 유형을 탐색 가능한 시작 경로로 번역한다.

## Execution

| question type | start paths | second paths | avoid-first |
| --- | --- | --- | --- |
| current state / what is locked | `CURRENT.md`, `vectorfl_status.md` | `source_assets/baselines/folder_status.md`, `docs/policies/*` | generated views |
| authority / baseline conflict | `source_assets/baselines/*`, `docs/policies/*` | `docs/baselines/*`, `docs/specs/*` | reports before baseline |
| where is an asset | `docs/guides/vectorfl_space_asset_access_map_v0.md`, `docs/indexes/space_asset_map_v0.md` | `folder_status.md`, `rg --files` | blind full-tree reading |
| how should Codex operate | `source_assets/baselines/codex_baseline_vectorfl_replica_intake_and_operation_v1.md`, `docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md` | `source_assets/handoffs/*`, `docs/guides/*` | UI docs |
| question interpretation / routing | `docs/specs/question_interpretation_contract_v0.md` | `runtime/contracts/question_interpretation_packet_v0.json`, `docs/guides/question_mode_examples_for_codex_v0.md` | direct search before packet |
| evidence / exploration | `docs/specs/space_exploration_contract_v0.md` | `docs/guides/evidence_selection_rules_v0.md`, `runtime/contracts/space_exploration_result_v0.json` | answer-only output |
| merge/diff/hold | `docs/specs/source_authority_ladder_v0.md`, `docs/specs/evidence_merge_diff_hold_contract_v0.md` | `docs/guides/alignment_resolution_rules_v0.md` | flattening tension |
| reingress / return | `docs/specs/space_return_package_v0.md`, `docs/specs/space_reingress_package_v0.md` | `runtime/contracts/space_reingress_record_v0.json` | final answer only |
| execution/script question | `docs/notes/executable_runner_index_v0.md`, `scripts/folder_status.md` | target script source | docs-only answer |
| raw input / source document | `inputs/README.md`, `source_assets/README.md` | `docs/guides/input_dropzones.md` | runtime output first |

## Interpretation

질문은 하나의 답 매칭이 아니라 작업 구조다. 같은 "어디 있어?" 질문도 현재성, 권위, 실행 흔적, source provenance 중 어느 층을 묻는지에 따라 탐색 경로가 달라진다. 이 map은 retrieval을 줄이기보다 retrieval 전에 translation을 안정화한다.

## Validation

- 질문 유형별 시작점이 실제 폴더 구조와 맞다.
- baseline 질문이 report에서 시작하지 않게 했다.
- UI는 Phase 1에서 후순위로 둔다.
- packet/contract 관련 질문은 새 Phase 1 문서로 연결된다.

## Stage 1 Closeout

- Verdict: `PASS`
- Files created: `docs/guides/question_type_to_search_path_map_v0.md`
- Key decisions: 질문 유형은 탐색 시작 경로를 결정한다.
- Risks: 복합 질문은 여러 row를 동시에 따라야 한다.
- Entry condition for next stage: interpretation packet이 `task_mode`와 `search_targets`를 담는다.
