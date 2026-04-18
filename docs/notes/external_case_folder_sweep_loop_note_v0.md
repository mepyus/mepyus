# external case folder sweep loop note v0

## Purpose

This note locks the bounded loop shape for sweeping `inputs/external_cases` later.

The point is not to run the whole folder now.
The point is to create a reusable loop structure that can be called later when the folder is ready.

## Loop shape

Per file:

1. detect file kind
2. decide whether structured intake is natural
3. run raw intake probe
4. reserve report slots for:
   - transcript-aware first pass
   - latent line watchpoints
   - strong line contact

## Guardrail

- no new route expansion
- no automatic promotion
- no global line judgment
- no broad folder execution by default

## Current execution mode

The loop runner is plan-first.

- default: `plan_only`
- optional later: `--execute`

That keeps the structure ready without forcing the whole folder to run now.

## Why this is the right level

The current repo can already take one external file through:

- intake
- first structural read
- watchpoint separation
- strong line contact read

So the next natural step is not a new system.
It is a bounded file-by-file sweep loop that reuses that same shape.
