# SESSION_4_EXECUTION_INSTRUCTION.md

## 1. Goal
Create `CONTEXT_BUNDLE_TEMPLATE_V0`, `CONTEXT_BUNDLE_TYPES_V0`, `CONTEXT_BUNDLE_ASSEMBLY_FLOW_V0`, and `CONTEXT_BUNDLE_EXAMPLES_V0` to formalize how activated materials are packaged for external tools.

## 2. Search First
- Existing Context Bundle/Handoff records.
- Space Material Activation Map & Material Family Index (Session 2).
- Tool-Readable Surface rules (Session 3).
- Tool drift records (Codex/Gemini implementation drift).

## 3. Required Outputs (Artifacts)
- **Context Bundle Template**: Fields (bundle_id, user_purpose, activation_trigger, related_line, etc.).
- **Bundle Types (6+)**: Intake, Codex Review, Gemini Analysis, Boundary Review, Surface Revision, Issue Review.
- **Assembly Flow**: User Purpose -> Activation -> Packaging -> Handoff -> Recovery.
- **Examples (3+)**: External Intake, Codex Review, Boundary Risk Review.

## 4. Constraints
- **Bounded Handoff Object**, not whole-project dump.
- **Not a Controller, Not Automation.**
- Keep focus on "Read-Interpret-Propose" workflow.
- Log non-blocking issues.
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_5_HANDOFF.md` for Tool Role Profiles session.
