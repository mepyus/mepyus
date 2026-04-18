# space operating organ reading v0

## 1. verdict

현재 공간은 이미 어느 정도 `기관 분화된 공간`으로 읽힌다. 다만 그 분화는 단일 모듈에 깔끔히 잠겨 있기보다, `선언 문서 + runtime surface + ingest/output contract + append-only ledger + adapter script`에 걸쳐 분산되어 있다. 특히 입력, 기록/기억, 표면구성은 강하게 보이고, 흐름해석과 라인번역도 실무적으로는 작동하고 있다. 반면 라인생성기와 라인추출기는 강한 흔적이 있지만 아직 하나의 명시 기관으로 잠기기보다 `distributed organ`으로 읽는 편이 더 정확하다.

또한 현재 저장소는 `line만 있는 공간`이라기보다, `fragment`, `origin/provenance`, `split unit`, `phase decision`, `surface`, `event`, `hint`, `route`, `residue` 같은 복수의 first-class unit이 함께 작동하는 공간으로 보인다. 즉 line은 중요하지만 유일한 중심 단위는 아니다.

아직 분산/중첩/미명시 상태가 남아 있는 곳은 다음이다.

- 입력기와 라인번역기 사이의 경계
- 라인생성기와 라인추출기 사이의 경계
- 흐름해석기와 제동/감독기 사이의 경계
- 라인 중심 서술과 broader unit 중심 서술의 혼용

따라서 지금 단계에서 가장 정확한 표현은, 이 공간이 이미 `기관 분화의 실질은 상당히 진행된 상태`이지만, `기관 registry와 경계 선언은 아직 문서적으로 덜 잠긴 상태`라는 것이다.

## 2. why this reading

이번 읽기는 외부 레퍼런스를 바로 가져오기 위한 것이 아니다. 오히려 외부 레퍼런스를 섣불리 덧씌우지 않기 위해, 현재 저장소 안에서 이미 형성된 역할 기관 후보를 먼저 읽어내고, 그 근거를 명시적으로 모으는 작업이다.

즉 비교의 목적은 모방이 아니라 설명이다. 이미 존재하는 구조를 더 분명하게 말할 수 있어야, 이후 어떤 external host나 reference를 보더라도 우리 공간을 과장 없이 설명할 수 있다.

## 3. boundary reading

현재 공간의 경계는 하나의 파일에만 잠겨 있지 않고, 여러 선언면에서 반복적으로 드러난다.

- 저장소 전체는 `app / scripts / runtime / references`를 함께 포함하는 엔진형 작업공간으로 규정된다. `runtime`은 실행 결과와 현재 읽기면, `references`는 외부 비교/참조 자산, `app`은 코어/워크 구조를 담는 안쪽 층으로 읽힌다. 근거: `vectorfl_status.md`
- 현재 baseline은 `fragment` 중심과 `observer-first`, `measurement retention`, `source/space projection`을 핵심으로 잠그고 있으며, `app/runtime`와 `app/core/runtime`의 경계가 아직 일부 모호하다고 직접 인정한다. 근거: `CURRENT.md`
- 공간의 상위 규정은 `bounded functional space`, `family`, `projection`, `route`, `residue`를 가진 line operating space 쪽으로 정리돼 있다. 근거: `docs/reviews/vectorfl_host_coupled_maturation_strategy_v0.md`, `docs/reviews/bounded_functional_space_instances_v0.md`
- generated/manifest/log 자산은 `ledger / active surface / replayable residue`로 구분되며, append-only 원장과 현재 surface가 명시적으로 분리된다. 근거: `docs/reviews/generated_retention_map_v1.md`
- `current layer`는 빠른 정답 확정층이 아니라 `hold 이유 기록 + re-entry 가능성 보존 + observer-first 운영`을 담당하는 보호 층으로 잠겨 있다. 근거: `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`

현재 경계를 요약하면 다음과 같다.

- 안쪽 핵심: `app/core`, `app/runtime`, `runtime/manifests`, `runtime/events`, `runtime/views`
- 실험/중간 belt: `app/work/*`
- 바깥 참조층: `references/*`
- 보호/직접 수정 금지 성격이 강한 층:
  - append-only ledger (`runtime/events/engine_event_ledger.jsonl`, `runtime/logs/*.jsonl`)
  - baseline contract (`CURRENT.md`, `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`)
  - current control profile (`runtime/current_phase.json`, `runtime/preflight_last_decision.json`)

즉 이 공간의 boundary는 단순 폴더 경계가 아니라 `baseline layer / operating layer / residue layer / reference layer`의 중첩 경계로 드러난다.

## 4. first-class units

현재 공간에서 반복적으로 등장하는 핵심 단위는 다음과 같다.

- `fragment`
  - 현재 baseline에서 가장 명시적으로 잠긴 핵심 단위다. source에서 anchor/provenance를 가진 분절된 재료 단위로 읽힌다.
  - 근거: `CURRENT.md`, `app/fragment/schema.py`
- `anchor`
  - fragment가 어디에 걸려 있는지와 provenance를 유지하는 고정점이다.
  - 근거: `app/fragment/schema.py`
- `provenance / origin map`
  - source와 derived artifact를 연결하는 추적 단위다. 입력 경로와 char-span, heading lineage를 유지한다.
  - 근거: `app/input_layer/source_locator/origin_map_minimum_v1.py`, `scripts/process_structured_doc_with_routing.py`, `docs/reviews/generated_retention_map_v1.md`
- `split unit`
  - ingest 과정에서 입력이 잘린 관찰/분해 단위다.
  - 근거: `app/work/observer_ingest_min/observer_ingest_min_spec.md`, `app/work/observer_ingest_min/contracts/observer_output_contract_v1.md`
- `source manifest`
  - 입력 원본과 ingest 산출을 읽는 요약 manifest다.
  - 근거: `app/work/observer_ingest_min/observer_ingest_min_spec.md`
- `processing trace`
  - 입력 처리 과정과 분기 흔적을 남기는 실행 trace다.
  - 근거: `app/work/observer_ingest_min/observer_ingest_min_spec.md`, `app/work/observer_ingest_min/contracts/observer_output_contract_v1.md`
- `event`
  - append-only ledger에 기록되는 최소 사실 단위다.
  - 근거: `runtime/events/event_schema_v1.md`, `runtime/events/engine_event_ledger.jsonl`, `scripts/record_operation_event.py`
- `ticket`
  - structured doc routing 등에서 문서 파생 작업을 연결하는 work record다.
  - 근거: `scripts/process_structured_doc_with_routing.py`, `runtime/manifests/ticket_registry_v1.json`
- `hint`
  - artifact를 family/projection/route 방향으로 기울게 만드는 초기 bias 단위다.
  - 근거: `app/core/runtime/auto_hint_generation.py`, `runtime/manifests/source_to_family_hints_v0.json`
- `signal_kind`
  - classifier 이전 단계에서 artifact 의미를 다루는 entry vocabulary다.
  - 근거: `docs/reviews/signal_kind_taxonomy_v0.md`, `runtime/manifests/signal_kind_taxonomy_v0.json`
- `family`
  - same-root invariant를 공유하는 line 계보 단위다.
  - 근거: `docs/reviews/upper_family_layer_v0.md`, `docs/reviews/family_invariants_and_routes_v0.md`
- `projection`
  - 같은 family 아래에서 질문/역할이 달라진 line 투영면이다.
  - 근거: `docs/reviews/projection_line_schema_v0.md`, `runtime/manifests/projection_registry_v0.json`
- `route`
  - family/projection이 실제로 어떤 경로로 작동할지 정한 operating path다.
  - 근거: `docs/reviews/route_signature_schema_v0.md`, `runtime/manifests/route_registry_v0.json`
- `line`
  - difference를 중심으로 의미를 연결하고 다음 재독해/행동 기준이 되는 해석 경로다.
  - 근거: `docs/reviews/vectorfl_line_facet_v0.md`, `runtime/manifests/line_registry.json`
- `phase decision`
  - 현재 읽기 frame, active latent lines, next check를 잠그는 control-plane summary 단위다.
  - 근거: `runtime/current_phase.json`, `docs/reviews/generated_retention_map_v1.md`
- `surface`
  - 현재 읽기면 또는 operator-facing 요약면이다.
  - 근거: `runtime/views/operation_board_latest.md`, `runtime/views/engine_state_latest/index.json`, `app/runtime/operating_ui_phase1_adapter.py`
- `residue`
  - 즉시 코어 판정으로 닫지 않고 다음 re-entry를 위해 남기는 잔여 판단/경향 단위다.
  - 근거: `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`, `docs/reviews/residue_backed_reentry_rule_v0.md`
- `trace`
  - 실제 실행 경로와 transition path를 비교 가능하게 남기는 run record다.
  - 근거: `app/core/runtime/execution_trace.py`, `runtime/manifests/execution_trace_log_v0.jsonl`
- `asset / state row`
  - runtime의 현재 대상과 상태 변화 이력을 읽는 단위다.
  - 근거: `runtime/views/engine_state_latest/index.json`, `app/runtime/state_attention_memory.py`

이 목록만 봐도, 현재 공간은 `line only space`라기보다 `input material + routing bias + family/projection/route + state/control surface + residue/trace`가 함께 작동하는 구조임을 알 수 있다.

## 5. actual operating loop

현재 저장소에서 보이는 실제 순환 구조는 대략 아래처럼 읽힌다.

1. 입력/원본이 들어온다.
   - structured doc, external transcript, runtime state surface, engine artifact 등이 진입점이 된다.
   - 근거: `scripts/process_structured_doc_with_routing.py`, `app/work/external_input_preprocess/README.md`, `runtime/views/engine_state_latest/index.json`

2. 입력이 구조화된다.
   - origin map 생성, label packet 부착, observer ingest, split unit/processing trace/readable input board 생성이 이 층에서 일어난다.
   - 근거: `scripts/process_structured_doc_with_routing.py`, `app/input_layer/source_locator/origin_map_minimum_v1.py`, `app/work/observer_ingest_min/observer_ingest_min_spec.md`

3. 재독해/비교/entry bias가 붙는다.
   - auto hint generation, family-rooted alias, signal/classifier, route selection이 이 단계에 해당한다.
   - 근거: `app/core/runtime/auto_hint_generation.py`, `app/core/runtime/classifier_adapter.py`, `docs/reviews/entry_execution_loop_v0.md`, `docs/reviews/prototype_execution_spine_v0.md`

4. 판단/hold/보류가 생긴다.
   - current layer baseline은 mixed hold, observer-only split, promotion 금지, re-entry 가능성을 잠근다.
   - phase decision surface는 active latent lines, decision, next check trigger를 남긴다.
   - 근거: `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`, `runtime/current_phase.json`

5. surface가 구성된다.
   - operation board, engine state latest, operating UI payload, observer readable board 같은 현재 읽기면이 구성된다.
   - 근거: `runtime/views/operation_board_latest.md`, `runtime/views/engine_state_latest/index.json`, `app/runtime/operating_ui_phase1_adapter.py`, `app/work/observer_ingest_min/contracts/observer_output_contract_v1.md`

6. trace / memory / ledger로 남는다.
   - engine event ledger, provenance index, source hints, execution trace, attention memory, line registry/log가 append-only 또는 cumulative 형태로 남는다.
   - 근거: `runtime/events/engine_event_ledger.jsonl`, `docs/reviews/generated_retention_map_v1.md`, `app/core/runtime/execution_trace.py`, `app/runtime/state_attention_memory.py`, `runtime/manifests/line_registry.json`

7. residue-backed re-entry 또는 다음 hop으로 이어진다.
   - current hint, saved hint, residue reentry bias, classifier가 다음 family/projection/route bias를 만든다.
   - 근거: `docs/reviews/prototype_execution_spine_v0.md`, `docs/reviews/residue_backed_reentry_rule_v0.md`, `app/core/runtime/classifier_adapter.py`

즉 현재 저장소는 이미 `입력 -> 구조화 -> 재독해/비교 -> 판단/hold -> surface -> trace/memory -> re-entry`의 순환 구조를 갖고 있다. 다만 이 순환은 하나의 거대한 엔진 파일보다, `script + runtime summary + contract + registry`에 분산되어 나타난다.

## 6. organ-by-organ reading

### 입력기

- status:
  - distributed strong

- role:
  - 바깥 입력을 받아서 최소 provenance와 intake 분류를 붙이고, 구조화 가능한 재료 상태로 넘긴다.

- current evidence:
  - `scripts/process_structured_doc_with_routing.py`
  - `app/input_layer/source_locator/origin_map_minimum_v1.py`
  - `app/work/observer_ingest_min/observer_ingest_min_spec.md`
  - `app/work/external_input_preprocess/README.md`
  - 위 파일들은 입력 수집, marker parse, origin map, observer ingest, preprocess compare를 실제로 보여준다.

- input:
  - structured doc
  - external transcript/raw text
  - runtime surface artifact

- transformation:
  - marker parse
  - origin/provenance map 생성
  - core intake label 부착
  - observer ingest 호출
  - preprocess compare/ambiguity 확인

- output:
  - source manifest
  - split units
  - processing trace
  - label packet
  - routing basis

- trace:
  - origin maps
  - engine event ledger
  - processing trace
  - source manifest

- hold/governance touchpoint:
  - ambiguity가 있으면 direct ingest보다 preprocess/observer 경로로 기울게 한다.
  - 근거: `docs/reviews/route_selection_policy_v0.md`, `app/work/external_input_preprocess/README.md`

- note:
  - 하나의 intake service라기보다 script와 work belt에 분산된 기관이다.

### 라인생성기

- status:
  - distributed strong

- role:
  - 재료, distinction, linkage, direction을 가진 line 후보나 line registry 항목을 형성한다.

- current evidence:
  - `docs/reviews/vectorfl_line_facet_v0.md`
  - `runtime/manifests/line_registry.json`
  - `runtime/current_phase.json`
  - `scripts/process_structured_doc_with_routing.py`
  - line 생성은 facet 문서, registry, active latent lines, reread observation 기록이 함께 보여준다.

- input:
  - fragment/source material
  - reread observation
  - current phase signals
  - bounded space context

- transformation:
  - distinction 형성
  - linkage 정리
  - route/family와 연결 가능한 line 상태로 응축
  - support/caution/weakness 등을 누적

- output:
  - line registry row
  - latent/active line state
  - reread observation 기반 line thickening 흔적

- trace:
  - `runtime/manifests/line_registry.json`
  - `runtime/logs/line_promotion_log.jsonl`
  - `runtime/logs/reread_observation_log.jsonl`

- hold/governance touchpoint:
  - stable closure 미도달, observer-only split, promotion 금지 같은 baseline과 직접 부딪힌다.
  - 근거: `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`

- note:
  - explicit `line generator`라는 단일 모듈은 아직 없고, baseline 문서 + registry + reread record로 분산되어 존재한다.

### 흐름해석기

- status:
  - distributed strong

- role:
  - artifact가 어느 family/projection/route로 들어가야 하는지, 그리고 어떤 순서/전환으로 읽어야 하는지를 해석한다.

- current evidence:
  - `docs/reviews/entry_execution_loop_v0.md`
  - `docs/reviews/prototype_execution_spine_v0.md`
  - `app/core/runtime/classifier_adapter.py`
  - `runtime/current_phase.json`
  - `app/core/runtime/flow_candidate_detection.py`
  - 이 층은 entry spine, classifier, phase surface, repeated transition detection에 분산되어 나타난다.

- input:
  - current hint
  - signal kind
  - previous residue bias
  - phase decision surface
  - execution trace records

- transformation:
  - family/projection/route bias 계산
  - reentry prebias 반영
  - transition path / family handoff / route edge 비교

- output:
  - selected family/projection/route
  - ordered transition path
  - flow candidate weak/medium/strong 판단

- trace:
  - execution trace log
  - current phase summary
  - flow candidate observation report

- hold/governance touchpoint:
  - ambiguity나 mixed hold일 때 빠른 단일 route 확정 대신 observer/reentry 경로로 남긴다.

- note:
  - `flow interpreter`는 실질적으로 존재하지만, phase reader / route selector / flow candidate detector로 나뉜 distributed organ이다.

### 라인추출기

- status:
  - partial candidate

- role:
  - 이미 누적된 trace나 state에서 반복되는 line, route, family handoff, residue tendency를 뽑아내는 쪽으로 읽힌다.

- current evidence:
  - `app/core/runtime/flow_candidate_detection.py`
  - `app/core/runtime/execution_trace.py`
  - `runtime/manifests/execution_trace_log_v0.jsonl`
  - `docs/reviews/flow_candidate_detection_loop_v0.md`
  - 이 기관은 “있다/없다”보다 최근에 가시화되기 시작한 추출 층으로 보인다.

- input:
  - execution trace records
  - family sequence
  - route sequence
  - residue reentry bias

- transformation:
  - repeated pattern grouping
  - support count 계산
  - weak/medium/strong bounded heuristic
  - ambiguity warning 부착

- output:
  - candidate pattern id
  - observed sequence
  - supporting runs
  - strength level

- trace:
  - flow candidate detection output
  - execution trace log

- hold/governance touchpoint:
  - 현재는 full `flow line` 승격을 금지하고 candidate로만 남긴다.
  - 근거: `docs/reviews/flow_candidate_detection_loop_v0.md`

- note:
  - 명시 기관으로 막 잠기기 시작한 단계다. 아직 전체 공간의 상시 기관이라기보다 제한된 실험적 추출기 성격이 강하다.

### 라인번역기

- status:
  - distributed strong

- role:
  - source artifact를 family/projection/route 또는 line-aware bias로 번역해 현재 공간의 operating grammar에 맞게 바꾼다.

- current evidence:
  - `app/core/runtime/auto_hint_generation.py`
  - `app/core/runtime/classifier_adapter.py`
  - `docs/reviews/vectorfl_line_facet_v0.md`
  - `docs/reviews/prototype_execution_spine_v0.md`
  - 이 층은 hint generation, classifier, facet/pipeline 문법에 걸쳐 나타난다.

- input:
  - source artifact fields
  - previous hint
  - residue-backed reentry bias
  - signal kind / alias

- transformation:
  - artifact field bundle -> hint
  - hint -> classifier-ready bias
  - current context -> family/projection/route translation

- output:
  - source-to-family hint
  - selected family/projection/route
  - reentry bias

- trace:
  - `runtime/manifests/source_to_family_hints_v0.json`
  - execution traces
  - current phase decision summaries

- hold/governance touchpoint:
  - direct flattening보다 preservation-first bias, closure-before-presentation 같은 residue rule과 닿는다.
  - 근거: `docs/reviews/residue_backed_reentry_rule_v0.md`

- note:
  - 입력기와 가까워 헷갈리기 쉽다. 입력기는 자료를 받아 정리하고, 번역기는 그 자료를 공간 grammar로 바꾸는 쪽으로 읽는 편이 맞다.

### 기록기억기

- status:
  - explicit strong

- role:
  - 과거 사실, provenance, hint, trace, state attention, line history를 누적 보존하고 다음 읽기에 다시 쓰이게 한다.

- current evidence:
  - `runtime/events/engine_event_ledger.jsonl`
  - `docs/reviews/generated_retention_map_v1.md`
  - `app/runtime/state_attention_memory.py`
  - `runtime/manifests/line_registry.json`
  - `runtime/current_phase.json`
  - `runtime/breadcrumbs.jsonl`
  - append-only ledger와 active profile 유지 규칙이 아주 강하게 보인다.

- input:
  - event rows
  - runtime state history
  - line observations
  - hint save/update
  - phase decisions

- transformation:
  - append-only 저장
  - provenance cluster 유지
  - state diff/attention 패턴 계산
  - history summary/recurring signature 계산

- output:
  - ledger
  - runtime profile
  - attention memory summaries
  - line/history registry

- trace:
  - events/logs/manifests/views 전반

- hold/governance touchpoint:
  - ledger는 rewrite보다 보존 우선, current profile은 broad cleanup 대상이 아님이 명시돼 있다.
  - 근거: `docs/reviews/generated_retention_map_v1.md`

- note:
  - 이 기관은 현재 공간에서 가장 강하게 구현된 축 중 하나다.

### 제동/감독기

- status:
  - distributed strong

- role:
  - 성급한 승격/확정/평탄화를 막고, hold 이유와 observer-only 상태, 다음 check 조건을 잠그는 감독 층이다.

- current evidence:
  - `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`
  - `runtime/current_phase.json`
  - `scripts/process_structured_doc_with_routing.py`
  - `app/core/events/event_append_guard.py`
  - current layer contract와 phase control profile이 강한 감독 근거다.

- input:
  - mixed corridor
  - stable closure 여부
  - reread 결과
  - runtime event append 상황
  - next check trigger

- transformation:
  - mixed/canonical/unreadable 경계 잠금
  - promotion 금지
  - observer-only split 권고
  - hold reason 기록
  - append guard / tail recovery

- output:
  - current phase decision
  - hold corridor 상태
  - governance rules
  - safe append behavior

- trace:
  - current phase
  - preflight last decision
  - event ledger
  - baseline contract

- hold/governance touchpoint:
  - 기관 그 자체가 hold/governance 층이다.

- note:
  - 아직 unified governance surface 하나로 모여 있진 않다. baseline contract, phase profile, append guard, route selection policy가 함께 제동/감독기를 구성한다.

### 표면구성기

- status:
  - distributed strong

- role:
  - 현재 상태와 읽기 결과를 operator-facing surface로 재구성해, 실행면과 읽기면을 이어준다.

- current evidence:
  - `runtime/views/operation_board_latest.md`
  - `runtime/views/engine_state_latest/index.json`
  - `app/runtime/operating_ui_phase1_adapter.py`
  - `app/work/observer_ingest_min/contracts/observer_output_contract_v1.md`
  - `scripts/process_structured_doc_with_routing.py`
  - latest board, engine state, phase1 adapter, observer readable board가 surface construction을 보여준다.

- input:
  - live runtime payload
  - available assets
  - memory stickers/path residue
  - observer ingest outputs
  - per-run routing artifacts

- transformation:
  - payload adaptation
  - summary surface 생성
  - pointer surface 구성
  - multi-lens supervisor surface 요약
  - readable board / operator summary 생성

- output:
  - operation board latest
  - engine state latest
  - phase1 view model
  - readable input board
  - operator summary

- trace:
  - runtime/views/*
  - observer generated outputs
  - receipts / commands pointers

- hold/governance touchpoint:
  - current layer의 mixed/hold 설명이 readable surface 계약으로 들어온다.
  - 근거: `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`

- note:
  - `표면구성기`는 하나의 viewer 컴포넌트라기보다, runtime view writer + UI payload adapter + observer output builder로 분산되어 있다.

## 7. overlaps and confusions

현재 기관 간 경계가 가장 헷갈리는 지점은 다음과 같다.

- 입력기 vs 라인번역기
  - 입력 정리와 family/projection/route bias 형성이 연속으로 붙어 있어 경계가 흐려진다.
- 라인생성기 vs 라인추출기
  - 새로운 line을 형성하는 것과 이미 쌓인 trace에서 line/flow candidate를 뽑는 것이 아직 명확히 분리돼 있지 않다.
- 흐름해석기 vs 제동/감독기
  - 현재 phase를 읽고 다음 route를 잡는 기능과, promotion 금지/hold corridor를 잠그는 기능이 같은 surface에 같이 나타난다.
- line 중심 단위 vs broader unit 중심 단위
  - 문서적으로는 line family가 강조되지만, 실제 runtime에서는 fragment, event, hint, phase, asset, surface가 모두 강한 first-class unit처럼 작동한다.
- 표면구성기 vs 기록기억기
  - 일부 surface는 단순 view라기보다 baseline profile이기도 해서, active surface와 memory/profile의 경계가 겹친다.

즉 현재의 혼란은 “기관이 없음”보다 “기관들이 이미 존재하지만, registry 수준으로 분리 선언되지 않음”에 가깝다.

## 8. consolidation proposal

지금 당장 구현 변경이 아니라 문서적으로 먼저 명시하면 좋은 것은 아래와 같다.

- `boundary declaration`
  - baseline layer / operating layer / ledger layer / active surface / replayable residue / reference layer를 한 장으로 잠글 필요가 있다.
- `first-class unit map`
  - fragment, event, hint, family, projection, route, residue, phase decision, surface, trace가 어떤 위상 차이를 갖는지 문서적으로 정리할 필요가 있다.
- `organ registry`
  - 이번 문서 수준의 판단을 한 단계 더 짧게 잠가, 어떤 기관이 `explicit / distributed / partial / weak`인지 일관되게 보이게 할 필요가 있다.
- `governance surface summary`
  - current layer baseline, current_phase, preflight decision, route selection policy를 묶어 제동/감독기 면을 한 장으로 읽게 할 필요가 있다.
- `intake-to-surface loop summary`
  - structured doc intake, observer ingest, auto hint/classifier, surface writer, ledger append를 한 장으로 요약하면 실제 operating loop가 더 명시적으로 보일 것이다.
- `line vs non-line unit clarification`
  - line을 살리되, line 외 단위들이 이미 first-class로 작동한다는 점을 함께 잠글 필요가 있다.

이 제안들은 새 구조 발명이라기보다, 이미 있는 근거를 더 명시적으로 읽게 만드는 문서 정리 제안이다.

## 9. final judgment

지금 우리 공간은 이미 상당히 기관 분화가 이루어진 상태다. 특히 입력기, 기록기억기, 제동/감독기, 표면구성기는 실질적으로 강하다. 라인번역기와 흐름해석기도 현재 spine과 classifier/reentry 체인에서 분명히 보인다. 라인생성기는 실질은 강하지만 여러 층에 흩어져 있고, 라인추출기는 최근에 명확해지기 시작한 `partial candidate`다.

아직 철학/감각 수준에 더 머무는 것은 “기관들의 경계 선언”과 “line 중심 설명과 broader unit 중심 설명 사이의 균형”이다. 반대로 이미 명시 구조로 잠글 준비가 된 것은 다음이다.

- boundary reading
- first-class unit map
- operating loop summary
- organ-by-organ status map
- governance surface summary

즉 현재 단계의 정확한 진단은, 이 공간이 아직 막연한 철학 공간은 아니며 이미 꽤 작동하는 operating organs를 가진다. 다만 그 기관들이 아직 `한 눈에 보이는 이름표`보다 `분산된 흔적과 계약`으로 존재하므로, 문서적 명시화가 다음 과제라는 것이다.

## appendix. evidence file list

- `CURRENT.md`
- `vectorfl_status.md`
- `docs/reviews/vectorfl_host_coupled_maturation_strategy_v0.md`
- `docs/reviews/vectorfl_line_facet_v0.md`
- `docs/reviews/bounded_functional_space_instances_v0.md`
- `docs/reviews/entry_execution_loop_v0.md`
- `docs/reviews/prototype_execution_spine_v0.md`
- `docs/reviews/generated_retention_map_v1.md`
- `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`
- `app/work/observer_ingest_min/observer_ingest_min_spec.md`
- `app/work/observer_ingest_min/contracts/observer_output_contract_v1.md`
- `app/work/external_input_preprocess/README.md`
- `runtime/views/operation_board_latest.md`
- `runtime/views/engine_state_latest/index.json`
- `runtime/current_phase.json`
- `runtime/events/event_schema_v1.md`
- `runtime/events/engine_event_ledger.jsonl`
- `runtime/manifests/line_registry.json`
- `scripts/process_structured_doc_with_routing.py`
- `scripts/record_operation_event.py`
- `app/input_layer/source_locator/origin_map_minimum_v1.py`
- `app/core/runtime/auto_hint_generation.py`
- `app/core/runtime/classifier_adapter.py`
- `app/core/runtime/execution_trace.py`
- `app/core/runtime/flow_candidate_detection.py`
- `app/runtime/state_attention_memory.py`
- `app/runtime/operating_ui_phase1_adapter.py`
- `app/fragment/schema.py`
