# Space Request Orchestration Runtime Directive v1

## 1. Directive Purpose

This directive fixes how Codex or another operator should execute the space request orchestration package.

## 2. When To Use This Package

Use this package when:

- a short user request must be expanded into real internal work
- the answer may depend on space assets
- external reinforcement may be needed
- the result may become reusable

## 3. Default Execution Order

1. read the raw user request
2. interpret the user intent
3. choose the route mode
4. identify primary space scope
5. identify whether external reinforcement is needed
6. build the request packet
7. perform bounded reading / mapping / reinforcement
8. produce usable output
9. judge reinjection

## 4. Request Type Judgment Rules

At minimum, classify the request as one or more of:

- `structure_read`
- `adaptation`
- `variation`
- `incident_triage`
- `external_enrichment`
- `reinjection_design`

Do not require the user to name the type.

## 5. Space Reading Rule

Do not jump to a generic answer.

If a relevant internal asset already exists:

- read the space first

If the target lives mainly in external material:

- read the imported or referenced target first
- then map it into the space

## 6. Structure Reading Rule

Do not stop at description.

Identify:

- target structure
- our matching structure
- alignment
- misalignment
- what can be adopted, separated, or rejected

## 7. Space Connection Rule

The result must state how the target connects to our current space.

That means at least:

- which space assets mattered
- which internal structure it attaches to
- what should remain outside the current structure

## 8. External Reinforcement Rule

Use external reinforcement only when:

- the user explicitly asks for it
- freshness matters
- conflict or uncertainty remains after the initial read

Do not default to web/external search when the space already contains relevant bounded material.

## 9. User-Purpose Output Rule

The final answer must be shaped for use.

It must provide:

- user-language interpretation
- structure-grounded judgment
- usable output

## 10. Reinjection Judgment Rule

After producing the answer, decide whether the result should remain ephemeral or become:

- `reference`
- `candidate`
- `operating_asset`

Do not force reinjection when the answer is only transient.

## 11. Forbidden Actions

Do not:

- answer immediately from the raw sentence alone
- mix space/model/external authority without distinction
- use external search first when the space already has the relevant bounded source
- replace useful output with internal explanation
- force reinjection without reuse value

## 12. Output Surface Rule

The answer should flow in this order:

1. user request restatement
2. request interpretation
3. assets used
4. structural reading
5. usable output
6. reinjection judgment if relevant
