# SESSION_6_EXECUTION_INSTRUCTION.md

## 1. Goal
Create `CLI_SESSION_PROTOCOL_V0`, `SESSION_START_CHECKLIST_V0`, `SESSION_RETURN_FORMAT_V0`, and `SESSION_DRIFT_RESPONSE_RULES_V0` to formalize the standardized operation of bounded pipeline sessions.

## 2. Search First
- Session operation records (Session 0-5).
- Existing tool drift reports (Implementation, Controller drift).
- Review Gate logic and Recovery classifications.
- Hand-off structures used in previous passes.

## 3. Required Outputs (Artifacts)
- **CLI Session Protocol**: The standardized template for every session (session_id, session_goal, work_steps, etc.).
- **Start Checklist**: Mandatory 13-point pre-flight checklist for CLI tools.
- **Return Format**: 4-Line Judgment Card, Package Digest, Issue Log, Handoff rules.
- **Drift Response Rules**: Mapping signal phrases to responses for 10+ drift categories.

## 4. Constraints
- **Standardized Procedure**, not automation.
- **Search-First Pipeline**: Tools MUST search the space before proposing work.
- Keep focus on "Read-Interpret-Propose" workflow.
- Log non-blocking issues.
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_7_HANDOFF.md` for Review & Recovery Gate session.
