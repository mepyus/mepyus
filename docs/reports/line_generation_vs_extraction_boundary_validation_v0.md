# line generation vs extraction boundary validation v0

## 1. verdict

현재 저장소에서 `line generation`과 `line extraction`은 완전히 다른 기관으로 깔끔히 분리되기보다, 일부는 겹치고 일부는 강도가 다르다. 가장 정확한 판정은 이렇다. `line generation`은 독립 단일 모듈은 아니지만, latent line 유지, thickening, line registry, family/projection/route 형성 쪽에서 실질 기관으로 계속 유지 가능하다. 반면 `line extraction`은 아직 retrospective grouping과 candidate observation에 가까워서 `partial candidate`로 두는 편이 맞다.

즉 둘의 관계는 `생성 vs 추출`의 완전 분리라기보다, `현재면에서 line/state를 형성·유지·두껍게 하는 축`과 `사후 trace를 묶어 candidate pattern으로 읽는 축`의 분화 초기 단계로 보는 것이 가장 정확하다.

## 2. why this validation

직전 applied validation에서 가장 흔들린 기관이 `라인생성기`와 `라인추출기`였다. 많은 사례에서 line generation은 새 형성보다 thickening/reuse/carry에 가까웠고, line extraction은 실제 추출이라기보다 later comparison을 위한 trace grouping에 더 가까웠다.

그래서 이번 검증은 기관 전체를 다시 넓게 보는 대신, 이 둘만 좁고 깊게 봐서 현재 registry 표현을 계속 유지할 수 있는지, 혹은 강도를 더 낮춰야 하는지 판정하려는 것이다.

## 3. selected cases

- `transition thickening / current_phase`
  - line/state thickening과 latent line 유지가 직접 보이는 사례라서 선택했다.
- `flow candidate detection / execution trace grouping`
  - execution trace, candidate detection, pattern grouping이 가장 명시적으로 보이는 사례라서 선택했다.
- `structured doc routing / saltlux-goover reference ingest`
  - line보다 non-line 단위가 더 중심인 사례로, generation/extraction 기관 언어를 어디서 멈춰야 하는지 보기 위해 선택했다.

## 4. case-by-case reading

### case 1. transition thickening / current_phase

#### 4-1. case summary

`runtime/current_phase.json`은 `phase=thickening`, `active_latent_lines=[pre_read_eye, raw_return_preservation]`, `decision_reason=... not closure-ready`, `next_check_trigger`를 보여준다. 이 사례는 새 line을 크게 발명한다기보다, 기존 latent line을 유지하고 현재 thickening 상태를 current-reading surface에 잠그는 쪽이 강하다.

#### 4-2. line generation reading

- fit level: usable
- what counts as generation here
  - active latent line을 현재 phase surface에서 `살아 있는 line/state`로 유지하고, thickening 상태를 현재면에 명시하는 것
- 무엇이 새 형성이고 무엇이 thickening/reuse인지
  - `pre_read_eye`, `raw_return_preservation` 자체는 이미 있던 latent line이다
  - 여기서 보이는 것은 새 line 생성보다 `existing line carry + thickening + current-state articulation`이다

#### 4-3. line extraction reading

- fit level: weak
- what counts as extraction here
  - 이 사례에서는 extraction이라고 부를 만한 독립 grouping은 거의 없다
- 실제 추출인지, future-readable residue인지
  - current_phase는 later comparison을 가능하게 하는 profile을 남기지만, 그 자체는 추출보다 `future-readable control profile`에 가깝다

#### 4-4. generation vs extraction boundary

- 입력 차이
  - generation 쪽 입력: latent lines, phase signals, reread state
  - extraction 쪽 입력: 이 사례에서는 거의 없음
- 출력 차이
  - generation 쪽 출력: active latent lines, thickening status, next check trigger
  - extraction 쪽 출력: 없음에 가깝고, 있어도 나중에 비교 가능한 residue/profile 수준
- timing 차이
  - generation은 current-reading surface에서 즉시 보인다
  - extraction은 이 사례 자체에는 아직 없다
- surface 차이
  - generation은 `current_phase.json`에서 직접 보인다
  - extraction은 retrospective surface가 필요하다
- 겹침/혼동 지점
  - phase profile을 “새 line 생성”으로 과장하기 쉽다

#### 4-5. governance involvement

- `closure-ready 미도달`이 generation 쪽에 강하게 개입한다
- `next_check_trigger`가 same-line reread를 요구한다
- `promotion 금지`, `mixed hold`, `observer-only`는 새로운 line 승격보다 current thickening 유지에 더 강하게 작동한다

#### 4-6. final note for this case

이 사례는 extraction보다 generation 쪽에 더 가깝다. 다만 generation도 “새 형성”보다 “thickening/reuse/carry”로 읽는 것이 정확하다.

### case 2. flow candidate detection / execution trace grouping

#### 4-1. case summary

`execution_trace_log_v0.jsonl`에 남은 run traces를 [flow_candidate_detection.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/flow_candidate_detection.py)가 읽고, stage sequence, family handoff, route edge, reentry hook, residue-to-next-family tendency를 반복 패턴으로 묶어 `weak / medium / strong` heuristic을 부여한다. [flow_candidate_first_observation_report_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/flow_candidate_first_observation_report_v0.md)는 이 결과를 promotable flow line이 아니라 bounded candidate evidence로만 남긴다.

#### 4-2. line generation reading

- fit level: weak
- what counts as generation here
  - 이 사례에서 generation이라고 부를 수 있는 것은 사실상 거의 없다
- 무엇이 새 형성이고 무엇이 thickening/reuse인지
  - detector는 새 line을 만들지 않고, 이미 남은 trace를 grouping한다
  - 따라서 generation을 말한다면 과장에 가깝다

#### 4-3. line extraction reading

- fit level: usable
- what counts as extraction here
  - repeated stage sequence
  - repeated family handoff
  - repeated reentry hook
  - repeated residue-to-next-family tendency
  - 를 trace에서 끌어내 candidate pattern으로 묶는 것
- 실제 추출인지, future-readable residue인지
  - 실제 추출은 일어나지만, 독립 제도보다 `retrospective grouping`에 가깝다
  - formal flow line이 아니라 future-readable candidate evidence를 남기는 수준이다

#### 4-4. generation vs extraction boundary

- 입력 차이
  - generation 입력: 없음에 가깝고, 있어도 이미 형성된 trace의 전단계에 있다
  - extraction 입력: execution trace log, family sequence, route sequence, residue notes
- 출력 차이
  - generation 출력: 없음
  - extraction 출력: candidate pattern id, observed sequence, supporting runs, strength warning
- timing 차이
  - generation이 아니라 post-run retrospective 단계에서만 작동한다
  - extraction은 later comparison에서만 보인다
- surface 차이
  - generation은 current-reading surface와 연결되지 않는다
  - extraction은 report/detector output surface에서만 보인다
- 겹침/혼동 지점
  - trace가 남았다는 사실만으로 extraction이 이미 강한 기관이라고 과장하기 쉽다

#### 4-5. governance involvement

- `candidate-only 유지`가 extraction 쪽에 가장 강하게 개입한다
- `formal flow line 선언 금지`, `promotion하지 않음`, `small sample overclaim 금지`가 모두 extraction의 경계 규칙이다
- generation governance보다 extraction governance는 `승격 억제` 쪽이 더 직접적이다

#### 4-6. final note for this case

이 사례는 generation보다 extraction 쪽이 더 맞다. 다만 extraction도 아직 독립 strong 기관보다 `partial candidate` 또는 `usable retrospective grouping`으로 보는 것이 정확하다.

### case 3. structured doc routing / saltlux-goover reference ingest

#### 4-1. case summary

structured doc가 들어와 marker normalize, registration, label packet, observer ingest outputs, origin map, receipt, board surface가 생성된 사례다. 이 흐름은 입력과 표면구성이 선명하지만, line generation/extraction을 앞세우면 오히려 설명이 흐려진다.

#### 4-2. line generation reading

- fit level: forced
- what counts as generation here
  - 굳이 말하면 multi-lens readout이나 observer split에서 line seed가 생길 수 있다
- 무엇이 새 형성이고 무엇이 thickening/reuse인지
  - 그러나 실제 전면에는 doc registration, split unit, processing trace, receipt가 서 있다
  - 이 사례를 line generation 사례로 읽는 것은 과하다

#### 4-3. line extraction reading

- fit level: forced
- what counts as extraction here
  - split unit이나 processing trace를 나중에 line material로 읽을 수는 있다
- 실제 추출인지, future-readable residue인지
  - 하지만 그건 line extraction이라기보다 `future-readable ingest residue`에 가깝다

#### 4-4. generation vs extraction boundary

- 입력 차이
  - generation 입력/ extraction 입력 모두 뚜렷하지 않고, 실제 입력기는 doc/marker/origin이다
- 출력 차이
  - 실제 출력은 source manifest, split units, processing trace, readable board, receipt다
  - line generation/extraction 출력은 전면에 없다
- timing 차이
  - generation/extraction을 말하려면 이후 reread/line work가 더 들어와야 한다
- surface 차이
  - current-reading surface는 operation board/receipt/readable board이지 line surface가 아니다
- 겹침/혼동 지점
  - ingest artifacts를 곧바로 line artifacts로 부르는 오판이 생기기 쉽다

#### 4-5. governance involvement

- `ingest_only`, `execution_linkable=false`, append-only event/receipt 보호가 보인다
- 이는 line generation/extraction governance라기보다 입력 경계와 기록 보호 governance다

#### 4-6. final note for this case

이 사례는 generation도 extraction도 모두 과하다. line보다 `doc / split unit / processing trace / receipt / board`가 중심이라고 적는 편이 정확하다.

## 5. cross-case findings

- line generation에 반복적으로 나타나는 특징
  - current-reading surface에서 직접 보이는 경우가 많다
  - 새 형성보다 `thickening / reuse / carry / latent line 유지`가 더 자주 나타난다
  - phase, active latent lines, reread 조건과 강하게 붙어 있다

- line extraction에 반복적으로 나타나는 특징
  - current-reading surface보다 later comparison/report 단계에서 보인다
  - execution trace, ordered transition path, family sequence 같은 retrospective material을 입력으로 쓴다
  - 결과는 line 그 자체보다 `candidate evidence`, `grouping`, `warning`에 가깝다

- generation이 실제보다 과장되기 쉬운 조건
  - latent line 유지나 current phase articulation을 곧바로 “새 line 생성”이라 부를 때
  - routing/ingest 산출물을 line 생성으로 평탄화할 때

- extraction이 실제보다 과장되기 쉬운 조건
  - trace를 남긴 것만으로 extraction이라 부를 때
  - 2-run repetition을 strong pattern처럼 말할 때
  - candidate grouping을 formal flow object처럼 말할 때

- line이 아니라 phase/hint/residue/trace가 중심인 경우 어떤 오판이 생기는지
  - phase profile을 line 생성으로 과장
  - hint/reentry override를 line extraction으로 오독
  - ingest residue를 line artifact로 조기 승격

## 6. keep / demote / hold recommendation

- keep:
  - `라인생성기`는 organ registry에 계속 유지할 수 있다
  - 다만 설명할 때는 `새 line 생성`보다 `line/state thickening, carry, reuse를 포함하는 distributed generation function`으로 읽는 편이 맞다

- demote:
  - line generation을 모든 line 관련 사례의 중심 기관처럼 쓰는 표현
  - 특히 structured ingest 사례를 line generation 사례처럼 부르는 표현

- hold:
  - `라인추출기`를 독립 strong 기관처럼 쓰는 표현
  - 현재는 여전히 `partial candidate`로 두는 것이 맞다
  - extraction은 지금 단계에서 `retrospective grouping / future-readable candidate evidence` 수준으로 설명하는 편이 정확하다

특히 이번 판정은 아래와 같다.

- `라인생성기`를 현재 organ registry에서 계속 유지할 수 있는가?
  - 예. 다만 `distributed strong`을 “새 line을 많이 만든다”가 아니라 “line/state를 형성·유지·두껍게 한다”는 의미로 읽어야 한다.
- `라인추출기`를 여전히 partial candidate로 두는 것이 맞는가?
  - 예. 현재 근거로는 가장 정확하다.
- 둘을 지금 문서적으로 분리 유지할지, 아니면 더 많은 증거 전까지 주석적 구분으로 둘지
  - 분리 자체는 유지하되, extraction은 더 많은 증거 전까지 주석적/보수적 사용이 맞다.

## 7. final judgment

다음 단계로 가장 맞는 것은 `더 많은 사례 검증`이다.  
당장 organ registry wording을 크게 바꿀 정도의 충돌은 없지만, line generation의 의미를 계속 `thickening/reuse/carry`까지 포함한 보수적 표현으로 써야 하고, line extraction은 현재 상태 그대로 `partial candidate`로 두는 편이 가장 정확하다.

즉 지금 단계의 판정은 `현 상태 유지 + 보수적 사용`이다.

## appendix. evidence files

- [space_operating_organ_registry_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/space_operating_organ_registry_v0.md)
- [space_operating_organ_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/space_operating_organ_reading_v0.md)
- [space_operating_organ_applied_validation_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/space_operating_organ_applied_validation_v0.md)
- [space_boundary_declaration_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/space_boundary_declaration_v0.md)
- [governance_surface_summary_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/governance_surface_summary_v0.md)
- [current_phase.json](/Users/sungsookim/universe/vectorfl_replica/runtime/current_phase.json)
- [reentry_prebias_execution_check_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/reentry_prebias_execution_check_v0.md)
- [execution_trace_log_v0.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/execution_trace_log_v0.jsonl)
- [flow_candidate_detection.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/flow_candidate_detection.py)
- [flow_candidate_detection_loop_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/flow_candidate_detection_loop_v0.md)
- [flow_candidate_first_observation_report_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/flow_candidate_first_observation_report_v0.md)
- [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
- [doc_tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1_operation_receipt.md](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts/doc_tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1_operation_receipt.md)
