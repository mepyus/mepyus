# Gemini Space Exploration Packet - Plan from Space / Session Convergence Prevention

## Role

You are doing bounded space exploration for VectorFL. Do not edit files. Do not create files. Do not declare a baseline.

Your job is to find existing space records that should feed a new Anchor Stack setup:

- Stable Space Operating Anchor
- Plan from Space Line Asset Map
- Session Space Anchor template
- Movement Record template

## Current User Thesis

The user wants external tools to stop planning from model default. The current principle candidate is:

```text
Plan from Space, not from Model Default.
```

Expanded operating candidate:

```text
Plan from Space.
Execute within Space Boundary.
Loop with Space Re-Entry.
Closeout as Return-to-Space.
```

The main failure pattern is session convergence:

- external tools split work into analysis / design / execution / verification / review / closeout by default
- small sessions close inside their own goals
- user becomes a relay / dispatcher
- hard boundaries and watch items are confused
- outputs close without Return-to-Space Value

## Bounded Search Scope

Read only as needed. Prefer targeted files over broad scans.

Primary candidate files:

- `app/work/PROGRAM_FRAME_EXTERNAL_PATTERN_MAP_V0.md`
- `app/work/SESSION_39_RESULTS_V0.md`
- `app/work/SESSION_43_RESULTS_V0.md`
- `app/work/SESSION_44_RESULTS_V0.md`
- `app/work/SESSION_45_RESULTS_V0.md`
- `app/work/SESSION_46_RESULTS_V0.md`
- `app/work/SESSION_47_RESULTS_V0.md`
- `runtime/commands/SESSION_39_EXECUTION_INSTRUCTION.md`
- `runtime/commands/SESSION_43_EXECUTION_INSTRUCTION.md`
- `runtime/commands/SESSION_46_EXECUTION_INSTRUCTION.md`
- `runtime/commands/SESSION_47_EXECUTION_INSTRUCTION.md`
- `docs/reports/space_feedback_loop_return_to_space_record_minimum_v0.md`
- `docs/specs/line_maturity_and_operating_anchor_direction_lock_v0.md`

Secondary candidate areas if needed:

- `app/work/space-skill-sandbox/runs/`
- `app/work/space-skill-sandbox/packages/`
- `docs/specs/`
- `docs/reports/`
- `docs/indexes/`

Use targeted searches only for these terms:

- `Return-to-Space`
- `Movement Record`
- `Package 5`
- `Package Closeout`
- `Product-Attachable`
- `hard boundary`
- `watch item`
- `user_burden`
- `tool_drift`
- `session`
- `anchor`
- `line`

## Output Required

Return a compact report with these sections:

1. `Space Assets Consulted`
   - 5 to 12 records maximum.
   - Include file path and one-line reason.

2. `Lineage Finding`
   - How the Product-Attachable pipeline, Package 5, Sessions 43-47, and Return-to-Space material connect.

3. `Judgment Map Seeds`
   - hard boundary candidates
   - watch item candidates
   - continue-with-issue-log candidates
   - package sizing signals
   - user relay burden signals

4. `Plan from Space Line Map Inputs`
   - line definition candidate
   - main axes
   - main cameras
   - main lenses
   - use-when triggers

5. `Anchor Stack Setup Advice`
   - what should go into the stable anchor
   - what should go into the line map
   - what should go into the session anchor
   - what should go into the movement record

6. `Risks / Do Not Promote`
   - what should remain HOLD
   - what should not become automation or baseline yet

7. `Return-to-Space Value`
   - 3 to 7 reusable findings for future sessions.

## Constraints

- Do not produce a giant summary.
- Do not propose a new automation runner.
- Do not ask the user to relay content.
- Do not say "ready" or "baseline".
- Treat Gemini logs and tool output as raw trace, not VectorFL memory.
- Cite file paths for every concrete claim.
