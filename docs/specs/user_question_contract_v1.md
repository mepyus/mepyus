# User Question Contract v1

## Purpose

This contract defines how little the user should have to specify when making a request.

The system should carry the routing burden.
The user should not have to carry the orchestration burden.

## What The User Is Not Required To Know

The user does **not** need to know:

- entrypoint names
- internal route modes
- skill names
- template names
- packet field names
- reinjection classes
- folder or asset taxonomy

## Minimum User Input

The user only needs to provide, in short form:

1. target
2. purpose

Optional but helpful:

3. desired output shape
4. whether external reinforcement is explicitly wanted

## Recommended Question Pattern

The most useful short pattern is:

`[target] + [what I want done with it]`

Examples:

- `Read this in our space and structure it for use.`
- `Find this in the space and turn it into something we can apply.`
- `Use this target and make a draft for our current purpose.`
- `Map this external structure to our space and tell me how it should attach.`

## Question Classes The System Must Interpret

The user may be asking for:

- explanation
- structure read
- adaptation
- variation
- incident triage
- external enrichment
- reinjection-ready result

The user does not need to label the class.
The system must infer it.

## Expected System Behavior

When a user asks a short question, the system must:

1. interpret the intent
2. choose the route mode
3. decide whether space assets must be read
4. decide whether external reinforcement is needed
5. produce a usable output
6. decide whether reinjection should be considered

## User Burden That Is Explicitly Rejected

Do not require the user to:

- say “use space-first”
- say “use external-first”
- say where to store the answer
- say which template to use
- say whether the result is `reference` or `candidate`
- say which line/axis/boundary to inspect

Those are system duties.

## Short Call Examples

These are valid calls:

- `Read [target] in our space and organize it so we can use it.`
- `Find [target] in our space and turn it into an applicable structure.`
- `Use [target] to make a draft for the current purpose.`
- `Read [target], compare it to our space, and tell me what we should adopt.`
- `Check [target] and tell me whether it should become a reusable note in our space.`

## Output Expectation

The user should receive:

1. a short user-facing interpretation
2. a structure-grounded answer
3. a usable output, not only explanation
4. reinjection judgment when relevant

## Contract Summary

The user only needs to say enough to identify the target and the purpose.

The system must perform:

- routing
- asset selection
- enrichment judgment
- output shaping
- reinjection judgment
