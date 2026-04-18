# repo_delta_log_latest_v1.md

## latest addendum

- 2026-03-29: `reference/washtank/src/officeout.jsx` 요청을 실제 repo 구조인 `references/WashTank/app/main/Officeout.jsx` 기준으로 재해석해 donor feasibility review를 남겼다. 판정은 `조건부 OK`이며, `Officeout`은 보드 셸/카드/우측 패널 donor로는 유효하지만, 서비스 결합과 wash tank naming이 강하고 상세 모달은 같은 donor군의 `TankControl`/`Fhandler`에서 별도 추출해야 한다.
- 2026-03-29: 메모리 한계를 전제로 `engine_memory_spine_and_context_externalization_v1`와 `engine_memory_spine_v1.json`을 추가했다. 철학 방향성 기억, 사용자 문제 인식 기억, 자원 경계 기억, run 에피소드 기억, current reality 기억을 분리한 memory spine을 만들고, `runtime/memory/problem_recognition/`을 새 층으로 열어 사용자 문제 인식 방식을 별도 operator memory로 외부화했다.
- 2026-03-29: 현재 대화의 철학적 맥락을 모든 처리의 상위 기준으로 쓰기 위해 `engine_philosophical_directionality_checklist_v1`를 추가했다. 이 체크리스트는 자동화, 위임, canonicalization, process-console 운용이 단순 수학적 처리나 결과 생산으로 납작해지지 않고, 차이·층위·과정 기억을 보존하는 방향성을 유지하는지 점검하는 최상위 기준문이다.
- 2026-03-29: Gemini 및 향후 외부 자원 위임의 전제 기억을 `resource_capability_boundary_memory_v1`로 고정했다. 외부 자원을 Codex와 동등한 처리 주체로 가정하지 않고, 능력 차이와 실패 위험을 먼저 기록한 뒤 반복 검증을 거쳐서만 delegation 범위를 넓히는 원칙을 잠갔다.
- 2026-03-29: `gemini/` 폴더를 점검하고, Gemini CLI handoff 경계를 `gemini_task_dispatch_policy_v1`와 `gemini_task_assignment_checklist_v1`로 고정했다. 이제 Gemini에는 summary/diff/pointer/discrepancy 같은 read-only 보조 업무만 넘기고, canonical 판정·state write·policy/freeze 변경·승격은 계속 Codex 전담으로 유지한다.
- 2026-03-29: `choi_ai_classroom_*` 계열 4개를 lecture transcript cohort로 batch 실행했다. 모두 `index_support / w6 / s3`에서 multi-window packet을 만들었고, canonical state는 공통적으로 `structured_open_low_emergence / partially_grounded / low_emergence / medium carryover / weak / traceable`로 수렴했다. 따라서 이 cohort는 turboquant 대비 `lecture-structured recoverable cohort`로 잠갔다.
- 2026-03-29: 메인 테크니션-자동화 경계 정리를 추가했다. 앞으로 probe/state refresh/queue/memory/process-console payload/receipt-log 같은 반복 루프는 가능한 한 스크립트화하고, canonical enum 선택, compare verdict, blocker 의미 분리, freeze policing 같은 경계 판단은 메인 테크니션 직접 판단층으로 고정한다.
- 2026-03-29: `turboquant_youtube`에 대해 baseline 대비 resegmentation/rewindow compare를 수행했다. `w3/s1/index_support`, `w4/s2/index_support` 모두 `block_count=1`, `window_count=1`로 유지되어 packet/state 이동이 없었고, 이번 범위에서는 `segmentation-sensitive recoverable`보다 `compression-dominant intrinsic` 판정이 더 맞는 것으로 고정했다.
- 2026-03-29: `TurboQuant_youtube.txt`를 첫 실운용 입력으로 태워 `turboquant_youtube` canonical state를 생성했다. 이번 run은 source intake, probe packet, first canonical append, latest/history 갱신, diff/attention/memory 파생, process console read까지 실제로 관통했고, packet은 `overcompressed_closure_heavy`, carryover는 `high`, traceability는 `traceable`로 보수 판정했다.
- 2026-03-28: `runtime_evidence_priority_router_v1`와 `state_change_attention_queue_v1`를 추가해, process console이 최신 canonical state와 lineage/diff를 그대로 유지한 채 어떤 변화를 먼저 열어봐야 하는지 얇은 attention layer로 읽게 만들었다.
- 현재 representative recent update는 모두 `provenance_only`이므로 active queue로 올리지 않고 `background summary`로만 표면화한다.
- raw history, canonical schema, update policy는 그대로 유지되고, attention queue는 전부 derived surface로만 생성된다.
- 2026-03-28: `attention_resolution_loop_v1`를 추가해, attention item이 `new/suppressed/resolved/reopened` 생애주기를 가지도록 만들고, provenance-only flooding은 빠르게 suppressed/background로 흡수하며 stricter canonical shift 계열은 별도 active attention으로 남길 수 있는 바닥을 고정했다.
- 2026-03-29: `state_attention_memory_v1`를 추가해, 자산별 attention 반복 패턴을 얇게 기억하는 derived memory surface를 만들었다. 현재 representative 4개 자산은 모두 `mostly provenance_only background updates`로 읽히며, 이는 canonical state가 아니라 recent attention tendency를 요약한 운용 기억이다.
- 2026-03-29: `engine_operating_layer_freeze_v1`를 추가해 현재 stack을 `core / derived / surface / experimental` 4계층으로 공식 고정했다. 이 freeze는 state-first process console 엔진의 1차 운영층 완료선을 의미하며, 앞으로 core 변경은 explicit freeze 해제 없이 진행하지 않도록 경계를 잠근다.
- 2026-03-29: shared reality maintenance follow-up으로 `folder_status.md`, `current_asset_map_v1.md`, `repo_shared_reality_pack_index_v1.md`를 현재 process-console / layer-freeze 기준으로 재정렬했다. 이제 runtime/views의 child surface, operating-layer manifest, process-console 본체 위치가 공식 읽기면에도 반영된다.

## 1. delta snapshot

- snapshot_date: 2026-03-28
- snapshot_scope: recent bounded surface maintenance + external-case validation batches
- prepared_by: Codex
- related_run_or_change_batch: stable_with_minor_fix_bounded_surface_repair_001
- change_type_summary:
  - spec reality alignment
  - latest delta compaction
  - maintenance surface follow-up

---

## 2. one-line delta summary

- bounded surface repair 이후, same-topic transformer classroom intake/comparative/refinement pass와 `graphrag_neosh.txt` negative control pass를 거친 뒤, transformer classroom frame을 local candidate로만 유지하고 promotion hold 상태를 lock note로 고정했다

## 2A. recent comparison addendum

- `claude_code_index.txt`를 비교 도메인으로 넣어 4개 2차 축적 스크립트를 그대로 적용했다.
- 유지된 것:
  - question opening / relation movement / residue priority shift를 보려는 2차 판독 태도
  - `supporting_first_pass_patterns`, `domain_specific_suspicion`, `reusable_attitude_hint`, `candidate_status`, `hold_reason` 같은 축적 메타데이터
- 붕괴된 것:
  - block/window granularity가 단일 mega block으로 수렴
  - heading 기반 paragraph role reading이 바로 깨짐
  - context unit 재구성이 아직 `youtube_03_22` scaffold를 강하게 끌고 있음
- 새로 선명해진 것:
  - `single operational block collapse`
  - `AI object vocabulary overfire`
  - object lift를 아직 보류해야 하는 비교 근거

### current read

- 지금 2차 스크립트는 `잘 읽는 판정기`보다 `조건과 붕괴 양상을 남기는 축적기`로 보는 것이 맞다.
- 다음 단계는 object lift 본 구현이 아니라, repeated pattern / split note / candidate registry / operating surface를 비교 결과로 더 정교화하는 것이다.

## 2B. readable condition / scaffold / failure addendum

- 이번 턴에서는 2차 결과를 더 만들지 않고, 무엇이 어떤 조건에서 읽히고 어디서 scaffold-bound 하며 어떻게 실패하는지를 분리 기록했다.
- 신규 정리판:
  - `second_order_readable_condition_table_draft_v1`
  - `second_order_scaffold_dependency_log_v1`
  - `second_order_failure_accumulation_note_v1`
- 이번에 더 선명해진 것:
  - question opening / relation movement / residue priority shift는 조건만 맞으면 비교적 살아남는다
  - context unit / paragraph role / pivot 계열은 segmentation, heading, pointer scaffold 의존성이 높다
  - failure도 2차 자료이며, object lift hold의 직접 근거가 된다

### current read

- 지금은 `무엇을 읽었는가`보다 `무엇이 어떤 조건에서 읽히는가`를 먼저 남기는 단계다.
- 다음 단계도 여전히 object lift 구현이 아니라, failure와 readable condition을 더 쌓아 segmentation / role / pointer 보정의 정확한 출발점을 찾는 쪽이 맞다.

## 2C. scaffold reduction priority addendum

- 이번 턴에서는 scaffold dependency를 줄이는 우선순위와 구조 잠금을 먼저 고정했다.
- 신규 자산:
  - `second_order_scaffold_reduction_priority_matrix_v1`
  - `second_order_structure_lock_note_v1`
  - `minimal_scaffold_intervention_experiment_plan_v1`
- 현재 우선순위:
  - 1순위 `segmentation`
  - 2순위 `pointer`
  - 3순위 `heading`
- 현재 고정층:
  - 1차는 센서값
  - 2차는 재독해/보정/축적층
  - question opening / relation movement / residue priority shift 우선 관찰
  - object lift hold 유지
- 현재 실험층:
  - segmentation support
  - pointer stabilization
  - heading-independent role probe

### current read

- 지금은 더 잘 맞히는 단계가 아니라, 어떤 기관부터 줄여야 reusable attitude가 더 넓게 살아나는지 순서를 잠그는 단계다.
- 다음 최소 실험도 이 순서를 벗어나지 않는다.

## 2D. segmentation support probe addendum

- 이번 턴에서는 `claude_code_index.txt`에 대해 1순위 최소 개입 실험으로 `segmentation support` probe를 실제 실행했다.
- 최소 개입:
  - splitter 전면 교체 없이, 인덱스형 구조에서 짧은 제목행 + timestamp 패턴을 segmentation assist로 해석하는 얇은 support만 추가했다.
- baseline 붕괴:
  - block/window가 `1 / 1`로 collapse
  - downstream 2차 판독이 사실상 단일 mega block 위에만 매달림
- support 후 변화:
  - block/window 다양성은 `518 / 516` 수준으로 회복
  - relation movement surface와 reusable attitude 관찰 기반은 다시 확보됨
- support 후에도 남은 한계:
  - stable question-inducing candidate는 아직 0
  - pivot / compression은 실질 회복 안 됨
  - context unit ref empty 문제 유지
  - naming-with-support coherence도 여전히 약함

### current read

- segmentation은 2차 판독 생존의 필요조건이라는 점이 실제 비교로 확인됐다.
- 하지만 segmentation만으로는 충분하지 않았고, 다음 2순위 `pointer` 축이 왜 필요한지 더 선명해졌다.
- object lift hold는 그대로 유지된다.

## 2E. pointer stabilization probe addendum

- 이번 턴에서는 `segmentation support` 이후에도 남아 있던 grounding/ref 문제를 대상으로 `pointer stabilization` 최소 개입 실험을 실행했다.
- 최소 개입:
  - direct candidate ref가 없을 때, 이미 살아 있는 `purpose_synthesis top_windows`를 object-overlap 기반 fallback evidence pointer로 재연결하는 얇은 stitching만 추가했다.
- baseline after segmentation:
  - context unit `3 / 3` empty-ref
  - question-inducing candidate `0`
  - naming survives but support weak
- pointer support 후 변화:
  - empty-ref context unit은 `0`으로 감소
  - `fallback_grounded` context unit이 생김
  - naming-without-support는 일부 `better-supported hold`로 이동
- pointer support 후에도 남은 한계:
  - direct grounded context unit은 아직 `0`
  - question-inducing candidate는 여전히 `0`
  - pivot / compression은 direct support로 회복되지 않음

### current read

- pointer는 실제로 grounding/ref 품질에 영향을 주는 2순위 축이라는 점이 비교로 확인됐다.
- 다만 이번 회복은 `direct grounding`이 아니라 `fallback grounding`이며, object lift hold를 풀 수준은 아니다.
- 다음 3순위 `heading`은 여전히 paragraph-role 계열에만 국한된 후행 축으로 남는다.

## 2F. heading-independent role probe addendum

- 이번 턴에서는 `claude_code_index.txt`에 대해 3순위 최소 개입 실험으로 `heading-independent role probe`를 실행했다.
- 최소 개입:
  - explicit heading을 찾지 않고, pointer probe 이후 살아 있는 `context_unit`, `page_role`, `relation_movement`, `evidence_pointers`를 이용해 약한 `role-like hint`만 남기는 functional-cue probe를 추가했다.
- baseline after pointer:
  - paragraph role 기관은 여전히 heading mismatch에 강하게 묶여 있었음
  - role 계열은 사실상 hard fail 또는 rigid mapping risk 상태였음
- heading probe 후 변화:
  - role-like analyses `3`건 생성
  - 모두 evidence-linked pointer를 가짐
  - unsupported role naming 증가는 통제됨
- heading probe 후에도 남은 한계:
  - 전부 `weak_medium + fallback_grounded`
  - generalized paragraph-role system recovery는 아님
  - question-inducing candidate 공백은 그대로임

### current read

- heading은 3순위가 맞고, hard failure를 `weak evidence-linked role-like reading`으로 낮추는 정도의 가치가 확인됐다.
- 하지만 role 계열은 여전히 reusable attitude라기보다 scaffold-bound institution에 더 가깝다.
- object lift hold는 그대로 유지된다.

## 2G. three-axis integration addendum

- 이번 턴에서는 segmentation / pointer / heading 최소 개입 실험 결과를 하나의 현재 판정 구조로 통합했다.
- 공식 역할 분리:
  - segmentation = 필요조건 복구축
  - pointer = grounding 보강축
  - heading = weak role-probe 보조축
- 공식 현재 상태:
  - reusable attitude는 일부 살아남음
  - 구조 기관은 아직 weak / fallback / partial 수준에 머무름
- 공식 hold read:
  - object lift hold는 감각적 보수성이 아니라, direct grounding 부족 / candidate zero 지속 / role 기관 약함 / naming carryover 위험에 근거한 구조 판정이다
- 공식 다음 루프 read:
  - 다음 루프는 승격 루프가 아니라, weak/fallback recovery가 반복 가능성과 directness를 얻는지 검증하는 조건부 루프다

### current read

- 지금 2차 계층은 상위 승격 직전이 아니라, 실험 결과를 운영 규정과 진입 게이트로 잠그는 단계다.
- object lift hold는 유지되고, 다음 반복은 entry criteria가 충족될 때만 열린다.

## 2H. openai_02_11 gate validation addendum

- 이번 턴에서는 `inputs/external_cases/openai_02_11.md`를 현재 잠근 3축 구조와 `next loop entry gate` 기준 위에서 비교 검증했다.
- 확인된 것:
  - single block collapse 없이도 reusable attitude는 살아남는다
  - `question opening`, `relation movement`, `residue priority shift`는 중간 구조 자산에서도 다시 나타난다
  - object/layer/relation purpose reading은 강하게 유지된다
- 그러나 같이 확인된 한계:
  - question-inducing candidate는 여전히 `0`
  - context unit은 전부 `fallback_grounded`
  - role-like reading은 이 자산에서 사실상 회복되지 않음
  - 따라서 `next loop entry gate`는 통과하지 못함

### current read

- `openai_02_11`은 현재 2차 계층이 완전히 AI dialogue overfit 상태는 아님을 보여준다.
- 하지만 동시에 reusable attitude survival만으로는 다음 gated loop를 열 수 없고, direct grounding / candidate emergence / repeated role-like recovery가 여전히 부족하다는 점도 같이 확인해 준다.

## 2I. graphrag / enterprise gate validation addendum

- 이번 턴에서는 비교 예제 2순위 / 3순위였던 `graphrag_neosh.txt`, `enterprise.txt`를 현재 잠근 3축 구조 위에서 실제로 검증했다.
- baseline 결과:
  - 두 자산 모두 `1 / 1` collapse
  - 즉 baseline 자체로는 next-loop validation 대상이 아니라 segmentation support가 먼저 필요한 자산이었다.
- segmentation support 후:
  - `graphrag_neosh`: `200 / 67`
  - `enterprise`: `334 / 111`
  - 즉 segmentation은 다시 한번 필요조건 복구축으로 확인됐다.
- 그러나 support 이후에도:
  - question-inducing candidate는 둘 다 `0`
  - context unit은 둘 다 `fallback_grounded`
  - role-like reading은 `weak_medium`만 회복
  - context scaffold naming이 두 자산에서 거의 동일하게 carryover 됨

### current read

- 이 두 자산은 현재 2차 계층이 완전히 무너지는 건 아니라는 점을 보여주지만, gate를 열 근거는 주지 않는다.
- 오히려 reusable attitude는 살아남되 institution은 아직 scaffold-bound 하다는 현재 공식 판정을 cross-asset 쪽에서 더 두껍게 지지한다.

## 2J. entry gate common bottleneck addendum

- 이번 턴에서는 `openai_02_11`, `graphrag_neosh`, `enterprise`, `claude_code_index`의 gated validation 결과를 통합해 `ENTRY_GATE_NOT_PASSED`의 공통 blocker 구조를 압축했다.
- 공통 blocker:
  - non-zero question-inducing candidate 부재
  - fallback grounding dominance
  - weak role-like only
  - pivot/compression non-recurrence
  - scaffold carryover risk

## 2K. operating surface component reinforcement addendum

- 이번 턴에서는 `engine_operating_surface_component_spec_v1`에 process console 성격을 더 강하게 잠그는 보강점을 명시적으로 추가했다.
- 강화된 포인트:
  - `AssetRail`의 `comparison memory reason`
  - `MemoryPacketBridgePanel`의 `packet formation why`
  - `SecondOrderRereadingPanel`의 `new opening vs carryover` 분리
  - `MaturationStatePanel`의 `state history / time axis`

### current read

- 이 보강은 UI 편의 추가가 아니라, 운용화면이 결과 전시판이 아니라 process console로 읽히게 만드는 최소 reinforcement다.

## 2L. engine operating state schema addendum

- 이번 턴에서는 recent process-trace / packet / second-order 자산 위에서 바로 사용할 수 있는 canonical operating-state schema를 고정했다.
- 신규 자산:
  - `docs/specs/engine_state_schema_v1.md`
  - `app/core/schemas/engine_state_schema_v1.json`
- 코드 바닥 추가:
  - `app/core/states.py`
    - `PacketTexture`
    - `GroundingStatus`
    - `EmergenceStatus`
    - `CarryoverRisk`
    - `MaturationState`
    - `TraceabilityStatus`
    - `ComparisonMemoryReason`
    - `GateBlockerSummary`
  - `app/core/models/entities.py`
    - `EngineStateRecord`

### current read

- 지금 canonicalize한 것은 상위 의미 객체가 아니라 운용 상태값이다.
- 즉 엔진은 먼저 `packet texture / grounding / emergence / carryover / maturation / traceability / comparison memory / gate blocker`를 공통 상태로 사용하고, naming 계열은 계속 experimental namespace에 보류한다.

## 2M. engine state store and backfill addendum

- 이번 턴에서는 `engine_state_schema_v1`를 실제 저장/조회 가능한 store layer로 연결했다.
- 신규 자산:
  - `app/core/state_store/engine_state_store.py`
  - `app/core/state_store/__init__.py`
  - `app/core/schemas/engine_state_schema_v1.json`
  - `docs/specs/engine_state_store_v1.md`
  - `docs/reports/engine_state_backfill_v1_report.md`
  - `runtime/views/engine_state_latest/index.json`
  - `runtime/views/engine_state_latest/youtube_03_22.json`
  - `runtime/views/engine_state_latest/openai_02_11.json`
  - `runtime/views/engine_state_latest/knowledge_editing_youtube.json`
  - `runtime/views/engine_state_latest/gary_tan_brain.json`
- representative backfill:
  - `youtube_03_22`
  - `openai_02_11`
  - `knowledge_editing_youtube`
  - `gary_tan_brain`

### current read

- 이제 process console은 자산 클릭 시 canonical operating state를 latest surface에서 바로 읽을 수 있다.
- canonical top-level에는 state field만 남기고, naming-heavy 해석은 `experimental_namespace`로 밀어내는 guard도 같이 작동한다.

## 2N. engine state update policy addendum

- 이번 턴에서는 canonical operating state의 생애주기 규칙을 `engine_state_update_policy_v1`로 고정했다.
- 신규 자산:
  - `docs/specs/engine_state_update_policy_v1.md`
  - `docs/reports/engine_state_update_policy_v1_adoption_note.md`
  - `app/core/state_store/engine_state_update_policy.py`
- 실제 연결:
  - `engine_state_store`가 `append-first`, `latest-is-derived`, `evidence-backed update`, `canonical contamination guard`를 policy helper를 통해 집행
  - representative backfill history에는 `update_trigger_type=backfill`, `update_reason=representative_asset_backfill_v1`가 실제 기록됨

### current read

- 이제 canonical operating state는 단순 값 저장을 넘어서, 언제 어떤 근거로 append되고 latest에 반영되는지까지 lifecycle rule이 잠겼다.
- top-level canonical field는 계속 state-first를 유지하고, naming-heavy 해석은 policy level에서도 experimental namespace에 묶인다.

## 2O. state validation fixture addendum

- 이번 턴에서는 representative asset 4개를 기준 fixture로 고정하고 canonical operating state layer의 repeatability를 검증했다.
- 신규 자산:
  - `docs/specs/state_validation_fixture_v1.md`
  - `docs/reports/state_validation_fixture_v1_report.md`
  - `scripts/run_state_validation_fixture_v1.py`
  - `app/core/state_store/state_validation_fixture.py`
  - `runtime/validation/state_fixture_expected/*.json`
  - `runtime/validation/state_fixture_results/*.json`

### current read

- 현재 canonical operating state layer는 representative fixture 기준에서 schema/store/policy/latest 일치가 유지된다.
- `comparison_memory_reason`, `gate_blocker_summary`는 exact equality보다 subset-based drift note가 더 적합하다는 점도 다시 확인됐다.
- experimental namespace leakage는 현재 fixture 결과에서 관찰되지 않았다.
- 현재 공식 판정:
  - reusable attitude는 여러 자산에서 반복되지만
  - 기관은 위 blocker 묶음 때문에 아직 scaffold-bound 상태다
  - 따라서 next loop gate는 계속 닫혀 있다

### current read

- 다음 판단은 더 많은 실험 제안이 아니라, 위 공통 blocker가 실제로 약해졌는가를 보는 방식으로 바뀌어야 한다.
- 지금은 failure를 더 모으는 단계에서 한 번 나아가, gate를 막는 최소 병목 묶음을 운영 기준으로 잠그는 단계다.

## 2K. internal state reorientation addendum

- 이번 턴에서는 recent second-order validation 자산을 실패 목록이 아니라 기억/가능성/생육 기록 자산으로 재배치했다.
- 재선언한 핵심:
  - structure는 meaning lock이 아니라 reinterpretation tolerance의 바닥
  - 1차는 센서값이면서 씨앗 흔적 보존층
  - 2차는 승격 심사기가 아니라 재순환/재독해층
  - hold는 rejection이 아니라 deferred openness
  - weak / fallback / partial은 폐기 대상이 아니라 future comparison memory

### current read

- 지금 recent documents는 “안 된 것 목록”이 아니라, 재료가 어디서 열리고 어디서 조기 고정되는지 보여주는 계절 기록으로 읽어야 한다.
- 현재 엔진은 여전히 열린 숙성 공간으로 유지되어야 하며, blocker와 hold도 그 열린 구조를 보존하기 위한 장치로 다시 읽는다.

---

## 3. delta categories

- [x] structure cleanup
- [ ] folder relocation
- [ ] naming cleanup
- [ ] policy update
- [x] spec update
- [ ] runtime surface addition
- [ ] runtime surface replacement
- [ ] intake flow adjustment
- [ ] registry / provenance adjustment
- [ ] script split / script entrypoint change
- [ ] work isolation
- [ ] deprecation / replacement
- [ ] no-structure-impact local change

### structure impact level
- workspace_wide

---

## 4. recent changed assets

- [folder_role_table_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/folder_role_table_v1.md)
  - role: 폴더 책임표
  - class: spec
  - what changed: `source_assets / docs / runtime / inputs` 실제 역할과 `runtime/logs`, `runtime/tmp`, `inputs/external_cases residue` 구분을 보강
  - impact: workspace_reading_changed

- [repo_delta_log_latest_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/repo_delta_log_latest_v1.md)
  - role: 최근 구조 변화 공식 변화면
  - class: runtime_view
  - what changed: 장기 연혁성 설명을 줄이고 recent bounded repair 중심 latest surface로 압축
  - impact: runtime_priority_changed

- [saltlux_ai.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/saltlux_ai.txt)
  - role: external case canonical input
  - class: input_asset
  - what changed: single-case reality test가 실행되어 source / derived / report / evidence 분리 경로를 실전 검증함
  - impact: intake_reading_changed

- [dual_external_case_validation_saltlux_ai_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/dual_external_case_validation_saltlux_ai_v1.md)
  - role: bounded dual external-case validation report
  - class: report
  - what changed: canonical-vs-summary separation과 cross-case repeated outer frame comparison이 실제 실행 결과로 기록됨
  - impact: workspace_reading_changed

- [same_topic_transformer_classroom_intake_batch_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/same_topic_transformer_classroom_intake_batch_v1.md)
  - role: same-topic external-case intake batch report
  - class: report
  - what changed: transformer classroom topic의 두 txt가 서로 대체되지 않는 독립 canonical input으로 intake되었음
  - impact: intake_reading_changed

- [same_topic_transformer_classroom_comparative_pass_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/same_topic_transformer_classroom_comparative_pass_v1.md)
  - role: same-topic transformer classroom comparative pass report
  - class: report
  - what changed: repeated explanatory outer frame와 case-specific emphasis를 얇게 비교하고 later refinement value를 기록함
  - impact: workspace_reading_changed

- [same_topic_transformer_classroom_bounded_refinement_pass_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/same_topic_transformer_classroom_bounded_refinement_pass_v1.md)
  - role: same-topic transformer classroom bounded refinement report
  - class: report
  - what changed: repeated frame candidate, emphasis split candidate, defer bucket을 승격 없이 더 선명하게 정리함
  - impact: workspace_reading_changed

- [negative_control_file_selection_check_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/negative_control_file_selection_check_v1.md)
  - role: negative control file selection check
  - class: report
  - what changed: `claude_code.txt`와 `graphrag_neosh.txt` 중 negative control 우선 후보를 고르는 기준과 현재 repo 기준 선택 결과를 기록함
  - impact: workspace_reading_changed

- [graphrag_neosh_negative_control_pass_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/graphrag_neosh_negative_control_pass_v1.md)
  - role: graphrag negative control pass report
  - class: report
  - what changed: transformer classroom frame의 false generalization 여부를 확인하기 위해 graphrag 설명 자료를 bounded negative control로 비교함
  - impact: workspace_reading_changed

- [transformer_classroom_local_candidate_lock_note_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/transformer_classroom_local_candidate_lock_note_v1.md)
  - role: local candidate hold lock note
  - class: baseline_note
  - what changed: transformer classroom frame을 `VALID_LOCAL_CANDIDATE`로만 유지하고 broader general technical frame은 `NOT_YET_CONFIRMED`로 잠금
  - impact: workspace_reading_changed

- [interview_style_external_case_batch_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/interview_style_external_case_batch_v1.md)
  - role: interview-style external-case batch report
  - class: report
  - what changed: `dario_amodei_youtube.txt` 와 `andrej_karpathy_youtube.txt`를 새 canonical input으로 안착시키고, 기존 `alexkarp_youtube.txt`와 함께 bounded interview-style batch comparison을 실행함
  - impact: intake_reading_changed

- [interview_style_external_case_raw_intake_gap_analysis_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/interview_style_external_case_raw_intake_gap_analysis_v1.md)
  - role: raw intake vs manual first-pass gap analysis
  - class: report
  - what changed: 인터뷰형 외부자료 3건을 `inputter + labeler` raw probe로 다시 읽어, scene/flow flattening 과 generic anchor noise 가 case-level frame extraction과 얼마나 벌어지는지 비교함
  - impact: workspace_reading_changed

- [raw_intake_gap_analysis_before_middle_layer_fix_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/raw_intake_gap_analysis_before_middle_layer_fix_v1.md)
  - role: three-path comparison report before middle-layer fix
  - class: report
  - what changed: structured document path, external case intake path, engine-only raw intake path 를 같은 비교 프레임으로 정리해 raw flattening 과 missing middle-layer 기능을 기록 기반으로 도출함
  - impact: workspace_reading_changed

- [middle_layer_requirement_before_fix_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/middle_layer_requirement_before_fix_v1.md)
  - role: middle-layer requirement note
  - class: spec
  - what changed: transcript pre-normalization, topic-bearing anchor uplift, case block aggregation, provisional frame sketch, compare-ready packaging 을 middle-layer 요구사항으로 잠금
  - impact: workspace_reading_changed

- [middle_layer_verification_plan_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/middle_layer_verification_plan_v1.md)
  - role: middle-layer verification plan
  - class: report
  - what changed: future middle-layer patch를 raw interview transcript 3건 기준으로 어떻게 검증할지 bounded plan을 정리함
  - impact: workspace_reading_changed

- [middle_layer_thickening_step1_result_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/middle_layer_thickening_step1_result_v1.md)
  - role: middle-layer thickening step result
  - class: report
  - what changed: read-only interview middle-layer probe v0를 실행해 transcript pre-normalization, discourse suppression, case block aggregation, compare-ready packet 생성을 시험했고, signal uplift는 일부 있었지만 frame sketch는 아직 coarse하다고 판정함
  - impact: workspace_reading_changed

- [middle_layer_thickening_step2_result_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/middle_layer_thickening_step2_result_v1.md)
  - role: middle-layer role resolution refinement result
  - class: report
  - what changed: read-only interview middle-layer probe의 Layer 3/4를 refinement해 dominant/secondary/observer-only role mix와 role evidence terms를 분리했고, Dario / Andrej / Alex가 더 compare-meaningful한 packet v1으로 갈라지기 시작함
  - impact: workspace_reading_changed

- [interview_case_renamed_engine_internal_test_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/interview_case_renamed_engine_internal_test_v1.md)
  - role: renamed interview variant internal test result
  - class: report
  - what changed: 인터뷰 3건을 이름 힌트를 줄인 work-side 변형본으로 다시 넣어 raw와 middle-layer를 비교했고, raw는 여전히 `review / compare`로 평평했지만 middle-layer는 case-specific dominant role mix를 유지해 현재 분화가 파일명보다 내용 신호에 더 기대고 있음을 확인함
  - impact: workspace_reading_changed

- [ai_future_segment_probe_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/ai_future_segment_probe_v1.md)
  - role: ai future segment probe result
  - class: report
  - what changed: external cases 전체를 대상으로 엔진의 raw 분절/label 구조에서 `미래 / future / AGI / 초지능 / 자동화` 관련 조각만 추려 보았고, 이 축이 단순 review/compare뿐 아니라 일부 impl/run, evidence/run, spec/fix까지 얇게 퍼진 다층 분포를 가진다는 점을 확인함
  - impact: workspace_reading_changed

- [codex_reusable_internal_hardening_process_directive_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/directives/codex_reusable_internal_hardening_process_directive_v1.md)
  - role: reusable internal hardening process directive
  - class: directive
  - what changed: 외곽 기준면은 잠그고 standard / external / general 문서의 출력 비교와 판단 이유 추출을 통해 내부 refinement를 반복 호출하는 재사용 공고화 패턴을 운영 지시로 고정함
  - impact: workspace_reading_changed

- [codex_future_scaling_guardrails_directive_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/directives/codex_future_scaling_guardrails_directive_v1.md)
  - role: future scaling guardrails directive
  - class: directive
  - what changed: 다음 성장 단계에서 judgment versioning, reasoning residue, PASS_WITH_NOTE/hold discipline, evidence-gated outer-layer governance, failure-axis comparison을 운영 경계선으로 잠가 output abundance만 늘고 판단 기준은 엔진 밖에 남는 drift를 막도록 지시함
  - impact: workspace_reading_changed

- [ontology_vectorfl_layer_probe_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/ontology_vectorfl_layer_probe_v1.md)
  - role: ontology/vectorfl-linked layer probe report
  - class: report
  - what changed: external cases 전체를 대상으로 `객체 / 연결 / 온톨로지 / 벡터플 / 그래프` 계열 분절값을 engine-internal probe로 다시 모아 보았고, 이 축이 review/compare 중심 위에 impl/run, evidence, spec 층을 얇게 겹친 다층 분포를 가진다는 점을 기록함
  - impact: workspace_reading_changed

- [connection_meaning_and_user_layer_translation_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/connection_meaning_and_user_layer_translation_baseline_v1.md)
  - role: connection meaning and user-layer translation baseline
  - class: baseline
  - what changed: 내부 분절/라벨/앵커 refinement를 곧바로 수정 문제로 보지 않고, 먼저 연결의 의미와 사용자 질문의 층위 번역 기준을 통과하게 만드는 상위 기준선을 잠금
  - impact: workspace_reading_changed

- [repeated_learning_asset_exposure_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/repeated_learning_asset_exposure_baseline_v1.md)
  - role: repeated learning asset exposure baseline
  - class: baseline
  - what changed: Codex가 철학과 운용 감각을 한 번에 체득한다고 가정하지 않고, baseline / directive / example / review 자산을 반복 참조시키는 방식으로 학습시켜야 한다는 상위 운영 기준을 잠금
  - impact: workspace_reading_changed

- [vectorfl_engine_job_definition_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/vectorfl_engine_job_definition_v1.md)
  - role: vectorfl engine job definition baseline
  - class: baseline
  - what changed: 엔진의 최상위 직무를 객체 성장 사건 수용, 객체 상태 판독, 관계 운동 생성, 사용자 층위 번역, 기억 바닥 유지로 정의하여, 분절/라벨/요약기보다 더 넓은 공간 운영 엔진으로 읽는 상위 기준을 잠금
  - impact: workspace_reading_changed

- [high_density_dialogue_asset_loop_testing_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/high_density_dialogue_asset_loop_testing_v1.md)
  - role: high-density dialogue asset loop testing baseline
  - class: baseline
  - what changed: 유튜브 대화 스크립트 같은 고밀도 대화 자산을 철학 정답 추출용이 아니라 객체/층위/관계/질문 의도 판독 능력을 반복 검증하는 테스트 자산으로 읽는 기준선을 잠금
  - impact: workspace_reading_changed

- [youtube_03_22_high_density_dialogue_loop_test_report_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/youtube_03_22_high_density_dialogue_loop_test_report_v1.md)
  - role: youtube_03_22 high-density dialogue loop test report
  - class: report
  - what changed: `youtube_03_22.md`를 4개 window/stride 조건의 bash loop로 반복 probe하여 객체 후보, 다층 판독, 관계 힌트, 질문 의도 적합 window, residue 간섭 위치를 확인했고 reusable high-density test asset으로 유효하다고 판정함
  - impact: workspace_reading_changed

- [youtube_03_22_high_density_dialogue_loop_test_review_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/youtube_03_22_high_density_dialogue_loop_test_review_v1.md)
  - role: repeated review report for youtube_03_22 dialogue loop test
  - class: report
  - what changed: 같은 bash loop를 한 번 더 실행해 이전 run과 교차 비교했고, 객체 후보 / 층위 / 관계 힌트 / 질문 의도 적합 window / residue 분포가 거의 동일하게 재현되어 이 자산이 reinforcement-style repeated learning loop에도 안정적이라는 점을 템플릿 기반 리뷰 형식으로 정리함
  - impact: workspace_reading_changed

- [run_dialogue_asset_purpose_synthesis.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_dialogue_asset_purpose_synthesis.py)
  - role: high-density dialogue purpose-reading synthesis helper
  - class: script
  - what changed: 반복 loop 결과를 그대로 나열하는 대신, 고밀도 대화 자산이 어떤 객체 성장 사건과 시대 질문을 품는지 `객체 / 층위 / 관계 / 질문 의도 / residue` 기준으로 다시 읽는 목적 정렬 synthesis layer를 추가함
  - impact: workspace_reading_changed

- [youtube_03_22_engine_purpose_reset_reading_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/youtube_03_22_engine_purpose_reset_reading_v1.md)
  - role: purpose-aligned reading report for youtube_03_22
  - class: report
  - what changed: `youtube_03_22.md`를 단순 분절 테스트 자산이 아니라 `AI 시대를 어떻게 살아갈 것인가`라는 질문 아래 모델 경쟁, agent app 전환, 일의 재배치, 사업 적응이 함께 자라는 객체 성장 자산으로 다시 읽고, 엔진이 이 자산에서 배워야 할 사용자 층위 opening과 relation movement를 별도 report로 정리함
  - impact: workspace_reading_changed

- [input_reading_maturation_and_operating_space_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/input_reading_maturation_and_operating_space_baseline_v1.md)
  - role: input reading / internal maturation operating baseline
  - class: baseline
  - what changed: 엔진 운용을 입력 구조와 내부 숙성 구조로 분리하고, 1차 판독값과 2차 보정값을 나눠 내부 스크립트와 loop로 상위 해석 객체를 길러내는 방향을 Codex 기준으로 잠금
  - impact: workspace_reading_changed

- [question_inducing_block_promotion_and_summary_stage_deprioritization_review_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/question_inducing_block_promotion_and_summary_stage_deprioritization_review_v1.md)
  - role: question-inducing block promotion and summary-stage deprioritization review
  - class: report
  - what changed: `youtube_03_22.md`의 high-density dialogue outputs에서 다음 탐색을 여는 block candidate를 별도 응축핵 후보로 정리하고, residue는 hard suppression 대신 summary-stage 후순위 후보로만 다루는 bounded refinement 방향을 report로 남김
  - impact: workspace_reading_changed

- [run_question_inducing_block_review.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_question_inducing_block_review.py)
  - role: dialogue question-inducing block and deprioritization review helper
  - class: script
  - what changed: 반복 probe outputs를 읽어 question-inducing block candidate와 summary-stage residue deprioritization 후보를 자동으로 정리하는 얇은 review helper를 추가함
  - impact: workspace_reading_changed

- [question_inducing_block_and_summary_priority_shift_declaration_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/declarations/question_inducing_block_and_summary_priority_shift_declaration_v1.md)
  - role: local declaration after question-inducing block review
  - class: declaration
  - what changed: `youtube_03_22.md`의 현재 local reading을 짧게 잠궈, question-inducing block candidate는 실제로 살아났고 residue는 hard suppression이 아니라 summary-stage priority shift로 다루는 것이 맞다는 점만 선언문으로 정리함
  - impact: workspace_reading_changed

- [run_multi_pass_interpretation_training.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_multi_pass_interpretation_training.py)
  - role: multi-pass reinterpretation and context-unit reconstruction helper
  - class: script
  - what changed: 같은 자산을 `object/layer`, `pivot/flow`, `summary/residue` 세 해석 레이어로 다시 읽고, 그 차이를 바탕으로 문단보다 더 살아 있는 context unit candidate를 재구성하는 training helper를 추가함
  - impact: workspace_reading_changed

- [multi_pass_interpretation_and_context_unit_rereading_training_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/multi_pass_interpretation_and_context_unit_rereading_training_v1.md)
  - role: multi-pass interpretation training report
  - class: report
  - what changed: `youtube_03_22.md`를 여러 해석 레이어로 반복 판독했을 때 무엇이 새롭게 보이는지, 어떤 객체가 더 두꺼워지는지, 어떤 context unit이 문단보다 더 살아 있는지, 템플릿이 실제로 읽기 장치로 작동하는지를 학습 보고서로 남김
  - impact: workspace_reading_changed

- [multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/multi_pass_interpretation_and_context_unit_rereading_training_baseline_v1.md)
  - role: multi-pass reinterpretation and context-unit rereading baseline
  - class: baseline
  - what changed: 같은 자산을 여러 해석 레이어로 반복 읽고 그 차이로 문단보다 더 살아 있는 context unit을 다시 세우는 과정을 Codex의 핵심 학습 훈련 기준선으로 잠가, 반복 판독을 단순 요약이 아니라 사용자의 의미 층위 감각 학습으로 유지하도록 정리함
  - impact: workspace_reading_changed

- [run_paragraph_role_interpretation_training.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_paragraph_role_interpretation_training.py)
  - role: actual paragraph role interpretation helper
  - class: script
  - what changed: `youtube_03_22.md`의 실제 단락을 골라 local context / page flow / comparison context 기준으로 역할 판독을 수행하고, 내용 요약이 아니라 `seed / pivot / compression node` 같은 역할 읽기를 report/json으로 남기는 helper를 추가함
  - impact: workspace_reading_changed

- [report_guided_paragraph_interpretation_training_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/report_guided_paragraph_interpretation_training_v1.md)
  - role: actual paragraph role interpretation training report
  - class: report
  - what changed: `Bundle-Unbundle 프레임워크`, `GTC 키노트와 일의 미래`, `RLVR과 CUA` 단락을 실제로 역할 단위로 판독해, 같은 단락이 맥락과 비교축에 따라 question seed / strategy pivot / compression node로 다르게 읽힌다는 점을 실행 결과로 기록함
  - impact: workspace_reading_changed

- [second_order_accumulation_structure_alignment_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/second_order_accumulation_structure_alignment_v1.md)
  - role: second-order accumulation structure alignment note
  - class: report
  - what changed: 현재 2차 보정 스크립트를 더 잘 맞히는 판정기보다 `조건과 맥락을 남기는 축적기`로 재정렬하고, 공통 축적 필드가 왜 필요한지 정리함
  - impact: workspace_reading_changed

- [second_order_comparison_domain_preparation_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/second_order_comparison_domain_preparation_v1.md)
  - role: comparison-domain preparation note for second-order scripts
  - class: report
  - what changed: 비교 도메인 1순위로 `claude_code_index.txt`를 준비 후보로 두고, AI 특화 객체명이 깨져도 2차 판독 태도가 유지되는지 앞으로 무엇을 관찰해야 하는지 정리함
  - impact: workspace_reading_changed

- [repeated_second_order_pattern_table_draft_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/repeated_second_order_pattern_table_draft_v1.md)
  - role: repeated second-order pattern table draft
  - class: spec
  - what changed: object lift 전에 객체명보다 반복 패턴을 먼저 표로 묶는 초안을 만들고, question opening / context unit / role shift 패턴을 hold 상태로 적재하기 시작함
  - impact: workspace_reading_changed

- [domain_specific_vs_reusable_split_note_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/domain_specific_vs_reusable_split_note_v1.md)
  - role: domain-specific vs reusable split note
  - class: report
  - what changed: `business_power_shift`, `orchestration`, `domain_to_component_reframing` 같은 이름은 아직 도메인 특화 쪽에 두고, 그 아래 재사용 가능한 2차 판독 태도와 조건을 분리해 기록함
  - impact: workspace_reading_changed

- [object_lift_candidate_registry_draft_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/object_lift_candidate_registry_draft_v1.md)
  - role: pre-object-lift candidate registry
  - class: report
  - what changed: 상위 객체를 확정하지 않고 hold 상태 후보와 근거, 다음 비교 체크 포인트를 쌓는 대기실 구조를 마련함
  - impact: workspace_reading_changed

- [second_order_operating_surface_definition_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/second_order_operating_surface_definition_v1.md)
  - role: second-order operating surface definition
  - class: report
  - what changed: 앞으로 운용화면이 내부 값 나열이 아니라 `자라는 객체 후보 / question seed / hold 후보 / residue 간섭 / domain split` 같은 숙성 상태를 감독하도록 보여줘야 한다는 표면 정의를 남김
  - impact: workspace_reading_changed

- [user_friendly_label_anchor_surface_refinement_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/user_friendly_label_anchor_surface_refinement_v1.md)
  - role: user-friendly label/anchor bounded refinement report
  - class: report
  - what changed: axis는 그대로 두고 concept probe와 middle-layer probe의 label/anchor output surface에 display label, anchor bucket, user-layer hint, user-facing summary를 추가해 사용자 질문과 가까운 읽기면으로 한 단계 조정함
  - impact: workspace_reading_changed

- [user_facing_gloss_stability_and_residue_review_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/user_facing_gloss_stability_and_residue_review_v1.md)
  - role: user-facing gloss stability and residue review
  - class: report
  - what changed: broad concept probe와 interview packet을 가로로 읽어 user-facing gloss의 안정성을 점검했고, 다음 bounded step은 gloss 증식보다 residue interference reduction 쪽이 더 적절하다는 점을 정리함
  - impact: workspace_reading_changed

- [interview_residue_interference_reduction_review_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/interview_residue_interference_reduction_review_v1.md)
  - role: interview residue interference reduction review
  - class: report
  - what changed: interview류 packet과 concept probe를 기준으로 residue를 `discourse connective / generic abstraction / quasi-topic / observer transition / speaker-source`로 더 세분해 읽고, 다음 step은 suppression 실행이 아니라 summary-stage candidate review라는 점을 정리함
  - impact: workspace_reading_changed

- [interview_summary_stage_deprioritization_candidate_review_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/interview_summary_stage_deprioritization_candidate_review_v1.md)
  - role: interview summary-stage deprioritization candidate review
  - class: report
  - what changed: 예시서를 학습 기준으로 삼아 interview류 다음 step을 hard suppression이 아니라 summary rendering 우선순위 review로 정리하고, Dario / Andrej / Alex별 provisional deprioritization candidate만 남김
  - impact: workspace_reading_changed

---

## 5. reading priority after this delta

### primary current reality
- path: [repo_shared_reality_pack_index_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/repo_shared_reality_pack_index_v1.md)
- reason: shared reality pack 전체를 한 번에 가리키는 공식 첫 진입면

### primary SSOTs
- path: [engine_input_lane_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/engine_input_lane_baseline_v1.md)
- reason: intake lane 및 입력 혼잡 방지 기준

- path: [codex_baseline_program_grade_workspace_upgrade_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md)
- reason: workspace 상위 구조 기준

- path: [folder_role_table_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/folder_role_table_v1.md)
- reason: 폴더 책임과 배치 판단 기준

### primary runtime views
- path: [current_asset_map_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/current_asset_map_v1.md)
- reason: 공식 current reality surface

- path: [repo_delta_log_latest_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/repo_delta_log_latest_v1.md)
- reason: recent bounded repair와 latest 해석 우선순위를 보는 공식 delta surface

### no-longer-primary surfaces
- path: legacy latest / old summary 계열 전반
- why no longer primary: current reality / delta reading을 shared reality pack surfaces가 우선 담당함

---

## 6. must-know after this delta

- 이번 변경은 코어 수정이 아니라 bounded surface repair다
- `folder_role_table_v1.md`는 이제 실제 repo의 `source_assets / docs / runtime/logs / inputs residue` 구분을 더 정확히 반영한다
- `repo_delta_log_latest_v1.md`는 long history가 아니라 recent latest surface로 읽는다
- `saltlux_ai.txt` single-case test는 current_asset_map을 키우지 않고 source / derived / report / receipt / raw log 경계만 검증하는 방식으로 처리됐다
- summary-pair validation에서는 `saltlux_ai.txt`가 canonical로 유지되고 `saltlux_ai_summary.txt`는 secondary로만 남았다
- cross-case comparison에서는 ontology / symbolic grounding / agentic composition이 repeated outer frame으로 더 선명해졌지만 core promotion은 열지 않았다
- same-topic transformer classroom batch에서는 `transformer1`과 `transformer2`를 합치지 않고 각각 독립 source로 intake했으며 current는 그대로 유지했다
- same-topic transformer classroom comparative pass에서는 설명 구조 반복과 각 강의의 encoder/decode 강조 차이를 분리했지만 current를 키우거나 core를 건드리지는 않았다
- same-topic transformer classroom bounded refinement pass에서는 repeated frame / emphasis split / defer bucket을 refinement candidate 수준으로만 정리했고, 승격은 열지 않았다
- negative control 선택 점검에서는 candidate A를 `claude_code.txt`가 아니라 `claude_code_index.txt`로 정정했고, 현재 기준으로는 `graphrag_neosh.txt`를 조금 더 깨끗한 첫 후보로 남겼다
- graphrag negative control pass에서는 transformer classroom의 exact 3단 frame이 그대로 반복되지는 않았고, 더 넓은 기술 설명형 overlap만 부분적으로 남았다
- 그래서 현재 판정은 `VALID_LOCAL_CANDIDATE / NOT_YET_CONFIRMED / HOLD` 조합으로 잠기며, current surface는 확장하지 않는다
- interview-style external-case batch에서는 `dario_amodei_youtube.txt`, `andrej_karpathy_youtube.txt`, `alexkarp_youtube.txt`를 서로 합치지 않고 독립 canonical input으로 유지했으며, 반복되는 것은 interview-style explanatory flow이고 주제 frame 자체는 다르다고 정리했다
- raw intake gap check에서는 같은 3건을 기준 해석 없이 다시 넣었을 때 `review/compare` 쪽으로 평평해지고 generic discourse anchor가 상위를 차지해, 현재 입력기와 case-level frame extraction 사이의 gap이 분명해졌다
- middle-layer fix 전 비교 분석에서는 이 문제가 stopword 하나의 문제가 아니라, `inputter + labeler` 와 case-level frame extraction 사이에 transcript normalization / topic-bearing anchor uplift / case block aggregation / provisional frame sketch 층이 비어 있기 때문이라고 정리했다
- middle-layer thickening step 1에서는 read-only helper로 그 중간층을 외부화해봤고, generic discourse 억제와 packet 생성은 일부 성공했지만 문서별 역할 분화는 아직 부족해 다음 bounded refinement가 필요하다고 남겼다
- middle-layer thickening step 2에서는 role resolution refinement를 통해 Dario는 `mechanism + verification`, Andrej는 `reflection/gap + problem`, Alex는 `problem + control/deployment` 쪽 dominant role mix를 보이기 시작했지만, promotion은 여전히 열지 않았다
- ontology/vectorfl-linked concept probe에서는 `객체 / 연결 / 온톨로지 / 그래프` 축이 단일 철학 층으로만 읽히지 않고, review/compare 중심 위에 impl/run, evidence, spec 층이 얇게 겹친 다층 분포를 보였다
- 앞으로 internal refinement는 engine-internal category 개선만으로 평가하지 않고, 사용자 질문의 의미 층위 번역에 실제로 기여하는지 먼저 기준선으로 확인한다
- label/anchor refinement는 axis refactor 없이도 가능한 초기 표면 조율로 먼저 수행하고, 사전류/백과사전류 투입은 공간 형성 이후의 후행 단계로 둔다
- gloss stability review 결과, broad thematic probe에서는 현재 gloss가 반복 사용 가능한 수준이지만 interview-like case에는 아직 discourse/generic residue 간섭이 커서 사전류 투입은 계속 보류한다
- interview류 residue review 결과, 가장 실제적인 간섭 위치는 anchor extraction보다 user-facing summary 생성 단계이며, 다음 bounded step은 hard suppression이 아니라 summary-stage deprioritization candidate review 쪽이 더 적절하다
- 예시서 학습 이후에도 outer layer나 axis는 건드리지 않고, interview류 다음 단계는 summary-stage 후보 후순위 조정 검토로만 좁혀 간다
- 앞으로 철학/운용 대화는 일회성 설명이 아니라 반복 노출용 build material로 취급하고, baseline / directive / example / review를 다음 턴들에서 계속 재참조한다
- 엔진의 직무는 단순 검색/요약/자동화가 아니라, 객체 성장·관계 누적·사용자 층위 번역·원본/로그 바닥 유지까지 포함하는 공간 운영으로 읽는다
- reusable internal hardening directive에서는 이 흐름을 일회성 tuning이 아니라, 외곽 untouched 확인 -> standard/external/general 3종 비교 -> 판단 이유 추출 -> bounded refinement -> reusable lesson 기록의 반복 패턴으로 잠갔다
- future scaling guardrails directive에서는 이 반복 패턴을 더 확장해 judgment history, reasoning residue, premature generalization 억제, failure-axis comparative reading까지 같이 유지해야 한다는 다음 성장 단계 경계선을 잠갔다
- renamed interview variant internal test에서는 파일명 힌트를 줄여도 raw path는 그대로 flattening 되었고, middle-layer는 여전히 role divergence를 유지해 내부 role resolution이 내용 기반으로 작동하고 있음을 bounded하게 재확인했다
- ai future segment probe에서는 `AI의 미래` 관련 분절값이 단일 전망 서술층에만 머물지 않고 review/compare 중심 위에 impl/run, evidence/run, spec/fix 쪽으로도 얇게 퍼져 있는지 엔진 내부 구조 기준으로 확인했다
- 더 긴 연혁은 [repo_delta_log.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/logs/repo_delta_log.jsonl) 로 내려간다

---

## 7. follow-up actions

- [x] `folder_role_table_v1.md` 현실화 보수 완료
- [x] `repo_delta_log_latest_v1.md` recent 중심 압축 완료
- [x] `saltlux_ai.txt` single-case reality test 실행 완료
- [x] summary-pair validation 실행 완료
- [x] cross-case ontology comparison 실행 완료
- [x] same-topic transformer classroom intake batch 실행 완료
- [x] same-topic transformer classroom comparative pass 실행 완료
- [x] same-topic transformer classroom bounded refinement pass 실행 완료
- [x] negative control file selection check 실행 완료
- [x] graphrag negative control pass 실행 완료
- [x] transformer classroom local candidate hold lock note 기록 완료
- [x] interview-style external-case batch 실행 완료
- [x] interview-style raw intake gap check 실행 완료
- [x] raw intake vs structured vs external three-path comparison 완료
- [x] middle-layer requirement note 작성 완료
- [x] middle-layer verification plan 작성 완료
- [x] middle-layer read-only probe v0 실행 완료
- [x] middle-layer role resolution refinement v1 실행 완료
- [ ] legacy latest / old summary 계열의 `no-longer-primary` 표기 보강 필요
- [ ] `current_asset_map_v1.md` 길이 추가 압축은 후속 bounded repair로 가능

### follow-up notes
- current / delta / shared reality 역할 충돌은 이번 턴 기준 없음
- current read order는 계속 `index -> current_asset_map -> delta_log` 를 유지한다

---

## 8. delta impact summary

- intake 영향:
  - 직접 변경 없음
- runtime 영향:
  - latest delta surface가 recent 중심으로 더 선명해짐
- docs 영향:
  - 폴더 책임표가 현재 repo 현실과 더 정확히 맞춰짐
- script 영향:
  - 직접 변경 없음
- core logic 영향:
  - 없음
- user reading habit 영향:
  - 긴 delta 설명 대신 latest는 recent만 읽고, 긴 연혁은 raw log로 내려가는 습관을 강화

---

## 9. final delta judgment

- structural_cleanup

### judgment note
- 이번 delta는 `STABLE_WITH_MINOR_FIX` 상태를 줄이기 위한 bounded repair이며, core logic이나 상위 기준 철학 변경은 아니다

---

## 10. final lock

이 문서는 단순 변경 사실 나열문이 아니다.  
이 문서는 최근 무엇이 바뀌었고, 그 결과 지금부터 무엇을 기준으로 읽어야 하는가를 압축하는 공식 latest delta surface다.

---

## recent note

- `first_order_second_order_connection_map_v1` 추가
  - 1차 코어 / 1.5차 probe bridge / 2차 숙성 / 운용 표면을 한 장으로 다시 읽었다.
  - 현재 구조는 철학적으로는 `입력 흔적 보존 -> 재독해 -> 숙성` 흐름에 맞지만,
    구현상으로는 아직 `runtime memory direct loop` 보다 `generated sidecar bridge` 의존이 강하다는 점을 명시했다.
  - 또한 2차 일부 기관이 아직 기존 AI dialogue scaffold를 끌고 있다는 점을 구조적 사실로 분리 기록했다.

- current space meaning / second-order asset repositioning / 1.5 bridge role reset
  - 현재 공간을 점/군집 결과면보다 원문-값-연결-재독해를 운영자가 따라가는 운용화면으로 다시 정의했다.
  - recent second-order 자산들을 실패 목록이 아니라 기억 / 가능성 / 생육 기록 자산으로 재배치했다.
  - `run_dialogue_asset_probe.py`를 단순 generated sidecar가 아니라 `re-readable memory packet bridge`의 현재 구현으로 재정의했다.
  - 2차 일부 코드에 남아 있는 AI dialogue scaffold carryover는 기관 미달이 아니라 열린 재독해를 조기 고정시키는 지점으로 기록했다.

- reoriented process validation
  - `youtube_03_22`와 `openai_02_11`를 기준으로 현재 구조가 실제로 `원문 -> 1차 -> 1.5차 -> 2차 -> 상태면` 흐름으로 추적되는지 검증했다.
  - 결과 cluster보다 process console 읽기가 더 정확하다는 점을 다시 확인했다.
  - `run_dialogue_asset_probe.py`가 실제로 rereading 가능한 `memory packet bridge`처럼 기능한다는 점을 자산 비교로 확인했다.
  - 다만 2차 일부 기관은 여전히 prepared scaffold carryover를 보이며, 이 점은 다음 교정의 중심으로 남는다.

- knowledge_editing_youtube process-trace validation
  - `knowledge_editing_youtube.txt`를 현재 process console 기준으로 2차까지 추적했다.
  - source -> 1차 -> 1.5차 packet -> 2차 -> hold/residue/weak/fallback 흐름 자체는 유지됐다.
  - 다만 이 자산은 baseline에서 거의 `1 block / 1 window`로 과압축되어, memory packet bridge는 성립하지만 `overcompressed bridge` 질감을 보였다.
  - 2차는 이 자산에서 열린 재독해보다 prepared scaffold carryover와 empty-ref weak role probe를 더 선명하게 드러냈고, 이 점이 현재 조기 고정 지점의 비교 기억으로 기록됐다.

- gary_tan_brain process-trace validation
  - `gary_tan_brain.txt`도 현재 process console 기준으로 2차까지 추적했다.
  - 이 자산 역시 baseline에선 `1 block / 1 window`로 과압축되지만, `knowledge_editing_youtube`보다 object/layer/relation 밀도가 높고 question-inducing candidate가 `1`건 살아나면서 `overcompressed but breathing` packet 질감을 보였다.
  - 1.5차 memory packet bridge는 여전히 성립했고, 2차는 최소 emergence를 보였지만 context unit / role 계열에선 scaffold carryover와 empty-ref weak probe가 계속 드러났다.

- memory packet texture spectrum
  - 최근 process-trace 자산들을 `잘 읽힘/안 읽힘`이 아니라 packet 질감 언어로 다시 정리했다.
  - `youtube_03_22 = moderately open / dialogue-supportive`
  - `openai_02_11 = structured-open but low-emergence`
  - `knowledge_editing_youtube = overcompressed and closure-heavy`
  - `gary_tan_brain = overcompressed but breathing`
  - 또한 packet 질감 문제와 2차 scaffold carryover 문제를 분리해서 읽는 기준을 공식화했다.

- engine operating surface component spec
  - process console 철학을 바로 UI 컴포넌트 단위로 내렸다.
  - `AssetRail`, `SourceViewer`, `FirstPassTracePanel`, `MemoryPacketBridgePanel`, `SecondOrderRereadingPanel`, `MaturationStatePanel`, `ComparativeMemoryStrip`을 MVP 기준으로 고정했다.
  - 특히 `comparison memory reason`, `packet formation why`, `new opening vs carryover`, `state history / time axis`를 추가해 운용화면이 결과 전시판이 아니라 읽힘의 과정과 막힘의 상태를 추적하는 표면으로 읽히도록 보강했다.

- process console state wiring
  - canonical operating state layer를 process console의 실제 read path에 연결했다.
  - `/process-console`와 `/api/process-console`가 `runtime/views/engine_state_latest/index.json` 및 자산별 latest JSON을 1차 read source로 사용한다.
  - `header badge`, `asset rail`, `state panel`, `compare entry`, `latest state preview`가 canonical state 기반으로 동작하고, filter/sort도 `packet_texture`, `grounding_status`, `emergence_status`, `carryover_risk`, `maturation_state`, `traceability_status` 중심으로 연결됐다.
  - `experimental_namespace`는 기본 숨김 처리되며, latest state가 없을 때는 `state_unavailable / no_canonical_state_yet` fallback으로 표면을 유지한다.
  - representative 4개 자산 기준으로 자산 클릭 시 latest load, badge 6개 표기, compare candidate 생성, experimental hidden-by-default가 모두 확인됐다.

- engine state runtime update bridge
  - runtime evidence를 canonical operating state lifecycle에 연결하는 bridge를 추가했다.
  - runtime 산출물은 latest를 직접 덮어쓰지 않고 `patch proposal -> policy validate -> history append -> latest regenerate` 경로로 들어간다.
  - `runtime/views/engine_state_update_events/`에 asset별 latest update event와 index를 남겨 lightweight provenance surface를 만들었다.
  - representative 4개 자산에 `runtime_evidence` append를 실제로 실행했고, canonical drift 없이 provenance와 evidence refs만 보강된 상태로 latest가 재생성됐다.
  - append 이후 process console은 같은 latest path를 계속 읽으면서 갱신된 `updated_at`과 merged evidence refs를 바로 반영했다.

- process console history drill-down
  - process console 안에서 asset별 history lineage를 drill-down으로 읽을 수 있게 연결했다.
  - authoritative source는 `runtime/state/engine_state_history/<asset_id>.jsonl`이고, `runtime/views/engine_state_update_events/<asset_id>.json`는 helper summary로만 사용한다.
  - state panel에는 `HistorySummaryStrip`, 우측 패널에는 `LatestLineageLink`와 recent timeline이 붙었다.
  - changed fields는 인접 이전 record와 canonical 8필드를 비교해 derived로 계산하고, canonical drift가 없으면 `provenance_only`로 읽는다.
  - representative 4개 자산에서 latest runtime append가 `runtime_evidence / provenance_only`로 읽히는 것이 확인됐고, missing asset도 `state_unavailable / history_unavailable` fallback으로 유지된다.

- state change diff surface
  - process console 안에서 adjacent canonical state pair를 비교하는 diff surface를 추가했다.
  - 기본 단위는 `latest vs previous`, 필요 시 history timeline item에서 `compare to previous`로 adjacent diff를 연다.
  - diff는 canonical 8필드만 직접 비교하고, `comparison_memory_reason`와 `gate_blocker_summary`는 set-like added/removed 방식으로 읽는다.
  - canonical 8필드 변화가 없으면 `provenance_only`로 분리해 얇게 표기하고, 현재 representative latest runtime append는 모두 이 형태로 읽힌다.
  - oldest record에는 `no_previous_state` fallback이 붙고, experimental namespace는 기본 diff 본문에 새지 않도록 유지했다.

- state change interpretation badge + history compaction policy
  - diff/history 위에 derived interpretation badge layer를 추가했다.
  - representative recent update는 `provenance_only + runtime_update` badge로 얇게 읽히며, 이 badge는 canonical truth가 아니라 reading aid로만 동작한다.
  - history는 raw jsonl을 유지한 채 `recent full lineage + older compacted summary` 구조를 갖게 됐다.
  - current thin surface에서는 recent `3`개를 full display로 유지하고, older provenance-heavy 구간은 summary/anchor node로 압축한다.
  - representative 4개 자산에서 recent badge, older compacted node, missing fallback이 모두 확인됐고 raw history 길이는 유지됐다.
