# External Lens Space Re-evaluation Round 015
# Topic: Low-Friction Human Review Ergonomics

## 0. Research Declaration
- **Mode:** Web research first, external view first.
- **Scope:** Read-only / No source-space modification.
- **Status:** Research report only; no implementation or internal design.
- **Authority:** All findings are provisional external thought assets.
- **Date:** 2026-04-26

## 1. Why Round 015
Round 014 confirmed that a "Summary-to-Evidence" drill-down is the fundamental pattern for balancing "Intent" and "Provenance." However, even a frictionless drill-down can become a bottleneck if the *review act itself* (accepting, rejecting, escalating) is high-friction. This round investigates how external systems design for "Review Ergonomics," ensuring human supervisors can perform oversight in seconds rather than minutes.

## 2. External Case Harvest

### A. Code Review (GitHub/Gerrit)
- **Key Concepts:** Review queues, keyboard-driven triage, inline diffs, "Approve/Request Changes."
- **External View:** The "Review" is an ergonomic interaction, not a process hurdle.
- **Borrowable Asset:** **"Keyboard-driven Triage."** Using hotkeys (`a` for approve, `r` for request) to move through the queue in seconds.
- **Dangerous Assumption:** Shortcuts can lead to "Rubber-Stamping" (approving without actual review).

### B. Security Operations (SOC)
- **Key Concepts:** Alert disposition, incident prioritization, analyst workbench.
- **External View:** Analysts triage thousands of alerts using "Disposition" shortcuts (True Positive, False Positive, Ignored).
- **Borrowable Asset:** **"Rapid Disposition."** Categorizing every incoming candidate into a immediate "Disposition bucket" rather than treating every event as a unique task.
- **Dangerous Assumption:** That the analyst has enough context to make a "True/False Positive" decision in seconds.

### C. Observability (Incident Management)
- **Key Concepts:** Alert acknowledgment, escalation paths, severity sorting.
- **External View:** The "On-call" engineer acknowledges an alert instantly; resolution happens later.
- **Borrowable Asset:** **"Acknowledgment vs. Resolution."** Separate the *acknowledgment* of a candidate (Sovereign Lock) from the *full resolution* (the implementation phase).
- **Dangerous Assumption:** Acknowledgment without resolution creates a sense of false security.

### D. Medical Decision Support (CDSS)
- **Key Concepts:** Interruptive vs. Passive, alert filtering.
- **External View:** Interrupting a doctor is costly. Only the most critical, actionable alerts get an interruptive UI.
- **Borrowable Asset:** **"Threshold-based Interruption."** AI alerts should be graded by *Human Attention Cost*.
- **Dangerous Assumption:** That a doctor can accurately grade alert importance in a high-stress environment.

### E. Research/Annotation Workflows
- **Key Concepts:** Active Learning, annotation queues, confidence-based sampling.
- **External View:** Humans are asked to label only the items where the AI is most uncertain.
- **Borrowable Asset:** **"Uncertainty-gated Review."** Only surface items that the AI is *unsure* about to the Human Sovereign Observer.
- **Dangerous Assumption:** That "uncertainty" in AI logic maps to "importance" for the human.

---

### 3. External Review Ergonomics Matrix

| External System | Review Object | First-view Summary | Immediate Actions | Inline Evidence | Hidden Evidence | Friction Reduction | Authority Protection | Failure Mode | User Space Relevance |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Code Review** | Pull Request | Diff Summary | App/Req Change | Diff Context | Review thread | Keyboard shortcuts | Human Lock | Rubber Stamping |
| **SOC** | Incident | Alert Card | True/False Pos | Timeline | Raw Events | Rapid Disposition | Evidence Chain | False Positive |
| **Observability**| Incident | Alert Summary | Ack/Escalate | Trace View | Raw Metrics | Acknowledgment | Root Cause | Metric Bias |
| **Medical** | Alert | Risk Summary | Accept/Ignore | Vitals History | Audit Trail | Tiered alerts | Sovereign Triage | Alarm Blindness |
| **Research** | Annotation | Sample Point | Accept/Reject | Metadata | Source Data | Confidence Triage | Reviewer fatigue | Annotation Bias |

---

### 4. User Space Seen Through Low-Friction Human Review Lens
- **Review Bottleneck:** In our space, the "Sovereign Lock" is currently a high-friction process (manual check, copy-paste, manual validation).
- **Ergonomics Requirement:** We need to transform the "Locking" process into a "Disposition" process (Accept, Defer, Quarantine, Escalate) that can be done at the speed of thought.
- **Sovereign Attention:** Our goal is not *less* review; it is *faster, higher-quality* review through better affordances.

### 5. External Critique

#### Strengths
- **Sovereign Authority:** We don't automate "Locking," we only automate the *visibility* of what needs to be locked.

#### Weaknesses
- **Interaction Model:** Our interaction model is purely "Manual"; we lack keyboard/shortcut-style triage for candidates.

#### Misunderstanding Risk
- Outsiders will see our "Sovereign Lock" as an "Inefficient UI" rather than an "Integrity Protocol."

#### Differentiation
- We group by **Conceptual Maturation**, not just time or error-code.

#### Borrowable Assets
- **"Rapid Disposition":** Categorizing every incoming candidate into a clear bucket (e.g., [Keep], [Discard], [Escalate]) immediately upon viewing.
- **"Acknowledgment Tiers":** Distinguishing between "Acknowledged" (Human sees it) and "Locked" (Canonical truth established).

#### Dangerous Assumptions
- **"Human will drill down":** Human observers will skip verification if the friction is too high.

---

### 6. Next External Search Questions
- How to design "Human-in-the-loop" interfaces that are invisible until an "Off-Nominal" event occurs?
- Are there models for "Confidence Scaling"—where AI confidence is weighted by the *risk* of the operation?

### 7. Closeout
This report is external-lens research only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, review UI, triage dashboard, shortcut design, evidence schema, event grouping design, suppression logic, status schema, dashboard, UI, reingestion design, UI, JSON schema, CLI trace contract, or aggregation threshold was created.
All findings remain provisional external thought assets.
