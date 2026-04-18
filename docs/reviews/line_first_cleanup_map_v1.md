# line_first_cleanup_map_v1

## purpose

이 문서는 공간 정리를 `삭제` 기준이 아니라 `line` 기준으로 다시 시작하기 위한 기준면이다.

이번 정리의 핵심은 아래다.

1. 이미 살아 있는 line은 더 분명하게 잠근다.
2. 아직 이름이 없지만 반복 흔적이 있는 공간은 한 번 더 읽어 `emergent line`으로 살린다.
3. 기존 자료 중 겉보기에 낡아 보이는 것들도 line source / line residue / dead weight로 나눠 본 뒤에만 정리한다.

즉 이번 정리는 `치우기`가 아니라 `line-preserving reconstruction`이다.

## current reading

이번 재점검에서 반복적으로 확인된 사실은 아래다.

- repo 비대화의 중심은 `app/` 코드보다 `runtime/` 산출물과 `references/` 저장소다.
- `app/work/` 는 단일 실험장이 아니라 `baseline-memory`, `staged corridor`, `utility-sidecar`가 섞인 pre-promotion workspace다.
- `docs/reports/` 는 단순 보고서 모음이 아니라 line 형성사와 운영 판단이 누적된 memory belt다.
- 정리 리스크가 큰 것은 재생산 가능한 generated보다, 겉보기엔 오래되었지만 아직 line으로 흡수되지 않은 기존 자료다.

## what line means here

이 공간에서 `line`은 단순 주제 묶음이 아니다.

line은 아래를 함께 만족하는 반복 방향이다.

- 선언문, baseline, status, report, code, runtime evidence 사이에 같은 판단축이 반복된다.
- 한 번의 산출물이 아니라 여러 재료를 다시 읽게 만드는 운영 방향이다.
- 폴더 구조보다 먼저 `무엇을 보존하고 무엇을 늦추고 무엇을 승격하는가`를 결정한다.

line은 파일보다 깊고, 폴더보다 오래가야 한다.

## line taxonomy

### 1. locked line

이미 현재 공간의 중심 동작으로 인정된 line.

판정 기준:

- `CURRENT.md`
- `vectorfl_status.md`
- work baseline
- runtime evidence

에서 같은 방향이 반복된다.

### 2. emergent line

아직 코어로 잠기진 않았지만 여러 자료군에서 반복되어 line 승격 가능성이 보이는 것.

판정 기준:

- 2개 이상 폴더/문서군에서 반복 등장
- 단발 실험으로 끝나지 않음
- 이후 코어/운영면으로 옮길 가치가 있음

### 3. line source

line을 세우거나 강화하는 원본 자료.

예:

- baseline
- declaration
- staged probe
- representative report
- 핵심 runner

### 4. line residue

line 형성에는 기여했지만 직접 코어로 남기기엔 과한 자료.
삭제 대상이 아니라 `축약 보관` 또는 `archive candidate`다.

예:

- 반복 실험 보고서 묶음
- stage generated exemplar
- 중복된 validation 보고서

### 5. dead weight

line에도 연결되지 않고, 기존 line 형성사에도 기여하지 않으며, 재생산 가능하거나 의미가 소실된 자료.

예:

- cache
- `.DS_Store`
- 재귀 sandbox
- import가 끊긴 잔여 경로를 더 악화시키는 임시 부산물

## locked lines

### A. baseline-memory line

의미:

- 공간의 철학과 현재 계약을 잠그는 중심선

핵심 경로:

- [CURRENT.md](/Users/sungsookim/universe/vectorfl_replica/CURRENT.md)
- [vectorfl_status.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_status.md)
- [engine_philosophy_declaration_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/engine_philosophy_declaration_v1.md)
- [current_layer_baseline_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/current_layer_baseline_contract_v1.md)

정리 원칙:

- 이 line은 축약하지 않는다.
- 다른 폴더를 정리할 때도 항상 이 line 기준으로만 판단한다.

### B. fragment retention line

의미:

- source / fragment / measurement / observer를 닫기 전에 먼저 남기는 line

핵심 경로:

- [CURRENT.md](/Users/sungsookim/universe/vectorfl_replica/CURRENT.md)
- [app/fragment](/Users/sungsookim/universe/vectorfl_replica/app/fragment)
- [app/measurement](/Users/sungsookim/universe/vectorfl_replica/app/measurement)
- [app/core](/Users/sungsookim/universe/vectorfl_replica/app/core)

정리 원칙:

- 보존 우선, overwrite 금지, reread 가능성 유지가 기준이다.

### C. input routing line

의미:

- 입력이 바로 실행되지 않고 parse / normalize / register / provenance를 거쳐 들어오는 line

핵심 경로:

- [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
- [app/input_layer](/Users/sungsookim/universe/vectorfl_replica/app/input_layer)
- [runtime/manifests/origin_maps](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/origin_maps)
- [observer_ingest_min](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min)

정리 원칙:

- input 관련 기존 자료는 버리기 전에 provenance / routing 의미가 있는지 먼저 본다.

### D. observation and line-thickening line

의미:

- 후보를 덮어쓰는 대신 observation을 append하고 reread를 통해 선을 두껍게 하는 line

핵심 경로:

- [line_thickening.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/line_thickening.py)
- [latent_line_registry_and_material_scan_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/latent_line_registry_and_material_scan_v1.md)
- [internal_space_line_drawing_practice_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/internal_space_line_drawing_practice_v0.md)
- [runtime/manifests/latent_line_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/latent_line_registry_v1.json)

정리 원칙:

- line 관련 오래된 자료는 바로 버리지 않는다.
- `line source` 와 `line residue`를 먼저 가른다.

### E. surface and readout line

의미:

- receipt, latest board, source/measurement/process console/viewer로 기록을 다시 읽는 line

핵심 경로:

- [runtime/views](/Users/sungsookim/universe/vectorfl_replica/runtime/views)
- [runtime/receipts](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts)
- [app/runtime](/Users/sungsookim/universe/vectorfl_replica/app/runtime)
- [app/core/runtime/viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)

정리 원칙:

- latest / canonical surface만 남기고, 반복 generated는 residue로 내릴 수 있다.

### F. promotion governance line

의미:

- 실험을 바로 코어에 박지 않고 checklist, trigger, thin rules로 늦추는 line

핵심 경로:

- [thin_operation_rules_lock_v1.md](/Users/sungsookim/universe/vectorfl_replica/thin_operation_rules_lock_v1.md)
- [core_promotion_checklist_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/core_promotion_checklist_v1.md)
- [refinement_trigger_rules_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/refinement_trigger_rules_v1.md)

정리 원칙:

- stage 결과를 버릴 때도 “이게 promotion 근거였는가”를 먼저 본다.

## emergent lines

### A. transcript preprocess line

근거:

- `app/work/external_input_preprocess`
- transcript 비교 / regroup / post-preprocess probe 스크립트
- external case 보고서 다수

판정:

- 아직 코어 line은 아니지만 반복도가 높아 `emergent line`으로 본다.

### B. multi-lens reading line

근거:

- multi-lens runtime flow
- reading / segmentation validation
- structured doc routing에서 관찰면으로 확장

판정:

- line 후보로 충분하다.
- 단순 side experiment로 치우면 안 된다.

### C. operating state/history line

근거:

- `app/runtime/state_*`
- process console/history 계열
- phase1/phase2 operating surfaces

판정:

- 사용자 readout line의 확장선이다.
- 아직 wrapper와 구현 경계가 흐려서 재구성 대상이다.

### D. external case cohort validation line

근거:

- `docs/reports/*engine_purpose_validation*`
- `*multi_pass_validation*`
- `*paragraph_role_validation*`
- `*process_trace_validation*`

판정:

- 개별 문서는 residue가 많지만, cohort validation 자체는 line으로 남길 가치가 있다.

## space classification

### 1. top-level

- `app/`: locked line 구현 공간
- `docs/`: line memory와 operator-facing interpretation 공간
- `runtime/`: canonical runtime evidence + generated accumulation 공간
- `references/`: 비교와 외부 참조 공간
- `source_assets/`: declaration / baseline / directive 원천 공간
- `inputs/`: raw input 공간

### 2. app/work

#### keep as line source

- `current_layer_baseline`
- `observer_ingest_min`
- `mixed_reentry_probe_stage1`
- `mixed_reentry_observer_stage2`
- `mixed_corridor_boundary_probe_stage3`
- `mixed_corridor_format_disentangle_stage4`
- `technical_business_corridor_decompose_stage5`

#### keep as emergent line source

- `external_input_preprocess`
- `dialogue_loop_test`
- `operating_ui`

#### keep as support cluster

- `processor_compare`
- `archive_review/transition_support/workbench_stage1`
- `archive_review/transition_support/result_value_bundle_stage1`
- `operating_ui/fixtures`
- `archive_review/transition_support/youtube_transcript_probe_0322`
- `archive_review/transition_support/youtube_transcript_probe_0322_b`
- `archive_review/probe_support/future_segment_probe`
- `archive_review/probe_support/concept_segment_probe`
- `archive_review/external_case_support/external_case_flowline_sweep`
- `archive_review/external_case_support/external_case_folder_sweep`
- `archive_review/interview_support/middle_layer_experiments`
- `archive_review/transition_support/transition_mixed_close_reading`
- `archive_review/transition_support/transition_mixed_surface_refine`

예외 잠금:

- `processor_compare` 는 support cluster이지만 archive belt로 내리지 않는다.
- 이유는 `app/core/runtime` 과 여러 ingest/runtime helper가 직접 import 하며, 단순 보관물이 아니라 현재 비교/anchor/observer sidecar의 실행 기반이기 때문이다.
- 따라서 이 폴더는 `root-retained support cluster` 로 취급한다.

#### archive review candidate

- `archive_review/experiments`
- `archive_review/evaluations`
- `archive_review/prompts`

이 세 폴더는 실제로 `archive_review` 아래로 1차 이동했다.
현재는 보존 상태를 유지하되, 다음 정리 배치에서 세부 재분류가 필요하다.

추가 1차 이동:

- `result_value_bundle_stage1`
- `transition_mixed_close_reading`
- `transition_mixed_surface_refine`
- `workbench_stage1`
- `youtube_transcript_probe_0322`
- `youtube_transcript_probe_0322_b`

이 여섯 support cluster는 [app/work/archive_review/transition_support](/Users/sungsookim/universe/vectorfl_replica/app/work/archive_review/transition_support) 아래로 이동했다.

### 3. root markdown files

#### keep at root

- [CURRENT.md](/Users/sungsookim/universe/vectorfl_replica/CURRENT.md)
- [vectorfl_status.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_status.md)

#### keep but review as line source or interpretation anchor

- [vectorfl_philosophical_interpretation_v1.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_philosophical_interpretation_v1.md)
- [tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md](/Users/sungsookim/universe/vectorfl_replica/tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md)
- [external_case_example_saltlux_goover_relation_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/external_case_example_saltlux_goover_relation_reading_v0.md)
- [codex_content_pack.md](/Users/sungsookim/universe/vectorfl_replica/codex_content_pack.md)
- [codex_processor_standard.md](/Users/sungsookim/universe/vectorfl_replica/codex_processor_standard.md)

## docs report family map

`docs/reports/` 는 파일 단위로 보면 과밀하지만, family 단위로 보면 몇 개 line belt로 압축된다.

### keep as locked or emergent line belt

- `line_thickening_*`
  - observation and line-thickening line의 핵심 belt
- `operating_ui_*`, `phase1_*`, `phase2_*`, `history_*`
  - surface and readout line의 확장 belt
- `latent_line_*`
  - line memory belt
- `multi_lens_*`
  - emergent line belt
- `folder_*`
  - 공간 정리 판단 belt

현재 1차 재배치:

- `multi_lens_*` 일부는 [docs/reports/multi_lens](/Users/sungsookim/universe/vectorfl_replica/docs/reports/multi_lens) 아래로 이동했다.
- `folder_*` 핵심 점검 문서는 [docs/reports/space_structure](/Users/sungsookim/universe/vectorfl_replica/docs/reports/space_structure) 아래로 이동했다.
- `history_companion_*` 묶음은 [docs/reports/history](/Users/sungsookim/universe/vectorfl_replica/docs/reports/history) 아래로 이동했다.

### keep as cohort validation belt

- `*_engine_purpose_validation_*`
- `*_multi_pass_validation_*`
- `*_paragraph_role_validation_*`
- `*_process_trace_validation_*`
- `question_inducing_block_*`

이 계열은 개별 파일 중복이 있어도 cohort 자체는 line source 또는 line residue로 남긴다.

### candidate for condensation

- 동일 cohort 안에서 형식만 다른 반복 validation 문서
- 동일 기능의 wording/polish 세부 점검 문서
- 구현 이전 중간 메모 성격의 v0 보고서

이 계열은 파일별 삭제보다 `family summary + exemplar 보관` 방식이 맞다.

## generated retention companion

generated / manifest / log 자산의 보존 기준은
[generated_retention_map_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/generated_retention_map_v1.md)
를 따른다.

현재 broad cleanup 종료선은
[cleanup_freeze_boundary_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/cleanup_freeze_boundary_v1.md)
를 따른다.

## old material evaluation rule

기존 자료를 버리기 전에 아래 순서로 본다.

1. 이 자료가 어떤 line을 처음 드러냈는가
2. 이 자료의 판단이 다른 문서/코드/runtime evidence에 다시 등장하는가
3. 이미 다른 canonical 문서에 흡수되었는가
4. 실패 사례 또는 residue로 남길 가치가 있는가

아래 중 하나라도 참이면 바로 삭제하지 않는다.

- line source
- line residue
- canonical absorption trace

## immediate no-delete zones

아래 구역은 정리 전 재독이 먼저다.

- `docs/reports/` 의 line, validation, operating, history 관련 보고서
- `app/work/` 의 staged corridor 폴더
- 루트의 interpretation/reference 성격 md
- `source_assets/` 와 연결된 declaration / baseline 계열

## immediate cleanup-safe zones

아래는 line 의미를 거의 잃지 않고 정리할 수 있다.

- `.DS_Store`
- `__pycache__`
- `*.pyc`
- `runtime/sandboxes`
- `runtime/tmp`

단, `runtime/sandboxes` 는 먼저 재귀 생성 원인을 막은 뒤 비우는 것이 맞다.
2026-04-05 기준으로 nested `sandboxes/` 자기복제 하위는 제거했다.
지금 남은 top-level sandbox는 원인 분석 전까지 보관한다.

추가 주의:

- 새 `.gitignore` 는 앞으로의 오염 유입을 줄이는 장치다.
- 이미 Git이 추적 중인 `.DS_Store`, `__pycache__`, `*.pyc` 는 별도 정리 배치에서 index 기준으로 제거해야 한다.

## next cleanup phases

### phase 1

- import 기준선 복구
- `app/core/runtime` 와 `app/runtime` 경계 정리 시작
- cache / sandbox / temp ignore 잠금

### phase 2

- `docs/reports` 를 line belt 기준으로 재분류
- `app/work` 를 line source / support cluster / archive review로 재배치

### phase 3

- representative generated만 남기고 반복 generated를 residue 보관 또는 archive
- root md 중 interpretation / declaration anchor 재배치

## one-line lock

이번 공간 정리는 `무엇을 지울까`가 아니라 `어떤 line이 이 공간의 의미를 만들었고, 그 line을 살리려면 무엇을 남기고 무엇을 내려야 하는가`를 먼저 판정하는 작업이다.
