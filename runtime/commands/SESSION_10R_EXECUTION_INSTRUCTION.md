# SESSION_10R_EXECUTION_INSTRUCTION.md

## 1. Goal
Patch `SECOND_PASS_RECOMPOSITION_V0` using `ROUND_1_CLOSEOUT_AND_EVIDENCE_REVIEW` findings to ensure the system is ready for the Second Pass run without unnecessary rebuilds.

## 2. Search First
- `ROUND_1_CLOSEOUT_V0` (Summary, Consistency Review, Preserve/Fix/Hold Table).
- `CLI_SESSION_PROTOCOL_V0` (Session logic to be patched).
- `REVIEW_RECOVERY_GATE_V0` (Classification granularity gaps).
- Previous drift findings (Codex implementation drift, Gemini wording drift).

## 3. Required Outputs (Artifacts)
- **Patch Summary**: Summary of preservation, patched items, and readiness conditions.
- **Drift Patch Table**: Corrective actions for identified drifts.
- **Review Gate Patch**: More granular judgment classifications.
- **Second Pass Ready Board**: Compact operator board.

## 4. Constraints
- **Patch, NOT Redesign.**
- **Preserve User Judgment.**
- No implementation, No automation.
- Log non-blocking issues.
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_11_HANDOFF.md` for Second Pass Run session.
