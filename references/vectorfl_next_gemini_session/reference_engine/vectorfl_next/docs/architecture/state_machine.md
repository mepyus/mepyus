# State Machine

현재 스캐폴드는 과정 상태를 append-only event로 남기는 것을 우선한다.

## SeedState

- `isolated`
- `forming`
- `reentering`
- `cell_candidate`
- `cell_bound`

## CellState

- `candidate`
- `held`
- `unstable`
- `reentering`
- `dissolved`

## LocalSpaceState

- `forming`
- `stable_local`
- `sparse`
- `boundary_heavy`
- `bridge_exposed`

`bridge_exposed`는 relocation 반응이나 attached bridge trace 때문에 local space가 인접 공간을 향해 열려 있는 상태를 뜻한다.
이 상태는 durable bridge holding과 같지 않다. 처음에는 노출만 생기고, 반복 support round가 쌓일 때 bridge 쪽만 `held`로 숙성된다.
이 숙성은 최소 temporal spacing을 요구하지만, 시간 자체를 별도 core ontology로 만들지는 않는다.

## Reactive interpretation

- `thickening` 반응은 cell을 더 강하게 붙잡는 방향으로 읽는다.
- `split` 반응은 local space 내부 경계와 긴장 증가로 읽는다.
- `relocation` 반응은 bridge 노출과 space 간 이탈 가능성 증가로 읽는다.
- `stable_local` 숙성은 thickening count보다 boundary durability를 먼저 본다.

원칙:

- 현재 상태와 전이 이력은 분리 저장한다.
- 상태 변경은 event log에 append-only로 남긴다.
- 직접 덮어쓰기보다 전이 기록을 우선한다.
