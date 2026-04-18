# Integrated Engine Rollback Reread Consolidation Decision Note v0

## 1. Verdict

Verdict: PASS_WITH_NOTE

The current rollback rule reread support should not remain only as scattered weak support.
A minimal consolidation patch is justified, but not implemented in this step.

This decision does not promote the camera.
It does not expand the schema to other documents.
It does not create a new protocol.

## 2. Current State

Current reread support:

- `review guideline reread` = directly
- `rollback rule reread` = weakly

The review guideline path is already readable because the patched note clearly separates `eligible`, `not promoted`, and `rollback-only` review states.

The rollback rule path is visible, but it depends on gathering cues from multiple places:

- `base_content_trace`
- `applied_lens_record`
- `structural_principle`
- `layer_reapplication_hint`
- `what_this_is_not`
- blocker notes
- authority boundary notes

## 3. Decision

Decision:

```text
minimal consolidation patch justified
```

## 4. Reason

The existing rollback cues are real and already evidence-backed, but they are too scattered to function reliably as reread material.

Evidence from the existing notes:

- The rollback validation note found the result to be `weakly`, not `directly`.
- The strongest rollback-like material is split between rollback boundary checks, `rollback-detection lens`, rollback discipline, partial/missing judgment, rollback destinations, and invalid target boundaries.
- The valid scope lock note keeps the proof review-stage bounded and warns against broader rollout.
- The source review note already says rollback discipline must remain attached and that intake-note-only / metadata-only / pointer-only / scaffold-only targets are not full probe-valid material.

Because the material already exists, a small local consolidation would improve rereadability without changing verdict, authority, or document role.
The purpose would be to gather existing rollback cues, not to invent a rollback system.

## 5. If Patch Were Justified

Maximum safe patch shape:

Add one short local section inside the existing review note that consolidates already-present rollback cues under a bounded review-stage heading.
The section should only restate the current rollback conditions, such as invalid target shape, forced slot reading, hidden partial/missing status, and promotion-like drift.
It should also restate the permitted rollback destination as review-stage hold / rollback-only / not-promoted preservation.
It must not introduce a new protocol, new status, new camera authority, or broader schema rollout.

No patch text is provided here.
No implementation is performed in this decision note.

## 6. Authority Boundary

This decision does not promote the camera.

This decision does not authorize broader schema rollout.

This decision does not create a new protocol.

This decision does not validate line, axis, or camera-slot reread paths.

This decision only says that a minimal local consolidation patch is justified if the next step chooses to patch the same review note.

## 7. Final Lock

The status remains:

```text
eligible for provisional camera candidate
not promoted
```

