# Full Entry Reentry Chain Execution Check v0

## 목적

이 문서는
`auto hint -> optional reentry prebias -> classifier`
까지 이어지는 현재 full chain을
실행 결과 기준으로 짧게 정리한다.

관련 실행기:

- [run_classifier_chain_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_classifier_chain_stub.py)
- [run_prototype_execution_spine_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_prototype_execution_spine_stub.py)

## 1. readout direct entry

실행:

```bash
python3 scripts/run_classifier_chain_stub.py runtime/views/engine_state_latest/index.json
```

결과 핵심:

- current hint:
  `fam_operator_readout / proj_operator_board_readout / route_readonly_board`
- inferred signal:
  `operator_overview_request`
- selected classifier rule:
  `cls_rule_operator_overview`

판단:

direct readout entry에서는
hint와 classifier가 거의 그대로 일치한다.

## 2. transition -> readout reentry

실행:

```bash
python3 scripts/run_classifier_chain_stub.py runtime/views/engine_state_latest/index.json \
  --previous-artifact runtime/current_phase.json \
  --question-shift transition_condition_to_operator_readability
```

결과 핵심:

- source hint:
  `fam_operator_readout / proj_operator_board_readout`
- reentry prebias:
  `fam_transition_thickening` first,
  then `fam_operator_readout`
- selected classifier rule:
  `cls_rule_transition_readout_override`
- selected projection:
  `proj_transition_operator_readout`
- selected route:
  `route_readonly_board`

판단:

이 케이스는 classifier가
새 artifact의 broad readout hint를 그대로 따르지 않고,
residue-backed reentry가 만든
`transition-family explanation first`
방향을 유지한다는 점을 보여준다.

## 3. input -> transition full spine

실행:

```bash
python3 scripts/run_prototype_execution_spine_stub.py runtime/current_phase.json \
  --previous-artifact app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json \
  --question-shift entry_shaping_to_transition_condition
```

결과 핵심:

- generated hint:
  `fam_transition_thickening / proj_transition_preflight_reread / route_preflight_reread`
- reentry rule:
  `reentry_rule_preservation_to_transition`
- selected classifier rule:
  `cls_rule_transition_blockage`

판단:

이 방향은
auto hint, residue rule, classifier가 모두 같은 family/projection/route로 수렴하는
안정적인 same-family chain이다.

## 한 줄 요약

full entry reentry chain execution check v0는
현재 VectorFL의 최소 실행체인이
`direct readout`, `transition -> readout`, `input -> transition`
세 상황에서 실제로 classifier까지 닫힌다는 점을 보여준다.
