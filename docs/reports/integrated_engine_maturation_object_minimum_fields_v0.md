# Integrated Engine Maturation Object Minimum Fields v0

Date: 2026-04-15

## 0. purpose

This document is a working draft, not a final schema.

It defines minimum fields for maturation objects such as:

- line candidate
- axis candidate
- interpretation note
- harvest bundle
- comparison bundle
- relation memo
- reread artifact

These are meaning-maturation objects, not anchor objects and not operating processing objects.

Do not read this document as:

- final maturity enum
- final line / axis promotion rule
- evidence-density scoring system
- automatic clustering design
- canonical naming rule for all maturation objects

Read it as:

- v0 meaning-maturation grammar for low-intensity integrated-engine setup
- a minimum field set for preserving origin, position, maturity, linkage, and open edges while meaning develops

## 1. why maturation objects are separate

A maturation object is not a bottom anchor.

It is also not primarily an operating object that moves through explicit slots.

Its role is to:

- hold incoming material
- connect with other objects
- accumulate repetition and cohesion
- preserve not-yet-final meaning
- keep the possibility of later line or axis emergence

Key sentence:

> A maturation object is not a finished concept object. It is a meaning object before or during emergence, preserved so it can develop through connection, repetition, and reread.

## 2. minimum fields v0

v0 uses ten minimum fields:

- `object_id`
- `object_name`
- `object_kind`
- `origin_refs`
- `anchor_refs`
- `current_position`
- `maturity_stage`
- `linked_objects`
- `evidence_density`
- `open_edges`

These are minimum operating slots for maturation tracking, not final DB columns.

## 3. field meanings

### object_id

Unique identifier for the maturation object.

Examples:

- `line_candidate_alpha`
- `axis_probe_02`
- `harvest_bundle_round1_a`

Reason:

- The object must be reread, linked, and refluxed without losing continuity.

### object_name

Short human-readable name.

Good names should reflect current status without pretending finality.

Examples:

- 반복되는 검증-보강 흐름 후보
- 사용자면-엔진면 왕복 라인 후보
- 외부 보강 축 탐침 묶음

### object_kind

The current operating kind of the maturation object.

Examples:

- `line_candidate`
- `axis_candidate`
- `interpretation_note`
- `harvest_bundle`
- `comparison_bundle`
- `relation_memo`
- `reread_artifact`

Boundary:

- This is the current operating kind, not a final concept identity.

### origin_refs

Where this object came from.

Examples:

- user utterance
- engine return
- external material
- comparison note
- previous harvest round

Reason:

- Maturation objects become vague quickly if provenance is lost.
- This is naturally a list, not a single value.

### anchor_refs

Anchors used to read this object.

Examples:

- `integrated_engine_3_surface_baseline`
- `canonical_placement_rule`
- `packet_routing_anchor_v0`

Reason:

- Maturation objects can remain flexible.
- They should not float without reference criteria.

### current_position

Where the object currently sits in the maturation space.

Examples:

- `semantic_maturation`
- `line_candidate_zone`
- `axis_candidate_zone`
- `external_enrichment_zone`
- `reread_zone`
- `comparison_zone`

Boundary:

- This is not just a folder path.
- It is the operating position of the object.

### maturity_stage

How far the object has emerged.

Examples:

- `raw_fragment`
- `grouped`
- `candidate`
- `enriched`
- `under_reread`
- `partially_stabilized`

Boundary:

- These are working labels, not final enum values.
- The important question is not whether the object is final, but how far it has emerged.

### linked_objects

Objects connected to this maturation object.

Examples:

- related line candidates
- related axis candidates
- related comparison bundles
- related request or return packets
- related external material bundles

Reason:

- Maturation grows through connection.
- This is naturally a list.

### evidence_density

The density of evidence supporting this object.

Working labels:

- `low`
- `medium`
- `high`

Alternative working labels:

- `sparse`
- `clustered`
- `reinforced`

Boundary:

- This is not a numeric scoring model in v0.

### open_edges

Open sides that should not be prematurely closed.

Examples:

- external enrichment needed
- more comparison needed
- axis promotion judgment held
- possible line split
- user-surface reread needed

Reason:

- `open_edges` preserves the next maturation direction.
- Without this field, maturation objects close too early.

## 4. optional fields for later

These fields are useful, but not required in v0:

- `summary_note`
- `linked_lines`
- `linked_axes`
- `reflux_value`
- `reread_priority`
- `last_touched_by`
- `last_touched_reason`

Recommended later fields:

### reflux_value

How valuable this object is as future space material.

### reread_priority

How important it is to reread later.

Reason:

- Maturation objects are not finished by one pass.
- They often become valuable through repeated reread.

## 5. minimum example 1 - line candidate

```text
object_id: line_candidate_user_vector_engine_loop
object_name: 사용자면-벡터플면-엔진면 왕복 라인 후보
object_kind: line_candidate
origin_refs: [recent_dialogue_01, packet_flow_note_02]
anchor_refs: [integrated_engine_3_surface_baseline]
current_position: line_candidate_zone
maturity_stage: candidate
linked_objects: [request_packet_v0_note, return_flow_observation]
evidence_density: medium
open_edges: [external enrichment need unclear, axis promotion possibility open]
```

Reading:

- This is a line candidate.
- It may later contribute to an axis, but that is not locked.

## 6. minimum example 2 - axis candidate

```text
object_id: axis_candidate_anchor_packet_reflux
object_name: 앵커-패킷-환류 결합 축 후보
object_kind: axis_candidate
origin_refs: [anchor_discussion_note, packet_discussion_note, reflux_loop_note]
anchor_refs: [integrated_engine_3_surface_baseline, packet_routing_anchor_v0]
current_position: axis_candidate_zone
maturity_stage: enriched
linked_objects: [line_candidate_user_vector_engine_loop, comparison_bundle_03]
evidence_density: medium
open_edges: [relation to validation loop needs more work, naming not stabilized]
```

Reading:

- This object has cohesion.
- It is not yet a stable final axis.

## 7. minimum example 3 - harvest bundle

```text
object_id: harvest_bundle_round1_operating_language
object_name: 운영 언어 수확 묶음 1차
object_kind: harvest_bundle
origin_refs: [dialogue_segment_21, dialogue_segment_22, external_case_note_01]
anchor_refs: [integrated_engine_3_surface_baseline]
current_position: semantic_maturation
maturity_stage: grouped
linked_objects: [line_candidate_user_vector_engine_loop, language_signal_dict_v0]
evidence_density: medium
open_edges: [reread needed, some expressions remain working-lexicon candidates]
```

Reading:

- This is grouped language material.
- It should not be treated as final lexicon by default.

## 8. maturation review questions

When creating or reviewing a maturation object, ask:

1. Where did this object come from?
2. What kind of object is it currently read as?
3. How far has it matured?
4. What is it connected to?
5. What remains open?

If these questions cannot be answered, the object is not ready to be handled as a maturation object.

## 9. fields that should not be missing

The most important fields are:

- `origin_refs`
- `current_position`
- `maturity_stage`
- `linked_objects`

Reason:

- A maturation object must preserve where it came from.
- It must show where it currently sits.
- It must show how far it has emerged.
- It must show what it is connected to.

Without these four, maturation state and emergence potential are lost.

## 10. difference from anchor objects

Anchor objects focus on:

- `scope`
- `governs_what`
- `locked_boundary`
- `comparison_rule`

Maturation objects focus on:

- origin
- position
- maturity
- linkage
- open edges

Working contrast:

- Anchors are about fixation and comparison.
- Maturation objects are about connection and emergence.

## 11. difference from operating objects

Operating objects focus on:

- current slot
- next slot
- route movement
- movement log
- assigned executor when needed

Maturation objects focus less on slot transfer and more on:

- cohesion
- linkage expansion
- maturity change
- reread potential
- emergence into lines or axes

Working contrast:

- Operating objects are about transition.
- Maturation objects are about maturation-stage change.

## 12. lock level

### usable now

- Maturation objects are not completed concept objects.
- They are meaning objects before or during emergence.
- v0 uses ten minimum fields.
- `origin_refs`, `current_position`, `maturity_stage`, and `linked_objects` are core fields.
- `open_edges` should remain visible so the object does not close too early.

### not locked

- Full `maturity_stage` enum
- Final line / axis judgment rules
- Numeric evidence-density method
- Automatic clustering rules
- Canonical naming for every maturation object

## 13. relation to packets, operating objects, and anchors

Transfer packets can carry maturation objects as `related_objects`.

Operating objects may produce or update maturation objects during validation, return, or reflux.

Anchor objects give maturation objects comparison criteria so they do not drift without reference.

Minimum relation:

- A maturation object should preserve `origin_refs`.
- It should declare at least one relevant `anchor_ref` when possible.
- It should show where it sits now through `current_position`.
- It should preserve `open_edges` so reflux and reread remain possible.

## 14. core sentence

Maturation objects are not fixed concept objects. They are meaning-maturation targets that can emerge into lines or axes through connection, repetition, and reread.

v0 should only test whether each maturation object can preserve at least:

```text
origin_refs + current_position + maturity_stage + linked_objects
```

so maturation state and emergence potential are not lost.

