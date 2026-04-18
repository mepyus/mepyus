# Integrated Engine Precedent Mining to Decision Bridge v0

## Status

PASS_WITH_NOTE

This bridge turns mined fragments into a bounded decision.
It does not create a camera, axis, glossary, canonical record, UI implementation, or automation.

## Decision Questions

Ask before choosing a branch:

- Is this frame-level evidence or only content-specific material?
- Does an existing camera slot already read it?
- Is a new lens needed, or do existing lenses compose well enough?
- Is the case actually a target-shape difference?
- Is the precedent weak while the naming sounds attractive?
- Is this a false precedent?

## Decision Branches

### 1. Reuse Existing Camera

- choose when: C0-C6 can read the target without naming changes or new slot behavior.
- required evidence: content-bearing target, slot fit, no unhandled rollback signal.
- common false positive: repeated content theme mistaken for frame fit.
- immediate next step: use current usage procedure with match/partial/missing.
- record: source fragments, slot fit, lens used, rollback signals checked.
- rollback condition: frame forcing, low reuse value, mismatch opacity.

### 2. Vary Existing Camera

- choose when: frame roles hold but naming, order, or slot emphasis needs bounded variation.
- required evidence: frame-level match survives content variation.
- common false positive: target-specific rewrite called camera variation.
- immediate next step: draft variation note, not promotion.
- record: base frame, varied slots, reason for variation, affected target shapes.
- rollback condition: content overgeneralization or scope collapse.

### 3. Reuse Or Attach Lens Only

- choose when: camera frame is enough, but the reading purpose changes.
- required evidence: existing lens or lens combination answers the verification question.
- common false positive: lens name becomes a new camera.
- immediate next step: update lens-slot compatibility or run lens-specific review.
- record: lens id, target slots, expected return, invalid shape.
- rollback condition: lens covers too many slots or becomes glossary.

### 4. Asset-Specific Reading, No Camera Expansion Yet

- choose when: target has useful local pattern but not enough transfer evidence.
- required evidence: local usefulness, weak transferability, or target-shape mismatch.
- common false positive: asset-specific pattern treated as reusable frame.
- immediate next step: write asset-specific note or support object record.
- record: what worked locally, why not reusable, future reread condition.
- rollback condition: later evidence shows repeated frame-level match.

### 5. Truly New Camera/Lens Candidate Needed

- choose when: mined precedents do not cover the case and existing slots/lenses cannot read it without forcing.
- required evidence: failed reuse/variation/lens-only/asset-specific checks; multiple content-bearing examples or a very clear operational gap.
- common false positive: attractive naming or one isolated case.
- immediate next step: create candidate review brief, not promotion.
- record: missing precedents, failed branches, target-shape evidence, rollback rule.
- rollback condition: new evidence shows existing camera/lens was sufficient.

## Branch Comparison

| branch | default? | promotion allowed? | valid endpoint? |
|---|---|---|---|
| reuse existing camera | yes if evidence supports | no | yes |
| vary existing camera | yes if frame holds but content shifts | no | yes |
| reuse or attach lens only | yes if purpose shift is lens-level | no | yes |
| asset-specific reading | yes if transfer is weak | no | yes |
| truly new candidate | last resort | no | yes, review-only |

New camera/lens candidate is last resort.
Asset-specific reading is a valid endpoint, not a failure.

## Target-Shape Connection

Before any branch:

1. confirm target shape
2. reject intake-note-only as full evidence
3. classify support-only material separately
4. only then choose reuse / variation / lens-only / asset-specific / new candidate

## Mandatory Verification

- new camera branch is not default: yes.
- reuse/variation is connected to target-shape gate: yes.
- asset-specific remains a valid endpoint: yes.
- false precedent must be checked before branch decision: yes.

## Pointers

- Protocol: `docs/reports/integrated_engine_internal_camera_lens_precedent_mining_protocol_v0.md`
- Taxonomy: `docs/reports/integrated_engine_precedent_fragment_taxonomy_v0.md`
- Excavation discipline: `docs/reports/integrated_engine_precedent_excavation_discipline_v0.md`
