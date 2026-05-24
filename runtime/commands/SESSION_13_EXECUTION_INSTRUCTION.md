# SESSION_13_EXECUTION_INSTRUCTION.md

## 1. Goal
Create `OPERATOR_BOARD_V0`, `BOARD_STATUS_SCHEMA_V0`, `OPERATOR_BOARD_VIEW_V0`, `BOARD_UPDATE_RULES_V0`, and `BOARD_TO_NEXT_ACTION_RULES_V0` to provide compact visibility into the pipeline.

## 2. Search First
- Existing work board/status records.
- Session 0-12 Handoff records.
- Boundary Rules and Drift Watchlist.
- User visibility problems (copy-paste relay, manual stitching).

## 3. Required Outputs (Artifacts)
- **Operator Board**: Fields (Current Goal, Stage, Status, Active Artifacts, Next Action, etc.).
- **Status Schema**: Definitions for Review Status, Stage Status, Boundary Status, Decision Status.
- **Operator Board View**: Compact, readable one-minute board.
- **Update/Action Rules**: When to update, how to recommend next actions.

## 4. Constraints
- **Visibility Layer, NOT Controller.**
- Keep it compact and human-readable.
- Do not add automation, implementation, or dashboard coding.
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_14_HANDOFF.md` for Limited Trial or Evidence Review.
