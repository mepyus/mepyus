# phase2 history replay trace minimum read shell v1

## package status

complete for this turn

## files created / changed

- [operating_ui_history.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_history.py)
- [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)
- [phase2_history_replay_trace_minimum_read_shell_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase2_history_replay_trace_minimum_read_shell_v1.md)

## 1. minimum shell structure

The new adjacent surface is available as:

- `/operating-ui-history`

It exposes the minimum read-oriented sections only:

- `Recent Runs / Snapshots`
- `Activity Cluster List`
- `Trace Reading Panel`
- `Replayable State Preview`
- `Return / Open in phase1`

The shell stays read-oriented. It does not introduce execution controls, rerun controls, or dashboard-style command behavior.

## 2. reading units used

The shell renders the baseline reading units as follows:

- `run_snapshot_vm`
  - built from `engine_state_latest` items
  - used in `Recent Runs / Snapshots`
- `activity_cluster_vm`
  - translated from history timeline items, or falls back to one latest-linked cluster when history is sparse
  - used in `Activity Cluster List`
- `trace_entry_vm`
  - translated into operator-facing units like `trigger and reason`, `state change read`, `evidence link count`, `state note`
  - used in `Trace Reading Panel`
- `replayable_state_vm`
  - view-level reread of a selected or latest-linked canonical slice
  - used in `Replayable State Preview`

## 3. sources connected

Connected sources:

- `runtime/views/engine_state_latest`
- `runtime/state/engine_state_history/<asset_id>.jsonl`
- `runtime/views/engine_state_update_events/<asset_id>.json` when available

Not yet connected:

- broader compaction layers
- richer multi-asset replay logic
- any execution or rerun path

Reason:

- this turn is a minimum read shell only
- it should stay thin and honest before any richer time-axis work

## 4. degraded / empty honesty

The shell distinguishes:

- `no runs yet / latest snapshot source unavailable`
- `partial trace only / no activity clusters loaded`
- `trace reading unavailable / partial source only`
- `replay preview unavailable`

When history is sparse but latest exists, the surface does not fake a rich trace. It creates a `latest-linked cluster` and marks the trace as partial.

## 5. phase1 linkage

The surface links back to phase1 only through explicit links:

- top-level `open current context in phase1`
- panel-level `return / open in phase1`

These links pass only `asset_id` in the URL.

They do not mutate phase1 shared spine or embed history behavior into phase1.

## 6. source sparsity / current limitations

- update-event helper data may be missing
- some latest snapshots have little or no lineage depth
- activity clusters are currently thin translations of recent history items, not a mature compaction model
- replay preview is a rereadable state slice, not a replay engine

## 7. next candidates

- add one thin adapter/probe check for `history sparse but latest available` versus `source unavailable`
- evaluate whether first implementation should read compacted history when recent history count grows
