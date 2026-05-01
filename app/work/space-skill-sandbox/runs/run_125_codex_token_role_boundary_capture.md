# Run 125 - Codex Token / Role Boundary Capture

## Mode

CODEX / ROLE BOUNDARY CAPTURE / TOKEN DISCIPLINE / NO AUTOMATION / NO BASELINE PROMOTION

## Purpose

Capture the user's correction that Codex must preserve tokens and stay in its structural role.

## User Correction

Codex should not behave as the primary execution worker.

Codex should focus on:

```text
structural inspection
analysis
judgment
handoff / packet shaping
review of returned worker evidence
```

Execution should be routed to Gemini first.

ChatGPT should be treated as the design / validation counterpart that checks Codex's structural framing, not as the default execution worker.

Codex should perform execution only when Gemini cannot handle the task, when a local file edit is specifically needed, or when the user explicitly asks Codex to do the work.

## Operating Rule Candidate

```text
Codex conserves tokens by reading narrowly, judging structurally, and preparing bounded packets.
Gemini performs long reads, repeated observation, and execution when capability allows.
If Gemini cannot proceed, Codex records the blocker and only then performs the minimum required local action.
```

## Immediate Consequence

Future Codex turns should prefer:

- read only the current entry / packet / review files needed
- avoid broad repo scans unless position is lost
- avoid restating large context already in durable records
- produce short STRUCTURE_PACKETs for Gemini
- review Gemini returns by authority class
- preserve user approval gates

## Boundary

- automation_created: false
- schema_created: false
- controller_created: false
- baseline_promoted: false

## Position Addendum

Position:
Run 122 has recovered current position; Run 124 accepted it with a memory-signal gap; Run 125 captures Codex token and role discipline.

Direction:
Keep Codex as structural reviewer / packet maker, not default executor.

Preserve:
Gemini-first execution, Codex narrow reading, ChatGPT structural validation, user approval authority.

Hold:
No Package 033 promotion and no Package 032 artifact read.

Next:
Use Gemini for the next execution/observation step unless Gemini is blocked or the user explicitly assigns Codex execution.
