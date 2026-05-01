# External Lens Space Re-evaluation Round 003
# Topic: Multi-Agent Friction / Worker Noise

## 0. Research Declaration
- **Mode:** External-lens research only.
- **Scope:** Read-only / No source-space modification.
- **Status:** No implementation, internal design, or gate implementation.
- **Authority:** All findings are provisional external thought assets.
- **Date:** 2026-04-26

## 1. Why Round 003
Round 002 established that we need a high-resolution "Residue Reingestion" loop. However, as the number of agents, workers, and traces grows, we face a new bottleneck: **Multi-Agent Friction**. External orchestration systems (CrewAI, AutoGen, LangGraph) deal with "coordination cost" and "output fatigue." To avoid these pitfalls, we must examine their coordination models and their assumptions about human review, ensuring we don't accidentally import their "Agent Autonomy" bias into our "Sovereign Observer" universe.

## 2. External Case Harvest

### A. Multi-Agent Frameworks (CrewAI, AutoGen, LangGraph)
- **Their View:** Coordination is a graph-transition or dialogue-negotiation problem.
- **What They Build:** Explicit Orchestrators (Supervisors), Chat-loops, or Flow-based State Machines.
- **Coordination Model:** Explicit routing (LangGraph), Conversational negotiation (AutoGen), or Role-based process hierarchies (CrewAI).
- **Noise Handling:** Managing context windows via state pruning or conversation summarization.
- **Human Oversight:** Often an "interrupt" that pauses the agent flow to seek input.
- **Hidden Assumption:** "Supervisor Agent" + "Human Interrupt" = Sufficient coordination.
- **External Lens View of User Space:** Sees our space as an "Under-orchestrated universe." They would try to add a "Supervisor Agent" immediately, which would be a **Dangerous Product Assumption** that destroys the human's sovereign lock.

### B. Agentic Workflows (Orchestration vs. Autonomy)
- **Their View:** Autonomy is the goal; orchestration is the guardrail.
- **What They Build:** Autonomous agents with "Tools" (Tool-use loops).
- **Coordination Model:** The agent "thinks" (ReAct) to decide tool use.
- **Noise Handling:** Guardrails (e.g., NeMo Guardrails) to prevent off-script execution.
- **Human Oversight:** Manual confirmation of tool execution.
- **Hidden Assumption:** "Tool-use = Agentic Intelligence."
- **External Lens View of User Space:** Sees our refusal to automate as a "Bottleneck."

### C. Knowledge Work Friction (Fatigue / Load)
- **Their View:** Cognitive load is a function of "Choice" and "Context Switching."
- **What They Build:** Automated filters, priority dashboards, AI curators.
- **Coordination Model:** Push-based notifications vs. Pull-based dashboards.
- **Noise Handling:** Filtering alerts (Alert Fatigue).
- **Human Oversight:** Reviewing summaries.
- **Hidden Assumption:** "Aggregation = Clarity."
- **External Lens View of User Space:** Our manual lock policy looks like "high-friction governance."

### D. Software Engineering (CI/CD / Observability)
- **Their View:** Signal-to-Noise Ratio (SNR) is a runtime optimization problem.
- **What They Build:** Tail-based sampling, Trace vs. Log separation.
- **Coordination Model:** Sampling, aggregation, aggregation-rules.
- **Noise Handling:** Tail-based sampling (keep what is significant).
- **Human Oversight:** Alerting on high-value incidents.
- **Hidden Assumption:** "Metrics = Truth."
- **External Lens View of User Space:** Our `residue` concept is a "Domain-Event Sampling Strategy."

---

## 3. External Coordination Matrix

| External Pattern | Their Coordination Assumption | Agent Role | Human Role | Noise Handling | How User Space Differs | Useful Asset | Risk |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Orchestrator** | Supervisor defines logic. | Worker | Final Approval | Routing/Pruning | Space defines laws, not the agent. | Supervisor Pattern | Auto-Promotion |
| **Conversational** | Negotiation leads to truth. | Debater | Mediator | History Truncation | Provenance is higher than negotiation. | Consensus Log | Emergent Chaos |
| **State Machine** | Transition rules define reality. | Executor | State Designer | Explicit Paths | Layers precede state. | Temporal Checkpoints| Schema Suffocation|
| **Observability** | Sampling reduces cost. | Recorder | Alert Receiver | Sampling Strategy | Resolution > Storage. | Tail-Sampling | Metric Bias |

---

## 4. User Space Seen Through Multi-Agent Friction Lens
1. **As an Agentic Workspace:** A "Managed Environment" where the agent is a worker subject to the laws of the space.
2. **Why Agent is a Worker, not the body:** If the agent *is* the body, the space becomes just a temporary staging ground (RAM). If the space is the body, the agent is merely a temporary resident (worker).
3. **Biggest Difference:** External orchestration *automates coordination* to reduce human cost. User space *stratifys observation* to increase human intelligence.
4. **User Space Strengths:** Our "Human Lock" prevents the "Agent Autonomy Drift" that plagues external orchestration.
5. **Weaknesses/Ambiguity:** We currently lack a "Residue Filtration Rule," which externally is handled by "Orchestration Logic."

---

## 5. External Critique
- **Strengths Seen from Outside:** The "Human Lock" is a sophisticated guardrail against the "Agentic Autonomy" common in external frameworks.
- **Weaknesses Seen from Outside:** The lack of automated coordination logic means the human currently performs the "Orchestration" task.
- **Misunderstanding Risk:** External observers will confuse our "manual locking" with "system slowness" rather than "Sovereign Authority."
- **Differentiation:** We prioritize **provenance** and **layer-integrity** over *coordination speed*.
- **Borrowable Assets:** Tail-based sampling (OTel) for filtering residue, Supervisor Patterns for logical flow (but without auto-lock).
- **Do-not-borrow:** Any framework that grants agents "Self-Editing" authority over canonical memory.

---

## 6. Diff / Merge Findings
- **Diff:** External systems automate the *logic* of coordination. We *stratify* the logic of coordination so humans can read it through lenses.
- **Merge:** We can merge the **Supervisor Pattern** for organizing AI-proposal layers (e.g., a "Classifier Worker" proposing a residue, followed by a "Refiner Worker"), provided the final lock is Human.

---

## 7. Borrowable Thought Assets
- **"Tail-based Reingestion":** Use the interaction outcome (success/error/novelty) to judge the reingestion value.
- **"Supervisor Pattern" (Logic-only):** AI proposing roles for other AI (e.g., "Refiner," "Classifier") in the Sovereign Tray.
- **"Sampling for Resolution":** Only store sessions that push the space's "Information Frontier."

---

## 8. Dangerous Assumptions
- **"The Supervisor Agent knows all":** Never trust an AI to supervise itself without provenance tracing.
- **"Automation reduces friction":** Coordination automation often shifts friction from "doing the work" to "verifying the automation."
- **"Agent Memory is State":** Agentic systems store state to *act*. We store residues to *understand*.

---

## 9. Next External Search Questions
- How to implement "Automated Coordination Proposals" that still require 100% human lock?
- Are there models for "Layer-Aware Supervision" where an AI proposes a residue *only for a specific layer*?

## 10. Closeout
This report is external-lens research only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, MCP prototype, reingestion design, UI, JSON schema, CLI trace contract, or aggregation threshold was created.
All findings remain provisional external thought assets.
