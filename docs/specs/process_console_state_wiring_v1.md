[[A]] [[OBJ:process_console_state_wiring_v1]] [[SEM:wiring_spec_for_canonical_state_read_path_in_process_console]]

# process_console_state_wiring_v1

## 1. purpose

- 이번 wiring의 목적은 검증된 canonical operating state layer를 process console의 실제 read path에 연결하는 것이다.
- 이 단계의 본체는 result map이 아니라 state-reading operating surface다.

## 2. primary read source

- asset-specific latest:
  - `runtime/views/engine_state_latest/<asset_id>.json`
- list/filter/sort source:
  - `runtime/views/engine_state_latest/index.json`

## 3. wired components

### A. HeaderBadgeBar

- source:
  - asset-specific latest JSON
- shown fields:
  - `packet_texture`
  - `grounding_status`
  - `emergence_status`
  - `carryover_risk`
  - `maturation_state`
  - `traceability_status`

### B. AssetRail

- source:
  - latest index + per-asset latest hydration
- supports:
  - filter by `packet_texture`
  - filter by `grounding_status`
  - filter by `emergence_status`
  - filter by `carryover_risk`
  - filter by `maturation_state`
  - `traceable_only`
  - sort by `updated_at`
  - sort by `packet_texture`
  - sort by `maturation_state`
  - sort by `carryover_risk`
  - sort by `emergence_status`

### C. StatePanel

- source:
  - selected asset latest JSON
- shows:
  - canonical 8-field subset in UI priority order
  - `state_notes`
  - `evidence_refs`
  - `comparison_memory_reason`
  - `gate_blocker_summary`

### D. CompareEntry

- source:
  - latest index + selected latest JSON
- compare keys:
  - same `packet_texture`
  - same `carryover_risk`
  - overlapping `comparison_memory_reason`
  - overlapping `gate_blocker_summary`
  - compressed family pair
  - breathing contrast pair

### E. LatestStatePreview

- source:
  - selected asset latest JSON
- shows:
  - `packet_texture`
  - `maturation_state`
  - `traceability_status`
  - `updated_at`

## 4. guard rules

- `experimental_namespace` hidden by default
- top-level naming-heavy contamination never rendered as canonical state
- missing latest state -> `state_unavailable` fallback
- history is not the primary read path

## 5. service split

- loader:
  - [process_console_state_loader.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_state_loader.py)
- selectors:
  - [process_console_state_selectors.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_state_selectors.py)
- view builder:
  - [builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py)
- html render:
  - [render.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/render.py)
- server route:
  - [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)

## 6. one-line lock

> `process_console_state_wiring_v1`는 canonical operating state를 process console의 실제 read path에 연결해, 자산 클릭 시 결과 해석보다 먼저 state-first surface가 열리게 만드는 wiring 규정이다.
