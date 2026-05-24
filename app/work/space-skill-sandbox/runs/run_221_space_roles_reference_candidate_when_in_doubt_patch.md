# Run 221 - Space Roles Reference Candidate When in Doubt Patch

## 1. Patch Purpose

Applied a minimal wording patch to improve quick-use clarity and reduce baseline/authority drift in the Roles reference candidate.

This patch follows:

```text
app/work/space-skill-sandbox/runs/run_220_space_roles_reference_candidate_review.md
```

## 2. File Modified

```text
app/work/space-skill-sandbox/outputs/space_roles_reference_candidate_v0.md
```

## 3. Exact Section Added

Added near the top, after Document Status and before Why This Document Exists:

```markdown
## When in Doubt

Use this reference to prevent role confusion, not to grant authority.

If a material is useful, treat it as a candidate reference until the User explicitly promotes it.
If a risk is repeated, treat it as a watch item until the User explicitly turns it into a rule.
If a worker can do something, do not treat that capability as permission.
If a run record exists, do not treat it as approval.
If a current-position or summary points somewhere, do not treat it as a registry, index, or task queue.
If a principle sounds right, do not treat it as policy.
If a helper reduces friction, do not treat it as workflow or automation.

When unsure, stop and ask for User purpose or User decision.
```

## 4. Why This Patch Is Safe

```text
The patch only adds a quick-use clarification section.
It does not rename the document.
It does not change status from CANDIDATE_REFERENCE.
It does not alter the role table.
It does not add baseline, workflow, protocol, schema, automation, or permission-system language.
It reinforces User decision and no-promotion boundaries already present in the document.
```

## 5. What Was Not Changed

```text
Document title unchanged
Document status unchanged
Role table unchanged
Reread matrix unchanged
Promotion rule unchanged
Boundary confirmation unchanged
No package status changed
No current-position entry changed
```

## 6. Current-Position Decision

```text
NO_CURRENT_POSITION_UPDATE_REQUIRED
```

Reason:

```text
This is a minimal wording patch to an existing candidate reference. It does not change the active anchor, move packages, approve packages, approve Run 117, or create a new operating authority.
```

## 7. Recommendation After Patch

```text
KEEP_AS_ROLE_REFERENCE_CANDIDATE
```

## 8. Boundary Confirmation

```text
no baseline promotion
no official workflow creation
no architecture finalization
no source-space policy creation
no interface schema creation
no automation/router/controller
no registry/index/ledger promotion
no formal permission system
no Package 034/035/036 movement
no Package approval
no Run 117 approval
no Gemini broad run
no Codex implementation authority
no current-position update unless explicitly required
```

`STATUS: SPACE_ROLES_REFERENCE_WHEN_IN_DOUBT_PATCH_COMPLETE`
