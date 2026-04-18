# Integrated Engine Operating Object Slot Movement Rules v0

Date: 2026-04-15

## 0. purpose

This document is a working draft, not a final state machine.

It defines minimum slot-movement rules for operating objects such as:

- request
- handoff package
- review brief
- validation request
- return package
- processing manifest

These are operating processing objects, not maturation objects.

Do not read this document as:

- final enum set
- final routing automation
- DB schema
- full exception map
- team assignment lock

Read it as:

- v0 movement grammar for low-intensity integrated-engine operation
- a guard against skipping VectorFL review, validation, and return judgment

## 1. why slot movement rules exist

Operating objects are different from maturation objects.

Maturation objects can:

- connect and grow
- be reread later
- become line or axis candidates
- preserve provenance and anchor references while meaning develops

Operating objects instead need to preserve:

- who received the object
- where it is now
- where it should move next
- why it moved
- when the current loop closes

Key sentence:

> Operating processing objects are not primarily objects that grow by meaning maturation. They are objects that must move through explicit slots while preserving processing state and next action.

## 2. base slots v0

v0 uses seven base slots:

- `inbox`
- `vectorfl_review`
- `engine_processing`
- `external_support`
- `validation`
- `return_ready`
- `closed`

### inbox

The request has entered, but has not yet been routed or mediated.

### vectorfl_review

The VectorFL surface reads purpose, directionality, anchor references, and validation points.

### engine_processing

The engine surface is processing an explicit operating unit.

### external_support

External search, enrichment, or optional tool support is needed.

### validation

Returned or intermediate material needs checking, comparison, and judgment.

### return_ready

The return is ready to send to the user surface, next operator, or next route.

### closed

The current operating loop is closed.

Boundary:

- `closed` is current-loop closure, not permanent deletion.
- A closed object can lead to a new request packet or a reflux packet.

## 3. default route

The default v0 route is:

```text
inbox
-> vectorfl_review
-> engine_processing
-> validation
-> return_ready
-> closed
```

This is the basic processing loop.

Important:

- An operating object should not jump directly from user intake to engine processing.
- The VectorFL surface must read directionality, anchors, and validation points first.

## 4. external support route

When external support is needed, the route can branch:

```text
vectorfl_review
-> external_support
-> validation
-> return_ready
```

or:

```text
engine_processing
-> external_support
-> validation
```

External support is not an endpoint.

It is a support slot that must return to validation.

## 5. core principles

### principle 1 - inbox does not go directly to engine_processing

`inbox -> engine_processing` is not allowed in v0.

Reason:

- Purpose must be checked.
- Directionality must be shaped.
- Anchor references must be attached.
- Validation points must be set.

Without this, execution falls back into conversation-dependent context.

### principle 2 - engine_processing does not go directly to closed

`engine_processing -> closed` is not allowed in v0.

Reason:

- Engine result is processing completion.
- It is not automatically VectorFL validation or user-facing completion.

### principle 3 - external_support is not terminal

`external_support -> closed` is not allowed in v0.

Reason:

- Search or enrichment does not complete the loop.
- External material must return to validation.

### principle 4 - closed is current-loop closure

`closed` means this operating loop is closed.

It does not prevent:

- a new request packet
- a reflux packet
- future reread

## 6. required checks by slot

### inbox

Check:

- Who requested it?
- Does it have a purpose?
- Is there a related object?

Minimum required values:

- `purpose`
- `source_surface`
- `related_objects`

### vectorfl_review

Check:

- What is the directionality?
- Which anchors does it rely on?
- Should this go to engine processing or external support?
- What must be validated later?

Minimum required values:

- `directionality`
- `anchor_refs`
- `validation_points`
- `requested_or_next_action`

### engine_processing

Check:

- Is the processing unit explicit?
- Are input materials present?
- Is the expected output shape clear?

Minimum required values:

- `request_type`
- `input_materials`
- `expected_output_shape`

### external_support

Check:

- Why is external support needed?
- What gap should support fill?
- What must be validated after support returns?

Minimum required values:

- `external_support_need`
- `purpose`
- `validation_points`

### validation

Check:

- Does the return match the purpose?
- Does it fit the anchor criteria?
- Is follow-up needed?
- Does it have reflux value?

Minimum required values:

- `return_summary`
- `result_confidence`
- `open_questions`
- `reflux_need`

### return_ready

Check:

- Who should receive the return?
- What is the minimal return shape?
- Which artifacts should be referenced?

Minimum required values:

- `suggested_next_route`
- `return_summary`
- `produced_artifacts`

### closed

Check:

- Why did this operating loop close?
- Can it close without another request?
- Is reflux needed?

Minimum required values:

- `packet_status`
- `closure_reason`
- `reflux_need`

## 7. allowed transitions v0

Allowed:

- `inbox -> vectorfl_review`
- `vectorfl_review -> engine_processing`
- `vectorfl_review -> external_support`
- `engine_processing -> validation`
- `engine_processing -> external_support`
- `external_support -> validation`
- `validation -> return_ready`
- `validation -> engine_processing`
- `validation -> external_support`
- `return_ready -> closed`

Conditionally allowed:

- `validation -> vectorfl_review`
- `return_ready -> vectorfl_review`

Conditions:

- Use `validation -> vectorfl_review` only when purpose, directionality, or anchor fit must be reread.
- Use `return_ready -> vectorfl_review` only when a return needs re-mediation before user-facing delivery.

Not allowed in v0:

- `inbox -> closed`
- `inbox -> external_support`
- `inbox -> engine_processing`
- `engine_processing -> closed`
- `external_support -> closed`

## 8. reprocessing and rewind rules

Rewind is allowed, but it must carry a reason.

### validation -> engine_processing

Allowed when:

- result exists but needs reprocessing
- input scope must be adjusted
- output shape is insufficient

### validation -> external_support

Allowed when:

- external evidence is insufficient
- comparison material is missing
- judgment is impossible without enrichment

### validation -> vectorfl_review

Allowed when:

- purpose must be reread
- request direction must be changed
- anchor conflict appears

Working sentence:

> Rewind is not failure. It is a structural signal that mediation, enrichment, or reprocessing is needed.

## 9. slot movement log

Operating movement itself is meaningful.

Every slot movement should leave a movement log with:

- `from_slot`
- `to_slot`
- `moved_by`
- `move_reason`
- `timestamp_or_order`
- `related_packet_id`

Reason:

- Without movement logs, the system loses why an object returned to external support, why validation rewound it, or why it closed.

## 10. human-readable slot state sentences

Use human-readable state sentences before locking detailed enum values.

Working sentences:

- `inbox`: request received, not mediated yet
- `vectorfl_review`: direction and criteria under review
- `engine_processing`: engine processing in progress
- `external_support`: external enrichment or support in progress
- `validation`: result under validation and comparison
- `return_ready`: return has been organized for next route
- `closed`: current operating loop closed

Boundary:

- These are readability labels for v0.
- Do not treat them as final enum values.

## 11. example flow 1 - enrichment with external support and reprocessing

User request:

> 이 축 후보를 보강할 외부 자료를 찾고, 필요하면 엔진에 다시 돌려보자.

Flow:

```text
inbox
-> vectorfl_review
-> external_support
-> validation
-> engine_processing
-> validation
-> return_ready
-> closed
```

Reading:

- `inbox`: request is created.
- `vectorfl_review`: axis enrichment purpose is checked, anchors are attached, external support is chosen.
- `external_support`: external material is searched or collected.
- `validation`: material is judged for axis-enrichment value.
- `engine_processing`: engine reprocesses with enriched material.
- `validation`: result is checked again.
- `return_ready`: return is organized.
- `closed`: current loop closes, with optional reflux.

## 12. example flow 2 - direct engine processing after VectorFL review

User request:

> 이 구현 참고자료를 기반으로 바로 코드 작업에 필요한 정리만 뽑아줘.

Flow:

```text
inbox
-> vectorfl_review
-> engine_processing
-> validation
-> return_ready
-> closed
```

Reading:

- External support is not needed.
- The request still passes through VectorFL review before engine processing.

## 13. lock level

### usable now

- Operating objects move through explicit slots.
- v0 slots are `inbox`, `vectorfl_review`, `engine_processing`, `external_support`, `validation`, `return_ready`, and `closed`.
- `inbox` must pass through `vectorfl_review`.
- Engine results do not close directly.
- `external_support` returns to validation.
- Slot movement logs should be preserved.

### not locked

- Full enum set
- Automatic routing rules
- Full team branch rules
- DB representation
- Complete exception map
- UI implementation pattern

## 14. relation to transfer packets

Transfer packets describe what is being carried between surfaces.

Operating object slot rules describe where an operating object is in the processing loop and which movement is allowed next.

Minimum relation:

- A packet should identify `requested_or_next_action`.
- An operating object should identify current slot, next slot, and movement reason.
- A movement log should reference `related_packet_id` when movement is caused by a packet.

## 15. core sentence

Operating processing objects are not meaning-maturation objects that can drift and grow freely. They must move through explicit slots while preserving processing state, movement reason, and next action.

v0 should test whether the default loop:

```text
inbox -> vectorfl_review -> engine_processing / external_support -> validation -> return_ready -> closed
```

is enough to keep low-intensity integrated-engine operation traceable without prematurely locking final routing automation.

