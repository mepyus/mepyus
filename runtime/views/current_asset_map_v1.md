# current_asset_map_v1.md

## 1. current repo state

- 상태: state-first process console 엔진의 1차 운영층 freeze 완료
- 한 줄 요약: canonical operating state core와 derived operating layer가 잠겼고, process console이 latest + lineage + diff + attention + memory를 읽는 메인 표면으로 고정된 상태
- 현재 최우선 축:
  - core / derived / surface / experimental 경계 유지
  - process console surface drift 방지
  - current map + delta log + shared reality pack 갱신 루틴 고정
  - latest / history / derived surface read consistency 유지
  - experimental namespace의 기본 표면 침투 방지
- 현재 금지/보류 축:
  - graph-first 본체 재정의
  - derived layer의 canonical 오인
  - experimental naming의 무단 core 승격
  - latest 직접 overwrite
  - policy 우회 state write

---

## 2. current priority

1. state-first process console 운영 기준 유지
2. current_asset_map / repo_delta_log / shared reality pack 갱신 루틴 고정
3. core / derived / surface / experimental 경계 유지
4. latest / history / derived surface read consistency 유지

---

## 3. current SSOTs

### intake SSOT
- path: [engine_input_lane_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/engine_input_lane_baseline_v1.md)
- role: 입력 lane 기준문
- status: locked

### workspace SSOT
- path: [codex_baseline_program_grade_workspace_upgrade_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md)
- role: 프로그램형 작업공간 승격 기준문
- status: locked

### folder role SSOT
- path: [folder_role_table_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/folder_role_table_v1.md)
- role: 폴더 책임표
- status: locked

### shared reality pack index
- path: [repo_shared_reality_pack_index_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/repo_shared_reality_pack_index_v1.md)
- role: shared reality pack 공식 입구 문서
- status: active_current

### delta surface SSOT
- path: [repo_delta_log_latest_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/repo_delta_log_latest_v1.md)
- role: 최근 구조 변화와 읽기 우선순위 변화 요약면
- status: active_current

### operating layer freeze SSOT
- path: [engine_operating_layer_freeze_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/engine_operating_layer_freeze_v1.md)
- role: 현재 engine stack의 `core / derived / surface / experimental` 경계와 authoritative hierarchy를 잠그는 공식 freeze 기준문
- status: locked

### operating layer manifest
- path: [engine_operating_layer_manifest_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_operating_layer_manifest_v1.json)
- role: 현재 operating layer 분할과 hierarchy를 machine-readable하게 보여주는 manifest
- status: active_current

### engine memory spine
- path: [engine_memory_spine_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_memory_spine_v1.json)
- role: 철학 방향성 / 사용자 문제 인식 / 자원 경계 / run 에피소드 / current reality를 어떤 층으로 외부화해 기억할지 보여주는 memory spine
- status: active_current

### operator problem-recognition memory
- path: [operator_problem_recognition_basis_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/memory/problem_recognition/operator_problem_recognition_basis_v1.md)
- role: 사용자가 문제를 어떻게 인식하고 어떤 작은 간극을 중요하게 보는지 복원하기 위한 operator memory
- status: active_guidance

### engine memory spine spec
- path: [engine_memory_spine_and_context_externalization_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/engine_memory_spine_and_context_externalization_v1.md)
- role: 무엇을 어느 층에 외부화해 기억하고 컨텍스트 회전 시 어떤 순서로 복귀할지 잠그는 기준문
- status: locked

### next-phase direction declaration
- path: [program_grade_next_phase_declaration_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/declarations/program_grade_next_phase_declaration_v1.md)
- role: 코어 보존, intake/shared reality 우선, read-only operation view 선행이라는 다음 단계 방향 선언
- status: locked

### surface maintenance directive
- path: [program_grade_workspace_surface_maintenance_directive_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/directives/program_grade_workspace_surface_maintenance_directive_v1.md)
- role: current / delta / shared reality를 짧고 정확하게 유지하는 운영 지시
- status: active_guidance

### surface maintenance checklist
- path: [program_grade_workspace_surface_maintenance_checklist_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/directives/program_grade_workspace_surface_maintenance_checklist_v1.md)
- role: 기준면 drift를 짧고 반복 가능하게 점검하는 체크리스트
- status: active_guidance

### reusable internal hardening directive
- path: [codex_reusable_internal_hardening_process_directive_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/directives/codex_reusable_internal_hardening_process_directive_v1.md)
- role: 외곽은 잠그고 standard / external / general 비교를 통해 내부 판단 기준과 사고 흐름을 bounded micro-tuning으로 이식하는 재사용 운영 지시
- status: active_guidance

### future scaling guardrails directive
- path: [codex_future_scaling_guardrails_directive_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/directives/codex_future_scaling_guardrails_directive_v1.md)
- role: judgment versioning, reasoning residue, hold discipline, evidence-gated outer-layer governance, failure-axis comparison을 다음 성장 단계의 운영 경계선으로 잠그는 지시
- status: active_guidance

### connection meaning and user-layer translation baseline
- path: [connection_meaning_and_user_layer_translation_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/connection_meaning_and_user_layer_translation_baseline_v1.md)
- role: engine-internal refinement를 바로 진행하지 않고, 연결의 의미와 사용자 질문의 층위 번역을 먼저 확인하게 만드는 상위 기준선
- status: active_guidance

### repeated learning asset exposure baseline
- path: [repeated_learning_asset_exposure_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/repeated_learning_asset_exposure_baseline_v1.md)
- role: Codex가 철학과 운용 감각을 한 번에 체득한다고 가정하지 않고, baseline / directive / example / review 자산을 반복 참조시키는 학습 운영 기준선
- status: active_guidance

### vectorfl engine job definition
- path: [vectorfl_engine_job_definition_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/vectorfl_engine_job_definition_v1.md)
- role: 엔진을 단순 분류기나 검색기가 아니라 객체 성장, 관계 누적, 사용자 층위 번역, 기억 바닥 유지까지 맡는 공간 운영 엔진으로 정의하는 직무 baseline
- status: active_guidance

### high-density dialogue asset loop testing baseline
- path: [high_density_dialogue_asset_loop_testing_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/high_density_dialogue_asset_loop_testing_v1.md)
- role: youtube dialogue script 같은 고밀도 대화 자산을 객체/층위/관계/질문 의도 판독 능력을 반복 검증하는 학습형 테스트 자산으로 읽게 하는 기준선
- status: active_guidance

### multi-pass interpretation and context-unit rereading baseline
- path: [multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1.md)
- role: 같은 자산을 여러 해석 레이어로 반복 읽고, 그 차이로 문단보다 더 살아 있는 context unit을 다시 세우며 Codex가 사용자의 의미 층위 감각과 질문 방식을 학습하게 하는 훈련 기준선
- status: active_guidance

### input reading and internal maturation baseline
- path: [input_reading_maturation_and_operating_space_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/input_reading_maturation_and_operating_space_baseline_v1.md)
- role: 엔진 운용을 입력 구조와 내부 숙성 구조로 분리하고, 1차 판독값과 2차 보정값을 나눠 내부 재료와 loop/script로 상위 해석 객체를 길러내게 하는 운영 기준선
- status: active_guidance

### entry gate common blocker baseline
- path: [entry_gate_common_blocker_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/entry_gate_common_blocker_baseline_v1.md)
- role: `ENTRY_GATE_NOT_PASSED`를 막연한 보류가 아니라 반복된 공통 blocker 묶음으로 읽게 하여, 다음 판단을 실험 제안보다 blocker 약화 기준으로 정렬하는 운영 기준선
- status: active_guidance

### user-friendly label and anchor refinement directive
- path: [user_friendly_label_and_anchor_refinement_before_lexicon_thickening_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/directives/user_friendly_label_and_anchor_refinement_before_lexicon_thickening_v1.md)
- role: axis를 건드리지 않고 label/anchor surface를 사용자 친화적으로 조율한 뒤, 사전류 기반 기억 두께 강화는 후행으로 미루게 하는 bounded refinement 지시
- status: active_guidance

---

## 4. current operating entrypoints

### intake entrypoint
- path: [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
- role: 현재 intake 실행과 structured doc routing의 공식 시작점
- note: 표준문서 intake와 receipt/routing 기록의 기본 entrypoint

### registry / provenance entrypoint
- path: [run_provenance_dedupe_review.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_provenance_dedupe_review.py)
- role: provenance hygiene 점검의 대표 실행 entrypoint
- note: append core는 `app/core/registry/`에 있고, 운영 점검 entry는 이 스크립트를 우선 본다

### runtime / render entrypoint
- path: [folder_status_sync.py](/Users/sungsookim/universe/vectorfl_replica/scripts/folder_status_sync.py)
- role: folder status / inventory / rendered status 동기화의 공식 시작점
- note: latest/read surface 반영과 구조 상태 sync에 가장 자주 쓰는 진입점

### process console runtime entrypoint
- path: [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)
- role: process console과 secondary view를 여는 공식 runtime surface entrypoint
- note: 현재 메인 표면은 graph가 아니라 `/process-console`

### validation / check entrypoint
- path: [run_structured_doc_stability_check.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_structured_doc_stability_check.py)
- role: 구조/경로/상태 점검의 공식 시작점
- note: 일회성 check script보다 현재 반복 검증에 쓰는 entrypoint를 우선 둔다

### 기타 운영 핵심
- name: exploration observation stub
- path: [create_exploration_observation_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/create_exploration_observation_stub.py)
- role: exploration observation sidecar 초안 생성 helper
- note: thin operation rules 기반 observation layer 보조 스크립트

---

## 5. current read surfaces

### primary current reality
- path: [repo_shared_reality_pack_index_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/repo_shared_reality_pack_index_v1.md)
- role: shared reality pack 전체를 한 번에 가리키는 공식 진입면
- 언제 읽는가: 구조 현실을 맞추기 위해 가장 먼저 읽는다

### current asset map
- path: [current_asset_map_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/current_asset_map_v1.md)
- role: 지금 repo에서 무엇이 기준이고 무엇이 핵심이며 무엇이 아직 실험인지 보여주는 공식 현재 현실면
- 언제 읽는가: index를 본 뒤 현재 상태와 SSOT를 파악할 때 읽는다

### operating layer manifest
- path: [engine_operating_layer_manifest_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_operating_layer_manifest_v1.json)
- role: core / derived / surface / experimental 분리와 authoritative hierarchy를 얇게 확인하는 current operating manifest
- 언제 읽는가: process console stack의 layer 경계를 빠르게 확인할 때 읽는다

### delta latest
- path: [repo_delta_log_latest_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/repo_delta_log_latest_v1.md)
- role: 최근 구조 변화와 읽기 우선순위 변화 요약면
- 언제 읽는가: current map을 본 뒤 최근 변경을 확인할 때 읽는다

### latest board / command surface
- path: [operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
- role: 현재 작업/지시/운영 보드면
- 언제 읽는가: 실제 운영 흐름 또는 즉시 실행 기준을 볼 때 읽는다

### summary / compacted surface
- path: [provenance_compacted_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/provenance_compacted_latest.md)
- role: 압축된 provenance 최신 읽기면
- 언제 읽는가: 원로그 대신 얇은 최신면이 필요할 때 읽는다

### 기타 읽기면
- name: exploration observation surfaces
- path: [runtime/observer/exploration](/Users/sungsookim/universe/vectorfl_replica/runtime/observer/exploration)
- role: exploration observation json/md sidecar 읽기면
- 언제 읽는가: 외부사례 first-pass와 observation layer 상태를 볼 때 읽는다

---

## 6. current intake state

### active intake lanes
- declaration
- baseline
- directive
- external_input
- general_input
- unclassified

### current intake emphasis
- 현재 많이 들어오는 입력:
  - AI 관련 external_input
  - declaration / baseline / directive 계열 표준문서
- 현재 intake line에서 주로 보는 문제:
  - lane 힌트 부족
  - external canonical source 정리
  - general_input과 baseline 초안 혼합
  - unclassified 처리 후 재판독 기준 안정화
- 현재 보정 중인 부분:
  - external_input first-pass chain
  - canonical source 우선 intake
  - shared reality pack 기준으로 intake 해석 정렬

---

## 7. zone status

### locked zones
- path: [docs/policies](/Users/sungsookim/universe/vectorfl_replica/docs/policies)
- reason: 상위 기준문 보관 구역
- note: baseline / policy 계열은 쉽게 흔들지 않는다

- path: [docs/specs](/Users/sungsookim/universe/vectorfl_replica/docs/specs)
- reason: 구조 명세 및 책임표 보관 구역
- note: 역할 명세는 SSOT 기준으로 유지한다

- path: [source_assets/baselines](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines)
- reason: source baseline 원문 보관 구역
- note: canonical baseline 자산은 여기서 회수한다

- path: [source_assets/declarations](/Users/sungsookim/universe/vectorfl_replica/source_assets/declarations)
- reason: source declaration 원문 보관 구역
- note: 방향 선언은 source asset으로 보존한다

### semi-locked / caution zones
- path: [runtime/views](/Users/sungsookim/universe/vectorfl_replica/runtime/views)
- reason: 공식 읽기면이지만 latest/current 재정렬 가능성 존재
- note: 읽을 수는 있으나 raw history 전체를 대체하지 않는다

- path: [runtime/contracts](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts)
- reason: exploration/readout 계약과 판독 결과가 모이는 구역
- note: 반복 참조 대상이지만 상위 기준문과는 위상이 다르다

### work / experiment zones
- path: [app/work](/Users/sungsookim/universe/vectorfl_replica/app/work)
- reason: 엔진 근접 실험/관찰/비교 구역
- note: 유용해 보여도 즉시 기준 자산처럼 인용하지 않는다

- path: [work](/Users/sungsookim/universe/vectorfl_replica/work)
- reason: 임시 실험 및 보조 작업 구역
- note: 존재 시 검증 전에는 lock 금지

- path: [runtime/tmp](/Users/sungsookim/universe/vectorfl_replica/runtime/tmp)
- reason: 임시 runtime 산출물 구역
- note: 공식 current surface로 오인하지 않는다

---

## 8. current cautions

- 일부 latest surface는 raw registry / history를 완전히 대체하지 않는다
- work 자산은 유용해 보여도 SSOT처럼 인용하면 안 된다
- old 문서가 남아 있어도 current SSOT는 본 문서의 SSOT 섹션을 우선한다
- path만 보고 자산 위상을 단정하지 말고 role과 zone 상태를 함께 본다
- `inputs/external_cases`는 새 raw input 기준은 명확하지만 과거 mixed md가 일부 같이 보인다
- refinement trigger는 candidate 상태까지 올라왔지만 아직 정련 패스를 실행하지 않았다

---

## 9. recent structural change summary

- canonical operating state core가 schema / store / history / latest / policy / fixture까지 잠겼다
- process console이 latest + lineage + diff + attention + memory를 읽는 메인 표면으로 고정됐다
- runtime evidence bridge와 attention queue / resolution / memory가 붙어 state-first 운영 루프가 형성됐다
- current engine stack은 `core / derived / surface / experimental` 4계층으로 freeze 완료됐다

---

## 10. next steps

1. current_asset_map / repo_delta_log / shared reality pack 갱신 루틴 유지
2. process console surface drift 점검
3. derived layer 확장은 queue/attention/history readability tuning 범위에서만 진행

---

## 11. reading rule

### user
- 먼저 [repo_shared_reality_pack_index_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/repo_shared_reality_pack_index_v1.md)를 본다
- 그다음 이 문서를 본다
- 최근 변경은 [repo_delta_log_latest_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/repo_delta_log_latest_v1.md)를 본다
- 기준 충돌이 의심되면 SSOT 문서를 연다

### assistant
- 구조 판단 시 [repo_shared_reality_pack_index_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/repo_shared_reality_pack_index_v1.md)와 이 문서를 공식 현실면으로 본다
- 옛 대화 기억보다 이 문서와 delta log를 우선한다

### codex
- 실제 수정 후 이 문서를 갱신한다
- entrypoint / primary view / zone status가 바뀌면 반드시 반영한다

---

## 12. final lock

이 문서는 전체 폴더 트리를 대신하는 덤프가 아니다.  
이 문서는 지금 repo에서 무엇이 기준이고 무엇이 핵심이며 무엇이 아직 실험인지를 가장 짧게 고정하는 공식 현재 현실면이다.

현재 한 줄 잠금:

**이 repo의 현재 본체는 graph-first 결과판이 아니라, canonical state core 위에 derived operating layer를 얹고 process console이 이를 읽는 state-first operating engine이다.**
