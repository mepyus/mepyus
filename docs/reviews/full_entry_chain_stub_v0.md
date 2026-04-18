# Full Entry Chain Stub v0

## 목적

이 문서는
현재 prototype chain에서 classifier까지 실제로 붙이는
최소 통합 stub를 고정한다.

실행 스크립트:

- [run_full_entry_chain_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_full_entry_chain_stub.py)

핵심 로직:

- [auto_hint_generation.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/auto_hint_generation.py)
- [reentry_prebias.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/reentry_prebias.py)
- [classifier_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/classifier_adapter.py)

## stub 범위

이 stub는 아래를 한 번에 한다.

- new artifact에서 auto hint generation
- 필요하면 hint save
- current hint 로드
- optional previous hint + residue-backed reentry prebias
- current hint 또는 reentry prebias에서 signal candidate 역추정
- selected signal로 classifier selection

즉 이 stub는
현재 VectorFL의 minimal full entry/reentry chain을
한 번에 출력한다.

## expected use

### entry only

```bash
python3 scripts/run_full_entry_chain_stub.py runtime/views/engine_state_latest/index.json
```

### entry + reentry + classifier

```bash
python3 scripts/run_full_entry_chain_stub.py runtime/current_phase.json \
  --previous-artifact app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json \
  --question-shift entry_shaping_to_transition_condition
```

## current meaning

이 stub가 생기면
이제 chain은
`artifact -> hint -> save/load -> residue reentry -> signal inference -> classifier`
까지 한 번에 이어진다.

아직 route execution은 하지 않지만,
entry router 관점에서는 거의 한 바퀴 닫힌 상태다.

## 한 줄 요약

full entry chain stub v0는
현재 VectorFL의 최소 entry/reentry adapter chain을 classifier selection까지 연결한 통합 실행 도구다.
