# Runtime Manifest Policy

## Decision

반응형 공간 상태는 core 저장과 별도로 manifest 요약을 남긴다.

## Runtime layout

- `runtime/core/materials`
- `runtime/core/traces`
- `runtime/core/pressure_profiles`
- `runtime/core/point_seeds`
- `runtime/core/space_cells`
- `runtime/core/local_spaces`
- `runtime/core/bridge_traces`
- `runtime/events/formation_events.jsonl`
- `runtime/manifests/reactive_spaces`
- `runtime/manifests/bridges`

## Why

- core record는 세부 이력을 보존한다.
- manifest는 현재 반응형 공간 상태를 빠르게 재읽고 재유입하기 쉽게 만든다.
- 공간 엔진의 산출물 자체가 다음 material이 될 수 있어야 한다.

## Current manifest scope

- local space manifest
  - state
  - cell ids
  - bridge trace refs
  - pressure profile id
  - shared boundary strength
  - reaction counts
  - cell states
- cell manifest
  - state
  - pressure profile id
  - material / trace / seed counts
  - boundary strength
  - reaction counts
  - cohesion note
- bridge manifest
  - state
  - source / target local space
  - trace ref count
  - note

## Follow-up risk

- 아직 runtime 루트의 기존 placeholder 디렉터리와 완전한 migration은 하지 않았다.
- 다음 단계에서 실제 workspace runtime bootstrap도 정리해야 한다.
