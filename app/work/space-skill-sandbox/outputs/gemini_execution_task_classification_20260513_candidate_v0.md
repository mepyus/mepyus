# Gemini Execution Task Classification
# 2026-05-13 Candidate v0

## 1. Status

Document:
  candidate Gemini execution task classification

Authority:
  execution planning / lane separation support only

Not:
  final task plan
  workflow
  registry
  baseline
  current-position
  output_manifest
  automation
  Big Frame Candidate Map approval

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH

---

## 2. Purpose

Classify the next Gemini-facing work from the current large-frame direction without forcing the user back into long-prompt relay work.

This file separates:

- what Gemini can execute / observe
- what Codex should implement
- what ChatGPT / User must judge
- what remains HOLD

---

## 3. Current Large-Frame Basis

Operating principle:
  ChatGPT / User hold large-frame design and judgment.
  Codex implements structure.
  Gemini executes, observes, verifies, and detects structural gaps.
  User remains final approval authority.

Current evidence:
  - Manual Cycle Relay has been tested through Cycle 006.
  - Gemini can execute from a cycle work_order path.
  - Codex can implement structure from Gemini-discovered gaps.
  - Genealogy Reservoir Index exists as a thin orientation source.
  - Big Frame Candidate Map remains HOLD until explicit user approval.

---

## 4. Gemini Task Classes

| Class | Gemini role | Suitable tasks | Not Gemini's role | Output |
|---|---|---|---|---|
| G1. Execution Usability Check | test whether a structure can be used | read a work_order, inspect a skeleton, report usability | edit repo files | usability verdict |
| G2. Evidence Density Observation | inspect evidence strength | compare index / readiness / skeleton and identify strong / weak areas | declare baseline | evidence density notes |
| G3. Boundary Stress Test | test whether guardrails hold | look for workflow / registry / current-position drift | fix structure directly | WATCH / HOLD risks |
| G4. Structural Gap Detection | find missing files or ambiguous structure | identify Codex-needed work | implement the fix | Codex request entry |
| G5. Thin-Surface Fitness Test | test whether a surface stays small enough | identify repetition, overload, or hidden inventory drift | compress active surface directly | thinness verdict |
| G6. Release Readiness Observation | observe whether a held action is ready for user decision | state what supports release and what argues for HOLD | approve release | decision support |

---

## 5. Next Gemini Work Bundle

Cycle:
  cycle_007_big_frame_gemini_execution_batch

Goal:
  Ask Gemini to inspect the current Big Frame map-adjacent materials as an execution / observation batch and return one cycle-level result.

Gemini should check:
  1. Whether the Genealogy Reservoir Index is sufficient as the preferred compressed source for a later map draft.
  2. Whether the existing Big Frame Candidate Map draft packet should be revised before any execution.
  3. Whether the current release decision surface is clear enough for User / ChatGPT judgment.
  4. Whether the thin-surface principle is preserved.
  5. Whether any structural gap requires Codex.

Gemini must not:
  - create the Big Frame Candidate Map
  - approve map execution
  - edit repo files
  - promote any candidate
  - treat observation as authority

---

## 6. Ownership

Gemini:
  execute the observation batch and return evidence / gaps.

Codex:
  provide the cycle files and later process approved structure requests.

ChatGPT / User:
  decide whether Gemini's result supports revise-packet-first, release-with-watch, keep-hold, or ChatGPT large-frame review.

---

## 7. WATCH

- Gemini may overstate readiness as approval.
- Release readiness can be confused with release permission.
- Index can become a registry if treated as complete coverage.
- Draft packet revision can drift into map creation.
- Thin orientation surface can become a second inventory.

---

## 8. HOLD

- Big Frame Candidate Map creation.
- Final framework declaration.
- Baseline / workflow / registry / schema promotion.
- current-position update.
- output_manifest update.
- automation / scripts.

---

## 9. Do Not Promote

- task classification != workflow
- Gemini task bundle != execution approval
- release observation != release
- index sufficiency != official history
- draft-packet revision != map creation
