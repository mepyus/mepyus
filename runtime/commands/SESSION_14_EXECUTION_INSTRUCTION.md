# SESSION_14_EXECUTION_INSTRUCTION.md

## 1. Goal
Review the actual content of all Round 1/2 artifacts (from Session 0/1 to Session 13), stabilize the state (CONTENT_REVIEWED vs. REPORTED_COMPLETE), and determine the next action (Limited Trial or further Evidence Review).

## 2. Scope of Review
- All artifacts in `app/work/` and `runtime/commands/`.
- Verify existence, purpose-fit, cross-component linkage, and boundary integrity.

## 3. Required Outputs (Artifacts)
- **Content Review Report**: Summary of review status and overall judgment.
- **Artifact Review Table**: Mapping of artifact status, purpose fit, and action required.
- **Stabilization Patch List**: Priority patches before next action (only if blocking).
- **Updated Operator Board**: Finalized operational state based on review.
- **Next Action Decision**: Decision on proceeding to Limited Trial or holding for Evidence Review.

## 4. Constraints
- **Review content, DO NOT recreate structure.**
- Distinguish between "Reported Complete" and "Reviewed Complete".
- Keep boundaries closed (No implementation, No automation).
- Log evidence gaps.

## 5. Next Handoff
Prepare for the next chosen action (e.g., `LIMITED_REAL_CODEX_OMX_TRIAL_PREP`).
