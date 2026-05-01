# Space Output And Reinjection Manual v0

## Purpose

This manual explains how answers should end and when they should be handed back into the space.

## Output Rule

A good answer in this space should end in usable form, not only explanation.

The minimum visible order is:

1. what the user asked
2. how it was interpreted
3. what assets mattered
4. what structure was found
5. what the user can use now

## Reinjection Rule

Not every answer should be stored.

Reinjection should be considered only when the result is reusable beyond the current turn.

Current reinjection classes:

- `reference`
- `candidate`
- `operating_asset`

## When To Keep The Answer Ephemeral

Keep it ephemeral when it is:

- casual clarification
- one-off explanation
- unstable early thinking without reuse value

## When To Consider Reinjection

Consider reinjection when the result is:

- a structure proposal
- an adaptation mapping
- a reusable operating note
- a bounded external-to-space translation

## Recommended Output / Handoff Path

Use:

- [space_request_output_template_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/templates/space_request_output_template_v1.md)
- [space_reinjection_note_template_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/templates/space_reinjection_note_template_v1.md)
- [answer_reinjection_handoff_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/answer_reinjection_handoff_contract_v0.md)

## Important Boundary

Reinjection is secondary.

The system must first provide a useful answer.
Only then should it decide whether the result should remain in the space.

## Practical Check

Ask:

1. would this result be useful later?
2. would losing it force repeated work?
3. is it stable enough to keep as reference or candidate?

If the answer is mostly no, do not reinject.

## One-Line Summary

Finish with usable output first, then keep only what deserves to become reusable space memory.
