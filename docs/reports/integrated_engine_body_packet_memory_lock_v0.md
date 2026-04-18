# Integrated Engine Body / Packet / Memory Lock v0

## Verdict

LOCKED_FOR_CURRENT_WORK

## Lock Purpose

This document records the operational lock extracted from the 2026-04-17 source notes.

It does not replace the 3-surface baseline. It thickens it so future implementation work does not collapse into CLI control panels, isolated cards, or visual cleanup.

## Body Lock

The integrated engine body is the fixed 3-surface structure:

| surface | body role | first reading |
| --- | --- | --- |
| User Surface | organization / assignment / approval / priority / constraints | decision |
| VectorFL Surface | interpretation / mediation / internal-search trigger / route decision / reflux | interpretation and branching |
| Engine Surface | input, generation, translation, extraction, flow, processing, structure/alignment execution | process |

CLI tools sit on top of the body. They do not become the body.

## Common Process Lock

Every non-trivial task should be read through this process:

```text
instruction intake
-> internal search
-> evidence bundle
-> VectorFL mediation / work-packet shaping
-> User organization
-> Engine processing
-> VectorFL reflux
-> record / sedimentation
```

If a task skips internal search, it is a fast path exception and should be named as such.

## Work Packet Lock

The basic operating unit is the work packet, not the panel.

Minimum work-packet fields:

- purpose
- task type / lens
- assigned team / role
- tool / operator
- do
- do-not
- current state
- current surface
- next route candidate
- hold / reread / validation / deposit state
- internal evidence bundle
- trace / memory record

Minimum packet layers:

1. header / outer frame
2. internal evidence
3. mediation / guard
4. trace / record

## Material Lock

The engine body must digest five core materials:

1. purpose
2. memory
3. process
4. decision
5. sedimentation

These form a loop:

```text
purpose -> memory -> process -> decision -> sedimentation -> memory
```

The engine also generates derived materials:

- event
- interpretation
- external translation
- self-structuring
- emotion / pressure

Derived materials should be interpreted and structured, not treated as noise.

## Memory Lock

Memory is not storage.

Memory is a metabolic process that decides what prior material should change the current task.

Memory states:

- immediate memory
- held memory
- compressed memory
- warning memory
- promoted memory

Memory capture triggers:

- friction
- repetition
- reusability
- structural-change potential
- connection power

Locked sentence:

```text
Memory is "the past that changes the current task."
```

## Self-Learning Lock

Self-learning is not hidden automation.

It is a formal work frame:

```text
event -> pattern recognition -> structuring -> re-entry
```

Potential outputs:

- line
- axis
- watchpoint
- routine
- skill
- assignment rule
- translation rule

Surface split:

- VectorFL captures and judges whether an event is worth holding.
- Engine structures the event and creates candidates.
- User decides whether the candidate is promoted into an official work method or asset.

## Self-Structuring Lock

Self-structuring is not cleanup.

It is the engine's maintenance process for classifying its own products:

- body asset
- operating asset
- space asset
- hold / experiment asset
- external reference asset

This should become a recurring lens before deletion or large folder cleanup happens.

## Current Diagnosis

What is already relatively strong:

- fixed 3-surface shell
- CLI-on-top first path
- candidate / route / mark discipline
- `deposit_candidate` as `not_ingested`
- active / support / hold awareness

What is weak:

- internal search gate is not yet formal in the UI
- memory is present but not yet a forced prior input
- Engine surface still reads partly as return/candidate feed, not full process surface
- sedimentation exists as candidate artifact but does not yet feed memory strongly
- work-packet fields are not yet explicit in the main UI

## Operating Rule For The Next Patch

Before adding new tools or adapters, inspect whether the active screen makes these visible:

- purpose
- memory/evidence
- process
- decision
- sedimentation

If not, patch the body before adding another lens.

