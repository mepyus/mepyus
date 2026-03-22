# Pressure-Aware Cell Branching

## Decision

같은 family에서 생긴 seed라도 pressure signature가 다르면 기존 `space_cell`에 합치지 않고 새 cell을 연다.
pressure signature가 충분히 같으면 기존 family cell을 확장한다.

## Current rule

- pressure signature는 각 axis의 이름과 strength bucket으로 만든다.
- bucket은 `low`, `mid`, `high` 세 단계다.
- 같은 family material을 포함한 기존 cell 중 signature가 같은 것이 있으면 그 cell을 확장한다.
- signature가 다르거나 기존 family cell이 없으면 새 candidate cell을 만들고 branch event를 남긴다.

## Why

- family 일치만으로 cell을 합치면 조기 수렴이 일어난다.
- pressure를 필드 저장으로만 끝내지 않고 실제 cell path에 영향을 주게 해야 한다.
- 하지만 초기에 너무 복잡한 clustering 규칙을 넣으면 다시 회귀한다.

## Contract check memo

- formation-first: 유지
- anti-collapse: 강화
- cell integrity: 유지
- core/reader separation: 유지
- multi-local-space openness: 강화

## Follow-up risk

- 현재 bucket 단위는 거칠다.
- 다음 단계에서 local space criteria를 넣을 때 pressure signature와 cell recurrence를 함께 봐야 한다.
