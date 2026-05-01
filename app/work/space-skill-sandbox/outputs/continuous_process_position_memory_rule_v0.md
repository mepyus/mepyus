# Continuous Process Position Memory Rule v0

## Status

- artifact_status: operating rule candidate
- scope: Codex / Gemini / sandbox / integrated-engine collaboration
- baseline_status: not baseline
- automation_status: not automation
- purpose: preserve long-horizon direction across changing sessions, workers, and viewpoints

## Core Principle

The goal is not to fix one Gemini session.

The goal is to preserve process memory so that each correction, drift, halt, reorientation, and candidate decision can become future-readable operating material.

Every meaningful turn should leave a record of:

- where we are
- what direction we are moving
- what changed
- why the change happened
- what must not be over-promoted
- what remains open, held, watched, or ready

## Why This Exists

This project changes direction and viewpoint often by design. That is not a failure.

The risk is that an agent treats a local correction as the whole objective, or forgets the larger frame:

```text
sandbox experiment -> validation -> integrated-engine / line-axis / CLI attachment / reusable space material
```

Therefore, each run must preserve not only the result but also the reason for the result and the current position in the long-running process.

## Required Recording Moments

Create or update a written record when any of these happen:

- a run changes direction
- a Gemini/Codex/user role boundary is clarified
- a worker misreads, overstates, or narrows the goal
- a halt/brake condition is discovered or used
- a candidate is accepted, held, rejected, or reclassified
- a sandbox signal is translated outward toward the engine
- a package sequence state changes
- a next run is proposed
- implementation, automation, schema, graph, ontology, ledger, or baseline promotion is explicitly held back

## Required Position Fields

Each position record should include these fields when relevant:

```text
current_position:
current_direction:
latest_state:
accepted_sequence:
hold_sequence:
active_candidate:
what_changed:
why_it_changed:
misread_or_drift_observed:
correction_applied:
what_to_preserve:
what_not_to_promote:
next_allowed_step:
next_disallowed_step:
```

The fields are not a schema or automation contract. They are a memory checklist for durable collaboration.

## Process Memory Over Session Fixing

When Gemini or another worker misreads the task, the priority order is:

1. Stop the immediate drift if needed.
2. Record what the worker misread.
3. Analyze why the misread happened.
4. Convert the analysis into a bounded next instruction or watch item.
5. Preserve the larger direction.

Do not make the single worker session the center of the project.

## Current Long-Horizon Direction

The current long-horizon direction is:

```text
Use sandbox experiments to test operating moves, validate useful constraints, and return those signals to the integrated engine as current-work-package evidence, line/axis material, CLI attachment guidance, or reflux memory.
```

The sandbox is a proving ground, not the destination.

Gemini is a bounded support worker, not the final judge.

Codex maintains structure, files, packets, reviews, and repo-local translation.

The user decides direction, promotion, and whether a candidate becomes actual work.

## Anti-Patterns

Avoid these patterns:

- fixing one Gemini session while losing the reason it failed
- turning every correction into a stricter rule system
- treating a halt condition as the whole operating goal
- letting package bookkeeping replace engine direction
- turning candidate briefs into official policy too early
- promoting Gemini support language into services, agents, controllers, or automation
- relying on chat memory for decisions that must survive handoff or compaction

## Minimum Closeout Addendum

At the end of meaningful work, include a brief position addendum:

```text
Position:
Direction:
Preserve:
Hold:
Next:
```

This can live in a run record, Codex review, Gemini packet, package closeout, or output note.

## Boundary

- This rule does not create a formal ledger.
- This rule does not require automation.
- This rule does not promote every note to baseline.
- This rule does not replace user judgment.
- This rule exists to keep long-running collaboration readable.
