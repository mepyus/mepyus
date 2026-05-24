# Plan from Space Position Map Seed v0

## Status

```yaml
status: position_map_seed_candidate
date: 2026-05-06
baseline_lock: false
automation: false
scope: plan_from_space_session_convergence_prevention
```

## Purpose

This seed gives future small Session Space Anchors compact position values.

It is a seed, not a completed map.

## Position Values

### PV-001 Plan Basis Gate

```yaml
position_id: PV_PLAN_BASIS_GATE
asset_family: line / axis / lens / camera reference
authority_state: candidate_reference
maturity_state: operating_anchor_candidate
active_line: Plan from Space / Session Convergence Prevention
axis_tension: model-default planning vs space-grounded planning
camera_position: external tool plan mode
lens_gate: Plan Basis present
worker_boundary: external tool must not plan first
return_shape: Plan Basis + bounded plan + Return-to-Space
watch_signal: decorative_lacl_watch
reentry_trigger: tool returns a plan without space grounding
do_not_infer: no baseline, no universal workflow
```

Use:

When a tool gives a plan immediately, ask for Plan Basis first.

### PV-002 Broad-But-Bounded Package

```yaml
position_id: PV_BROAD_BOUNDED_PACKAGE
asset_family: package / candidate reference context
authority_state: candidate_reference
maturity_state: reusable_setting_candidate
active_line: Plan from Space / Session Convergence Prevention
axis_tension: small split vs broad-but-bounded package
camera_position: user relay burden
lens_gate: package sizing justified
worker_boundary: worker may include internal check but not multiply sessions by default
return_shape: bounded package with issue log and movement record
watch_signal: session_convergence_watch
reentry_trigger: analysis/design/execution/verification/review split appears by default
do_not_infer: no permission to expand scope or skip hard boundary
```

Use:

When a model splits safe-looking work into many sessions without a blocking reason.

### PV-003 Raw Trace Boundary

```yaml
position_id: PV_RAW_TRACE_BOUNDARY
asset_family: worker evidence / Gemini process record
authority_state: raw_trace
maturity_state: raw_record
active_line: External Tool Boundary / Raw Trace
axis_tension: raw trace vs interpreted memory
camera_position: provenance integrity
lens_gate: Return-to-Space Value present
worker_boundary: Gemini/Codex/Hermes logs are not VectorFL memory
return_shape: worker return packaging or movement record after interpretation
watch_signal: raw_trace_promotion_watch
reentry_trigger: worker output looks polished or claims finality
do_not_infer: no tool authority, no verified truth
```

Use:

When external tool output, logs, memory, or session state needs to enter the space safely.

### PV-004 Manual Relay Bridge

```yaml
position_id: PV_MANUAL_RELAY_BRIDGE
asset_family: worker evidence / Gemini process record
authority_state: watch_only
maturity_state: hold_signal
active_line: User Relay Burden Reduction
axis_tension: tool runner instability vs user relay burden
camera_position: user relay burden
lens_gate: manual relay packaged immediately
worker_boundary: user may temporarily relay, but not as steady-state dispatcher
return_shape: manual worker return packaging
watch_signal: user_relay_burden_watch
reentry_trigger: user manually brings external tool result
do_not_infer: no permanent relay workflow, no normalized dispatcher role
```

Use:

When the user manually supplies Gemini/Codex/other tool output because the runner is unreliable.

### PV-005 Non-Inspected Evidence Disclosure

```yaml
position_id: PV_NON_INSPECTED_DISCLOSURE
asset_family: role and authority boundary
authority_state: candidate_reference
maturity_state: process_asset_candidate
active_line: Plan from Space / Session Convergence Prevention
axis_tension: evidence confidence vs overclaim
camera_position: provenance integrity
lens_gate: non-inspected evidence disclosed
worker_boundary: worker must say what it did not inspect
return_shape: evidence pointers + not-inspected scope
watch_signal: evidence_overclaim_watch
reentry_trigger: worker reports conclusions from partial read
do_not_infer: no full-space read claim, no final verification
```

Use:

When a worker consults bounded files and might overstate coverage.

### PV-006 Line Maturity Caution

```yaml
position_id: PV_LINE_MATURITY_CAUTION
asset_family: line / axis / lens / camera reference
authority_state: watch_only
maturity_state: hold_signal
active_line: Line Maturity / Operating Anchor
axis_tension: reading lens vs operating anchor
camera_position: program continuity
lens_gate: no premature promotion
worker_boundary: line can guide anchor only within bounded purpose
return_shape: watch item or future reuse note
watch_signal: axis_ontology_watch
reentry_trigger: a line starts acting like ontology, registry, or law
do_not_infer: no line registry baseline, no agent station
```

Use:

When `Plan from Space` or any line starts being treated as a global authority.

### PV-007 Return-To-Space Closeout

```yaml
position_id: PV_RETURN_TO_SPACE_CLOSEOUT
asset_family: current-position / anchor state
authority_state: candidate_reference
maturity_state: process_asset_candidate
active_line: Return-to-Space Recovery
axis_tension: output completion vs return-to-space recovery
camera_position: space recovery
lens_gate: reusable judgment present
worker_boundary: worker may complete output but Codex/space judges memory value
return_shape: Movement Record
watch_signal: done_without_memory_watch
reentry_trigger: closeout says done but leaves no reusable value
do_not_infer: no automatic memory promotion
```

Use:

When a plan or run is about to close.

### PV-008 Current Position Entry

```yaml
position_id: PV_CURRENT_POSITION_ENTRY
asset_family: current-position / anchor state
authority_state: current_position_entry
maturity_state: reusable_setting_candidate
active_line: Return-to-Space Recovery
axis_tension: session-loss drift vs re-entry memory
camera_position: program continuity
lens_gate: next safe position stated
worker_boundary: current work should not auto-continue
return_shape: current-position entry
watch_signal: session_loss_watch
reentry_trigger: session may be lost or next session needs recovery
do_not_infer: no official session protocol, no baseline
```

Use:

When a future session needs compact re-entry memory without replaying the whole prior context.

### PV-009 Bounded Reread Unit

```yaml
position_id: PV_BOUNDED_REREAD_UNIT
asset_family: docs/reports thought asset
authority_state: candidate_reference
maturity_state: process_asset_candidate
active_line: Plan from Space / Session Convergence Prevention
axis_tension: reread vs rewrite
camera_position: token budget
lens_gate: retrieval_scope_boundary applied
worker_boundary: Gemini as bounded reader
return_shape: evidence inventory / structural observation
watch_signal: broad_scan_watch
reentry_trigger: need to apply one lens to one bounded artifact or representative anchor set
do_not_infer: no content revision, no promotion review
```

Use:

When Gemini or another worker should read more space without turning the task into broad scan or whole-space summary.

## Current Missing Positions

These need Gemini or future bounded reads:

- useful shape vs reusable setting boundary
- older docs/reports active vs residue sample marker
- latent_line to current line-axis mapping
- package source ambiguity / HOLD handling
- Gemini result inconsistency around `PV_LINE_MATURITY_CAUTION` family mention without candidate block

## How Small Anchors Should Use This

A small Session Space Anchor should include 1-3 position IDs, not the whole map.

Example:

```text
Position IDs:
- PV_PLAN_BASIS_GATE
- PV_BROAD_BOUNDED_PACKAGE
- PV_RETURN_TO_SPACE_CLOSEOUT
```

Then include only the relevant watch signals and do-not-infer lines.

For external tool planning, the current best set is:

```text
Position IDs:
- PV_PLAN_BASIS_GATE
- PV_BROAD_BOUNDED_PACKAGE
- PV_NON_INSPECTED_DISCLOSURE
- PV_RETURN_TO_SPACE_CLOSEOUT
```

For bounded Gemini reread, use:

```text
Position IDs:
- PV_BOUNDED_REREAD_UNIT
- PV_NON_INSPECTED_DISCLOSURE
- PV_RAW_TRACE_BOUNDARY
```
