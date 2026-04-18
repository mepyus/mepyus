# VectorFL Paper Supervisor Report Format v0

## Purpose
This is the human-readable supervision surface format.
It exists so the user does not become the system's interpretation bottleneck.

## Core Rule
The report must help a supervisor decide:
- `go`
- `hold`
- `reopen`
- `redirect`

If a report does not support one of those decisions, it is incomplete.

## Required Sections

### 1. `current status`
- What loop or scenario is being discussed
- Which cell just completed work
- Whether the current recommendation is `go`, `hold`, `reopen`, or `redirect`

### 2. `why this step happened`
- Why this cell acted now
- Which earlier pressure or gap triggered this step

### 3. `what was produced`
- Stable points
- New line seeds or confirmed lines
- Candidate references or injected references
- Any newly shaped handoff artifacts

### 4. `what changed`
- What became clearer
- What became less trustworthy
- What shifted after external comparison

### 5. `what remains unclear`
- Tensions still open
- Risks of moving too early
- Reasons a reopen might be better than a go

### 6. `next recommendation`
- One of:
  - `go`
  - `hold`
  - `reopen`
  - `redirect`
- Must include one-sentence rationale

### 7. `next loop proposal`
- Which cell should act next
- What inputs it should receive
- What question it should carry

## Preferred Output Shape

```md
# Supervisor Report

## Current Status
...

## Why This Step Happened
...

## What Was Produced
...

## What Changed
...

## What Remains Unclear
...

## Recommendation
- hold
- reason: ...

## Next Loop Proposal
- next_cell: synthesis_cell
- carry_forward:
  - ...
  - ...
```

## Style Rules
- Human language first
- No unexplained internal jargon
- No dashboard-only metrics without interpretation
- No generic “progress was made” phrasing
- Every recommendation must be tied to evidence

## Minimum Decision Check
A report is acceptable only if the supervisor can answer:
- What happened?
- Why did it happen?
- What do I do now?
