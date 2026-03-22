# Ambiguity Review Policy

## Purpose

When a value or judgment is visibly ambiguous, the workflow should not jump directly to silent internal resolution.

The replica should first obtain an explicit external draft judgment, then let the user decide.

## Current Review Order

For ambiguous values or uncertain judgments:

1. produce or obtain a first-pass draft from web ChatGPT
2. apply that draft as the temporary external reference
3. let the user review and decide
4. preserve both the draft and the user decision in logs or metadata when possible

## Scope

This applies to:

- anchors
- scene / flow labels
- D / I / S values
- fragment boundary judgments
- connection reasons
- spatial interpretation hints

## Recording Rule

If a web ChatGPT draft is used, record:

- that the draft came from web ChatGPT
- what value or judgment it proposed
- whether the user accepted, revised, or rejected it

## Non-Override Rule

The web ChatGPT draft is not the final authority.
The user decision remains the final decision when one is provided.
