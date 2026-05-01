# Camera Support Bundle v0 Spec

## Verdict

`PASS_WITH_NOTE`

## Purpose

`camera_support_bundle_v0` is a lower-side `evidence_only` support artifact.

It exists to record:

- which camera-like observation surface may be viable later;
- what bounded lower evidence supports that viability;
- what is still missing before any stronger upper reading.

It is explicitly **not**:

- a verdict;
- a lens result;
- an axis;
- a promotion decision;
- a packet candidate.

It is a lower-side observation-possibility support artifact.

## Minimum Camera Set

### 1. Change Camera

Lower-side meaning:

- shift / before-after;
- recast / reinterpretation;
- scope revision;
- local movement or repositioning pressure.

This camera does not conclude what the change means. It only records that change-oriented observation is supportable.

### 2. Boundary Camera

Lower-side meaning:

- hold / not-yet;
- `evidence_only`;
- thin / weak / unknown;
- spec-first / light-patch-only;
- rollback or non-promotion cues.

This camera does not conclude policy or final lock. It only records that a boundary-sensitive observation is supportable.

### 3. Flow Camera

Lower-side meaning:

- sequence / chain;
- layer position;
- handoff / carry-forward;
- insertion between layers;
- organ or runtime placement cues.

This camera does not conclude final structural meaning. It only records that flow-sensitive observation is supportable.

## Minimum Meaning Slots

The slot names are provisional, but the semantic slots should be stable.

### Identity and Trace

- `camera_support_id`
- `source_ref`
- `source_unit_refs` or `upstream_artifact_refs`
- `upstream_support_refs`

### Core Summary

- `camera_signal_summary`
- `classification`

`classification` must be:

- `evidence_only`

### Change Support Slot

- `change_signal_strength`
- `change_support_note`
- `change_signal_refs`

Meaning:

- whether change-like observation support exists;
- what lower evidence points toward that support;
- how thin or partial it is.

### Boundary Support Slot

- `boundary_signal_strength`
- `boundary_support_note`
- `boundary_signal_refs`

Meaning:

- whether hold/not-yet/evidence-only/non-promotion pressure is visible;
- what lower evidence supports it;
- where the boundary remains weak.

### Flow Support Slot

- `flow_signal_strength`
- `flow_support_note`
- `flow_signal_refs`

Meaning:

- whether sequence/layer/handoff/insertion observation is supportable;
- what lower evidence supports it;
- where continuity is still thin.

### Insufficiency / Gap Slot

- `insufficiency_note`
- `missing_context`
- `not_ready_for_lens_reason`

Meaning:

- what is missing before stronger upper reading;
- what context span is absent;
- why this must remain support-only.

### Carry-Forward Handle

- `carry_forward_handle`

Meaning:

- a short handoff pointer for upper-side reread;
- not an interpretation result;
- not a packet seed.

## Strength and Expression Rules

Allowed expression style is weak or provisional only.

Allowed strengths:

- `has_signal`
- `thin`
- `insufficient`
- `unclear`
- `weak`
- `medium`

Not allowed:

- hard yes/no judgment;
- final confidence;
- strong conclusion language;
- axis-like naming.

Rule:

- if support is sparse, say `thin` or `insufficient`;
- if support conflicts locally, say `unclear`;
- if support is bounded but usable, say `weak` or `medium`;
- never imply promotion by naming the camera signal too strongly.

## Forbidden Moves

Lower-side must not:

- store lens conclusions in this artifact;
- store axis naming in this artifact;
- store precursor/held-axis judgment in this artifact;
- imply promotion;
- treat the artifact as packet-worthy;
- override lower readiness;
- bypass `evidence_only`.

## Boundary With Neighbor Layers

### Compared with Content-Role

Content-role says:

- what a chunk is doing.

Camera support says:

- what observation mode may later read this chunk/bundle meaningfully.

### Compared with Line Seed

Line seed says:

- what local pressure or linkage is forming.

Camera support says:

- which camera can later inspect that pressure or linkage.

Camera support is downstream of content-role and line seed. It should not replace either.

## Upper Handoff Rule

Upper-side may use this artifact only as:

- evidence support;
- observation cue;
- reread hint;
- context-span reminder.

Upper-side must not treat it as:

- lens output;
- axis precursor by itself;
- held axis basis by itself;
- packet candidate.

Allowed handoff posture:

```text
lower camera support
-> upper reread cue
-> lens reading
-> precursor / held-axis judgment elsewhere
```

## Why This Partition Exists

If camera support starts carrying lens meaning, lower and upper collapse into one layer.

If camera support starts carrying axis naming, support becomes premature organization.

If camera support becomes packet-worthy, the bridge minimum is silently bypassed.

The artifact must therefore stop at observation possibility.

## Compatibility With Current Working Core

This spec does not:

- change baseline or constitution;
- change the Phase 1.13 working core;
- change Phase 1.14 classifier semantics;
- change lower readiness;
- change bridge minimum;
- change four-artifact spine;
- change promotion logic.

It fits the current core because it stays:

- lower-side;
- additive;
- `evidence_only`;
- support-only.

## Short Note On Future Fit

Future implementation may let this artifact sit beside:

- `lower_support_layers`;
- observer ingest generated companions;
- preprocess comparison support companions;
- existing classifier as `lower_support_layer`.

But this document does not require that implementation now.

## Thin Points In The Current Spec

1. `change/boundary/flow` signal strengths are still semantically clearer than lexically locked.
2. `carry_forward_handle` is conceptually useful but still underspecified for exact formatting.
3. The threshold between `thin` and `weak` is not yet operationalized.

## Next Implementation Candidates

1. Add `camera_support_bundle` as a companion/generated support artifact over current role+seed outputs.
2. Add bounded emitter logic for observer/preprocess families using `change/boundary/flow` support slots only.

## Risk If Implemented Too Early

1. The emitter may leak lens interpretation into lower artifacts if slot discipline is weak.
2. The bundle may be mistaken for packet-worthy support unless classifier/file-family handling stays conservative.
