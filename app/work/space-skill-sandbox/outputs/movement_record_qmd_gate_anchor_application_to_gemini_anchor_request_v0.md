# Movement Record - QMD Gate Anchor Application to Gemini Anchor Request v0

## Status

```yaml
status: movement_record_candidate
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
qmd_runtime_executed_for_this_review: false
external_return_reviewed: true
verdict: PASS_WITH_WATCH_AS_GATE_ANCHOR_APPLICATION_TRIAL
```

## Input Purpose

Continue from QMD subset 002 by testing whether QMD-retrieved gate anchors can be applied to a real external-tool return.

## Activated Space Memory

Line:

```text
Plan from Space / Feature-Level External Retrieval Attachability
```

Axis:

```text
retrieved gate anchor vs external return review
anchor request vs model-default plan
Codex judgment vs QMD authority
```

Camera:

```text
worker planning behavior
pre-plan gate
space recovery
authority downshift
```

Lens:

```text
Plan Basis before plan
Anchor Request validity
hard boundary vs watch
Return-to-Space recovery
```

## Space Assets Consulted

```text
app/work/space-skill-sandbox/outputs/qmd_vectorfl_subset_002_gate_specs_codex_recovery_v0.md
app/work/space-skill-sandbox/outputs/movement_record_qmd_vectorfl_subset_002_gate_specs_trial_v0.md
docs/specs/external_tool_plan_prompt_wrapper_v0.md
docs/specs/anchor_stack_gate_checklist_v0.md
app/work/space-skill-sandbox/relay/outbox/space_loop_test_001_anchor_request_20260507_gemini_outbox_20260507_180852.md
```

## External Tool Role

```text
retrieval_carrier: QMD surfaced gate-spec pointers in prior run
reviewed_tool: Gemini
codex_role: Recovery Editor / Anchor Broker
```

## Tool Output Summary

Gemini returned:

```text
EXTERNAL_TOOL_INTERPRETATION
ANCHOR_REQUEST
STOP_BEFORE_EXECUTION
```

Codex reviewed it using the gate anchors QMD had surfaced.

## Read Trace / Evidence

Evidence from Gemini return:

```text
user purpose understanding present
material families requested
PV_PLAN_BASIS_GATE and PV_RETURN_TO_SPACE_CLOSEOUT present
LACL-like line/axis/camera/lens present
unsafe inferences named
STOP_BEFORE_EXECUTION present
```

Evidence from gate anchors:

```text
external_tool_plan_prompt_wrapper_v0 requires PLAN_BASIS before PLAN and canonical Position IDs.
anchor_stack_gate_checklist_v0 allows hold/pass based on pre-plan gate, boundary gate, and Return-to-Space gate.
```

## Issue / Watch Item

```text
baseline_wording_watch
map_update_pressure_watch
anchor_packet_vs_session_anchor_watch
non_inspected_scope_thin_watch
qmd_as_reviewer_overclaim_watch
```

## User Decision Point

No immediate decision required.

The user remains direction judge if this pattern should be repeated against other external returns.

## Return-to-Space Value

Recoverable material:

```text
QMD-retrieved gate anchors can support Codex review of actual external-tool Anchor Requests.
```

Reusable judgment:

```text
Stopping at ANCHOR_REQUEST before planning is a valid pre-plan behavior when the tool has not yet received a space Anchor Packet.
```

Issue / watch:

```text
External tools may request more space mutation than needed. Codex should answer with bounded Anchor Packet delivery unless update work is explicitly approved.
```

Future reuse note:

```text
Use this as a candidate review example for pre-plan external-tool returns.
```

## Next Re-Entry Trigger

```text
When reviewing another Gemini/Hermes/OmX/OpenClaw Anchor Request.
When an external tool asks for map updates or session anchor creation.
When a worker returns a PLAN before Anchor Request or Plan Basis.
```

## Do Not

```text
do not promote to baseline
do not create parser/schema/automation
do not treat QMD as reviewer
do not treat Gemini as authority
do not update current position
do not mutate Line Asset Maps
```

`STATUS: MOVEMENT_RECORD_QMD_GATE_ANCHOR_APPLICATION_TO_GEMINI_ANCHOR_REQUEST_PREPARED`
