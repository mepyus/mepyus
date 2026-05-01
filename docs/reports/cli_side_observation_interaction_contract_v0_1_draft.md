# CLI-side Observation Interaction Contract v0.1 Draft
# Topic: Minimum Interaction Contract for CLI-Space Operation

## 0. Declaration
- **Mode:** Draft-only synthesis.
- **Scope:** Read-only / No source-space modification.
- **Status:** Strategic reference material only; no implementation or internal design.
- **Authority:** All fields and boundaries remain provisional thought assets.
- **Date:** 2026-04-26

## 1. Why This Contract Exists
The "Sovereign Cognitive Universe" requires a clear interface between the "Work" (CLI/Worker) and the "Universe" (Space). This contract provides the minimum shared language to move from "Raw Execution" to "Human-Lock Integrity" without requiring complex UI or schemas. It ensures the CLI outputs are "Observation-Ready" without imposing automation-heavy structures.

## 2. Contract Participants
- **CLI/Worker:** Executes raw tasks (The "Hand").
- **Observation Record:** A compressed, intent-based log of the session (The "Trace").
- **Observation Surface:** The thin, ambient layer that informs the user (The "Eye").
- **Human User:** The Sovereign Observer who holds the Lock authority.

## 3. Worker Structured Footer v0.1
*All worker output MUST conclude with this footer.*

```text
--- STRUCTURED FOOTER v0.1 ---
status: [Value]
task_intent: [Value]
packet_type: [Value]
scope: [Value]
summary: [Value]
source_ref: [Value]
risk_signal: [Value]
validation_required: [Bool]
human_review_required: [Bool]
evidence_ref: [Value/None]
next_packet_candidate: [Value]
note: [Value]
--- END FOOTER ---
```

## 4. Minimum Observation Record Fields
- **Required:** `status`, `task_intent`, `packet_type`, `scope`, `summary`, `source_ref`, `risk_signal`, `validation_required`, `human_review_required`, `next_packet_candidate`, `note`.
- **Conditional:** `evidence_ref` (required if `validation` or `human_review` is true), `layer_alignment` (if applicable).
- **Hidden:** `packet_type`, `scope`, `source_ref` (can be abstracted/collapsed).

## 5. Minimum Observation Surface Display
- **Visible:** `Status`, `Summary`, `Risk Signal`, `Human Review Flag`, `Note`.
- **Drill-down (Collapsed):** `Evidence Link`, `Provenance Anchor`.

## 6. Allowed Status Vocabulary
- **OK** (Success; not truth/lock)
- **RUNNING** (Active execution)
- **FAILED** (Execution anomaly)
- **BLOCKED** (Cannot proceed)
- **VALIDATION_REQUIRED** (Needs logic check)
- **HUMAN_REVIEW_REQUIRED** (Needs sovereign approval)
- **HOLD** (System-level pause)

*Forbidden:* `PENDING`, `APPROVED`, `LOCKED`, `CANONICAL`, `PROMOTED`, `TRUE`

## 7. Routing Boundary
- **Read-only report** -> `OK` or `VALIDATION_REQUIRED`
- **Code modification** -> `VALIDATION_REQUIRED` (Implementation)
- **Refactor (logic_changed=false)** -> `VALIDATION_REQUIRED`
- **Architecture proposal/Baseline** -> `HUMAN_REVIEW_REQUIRED` -> `HOLD`
- **File deletion** -> `HUMAN_REVIEW_REQUIRED` -> `HOLD` (Archive)
- **External research** -> `VALIDATION_REQUIRED` -> `Space Intake`
- **Worker result** -> `VALIDATION_REQUIRED` (Default)

## 8. Validation Required Conditions
- Any changes impacting current code logic.
- Result of an AI research/synthesis task.
- Changes tagged as "High-risk."
- Discrepancy between code change and `logic_changed=false` flag.

## 9. Human Review Required Conditions
- Changes to `baseline/` or `schema/` directory.
- `file_deletion` requests.
- External methodology adoption.
- Changes impacting "Security/Privacy Governance" layers.
- AI proposals that involve "Locking" or "Promoting" a candidate.

## 10. Forbidden Interpretations
- **OK is not lock/truth/baseline:** Executing successfully is not equivalent to finalizing a rule.
- **Summary is not evidence:** A summary without a provenance anchor is an unverified claim.
- **Human Review is not a bottleneck:** It is the integrity protocol that differentiates a "Universe" from an "Automation."
- **Status is not ontology:** It is an observer signal, not a fixed classification.

## 11. Remaining Ambiguities
- **Report Packet Status:** Should we handle simple read-only reports with a separate `Report Packet` or consolidate into `Research`?
- **Evidence Access:** How do we make `evidence_ref` clickable/accessible in a terminal-based CLI view without a full UI?
- **Fatigue:** Is the number of `VALIDATION_REQUIRED` cases per session sustainable?
- **Session-level Aggregation:** When do we compress 10+ packets into one?

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
