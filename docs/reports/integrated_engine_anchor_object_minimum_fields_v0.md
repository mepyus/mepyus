# Integrated Engine Anchor Object Minimum Fields v0

Date: 2026-04-15

## 0. purpose

This document is a working draft, not a final schema.

It defines minimum fields for anchor objects.

Anchor objects are the bottom reference points that let other objects keep their position, boundary, and comparison criteria.

Do not read this document as:

- final anchor type enum
- final anchor hierarchy
- automatic drift detection
- DB schema
- full asset tagging requirement

Read it as:

- v0 reference grammar for low-intensity integrated-engine setup
- a minimum field set for deciding whether another object is in scope, out of scope, role-aligned, or drifting

## 1. why anchor objects are separate

An anchor object is not primarily a meaning-producing object.

Its role is to show:

- where meaning should attach
- what is allowed
- what is prohibited
- where a current object has drifted from the baseline

Anchor objects provide three things:

- comparison criteria
- boundaries
- position judgment criteria

Key sentence:

> An anchor object is not a direct producer of meaning. It is a bottom reference point that lets other objects be compared by position, allowed range, and role fit.

## 2. minimum fields v0

v0 uses eight minimum fields:

- `anchor_id`
- `anchor_name`
- `anchor_scope`
- `anchor_role`
- `governs_what`
- `locked_boundary`
- `comparison_rule`
- `change_rule`

These are minimum reference slots, not final DB columns.

## 3. field meanings

### anchor_id

Unique identifier for the anchor.

Examples:

- `integrated_engine_3_surface_baseline`
- `canonical_placement_rule`
- `page_composition_return_baseline_v1`

### anchor_name

Human-readable short name.

Examples:

- 통합엔진 3면 기준선
- canonical placement 규칙
- 페이지 구성 기준선

### anchor_scope

The range this anchor governs.

Examples:

- `whole_system`
- `user_surface`
- `vectorfl_surface`
- `engine_surface`
- `packet_routing`
- `placement_only`
- `validation_only`

Reason:

- Scope helps decide which anchor has authority when anchors appear to conflict.

### anchor_role

The kind of reference point this anchor provides.

Examples:

- `top_principle`
- `structure_baseline`
- `placement_anchor`
- `boundary_anchor`
- `routing_anchor`
- `evaluation_anchor`

Reason:

- Role answers what kind of judgment this anchor can support.

### governs_what

The concrete object, behavior, or boundary governed by this anchor.

Examples:

- three-surface role separation
- canonical asset placement
- transfer packet boundary
- validation transition condition
- screen panel classification criteria

Reason:

- `anchor_scope` says where the anchor applies.
- `governs_what` says what it actually controls.

### locked_boundary

The boundary that should not be casually crossed.

Examples:

- Do not mix user surface, VectorFL surface, and engine surface roles.
- Do not bypass VectorFL review before engine processing.
- Do not promote temporary generated output into canonical placement.
- Do not skip validation before closure.

Reason:

- This field turns the anchor from explanation into an operating boundary.

### comparison_rule

How another object should be compared against this anchor.

Examples:

- position match / mismatch
- inside allowed scope / out of scope
- role fit / role conflict
- baseline proximity / drift detected

Reason:

- Without comparison rules, anchor references become decorative labels.

### change_rule

How the anchor can be changed.

Examples:

- `controlled_revision_only`
- `explicit_unlock_required`
- `comparative_evidence_required`
- `supervisor_approval_required`

Reason:

- An anchor is a fixed device, but not necessarily eternal.
- Change must be controlled so the anchor does not drift emotionally or casually.

## 4. optional fields for later

These fields are useful, but not required in v0:

- `parent_anchor`
- `related_anchors`
- `priority_level`
- `anchor_status`
- `canonical_examples`
- `drift_signals`

Recommended later fields:

### parent_anchor

The higher-level anchor this anchor belongs under.

Example:

- `CONSTITUTION`

### drift_signals

Signals that show an object may be drifting away from this anchor.

Examples:

- surface role mixing
- validation skipped
- placement mismatch
- packet purpose unclear

Reason:

- This can later support validation, monitoring, and review work.

## 5. minimum example 1 - integrated engine three-surface baseline

```text
anchor_id: integrated_engine_3_surface_baseline
anchor_name: 통합엔진 3면 기준선
anchor_scope: whole_system
anchor_role: structure_baseline
governs_what: user surface / VectorFL surface / engine surface role separation
locked_boundary: do not mix surface roles
comparison_rule: compare whether each asset, request, packet, or panel belongs to the correct surface role
change_rule: explicit_unlock_required + comparative_evidence_required
```

Reading:

- This is the representative anchor for reading the whole integrated-engine body.

## 6. minimum example 2 - canonical placement rule

```text
anchor_id: canonical_placement_rule
anchor_name: canonical placement 규칙
anchor_scope: placement_only
anchor_role: placement_anchor
governs_what: asset landing position and canonical path
locked_boundary: do not promote temporary output or generated output directly into canonical placement
comparison_rule: compare current position against canonical position
change_rule: controlled_revision_only
```

Reading:

- This anchor helps decide whether an asset is in the right place or still provisional.

## 7. minimum example 3 - packet routing anchor v0

```text
anchor_id: packet_routing_anchor_v0
anchor_name: 전달 패킷 라우팅 기준
anchor_scope: packet_routing
anchor_role: routing_anchor
governs_what: request / return / reflux packet movement between surfaces
locked_boundary: do not move from inbox directly to engine_processing
comparison_rule: compare whether the packet route follows the v0 movement loop
change_rule: controlled_revision_only
```

Reading:

- This anchor supports operating-object movement without turning v0 into final automation.

## 8. anchor review questions

When creating or reviewing an anchor, ask:

1. What is this anchor a reference point for?
2. How far does this anchor apply?
3. What does this anchor prohibit?
4. How does this anchor compare other objects?
5. How can this anchor be changed?

If these questions cannot be answered, the object is not ready to function as an anchor.

## 9. fields that should not be missing

The most important fields are:

- `anchor_scope`
- `governs_what`
- `locked_boundary`
- `comparison_rule`

Reason:

- An anchor must say where it applies.
- It must say what it governs.
- It must say where the boundary is.
- It must say how comparison happens.

Without these four, an anchor is only a label.

## 10. lock level

### usable now

- Anchor objects are comparison / boundary / position-judgment reference points.
- v0 uses eight minimum fields.
- `anchor_scope`, `governs_what`, `locked_boundary`, and `comparison_rule` are core fields.
- Anchors are not unchangeable forever; they need controlled change rules.

### not locked

- Full `anchor_type` enum
- Full anchor hierarchy
- Automatic drift detection rules
- DB column structure
- Converting every document into an anchor

## 11. relation to packets and operating objects

Transfer packets use `anchor_refs` so purpose, directionality, validation, and reflux need can be read against stable criteria.

Operating objects use anchors to decide whether a movement is allowed or whether it should rewind to VectorFL review, validation, or external support.

Minimum relation:

- A request packet should know which anchors it relies on.
- A validation step should compare return material against relevant anchors.
- A closed operating loop should be able to say which anchor made closure acceptable.

## 12. core sentence

Anchor objects are not direct meaning producers. They are bottom reference points that let other objects be compared by position, allowed range, and role fit.

v0 should only test whether each anchor can provide at least:

```text
scope + governs_what + locked_boundary + comparison_rule
```

as a practical comparison basis.

