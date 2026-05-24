# SESSION_8_EXECUTION_INSTRUCTION.md

## 1. Goal
Create `FIRST_FULL_PASS_PLAN_V0`, `FIRST_PASS_FLOW_V0`, `FIRST_PASS_SESSION_SEQUENCE_V0`, `FIRST_PASS_TEST_CASES_V0`, `FIRST_PASS_STOP_AND_CONTINUE_RULES_V0`, and `POST_PASS_REVIEW_INPUT_V0` to formalize the one-time walkthrough of the constructed pipeline.

## 2. Search First
- All previously generated session records (Session 0-7).
- First/Second pass operation records in the space.
- Known drift/failure cases (Codex/Gemini implementation drift).

## 3. Required Outputs (Artifacts)
- **First Full Pass Plan**: Definitions for pass_id, scope, session_sequence, criteria, etc.
- **Flow/Sequence**: Step-by-step walkthrough (User Purpose -> Activation -> Packaging -> Handoff).
- **Test Cases (5+)**: External Intake, Codex/OmX Review, Gemini Output, Boundary Risk, Program Continuity.
- **Stop/Continue Rules**: Explicit triggers for halting vs. logging.
- **Post-Pass Review Input**: Structuring what Session 9 needs to fix/refine.

## 4. Constraints
- **Connected Walkthrough**, not final standard or readiness.
- No implementation, No automation, No runner/script.
- Keep momentum; log non-blocking issues.
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_9_HANDOFF.md` for Post-Pass Review & Fix session.
