# Manual Cycle Relay Fast-Path Contract
# 2026-05-13 Candidate v0

## 1. Status

Document:
  candidate fast-path operating contract

Authority:
  speed / delegation support only

Not:
  automation
  workflow
  registry
  schema
  baseline
  current-position
  output_manifest
  release approval
  final authority model

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH

---

## 2. Purpose

Reduce relay drag without weakening authority boundaries.

The current bottleneck is not the ability to do the work.
The bottleneck is excessive micro-gating around relay, recovery, state alignment, and next packet creation.

This contract defines when Codex may proceed directly, when Gemini should be used as execution / verification lane, and when User / ChatGPT judgment is required.

---

## 3. Fast-Path Rule

Codex may proceed directly when all are true:

- the work is bounded repo-side structure implementation
- no HOLD is released
- no candidate is promoted
- no current-position or output_manifest file is updated
- no automation or script is created
- no final artifact is created
- the change preserves WATCH / HOLD boundaries

Codex should create a run record and keep the result candidate with watch.

---

## 4. Stop-Path Rule

Codex must stop for User / ChatGPT judgment when the work:

- releases HOLD
- creates the final Big Frame Candidate Map
- promotes baseline / workflow / registry / schema
- updates current-position
- updates output_manifest
- creates automation or scripts
- changes large-frame meaning
- resolves a meaning ambiguity that belongs to User / ChatGPT

---

## 5. Gemini Batch Rule

Use Gemini when the work requires:

- execution / observation
- bounded broad reading
- verification against multiple files
- dry-fill or usability test
- evidence-density check
- structural gap detection

Prefer one cycle-level Gemini return over many small relay prompts.

Gemini must not:

- edit repo files
- approve release
- promote candidates
- treat observation as authority

---

## 6. Cycle Closeout Rule

Codex may close a cycle directly when:

- Gemini return is already provided
- no authority change is required
- Codex requests are structure-only
- WATCH / HOLD are preserved
- the cycle return records that Gemini output is not approval

Codex must not close a cycle as approval for:

- map creation
- baseline promotion
- current-position update
- automation

---

## 7. Next-Action Selection Rule

When user says "계속" or "계속 빌드업":

Codex should choose the next safe structure implementation step, not wait for a new long instruction.

Default safe next steps:

1. align cycle state
2. create or revise packet / work_order
3. package Gemini return
4. prepare Gemini batch verification
5. create candidate support surface

Default unsafe next steps:

1. create final map
2. release HOLD
3. promote baseline / workflow / registry / schema
4. update current-position or output_manifest
5. create automation / scripts

---

## 8. Decision Table

| Situation | Owner | Fast path? | Required action |
|---|---|---|---|
| Gemini return needs packaging | Codex | yes | recover, place with watch, record hard stops |
| Packet needs source/path correction | Codex | yes | patch packet, record run |
| Missing template/file found | Codex | yes | create candidate file, record run |
| Broad evidence check needed | Gemini | no Codex local execution | create work_order |
| HOLD release requested | User / ChatGPT | no | stop for explicit decision |
| Map draft execution requested | User approval then Codex | no until approval | require RELEASE_WITH_WATCH |
| current-position update considered | User / ChatGPT then Codex | no | require explicit approval |
| Automation considered | User / ChatGPT | no | HOLD unless approved |

---

## 9. WATCH

- speed becoming hidden authority
- Codex doing broad analysis instead of Gemini
- fewer handoffs becoming weaker judgment
- fast-path changes accumulating into workflow
- run records becoming memory or registry
- "continue" being mistaken for release approval

---

## 10. HOLD

- Big Frame Candidate Map creation
- baseline / workflow / registry / schema promotion
- current-position update
- output_manifest update
- automation / scripts

---

## 11. Do Not Promote

- fast path != automation
- fast path != authority
- cycle close != approval
- run record != memory
- Gemini verification != release
- user "continue" != HOLD release unless explicit
