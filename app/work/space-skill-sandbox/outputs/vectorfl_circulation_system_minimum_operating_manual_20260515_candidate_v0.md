# VectorFL Circulation System v0
# Minimum Operating Manual
# 2026-05-15 Candidate v0

## 1. Status

Verdict:
  VECTORFL_CIRCULATION_SYSTEM_V0_USABLE_WITH_WATCH

Position:
  minimum manual operating guide

Not:
  policy
  workflow
  schema
  registry
  ontology
  automation approval
  memory database
  baseline
  AGENTS.md
  SKILL.md
  eval
  product architecture

Source sequence:
  `1.md` through `26.md`, with `13.md` absent

## 2. Core Definition

VectorFL is a judgment circulation space around external tools.

It does not replace Codex, Gemini, browser tools, APIs, CLIs, or memory systems. It controls how candidate inputs are placed, how external-tool outputs are recovered, how repeated judgment is matured, and how the next bounded packet is prepared.

## 3. Six Surfaces

### 1. One-page Operator Surface

Use when:
  a new external tool candidate appears

Purpose:
  place the candidate before execution

Output:
  `REFERENCE_ONLY`, `BOUNDED_TEST_CANDIDATE`, `HOLD`, or tightly justified `USE_NOW`

### 2. Maturation Queue Item

Use when:
  a result, correction, candidate, or HOLD recheck enters the space

Purpose:
  split raw material into recovered judgment, boundary flags, signals, and placement

Output:
  candidate item for the Daily Loop

### 3. Daily Circulation Loop

Use when:
  several items exist or a work round needs closure

Purpose:
  detect repeated WATCH, conflicts, HOLD recheck conditions, and packet potential

Output:
  lens candidate, filter candidate, packet fragment, compression, archive/drop

### 4. Packet Builder v0.1

Use when:
  the Daily Loop produces `PACKET_NEXT` or the user asks to use an external tool

Purpose:
  export only the smallest needed anchor and risk focus

Output:
  tool-mode aware packet

### 5. Return Packet

Use when:
  an external tool returns output

Purpose:
  recover judgment instead of storing raw output as authority

Output:
  what worked, what failed, what remains WATCH/HOLD, what should be decomposed

### 6. Re-entry Compression

Use when:
  a round must be made cheaper to resume

Purpose:
  reduce the next entry cost without promoting the result

Output:
  short re-entry note and next smallest action

## 4. Operating Loop

```text
1. Input appears
2. If it is an external tool candidate, apply One-page Operator Surface
3. If it is returned material, create a Maturation Queue Item
4. Run Daily Circulation Loop manually
5. If a next packet is justified, build it with Packet Builder v0.1
6. If an external tool is actually used, require Return Packet
7. Convert the return into Queue Item(s)
8. Compress the round for re-entry
9. Stop before promotion unless the user explicitly asks for it
```

## 5. Approval Boundary

The manual can prepare a packet. It cannot approve:

- credential use
- API calls
- uploads/downloads
- account mutation
- file writes outside the explicit task
- automation
- scheduler/background process
- baseline promotion
- current-position update
- app route wiring
- policy/schema/workflow creation

## 6. Stress-test Results

Codex case:
  passed as an execution-capable packet when file/command/patch scope stayed bounded and returns were recovered.

Gemini case:
  passed as a broad-reading packet when fluent synthesis stayed reference/lens/WATCH material and did not become adoption pressure.

API/CLI high-risk case:
  remains HOLD unless credential/API/account/data-transfer boundary is explicit and separately approved.

## 7. Minimum Use Example

```text
Input:
  "I want to try a new CLI tool."

Step:
  Apply One-page Operator Surface.

Likely decision:
  HOLD or BOUNDED_TEST_CANDIDATE until actual enablement boundary is known.

If bounded test becomes possible:
  Build Packet Builder v0.1 packet with API-data-transfer or execution-capable risk focus.

If tool returns output:
  Recover via Return Packet.

Then:
  Create Maturation Queue Item and run Daily Loop.
```

## 8. Do Not Promote

- The system is usable as manual candidate operating material.
- It is not ready to become repo law.
- It is not an automation plan.
- It is not a product architecture.
- It is not an eval or benchmark.

## 9. Next Scenario Trials

Use this manual on three real but bounded scenarios:

1. one new external tool candidate
2. one returned Codex result
3. one Gemini-style synthesis or broad-reading return

Stop after manual recovery and compression.

`STATUS: VECTORFL_CIRCULATION_SYSTEM_MINIMUM_OPERATING_MANUAL_CANDIDATE_PREPARED_WITH_WATCH`
