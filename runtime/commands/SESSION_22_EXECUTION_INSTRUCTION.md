# SESSION_22_EXECUTION_INSTRUCTION.md

## 1. Goal
Test if `TOOL_READABLE_SURFACE_V0` acts effectively as an instruction surface for external tools, verifying adherence to reading order, purpose understanding, and boundary constraints without broad-scanning.

## 2. Search First
- `TOOL_READABLE_SURFACE_V0.md` (Target surfaces).
- `CLI_SESSION_PROTOCOL_V0.md` (Protocol expectations).
- Previous issues with tool implementation drift.

## 3. Required Outputs (Artifacts)
- **Compatibility Result**: Summary of how well the tools read/understand the surface.
- **Drift Observations**: Any cases where tools attempted to bypass rules (e.g., broad scan attempts).
- **Instruction Quality**: Feedback on whether the surface is too long or ambiguous.
- **Next Action Recommendation**: Patching the surface vs. preparing for procedure testing.

## 4. Constraints
- **Test Reading, NOT Implementation.**
- No modification of files unless approved.
- Preserve first-pass momentum (Log issues instead of stopping).
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_23_HANDOFF.md` for Procedure Skill Test.
