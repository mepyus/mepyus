# phase2 operating history replay trace surface baseline lock v1

## package status

complete for this turn

## files created

- [phase2_operating_history_replay_trace_surface_baseline_lock_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/phase2_operating_history_replay_trace_surface_baseline_lock_v1.md)
- [phase2_operating_history_replay_trace_surface_baseline_lock_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase2_operating_history_replay_trace_surface_baseline_lock_v1.md)

## 1. why this is phase2 priority 1

This candidate is phase2 priority 1 because it answers the clearest post-phase1 pressure without reopening frozen phase1:

- phase1 is present-tense and intentionally thin
- time-axis rereading pressure is real
- existing repo history/lineage material already supports this direction

Compared with other adjacent candidates, this one has the clearest need and the cleanest boundary from phase1.

## 2. why this cannot be handled as phase1 internal expansion

If phase1 absorbs history / replay / trace reading:

- `Operating` stops being thin observation
- phase1 risks dashboard bloat
- current-state reading and time-axis reading get mixed again
- phase1 shared-spine semantics become harder to preserve

That is why this must remain an adjacent surface rather than a phase1 refinement.

## 3. minimum reading units chosen

The minimum reading units were locked as:

- `run snapshot`
- `activity cluster`
- `trace entry`
- `replayable state`

These are enough to express time-axis rereading without overbuilding a giant history system.

## 4. replay / trace / history guardrails

- `history`
  - read-oriented time-axis companion, not live operating replacement
- `replay`
  - view-level reread only, not rerun, reenactment, or simulation
- `trace`
  - translated operator-facing reading unit, not raw audit dump or debug console

These guardrails are the main reason to lock baseline before implementation.

## 5. open questions before implementation

- should first implementation read history jsonl alone or combine it with update-event helper views
- how much history compaction should be assumed at first read
- which explicit phase1 handoff anchor is best as the default jump target

## 6. why saved-path curation stays parked

The `saved-path curation surface` remains parked because its pressure is still more anticipatory than observed.

The need is plausible, but current saved-path accumulation evidence is thinner than the already visible time-axis reading pressure. Promoting curation now would risk reopening memory semantics too early.

## 7. package completeness

This package is complete for its stated goal.

It does not implement the surface. It locks the baseline so later implementation cannot drift into:

- phase1 operating expansion
- recommendation semantics
- execution/rerun semantics
- dashboard overgrowth
