# Gemini Instruction - Package C: Gemini Broad-Bounded Carrier Protocol v0

## Mission

You are acting as an external execution carrier for VectorFL.

Do not create micro-runs.
Do not return result per session.
Perform 10 internal sessions (C01-C10) in one broad-but-bounded pass and return one packaged result.

## Operating Principle

```text
Plan from Space, not from Model Default.
```

The goal of this package is to set up the protocol for Gemini to execute internal small work and return a recoverable package-level result.

## Current Operating Setting

- Hardened Worker Return Intake Shape (from Package A)
- Codex: anchor broker / recovery editor
- User: direction judge

## Space Anchors To Use

Primary anchors:

- `app/work/space-skill-sandbox/outputs/space_aware_external_execution_package_setup_20260507_v0.md`
- `app/work/space-skill-sandbox/outputs/worker_return_packaging_candidate_setting_hardened_v0.md` (Refer to the hardened 10-field shape and HOLD/WATCH table from Package A)
- `docs/specs/external_tool_plan_prompt_wrapper_v0.md`
- `docs/specs/plan_basis_template_v0.md`
- `docs/specs/anchor_stack_gate_checklist_v0.md`

## Package C - Session List

Execute these 10 sessions internally:

- **C01 - Instruction Shape Regrounding**: Restate the standard Gemini return shape. Ensure no baseline or finality language.
- **C02 - Anchor Packet Intake**: Define what Gemini receives from Codex (Route/PV/LACL/Material Family). Identify markers of a "grounded" packet.
- **C03 - Broad-Bounded Execution Discipline**: Define the bundling rule. Explain how to handle 3-10 small steps without externalizing intermediate traces.
- **C04 - PLAN_BASIS Gate**: Enforce PLAN_BASIS before any synthesis. Check for route selection and canonical PVs.
- **C05 - Evidence / Not-Inspected Discipline**: Require direct evidence pointers and explicit disclosure of skipped scope.
- **C06 - HOLD/WATCH Classification**: Apply the hardened priority table from Package A to sample Gemini returns.
- **C07 - Return-to-Space Extraction**: Focus on extracting 3-7 reusable judgments that change future worker behavior.
- **C08 - Do-Not-Promote Discipline**: List explicit non-promotions. Downshift "verified" or "stable" to "candidate."
- **C09 - User Relay Burden Check**: Ensure the final package is a single, pasteable unit that minimizes user effort.
- **C10 - Package Closeout**: Synthesize C01-C09 into a "Gemini Broad-Bounded Protocol Candidate."

## Required Return Shape

Return exactly one package-level result with these sections:

```text
PLAN_BASIS
PACKAGE_C_SESSION_SUMMARY
GEMINI_BROAD_BOUNDED_PROTOCOL_CANDIDATE
INSTRUCTION_TEMPLATE_CANDIDATE
RETURN_TO_SPACE_VALUE
MOVEMENT_RECORD_CANDIDATE
DO_NOT_PROMOTE
NEXT_USE
```

## Stop Conditions

Stop and return HOLD if:
- Authority/baseline/schema/automation claims appear.
- PLAN_BASIS is missing or model-default.
- The protocol suggests bypassing Codex recovery.
- Micro-run splitting begins.

`STATUS: GEMINI_PACKAGE_C_BROAD_BOUNDED_PROTOCOL_INSTRUCTION_PREPARED`
