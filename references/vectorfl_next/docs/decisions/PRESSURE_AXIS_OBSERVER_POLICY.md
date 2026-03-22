# Pressure Axis Observer Policy

## Decision

observer는 pressure signature 문자열뿐 아니라 axis별 bucket 분포도 읽을 수 있어야 한다.

## Current rule

- 반응 이벤트에 연결된 pressure profile의 axis를 모은다.
- 각 axis에 대해 `low`, `mid`, `high` bucket 분포를 센다.
- 이 출력은 observer용이며 코어를 바꾸지 않는다.

## Why

- signature 한 줄만으로는 어떤 압력 축이 많이 작동했는지 읽기 어렵다.
- axis 분포를 보면 temporal/session/tone/recurrence 같은 축의 작동 흔적을 빠르게 볼 수 있다.

## Follow-up risk

- bucket은 여전히 거칠다.
- 다음 단계에서 axis 조합 패턴이나 transition frequency를 읽을 수 있다.
