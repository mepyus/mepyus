# space operating organ applied validation v0

## 1. verdict

기관 언어는 실제 사례 읽기에 대체로 유효하다. 특히 `입력기`, `기록기억기`, `제동/감독기`, `표면구성기`, `라인번역기`는 최근 작업 흐름을 더 선명하게 읽게 해준다. 반면 `라인생성기`와 `라인추출기`는 사례에 따라 중심성이 크게 달라지고, 모든 사례에 강하게 적용하면 과해진다.

가장 잘 맞는 경우는 `입력 -> 구조화 -> current-reading surface -> trace/ledger`가 분명한 사례와 `phase/reentry`처럼 bias와 stop point가 분명한 사례다. 가장 조심해야 할 경우는 line보다 `artifact / event / hint / phase / surface`가 더 강한 사례를 line 중심으로 과장해 읽는 것이다.

## 2. why this validation

이번 검증은 구현 테스트가 아니라 운용 검증이다.  
즉 기관 spec들이 실제 사례를 더 잘 설명하는지, 아니면 문서 안에서만 그럴듯한지 확인하는 단계다.

따라서 질문은 “코드가 돌아가나?”보다, “현재 spec의 기관 언어가 실제 흐름의 진입점, 번역, 보류, surface, trace를 더 선명하게 읽게 해주는가?”에 있다.

## 3. selected cases

- `structured doc routing / saltlux-goover reference ingest`
  - 입력 -> 구조화 -> surface -> trace가 가장 선명하게 보이는 사례라서 선택했다.
- `transition thickening / current_phase + preflight`
  - hold, next_check, closure 미도달, observer-first 성격이 governance와 함께 가장 잘 드러나는 사례라서 선택했다.
- `transition -> readout reentry chain`
  - family/projection/route bias, residue-backed reentry, classifier override가 함께 보여서 흐름해석기와 라인번역기 언어가 실제로 버티는지 확인하기 좋았다.

## 4. case-by-case reading

### case 1. structured doc routing / saltlux-goover reference ingest

#### 4-1. case summary

`tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md`가 `scripts/process_structured_doc_with_routing.py`를 통해 들어와 marker normalize, doc registration, label packet 생성, observer ingest, origin map 생성, receipt 작성, operation board surface 업데이트까지 이어진 사례다. 이 사례에서는 line보다 `doc / label / split unit / processing trace / receipt / board`가 더 중심에 서 있다.

#### 4-2. organ mapping

- 입력기:
  - fit level: strong
  - why: raw doc, routing marker, intake label, observer ingest 진입이 매우 선명하다. 근거: [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py), [operation_receipt](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts/doc_tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1_operation_receipt.md)
- 라인생성기:
  - fit level: weak
  - why: 이 사례의 중심은 line 형성보다 doc registration과 ingest output 생성이다. multi-lens output이 생기긴 하지만 line registry나 active line 형성이 전면에 서 있지는 않다.
- 흐름해석기:
  - fit level: usable
  - why: `reference / ingest_only / normal` routing normalization은 흐름 판단에 가깝지만, family/projection/route 수준의 해석기보다는 routing shell에 가깝다.
- 라인추출기:
  - fit level: forced
  - why: 이 사례에서 반복 pattern 추출이나 candidate line extraction은 거의 보이지 않는다.
- 라인번역기:
  - fit level: usable
  - why: raw doc를 `structured_internal_doc`, `minimal_preprocess`, `reference`, `execution_linkable=false`로 바꾸는 번역이 분명히 있다. 다만 line grammar보다 intake/routing grammar가 더 중심이다.
- 기록기억기:
  - fit level: strong
  - why: events, receipt, origin map, command pointer, board, label packet이 append/cumulative 형태로 남는다.
- 제동/감독기:
  - fit level: usable
  - why: `RUNMODE=ingest_only`, `ticket not created`, `execution_linkable=false`가 일종의 경계/제동 역할을 한다. 다만 mixed hold 같은 강한 governance 사례는 아니다.
- 표면구성기:
  - fit level: strong
  - why: operation board, receipt, commands pointer, observer readable outputs, multi-lens surfaces가 모두 current-reading surface를 만든다.

#### 4-3. line vs non-line balance

이 사례의 실제 중심 단위는 line보다 `doc / label packet / split unit / processing trace / receipt / board` 쪽이다.  
line 중심 설명은 일부만 유효하고, 전체를 설명하기엔 non-line 단위가 더 강하다.

#### 4-4. governance reading

- `ingest_only` runmode가 실행 범위를 제한한다.
- `ticket not created`와 `execution_linkable=false`가 작업 확장을 막는다.
- event 기록은 append-only로 남고, receipt/board는 pointer surface로 정리된다.

즉 이 사례의 governance는 mixed hold보다는 `경계 잠금 + append-only 기록 보호` 쪽으로 보인다.

#### 4-5. what became clearer

- 입력기와 표면구성기가 실제로 강하다는 점
- 기록기억기가 receipt/event/origin map 층에서 매우 선명하다는 점
- line 언어 없이도 organ 언어가 구조 흐름을 꽤 잘 설명한다는 점

#### 4-6. what remained blurry

- 라인생성기와 라인번역기의 경계
- routing normalization을 흐름해석기로 볼지 입력기 내부 판단으로 볼지
- line 중심 설명의 적용 범위

### case 2. transition thickening / current_phase + preflight

#### 4-1. case summary

`runtime/current_phase.json`, `runtime/preflight_last_decision.json`, `runtime/manifests/phase_decision_log.jsonl`이 함께 `active_latent_lines`, `decision=thickening`, `next_check_trigger`, `closure-ready 아님`을 보여주는 사례다. 이 사례는 실제로 `fam_transition_thickening -> proj_transition_preflight_reread -> route_preflight_reread` spine을 여는 데모이면서, mixed hold와 governance가 가장 직접적으로 읽힌다.

#### 4-2. organ mapping

- 입력기:
  - fit level: usable
  - why: 진입점은 raw doc가 아니라 phase surface다. 입력기는 존재하지만, 이미 구조화된 current-reading surface를 받는 쪽에 가깝다.
- 라인생성기:
  - fit level: usable
  - why: `active_latent_lines`와 `thickening`은 line 상태를 분명히 보여주지만, 이 사례에서 주역은 새 line 생성보다 기존 line의 상태 유지/재독해다.
- 흐름해석기:
  - fit level: strong
  - why: signal, family, projection, route, next decision point가 가장 선명하게 붙는다. 근거: [loop_demo_case_transition_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/loop_demo_case_transition_v0.md)
- 라인추출기:
  - fit level: weak
  - why: 반복 sequence 추출보다는 same-family reread와 unresolved edge residue 유지가 중심이다.
- 라인번역기:
  - fit level: strong
  - why: phase artifact를 `transition_blockage -> fam_transition_thickening -> proj_transition_preflight_reread -> route_preflight_reread`로 바꾸는 번역이 분명하다.
- 기록기억기:
  - fit level: strong
  - why: current phase, preflight decision, phase decision log, breadcrumbs가 모두 누적/보존된다.
- 제동/감독기:
  - fit level: strong
  - why: `closure-ready 아님`, `remain in thickening`, `next_check_trigger`, `promotion 금지`가 이 사례의 핵심이다.
- 표면구성기:
  - fit level: usable
  - why: current_phase와 preflight는 current-reading surface 역할을 하지만, board-style readout보다 control profile 성격이 더 강하다.

#### 4-3. line vs non-line balance

이 사례는 line 중심 설명이 유효하다. 다만 실제 중심 단위는 `line 단독`보다 `phase / signal / active_latent_lines / next_check_trigger / residue`가 함께 묶인 상태다.  
즉 line은 강하지만, phase와 residue 같은 non-line unit도 동등하게 중요하다.

#### 4-4. governance reading

- `decision=thickening` 자체가 멈춤을 선언한다.
- `closure-ready 아님`이 canonical/promotion을 막는다.
- `next_check_trigger`가 다음 re-read 조건을 잠근다.
- baseline contract의 `mixed hold`, `observer-only`, `promotion 금지`가 이 사례 해석의 배경 규칙으로 깔려 있다.

#### 4-5. what became clearer

- 흐름해석기와 제동/감독기가 실제로 강하게 보이는 사례라는 점
- current_phase/preflight가 current-reading surface이자 governance surface라는 점
- line 중심 언어가 이 사례에서는 유효하다는 점

#### 4-6. what remained blurry

- 흐름해석기와 제동/감독기의 경계
- 라인생성기와 기존 latent line 재사용의 경계
- current-reading surface와 governance surface의 중첩

### case 3. transition -> readout reentry chain

#### 4-1. case summary

`runtime/views/engine_state_latest/index.json`을 새 artifact로 받고, 이전 artifact로 `runtime/current_phase.json` 또는 `runtime/preflight_last_decision.json`을 둔 뒤, `transition_condition_to_operator_readability` question shift를 걸었을 때, source hint는 `fam_operator_readout`을 가리키지만 residue-backed reentry가 `fam_transition_thickening`를 먼저 세우고 classifier가 `cls_rule_transition_readout_override`를 고르는 사례다. 이 사례는 broad readout이 들어와도 transition explanation first가 유지되는지를 보여준다.

#### 4-2. organ mapping

- 입력기:
  - fit level: usable
  - why: 진입점은 `engine_state_latest/index.json`이라는 current-reading surface다. 이미 구조화된 surface를 받기 때문에 raw intake 강도는 낮다.
- 라인생성기:
  - fit level: weak
  - why: 새 line 생성보다 existing family/projection/route override와 reentry bias가 중심이다.
- 흐름해석기:
  - fit level: strong
  - why: current hint, reentry prebias, classifier override, final selection이 모두 실제로 보인다. 근거: [full_entry_reentry_chain_execution_check_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/full_entry_reentry_chain_execution_check_v0.md), [execution_trace_log_v0.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/execution_trace_log_v0.jsonl)
- 라인추출기:
  - fit level: usable
  - why: 이 사례 단독으로는 약하지만, execution trace에 ordered transition path와 family sequence가 남아 later extraction의 재료가 된다.
- 라인번역기:
  - fit level: strong
  - why: broad board hint를 `transition-family explanation first`로 재번역하는 residue-backed reentry가 핵심이다.
- 기록기억기:
  - fit level: strong
  - why: current hint, previous hint, reentry_prebias, classifier rule, ordered transition path, residue notes가 모두 execution trace로 남는다.
- 제동/감독기:
  - fit level: strong
  - why: 새 artifact가 broad readout을 제안해도, `closure_before_presentation` residue rule이 direct presentation을 제동한다.
- 표면구성기:
  - fit level: usable
  - why: source artifact가 engine_state board surface이므로 표면구성기의 결과물을 다시 읽는 사례다. 다만 이 사례의 중심은 surface 생성보다 surface override 해석이다.

#### 4-3. line vs non-line balance

이 사례는 line 중심 설명이 꽤 유효하지만, 실제 중심 단위는 `hint / residue bias / question_shift / classifier rule / execution trace`다.  
즉 line 그 자체보다 `line-aware operating grammar`가 더 중심이다.

#### 4-4. governance reading

- broad readout hint가 바로 final selection이 되지 않는다.
- residue rule `closure_before_presentation`이 explanation-first를 강제한다.
- classifier는 source hint보다 reentry prebias를 우선한다.
- execution trace는 append-only로 남아 later extraction 재료가 된다.

#### 4-5. what became clearer

- 라인번역기와 흐름해석기의 차이가 이 사례에서 가장 잘 드러난다
- 제동/감독기는 baseline contract뿐 아니라 residue rule/classifier override에도 분산돼 있다는 점
- current-reading surface와 governance surface가 실제로 충돌/교섭할 수 있다는 점

#### 4-6. what remained blurry

- 라인추출기를 이 사례에 어디까지 적용할지
- 흐름해석기와 라인번역기의 경계
- 표면구성기의 역할이 source surface 생성에만 있는지, 이후 override 해석까지 포함되는지

## 5. cross-case findings

- 반복적으로 강하게 맞는 기관
  - 입력기: raw doc나 artifact 진입에서 consistently 유효하다
  - 라인번역기: hint/classifier/reentry가 있는 사례에서 매우 유효하다
  - 기록기억기: 거의 모든 사례에서 가장 안정적으로 보인다
  - 제동/감독기: mixed hold, next_check, reentry rule, append guard처럼 분산 stop points로 계속 드러난다
  - 표면구성기: output board, receipt, current_phase, engine_state 같은 current-reading surface에서 반복적으로 유효하다

- 반복적으로 약하거나 억지인 기관
  - 라인추출기: later comparison 재료로는 분명하지만, 각 사례 단독 설명에서는 종종 weak 또는 forced다
  - 라인생성기: 기존 line 상태를 읽는 사례에서는 strong보다 usable/weak로 머무는 경우가 많다

- 특히 헷갈린 경계
  - 입력기 vs 라인번역기
    - raw 입력 정리와 operating grammar 변환이 연속으로 이어져 경계가 흔들린다
  - 라인생성기 vs 라인추출기
    - line을 형성하는 것과 trace에서 pattern을 뽑는 것이 사례별로 분리되지 않는다
  - 흐름해석기 vs 제동/감독기
    - route/family를 읽는 것과 멈춤을 거는 것이 current_phase, classifier override, residue rule에서 겹친다

- current-reading surface와 governance surface의 맞물림
  - current_phase, preflight, engine_state board는 단순 readout이 아니라 governance와 이어진 현재면이다
  - 즉 surface는 “보여주는 면”이면서 동시에 “멈춤과 다음 hop을 잠그는 면”이기도 하다

## 6. keep / adjust / hold

- keep:
  - 입력기
  - 라인번역기
  - 기록기억기
  - 제동/감독기
  - 표면구성기
  - 이 다섯은 현재 기관 언어로 계속 써도 실제 사례 설명력이 높다

- adjust:
  - 라인생성기
  - 흐름해석기
  - 이 둘은 유효하지만, 사례에 따라 line 자체보다 phase/hint/residue/trace가 더 중심일 수 있음을 같이 적어야 한다

- hold:
  - 라인추출기
  - 아직은 `partial candidate` 이상의 강한 기관처럼 쓰지 않는 편이 맞다

## 7. final judgment

지금 기관 언어는 실제 운용 설명에 `부분적으로가 아니라 꽤 실질적으로` 유효하다. 다만 모든 사례를 line 중심으로만 읽으려 하면 어색해지고, 특히 structured-doc intake처럼 non-line unit이 중심인 사례에서는 organ language를 `line-centered`보다 `space-operating` 쪽으로 읽어야 더 맞다.

다음 단계로 가장 맞는 것은 추가 설계가 아니라 `더 많은 사례 검증`이다. 특히 line생성기와 라인추출기가 정말 독립 기관으로 버티는지, 아니면 계속 distributed/partial로 두는 편이 맞는지 더 많은 실제 흐름에서 확인하는 단계가 자연스럽다.

## appendix. evidence files

- [space_operating_organ_registry_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/space_operating_organ_registry_v0.md)
- [space_boundary_declaration_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/space_boundary_declaration_v0.md)
- [governance_surface_summary_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/governance_surface_summary_v0.md)
- [space_operating_organ_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/space_operating_organ_reading_v0.md)
- [space_spec_consistency_audit_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/space_spec_consistency_audit_v0.md)
- [space_spec_wording_alignment_closeout_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/space_spec_wording_alignment_closeout_v0.md)
- [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
- [doc_tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1_operation_receipt.md](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts/doc_tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1_operation_receipt.md)
- [operation_board_run_20260403_184903_920534_18de5b4f_1ea134.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_run_20260403_184903_920534_18de5b4f_1ea134.md)
- [structured_doc_routing_commands_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/commands/structured_doc_routing_commands_v1.md)
- [loop_demo_case_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/loop_demo_case_v0.md)
- [loop_demo_case_transition_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/loop_demo_case_transition_v0.md)
- [loop_demo_case_readout_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/loop_demo_case_readout_v0.md)
- [full_entry_reentry_chain_execution_check_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/full_entry_reentry_chain_execution_check_v0.md)
- [execution_trace_log_v0.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/execution_trace_log_v0.jsonl)
- [current_phase.json](/Users/sungsookim/universe/vectorfl_replica/runtime/current_phase.json)
- [preflight_last_decision.json](/Users/sungsookim/universe/vectorfl_replica/runtime/preflight_last_decision.json)
- [engine_state_latest/index.json](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_state_latest/index.json)
