# Reentry Prebias Execution Check v0

## 목적

이 문서는
[run_reentry_prebias_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_reentry_prebias_stub.py)
를 실제로 돌린 두 방향의 결과를 간단히 정리한다.

대상:

- `input -> transition`
- `transition -> readout`

## 1. input -> transition

실행:

```bash
python3 scripts/run_reentry_prebias_stub.py \
  --previous-artifact app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json \
  --new-artifact runtime/current_phase.json \
  --question-shift entry_shaping_to_transition_condition
```

결과 핵심:

- matched rule:
  `reentry_rule_preservation_to_transition`
- source hint family:
  `fam_transition_thickening`
- residue rule family:
  `fam_transition_thickening`
- final reentry family:
  `fam_transition_thickening`
- final projection:
  `proj_transition_preflight_reread`
- final route:
  `route_preflight_reread`

판단:

이 방향은 source hint와 residue rule이 같은 family를 가리켜서
reentry bias가 매우 안정적이다.

## 2. transition -> readout

실행:

```bash
python3 scripts/run_reentry_prebias_stub.py \
  --previous-artifact runtime/current_phase.json \
  --new-artifact runtime/views/engine_state_latest/index.json \
  --question-shift transition_condition_to_operator_readability
```

결과 핵심:

- matched rule:
  `reentry_rule_closure_to_readout`
- source hint family:
  `fam_operator_readout`
- residue rule family:
  `fam_transition_thickening`, `fam_operator_readout`
- final reentry family order:
  `fam_transition_thickening`, `fam_operator_readout`
- final projection order:
  `proj_transition_operator_readout`, `proj_operator_board_readout`
- final route:
  `route_readonly_board`

판단:

이 방향은 일부러 더 흥미롭다.

- new artifact hint는 broad operator readout을 가리킨다
- residue rule은 same-family projection shift를 먼저 보게 한다

즉 v0 output은
`projection shift first, full handoff second`
라는 handoff 원칙을 실제 순서로 드러낸다.

## 3. 현재 해석

지금 stub는 아래를 분리해서 보여준다.

- source hint contribution
- residue rule contribution
- combined reentry order

이 분리가 중요한 이유는
reentry가 단순 merge가 아니라
`새 artifact가 무엇을 가리키는가`
와
`과거 residue가 무엇을 보존하려 하는가`
를 함께 읽는 단계이기 때문이다.

## 한 줄 요약

reentry prebias execution check v0는
`input -> transition`은 안정적 same-family convergence로,
`transition -> readout`은 projection shift 우선 followed by full handoff 가능성으로 읽힌다는 점을 실제 실행 결과로 보여준다.
