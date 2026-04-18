# Issue Root Classifier Registry v0

## 목적

이 문서는 [issue_root_classifier_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/issue_root_classifier_v0.json)
을 현재 issue-root entry classifier의 첫 registry로 고정한다.

이 registry는
새 signal이 들어왔을 때
어느 family / projection / initial route로 보내는지를
rule-based로 기록한다.

## 현재 포함된 rule

- `cls_rule_input_preprocess_ambiguity`
- `cls_rule_input_raw_entry`
- `cls_rule_transition_blockage`
- `cls_rule_boundary_ambiguity`
- `cls_rule_operator_overview`
- `cls_rule_operator_search`
- `cls_rule_transition_readout_override`

## registry 의미

이 registry가 생기면서
이제 구조는 아래까지 닫힌다.

- source hint / signal prebias
- issue-root signal
- family 선택
- projection 선택
- initial route 선택
- route selection policy

즉 새로운 issue가 들어왔을 때
어디서부터 읽기 시작해야 하는지
더 이상 문장 설명만으로 두지 않게 된다.

## 아직 남은 약점

### 1. signal normalization이 얇다

`signal_kind` 종류와 생성 방식이 아직 최소 수준이다.

### 2. requested_outcome override가 일부만 있다

지금은 transition/readout override 한 가지 정도만 잡았다.

### 3. classifier priority 자체는 아직 명시적이지 않다

rule 충돌 시 우선순위를 별도 policy로 잠글 수 있다.

### 4. classifier 이전 prebias 층이 분리돼 있었다

이건 이제
[entry_prebias_policy_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/entry_prebias_policy_v0.md)
와
[entry_prebias_examples_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/entry_prebias_examples_v0.json)
로 보강됐다.

## 다음 단계

다음으로 자연스러운 일은 아래 둘 중 하나다.

1. `signal_kind taxonomy v0` 를 만들어 classifier 입력 신호를 더 체계화
2. `classifier_priority_policy_v0` 를 만들어 rule 충돌 해소 순서를 잠그기

현재로서는 1번이 더 상위라서 먼저다.
