# CLI-side Space Interaction Contract v0.1 (Final Integration)

## 0. Declaration
- **Mode:** Strategic Integration.
- **Scope:** Read-only reference for future implementation.
- **Status:** Integrated Strategy Document.
- **Authority:** Provisional thought asset.
- **Date:** 2026-04-26

## 1. Core Operating Identity
- **Sovereign Cognitive Universe:** Space is the primary authority; CLI/Assistants are transient worker-observers.
- **Event-Sourced Fabric:** The system state is derived from the provenance-linked event history, not fixed databases.
- **Ambient Maturation:** Structures (labels/schemas) emerge through Gradual Formalization; they are not imposed.

## 2. Interaction Loop
1. **Action (Worker):** CLI executes a command.
2. **Trace (Observer):** The system records the raw session trace.
3. **Triage (Observation Layer):** The system classifies the interaction into a `Session Summary Candidate`.
4. **Validation/Lock (Sovereign):** Human Sovereign Lock is applied if the candidate affects baseline, schema, or integrity.
5. **Reingestion (Storage):** Canonical residues are collapsed into the space, preserving the "Failure Trace."

## 3. Worker Output Contract (The Structured Footer)
*All worker output MUST include this footer for triage.*
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

## 4. Aggregation & Triage Policy
- **Primary vs. Secondary:** Surface the `Summary` (Intent); collapse mechanical `Evidence` (Secondary Residue) into the provenance anchor.
- **Review Threshold:** Only `HUMAN_REVIEW_REQUIRED` (or `HOLD`) items interrupt the user interface.
- **Atomic Intent:** One `Interaction Candidate` corresponds to one goal (e.g., "Designing Gates").

## 5. Verification Rules
- **OK != Lock:** `OK` status is for success logging only; it is not a promotion to `Canonical` truth.
- **Provenance-First:** A summary without an `evidence_ref` is an unverified claim.
- **Human Sovereign Lock:** AI proposes the baseline; Human locks it. No automation can bypass this.

## 6. Strategic Cautions (No Implementation)
- **Do not automate the Human Lock.**
- **Do not store log bloat as "Memory".**
- **Do not introduce Schema-First structures.**
- **Do not replace the "Failure Trace" with a "Clean Dashboard".**

## 7. Next Steps
- This contract serves as the "sanity check" for future implementation.
- Any UI/Tool implementation proposal must be mapped against these fields and principles.
- Implementation of the "Sovereign Tray" must respect the "Aggregation Threshold" logic defined herein.

## 8. Closeout
This contract is for strategic alignment only.
No source-space document was modified.
All findings remain provisional strategic reference material.
