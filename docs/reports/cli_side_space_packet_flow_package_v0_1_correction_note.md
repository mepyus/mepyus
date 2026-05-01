# CLI-Side Space Packet Flow Package v0.1 Correction Note

## 0. Declaration

- read-only
- patch report only
- no implementation
- no source-space modification
- no index update
- no automation/controller/schema
- no UI design
- no router implementation
- no JSON schema lock
- no baseline promotion

## 1. Why this correction exists

Gemini dry-run 001 showed that the packet flow works:

```text
Routing -> Packet -> Recovery -> State -> Transition
```

The dry-run preserved key safeguards:

- AI output was not promoted to baseline.
- The result was lowered to `human_review_candidate`.
- `evidence_anchor` was required.
- auto-promotion to baseline was forbidden.
- the next packet was connected to Validation.

However, the dry-run routed "Codex result review" to Space Intake. That is understandable if the Codex result is treated as a worker artifact entering the space, but the default routing should be Validation.

## 2. Worker Result Routing Rule

```text
Worker output review:
  default_packet: Validation Packet

  optional_substep:
    Space Intake reading

  condition:
    if the worker output introduces a new thought asset, caution asset, future option,
    architectural proposal, or layer-affecting claim.
```

Default rule:

- Codex result review -> Validation Packet
- Gemini result review -> Validation Packet
- CLI result review -> Validation Packet

Sub-step rule:

- If the result contains a new external concept, thought asset, direction-change candidate, future option, architectural proposal, or layer-affecting claim, perform Space Intake reading inside the Validation Packet.
- Do not create a new packet type for this.
- Treat it as:

```text
Validation Packet
  -> optional Space Intake sub-step
```

## 3. Space Intake vs Validation Boundary

### Validation Packet

Validation Packet checks whether an existing worker result fits the task and criteria.

It should:

- compare expected vs observed result
- issue a verdict
- check evidence anchors
- detect guardrail violations
- identify whether a note must carry forward
- choose the next packet candidate

It should not:

- auto-promote a candidate
- treat summary as truth
- ignore PASS_WITH_NOTE caveats
- route directly to baseline

### Space Intake Packet

Space Intake Packet reads whether new material, idea, external concept, or worker residue has value in the space.

It should:

- identify source surface
- perform layer/lens reading
- compare fit and risk
- recommend placement candidate
- preserve `do_not_use_as`

It should not:

- immediately adopt material
- implement the idea
- create schema/registry/automation
- promote to locked rule

Boundary rule:

```text
Reviewing a worker result = Validation by default.
Reading a new material or concept for space value = Space Intake.
Worker result that contains new space material = Validation with Space Intake sub-step.
```

## 4. Recovery Card v0.1 Change

Add this field to the Recovery Card:

```text
layer_alignment:
  target_layer:
  affected_layer:
  lens_used:
  layer_conflict:
  note:
```

Example:

```text
layer_alignment:
  target_layer: operation
  affected_layer: architecture
  lens_used: provenance / worker-boundary
  layer_conflict: possible
  note: Event Fabric proposal may affect architecture baseline, so human review required.
```

Do not use:

- `layer_alignment_score`
- numeric scoring
- confidence score as truth
- score-based auto-transition

The important residue is not a number. It is which layer is targeted, which layer may be affected, which lens was used, and whether a conflict needs human review.

## 5. Recovery Card v0.1

```text
packet_type:
source_task:
verdict:
primary_event:
evidence_anchor:
what_changed:
what_was_learned:
risk_or_warning:
reuse_hint:
pattern_candidate:
layer_alignment:
  target_layer:
  affected_layer:
  lens_used:
  layer_conflict:
  note:
human_lock_required:
recommended_next_state:
do_not_promote_as:
next_packet_candidate:
```

## 6. Transition Implication

If `layer_alignment.layer_conflict` is `possible` or `yes`, the next packet should not skip human review or validation.

Allowed:

- Validation -> Space Intake sub-step -> human_review_candidate
- Validation PASS_WITH_NOTE -> next packet with note included
- Implementation -> Validation -> Recovery

Forbidden:

- layer conflict -> baseline
- high confidence -> lock
- worker result -> implementation without validation
- PASS_WITH_NOTE -> ignore note

## 7. Dry-run 002 Direction

Do not repeat Candidate A immediately.

Next dry-run should use a small implementation request:

```text
사용자가 작은 기능 구현을 요청했다. 공간은 이를 Implementation Packet으로 라우팅하고,
worker 결과를 받은 뒤 Validation과 Recovery까지 시뮬레이션한다.
```

The goal is to test:

- whether Implementation routing stays bounded
- whether Validation is required after implementation
- whether Recovery Card v0.1 captures layer alignment
- whether transition remains provisional
- whether the structure is too heavy for a small task

## 8. Closeout

This correction is a patch note only.
No existing source-space document was modified.
No index was updated.
No automation, controller, schema, UI, router, runtime bridge, JSON schema, baseline, or agent architecture was created.
The v0.1 correction remains a provisional operating candidate.
