# Session Memory Loss Failure Analysis Pipeline v0

## Status

- status: candidate operating analysis
- baseline: false
- automation: false
- schema: false
- controller: false
- scope: VectorFL long-horizon collaboration memory

This document records why the recent restart / session-loss problem mattered and how it should be converted into process memory instead of being treated as a one-session inconvenience.

## Core Diagnosis

The problem is not that one model instance forgot a chat.

The deeper problem is that the current working position was not durable enough as a first-read surface for a new session, CLI, or worker.

The project had many records, but the live orientation still depended too much on:

- chat context
- CLI process memory
- a model's hidden context window
- the user's recollection
- scattered package/run records without a small current-position entry

When those volatile layers reset, the next agent could find many files but could not immediately know which records were trusted, held, invalid, orphaned, or next.

## Why This Matters

VectorFL is long-horizon work.

The goal is not to win one session. The goal is to build a space where the record of work, failure, correction, and direction can survive:

- context compaction
- model restart
- CLI restart
- human interruption
- worker timeout
- quota failure
- handoff across ChatGPT / Codex / Gemini
- later rereading by a different agent

If a failure happens, the important question is not only "how do we finish this task?" It is:

```text
What did the failure reveal about the operating pipeline?
What should be recorded so the next session starts from a better surface?
What should be corrected without over-promoting the correction into law?
```

## Failure Pattern Observed

Recent evidence:

- Run 118 already captured continuous process-position memory as a needed discipline.
- Run 121 halted correctly at a Package 033 approval gate, but it was too narrow to serve as next-session memory.
- Run 122 was created to recover current position, but an automatic Gemini runner attempt timed out and exposed tool/capability mismatch:
  - capacity retries
  - missing `write_file`
  - missing `run_shell_command`
  - blocked unauthorized tool calls
- The user then moved to a manual relay path because the automated path was too slow and brittle for the moment.

This should be preserved as signal:

```text
Failed runner attempt -> capability mismatch evidence -> manual relay fallback -> pipeline correction.
```

It should not be treated as accepted sequence evidence for Package 033.

## Root Causes

### 1. No Single Current-Position Entrance

There are many useful records, but a new session needs a small first-read entrance:

```text
current_position
last_trusted_point
accepted_state
hold_state
invalid_or_orphaned_state
next_allowed_action
forbidden_moves
```

Without this, the agent searches locally and may overweight the latest visible file.

### 2. Latest File Bias

A new worker often assumes the newest artifact is the current truth. In this workspace, the newest artifact may be:

- a failed run
- a halted approval gate
- an invalid observation
- a candidate packet
- a reference-only runner receipt

Latest does not mean trusted.

### 3. Result Memory and Process Memory Were Mixed

The space has result artifacts, package records, reports, and runner receipts. But "what happened" and "what this means for the next session" are different layers.

Process memory must record:

```text
what changed
why it changed
what must be preserved
what must not be promoted
what the next worker may do
```

### 4. Capability Was Not Checked Before Worker Assumption

The automatic Gemini route assumed file-writing and shell/tool capabilities that were not available in that execution context.

The pipeline needs a capability check before assigning output mode:

```text
can_write_files? -> file-output packet
cannot_write_files? -> manual chat-return packet
cannot_read_scope? -> blocker
quota/tool unstable? -> reference-only failed attempt, not sequence evidence
```

### 5. Corrections Were Not Always Converted Into Durable Pipeline Inputs

The user correction was not merely "make a better prompt." The correction was:

```text
Analyze why the process failed.
Record that analysis.
Modify the next packet based on it.
Let that accumulation become the space.
```

That needs to become a standing pipeline move.

## Candidate Pipeline

When memory loss, worker drift, timeout, capability mismatch, or wrong-scope execution occurs:

```text
1. Stop / hold
2. Classify the event
3. Preserve the raw trace
4. Separate authority
5. Analyze cause
6. Update the next handoff / packet
7. Record current position
8. Return useful signal to the larger direction
```

### 1. Stop / Hold

Do not continue into the next package or artifact just because a worker started.

### 2. Classify the Event

Use lightweight labels:

```text
trusted_sequence_evidence
candidate
hold
invalid_for_sequence
orphaned_observation
reference_only_failed_attempt
capability_mismatch
manual_relay_required
```

### 3. Preserve the Raw Trace

Keep the runner output, stderr, handoff, or chat return. Do not delete it just because it failed.

### 4. Separate Authority

Preserved does not mean authoritative.

Failed runner output can be useful as capability evidence while remaining invalid as package sequence evidence.

### 5. Analyze Cause

For every meaningful failure, answer:

```text
What failed?
Why did it fail?
Was the problem prompt, scope, capability, approval, tool route, memory entrance, or role boundary?
What should change in the next packet?
What should not be promoted?
```

### 6. Update the Next Handoff / Packet

Modify the next instruction using the analysis.

Example from Run 122:

```text
file-writing Gemini packet
-> manual relay packet returning RESULT_MD / SELF_AUDIT_MD in chat
```

### 7. Record Current Position

Leave a small current-position addendum:

```text
Position:
Direction:
Preserve:
Hold:
Next:
```

### 8. Return Signal to Larger Direction

Tie the lesson back to the long-horizon work:

```text
sandbox experiment
-> validation
-> integrated engine / line-axis / CLI attachment / reusable process memory
```

## Required Addendum for Future Meaningful Runs

For meaningful runs, include:

```text
Memory / Pipeline Addendum:
event_class:
volatile_layer_that_failed:
durable_record_created_or_updated:
authority_status:
pipeline_correction:
next_session_entry_signal:
```

This is not a formal schema. It is a memory checklist.

## Applied Correction Now

The immediate correction is:

- preserve the failed automatic Run 122 Gemini runner output as `reference_only_failed_attempt`
- use manual relay for Gemini because available tool capability is uncertain
- ask Gemini to return chat blocks instead of writing files
- add a memory-failure / pipeline-signal section to the Run 122 recovery packet
- record this analysis as a reusable process-memory candidate

## Non-Goals

Do not:

- build a controller
- build a ledger
- build a new database
- require every trivial exchange to create records
- turn every failure into permanent law
- treat failed runner output as package acceptance evidence
- make the current session the center of the project

## Closeout

The important lesson is:

```text
The space should not depend on any one model session remembering.
The space should accumulate failure analysis, correction, and next-position
records so a future worker can re-enter from the right surface.
```

