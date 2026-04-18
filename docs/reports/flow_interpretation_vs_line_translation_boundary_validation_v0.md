# flow interpretation vs line translation boundary validation v0

## 1. verdict

현재 저장소에서 `흐름해석기`와 `라인번역기`는 서로 다른 기관으로 말할 수는 있지만, 실제 실행 spine에서는 자주 연쇄적으로 붙어 나온다. 가장 정확한 판정은 이렇다. `흐름해석기`는 `경로/전환/다음 hop/미해결 edge`를 읽는 기관으로 유지 가능하고, `라인번역기`는 `source artifact 또는 current-reading surface를 family/projection/route bias가 걸린 operating grammar로 바꾸는 기관`으로 유지 가능하다. 다만 hint, classifier, residue-backed reentry, override가 들어가는 구간에서는 둘이 분리된 두 단계라기보다 `겹치는 연쇄의 두 기능`처럼 보인다.

강도만 보면 둘 다 유지 가능하다. 그러나 완전 분리로 서술하는 것은 과하고, `접점이 큰 두 기능`으로 읽는 것이 더 정확하다.

## 2. why this validation

applied validation과 generation/extraction 검증 이후에도 가장 남는 경계는 `흐름을 읽는 것`과 `운영 문법으로 바꾸는 것`의 차이였다. 특히 source hint 생성, classifier reverse-match, residue-backed reentry, question shift, current-reading surface override가 한 연쇄 안에서 이어지다 보니, 어느 단계까지를 번역이라 하고 어느 단계부터를 해석이라 할지 흔들릴 수 있었다.

그래서 이번 검증은 새 기관을 추가하려는 것이 아니라, 현재 저장소 기준으로 둘이 실제로 어디서 갈라지고 어디서 겹치는지 경계를 판정하려는 것이다.

## 3. selected cases

- `transition thickening / current_phase`
  - family / projection / route / next hop 해석이 가장 강하게 보이는 사례라서 골랐다.
- `transition -> readout reentry / classifier override`
  - hint, residue-backed reentry, classifier override, question shift가 한꺼번에 보이는 사례라서 골랐다.
- `direct board readout / engine_state_latest`
  - translation은 선명하지만 flow interpretation은 제한적인 사례라서 골랐다.

## 4. case-by-case reading

### case 1. transition thickening / current_phase

#### 4-1. case summary

`runtime/current_phase.json`과 `runtime/preflight_last_decision.json`은 `active_latent_lines`, `decision=thickening`, `not closure-ready`, `next_check_trigger`를 보여주고, 이를 `fam_transition_thickening -> proj_transition_preflight_reread -> route_preflight_reread`로 읽게 한다. 이 사례는 current-reading surface가 이미 transition line spine의 현재 위치를 노출하고 있는 사례다.

#### 4-2. flow interpretation reading

- fit level: strong
- what counts as interpretation here
  - `transition_blockage`를 읽는다
  - `thickening vs closure` 위치를 읽는다
  - `same-family reread`, `validation expansion`, `operator-facing handoff` 같은 next hop을 읽는다
- 무엇이 transition/path/next hop reading인지
  - `decision_reason`
  - `next_check_trigger`
  - `remain in thickening`
  - `closure review later`
  - 이 전부가 path/next hop reading이다

#### 4-3. line translation reading

- fit level: usable
- what counts as translation here
  - phase surface와 preflight surface를 `transition_blockage -> fam_transition_thickening -> proj_transition_preflight_reread -> route_preflight_reread`라는 operating grammar로 바꾸는 것
- 무엇이 source/surface/question을 operating grammar로 바꾸는 일인지
  - `active_latent_lines + decision=thickening + next_check_trigger`를 classifier-ready signal/family/projection/route로 recode하는 단계가 번역에 해당한다

#### 4-4. interpretation vs translation boundary

- 입력 차이
  - interpretation 입력: 이미 선택된 phase 상태, latent line 상태, next check 맥락
  - translation 입력: current phase surface 자체와 그 필드 조합
- 출력 차이
  - interpretation 출력: 왜 thickening에 머무는지, 무엇이 next hop인지
  - translation 출력: `transition_blockage`, `fam_transition_thickening`, `proj_transition_preflight_reread`, `route_preflight_reread`
- timing 차이
  - translation이 먼저 current surface를 operating grammar로 recode한다
  - interpretation은 그 grammar 위에서 path/next hop을 읽는다
- surface 차이
  - translation은 source surface를 entry grammar로 바꾼다
  - interpretation은 current-reading surface와 route contract를 함께 읽는다
- 겹침/혼동 지점
  - issue-root classifier와 route selection은 번역과 해석의 접점처럼 보인다

#### 4-5. governance involvement

- `closure-ready 미도달`은 interpretation 쪽에 더 강하게 개입한다
- `route_preflight_reread` 유지와 `same-family reread`는 interpretation 쪽 판단이다
- translation 쪽 governance는 phase surface를 direct readout이 아니라 transition thickening grammar로 읽도록 기울이는 정도로 작동한다

#### 4-6. final note for this case

이 사례는 interpretation 쪽이 더 맞는다. translation도 분명 존재하지만, 핵심은 경로와 다음 reread 방향을 읽는 데 있다.

### case 2. transition -> readout reentry / classifier override

#### 4-1. case summary

새 artifact인 `runtime/views/engine_state_latest/index.json`은 source hint 차원에서는 `fam_operator_readout / proj_operator_board_readout / route_readonly_board`를 가리킨다. 그러나 previous artifact가 `runtime/current_phase.json`이고 question shift가 `transition_condition_to_operator_readability`일 때, residue-backed reentry는 `fam_transition_thickening`를 먼저 세우고 classifier는 `cls_rule_transition_readout_override`를 선택해 최종적으로 `proj_transition_operator_readout / route_readonly_board`로 간다.

#### 4-2. flow interpretation reading

- fit level: strong
- what counts as interpretation here
  - `transition-family explanation first`라는 handoff logic을 읽는 것
  - `same-family projection shift first, full handoff second` 순서를 읽는 것
  - broad board를 그대로 보지 않고 unresolved transition explanation을 먼저 보게 하는 next hop reading
- 무엇이 transition/path/next hop reading인지
  - `fam_transition_thickening -> fam_operator_readout` family order
  - `proj_transition_operator_readout -> proj_operator_board_readout` projection order
  - `route_readonly_board`를 explanation-first로 쓰는 override

#### 4-3. line translation reading

- fit level: strong
- what counts as translation here
  - broad operator readout surface를 `transition-first explanation` grammar로 다시 바꾸는 것
  - question shift와 residue bias가 source hint를 다른 operating grammar로 recode하는 것
- 무엇이 source/surface/question을 operating grammar로 바꾸는 일인지
  - `engine_state_latest`라는 broad board surface
  - `transition_condition_to_operator_readability`라는 question shift
  - `closure_before_presentation` residue bias
  - 이 셋이 합쳐져 operator board를 transition explanation entry로 재번역한다

#### 4-4. interpretation vs translation boundary

- 입력 차이
  - interpretation 입력: 이미 재정렬된 family/projection order와 handoff logic
  - translation 입력: new artifact hint, previous residue bias, question shift
- 출력 차이
  - interpretation 출력: explanation-first reading order, projection shift, next handoff 의미
  - translation 출력: broad readout hint에서 transition-operator-readout grammar로의 shift
- timing 차이
  - translation은 source hint contribution과 residue rule contribution을 재조합하는 단계에서 먼저 일어난다
  - interpretation은 그 재조합 결과를 경로/우선순위로 읽는다
- surface 차이
  - translation은 `engine_state_latest`를 다른 entry grammar로 recode한다
  - interpretation은 `왜 transition family가 먼저인가`를 설명한다
- 겹침/혼동 지점
  - classifier override는 한쪽에만 속한다고 보기 어렵다
  - reentry prebias도 translation과 interpretation의 경계 혼합 지점이다

#### 4-5. governance involvement

- `closure_before_presentation`은 translation과 interpretation 둘 다에 개입한다
- `direct readout 보류`는 translation 쪽에서 broad board를 그대로 두지 않게 하고
- `explanation_first`는 interpretation 쪽에서 next hop 우선순위를 바꾼다
- `classifier override caution`은 접점 전체에 걸린 governance다

#### 4-6. final note for this case

이 사례는 둘이 실제로 겹친다. translation과 interpretation을 분리해 말할 수는 있지만, residue-backed reentry와 classifier override는 두 기능의 혼합 지점으로 보는 것이 가장 정확하다.

### case 3. direct board readout / engine_state_latest

#### 4-1. case summary

`runtime/views/engine_state_latest/index.json`은 broad operator overview surface이고, direct entry에서는 `operator_overview_request -> fam_operator_readout -> proj_operator_board_readout -> route_readonly_board`로 거의 곧바로 닫힌다. 이 사례는 current-reading surface가 이미 operator-facing grammar를 강하게 품고 있는 상태다.

#### 4-2. flow interpretation reading

- fit level: usable
- what counts as interpretation here
  - broad board 다음에 detail/search/activity로 내려갈 수 있다는 next route reading
  - readout family 안에서 board-first라는 경로 판단
- 무엇이 transition/path/next hop reading인지
  - `drill down`, `open activity panel`, `launch internal search` 정도가 next hop reading이다

#### 4-3. line translation reading

- fit level: strong
- what counts as translation here
  - engine state index surface를 `operator_overview_request`, `fam_operator_readout`, `proj_operator_board_readout`, `route_readonly_board` grammar로 바꾸는 것
- 무엇이 source/surface/question을 operating grammar로 바꾸는 일인지
  - raw current-state index를 broad operator board entry로 읽게 만드는 것이 번역의 핵심이다

#### 4-4. interpretation vs translation boundary

- 입력 차이
  - interpretation 입력: 이미 operator board entry로 정리된 상태
  - translation 입력: broad state surface 자체
- 출력 차이
  - interpretation 출력: board 다음 detail/search route 제안
  - translation 출력: overview request, operator readout family, board projection, readonly board route
- timing 차이
  - translation이 먼저 surface를 operating grammar로 recode한다
  - interpretation은 그 다음 경로만 약하게 읽는다
- surface 차이
  - translation은 current-reading surface 자체에 직접 붙는다
  - interpretation은 surface 이후의 next route에서만 약하게 보인다
- 겹침/혼동 지점
  - board-first route selection을 interpretation이라고 과장하기 쉽다

#### 4-5. governance involvement

- `direct readout 보류`는 거의 없다. 이 사례는 direct readout이 정당화된 사례다.
- governance는 `presentation caution residue` 정도로 약하게 개입한다.
- route selection caution은 detail/search로 너무 빨리 좁히지 않는 정도로만 작동한다.

#### 4-6. final note for this case

이 사례는 interpretation보다 translation 쪽이 더 맞는다. flow interpretation을 강하게 말하면 과장에 가깝다.

## 5. cross-case findings

- flow interpretation에 반복적으로 나타나는 특징
  - route 이후의 `next hop`, `handoff`, `projection shift`, `unresolved edge`, `remain/reopen/review`를 읽는다
  - phase, residue, reread direction, family order와 잘 붙는다
  - current-reading surface를 그대로 두기보다 `그 표면이 다음에 어디로 가야 하는가`를 읽는다

- line translation에 반복적으로 나타나는 특징
  - source artifact 또는 current-reading surface를 family/projection/route bias가 걸린 operating grammar로 recode한다
  - hint generation, signal inference, family-rooted alias, question shift, residue bias와 잘 붙는다
  - broad board, phase surface, raw comparison artifact를 “현재 공간이 읽을 수 있는 문법”으로 바꾸는 쪽에 강하다

- interpretation이 실제보다 과장되기 쉬운 조건
  - route를 하나 고른 것만으로 flow interpretation이라 부를 때
  - board/readout direct entry처럼 next hop reading이 약한 사례를 해석 중심 사례처럼 말할 때

- translation이 실제보다 과장되기 쉬운 조건
  - classifier 결과 전체를 번역이라고 한꺼번에 부를 때
  - route/next hop reasoning까지 모두 번역으로 밀어 넣을 때

- hint/classifier/reentry/override 사례에서 생기는 오판
  - hint가 있으니 번역기만 있다고 보는 오판
  - classifier가 family를 골랐으니 해석기만 있다고 보는 오판
  - override를 한쪽 기관의 소유로만 고정하는 오판
  - 실제로는 이 구간이 가장 강한 접점이며, `translation + interpretation`이 연쇄적으로 붙어 있다

- current-reading surface와 operator readout이 경계를 어떻게 흔드는지
  - current-reading surface가 이미 operator-facing grammar를 품고 있으면 translation과 surface adaptation이 거의 겹친다
  - 그 위에 transition explanation이나 question shift가 들어오면 interpretation이 급격히 강해진다
  - 즉 surface 자체의 성숙도가 두 기관 경계를 흔든다

## 6. keep / demote / hold recommendation

- keep:
  - `흐름해석기`는 current organ registry에서 계속 유지할 수 있다
  - `라인번역기`도 현재 강도로 계속 유지할 수 있다
  - 둘 다 실제 사례에서 유효하다

- demote:
  - classifier override를 자동으로 해석기 또는 번역기 한쪽으로만 부르는 표현
  - direct board readout 같은 사례를 해석 중심 사례처럼 과장하는 표현

- hold:
  - `흐름해석기`와 `라인번역기`가 완전히 분리된다고 단정하는 표현
  - 특히 hint/classifier/reentry/override 구간에서는 `겹치는 연쇄의 두 기능`이라는 주석적 설명을 붙이는 편이 맞다

특히 이번 판정은 아래와 같다.

- `흐름해석기`를 현재 organ registry에서 계속 유지할 수 있는가?
  - 예. 경로/전환/다음 hop reading이라는 축이 실제 사례에서 분명히 보인다.
- `라인번역기`를 현재 강도로 계속 유지할 수 있는가?
  - 예. source/surface/question을 operating grammar로 recode하는 기능이 실제 사례에서 선명하다.
- 둘을 지금 문서적으로 분리 유지할지, 아니면 더 많은 증거 전까지 “겹치는 연쇄의 두 기능”으로 주석적 설명을 붙여야 하는가?
  - 분리 유지 자체는 가능하다. 다만 hint/classifier/reentry/override 사례에는 `겹치는 연쇄의 두 기능`이라는 주석이 필요하다.

## 7. final judgment

다음 단계로 가장 맞는 것은 `더 많은 사례 검증`이다.  
지금 당장 organ registry wording을 바꿀 정도의 충돌은 없지만, 흐름해석기와 라인번역기를 서술할 때는 각각의 핵심을 유지하면서도, 접점 구간에서는 분리보다 연쇄를 함께 적는 보수적 문장 규칙을 유지하는 편이 맞다.

즉 현재 판정은 `현 상태 유지 + 접점 주석 강화`다.

## appendix. evidence files

- [space_operating_organ_registry_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/space_operating_organ_registry_v0.md)
- [space_operating_organ_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/space_operating_organ_reading_v0.md)
- [space_operating_organ_applied_validation_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/space_operating_organ_applied_validation_v0.md)
- [line_generation_vs_extraction_boundary_validation_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/line_generation_vs_extraction_boundary_validation_v0.md)
- [space_boundary_declaration_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/space_boundary_declaration_v0.md)
- [governance_surface_summary_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/governance_surface_summary_v0.md)
- [loop_demo_case_transition_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/loop_demo_case_transition_v0.md)
- [loop_demo_case_readout_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/loop_demo_case_readout_v0.md)
- [full_entry_reentry_chain_execution_check_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/full_entry_reentry_chain_execution_check_v0.md)
- [reentry_prebias_execution_check_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/reentry_prebias_execution_check_v0.md)
- [classifier_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/classifier_adapter.py)
- [auto_hint_generation.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/auto_hint_generation.py)
- [current_phase.json](/Users/sungsookim/universe/vectorfl_replica/runtime/current_phase.json)
- [engine_state_latest/index.json](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_state_latest/index.json)
