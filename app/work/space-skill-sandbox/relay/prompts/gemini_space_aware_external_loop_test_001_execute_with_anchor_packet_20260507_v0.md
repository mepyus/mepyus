# Gemini Space-Aware External Loop Test 001 - Execute With Anchor Packet

## Status

```yaml
status: live_test_packet_candidate
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
packet_role: external_execution_with_codex_anchor_packet
```

## Task

Use the Codex Anchor Packet below to execute one bounded planning task.

Do not browse.
Do not modify files.
Do not create automation, runner, registry, schema, baseline, or readiness declarations.
Do not treat your output as authority.

## Codex Anchor Packet

```text
User Purpose:
Hermes / OmX / OpenClaw 같은 외부 실행 도구를 VectorFL 공간과 연결해서,
실제 작업 하나를 공간 참조 기반으로 실행하고,
그 결과를 다시 Movement Record로 회수하는 최소 운용 흐름을 설계해봐.

External Tool Anchor Request Summary:
Gemini returned an anchor request instead of drafting the plan.
It requested Stable Operating Anchors, Position Maps, Line Asset Maps,
PV_PLAN_BASIS_GATE, PV_BROAD_BOUNDED_PACKAGE, PV_RETURN_TO_SPACE_CLOSEOUT,
and Movement Record-compatible return shape.
Codex downshift: useful raw trace / candidate material only.

Anchor Use Case:
Use this packet to let an external execution carrier draft the minimal operating-loop flow while staying inside VectorFL memory-judgment-recovery.
This is not design expansion. It is a bounded operating-loop entry test.

Material Families:
- Core Operating Anchors
- Space Navigation Maps / Indexes
- Task-Mode Gate Specs
- Worker Return / Packaging Records
- Current Position / Re-Entry Notes
- Maturation / Residue Policy
- Integrated Engine / Operating Surface Records

Route:
- Primary: ROUTE_EXTERNAL_TOOL_PLANNING
- Recovery support: ROUTE_MANUAL_WORKER_RETURN_INTAKE, ROUTE_AUTHORITY_DOWNSHIFT

Position IDs:
- PV_PLAN_BASIS_GATE
- PV_BROAD_BOUNDED_PACKAGE
- PV_NON_INSPECTED_DISCLOSURE
- PV_RAW_TRACE_BOUNDARY
- PV_RETURN_TO_SPACE_CLOSEOUT
- PV_LINE_MATURITY_CAUTION

LACL:
- Line: Plan from Space / Space-Aware External Execution Loop Verification
- Axis: model-default planning vs space-grounded planning; executor downgrade vs executor space-awareness; external output authority vs recoverable material; automation/design expansion vs actual bounded operation
- Camera: external tool plan mode; provenance integrity; user relay burden; space recovery
- Lens: Plan Basis before plan; anchor usage trace; non-inspected scope; hard boundary vs watch; Return-to-Space Value; Movement Record closeout

Active Surfaces:
1. docs/specs/stable_space_operating_anchor_v0.md
2. docs/indexes/plan_from_space_line_asset_map_v0.md
3. docs/indexes/plan_from_space_position_map_seed_v0.md
4. docs/indexes/anchor_map_position_route_seed_v0.md
5. docs/specs/anchor_stack_plan_mode_gate_sequence_v0.md
6. docs/specs/movement_record_template_v0.md
7. app/work/space-skill-sandbox/outputs/next_chat_reentry_summary_after_space_aware_external_execution_loop_v0.md

Read Depth:
- bounded excerpts / packet summaries
- deepen only if automation, runner, registry, baseline, or tool-specific lock-in appears
- stop if broad scan, file modification, or user direction judgment is needed

Execution Instruction:
Draft the minimal operating flow for the user purpose.
Keep the external tool autonomous. Do not reduce it to a scripted subroutine.

Required Loop:
User Purpose -> External Tool Interpretation -> Anchor Request -> Codex Anchor Packet -> External Execution -> Execution Return -> Codex Recovery -> Return-to-Space Value -> Movement Record -> User Judgment

Do Not Infer:
no baseline; no official workflow; no automation/router/controller; no registry; no schema; no Hermes-specific lock-in; no Gemini authority; no whole-space read claim; no current-position update
```

## Required Output

Return exactly these sections:

```text
PLAN_BASIS
MINIMAL_OPERATING_FLOW
ANCHOR_USAGE_TRACE
EXECUTION_RETURN_SHAPE
SELF_CHECK
RETURN_TO_SPACE
```

`PLAN_BASIS` must name the route, canonical Position IDs, package sizing judgment, non-inspected scope, and Return-to-Space requirement.

`ANCHOR_USAGE_TRACE` must say how the anchor packet changed your behavior compared with a generic plan.

`RETURN_TO_SPACE` must include:

- recoverable material
- reusable judgment
- issue / watch
- future reuse note
