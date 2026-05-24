# SESSION_15_EXECUTION_INSTRUCTION.md

## 1. Goal
Patch `TOOL_READABLE_SURFACE_V0` and `CONTEXT_BUNDLE_TEMPLATE_V0` based on the stabilization findings from Session 14, ensuring the pipeline is ready for limited trial preparation without structural redesign.

## 2. Search First
- `CONTENT_REVIEW_AND_STABILIZATION_V0` (Review gaps, Artifact content review).
- Tool-Readable Surface vs. Controller boundary logic.
- Context Bundle usage in 1st/2nd pass runs.
- Identified recurring drift patterns.

## 3. Required Outputs (Artifacts)
- **Patch Summary**: What was patched and why.
- **Surface Patch**: Clarification on "No Controller" role for Surface.
- **Bundle Patch**: Clarification on bounded handoff (not full project dump).
- **Trial Entry Check**: Final classification for `LIMITED_TRIAL_PREP`.

## 4. Constraints
- **Patch, NOT Redesign.**
- Keep boundaries closed (No implementation, No automation).
- Do not claim readiness/finality.
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_16_HANDOFF.md` for Limited Trial Preparation.
