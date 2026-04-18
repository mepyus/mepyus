# phase transition and hold rule v0

## 1. 목적

이 규칙은 `runtime/current_phase.json`을 선언값이 아니라 관찰된 신호 조합에 따라 전환되거나 hold 되는 상태 판정 장치로 다루기 위한 최소 규칙이다.

핵심은 phase를 억지로 바꾸지 않고, 신호가 충분할 때만 전환하며, 모호하면 hold를 구조적으로 허용하는 것이다.

## 2. 입력 신호

최소 입력 신호는 4개다.

- `continuity`
  - 현재 활성 latent line / breadcrumb / phase와의 연속성
- `residue`
  - 기존 구조로 설명되지 않고 남는 잔차
- `tension`
  - latent line / rule / phase 간 충돌 강도
- `sufficiency`
  - 지금 이 턴을 잠가도 되는 충분성

## 3. phase 종류

- `thickening`
- `widening`
- `closure`
- `hold`

## 4. 판정 원칙

- phase는 선언이 아니라 판정 결과다.
- 전환보다 hold가 먼저 보호되어야 한다.
- 단일 신호로 phase를 바꾸지 않는다.
- 전환 / 보류 이유는 모두 흔적으로 남아야 한다.

## 5. 현재 적용 결과

이번 preflight에서는 `space_reading` 기준으로 다음 active latent line이 먼저 잡혔다.

- `pre_read_eye`
- `raw_return_preservation`

판정 신호는 다음과 같다.

- `continuity = high`
- `residue = medium`
- `tension = low`
- `sufficiency = medium`

그래서 현재 phase는 `thickening`으로 내려갔다.

### 왜 hold가 아니었는가

- tension이 실제로 높지 않았다.
- boundary-only variation은 이미 watch rule과 breadcrumb로 설명 가능했다.
- 따라서 hold보다 기존 latent line을 더 두껍게 읽는 상태가 맞았다.

### 왜 widening이나 closure가 아니었는가

- residue가 아직 완전히 사라지지 않았다.
- sufficiency도 아직 high가 아니다.
- 현재는 정리/잠금보다 기존 선을 강화하는 쪽이 맞다.

## 6. hold 우선 보호 규칙

아래 경우에는 phase 전환보다 hold를 우선한다.

- tension = high
- active latent line 2개 이상이 강하게 충돌
- residue는 큰데 widening 방향이 불명확
- sufficiency가 낮고 closure 압력만 외부에서 강함
- 전환 이유를 명확히 설명할 수 없음

## 7. 무엇이 기록되었는가

- `runtime/current_phase.json`
- `runtime/manifests/phase_decision_log.jsonl`
- `runtime/preflight_last_decision.json`
- `runtime/breadcrumbs.jsonl`

## 8. 앞으로의 체크 조건

- 같은 latent line이 다음 reread에서도 반복되는가
- residue가 high로 올라가는가
- 새 관찰이 기존 candidate로 접히지 않는가
- hold가 정말 필요한 tension인지, 아니면 thickening이 맞는지

## 9. 한 줄 결론

> phase는 신호 조합에서만 전환되며, 지금은 hold가 아니라 `thickening`이 맞고, hold는 tension이 실제로 높아질 때만 우선 보호된다.

