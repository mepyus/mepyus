# External Lens Space Re-evaluation Round 005
# Topic: Invisible Oversight Interfaces

## 0. Research Declaration
- **Mode:** Web research first, external view first.
- **Scope:** Read-only / No source-space modification.
- **Status:** Research report only; no implementation or internal design.
- **Authority:** All findings are provisional external thought assets.
- **Date:** 2026-04-26

## 1. Why This Round
Round 004 successfully identified the "Review Fatigue" bottleneck but treated it as a triage problem. This round explores the **Invisible Oversight** interface—how external safety-critical systems keep the human "on the loop" (monitoring) rather than constantly "in the loop" (approving), until a critical threshold is hit. This is essential for maintaining Human Sovereign Lock without exhausting the user's attention.

## 2. External Case Harvest

### A. Aviation / Cockpit Alerting
- **Their View:** "Attention is a finite resource." Interfaces are designed to hide normalcy and highlight anomalies.
- **What is Hidden:** Normal flight parameters (altitude, speed, heading) are backgrounded via glass cockpit displays; only changes (deviations) are highlighted.
- **What is Surfaced:** "Off-nominal" events (e.g., engine fire, sudden decompression).
- **Fatigue Reduction:** Alerts are tiered (Advisory, Caution, Warning). "Silent alerts" handle minor deviations.

### B. Nuclear Control Rooms
- **Their View:** Oversight as "Abnormal Situation Management."
- **What is Hidden:** Stable cooling cycles and standard power generation are represented by ambient status indicators.
- **What is Surfaced:** Deviations from standard cooling trends or sensor inconsistencies.
- **Fatigue Reduction:** "Alarm suppression" hides cascading secondary alarms that are consequences of a single primary event.

### C. Medical / Clinical Decision Support
- **Their View:** "Interruptive vs. Passive" alerting.
- **What is Hidden:** Stable patient vitals (passive dashboards).
- **What is Surfaced:** Drug interaction risks or sudden vital sign drops (interruptive alerts).
- **Fatigue Reduction:** Only showing alerts that require immediate clinical action, filtering out "predictable" deviations.

### D. Security Operations (SOC)
- **Their View:** Triage-based alerting.
- **What is Hidden:** Known traffic patterns and routine system activity.
- **What is Surfaced:** Traffic from blacklisted IPs or impossible access patterns.
- **Fatigue Reduction:** SOAR (Security Orchestration, Automation, and Response) suppresses 99% of events, showing analysts only "verified" incidents.

### E. Industrial Supervisory Control
- **Their View:** "Adaptive Automation."
- **What is Hidden:** Fully automated routine control cycles.
- **What is Surfaced:** System performance degradations that might require a human intervention/reset.
- **Fatigue Reduction:** Letting the machine work while the human monitors for "Mode Confusion."

---

## 3. External Interface Matrix

| Lens | Hidden by Default | Surfaced When | Human Role | Fatigue Control |
| :--- | :--- | :--- | :--- | :--- |
| **Aviation** | Nominal flight status | Off-nominal deviation | Supervisor | Alert Tiering |
| **Nuclear** | Steady-state cooling | Cascade deviation | Abnormal Mgr | Alarm Suppression |
| **Medical** | Stable patient vitals | Actionable risk | Decision Support | Alert Filtering |
| **Security** | Known traffic patterns | Unverified incident | Triage Analyst | SOAR Orchestration |
| **Industrial** | Automated cycles | Performance lag | Monitor | Adaptive Automation |

---

## 4. User Space Seen Through Invisible Oversight Lens

1. **If seen as a Second Brain:** We are currently designing a dashboard that shows every "thought" (review fatigue), when we should be designing a "cockpit" that shows only "thought deviations."
2. **If seen as a Cognitive OS:** Our "Sovereign Tray" is currently an interruptive alert system; we need to add "Passive Monitoring" layers.
3. **If seen as a Dynamicland Place:** The space should be "quiet" until the laws of the universe are violated, then "surface" the anomaly.

---

## 5. External Critique

### Strengths
- **Sovereign Authority:** External systems often allow machines to auto-suppress. Our mandate keeps the Human Lock as the ultimate source of truth.

### Weaknesses
- **Static Alerting:** We treat AI residue as a flat stream rather than a tiered set of alerts (Advisory vs. Warning).

### Borrowable Assets
- **"Silent Exceptions":** Residues that are logged for provenance but do *not* appear in the Sovereign Tray unless linked to a high-risk event.
- **"Attention Tiers":** Grouping candidates by "Review Impact" (High/Medium/Low).
- **"Ghost Interfaces":** Displays that provide information *only* when the human focuses on them (Dynamicland principle).

### Dangerous Assumptions
- **"Human must know everything":** The belief that human oversight requires being "in the loop" for everything.
- **"Alerts are binary":** Information must be either "shown" or "hidden," ignoring "backgrounded" information.

---

## 6. Synthesis / Re-evaluation of Round 004
- **Correction:** Confidence-Gated Auto-Lock is dangerous. It should be **Confidence-Gated Auto-Suppress** or **Reversible Low-Risk Suggestion**.
- **The "Tray" Problem:** The "Sovereign Tray" must not be a simple inbox. It must be an "Alert Triage" dashboard where AI manages the backgrounded log, and Human manages the off-nominal candidates.

---

## 7. Recommended Next Loop
- **Round 006: CLI Interaction Trace Minimum Contract:** Finalizing the data needed to power this "Invisible Oversight."
- **Round 006: Human Review Fatigue Threshold:** Defining the "Alert Tiering" logic for Stage 0 Events.
- **Round 006: Weak Signal / Quarantine Handling:** Logic for safely archiving low-resolution residues without triggering human review.

## 8. Closeout
This report is external-lens research only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, MCP prototype, reingestion design, UI, JSON schema, CLI trace contract, aggregation threshold, review UI, invisible oversight implementation, or agent architecture was created.
All findings remain provisional external thought assets.
