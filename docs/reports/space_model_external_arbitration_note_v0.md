# Space / Model / External Arbitration Note v0

## Purpose

This note defines how the answering system should arbitrate between:

- current space assets
- model reasoning
- external research

It exists because the real problem is not whether each layer works.
It is whether they are connected in the right order for a given request.

## Arbitration Rule

The system should not treat all requests as search tasks.
It should first decide which source of authority should lead.

### Space leads when

- the request is about our own structure, runtime, package, line, axis, or operating boundary
- a relevant asset already exists internally
- adaptation to our own space is part of the goal

### Model leads when

- the request is conceptual
- no strong internal asset is required
- no current external validation is needed

### External leads when

- the user asks for latest or current outside information
- our space does not already contain the needed target material
- external mismatch or freshness is the main uncertainty

## Combined Pattern

The most important combined pattern is:

- external target read
- internal space mapping
- external reinforcement only where uncertainty remains
- usable output
- reinjection judgment if useful

This is the correct pattern for requests like:

- “read external structure and tell me how it should attach to our space”

## Separation Rule

The answer should keep these layers distinct:

- what was found in the space
- what was inferred by the model
- what was reinforced externally

Do not collapse these into one undifferentiated explanation.

## Practical Order

For a mixed request, use this order:

1. identify the target and intended output
2. check whether a relevant internal space asset already exists
3. read imported or referenced external material if the target lives there
4. use model reasoning to map the target to our space
5. use web/external reinforcement only where bounded uncertainty remains
6. produce a usable output
7. decide whether reinjection is appropriate

## Why This Matters

Without arbitration:

- space gets ignored even when it already has the answer shape
- external research gets overused
- model reasoning becomes ungrounded
- outputs remain chat answers instead of reusable working results

## Example Decision

For the OMX team/ralph example:

- space does not fully lead, because the target originates outside our own core assets
- model does not fully lead, because the user wants a structure-grounded adaptation
- external does not fully lead, because the target must be attached to our space rather than merely summarized

So the correct lead is:

- external target read + internal space mapping

with:

- bounded external reinforcement

## Current Boundary

This note defines answering order only.

It does not:

- define storage destination
- define final packet schema
- authorize broad automation
