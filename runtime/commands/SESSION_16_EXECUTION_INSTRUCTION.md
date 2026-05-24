# SESSION_16_EXECUTION_INSTRUCTION.md

## 1. Goal
Run a bounded walkthrough of 3 test cases using the Product-Attachable VectorFL Pipeline structure to observe runtime behavior and identify necessary package-end fixes.

## 2. Test Cases to Execute
1. External Material Intake
2. Codex/OmX Structure Review
3. User Relay Burden Check

## 3. Workflow for Each Case
- Trigger identification -> Space Material search (Read-only) -> Context Bundle assembly -> Tool role assignment -> Bounded review work -> Return/Recovery -> Issue log generation.

## 4. Key Constraints
- **RUN-FIRST / PATCH-LATER.**
- **NO Implementation, NO Automation.**
- If hard boundary is hit -> STOP and flag.
- If non-blocking issue occurs -> LOG and CONTINUE.
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_17_HANDOFF.md` for Package-End Fix Review.
