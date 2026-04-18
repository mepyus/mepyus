# Classifier Adapter Stub v0

## 목적

이 문서는
saved hint와 optional reentry prebias를 받아
최종 `family / projection / route`를 다시 고르는
최소 classifier adapter를 고정한다.

실행 스크립트:

- [run_classifier_chain_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_classifier_chain_stub.py)

핵심 모듈:

- [classifier_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/classifier_adapter.py)

## 현재 방식

이 stub는 signal을 맨땅에서 다시 추론하지 않는다.

대신:

- current hint
- optional reentry prebias
- classifier rule

을 reverse match 해서
가장 맞는 classifier rule을 다시 고른다.

즉 현재 방식은
`entry state -> classifier rule reverse match`
다.

## 왜 이 방식이 맞는가

특히 `transition -> readout` 같은 경우는
기본 taxonomy default만으로는
`proj_transition_operator_readout` 같은 override projection을
정확히 설명하기 어렵다.

그래서 classifier rule 자체를 다시 대입하는 편이
더 정직하다.

## expected use

### current hint only

```bash
python3 scripts/run_classifier_chain_stub.py runtime/views/engine_state_latest/index.json
```

### reentry-aware classification

```bash
python3 scripts/run_classifier_chain_stub.py runtime/views/engine_state_latest/index.json \
  --previous-artifact runtime/current_phase.json \
  --question-shift transition_condition_to_operator_readability
```

## 한 줄 요약

classifier adapter stub v0는
`saved hint + optional reentry prebias`
를 classifier rule에 다시 대입해
최종 `family / projection / route`를 선택하는 최소 adapter다.
