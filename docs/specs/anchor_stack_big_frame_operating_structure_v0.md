# Anchor Stack Big-Frame Operating Structure v0

## Status

```yaml
status: big_frame_candidate
date: 2026-05-06
baseline_lock: false
automation: false
schema: false
registry: false
scope: plan_from_space_anchor_stack_operation
```

## Purpose

Set the large operating frame for the Anchor Stack so future work does not wobble between abstract documentation, Gemini exploration, and Codex setup.

This is not a baseline. It is the current big-frame operating structure for bounded setup and trials.

## Core Operating Sentence

```text
Input enters through route/PV selection, not model-default planning.
Worker output returns through packaging, not authority.
Closeout becomes Movement Record, not completion prose.
```

## Big Frame

```text
0. Current Position
1. Input Classification / Route Selection
2. Compact Position Anchor
3. Plan Basis
4. Four Plan-Mode Gates
5. Bounded Work Package
6. Worker Return Packaging
7. Maturation / Residue Judgment
8. Movement Record / Next Current Position
```

## Layer 0. Current Position

Purpose:

- prevent broad replay of all setup records
- state where the work currently is
- provide the first small re-entry point

Current active file:

- `app/work/CURRENT_POSITION_20260506_ANCHOR_STACK_AFTER_SET_A_V0.md`

Rule:

If a future session is unsure where to begin, read Current Position first, not the full manifest.

## Layer 1. Input Classification / Route Selection

Purpose:

- decide which route should handle the input
- prevent immediate model-default planning
- choose 2-4 canonical PVs

Current primary route:

- `ROUTE_EXTERNAL_TOOL_PLANNING`

Current watch routes:

- `ROUTE_INPUT_CLASSIFICATION`
- `ROUTE_SPACE_RESIDUE_SAMPLING`

Rule:

Route selection happens before Plan Basis. Route expansion requires task-behavior change.

## Layer 2. Compact Position Anchor

Purpose:

- carry only the relevant PVs, watch signals, and do-not-infer lines
- avoid replaying the whole Anchor Stack

Rule:

Small anchors should not contain broad philosophy. They should transmit position.

## Layer 3. Plan Basis

Purpose:

- force the worker or Codex plan to expose its space grounding before plan
- make model-default planning detectable

Required fields:

- work type
- line
- route
- canonical PVs
- axis / camera / lens
- package sizing judgment
- stop / continue rule
- return shape

Rule:

No plan is accepted as space-grounded without Plan Basis.

## Layer 4. Four Plan-Mode Gates

Current gates:

1. Pre-Plan Gate
2. Plan Sizing Gate
3. Runtime Re-Entry Gate
4. Closeout / Return-to-Space Gate

Reference:

- `docs/specs/anchor_stack_plan_mode_gate_sequence_v0.md`

Rule:

The gates are checks inside a bounded package, not four separate sessions.

Validation lens:

The gates are only working if they change task behavior. If a plan still defaults to analysis / design / implementation / validation / review sessions, the Anchor Stack was referenced but not applied.

## Layer 5. Bounded Work Package

Default:

```text
broad-but-bounded
```

Small split requires:

- user decision branch
- unapproved implementation or file modification
- blocking evidence gap
- current line cannot be selected
- return shape unclear
- broad scan required

Rule:

Analysis / design / implementation / validation / review should not become separate sessions by default.

## Layer 6. Worker Return Packaging

Purpose:

- prevent worker output from becoming authority
- preserve useful findings without admitting raw trace as memory

Worker output states:

- Gemini/Codex/Hermes/OmX logs and reports are raw trace until interpreted.

Rule:

Manual relay is allowed only as bridge and must be packaged immediately.

Validation lens:

External tool output is useful only after Codex records read scope, non-inspected scope, authority downshift, and Return-to-Space value. Otherwise it remains raw trace.

## Layer 7. Maturation / Residue Judgment

Purpose:

- decide whether a new shape is only useful, reusable, active, watch, residue, or raw trace
- prevent every useful artifact from becoming anchor/policy

References:

- `docs/specs/useful_shape_maturation_boundary_v0.md`
- `docs/specs/active_residue_marker_policy_v0.md`

Rule:

Maturation labels guide bounded judgment. They are not schema, registry, or archive taxonomy.

Validation lens:

If a useful shape is immediately treated as anchor, policy, registry, or baseline, the maturation layer failed. Keep it as useful shape or candidate until repeated Movement Record support exists.

## Layer 8. Movement Record / Next Current Position

Purpose:

- capture Return-to-Space Value
- preserve reusable judgment
- state the next safe re-entry point

Current Movement Record:

- `app/work/MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0.md`

Rule:

Closeout without reusable judgment is not enough.

## Operating Defaults

```yaml
planning_default: Plan Basis before plan
package_default: broad_but_bounded
worker_output_default: raw_trace_until_packaged
manual_relay_default: temporary_bridge
route_expansion_default: hold_until_task_behavior_change
maturation_default: candidate_until_movement_record_support
```

## Codex-Owned Decisions

Codex owns:

- big-frame setup
- route/PV/gate synthesis
- worker return packaging
- authority downshift
- Movement Record updates
- deciding what becomes current operating structure

Gemini may support:

- bounded space exploration
- evidence crosscheck
- route validation
- plan-mode trial output

User owns:

- purpose and priority
- authority-shifting decisions
- approvals for implementation, runner, writer, automation, or baseline moves

## Do Not

- Do not treat this as baseline.
- Do not make this an automatic workflow.
- Do not create runner/writer/controller from this frame.
- Do not make the manifest a registry.
- Do not let Gemini decide operating authority.
- Do not add layers without removing confusion or changing task behavior.
