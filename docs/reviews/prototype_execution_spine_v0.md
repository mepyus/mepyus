# Prototype Execution Spine v0

## 목적

이 문서는 지금까지 만든 최소 adapter chain을
한 장의 실행 spine으로 묶는다.

핵심은 VectorFL이 현재 어디까지
실제로 흉내 내고 있는가를
high-level에서 한 번에 읽게 만드는 것이다.

## 핵심 문장

현재 prototype spine은 아래처럼 읽는다.

`artifact -> auto hint generation -> hint save/update -> entry prebias -> classifier-ready family/projection/route bias -> optional residue-backed reentry -> next family/projection/route bias`

즉 지금 단계의 VectorFL은
완전한 runtime engine은 아니지만,
entry와 reentry를 line-centered bias chain으로 다루는 최소 adapter stack을 갖고 있다.

## spine layers

## 1. artifact layer

출발점은 항상 artifact 또는 surface다.

대표 예:

- [builder_choi_interview_transcript_preprocess_comparison.json](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json)
- [runtime/current_phase.json](/Users/sungsookim/universe/vectorfl_replica/runtime/current_phase.json)
- [runtime/views/engine_state_latest/index.json](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_state_latest/index.json)

즉 line은 source를 대체하지 않는다.
artifact-first는 끝까지 유지된다.

## 2. auto hint generation layer

[auto_hint_generation_rules_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/auto_hint_generation_rules_v0.json)
이 field bundle을 읽어
first family/projection/route hint를 만든다.

실행 stub:

- [run_auto_hint_generation_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_auto_hint_generation_stub.py)

핵심 출력:

- `candidate_family_ids`
- `candidate_projection_ids`
- `candidate_route_ids`
- `residue_reentry_bias`

## 3. hint persistence layer

생성된 hint는
[source_to_family_hints_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/source_to_family_hints_v0.json)
에 append/update 된다.

이 단계가 중요한 이유는
다음 entry나 reentry에서
saved hint를 다시 참조할 수 있게 만들기 때문이다.

## 4. entry prebias layer

saved hint와 family-rooted alias가
classifier 이전에 family/projection/route bias를 만든다.

기준:

- [entry_prebias_policy_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/entry_prebias_policy_v0.md)

즉 classifier는 맨땅에서 family를 고르는 게 아니라
이미 기울어진 상태에서 final selection을 한다.

## 5. family/projection/route spine

이 단계부터는
line-centered entry grammar가 주도권을 가진다.

기준:

- [entry_coverage_check_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/entry_coverage_check_v0.md)

현재 coverage:

- input family
- transition family
- readout family

즉 `artifact -> hint -> alias -> signal -> classifier -> family -> projection -> route -> residue`
는 세 family 모두에서 성립한다.

## 6. residue-backed reentry layer

이전 family의 residue bias가
새 artifact와 question shift를 만나면
다음 family/projection/route bias를 강화한다.

기준:

- [residue_backed_reentry_rule_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/residue_backed_reentry_rule_v0.md)

실행 stub:

- [run_reentry_prebias_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_reentry_prebias_stub.py)

핵심 출력:

- source hint contribution
- residue rule contribution
- combined reentry order

## verified directions

현재 실제로 돌려본 방향은 두 개다.

### 1. input -> transition

- source residue:
  `preservation_before_flattening`
- question shift:
  `entry_shaping_to_transition_condition`
- resulting bias:
  `fam_transition_thickening`
  `proj_transition_preflight_reread`
  `route_preflight_reread`

### 2. transition -> readout

- source residue:
  `closure_before_presentation`
- question shift:
  `transition_condition_to_operator_readability`
- resulting bias order:
  `fam_transition_thickening` then `fam_operator_readout`
  `proj_transition_operator_readout` then `proj_operator_board_readout`
  `route_readonly_board`

이 두 번째 케이스가 특히 중요한 이유는
projection shift first / full handoff second라는 원칙을
실제 출력 순서로 보여주기 때문이다.

## current integrated execution stub

지금은 두 개의 stub가 분리되어 있다.

- auto hint:
  [run_auto_hint_generation_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_auto_hint_generation_stub.py)
- reentry prebias:
  [run_reentry_prebias_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_reentry_prebias_stub.py)

다음 단계는 이 둘을 이어서
single prototype loop stub로 보는 것이다.

## 현재 판단

지금 VectorFL은
아직 general runtime engine은 아니지만,
최소한 아래는 실제로 한다.

- artifact에서 hint를 뽑는다
- hint를 저장한다
- saved hint를 다시 읽는다
- residue-backed reentry bias를 계산한다
- next family/projection/route order를 출력한다

즉 지금은
`line-centered execution bias engine v0`
정도로 부를 수 있다.

## 한 줄 요약

prototype execution spine v0는
`artifact -> auto hint -> hint persistence -> entry bias -> family/projection/route spine -> residue-backed reentry`
로 이어지는 현재 VectorFL의 최소 실행 체인을 한 장으로 묶은 문서다.
