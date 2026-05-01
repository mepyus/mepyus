[[DOCROLE:memo]]
[[RUNMODE:ingest_only]]
[[PRIORITY:normal]]

# OMX team/ralph attach space check v0

## request frame

This document records a bounded judgment about whether OMX team/ralph should be attached to our current space.

The question was not whether OMX is interesting in general.
The question was whether our current space can support:

- role-assigned agents
- leader / worker separation
- inter-agent discussion and handoff
- hypothesis / verification / testing / execution / re-verification
- package-style continuation

while staying inside our current space boundaries.

## external reading summary

The OMX material shows a stable distinction:

- `team` is coordinated parallel execution with durable tmux/worktree/runtime state
- `ralph` is a persistent completion / verification loop with one owner

Recent OMX direction does not justify importing a built-in linked `team -> ralph` lifecycle.
The stronger current reading is:

- use `team` for coordinated parallel execution
- use `ralph` later as a separate explicit follow-up loop when needed

## current space mapping

Our current space already has:

- role / operator / tool framing
- package continuity
- actual worker run precedent
- wrapper -> packet -> downstream handoff
- append-only and provenance-sensitive record posture

Our current space does not yet have:

- durable team runtime state root
- mailbox / dispatch / worker lifecycle control
- leader / worker startup and shutdown semantics
- coordinated team runtime as a first-class operating surface

The current integrated engine still reads as a single-handler operating mode, not a team runtime.

## bounded judgment

Current judgment:

- full OMX team/ralph runtime import: no
- linked `team -> ralph` lifecycle import: no
- `team` pattern reuse: yes, bounded
- `ralph` pattern reuse: yes, bounded
- separate `team` execution plus later `ralph` follow-up: yes, bounded

## safest next interpretation

The safest attach path is pattern-level only:

1. leader / worker authority split
2. team verification lane
3. separate persistent follow-up loop
4. explicit handoff rather than linked lifecycle

This should be read as a structural comparison and bounded attachability note, not as authorization for runtime import.
