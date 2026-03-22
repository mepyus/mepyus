# Multi-Local Coexistence Policy

여러 local space는 하나로 collapse하지 않고도 shared terrain pressure 아래 함께 존재할 수 있어야 한다.

현재 coexistence mode:

- `isolated_local`
- `pressure_adjacent`
- `pressure_resonant`
- `bridge_adjacent`
- `terrain_resonant`
- `terrain_shared`

핵심 원칙:

- 같은 pressure signature를 가진다고 해서 local spaces를 자동 병합하지 않는다.
- pressure axis가 일부 겹친다고 해서 local spaces를 자동 병합하지 않는다.
- bridge가 있다고 해서 local spaces를 하나의 space로 취급하지 않는다.
- pressure adjacency와 bridge adjacency가 함께 있을 때만 `terrain_shared`로 읽는다.
- exact signature는 아니어도 pressure axis가 부분 공진하면 `pressure_resonant` 또는 `terrain_resonant`로 읽을 수 있다.

의도:

- multi-local terrain을 merge 이전의 넓은 공존 지형으로 읽는다.
- local space의 독립성을 유지하면서도 더 큰 terrain pressure를 표현한다.
- exact signature 일치가 아니어도 느슨한 terrain resonance를 읽어 공간 스케일을 좁히지 않는다.

금지 기준:

- coexistence mode를 merge trigger처럼 쓰지 않는다.
- terrain shared를 상위 절대 공간처럼 읽지 않는다.
