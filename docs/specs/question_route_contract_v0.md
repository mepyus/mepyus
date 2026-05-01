# Question Route Contract v0

## Purpose

This contract defines how a short user request is routed before any answer is produced.

The goal is not to make users specify the internal path.
The goal is to let the system choose the right path among:

- model-only
- space-first
- external-first
- space-plus-external
- answer-plus-reinjection

## Core Rule

Do not answer immediately from the raw user sentence alone.

First decide:

1. what the user is asking for
2. whether the answer depends on space assets
3. whether external freshness or external comparison is required
4. whether the output is likely to become a reusable space asset

## Route Modes

### 1. model-only

Use when:

- the request is conceptual or explanatory
- no current space asset is needed
- no external freshness is needed

Output:

- direct answer

### 2. space-first

Use when:

- the request is about our existing structure, line, axis, package, runtime, or current internal assets
- the most relevant evidence is already in the space

Output:

- answer grounded in current space assets

### 3. external-first

Use when:

- the user explicitly asks for current external information
- our space has no meaningful prior material for the target

Output:

- externally grounded answer
- optional note about whether later space reinjection is useful

### 4. space-plus-external

Use when:

- the target exists in external material or external repo references
- but the answer must be adapted to our current space
- external freshness or conflict-check is still needed

Output:

- adapted answer
- explicit separation between space-derived judgment and external reinforcement

### 5. answer-plus-reinjection

Use when:

- the user is asking for a structure, draft, plan, mapping, or applied form that could become a reusable asset
- the result is likely to matter beyond the current turn

Output:

- usable answer
- reinjection judgment

## Routing Questions

Before answering, the system should implicitly ask:

1. is this mainly about our current space?
2. is there already a relevant asset or precedent in the space?
3. is external verification or enrichment required?
4. is the user asking for explanation, adaptation, construction, or reusable structure?
5. should the result stay ephemeral, or should it become a candidate asset?

## Space / Model / External Priority

Default priority:

1. space first when a relevant internal asset already exists
2. external only when space is missing or freshness is the real issue
3. model-only only when neither space nor external lookup is necessary

Do not use external search as the first reflex when the space already holds a relevant bounded source.

## Output Boundary

The route decision must shape:

- what gets read
- what gets compared
- what gets written as the answer
- whether reinjection should be considered

The route decision does not itself decide:

- final reinjection storage
- promotion
- axis naming
- broad automation

## Example: OMX Team / Ralph Request

If the request is:

`Find the team/ralph structure in oh-my-codex, understand it, map it against our space, enrich with web search, and propose how OMX's team/ralph should attach to our space.`

The route should be:

- `space-plus-external`
- with `answer-plus-reinjection` candidate status

Reason:

- the target exists in imported reference material
- the answer must be adapted to our own space
- external reinforcement may still be needed
- the result is likely to become a reusable internal note or operating candidate

## Non-Goals

This contract does not:

- define final output formatting in detail
- define reinjection storage details
- define automation
- replace lower/upper bridge rules

## Working Lock

At v0, the system must first choose a route mode before producing the answer.
The user should not have to name that mode explicitly.
