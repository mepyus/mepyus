# Workspace Report Policy

## Decision

workspace manifest와 별도로 사람이 빠르게 읽을 수 있는 `workspace_report.md`를 `runtime/reports`에 남길 수 있어야 한다.

## Current rule

- report는 workspace manifest를 바탕으로 생성한다.
- coexistence status, core counts, manifest counts, legacy paths를 보여준다.
- process summary와 maturation signals도 함께 보여준다.
- migration 또는 삭제는 수행하지 않는다.
- 실제 발행 판단은 `REPORT_ISSUANCE_POLICY`를 따른다.

## Why

- manifest는 구조적으로 읽기 좋다.
- report는 사람이 현재 지형을 빠르게 판단하기 좋다.
- 둘 다 이후 material이 될 수 있다.
- 공간이 어떻게 익고 있는지도 report에서 직접 읽을 수 있어야 한다.

## Follow-up risk

- 아직 logs와 reports를 통합 요약하지 않는다.
- 다음 단계에서 report issuance policy를 둘 수 있다.
