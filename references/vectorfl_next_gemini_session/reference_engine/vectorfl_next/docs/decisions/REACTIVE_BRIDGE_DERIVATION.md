# Reactive Bridge Derivation

## Decision

`bridge_trace`는 수동 관계 등록만이 아니라 relocation 반응에서 유도될 수 있어야 한다.

## Current rule

- 지정된 cell들에 relocation 반응 이벤트가 있으면 bridge derivation이 가능하다.
- 또는 두 local space의 constituent cell들을 통해 bridge derivation이 가능하다.
- 첫 유도는 `observed`로 두고, local-space pair에 대한 반복 support round가 쌓일 때만 `held`로 올린다.
- `held`가 되려면 relocation이 2회 이상이고 shared boundary overlap이 1 이상이며 support round가 2 이상이어야 한다.
- 또한 반복 support 사이에 최소 temporal spacing이 있어야 한다.
- relocation 반응이 없으면 bridge를 만들지 않는다.
- bridge가 local space에 attach되면 해당 local space는 `bridge_exposed`로 다시 읽는다.

## Why

- bridge는 해석자가 나중에 붙이는 라벨이 아니라 공간 반응의 부산물이어야 한다.
- relocation이 반복되면 adjacent space 가능성이 구조적으로 드러나야 한다.
- bridge trace는 merge를 수행하지 않고 local space를 bridge-facing 상태로만 노출시킨다.
- durable bridge holding은 first exposure와 분리해서 늦게 열려야 한다.
- time은 독립 ontology가 아니라 persistence를 읽기 위한 최소 조건으로만 사용한다.

## Follow-up risk

- 현재는 relocation 이벤트 수와 boundary overlap만 본다.
- 이후에는 local space pressure divergence와 bridge persistence도 함께 봐야 한다.
