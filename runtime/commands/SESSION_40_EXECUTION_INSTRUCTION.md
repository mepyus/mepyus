# SESSION_40_EXECUTION_INSTRUCTION.md

## 1. Goal
Execute the first real-input trial run (External Article Analysis) to verify search, material activation, and context bundling flow.

## 2. Search First
- `SESSION_39_RESULTS_V0.md` (Package 5 frame).
- `SPACE_MATERIAL_ACTIVATION_MAP_V0.md` (Trigger: External Intake).
- `TOOL_ROLE_PROFILES_V0.md` (Gemini Analyst role).

## 3. Required Outputs (Artifacts)
- **Bounded Tool Work**: Analysis of the article based on VectorFL context.
- **Return Package**: Digest, Evidence Used, Not Inspected, Issue Log.
- **Result Card**: Usability-focused feedback.

## 4. Constraints
- **Search-First, Scoped-Search ONLY.**
- **NO Implementation, NO Automation.**
- Flag `BOUNDARY_RISK` if broad scan or file mod attempted.
- Log non-blocking issues.
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_41_HANDOFF.md` for Real Input Run 02.
