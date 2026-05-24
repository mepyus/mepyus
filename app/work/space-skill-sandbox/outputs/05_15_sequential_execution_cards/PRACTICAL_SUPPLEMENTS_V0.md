# Practical Supplements v0
# 05-15 Execution Usability Patch

## 1. Status

Status:
  PRACTICAL_SUPPLEMENTS_PREPARED_WITH_WATCH

Purpose:
  Make the 05-15 candidate system easier to use without adding new conceptual structure.

Not:
  new architecture
  schema
  workflow
  automation
  baseline

## 2. Queue Item Mini Form

Use when:
  input is simple, reference-only, or needs quick recovery.

```text
source:
  [where it came from]

recovered:
  [judgment candidate]

WATCH:
  [drift / risk]

HOLD:
  [must not do now]

boundary:
  [command / file / API / credential / account / memory / automation / none]

next:
  [smallest next action]
```

Use full Queue Item when:
  file write, command execution, API/credential/account boundary, user correction, repeated WATCH, conflict, HOLD recheck, or promotion risk appears.

## 3. Generator Threshold Rules

Full item required if:
  - command/file/API/credential/account/browser/memory boundary is unclear or present
  - user correction changes active frame
  - conflict signal is possible or strong
  - promotion risk is medium or high
  - item may become packet fragment, eval seed, or surface update

Review required if:
  - conflict_signal: strong
  - promotion_risk: high
  - boundary: unclear and action requested
  - HOLD recheck asks for execution

Add to generator output:

```text
uncertainty:
  low / medium / high

why_full_item:
  [reason or none]

review_trigger:
  [reason or none]
```

## 4. Daily Loop Trigger Rules

Run Daily Circulation Loop only when:
  - three or more meaningful inputs accumulated
  - user correction changes active frame
  - external tool result returns
  - HOLD recheck appears
  - next packet is being prepared
  - repeated WATCH appears across at least two items

Do not run when:
  - input is simple and has no reusable judgment
  - compression would add ceremony
  - no WATCH/HOLD/packet potential exists

Pattern threshold:
  - two repeats: WATCH_POOL
  - three repeats: PATTERN_CANDIDATE
  - repeat plus conflict: REVIEW_REQUIRED

## 5. Short Return Packet

Use for:
  read-only review, no-write inspection, chat-only packet return.

```text
verdict:
  [one line]

direct_answer:
  [answer]

WATCH:
  [risks]

HOLD:
  [not allowed]

next:
  [smallest next action]
```

Use Full Return Packet when:
  files were read/written, commands were run, patch/result evidence exists, API/credential/account/browser/memory boundary was touched, or user needs audit-quality trace.

## 6. Gemini Evidence Strength Add-on

Use for:
  broad-reading, synthesis, comparison, external reference analysis.

Add fields:

```text
evidence_strength:
  weak / medium / strong

observation_type:
  direct_observation / inference / candidate_lens

source_coverage:
  excerpt_only / selected_sources / broad_corpus

uncertainty:
  [what is not known]
```

Rule:
  Broad synthesis cannot become recovered judgment until evidence strength and source coverage are visible.

## 7. Packet Builder Unknown/Mixed Fallback

If tool_mode is unknown:
  default to REFERENCE_ONLY or HOLD.

If tool touches multiple high-risk modes:
  split into separate packets by action.

Example:
  mixed framework with docs + CLI + memory:
    packet 1: documentation-reference read only
    packet 2: execution-capable pre-use planning, only if requested
    packet 3: memory-retrieval review, no write/reindex

Add field:

```text
mode_conflict:
  [why one mode is insufficient]
```

Hard stop:
  no generic packet for mixed high-risk tool.

## 8. Operating Note

These supplements reduce weight. They do not promote the system.

If a supplement starts becoming required ceremony, downgrade to chat-only guidance.

`STATUS: PRACTICAL_SUPPLEMENTS_V0_PREPARED_WITH_WATCH`
