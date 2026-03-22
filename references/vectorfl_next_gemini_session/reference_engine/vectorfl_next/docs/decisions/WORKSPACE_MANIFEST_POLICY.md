# Workspace Manifest Policy

## Decision

workspace 수준에서 `runtime`의 core 형성과 legacy 공존 상태를 한 번에 읽는 manifest를 남길 수 있어야 한다.

## Current rule

- `workspace_manifest`는 core object 수를 센다.
- reactive manifest 수를 센다.
- legacy runtime 경로를 함께 나열한다.
- 전체 상태를 `empty`, `legacy_only`, `hybrid`, `core_only` 중 하나로 판정한다.

## Why

- 지금 workspace는 새 formation core와 legacy 흔적이 함께 존재한다.
- 이 공존 상태 자체가 중요한 material이다.
- migration 이전에 현재 지형을 읽을 수 있어야 한다.

## Output scope

- core counts
- manifest counts
- legacy paths
- coexistence status

## Follow-up risk

- 아직 이 manifest는 보고서 수준이며 migration action은 수행하지 않는다.
- 다음 단계에서 workspace report를 logs 또는 reports와 연결할 수 있다.
