# external_case_summary_pair_validation_saltlux_ai_v1

## 1. case setup
- canonical input: [saltlux_ai.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/saltlux_ai.txt)
- secondary summary: [saltlux_ai_summary.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/saltlux_ai_summary.txt)

## 2. pair reading
- `saltlux_ai.txt`는 raw primary input으로 유지된다.
- `saltlux_ai_summary.txt`는 원문을 대체하는 source가 아니라 secondary summary / derived reference로 읽는다.
- summary는 원문의 주요 구조 축을 빠르게 정리해 주지만, 강한 결론과 성능/우위 문장을 더 단단하게 보이게 만드는 경향이 있다.

## 3. same points
- agentic AI를 단순 생성이 아니라 추론/계획/도구 호출/반복 조사 흐름으로 읽는다.
- ontology / grounding / semantic layer를 구조 보강 재료로 읽는다.
- 공공/보안/온프레미스 제약을 운영 조건으로 읽는다.

## 4. distortion risk from summary
- 원문에서 `defer`로 가야 할 강한 수치/우위/제로 환각 표현이 summary에서는 더 정리된 사실처럼 보인다.
- summary는 vendor positioning과 sovereign framing을 더 단정적으로 읽히게 만든다.
- 따라서 summary는 판독 보조에는 유용하지만, source hierarchy를 뒤집을 정도의 우선권을 가지면 안 된다.

## 5. verdict
- canonical preserved: YES
- summary remained secondary: YES
- source hierarchy preserved: YES
- note:
  - summary는 유용하지만, 원문보다 먼저 판독 기준으로 쓰면 `defer` 영역이 과도하게 `outer_candidate`처럼 보일 수 있다.
