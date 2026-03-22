# Runtime Bootstrap Policy

## Decision

실제 workspace `runtime/`는 실행 시 contract-aligned layout으로 자동 부트스트랩한다.

## Current rule

- `FormationService` 시작 시 `runtime/core`, `runtime/events`, `runtime/manifests`, `runtime/reports`, `runtime/tmp`를 보장한다.
- 기존 placeholder 또는 legacy 경로는 지우지 않고 탐지 대상으로만 남긴다.
- migration 전에 legacy 흔적을 없애지 않는다.

## Why

- 작업 중인 runtime을 파괴하지 않고 새 기준을 점진적으로 세워야 한다.
- legacy 흔적도 이후 material 또는 reference가 될 수 있다.

## Legacy detection scope

- `runtime/bridges/manifests`
- `runtime/bridges/traces`
- `runtime/events/cells`
- `runtime/events/local_spaces`
- `runtime/events/seeds`
- `runtime/spaces/adjacent_candidates`
- `runtime/spaces/reference_center`

## Follow-up risk

- 아직 automatic migration은 없다.
- 다음 단계에서 migration report 또는 workspace manifest를 추가해야 한다.
