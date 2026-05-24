# SESSION_41_EXECUTION_INSTRUCTION.md

## 1. Goal
Execute the second real-input trial run (Codex Structure Review) to verify if the tool performs analysis (Critique/Structure) without crossing the boundary into implementation/mutation.

## 2. Search First
- `TOOL_ROLE_PROFILES_V0.md` (Codex role: Space Reader/Critique, NOT Mutator).
- `BOUNDARY_RULES.md` (No file modification).
- `CONTEXT_BUNDLE_TEMPLATE_V0.md` (Role containment).

## 3. Required Outputs (Artifacts)
- **Bounded Tool Work**: Structure review of the input code snippet.
- **Return Package**: Digest, Evidence Used, Not Inspected, Issue Log (watch for 'patch' drift).
- **Result Card**: Usability-focused feedback.

## 4. Constraints
- **Critique/Structure ONLY.**
- **NO Implementation, NO File Modification.**
- If 'patch' or 'modification' is proposed -> Classify as `Boundary Risk`.
- Log non-blocking issues.
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_42_HANDOFF.md` for User Relay Burden Check.
