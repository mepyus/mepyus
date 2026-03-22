# Reentry Seed Formation

## Decision

같은 `family_id`의 material이 다시 들어오면 기존 seed를 갱신하지 않는다.
대신 새로운 `point_seed`를 `reentering` 상태로 생성하고, 이전 seed들을 `lineage_refs`로 연결한다.

## Why

- 같은 family라도 압력 구성이 달라질 수 있다.
- 기존 seed를 덮어쓰면 formation path 변화가 사라진다.
- 재진입은 dedup이 아니라 새로운 형성 경로 개방으로 다뤄야 한다.

## Current rule

- family lookup은 material의 `family_id`를 기준으로 수행한다.
- 해당 family에 연결된 기존 seed id를 모아 새 seed의 `lineage_refs`에 넣는다.
- 새 seed는 항상 별도 id를 가진다.
- 이전 seed의 상태는 자동 변경하지 않는다.

## Contract check memo

- formation-first: 유지
- anti-collapse: 유지
- cell integrity: 아직 영향 없음
- core/reader separation: 유지
- multi-local-space openness: 유지

## Follow-up risk

- family 범위가 너무 넓으면 reentry seed lineage가 과잉 연결될 수 있다.
- 다음 단계에서 pressure-aware branching 규칙과 함께 family granularity를 다시 검토해야 한다.
