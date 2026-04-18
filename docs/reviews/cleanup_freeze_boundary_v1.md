# Cleanup Freeze Boundary v1

## 목적

이 문서는 현재 공간 정리를 어디서 멈출지 잠근다.

정리 원칙은 이미 세워졌고, 일부 실제 감량도 끝났다.
이제부터는 `계속 줄일 수 있음` 과 `지금 줄이면 line이 약해짐` 을 구분해야 한다.

## 1. current freeze decision

현재 시점에서 공간 정리는 아래 상태로 `freeze-ready` 다.

- `app/work` root 는 이유 없이 남은 support cluster가 거의 없다.
- archive로 내려갈 것들은 family belt 기준으로 대부분 정리됐다.
- `dialogue_loop_test/generated` 는 첫 실감량 배치를 통과했다.
- generated / manifests / logs 는 `ledger / active surface / replayable residue` 기준이 고정됐다.
- `runtime/sandboxes` 의 nested 자기복제 하위는 걷어냈고, top-level sandbox만 남겨뒀다.
- sandbox 생성 스크립트가 tempdir를 쓰고, repo 내부 sandbox 보고서가 canonical report와 중복되면 top-level sandbox도 residue로 제거할 수 있다.
- `runtime/current_phase.json`, `runtime/preflight_last_decision.json`, `runtime/breadcrumbs.jsonl` 은 기본 runtime profile로 유지한다.

따라서 다음부터는 `broad cleanup` 을 계속하지 않고,
필요한 경우에만 `targeted condensation` 으로 들어간다.

## 2. freeze-ready zones

### A. app/work root

현 상태에서 root에 남는 것이 맞는 것:

- `current_layer_baseline`
- staged corridor:
  - `mixed_reentry_probe_stage1`
  - `mixed_reentry_observer_stage2`
  - `mixed_corridor_boundary_probe_stage3`
  - `mixed_corridor_format_disentangle_stage4`
  - `technical_business_corridor_decompose_stage5`
- emergent / active line:
  - `external_input_preprocess`
  - `observer_ingest_min`
  - `dialogue_loop_test`
  - `operating_ui`
- root-retained support:
  - `processor_compare`
- transition root:
  - `input_layer`

판단:

- 이 목록은 현재 의미가 분명하다.
- 더 줄이려면 line 손상 위험이 먼저 커진다.
- `external_input_preprocess` 는 README / folder_status 를 갖춘 active belt로 복구됐다.

### B. archive_review families

아래 family는 현재 구조면에서 안정적이다.

- `transition_support`
- `probe_support`
- `external_case_support`
- `interview_support`
- `experiments`
- `evaluations`
- `prompts`

판단:

- 이제 broad move는 종료하고, 각 family 내부 축약만 별도 배치로 다룬다.

### C. docs/reports family belts

현재 고정:

- `history`
- `latent_line` index surface
- `multi_lens`
- `space_structure`

판단:

- 더 큰 재배치는 링크 비용이 크다.
- 새 family move보다 family index/readme 보강이 우선이다.

## 3. condensation freeze line

### dialogue_loop_test/generated

현재는 아래까지만 감량하고 멈춘다.

- `youtube_03_22_dialogue_loop_test_*`
  - reduced
- `claude_code_index_dialogue_loop_test_*`
  - reduced
- `claude_code_index_segmentation_probe_v1_*`
  - reduced

당분간 더 줄이지 않는 것:

- `context_unit_candidates_*`
- `dialogue_asset_purpose_synthesis_*`
- `question_inducing_block_candidates_*`
- `multi_pass_interpretation_training_*`
- `paragraph_role_interpretation_*`
- 각 `*_engine_purpose_validation_*`
- 각 `*_multi_pass_validation_*`
- 각 `*_paragraph_role_validation_*`
- already-two-file families:
  - `*_baseline_probe_*`
  - `enterprise_segmentation_probe_v1_*`
  - `graphrag_neosh_segmentation_probe_v1_*`

판단:

- 더 줄여도 용량 이득은 작고 reread 손상 위험이 커진다.

### observer_ingest_min/generated

현재는 경로 refresh까지만 하고 멈춘다.

- `operator_summary_*`
- `readable_input_board_*`
- `source_manifest_*`
- `processing_trace_*`
- `split_units_*`

판단:

- 이 폴더는 먼저 `대표본 정책` 이 더 필요하다.
- broad deletion은 아직 금지다.

## 4. do-not-touch without new trigger

아래는 새로운 명시적 trigger 없이는 다시 broad cleanup 하지 않는다.

- `runtime/manifests/folder_changes`
- `runtime/manifests/folder_inventory`
- `runtime/manifests/origin_maps`
- `runtime/logs/*.jsonl`
- `runtime/logs/work_sessions`
- `processor_compare`
- `dialogue_loop_test/generated` keep-all families

## 5. valid restart triggers

정리를 다시 크게 여는 조건은 아래뿐이다.

1. root에 새 support cluster가 다시 누적됨
2. report/link 구조가 archive family와 다시 어긋남
3. generated family가 2배 이상 다시 불어남
4. runtime sidecar가 더 이상 `processor_compare` 를 직접 import하지 않게 됨
5. 사용자가 새로운 condensation batch를 명시적으로 요청함

## 6. one-line lock

현재 정리는 `broad move phase` 를 끝내고 `targeted condensation only` 상태로 전환한다.
