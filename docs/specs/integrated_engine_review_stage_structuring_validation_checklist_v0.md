# Integrated Engine Review-Stage Structuring Validation Checklist v0

## 1. Purpose

This checklist tests whether a review-stage document using the micro-template is inspectable and bounded.

It does not authorize rollout.
It does not promote the camera.
It does not validate line, axis, or camera-slot reread.

## 2. Result Scale

Use only:

- `directly`: readable in concrete bounded form from the note itself
- `weakly`: visible but depends on inference or surrounding interpretation
- `not yet`: not meaningfully supported

## 3. Checklist

### Grounding Check

Question:

- Does `base_content_trace` preserve enough material trace for a later supervisor reread?

Result:

- `directly` if source basis, evidence, and boundary material are named clearly
- `weakly` if source basis is present but evidence chain is source-level only
- `not yet` if the field only summarizes or names no grounding material

### Lens Check

Question:

- Does `applied_lens_record` show the reading angle that shaped the judgment?

Result:

- `directly` if primary and supporting lenses are named with their effect on judgment
- `weakly` if lens names exist but their effect is unclear
- `not yet` if it only says the item was reviewed

### Principle Check

Question:

- Does `structural_principle` state a shaping rule rather than a retrospective summary?

Result:

- `directly` if it states required coupling, status separation, or guard logic
- `weakly` if it is partly rule-like but mostly summary
- `not yet` if it restates the conclusion only

### Boundary Check

Question:

- Does `what_this_is_not` block overreading and authority drift?

Result:

- `directly` if promotion, rollout, canonicalization, and invalid reuse are blocked
- `weakly` if only some authority drift is blocked
- `not yet` if boundaries are absent or vague

### Review Guideline Reread Check

Question:

- Can the note be reread as a review-stage guideline without inventing a new protocol?

Result:

- `directly` if eligible / not-promoted / rollback-only or equivalent states remain distinct
- `weakly` if guideline material exists but must be manually reconstructed
- `not yet` if no review-stage guideline path is visible

### Rollback Rule Reread Check

Question:

- Can the note be reread into rollback-rule-like handling inside review-stage?

Result:

- `directly` if rollback cue grouping and rollback boundary are locally readable
- `weakly` if rollback cues exist but are scattered
- `not yet` if rollback is absent or only implied by caution language

## 4. Required Risk Checks

### Promotion Drift

- Does any field imply that review eligibility equals camera promotion?
- If yes, result cannot exceed `not yet` until corrected.

### Rollout Drift

- Does the note authorize reuse across documents?
- If yes, result cannot exceed `not yet` until bounded.

### Template Overgeneralization

- Is the micro-template being treated as global?
- If yes, result must be downgraded.

### Evidence Thinning

- Are claims present without source or evidence path?
- If yes, mark `weakly` or `not yet`.

### Shadow-Fit False Positive

- Does a candidate look similar by wording but lack review-stage grounding?
- If yes, keep shadow-fit only and do not patch.

## 5. Phase 2 Validation

Micro-template boundary check:

- review-stage bounded? required
- global protocol language? forbidden
- rollout language? forbidden

Checklist usability check:

- can inspect current target note without inventing new categories? yes
- can separate `directly`, `weakly`, and `not yet`? yes

