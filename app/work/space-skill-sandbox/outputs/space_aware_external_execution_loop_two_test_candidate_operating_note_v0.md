# Space-Aware External Execution Loop Two-Test Candidate Operating Note v0

## Status

```yaml
status: candidate_operating_note
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
current_position_update: false
source_basis: two_gemini_runner_tests
verdict: REPEATABLE_WITH_WATCH
```

## Purpose

Capture what two actual Gemini-runner tests showed about the space-aware external execution loop.

This note is not a baseline, workflow, automation, schema, registry, or current-position update.

## Source Tests

Test 001:

```text
general space-aware external execution loop
verdict: PASS_WITH_WATCH_AS_FIRST_SPACE_AWARE_EXTERNAL_EXECUTION_LOOP_TEST
run: app/work/space-skill-sandbox/runs/run_240_space_loop_test_001_actual_operation_entry.md
movement record: app/work/space-skill-sandbox/outputs/movement_record_space_loop_test_001_space_aware_external_execution_v0.md
```

Test 002:

```text
QMD-like retrieval-side attachability trial
verdict: PASS_WITH_WATCH_AS_SECOND_SPACE_AWARE_EXTERNAL_EXECUTION_LOOP_TEST
run: app/work/space-skill-sandbox/runs/run_241_space_loop_test_002_qmd_attachability.md
movement record: app/work/space-skill-sandbox/outputs/movement_record_space_loop_test_002_qmd_attachability_v0.md
```

## Observed Repeatable Loop

Across two different inputs, the loop held:

```text
User Purpose
-> External Tool Interpretation
-> Anchor Request
-> Codex Anchor Packet
-> External Execution
-> Execution Return
-> Codex Recovery
-> Return-to-Space Value
-> Movement Record
-> User Judgment
```

The observed operating behavior was:

```text
External carrier can be asked to stop before planning and request anchors.
Codex can broker anchors by material family / route / PV / LACL / active surfaces.
External carrier can execute after receiving Anchor Packet.
External carrier can return Anchor Usage Trace and Return-to-Space Value.
Codex must downshift raw trace before it becomes space memory.
Movement Record can preserve the reusable judgment.
```

## What Changed Between Inputs

Test 001 requested general space-aware execution anchors:

```text
Core Operating Anchors
Space Navigation Maps / Indexes
Task-Mode Gate Specs
Worker Return / Packaging Records
Current Position / Re-Entry Notes
Integrated Engine / Operating Surface Records
```

Test 002 requested retrieval-specific anchors:

```text
Retrieval-side lineage
Evidence access protocol
Lower input organ boundary
Integrated-engine boundary
QMD as bounded retrieval candidate
Memory-card / retrieval minimum
```

Candidate judgment:

```text
The Anchor Request did not collapse into pure ritual across the two tests.
The second request adapted to the retrieval-side input.
```

## Candidate Operating Shape

Use this shape when the next external carrier or model needs to work from VectorFL Space:

### 1. Anchor Request First

External carrier should first return:

```text
EXTERNAL_TOOL_INTERPRETATION
ANCHOR_REQUEST
STOP_BEFORE_EXECUTION
```

The request should state:

```text
needed material families
needed route / PV / LACL signals
expected active surfaces
needed evidence / return shape
unsafe inferences without anchors
```

### 2. Codex Anchor Packet

Codex should return a bounded packet with:

```text
user purpose
external tool anchor request summary
material families
route
canonical Position IDs
LACL signals
active surfaces
read depth
execution instruction
required return shape
stop / hold conditions
do-not-infer list
```

### 3. External Execution Return

External carrier should return:

```text
PLAN_BASIS
bounded result
ANCHOR_USAGE_TRACE
EXECUTION_RETURN_SHAPE
SELF_CHECK
RETURN_TO_SPACE
```

Required in `PLAN_BASIS`:

```text
route
canonical Position IDs
package sizing judgment
non-inspected scope
Return-to-Space requirement
```

### 4. Codex Recovery

Codex should package:

```text
source trace
loop checks
accepted candidate signals
held / watch signals
downshift corrections
Return-to-Space Value
Movement Record
```

## Candidate Small Anchor Fields

For future small anchors, the two tests support this compact form:

```text
anchor_use_case
material_family
route
canonical_position_ids
LACL_line
LACL_axis
LACL_camera
LACL_lens
active_surfaces_3_to_7
read_depth_default
when_to_deepen
when_to_stop
required_return_shape
return_to_space_shape
movement_record_target
watch_items
do_not_infer
```

This is a candidate form only.

## Reusable Judgments

```text
Executor autonomy does not need to be downgraded for space-awareness.
The control point is Anchor Request, Anchor Packet, Anchor Usage Trace, and Return-to-Space packaging.
```

```text
Retrieval-side attachability is judged by boundary behavior, not search quality alone.
The sidecar must not become source of truth, lower-organ replacement, integrated-engine replacement, storage writer, schema, or automatic memory promotion.
```

```text
Gemini output is useful broad execution trace but continues to need downshift around baseline/reuse/storage/promotion language.
```

## Recurring Watch Items

```text
baseline_wording_watch
anchor_request_filler_watch
direct_surface_read_gap_watch
gemini_only_carrier_watch
storage_path_overclaim_watch
promotion_task_overclaim_watch
tool_specific_readiness_overclaim_watch
retrieval_metadata_authority_watch
sidecar_becoming_source_of_truth_watch
```

## What Is Not Proven

```text
No Hermes validation.
No OmX validation.
No OpenClaw validation.
No qmd-main source inspection.
No QMD readiness validation.
No production attach path.
No automation/runner/controller approval.
No schema/storage/MCP decision.
No current-position update.
No baseline.
```

## Next Re-Entry Use

Use this note when:

```text
testing a non-Gemini carrier
testing a third actual input
preparing a qmd-main direct source inspection package
reviewing a worker output that claims readiness/baseline/storage/promotion
building a future small Anchor Packet for external execution
```

## Candidate Next Moves

Safe next moves, not instructions:

```text
1. Run a non-Gemini carrier test if Hermes/OmX/OpenClaw or another carrier becomes locally available.
2. Run a qmd-main direct source inspection package to test the retrieval-output contract candidate.
3. Run a third Gemini-runner test with a non-retrieval input to check Anchor Request specificity further.
4. Stop here and wait for user direction.
```

## Do Not

```text
do not promote this note to baseline
do not create automation from this note
do not create registry/schema/storage from this note
do not treat two Gemini-runner tests as carrier-general proof
do not update current position from this note alone
```

`STATUS: SPACE_AWARE_EXTERNAL_EXECUTION_LOOP_TWO_TEST_CANDIDATE_OPERATING_NOTE_PREPARED`
