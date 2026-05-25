# Formation Layer Provisional Object Metadata Note v0

Date: 2026-04-24

## 0. purpose

This note records the current intermediate lock from the recent ontology / operating-frame discussion.

It does not define a final schema, UI design, database model, or routing state machine. It records the current reading frame for:

- A/B/C as operating frames
- T/X/R/L as deeper candidate lenses
- the formation layer and movement layer split
- provisional object families between those layers
- the minimum metadata needed before a provisional object can move

Read this as a formation-layer note that can later inform packet contracts, UI state, logs, and worker-return contracts.

## 1. current frame lock

The current stable operating frame is:

- A = precedence / permission-order principle
- B = boundary-surface / role-organization principle
- C = maturation / validation / hold grammar

This frame remains useful, but it should not be mistaken for the final ontology of the whole space.

The deeper candidate layer currently reads as:

- T = formation / ripeness / provisionality / qualification over time
- X = translation / transformation / re-expression across surfaces
- R = process / residue / detour / memory assetization
- L = lens / camera position / point-of-view structure

Current strongest candidate:

> The space tends to treat objects less as fixed finished products and more as entities that gain qualification through formation, maturation, rereading, and repeated embodiment. A and C may be structural and operational expressions of T.

## 2. T/X translation failure split

Translation failure should not be treated as one class.

### T-type failure

The object cannot yet translate because it is not sufficiently formed.

Examples:

- philosophy exists, but is not yet mature enough to become implementation instruction
- a concept exists, but has not survived repeated application enough to become a contract
- a structure exists, but is not embodied enough to produce stable expression

### X-type failure

The object is formed enough, but there is no adequate conversion structure between surfaces.

Examples:

- space language cannot yet become user-facing language
- assistant judgment cannot yet become a Codex one-shot packet
- worker return cannot yet normalize into usable JSON contract
- external reference cannot yet become internal reread-support form

Important refinement:

T and X can be sequential, not only parallel. A failure can be T-heavy early, then become X-heavy after enough maturation.

## 3. space / VectorFL / engine relation

The current reading is asymmetric coupling, not identity and not full separation.

- space = field where formation material, residue, provisional states, and reread possibility remain
- VectorFL surface = formation organ that rereads, shapes candidates, judges qualification, and prepares movement
- engine surface = movement organ that processes, validates, records trace, and returns material

Current body reading:

- identity body = formation layer centered on `space + VectorFL`
- movement body = engine surface centered movement layer

Operationally, the formation layer also needs the user surface as the access aperture:

- space = field
- VectorFL = formation organ
- user surface = access aperture

So the operational minimum formation layer is:

`user surface + space + VectorFL`

The ontological minimum formation layer is:

`space + VectorFL`

## 4. formation-to-movement interface

The interface between formation layer and movement layer is not a finished/unfinished export boundary.

It is better read as a conditional threshold that grants movement qualification to a provisional object for the current purpose.

The key conditions are:

- purpose fit
- explicit boundary
- manageable misunderstanding risk
- visible provisionality
- reread return possibility

The formation layer usually does not send a final answer. It sends an object structured enough to move.

Examples:

- executable candidate with direction
- bounded intermediate object
- partial structure with notes
- reread-supported action packet

## 5. provisional object families

### A. reread-priority object

Material that should remain inside the formation layer for further reading.

Example:

- an external reference whose subtype, merge value, or family-map position is still unclear

### B. framing candidate

A frame that has begun to connect to the current purpose, but is not yet an action packet.

Example:

- comparison frame
- upper operating principle candidate
- question-set candidate

### C. bounded action candidate

A provisional work unit that can move boundedly for the current purpose.

Example:

- Codex one-shot package draft
- bounded test packet

### D. guarded execution object

An executable object with notes, fallback, and constraints attached.

Example:

- hybrid contract trial
- execute-under-constraint object

### E. validation return object

An object that returns from movement layer into formation layer.

Example:

- Codex result
- dry-run result
- worker return
- refinement input

Grouped by layer:

- formation-layer internal objects: A, B
- interface objects: C, D
- return objects: E

The loop is:

`formation -> movement -> formation`

## 6. common minimum metadata

Provisional object metadata should not become decorative detail. Its purpose is to decide:

- whether the object must remain in formation
- whether it can move into the movement layer
- how it should return after movement

Common minimum fields:

```text
object_type
current_purpose
boundary
ripeness
confidence
note
next_allowed_move
reread_return_hook
source_trace
failure_mode
```

Field distinction:

- `ripeness` = formation maturity; primarily T-related
- `confidence` = usability for the current purpose; not the same as ripeness
- `boundary` = where the provisional object may and may not be used
- `reread_return_hook` = how the object returns to formation after movement
- `failure_mode` = likely way this object can mislead or collapse

Key rule:

> A C/D object should not move just because confidence is high. It should move only when confidence, boundary, provisionality, and reread return are all explicit enough.

Without this, the movement layer becomes a premature-promotion machine.

## 7. object-specific minimum slots

### A. reread-priority object

Minimum slots:

```text
object_type: reread_priority_object
source_trace
unresolved_question
reread_reason
boundary
next_allowed_move
```

Typical `next_allowed_move`:

```text
reread
compare
cluster
hold
```

### B. framing candidate

Minimum slots:

```text
object_type: framing_candidate
current_purpose
framing_claim
boundary
competing_frames
ripeness
next_allowed_move
```

Typical `next_allowed_move`:

```text
refine
compare
promote_to_action_candidate
hold
```

### C. bounded action candidate

Minimum slots:

```text
object_type: bounded_action_candidate
current_purpose
action_shape
boundary
expected_output
note
confidence
ripeness
next_allowed_move
```

Typical `next_allowed_move`:

```text
prepare_handoff
hold
split
return_to_framing
```

### D. guarded execution object

Minimum slots:

```text
object_type: guarded_execution_object
execution_instruction
guardrail
fallback
allowed_surface
failure_mode
validation_requirement
reread_return_hook
```

Typical `next_allowed_move`:

```text
execute_under_constraint
validate
abort_to_reread
return_with_note
```

### E. validation return object

Minimum slots:

```text
object_type: validation_return_object
execution_result
deviation
observed_failure
reusable_residue
validation_status
source_trace
next_allowed_move
```

Typical `next_allowed_move`:

```text
accept
refine
rerun
return_to_reread
deposit_as_memory_asset
```

## 8. relation to transfer packets

This note sits before and beneath transfer packets.

`integrated_engine_transfer_packet_minimum_slots_v0` defines a shared carrier between surfaces. This note defines what kind of provisional formation object may deserve to become part of such a carrier.

Useful split:

- provisional object metadata = formation qualification
- transfer packet slots = surface movement carrier
- worker return contract = movement-layer return normalization

Do not collapse these three too early.

## 9. next questions

The next productive questions are:

- Which of these fields must appear in UI, and which should remain only in logs/contracts?
- Should C and D be represented as documents, packets, UI states, logs, or contracts?
- Does the VectorFL surface need internal sub-organs for reread, candidate shaping, and handoff preparation?
- Should the user surface split into entry surface, explanation surface, and decision surface?

## 10. provisional lock sentence

The formation layer is best read as `space(field) + VectorFL(formation organ) + user surface(access aperture)`, while the movement layer is centered on the engine surface. The boundary between them is not an export point for final conclusions, but a conditional interface that grants movement qualification to provisional objects such as bounded action candidates and guarded execution objects. The minimum metadata must preserve purpose, boundary, ripeness, confidence, next move, source trace, and reread return so that execution does not become premature promotion.
