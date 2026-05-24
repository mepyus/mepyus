# Gemini LACL Manual Return Intake Contract v0

## Status

```yaml
status: intake_contract_candidate
date: 2026-05-06
baseline_lock: false
automation: false
source_route: user_manual_relay_or_runner_outbox
```

## Purpose

Define how Codex should receive the future Gemini deep exploration result for line / axis / camera / lens re-grounding.

The result must enter as worker evidence first.

It must not directly update:

- line map
- position map
- current-position
- baseline
- workflow
- registry

## Accepted Input Routes

### 1. User Manual Relay

Use when the user pastes Gemini's report.

Required packaging fields:

- source worker: Gemini
- delivery route: `user_manual_relay`
- original packet: `app/work/space-skill-sandbox/relay/prompts/gemini_lacl_regrounding_deep_exploration_packet_20260506_v0.md`
- pasted result summary
- Codex packaging judgment

### 2. Runner Outbox

Use if the script runner succeeds.

Required packaging fields:

- runner outbox path
- raw result path
- stderr path
- invocation status
- Codex packaging judgment

## Required Sections In Gemini Result

The result should include:

- Read Trace
- Current Line Candidates
- Axis Candidates
- Camera Candidates
- Lens / Gate Candidates
- LACL -> Position Value Mapping
- Best Small-Anchor Sets
- Conflict / Overlap / Missing Data
- HOLD / Do Not Promote
- Return-to-Space Value

If any section is missing, package it as:

```text
worker_return_with_missing_section_watch
```

Do not reject the whole result unless the missing section blocks synthesis.

## Codex Packaging Output

Create a packaging report with:

```yaml
status: worker_return_packaging
source_worker: gemini
delivery_route:
baseline_lock: false
automation: false
raw_trace_promoted: false
```

Then include:

- source trace
- read trace summary
- candidate lines
- candidate axes
- candidate cameras
- candidate lenses/gates
- proposed position map changes
- accepted candidate signals
- rejected/held signals
- missing evidence
- Codex synthesis targets
- Return-to-Space Value

## Promotion Rule

Gemini result can produce:

- candidate signal
- candidate map input
- watch item
- future bounded-read target
- small anchor set recommendation

Gemini result cannot produce by itself:

- baseline
- current-position update
- ontology
- schema
- registry
- workflow
- automation
- final line maturity promotion

## Immediate Codex Decision Labels

Use one:

- `PACKAGE_AS_CANDIDATE_MAP_INPUT`
- `PACKAGE_WITH_MISSING_SECTION_WATCH`
- `HOLD_FOR_EVIDENCE_GAP`
- `HOLD_FOR_USER_DECISION`
- `REJECT_AS_OVERPROMOTION`

