# Space Maturation Evidence Policy

숙성은 gate가 아니라 evidence layer로 읽는다.

핵심 원칙:

- `local_space`와 `bridge`는 상태 외에 별도의 `maturation_evidence`를 가진다.
- evidence는 통과/탈락 판정기가 아니라 공간이 어떻게 익어가고 있는지 보여주는 누적 흔적이다.
- 시간은 여기서도 엄격한 심사 기준이 아니라 `time_aged` 같은 증거 신호로만 남는다.

현재 local-space evidence 신호:

- `boundary_aged`
- `reentry_aged`
- `bridge_aged`
- `thickening_present`

현재 bridge evidence 신호:

- `bridge_exposed`
- `repeated_support`
- `time_aged`
- `durably_held`

현재 terrain-climate evidence 신호:

- `multi_local_climate`
- `shared_axis_climate`
- `distributed_axis_climate`
- `bridge_exposed_climate`
- `time_aged_climate`
- `durably_held_climate`
- `boundary_supported_climate`

현재 terrain-memory evidence 신호:

- `local_memory_present`
- `multi_local_memory`
- `bridge_memory_present`
- `persistent_bridge_memory`
- `durable_return_memory`
- `time_spaced_memory`
- `axis_memory`

의도:

- 공간이 너무 좁은 threshold 모델로 다시 수렴하지 않게 한다.
- 숙성을 더 넓은 스케일의 공간 변화로 읽는다.

금지 기준:

- evidence를 새 hard state처럼 다루지 않는다.
- evidence가 append-only event history를 대체하게 두지 않는다.
