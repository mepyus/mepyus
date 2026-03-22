# Report Issuance Policy

## Decision

workspace report는 항상 쓰는 것이 아니라, 읽을 가치가 있는 runtime 상태가 있을 때 발행한다.

## Current rule

- `hybrid` 또는 `legacy_only` 상태면 발행 대상이다.
- core formation state가 하나라도 있으면 발행 대상이다.
- reactive manifest가 하나라도 있으면 발행 대상이다.

## Why

- 텅 빈 runtime에 보고서를 남기는 것은 의미가 약하다.
- 반대로 core와 legacy가 함께 있거나 반응형 상태가 있으면 읽을 가치가 크다.

## Follow-up risk

- 현재 정책은 단순 카운트 기반이다.
- 이후에는 변화량이나 최근 event 존재도 발행 조건에 넣을 수 있다.
