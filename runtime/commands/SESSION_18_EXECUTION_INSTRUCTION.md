# SESSION_18_EXECUTION_INSTRUCTION.md

## 1. Goal
Apply the Fix-Now patch (ISS-05: Broad Scan Boundary) and execute the second limited trial walkthrough (3 cases) to verify the patch effectiveness.

## 2. Search First
- `ISSUE_CLASSIFICATION_TABLE_V0` (ISS-05 status).
- `FIX_NOW_PLAN_V0` (Specific patch details).
- `TOOL_ROLE_PROFILES_V0` (Codex profile to patch).
- Current Operator Board status.

## 3. Required Outputs (Artifacts)
- **Fix Now Applied**: Documentation of the applied boundary patch.
- **Case Results (3)**: Results of External Intake, Codex Review, User Relay Burden Check with the patch applied.
- **Broad Scan Drift Review**: Verification of whether the patch stopped the broad scan drift.
- **User Relay Burden Review**: Current status of relay burden.
- **Issue Log**: Logged issues from the run (Do NOT stop to fix).
- **Package Digest**: Summary of trial performance.

## 4. Constraints
- **RUN-FIRST / PATCH-LATER.**
- **NO Implementation, NO Automation.**
- Apply Fix Now items strictly.
- Log non-blocking issues.
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_19_HANDOFF.md` for the next review stage.
