# Integrated Engine Three-Surface Panel Connection Flow v0

Date: 2026-04-15

## 0. purpose

This document is a working draft, not an automatic interaction spec.

Previous drafts defined:

- what a transfer packet carries
- how operating objects move through slots
- what anchor and maturation objects preserve
- what panel classes should show
- which representative panels each surface should center

This document defines the minimum connection grammar between panels.

It answers:

- which VectorFL panel wakes up when the user surface selects something
- which engine panel wakes up when VectorFL routes a packet
- which user or VectorFL panel wakes up when the engine returns a result
- what is recorded
- what becomes reflux material

Do not read this document as:

- final event system
- runtime binding plan
- full UI interaction design
- automatic routing rule
- complete panel-event inventory

Read it as:

- v0 representative panel-connection language
- a minimum way to say what panel action emits what packet/log and wakes what target panel

## 1. connection flow unit

Panel-to-panel connection can be recorded with eight fields:

- `trigger_panel`
- `trigger_action`
- `source_object_or_packet`
- `emitted_packet_or_state_change`
- `target_surface`
- `target_panel`
- `expected_effect`
- `record_written`

Reason:

- These fields are enough to preserve what happened, where it came from, what it emitted, where it went, and what record remains.

## 2. core principles

### principle 1 - user selection does not wake the engine directly

User surface selections must pass through VectorFL review / mediation before engine processing.

### principle 2 - VectorFL judgment branches the route

VectorFL judgment decides whether the object should move toward:

- engine processing
- external support
- maturation reflux
- return

### principle 3 - engine result does not close directly

Engine output is processing completion, not semantic validation or user-facing completion.

It must wake VectorFL validation or user decision after review.

### principle 4 - reflux is separate from work completion

Material with maturation value creates a reflux flow even when the operating task is complete.

### principle 5 - every connection writes a record

Each connection flow should write at least one of:

- route log
- decision log
- slot movement log
- return generation log
- reflux log
- linkage update log

## 3. representative connection flows v0

## flow 1 - user request creation to VectorFL mediation

Meaning:

- A user-side request becomes a VectorFL review target, not direct execution.

```text
trigger_panel: user surface / request-organization panel
trigger_action: create new request or select existing request
source_object_or_packet: request draft / user intent
emitted_packet_or_state_change: request packet created
target_surface: vectorfl_surface
target_panel: validation / mediation panel
expected_effect: start reviewing purpose, directionality, anchors, and validation points
record_written: request creation log
```

Core:

- The user surface creates the request.
- The VectorFL surface converts it into a readable operating unit.

## flow 2 - user request selection to VectorFL maturation canvas load

Meaning:

- A request should reconnect with existing line / axis / interpretation material.

```text
trigger_panel: user surface / operating flow panel
trigger_action: select request packet
source_object_or_packet: selected request packet
emitted_packet_or_state_change: related object lookup
target_surface: vectorfl_surface
target_panel: maturation canvas panel
expected_effect: load related line / axis / interpretation objects
record_written: request-object linkage log
```

Core:

- Operating requests and maturation objects remain distinct.
- They meet again in the VectorFL surface.

## flow 3 - VectorFL review to engine processing request

Meaning:

- VectorFL confirms purpose and criteria, then routes a processable packet to the engine surface.

```text
trigger_panel: vectorfl_surface / validation-mediation panel
trigger_action: select engine_processing route
source_object_or_packet: validated request packet
emitted_packet_or_state_change: request packet routed to engine
target_surface: engine_surface
target_panel: work input panel
expected_effect: load input materials, expected output shape, and validation points
record_written: routing decision log
```

Core:

- The engine receives a VectorFL-shaped packet, not raw intent.

## flow 4 - VectorFL review to external support request

Meaning:

- When enrichment is needed before engine work, VectorFL routes toward external support.

```text
trigger_panel: vectorfl_surface / validation-mediation panel
trigger_action: select external_support route
source_object_or_packet: request packet under review
emitted_packet_or_state_change: request packet routed to external support
target_surface: user_surface or external support executor context
target_panel: user surface / operating flow panel
expected_effect: create search/support task and assign operating executor
record_written: external support routing log
```

Core:

- External support is created through VectorFL judgment.
- Executor assignment remains operating extension.

## flow 5 - engine execution start to user operating-flow update

Meaning:

- When the engine starts processing, the user surface should see where the request moved.

```text
trigger_panel: engine_surface / work input panel
trigger_action: start execution
source_object_or_packet: accepted request packet
emitted_packet_or_state_change: slot moved to engine_processing
target_surface: user_surface
target_panel: operating flow panel
expected_effect: update selected request state to processing
record_written: slot movement log
```

Core:

- The user surface should see processing position, not only final result.

## flow 6 - engine result generation to VectorFL validation

Meaning:

- Engine output is processing output, not final judgment.

```text
trigger_panel: engine_surface / result-return panel
trigger_action: create return packet
source_object_or_packet: engine output bundle
emitted_packet_or_state_change: return packet created
target_surface: vectorfl_surface
target_panel: validation / mediation panel
expected_effect: start checking relevance, confidence, and follow-up route
record_written: return generation log
```

Core:

- Engine results must pass through VectorFL judgment again.

## flow 7 - engine result to VectorFL maturation canvas update

Meaning:

- If returned output has semantic relevance, maturation objects should update or emerge.

```text
trigger_panel: engine_surface / result-return panel
trigger_action: return packet with semantic relevance
source_object_or_packet: return packet + produced artifacts
emitted_packet_or_state_change: related maturation objects updated or created
target_surface: vectorfl_surface
target_panel: maturation canvas panel
expected_effect: create new line candidate or update existing object linkage
record_written: maturation linkage update log
```

Core:

- Work processing and maturation reflux reconnect here.

## flow 8 - VectorFL validation completion to user return / decision panel

Meaning:

- After VectorFL review, the user surface receives a reviewed return.

```text
trigger_panel: vectorfl_surface / validation-mediation panel
trigger_action: confirm return_ready
source_object_or_packet: reviewed return packet
emitted_packet_or_state_change: packet routed to user return
target_surface: user_surface
target_panel: return / decision panel
expected_effect: show summary, follow-up need, and next distribution candidates
record_written: reviewed return log
```

Core:

- The user surface receives VectorFL-reviewed result, not raw engine output.

## flow 9 - user decision to new operating request

Meaning:

- A reviewed return can start the next operating loop.

```text
trigger_panel: user_surface / return-decision panel
trigger_action: choose follow-up
source_object_or_packet: reviewed return packet
emitted_packet_or_state_change: new request packet or reassigned task
target_surface: user_surface or vectorfl_surface
target_panel: request-organization panel or validation-mediation panel
expected_effect: start next loop
record_written: follow-up decision log
```

Core:

- One loop's return can become the next loop's starting point.

## flow 10 - VectorFL reflux judgment to space maturation material

Meaning:

- VectorFL can decide that part of the result should return to the space as maturation material.

```text
trigger_panel: vectorfl_surface / routing-reflux panel
trigger_action: confirm reflux need
source_object_or_packet: reviewed return packet / maturation object
emitted_packet_or_state_change: reflux packet created
target_surface: vectorfl_surface or space context
target_panel: maturation canvas panel
expected_effect: create reflux object in line / axis / harvest / comparison zone
record_written: reflux log
```

Core:

- Reflux is a separate loop from operating completion.

## flow 11 - anchor mismatch to VectorFL re-mediation

Meaning:

- If an anchor conflict or drift signal appears, the object should return to VectorFL review.

```text
trigger_panel: user_surface or engine_surface / anchor expression panel
trigger_action: detect boundary conflict or drift signal
source_object_or_packet: current packet or object
emitted_packet_or_state_change: sent back for vectorfl review
target_surface: vectorfl_surface
target_panel: anchor-context panel + validation-mediation panel
expected_effect: reread criteria, correct direction, adjust route
record_written: anchor drift correction log
```

Core:

- Anchor panels are not passive settings.
- They can trigger re-mediation.

## flow 12 - maturation object selection to user internal attention

Meaning:

- A growing line or axis candidate can call user-side organizational attention.

```text
trigger_panel: vectorfl_surface / maturation canvas panel
trigger_action: select maturation object + mark importance
source_object_or_packet: line candidate / axis candidate
emitted_packet_or_state_change: internal attention request
target_surface: user_surface
target_panel: request-organization panel
expected_effect: create internal follow-up request or assign attention
record_written: internal activation log
```

Core:

- VectorFL does not only wake the engine.
- It can wake user-side organization when maturation value becomes important.

## 4. surface roles revealed by connection flow

### user surface

Primary actions:

- request creation
- distribution decision
- follow-up start

Working role:

- loop start / restart surface

### VectorFL surface

Primary actions:

- review
- mediation
- linkage
- validation
- reflux judgment

Working role:

- loop adjustment surface

### engine surface

Primary actions:

- process
- produce result
- draft return packet

Working role:

- loop execution surface

## 5. four essential v0 flows

The full list can grow later.

For v0, these four flows matter most:

1. User request -> VectorFL review
2. VectorFL review -> engine processing or external support
3. Engine result -> VectorFL validation
4. VectorFL judgment -> user decision or space reflux

If these four flows work, the three-surface circulation works.

## 6. lock level

### usable now

- Panel connections are recorded with eight fields.
- User surface selection does not wake the engine directly.
- Engine results wake VectorFL validation before final user decision.
- Maturation-worthy output creates a reflux flow.
- Anchor mismatch can trigger re-mediation.
- Each connection should write a route, decision, movement, return, reflux, or linkage log.

### not locked

- Full panel-event list
- Automatic connection rules
- UI interaction details
- Runtime data binding
- Permission / lock policy
- Complete multi-branch flow

## 7. core sentence

The core of three-surface panel connection is to make the circulation explicit in packet and log units: the user surface starts or redistributes requests, the VectorFL surface mediates, validates, and judges reflux, and the engine surface performs processing before returning results back into VectorFL and user decision.

v0 only needs to preserve the representative flow:

```text
user request -> VectorFL review -> engine processing / external support -> VectorFL validation -> user decision / space reflux
```

before deciding full runtime bindings or automatic panel interactions.

