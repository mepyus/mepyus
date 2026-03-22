# Intake Role Helper Policy

## Decision

formation role은 강한 ontology로 박지 않고, intake helper를 통해 `material.metadata.formation_role`에 얇게 기록한다.

## Current rule

- `source_type`은 그대로 유지한다.
- `formation_role`은 optional metadata로만 기록한다.
- ingest event payload에도 같은 role을 남긴다.

## Why

- 지금 단계에서 role은 읽기와 추적을 돕는 최소 신호면 충분하다.
- 별도 enum이나 강한 schema로 굳히면 taxonomy가 너무 빨리 닫힐 수 있다.

## Follow-up risk

- role 값 검증은 아직 느슨하다.
- 다음 단계에서 intake policy 문서나 helper validation을 추가할 수 있다.
