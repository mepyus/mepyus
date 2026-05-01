# Answer Reinjection Handoff Contract v0

## Purpose

This contract defines when a produced answer should remain a one-turn answer and when it should be treated as a candidate for reinjection into the space.

The point is not to store everything.
The point is to avoid losing outputs that should become reusable space assets.

## Core Rule

A result may be considered for reinjection when it is more than a transient explanation.

Typical reinjection candidates:

- structure proposals
- adaptation mappings
- operating notes
- reusable comparisons
- bounded external-to-space translation results

Non-candidates by default:

- casual clarification
- ephemeral discussion
- answer fragments without stable use beyond the turn

## Handoff Questions

After producing the answer, the system should ask:

1. is this result reusable beyond the current turn?
2. does it clarify or extend our current operating structure?
3. would losing this answer force the same work to be repeated later?
4. should it become a reference note, candidate asset, or operating asset?

## Reinjection Classes

### 1. reference

Use when:

- the result is useful memory
- but not yet an operating decision

### 2. candidate

Use when:

- the result may later shape structure or operation
- but still needs review

### 3. operating asset

Use when:

- the result is already directly usable as part of the current operating surface
- and the role is clear enough

## Handoff Minimum

If reinjection is considered, the handoff should minimally record:

- what the result is
- why it should be kept
- what class it belongs to
- where it should probably live
- what still remains unresolved

## Output Rule

The answer itself should still be user-facing and useful first.

Reinjection is a second-layer judgment.
It should not replace the primary usable output.

## Example: OMX Team / Ralph Mapping

If the system produces:

- a mapped explanation of how OMX team/ralph should attach to our space
- a bounded recommendation about what to adopt, separate, or reject

then the result is likely:

- at least a `candidate`
- possibly a `reference`

because:

- it is reusable
- it maps external structure into our own operating space
- repeating the same work later would be wasteful

## Non-Goals

This contract does not:

- define exact folder placement
- force reinjection on every result
- define automatic asset writing

## Working Lock

At v0, every structured answer should be checked for reinjection potential, but only bounded reusable outputs should be handed off.
