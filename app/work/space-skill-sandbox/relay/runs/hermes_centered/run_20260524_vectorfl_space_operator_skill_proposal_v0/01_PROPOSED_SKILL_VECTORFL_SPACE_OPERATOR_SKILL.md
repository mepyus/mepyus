---
name: vectorfl-space-operator
description: Use when routing Codex-space work inside the Hermes-centered VectorFL loop: space check, Hermes work analysis, original-based retrieval, and reentry-based maturation with HOLD/no-mutation boundaries.
version: 0.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [VectorFL, Codex, Hermes, space, router, retrieval, maturation, HOLD]
    related_skills: [vectorfl-packetized-tool-bridges]
---

# VectorFL Space Operator

## Overview

Use this skill to turn short user/Codex instructions into bounded Codex space duties inside the Hermes-centered VectorFL loop.

Hermes remains the original interpretation, model merge, execution, and trace center. Codex owns space check, original-based space retrieval, Hermes work analysis, selected/rejected reference judgment, and HOLD-only maturation proposals. Gemini may appear only inside a Codex-side script-chain when Codex decides layer analysis is necessary; Hermes does not directly invoke Gemini.

## When to Use

Use when the user or Hermes says one of these:

- "공간을 확인해"
- "현재 공간 확인"
- "헤르메스 작업 내용을 분석해"
- "Hermes가 뭘 했는지 확인해"
- "공간자료를 찾아줘"
- Hermes provides an original/task packet and asks Codex for retrieval
- "공간 숙성 판단해"
- Hermes provides a reentry record after execution

Do not use this skill for generic coding, web research, source mutation, registry/current-position apply, folder moves, or direct API/server/replay lanes.

## Route Table

| User / Hermes instruction | Route | Codex duty |
| --- | --- | --- |
| 공간을 확인해 | CODEX_SPACE_CHECK | Read compact controls and latest handles, return a bounded space snapshot |
| 헤르메스 작업 내용을 분석해 | CODEX_HERMES_WORK_ANALYSIS | Read Hermes merge/reentry/validation and explain what Hermes did |
| 공간자료를 찾아줘 / retrieval request | CODEX_SPACE_RETRIEVAL_BY_ORIGINAL | Retrieve bounded original-relevant space material for Hermes merge |
| 공간 숙성 판단해 / reentry provided | CODEX_SPACE_MATURATION_BY_REENTRY_RECORD | Decide HOLD-only maturation proposals from Hermes reentry |

## Non-Negotiable Boundary

Default status is HOLD.

Never do these from this skill:

- mutate source code
- mutate authority
- apply current-position
- mutate registry
- move folders
- promote proposal to authority
- call Codex/Gemini through direct API
- ask Hermes to call Gemini directly
- run external API/direct/server/replay lanes

## Output Discipline

Every Codex return separates:

- read_files
- selected_material or selected_space_material
- rejected_material or rejected_space_material
- changed_judgment
- risks
- next_safe_lane
- promotion_status

Every Hermes work analysis separates:

- space refs Hermes used
- model reasoning Hermes added
- execution decision
- execution trace
- Codex-readable reentry handle
- HOLD or approval boundary

## Reference Files

In a real skill package, keep the longer route contract and schemas under references/:

- references/hermes_centered_loop.md
- references/operation_routes.md
- references/return_schemas.md
- references/boundaries.md

## Verification Checklist

- [ ] Route selected from exactly one of the four routes
- [ ] Required read files are listed before analysis
- [ ] Return schema includes read_files and promotion_status
- [ ] changed_judgment is present for retrieval/maturation routes
- [ ] no direct API/server/replay/folder/source/authority/current-position mutation
- [ ] Gemini is absent unless Codex-side layer analysis explicitly requires it
- [ ] output remains HOLD unless user separately approves promotion/apply
