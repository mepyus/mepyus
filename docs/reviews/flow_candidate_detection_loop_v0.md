# Flow Candidate Detection Loop v0

## 목적

이 문서는
현재 prototype execution spine 위에
bounded flow candidate detection loop를 어떻게 얹는지 정리한다.

## loop 구조

현재 loop는 아래 순서로 돈다.

1. artifact를 기존 spine으로 읽는다
2. current hint / optional reentry / classifier 결과를 얻는다
3. per-run execution trace를 append-only로 기록한다
4. 여러 trace를 비교한다
5. 반복되는 multi-step pattern을 flow candidate로 관찰한다
6. 아직은 promotion하지 않고 warning과 함께 남긴다

## trace에 남기는 최소 필드

- `run_id`
- `source_artifact`
- `source_surface_type`
- `current_hint`
- `previous_hint`
- `reentry_prebias`
- `final_family`
- `final_projection`
- `final_route`
- `classifier_rule_selected`
- `question_shift`
- `ordered_transition_path`
- `residue_related_notes`
- `timestamp`
- `execution_context`

## detector가 보는 것

현재 detector는 아래 반복만 약하게 본다.

- same stage sequence repeated
- same family handoff repeated
- same route edge repeated
- same reentry hook repeated
- same residue-to-next-family tendency repeated

## strength 해석

- `weak`
  - 2회 반복
- `medium`
  - 3회 반복
- `strong`
  - 4회 이상 반복

이건 어디까지나 bounded heuristic이다.
promotion 판정이 아니다.

## boundary rule

candidate detector는
반복을 보이게 하는 용도지,
grand orchestration을 formalize하는 용도가 아니다.

즉:

- classifier spine은 그대로 유지한다
- host logic와 VectorFL logic을 섞지 않는다
- candidate는 관찰 대상이지 규정된 flow object가 아니다

## 실행기

- [run_prototype_execution_spine_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_prototype_execution_spine_stub.py)
- [run_flow_candidate_detection_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_flow_candidate_detection_stub.py)

핵심 모듈:

- [execution_trace.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/execution_trace.py)
- [flow_candidate_detection.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/flow_candidate_detection.py)

## 한 줄 요약

flow candidate detection loop v0는
현재 line-centered execution spine을 여러 번 돌려
반복 transition pattern만 약하게 관찰 가능한 상태로 만드는 bounded observation loop다.
