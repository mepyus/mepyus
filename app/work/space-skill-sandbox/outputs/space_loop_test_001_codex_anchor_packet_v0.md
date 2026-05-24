# Space Loop Test 001 - Codex Anchor Packet v0

## Status

```yaml
status: anchor_packet_candidate
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
authority: false
test_id: space_loop_test_001
```

## User Purpose

```text
Hermes / OmX / OpenClaw 같은 외부 실행 도구를 VectorFL 공간과 연결해서,
실제 작업 하나를 공간 참조 기반으로 실행하고,
그 결과를 다시 Movement Record로 회수하는 최소 운용 흐름을 설계해봐.
```

## External Tool Anchor Request Summary

Gemini returned an anchor request instead of drafting the plan.

It requested:

```text
Stable Operating Anchors
Position Maps
Line Asset Maps
PV_PLAN_BASIS_GATE
PV_BROAD_BOUNDED_PACKAGE
PV_RETURN_TO_SPACE_CLOSEOUT
Movement Record-compatible return shape
```

Codex downshift:

```text
The request is useful raw trace / candidate material.
It is not authority, baseline, registry, schema, or proof of tool readiness.
```

## Anchor Use Case

```text
Use this packet to let an external execution carrier draft the minimal operating-loop flow while staying inside VectorFL memory-judgment-recovery.
```

This is not design expansion. It is a bounded operating-loop entry test.

## Material Families

```text
Core Operating Anchors
Space Navigation Maps / Indexes
Task-Mode Gate Specs
Worker Return / Packaging Records
Current Position / Re-Entry Notes
Maturation / Residue Policy
Integrated Engine / Operating Surface Records
```

## Route

Primary route:

```text
ROUTE_EXTERNAL_TOOL_PLANNING
```

Supporting route during recovery:

```text
ROUTE_MANUAL_WORKER_RETURN_INTAKE
ROUTE_AUTHORITY_DOWNSHIFT
```

## Position IDs

Use canonical Position IDs only:

```text
PV_PLAN_BASIS_GATE
PV_BROAD_BOUNDED_PACKAGE
PV_NON_INSPECTED_DISCLOSURE
PV_RAW_TRACE_BOUNDARY
PV_RETURN_TO_SPACE_CLOSEOUT
PV_LINE_MATURITY_CAUTION
```

## LACL Signals

Line:

```text
Plan from Space / Space-Aware External Execution Loop Verification
```

Axis:

```text
model-default planning vs space-grounded planning
executor downgrade vs executor space-awareness
external output authority vs recoverable material
automation/design expansion vs actual bounded operation
```

Camera:

```text
external tool plan mode
provenance integrity
user relay burden
space recovery
```

Lens:

```text
Plan Basis present before plan
anchor usage trace present
non-inspected scope disclosed
hard boundary vs watch separated
Return-to-Space Value present
Movement Record-compatible closeout
```

## Active Surfaces

Use these as the active surface pool. Do not claim whole-space coverage.

```text
1. docs/specs/stable_space_operating_anchor_v0.md
   Use: VectorFL space is memory-judgment-recovery; external tool logs are raw trace; Return-to-Space Value is required.

2. docs/indexes/plan_from_space_line_asset_map_v0.md
   Use: current line, axis, camera, lens; prevent model-default planning and user relay burden.

3. docs/indexes/plan_from_space_position_map_seed_v0.md
   Use: canonical PV meanings and watch signals.

4. docs/indexes/anchor_map_position_route_seed_v0.md
   Use: route selection and wrong-completion prevention.

5. docs/specs/anchor_stack_plan_mode_gate_sequence_v0.md
   Use: Pre-Plan Gate, Plan Sizing Gate, Runtime Re-Entry Gate, Closeout / Return-to-Space Gate.

6. docs/specs/movement_record_template_v0.md
   Use: minimum return record shape.

7. app/work/space-skill-sandbox/outputs/next_chat_reentry_summary_after_space_aware_external_execution_loop_v0.md
   Use: current handoff-specific operating sentence and tool/model/Codex/User role split.
```

## Read Depth

```text
read_depth_default: bounded excerpts / packet summaries
when_to_deepen: if the plan would create automation, runner, registry, baseline, or tool-specific lock-in
when_to_stop: if the result needs unapproved implementation, broad scan, or user direction judgment
```

## Execution Instruction

Draft the minimal operating flow for the user purpose.

Keep the external tool autonomous. Do not reduce it to a scripted subroutine.

The flow must show:

```text
User Purpose
External Tool Interpretation
Anchor Request
Codex Anchor Packet
External Execution
Execution Return
Codex Recovery
Return-to-Space Value
Movement Record
User Judgment
```

## Required Return Shape

Return exactly these sections:

```text
PLAN_BASIS
MINIMAL_OPERATING_FLOW
ANCHOR_USAGE_TRACE
EXECUTION_RETURN_SHAPE
SELF_CHECK
RETURN_TO_SPACE
```

## Stop / Hold Conditions

Return HOLD instead of a plan if:

```text
you need a broad scan
you need to modify files
you need current official docs
you would need to declare a tool ready/baseline
you cannot state Return-to-Space Value
you would make the user a routine relay
```

## Do Not Infer

```text
no baseline
no official workflow
no automation/router/controller
no registry
no schema
no Hermes-specific lock-in
no Gemini authority
no whole-space read claim
no current-position update
```
