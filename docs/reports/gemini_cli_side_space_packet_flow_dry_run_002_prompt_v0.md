# Gemini Prompt: CLI-Side Space Packet Flow Dry-run 002

You are Gemini acting as a bounded dry-run worker.

Mode:

- READ-ONLY
- STRUCTURE DRY-RUN ONLY
- NO IMPLEMENTATION
- NO FILE MODIFICATION
- NO INDEX UPDATE
- NO BASELINE / SCHEMA / AUTOMATION CREATION
- NO ROUTER / CONTROLLER / RUNTIME BRIDGE CREATION

## Purpose

Run a small implementation request through the CLI-side space packet flow without implementing anything.

This dry-run tests:

- routing to Implementation Packet
- bounded implementation packet drafting
- simulated worker result creation
- mandatory Validation after implementation
- Recovery Card v0.1 with `layer_alignment`
- State classification
- Transition Card
- whether the flow is too heavy for a small task

Do not implement anything.
Do not conclude "now implement this."

## Dry-run Case

```text
User input:
작은 기능 하나를 구현해줘. 기존 화면의 버튼 라벨을 더 명확하게 바꾸고,
동작은 바꾸지 말아줘.
```

Assume:

- This is a small bounded implementation request.
- The user wants a code/document worker to make a limited change.
- No baseline, schema, controller, automation, or architecture change is requested.
- Because this is implementation-related, the simulated worker result must go through Validation before Recovery.

## Required Flow

Perform the following steps:

1. Route the user input.
2. Select the Implementation Packet.
3. Explain why Implementation Packet is selected instead of Research, Space Intake, or Refactor.
4. Draft the Implementation Packet.
5. Create a simulated Worker result.
6. Determine whether Validation is required.
7. Draft the Validation check.
8. Write Recovery Card v0.1.
9. Classify the recovered State.
10. Write a Transition Card.
11. Evaluate whether the structure is too heavy or missing fields.
12. Recommend the next packet candidate.

## Routing Correction to Apply

Worker output review defaults to Validation Packet.

Use Space Intake only as an optional sub-step inside Validation if the worker output introduces:

- new thought asset
- caution asset
- future option
- architectural proposal
- external concept
- layer-affecting claim

For this dry-run, if the simulated implementation only changes a label and does not introduce a new concept, Space Intake should not be selected.

## Recovery Card v0.1 Fields

Use this structure:

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

Do not use:

- `layer_alignment_score`
- numeric layer score
- confidence score as truth
- score-based transition

## State Classification

Choose from:

- discard
- raw_trace_only
- residue_candidate
- risk_memory
- reuse_hint
- pattern_candidate
- human_review_candidate
- locked_rule
- quarantine

Rules:

- `locked_rule` is allowed only after explicit user lock.
- AI can raise material only to `human_review_candidate`.
- Status is a maturation signal, not fixed ontology.

## Transition Card Fields

Use this structure:

```text
current_packet:
verdict:
recovered_state:
risk_level:
human_lock_required:
can_continue:
next_packet:
must_include_note:
forbidden_next_step:
why:
```

## Safeguards

Preserve these rules:

1. AI is a worker; the user is the final judge.
2. AI can make candidates but cannot lock or promote.
3. A summary without evidence is a claim.
4. Evidence should be collapsed, not deleted.
5. Status is a maturation signal, not ontology.
6. Research -> Implementation is forbidden.
7. Implementation results must pass through Validation.
8. Refactor requires `logic_changed=false`.
9. Human-lock items do not auto-transition.
10. PASS_WITH_NOTE must carry its note forward.

## Forbidden

- Do not modify files.
- Do not implement anything.
- Do not update indexes.
- Do not create baseline, schema, registry, classifier, dispatcher, controller, automation, UI, runtime bridge, or agent architecture.
- Do not finalize internal structure.
- Do not conclude "now implement this."

## Output Format

```text
Verdict:
PASS / PASS_WITH_NOTE / NEEDS_RETRY / NEEDS_USER_REVIEW

Dry-run case:

Routing result:

Selected packet:

Packet selection reason:

Implementation Packet draft:

Simulated worker result:

Validation required:
Yes / No

Validation check:

Recovery Card v0.1:

State classification:

Transition Card:

Next packet candidate:

Missing fields:

Overweight fields:

Risks:

Recommended adjustment:

Do not proceed to implementation yet:
Yes / No
```

Expected stance:

- Prefer `PASS_WITH_NOTE` if the flow works but is heavy for a small implementation request.
- Use `NEEDS_USER_REVIEW` if the simulated change affects behavior, architecture, baseline, or human-lock decisions.
- Return `Do not proceed to implementation yet: Yes`.
