[[A]] [[OBJ:process_console_history_drilldown_v1]] [[SEM:history_drilldown_spec_for_process_console_lineage_surface]]

# process_console_history_drilldown_v1

## 1. purpose

- 이번 step의 목적은 process console이 latest canonical state만 보여주는 표면에서 멈추지 않고, 현재 상태가 어떤 trigger / evidence / changed fields를 거쳐 형성되었는지 시간축으로 읽게 하는 것이다.
- 기본 표면은 계속 latest-first를 유지하고, history는 drill-down lineage surface로 붙는다.

## 2. read sources

- primary history source:
  - `runtime/state/engine_state_history/<asset_id>.jsonl`
- optional helper source:
  - `runtime/views/engine_state_update_events/<asset_id>.json`
- latest link source:
  - `runtime/views/engine_state_latest/<asset_id>.json`

## 3. code split

- history loader:
  - [process_console_history_loader.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_history_loader.py)
- history selectors:
  - [process_console_history_selectors.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_history_selectors.py)
- process console builder:
  - [builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py)
- process console render:
  - [render.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/render.py)

## 4. lineage surface structure

### A. HistorySummaryStrip

- state panel 하단에서 최근 update count, latest trigger, latest reason, latest change kind를 얇게 보여준다.
- latest-first surface를 유지하면서도 현재 상태가 형성된 lineage가 있음을 드러낸다.

### B. LatestLineageLink

- `current latest formed from recent N updates` 식의 요약으로 latest와 최근 history chain을 바로 연결한다.
- latest trigger / reason / updated_at을 함께 보여준다.

### C. HistoryDrilldownPanel

- recent history timeline을 최신순으로 보여준다.
- 각 item은 `updated_at`, `update_trigger_type`, `update_reason`, `changed_fields`, `evidence_refs`, `state_notes`, `schema_version`, `canonical snapshot`, `experimental_namespace presence`를 가진다.
- default는 recent 10개 이하, 이후는 overflow count로 다룬다.

### D. HistoryTimelineItem

- trigger badge:
  - `backfill`
  - `runtime`
  - `recompute`
  - `manual`
- changed fields가 없으면 `provenance_only_update`로 읽는다.
- expand 시 canonical snapshot과 evidence refs를 보여주되 experimental namespace는 presence만 보여주고 내용은 기본 숨김 유지한다.

## 5. changed_fields rule

- history record 자체에 changed field가 없더라도 selector에서 계산한다.
- 계산 방식:
  - 인접 이전 record와 canonical 8필드 비교
  - 배열 field는 set-like 비교 허용
- first record:
  - bootstrap/backfill formation이므로 canonical 8필드 전체를 changed로 본다.
- no canonical drift:
  - `changed_fields = []`
  - derived label은 `provenance_only`

## 6. derived labels

- `canonical_change`
- `provenance_only`
- `traceability_change`
- `grounding_change`
- `emergence_change`
- `blocker_change`

주의:
- 이 값들은 UI 요약용 derived label이다.
- canonical schema field로 저장하지 않는다.

## 7. guard rules

- latest는 계속 primary read source다.
- history는 drill-down only다.
- malformed item은 가능한 범위에서 skip / warning 처리하고 패널 전체 crash는 막는다.
- evidence refs 누락이 있어도 panel 전체는 유지한다.
- experimental namespace는 기본 숨김 처리다.

## 8. one-line lock

> `process_console_history_drilldown_v1`는 current latest state를 정지된 결과가 아니라 trigger, reason, evidence, changed fields를 가진 lineage로 읽게 만드는 시간축 operating surface 규정이다.
