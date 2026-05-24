# SESSION_34_EXECUTION_INSTRUCTION.md

## 1. Goal
Select one optimal real input (data/task) that best tests the pipeline's space-depth understanding, tool role containment, and boundary discipline.

## 2. Search First
- `SPACE_DEPTH_TEST_FRAME_V0` (Evaluation criteria).
- Existing `ISSUE_LOG` (Where we had most drift).
- Past trial cases (What successfully triggered activation).

## 3. Required Outputs (Artifacts)
- **Selected Input Description**: Description of the chosen material/task.
- **Why Optimal**: Justification based on testing breadth (Activation, Drift, Role, Boundary).
- **Anticipated Activation Route**: Predicted Line/Axis/Camera/Lens.
- **Risk Assessment**: What boundary risk might this input trigger?

## 4. Constraints
- **Select, DO NOT Implement.**
- Keep focus on testing the pipeline (not the tool's performance alone).
- Log material/task selection rationale.
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_35_HANDOFF.md` for Space Material Activation Audit.
