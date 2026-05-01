# CLI-side Observation Interaction Contract v0.1 Draft
# Topic: Minimum Interaction Contract for CLI-Space Operation

## 0. Declaration
- **Mode:** Draft-only synthesis.
- **Scope:** Read-only / No source-space modification.
- **Status:** Strategic reference material only; no implementation or internal design.
- **Authority:** All fields and boundaries remain provisional thought assets.
- **Date:** 2026-04-26

## 1. Why This Contract Exists
The "Sovereign Cognitive Universe" requires a clear interface between the "Work" (CLI/Worker) and the "Universe" (Space). Without a defined contract, we face two risks: **Implementation Drift** (where the system becomes an uncontrolled automation machine) and **Sovereign Fatigue** (where the human observer is overwhelmed by raw logs). This contract provides the minimum shared language to move from "Raw Execution" to "Human-Lock Integrity" without requiring complex UI or schemas.

## 2. Contract Participants
- **CLI/Worker:** Executes raw tasks (The "Hand").
- **Observation Record:** A compressed, intent-based log of the session (The "Trace").
- **Observation Surface:** The thin, ambient layer that informs the user (The "Eye").
- **Human User:** The Sovereign Observer who holds the Lock authority.

## 3. Minimum Worker Output (Fields)

### Essential Fields
- **task_intent:** Why are we performing this? (Contextual summary).
- **packet_type:** Categorization (e.g., `Refactor`, `Implementation`, `Research`).
- **scope:** The domain of action (e.g., `code_change`, `file_deletion`).
- **result_state:** The outcome status (`OK`, `FAILED`, `BLOCKED`, etc.).
- **summary:** High-level intent-based description.
- **source_ref:** Link to the original task or request.
- **risk_signal:** Severity score (low/medium/high).
- **validation_required:** Boolean (logic check needed?).
- **human_review_required:** Boolean (sovereignty check needed?).
- **next_packet_candidate:** Proposed sequence (e.g., `validation`, `hold`).
- **note:** Essential observer notes (e.g., `logic_changed=false`).

### Conditional Fields (Included only if relevant)
- **evidence_ref:** Link to raw logs/traces (Provenance link).
- **layer_alignment:** Target layer (Philosophy/Operation/Implementation).
- **recovery_candidate:** The path to revert/quarantine.

## 4. Minimum Observation Surface Display

### Visible Fields (Primary Surface)
- `Status` (User-friendly: `완료`, `검증 필요`, `판단 필요`, `보류`)
- `Task` (Short intent summary)
- `Risk Signal` (Ambient cue)
- `Human Review Required` (Sovereignty flag)
- `Note` (Contextual alerts)

### Hidden Fields (Drill-down / Ambient)
- `source_ref`
- `provenance_anchor` (accessible via hover/shortcut)
- `packet_type` (can be abstracted into icons)
- `layer_alignment`
- `raw_logs` (physical reality behind the claim)

## 5. Allowed Status Vocabulary
- **OK** (Success; not truth)
- **RUNNING** (Active execution)
- **FAILED** (Execution anomaly)
- **BLOCKED** (Cannot proceed)
- **VALIDATION_REQUIRED** (Needs logic check)
- **HUMAN_REVIEW_REQUIRED** (Needs sovereign approval)
- **HOLD** (System-level pause)

*Forbidden:* `PENDING`, `APPROVED`, `LOCKED`, `CANONICAL`, `PROMOTED`, `TRUE`

## 6. Routing Boundary
- **Read-only report** -> `OK` or `VALIDATION_REQUIRED`
- **Code modification** -> `VALIDATION_REQUIRED` (Implementation)
- **Refactor (logic_changed=false)** -> `VALIDATION_REQUIRED`
- **Architecture proposal/Baseline** -> `HUMAN_REVIEW_REQUIRED` -> `HOLD`
- **File deletion** -> `HUMAN_REVIEW_REQUIRED` -> `HOLD` (Archive/Quarantine)
- **External research** -> `VALIDATION_REQUIRED` -> `Space Intake`
- **Worker result** -> `VALIDATION_REQUIRED` (Default)

## 7. Validation Required Conditions
- Any changes impacting current code logic.
- Result of an AI research/synthesis task.
- Changes tagged as "High-risk."
- Discrepancy between code change and `logic_changed=false` flag.

## 8. Human Review Required Conditions
- Changes to `baseline/` or `schema/` directory.
- `file_deletion` requests.
- External methodology adoption.
- Changes impacting "Security/Privacy Governance" layers.
- AI proposals that involve "Locking" or "Promoting" a candidate.

## 9. Hidden vs Visible Fields

| Field | Visibility | Reason |
| :--- | :--- | :--- |
| **Status** | Visible | Indicates system state at a glance. |
| **Summary** | Visible | Intent-based triage. |
| **Risk Signal** | Ambient | Peripheral awareness of safety. |
| **Human Review Flag** | Interruptive | Sovereign integrity is priority. |
| **Provenance Anchor** | Hidden | Drill-down resource only. |
| **Full Logs** | Collapsed | Secondary evidence for trace access. |

## 10. User-facing Language (User-friendly Translation)
- `OK` -> `완료`
- `VALIDATION_REQUIRED` -> `검증 필요`
- `HUMAN_REVIEW_REQUIRED` -> `사용자 판단 필요`
- `HOLD` -> `보류`
- `risk_signal` -> `주의 신호`
- `next_packet_candidate` -> `다음 작업`

## 11. Remaining Ambiguities
- **Report Packet Status:** Should we handle simple read-only reports with a separate `Report Packet` or consolidate into `Research`?
- **Evidence Access:** How do we make `evidence_ref` clickable/accessible in a terminal-based CLI view without a full UI?
- **Fatigue:** Is the number of `VALIDATION_REQUIRED` cases per session sustainable?
- **Pattern Maturation:** Does the system know when a `residue` has become a `pattern` automatically, or is that a human signal?

## 12. What This Contract Is Not
- Not an implementation plan.
- Not a UI design spec.
- Not a finalized JSON schema.
- Not an agent orchestration architecture.

## 13. Closeout
This contract draft is discussion-only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, verification UI, bridge logic, drill-down design, evidence schema, event grouping design, suppression logic, status schema, dashboard, UI, reingestion design, JSON schema, CLI trace contract, aggregation threshold, or agent architecture was created.
All findings remain provisional strategic reference material.
