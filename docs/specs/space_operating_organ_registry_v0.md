# Space Operating Organ Registry v0

이 문서는 [space_operating_organ_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/space_operating_organ_reading_v0.md)의 관찰 결과를 짧은 registry 형식으로 압축한 것이다.  
이 registry는 완결 조직표가 아니라, 현재 관찰 기준에서 잠금 가능한 기관 후보의 압축 registry다.  
새 구조를 발명하지 않고, 현재 저장소에서 이미 관찰된 기관 후보만 등록한다.

## 입력기

- status: `distributed strong`
- one-line role: 바깥 입력을 provenance와 intake 분류가 가능한 재료 상태로 받는 기관
- core input: structured doc, external transcript/raw text, runtime artifact
- core output: source manifest, split units, processing trace, label packet, routing basis
- trace: origin map, processing trace, engine event ledger
- governance touchpoint: ambiguity 시 direct ingest보다 preprocess/observer 경로 우선
- note: single module이 아니라 script, input layer, observer belt에 걸친 distributed organ으로 읽는다
- key evidence files:
  - [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
  - [origin_map_minimum_v1.py](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/source_locator/origin_map_minimum_v1.py)
  - [observer_ingest_min_spec.md](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/observer_ingest_min_spec.md)
  - [external_input_preprocess/README.md](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/README.md)

## 라인생성기

- status: `distributed strong`
- one-line role: 재료와 distinction/linkage를 응축해 line 상태와 line registry 항목을 형성하는 기관
- core input: fragment/source material, reread observation, phase signal, bounded space context
- core output: line registry row, latent/active line state, reread-based line thickening 흔적
- trace: line registry, reread observation log, line promotion log
- governance touchpoint: stable closure 미도달, observer-only split, promotion 금지와 직접 연결
- note: line generation은 단일 generator보다 registry, phase surface, reread observation에 분산된 distributed organ으로 읽는다
- key evidence files:
  - [vectorfl_line_facet_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/vectorfl_line_facet_v0.md)
  - [line_registry.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/line_registry.json)
  - [current_phase.json](/Users/sungsookim/universe/vectorfl_replica/runtime/current_phase.json)
  - [current_layer_baseline_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/current_layer_baseline_contract_v1.md)

## 흐름해석기

- status: `distributed strong`
- one-line role: artifact가 어떤 family/projection/route 순서로 읽혀야 하는지 해석하는 기관
- core input: current hint, signal kind, previous residue bias, phase decision, execution trace
- core output: selected family/projection/route, ordered transition path, flow candidate observation
- trace: execution trace log, phase summary, flow candidate observation surface
- governance touchpoint: mixed/ambiguous 상태를 빠른 단일 route 확정보다 observer/reentry 경로로 남김
- note: classifier, phase summary, trace reading에 걸쳐 나타나는 distributed organ이다
- key evidence files:
  - [entry_execution_loop_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/entry_execution_loop_v0.md)
  - [prototype_execution_spine_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/prototype_execution_spine_v0.md)
  - [classifier_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/classifier_adapter.py)
  - [flow_candidate_detection.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/flow_candidate_detection.py)

## 라인추출기

- status: `partial candidate`
- one-line role: 누적 trace에서 반복 pattern과 candidate sequence를 뽑아내는 기관 후보
- core input: execution trace record, family sequence, route sequence, residue bias
- core output: candidate pattern id, observed sequence, supporting runs, strength level
- trace: flow candidate detection result, execution trace log
- governance touchpoint: formal flow line 승격 전 단계에서 candidate로만 유지
- key evidence files:
  - [flow_candidate_detection.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/flow_candidate_detection.py)
  - [execution_trace.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/execution_trace.py)
  - [flow_candidate_detection_loop_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/flow_candidate_detection_loop_v0.md)

## 라인번역기

- status: `distributed strong`
- one-line role: source artifact를 family/projection/route bias로 번역해 현재 공간 grammar에 올리는 기관
- core input: source artifact fields, previous hint, residue-backed reentry bias, signal/alias
- core output: source-to-family hint, classifier-ready bias, selected family/projection/route
- trace: source hint manifest, execution trace, phase decision
- governance touchpoint: preservation-first, closure-before-presentation 같은 residue rule과 접속
- note: input organ과 인접하지만, single translator보다 hint/classifier/reentry 쪽에 분산된 distributed organ으로 읽는다
- key evidence files:
  - [auto_hint_generation.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/auto_hint_generation.py)
  - [classifier_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/classifier_adapter.py)
  - [prototype_execution_spine_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/prototype_execution_spine_v0.md)
  - [source_to_family_hints_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/source_to_family_hints_v0.json)

## 기록기억기

- status: `explicit strong`
- one-line role: event/provenance/hint/phase/trace/line history를 누적 보존하고 다음 읽기에 다시 연결하는 기관
- core input: event row, runtime state history, line observation, hint save/update, phase decision
- core output: ledger, runtime profile, attention memory summary, line/history registry
- trace: events, logs, manifests, views 전반
- governance touchpoint: ledger 보존 우선, current profile 보호, broad cleanup 제외
- note: explicit strong의 이유는 append-only ledger, history retention, runtime profile 보존면이 반복적으로 잠겨 있기 때문이다
- key evidence files:
  - [engine_event_ledger.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/events/engine_event_ledger.jsonl)
  - [generated_retention_map_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/generated_retention_map_v1.md)
  - [state_attention_memory.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/state_attention_memory.py)
  - [line_registry.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/line_registry.json)

## 제동/감독기

- status: `distributed strong`
- one-line role: 성급한 승격/확정/평탄화를 막고 hold 이유와 다음 check 조건을 잠그는 감독 기관
- core input: mixed corridor 상태, stable closure 여부, reread 결과, runtime append 상황, next check trigger
- core output: current phase decision, hold corridor 상태, governance rule, append-safe 기록
- trace: current phase, preflight decision, baseline contract, event ledger
- governance touchpoint: mixed hold 보호, observer-only 유지, promotion 금지, append guard
- note: 이 축의 분산 stop points 요약은 [governance_surface_summary_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/governance_surface_summary_v0.md)에서 같이 읽는다
- key evidence files:
  - [current_layer_baseline_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/current_layer_baseline_contract_v1.md)
  - [current_phase.json](/Users/sungsookim/universe/vectorfl_replica/runtime/current_phase.json)
  - [preflight_last_decision.json](/Users/sungsookim/universe/vectorfl_replica/runtime/preflight_last_decision.json)
  - [event_append_guard.py](/Users/sungsookim/universe/vectorfl_replica/app/core/events/event_append_guard.py)

## 표면구성기

- status: `distributed strong`
- one-line role: 현재 상태와 읽기 결과를 operator-facing surface로 요약/적응시키는 기관
- core input: live runtime payload, available assets, memory stickers/path residue, observer outputs, per-run artifacts
- core output: operation board, engine state latest, phase1 view model, readable input board, operator summary
- trace: runtime/views, observer generated outputs, receipt/command pointer surfaces
- governance touchpoint: mixed/hold 설명을 readable surface 계약에 반영
- note: 이 기관이 구성하는 면은 boundary 문서의 `현재 읽기면(current-reading surface)`과 직접 이어진다
- key evidence files:
  - [operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
  - [engine_state_latest/index.json](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_state_latest/index.json)
  - [operating_ui_phase1_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1_adapter.py)
  - [observer_output_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/contracts/observer_output_contract_v1.md)
