# 2026-04-11 Canonical Operating Flow Brief

## verdict

- canonical flow locked / not yet locked: `not yet locked`

## why

- 입력 축은 실제 canonical entry path가 보인다. `memo` 입력은 stage0 handoff를 거쳐 material, trace, local space까지 간다.
- surface 축도 실제 canonical operating surface 후보가 보인다. `process-console`이 canonical state read path이고, `operating-ui-live`와 `operating-ui-phase1`은 그 위에 얹힌 파생 surface다.
- 하지만 입력 상태화 축과 surface 축 사이에 직접 canonical state append가 없다. 즉 `live_input -> EngineStateRecord -> process-console`이 아직 하나의 선으로 잠기지 않았다.
- 운영 자산 축은 `weekend_pilot_first_loop_live_bundle`를 현재 canonical pilot seam으로 명시하고 있으나, 이 축도 input state 축과 직접 합쳐지지 않았다.
- 결론적으로 지금 워크트리는 하나의 운영선이라기보다, 강한 두 개의 부분선과 문서화된 pilot seam이 병렬로 열린 상태다.

## result 1. canonical operating flow 1장

### current best canonical flow

- entry:
  - `POST /api/ingest`
  - [app/core/runtime/viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)
  - [app/core/runtime/live_input.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input.py)
- state transition:
  - `memo` only
  - `build_handoff_materials(...)`
  - `service.ingest_material_with_role(...)`
  - `service.register_trace(...)`
  - `form_live_input_local_space(...)`
  - [app/core/runtime/stage0_handoff.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/stage0_handoff.py)
  - [app/core/runtime/live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)
- visible surface:
  - current canonical state surface is not fed by the ingest path above
  - actual state surface path is `EngineStateStore -> /process-console -> /operating-ui-live -> /operating-ui-phase1`
  - [app/core/state_store/engine_state_store.py](/Users/sungsookim/universe/vectorfl_replica/app/core/state_store/engine_state_store.py)
  - [app/runtime/process_console_view/builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py)
  - [app/runtime/operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)
  - [app/runtime/operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- supervisor checkpoint:
  - `runtime/manifests/vectorfl_paper_pilot_current_v0.json`
  - `runtime/contracts/vectorfl_paper_weekend_pilot_status_board_v0.json`
  - `docs/reports/vectorfl_paper_weekend_live_supervisor_report_v1.md`
- contract anchor:
  - weekend live chain around translated packet, runtime write-back, reinjection, governance gate
  - [runtime/manifests/vectorfl_paper_weekend_live_runtime_write_back_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/vectorfl_paper_weekend_live_runtime_write_back_v0.json)
  - [runtime/contracts/vectorfl_paper_weekend_live_translated_work_packet_v3.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_weekend_live_translated_work_packet_v3.json)
  - [runtime/contracts/vectorfl_paper_weekend_live_governance_gate_note_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_weekend_live_governance_gate_note_v0.json)
- report return:
  - `runtime_write_back -> reopen_case -> supervisor_report`
  - [docs/reports/vectorfl_paper_weekend_live_runtime_write_back_report_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/vectorfl_paper_weekend_live_runtime_write_back_report_v0.md)
  - [docs/reports/vectorfl_paper_weekend_live_reopen_report_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/vectorfl_paper_weekend_live_reopen_report_v0.md)
  - [docs/reports/vectorfl_paper_weekend_live_supervisor_report_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/vectorfl_paper_weekend_live_supervisor_report_v1.md)

### compressed sentence

- `user memo input -> stage0 handoff bridge-ready candidates -> material/trace/local space -> separate canonical engine-state surface via process-console -> operating-ui live/phase1 -> weekend pilot supervisor seam -> runtime write-back/reopen/governance reports`

## result 2. 핵심 파일 shortlist

### input SSOT

- [app/core/runtime/live_input.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input.py)
- [app/core/runtime/stage0_handoff.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/stage0_handoff.py)
- [app/core/runtime/live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)

### state SSOT

- [app/core/states.py](/Users/sungsookim/universe/vectorfl_replica/app/core/states.py)
- [app/core/models/entities.py](/Users/sungsookim/universe/vectorfl_replica/app/core/models/entities.py)
- [app/core/state_store/engine_state_store.py](/Users/sungsookim/universe/vectorfl_replica/app/core/state_store/engine_state_store.py)
- [app/runtime/engine_state_runtime_update_bridge.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/engine_state_runtime_update_bridge.py)

### surface SSOT

- [app/core/runtime/viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)
- [app/runtime/process_console_view/builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py)
- [app/runtime/operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)
- [app/runtime/operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [app/runtime/operating_ui_history.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_history.py)

### contract/report SSOT

- [runtime/manifests/vectorfl_paper_pilot_current_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/vectorfl_paper_pilot_current_v0.json)
- [runtime/contracts/vectorfl_paper_weekend_pilot_status_board_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_weekend_pilot_status_board_v0.json)
- [runtime/manifests/vectorfl_paper_weekend_live_runtime_write_back_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/vectorfl_paper_weekend_live_runtime_write_back_v0.json)
- [docs/reports/vectorfl_paper_weekend_live_supervisor_report_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/vectorfl_paper_weekend_live_supervisor_report_v1.md)

## result 3. 살아 있는 것 / 후보인 것 분리표

### alive

- `memo -> stage0 handoff -> material/trace/local space`
- `EngineStateStore -> process-console`
- `/process-console -> /operating-ui-live`
- `weekend_pilot_first_loop_live_bundle -> runtime_write_back -> reopen_case -> supervisor_report`

### connected but thin

- `/operating-ui-live -> /operating-ui-phase1 -> /operating-ui-history`
- `runtime/manifests/vectorfl_paper_pilot_current_v0.json` as canonical pilot bridge
- `EngineStateRuntimeUpdateBridge` as runtime evidence update path

### generated only

- [app/runtime/vectorfl_operable_surface_set.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/vectorfl_operable_surface_set.py) and most of [runtime/views/vectorfl_operable_surface](/Users/sungsookim/universe/vectorfl_replica/runtime/views/vectorfl_operable_surface)
- many `proper`, `actual_export`, `selection`, `board sections`, `page tree` assets that are named in `pilot_current` but not part of the shortest live loop
- most docs/reports/specs that describe future absorption or broader UI shape rather than the currently exercised loop

### hold

- `live_input -> EngineStateRecord append_state` direct lock
- `EngineStateRecord` as ingest-time canonical output
- `vectorfl_operable_surface` 101-file set as primary operator surface
- `actual_export` branch beyond stub/swap-ready status

## result 4. 오늘 이후 확장 금지선

### 지금 더 만들면 안 되는 영역

- new pages under `runtime/views/vectorfl_operable_surface`
- new `contracts`, `manifests`, and `reports` for paper pilot variants
- additional operating UI branches beyond `process-console`, `live`, `phase1`, `history`

### 먼저 잠가야 하는 영역

- whether canonical state starts at ingest or remains a separate evaluation/update lane
- one primary operator surface among `process-console`, `operating-ui-live`, `operating-ui-phase1`
- one supervisor entrypoint among `pilot_current`, `status_board`, `supervisor_report`

### 다음 확장은 무엇이 정렬된 뒤에만 가능한가

- `live_input` output must either append canonical engine state directly or explicitly hand off to the runtime update bridge
- one canonical surface path must be declared
- one pilot asset chain must be declared as the only supervision path

## axis readout

### A. input-state axis

- canonical entry path exists only for `memo`
- stage0 handoff unit is `bridge-ready candidate` from `build_handoff_materials(...)`
- material / trace / local space split is decided inside [app/core/runtime/live_input.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input.py) and [app/core/runtime/live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)
- `EngineStateRecord` is not emitted here

### enum / record usage split

- actually used on state surface:
  - `PacketTexture`
  - `GroundingStatus`
  - `EmergenceStatus`
  - `CarryoverRisk`
  - `MaturationState`
  - `TraceabilityStatus`
  - `ComparisonMemoryReason`
  - `GateBlockerSummary`
  - `EngineStateRecord`
- but used in separate state-store lane, not the ingest lane:
  - [app/core/state_store/engine_state_store.py](/Users/sungsookim/universe/vectorfl_replica/app/core/state_store/engine_state_store.py)
  - [scripts/backfill_engine_state_v1.py](/Users/sungsookim/universe/vectorfl_replica/scripts/backfill_engine_state_v1.py)
  - [app/runtime/engine_state_runtime_update_bridge.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/engine_state_runtime_update_bridge.py)

### B. operable surface axis

- shortest canonical surface path today:
  - `/process-console`
  - `/operating-ui-live`
  - `/operating-ui-phase1`
  - `/operating-ui-history`
- priority surface today:
  - `/process-console` for canonical state read
  - `/operating-ui-phase1` for broader operating composition
- non-core today:
  - `/operating-ui-demo`
  - `/search`
  - `/memory`
  - `/similar`
  - almost all of `vectorfl_operable_surface`

### C. operating asset axis

- current baseline is explicitly `weekend_pilot_first_loop_live_bundle`
- canonical asset set today:
  - [runtime/manifests/vectorfl_paper_pilot_current_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/vectorfl_paper_pilot_current_v0.json)
  - [runtime/contracts/vectorfl_paper_weekend_pilot_status_board_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_weekend_pilot_status_board_v0.json)
  - [runtime/manifests/vectorfl_paper_weekend_live_runtime_write_back_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/vectorfl_paper_weekend_live_runtime_write_back_v0.json)
  - [docs/reports/vectorfl_paper_weekend_live_supervisor_report_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/vectorfl_paper_weekend_live_supervisor_report_v1.md)
- real contract-manifest-report chain:
  - translated work packet
  - runtime write-back manifest
  - reopen case manifest
  - supervisor report

## locked path

- input:
  - `POST /api/ingest -> ingest_live_input -> memo stage0 handoff -> material/trace/local space`
- surface:
  - `EngineStateStore latest/history -> /process-console -> /operating-ui-live -> /operating-ui-phase1`
- supervision:
  - `runtime/manifests/vectorfl_paper_pilot_current_v0.json -> runtime/contracts/vectorfl_paper_weekend_pilot_status_board_v0.json -> docs/reports/vectorfl_paper_weekend_live_supervisor_report_v1.md`
- contract/report:
  - `translated_work_packet -> runtime_write_back -> reopen_case -> supervisor_report`

## unstable area

- ingest path and engine state path are split
- `vectorfl_operable_surface` competes with `process-console/operating-ui-*` as an apparent parallel surface family
- `pilot_current` names many future-facing assets, so canonical supervision entry can still drift

## hold area

- `vectorfl_operable_surface` expansion
- `proper` and `actual_export` branch broadening
- any new docs that describe future states before the current state path is locked

## next expansion gate

- next expansion is allowed only after one decision is made and implemented:
  - `EngineStateRecord` becomes either the canonical output of `live_input` or an explicitly downstream post-ingest evaluator with one declared handoff point
