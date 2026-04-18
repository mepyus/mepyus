# Signal Generation Sources Registry v0

## 목적

이 문서는 [signal_generation_sources_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/signal_generation_sources_v0.json)
을 현재 signal source registry로 고정한다.

이 registry는
어떤 artifact/surface/operator input이
어떤 `signal_kind` 를 낳는지 적는다.

## 현재 포함된 source 축

- input registry / entry material
- preprocess comparison outputs
- phase decision fields
- stage corridor outputs
- engine state latest views
- internal search query input
- entry summary/board families

## registry 의미

이 registry가 생기면서
entry path는 아래처럼 grounded 된다.

- artifact/source
- signal_kind
- classifier rule
- family/projection/route

즉 signal이 더 이상 추상 vocabulary에 머물지 않고,
실제 repo 안의 근거 surface와 연결된다.

## 아직 남은 약점

### 1. source coverage는 아직 얇다

대표 source만 먼저 잡았다.

### 2. source priority는 classifier priority와 별도다

source confidence와 rule precedence를 나중에 더 정교하게 연결할 수 있다.

### 3. readout 쪽은 operator input과 runtime view가 혼합돼 있다

향후 input-side signal과 state-side signal을 더 세분할 수 있다.

## 다음 단계

다음으로 자연스러운 일은 아래 둘 중 하나다.

1. `projection_selection_policy_v0`
2. `signal_to_classifier_binding_v0`

현재로서는 2번이 더 직접적이다.
