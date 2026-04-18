# Generated Retention Map v1

## 목적

이 문서는 generated / manifest / log 자산을

- `ledger`
- `active surface`
- `replayable residue`

세 층으로 나눠 정리 기준을 잠근다.

핵심 원칙:

- `ledger` 는 과거 사실을 보존하므로 경로가 오래돼도 임의 수정하지 않는다.
- `active surface` 는 현재 읽기면이므로 현재 공간 구조를 반영해야 한다.
- `replayable residue` 는 재생성 가능하므로 family 단위 보관 또는 축약 대상으로 본다.

## 1. runtime/manifests

### keep as ledger

- [folder_changes](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/folder_changes)
- [folder_inventory](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/folder_inventory)
- [origin_maps](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/origin_maps)
- top-level registry files:
  - `line_registry.json`
  - `latent_line_registry_v1.json`
  - `structured_internal_docs_registry_v1.json`
  - `ticket_registry_v1.json`
  - `reference_intake_memory_v0.json`

판단:

- 이 층은 append-only 원장 또는 그 렌더 기반이다.
- 과거 경로/이벤트가 남아 있어도 현재 구조에 맞춘 rewrite를 하지 않는다.

### keep as active surface

- [label_packets](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/label_packets)
- [measurement_views](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/measurement_views)
- [source_views](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/source_views)
- [operating_ui_phase1](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/operating_ui_phase1)
- [user_pages](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/user_pages)
- [reactive_cells](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/reactive_cells)
- [reactive_spaces](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/reactive_spaces)
- [bridges](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/bridges)

판단:

- 현재 viewer / surface / local-space readout 이 직접 기대는 현재면이다.
- 경로 드리프트가 생기면 현재 구조에 맞게 refresh 한다.

### keep as replayable residue

- [provenance_compaction](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/provenance_compaction)

판단:

- useful 하지만 원장 핵심층은 아니다.
- preview/apply 결과를 대표본 기준으로 줄일 수 있다.

## 2. runtime/logs

### keep as ledger

- [repo_delta_log.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/logs/repo_delta_log.jsonl)
- [line_promotion_log.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/logs/line_promotion_log.jsonl)
- [reread_observation_log.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/logs/reread_observation_log.jsonl)

판단:

- 과거 이벤트 기록이다.
- 오래된 경로 문자열도 기록 사실의 일부로 본다.

### keep as active surface

- [folder_status.md](/Users/sungsookim/universe/vectorfl_replica/runtime/logs/folder_status.md)

### keep as replayable residue

- `*.lock`
- [work_sessions](/Users/sungsookim/universe/vectorfl_replica/runtime/logs/work_sessions)

판단:

- lock 파일은 추적 불필요 쪽이 맞다.
- session note는 ledger보다는 보조 기록이다.

## 3. observer_ingest_min/generated

### keep as active surface

- `operator_summary_*`
- `readable_input_board_*`
- `source_manifest_*`
- `processing_trace_*`

판단:

- 현재 operator가 입력을 다시 읽는 면이다.
- 실제 구조가 바뀌면 예전 경로 표기도 current path로 refresh 할 수 있다.

### keep as replayable residue

- `split_units_*`

판단:

- useful 하지만 재분해 가능하다.
- 지금은 읽기 디버깅에 필요해 남기되, 장기적으로는 대표본만 남기는 축약 후보다.

## 4. dialogue_loop_test/generated

### keep as active surface

- `context_unit_candidates_*`
- `dialogue_asset_purpose_synthesis_*`
- `question_inducing_block_candidates_*`
- `multi_pass_interpretation_training_*`
- `paragraph_role_interpretation_*`
- `*_engine_purpose_validation_*`
- `*_multi_pass_validation_*`
- `*_paragraph_role_validation_*`

판단:

- 여러 report가 직접 물고 있는 살아있는 validation surface다.
- 지금은 archive residue로 내리지 않는다.

### keep as replayable residue

- 반복 `*_dialogue_loop_test_*`
- 반복 `*_baseline_probe_*`
- 반복 `*_segmentation_probe_*`

판단:

- 현재는 line 형성에 기여하므로 유지하지만, family별 대표본이 잠기면 window/step 반복본 일부는 축약 가능하다.

## 5. immediate cleanup rule

지금 당장 적용할 규칙:

1. `ledger` 는 rewrite보다 보존 우선
2. `active surface` 는 현재 경로/현재 reading contract 우선
3. `replayable residue` 는 family index를 먼저 세우고, 그 다음 대표본만 남기는 축약 검토

## 5A. runtime/sandboxes

### keep as replayable residue

- [runtime/sandboxes](/Users/sungsookim/universe/vectorfl_replica/runtime/sandboxes)

판단:

- sandbox recovery / reintroduction 스크립트는 repo 내부가 아니라 tempdir 아래에 sandbox를 생성한다.
- repo 안의 `runtime/sandboxes/*` 는 canonical runtime이 아니라 실행 중 흘러든 복제본으로 읽는 편이 맞다.
- sandbox 안의 report markdown이 이미 [runtime/reports](/Users/sungsookim/universe/vectorfl_replica/runtime/reports) 같은 canonical surface에 존재하면, sandbox copy는 보존 가치가 낮다.
- 따라서 nested 자기복제 하위는 즉시 제거 대상이고, top-level sandbox도 별도 참조가 없으면 제거 가능하다.

## 5B. baseline runtime profile

### keep as active surface

- [runtime/current_phase.json](/Users/sungsookim/universe/vectorfl_replica/runtime/current_phase.json)
- [runtime/preflight_last_decision.json](/Users/sungsookim/universe/vectorfl_replica/runtime/preflight_last_decision.json)
- [runtime/breadcrumbs.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/breadcrumbs.jsonl)

판단:

- 이 셋은 일회성 residue가 아니라 현재 읽기 frame과 다음 hop을 고정하는 control-plane profile이다.
- `current_phase` 와 `preflight_last_decision` 은 summary surface지만 매 실행마다 다시 필요한 현재면이다.
- `breadcrumbs.jsonl` 은 단순 debug 출력이 아니라 판단 이동을 누적하는 운영 기록이다.
- 따라서 broad cleanup 때 날리지 않고 baseline runtime profile로 유지한다.

## 6. next condensation candidates

- `dialogue_loop_test/generated`
  - family별 exemplar 1개 + latest 1개 + index 유지 검토
- `observer_ingest_min/generated/split_units_*`
  - current asset map이나 대표 report에 대응하는 exemplar 유지 검토
- `runtime/logs/*.lock`
  - 비추적 residue로 완전 분리 검토

세부 후보 표는
[dialogue_loop_generated_condensation_candidates_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/dialogue_loop_generated_condensation_candidates_v1.md)
를 따른다.

정리 종료선은
[cleanup_freeze_boundary_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/cleanup_freeze_boundary_v1.md)
를 따른다.
