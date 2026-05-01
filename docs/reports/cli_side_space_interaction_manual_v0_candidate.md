# CLI-side Space Interaction Manual v0 Candidate
# Topic: Lightweight Operational Guidelines for Sovereign Space

## 0. Declaration
- **Mode:** Read-only synthesis for discussion.
- **Scope:** Space reference only; no modification of source-space documents.
- **Status:** Provisional strategic reference material.
- **Authority:** All rules remain provisional until explicit user lock.
- **Date:** 2026-04-26

## 1. Why This Manual Exists
This manual consolidates the "Interaction Contract" (Rounds 001-017). Its purpose is to define the minimum language and constraints required for CLI-space interaction, ensuring the user maintains sovereignty without falling into "Automation Bias" or "Schema-First Suffocation."

## 2. Operating Model: The 3-Layer Universe
- **Deep Space:** The immutable provenance log and layered cosmology (The "Truth").
- **Light CLI:** The execution surface for fast, tactical operations (The "Hand").
- **Observation Surface:** A thin, non-interruptive membrane that interprets CLI execution results for human triage (The "Eye").

## 3. Worker Output Contract (Structured Footer v0.1)
*All CLI/Assistant outputs must conclude with this structure to facilitate observation triage.*

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

## 4. Operational Rules (Guardrails)
- **Primary Event vs. Residue:** Surface the "Primary Intent" (summary); collapse mechanical residue (logs) into the provenance link.
- **Sovereignty Lock:** AI can propose baseline/schema/delete operations, but the human MUST provide a sovereign lock before any mutation occurs.
- **Preflight Protocol:** High-impact operations (delete, baseline update) trigger a preflight warning that blocks file mutation until the user issues a secondary "Implementation" command.
- **No Direct Translation:** Research packets cannot auto-transition to implementation packets.
- **OK is NOT Truth:** `OK` signals execution completion, not a baseline lock or truth confirmation.

## 5. Status Vocabulary & User Language
- `OK` → **완료**
- `VALIDATION_REQUIRED` → **검증 필요**
- `HUMAN_REVIEW_REQUIRED` → **사용자 판단 필요**
- `HOLD` → **보류**
- `risk_signal` → **주의 신호**

*Forbidden:* `승인됨`, `확정됨`, `기준 반영됨`, `자동 반영됨`, `canonical`, `promoted`.

## 6. Provenance & Evidence Drill-down
- **Summary without drill-down = Claim.**
- **Drill-down:** Evidence must be "Collapsable." Use `근거: [내용]` as the standard anchor in the footer.
- **Failure Traces:** Never delete traces of abandoned paths; archive them as `Quarantine` assets to preserve provenance.

## 7. Aggregation & Triage
- **Session-level Aggregation:** Multiple residue records from a single session should be compressed into one summary candidate to prevent Sovereign Tray fatigue.
- **Grouping Policy:** Group by *intent* (e.g., "Designing Gates") rather than chronological order.
- **Splitting Policy:** Separate residues that involve different *layers* (e.g., Philosophy vs. Implementation) to avoid contamination.

## 8. Strategic Cautions (No Implementation)
- **Do not automate the Human Lock.**
- **Do not impose an ontology (Schema-first).**
- **Do not let "Confidence" replace "Verification."**
- **Do not replace the Failure Trace with a sanitized Dashboard.**

## 9. Safe Later Experiments (Manual Dry-run Candidates)
- **Manual Footer:** Worker manually adds footer to session logs.
- **Manual Disposition:** Human sorts results into `Keep`, `Quarantine`, or `Escalate`.
- **Manual Provenance Link:** Human manually creating the link between a CLI output and its evidence.
- **Human Sovereign Lock Simulation:** Practicing the "Proposal -> Lock" flow with hypothetical changes.

## 10. Remaining Ambiguities
- **Report Packet Status:** Standalone packet vs. Research sub-type.
- **Stale Provenance:** How to handle moved/renamed files in evidence logs.
- **Aggregation Threshold:** How many records trigger an automatic grouping?
- **Worker/Manual Sync:** How to ensure the CLI worker actually knows the "Operating Manual" rules without being hard-coded?

## 11. Closeout
This manual candidate is discussion-only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, verification UI, bridge logic, drill-down design, evidence schema, event grouping design, suppression logic, status schema, dashboard, UI, reingestion design, JSON schema, CLI trace contract, or aggregation threshold was created.
All findings remain provisional strategic reference material.
