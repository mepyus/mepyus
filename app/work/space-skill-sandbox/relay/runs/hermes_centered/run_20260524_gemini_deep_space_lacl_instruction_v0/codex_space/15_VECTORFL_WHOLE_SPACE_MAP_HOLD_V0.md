# VectorFL Whole Space Map HOLD V0

Status: HOLD map, not authority.

This map describes the current VectorFL/Hermes/Codex/Gemini space as of the canonical fast cross-inspection lane.

## 1. Top-Level Operating Shape

```text
User intent
  |
  v
Hermes execution workbench
  - preserves original input
  - decides whether fresh space reference is needed
  - requests bounded Codex retrieval when needed
  - merges original + space + model reasoning
  - executes or holds
  - writes trace/reentry for Codex
  |
  | shared_handoff/
  v
Codex space operator
  - checks current space
  - retrieves bounded references
  - analyzes Hermes execution/reentry
  - judges space_delta
  - proposes HOLD-only maturation
  - maintains arc/layer/pattern maps
  |
  | optional, Codex-side only
  v
Gemini wide lens
  - used only for layer ambiguity / broad LACL reading
  - evidence only, never authority
```

## 2. Write Zones

```text
runs/hermes_centered/<run_id>/
  hermes_exec/       Hermes write zone
  codex_space/       Codex write zone
  shared_handoff/    immutable cross-read board/pointers
```

Rules:
- Hermes does not write `codex_space/`.
- Codex does not write `hermes_exec/`.
- Shared files point to immutable artifacts with sha256.
- Promotion remains HOLD unless separately approved.

## 3. Canonical Fast Read Path

```text
shared_handoff/90_QUICK_EXCHANGE_BOARD.json
  -> codex_space/90_CODEX_LATEST_SUMMARY_CARD.json
  -> codex_space/11_L3_BATCH_PATTERN_MAINTENANCE_INPUT_FROM_GEMINI_HOLD_V0.json
  -> shared_handoff/99_LATEST_POINTERS.json
```

Actual readability test:
- verdict: PASS_CANONICAL_FAST_CROSS_INSPECTION_READABILITY_WITH_HOLD
- checks: 9/9 pass
- Hermes cross-read fields constructible:
  `source_handle`, `source_sha256`, `used_for`, `changed_judgment`, `owner_namespace`, `read_only_assertion`

## 4. Layer And Pattern Map

| Layer | Pattern | Root Items | Meaning |
|---|---:|---:|---|
| L1_FOUNDATION_RECOVERY_CURRENT_POSITION | P01_NO_CALL_RECOVERY_AND_CURRENT_POSITION_SURFACE | 9 | foundation, no-call recovery, current-position surface |
| L2_PROTOTYPE_BEHAVIOR_LOOP | P02_PROTOTYPE_BEHAVIOR_LOOP | 12 | scenario/four-shape/prototype behavior evidence |
| L3_PHASE2_FUNCTION_POSITIONS | P03_PHASE2_FUNCTION_POSITION_STACK | 16 | Phase2 S1-S7 function tests and support reports |
| L4_PHASE3_STRUCTURE_RELAYERING | P04_PHASE3_STRUCTURE_RELAYERING | 4 | Phase3 structure and relayering proposals |
| L5_HERMES_CENTERED_CODEX_SPACE_LOOP | P05_HERMES_CENTERED_CODEX_SPACE_LOOP | 6 | Hermes-centered Codex retrieval/maturation loop |
| L6_PROVIDER_CALL_BUDGET_GOVERNANCE | P06_PROVIDER_CALL_BUDGET_GOVERNANCE | 1 | no-direct-provider-call and budget governance |
| L7_EXTERNAL_SPACE_LENS_STACK | P07_EXTERNAL_SPACE_LENS_STACK | 5 | AI Frontier / infra-cost / external lens evidence |
| L8_SPACE_OPERATOR_GOVERNANCE_CHANNEL | P08_SPACE_OPERATOR_GOVERNANCE_AND_CHANNEL | 4 | skill, governance, dual-log, fast channel |

Total root items: 57.

## 5. Status Surface

| Status | Count | Meaning |
|---|---:|---|
| HOLD_EVIDENCE | 49 | usable as evidence, not authority |
| HISTORICAL_EVIDENCE_NEEDS_STATUS_NORMALIZATION | 5 | old foundation/current-position material needs status map |
| APPLIED_CURRENT_POSITION_HISTORY_KEEP_BOUNDARY_NOTE | 1 | historical applied state, no new apply here |
| APPLY_OR_STRUCTURE_HISTORY_HOLD_REVIEW_REQUIRED | 2 | structural/apply history needs HOLD review |

## 6. Pressure Map

| Pressure | Primary Location | Current Handling |
|---|---|---|
| Foundation status ambiguity | L1/P01 | AUTHORITY_VS_PROPOSAL_STATUS_MAP needed |
| Prototype evidence misclassification | L2/P02 | reclassify as behavior evidence, no authority promotion |
| Phase2 duplicate pressure | L3/P03 | PHASE2_FUNCTION_ROLLUP_INDEX_HOLD is next priority |
| Stale handoff language | L5/L6 | STALE_SUPERSEDED_HANDLE_MAP |
| Provider-call recurrence risk | L6 | L4 user-attention lane only |
| External lens overpromotion | L7 | keep as lens evidence, not core authority |
| Quick board version pressure | L8 | canonical 90 board + versioned boards + 99 pointers |

## 7. Maturation Queues

```text
L3M01_STATUS_NORMALIZATION_QUEUE
  -> normalize foundation/root authority vs proposal status

L3M02_PHASE2_ROLLUP_QUEUE
  -> compress Phase2 S1-S7 duplicate pressure
  -> next recommended lane

L3M03_STALE_HANDOFF_SUPERSEDED_QUEUE
  -> prevent old Codex/Gemini handoff docs from overriding Hermes-centered policy

L3M04_PROTOTYPE_RECLASSIFICATION_QUEUE
  -> preserve Z_OTHER prototype evidence as L2 behavior loop

L3M05_EXTERNAL_LENS_BUDGET_QUEUE
  -> use AI Frontier EP96/EP97 to strengthen budget lens, not authority
```

## 8. Current Judgment

The space is no longer just a collection of reports. It is now a Hermes-centered operating space with:

- one execution workbench: Hermes
- one space operator: Codex
- one optional wide-lens helper: Gemini
- one canonical fast cross-read route
- one HOLD-first maturation loop
- one main current bottleneck: Phase2 duplicate pressure

The strongest next safe lane is:

`RUN_L3M02_PHASE2_FUNCTION_ROLLUP_INDEX_HOLD_V0`

## 9. Boundary

- authority mutation: NO
- current-position apply: NO
- registry mutation: NO
- folder tree mutation: NO
- source code mutation: NO
- promotion: HOLD

