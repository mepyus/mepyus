# Prototype Execution Spine Stub v0

## 목적

이 문서는
auto hint generation, residue-backed reentry, classifier selection을
한 번의 흐름으로 묶는 최소 실행 stub를 고정한다.

실행 스크립트:

- [run_prototype_execution_spine_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_prototype_execution_spine_stub.py)

## stub 범위

이 stub는 아래를 한 번에 한다.

- new artifact에서 auto hint generation
- 필요하면 첫 hint를 manifest에 save
- saved current hint 재로드
- optional previous artifact hint 로드
- optional residue-backed reentry prebias 계산
- current hint와 optional reentry를 기반으로 classifier selection 수행
- 결과를 하나의 JSON payload로 출력

즉 이 stub는
현재 VectorFL의 최소 execution spine을
하나의 command로 보여주는 통합 adapter다.

## expected use

### entry only

```bash
python3 scripts/run_prototype_execution_spine_stub.py runtime/views/engine_state_latest/index.json --save
```

### entry + reentry

```bash
python3 scripts/run_prototype_execution_spine_stub.py runtime/current_phase.json \
  --save \
  --previous-artifact app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json \
  --question-shift entry_shaping_to_transition_condition
```

## current meaning

이 stub가 생기면
우리는 더 이상
auto hint와 reentry를 따로따로만 보지 않는다.

즉 현재 VectorFL이 가진 최소 adapter chain을
하나의 실행 단위로 확인할 수 있다.

## 한 줄 요약

prototype execution spine stub v0는
`auto hint -> save -> current hint -> optional reentry prebias -> classifier selection`
를 한 번에 실행하는 통합 최소 stub다.
