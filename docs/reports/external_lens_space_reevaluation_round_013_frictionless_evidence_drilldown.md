# External Lens Space Re-evaluation Round 013
# Topic: Frictionless Evidence Drill-down

## 0. Research Declaration
- **Mode:** Web research first, external view first.
- **Scope:** Read-only / No source-space modification.
- **Status:** Research report only; no implementation or internal design.
- **Authority:** All findings are provisional external thought assets.
- **Date:** 2026-04-26

## 1. Why This Round
Round 012 concluded that "Summary-to-Evidence" drill-down is the fundamental pattern for balancing "Intent" (Primary Event) and "Provenance" (Secondary Residue). We need to understand how high-signal systems (SRE, SOC, Aviation) lower the *cognitive friction* of moving from a summary to raw evidence without forcing the human to manage the complexity of the raw data. This round informs how we ensure our "Primary Events" don't become unverified claims.

## 2. Short User Space Summary
The User Space is a **Self-Forming Universe** where human attention is the primary unit of currency. We rely on **Layer-Aware Reading** and **Human Sovereign Lock** to ensure structural integrity, but currently lack the "Frictionless Drill-down" mechanism to bridge the gap between AI summaries and raw event provenance.

## 3. External Case Harvest

### A. Observability / Tracing (Datadog/Sentry)
- **Key Concepts:** Trace-to-Log correlation, Issue grouping, Root Cause Analysis.
- **External View:** The summary ("Issue") is a logical aggregation; the evidence (traces/logs) is the physical reality.
- **Borrowable Asset:** **"Logical-to-Physical Link."** Always store the logical correlation (why they are grouped) separately from the physical trace (what actually happened).
- **Dangerous Assumption:** "Everything must be correlated automatically." If automation fails, the user is lost.

### B. Security Operations (SIEM/SOAR)
- **Key Concepts:** Evidence chain, Incident Triage, Alert correlation.
- **External View:** Analysts triage "Incidents" (Summary), but their work depends on the "Evidence Chain" (Raw events).
- **Borrowable Asset:** **"Evidence Affordance."** The UI provides the *path* to evidence without demanding the user find it.
- **Dangerous Assumption:** Analysts always drill down.

### C. Clinical / Medical Decision Support
- **Key Concepts:** Audit trail, decision support evidence.
- **External View:** A summary diagnosis is a liability without an accompanying audit trail of the vitals that led to the alert.
- **Borrowable Asset:** **"Audit-First Summary."** The summary *includes* the audit trail metadata as a first-class citizen.
- **Dangerous Assumption:** That a doctor has time to audit a 24-hour log.

### D. Aviation / Industrial Control
- **Key Concepts:** Master Alert, Nested Warnings.
- **External View:** Primary event surfaces; secondary consequences are nested/collapsed.
- **Borrowable Asset:** **"Nested Evidence Collapse."** Primary warnings surface first; raw sensor readings are nested for drill-down.
- **Dangerous Assumption:** That the primary alert accurately identifies the "System Level" failure.

### E. Code Review / PR Interfaces
- **Key Concepts:** PR checks summary, drill-down to execution logs.
- **External View:** Summary status (Pass/Fail) is the entry; raw execution log is the evidence.
- **Borrowable Asset:** **"State-gated Drill-down."** Evidence visibility is triggered *by the state* (e.g., only show failed logs).
- **Dangerous Assumption:** "Passed = Good." A summary can pass all gates but still have architectural flaws.

---

### 4. External Evidence Drill-down Matrix

| External System | Summary Object | Backgrounded Evidence | Drill-down Trigger | Provenance Affordance | Fatigue Control | Failure if Over-grouped | User Space Relevance | Risk |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SRE** | Issue | Traces / Logs | Logical link | Trace ID | Deduplication | False convergence | Root Cause Trace | Metric bias |
| **SOC** | Incident | Raw events | Investigation | Evidence ID | Triage | Missed causality | Alert correlation | False Positive |
| **Medical** | Summary | Vitals history | Audit trail | Audit trail | Passive alerting | Over-omission | Triage summary | Alarm blindness |
| **Aviation** | Master Warning | Nested Advisories | Priority List | Flight log | Hidden cascade | Focus protection | Alert Tiering | Mode confusion |
| **Code Review**| Check Status | Test logs | State failure | Commit ID | Routing | Failed filter | Process Gate | Test-bias |

---

### 5. User Space Seen Through Frictionless Evidence Drill-down Lens
1. **Summary-as-a-Claim:** In our space, a summary without an evidence drill-down is an *unverified claim*.
2. **Residue-as-Evidence:** Secondary residues aren't noise; they are the "Drill-down Content" for primary events.
3. **Frictionless Bridge:** We need a way to link "Provisional Event Candidates" to the *original CLI traces* so the human lock is informed, not guessed.

---

### 6. External Critique

#### Strengths
- **Provenance-First:** Our lineage tracking is stronger than most external systems that just "group events."

#### Weaknesses
- **Drill-down Latency:** Our current interaction model has no "drill-down affordance"; every action is a "primary-level" event.

#### Misunderstanding Risk
- Outsiders will see our "Sovereign Tray" as a flat list and assume we don't differentiate between "Aha!" moments and mechanical steps.

#### Differentiation
- We group by **Conceptual Maturation**, not just time or error-code.

#### Borrowable Assets
- **"Summary-to-Evidence Link":** The fundamental bridge (e.g., [Summary] -> [Expand]).
- **"State-gated Drill-down":** Only exposing evidence when the primary event triggers a `Failure` or `Warning` status.

#### Dangerous Assumptions
- **"Human will drill down":** Human observers will skip verification if the friction is too high.

---

### 7. Next External Search Questions
- How do successful "Thinking Environments" handle human fatigue during verification?
- Are there models for "Contextual Status" where the residue's evidence is shown *only* when the human queries the layer?

---

### 8. Closeout
This report is external-lens research only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, drill-down UI, evidence schema, event grouping design, suppression logic, status schema, dashboard, UI, reingestion design, JSON schema, CLI trace contract, or aggregation threshold was created.
All findings remain provisional external thought assets.
