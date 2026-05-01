# Harness Engineering 구조 판독 리서치 결과

## 0. Declaration
- **Mode:** Research-only / Structure-reading.
- **Scope:** Read-only reference material; no modification of source-space documents.
- **Status:** Strategic synthesis; no implementation or internal design.
- **Authority:** All findings are provisional thought assets for future discussion.
- **Date:** 2026-04-26

## 1. Why This Round
We have established a provisional interaction contract. However, we must ensure that our "Space" doesn't inadvertently recreate the complexity of external "Agent Harnesses" (OpenHarness, AutoGen, etc.). By analyzing *why* these frameworks exist structurally, we can adopt their "Thought Assets" (e.g., provenance-tracking, safety hooks) while rejecting their "Dangerous Assumptions" (e.g., agent autonomy, auto-lock).

## 2. External Case Harvest

### A. OpenAI Harness Engineering (Codex)
- **Problem:** Agents need a predictable environment to reliably perform coding tasks.
- **Signal:** Tools/Knowledge are co-located in the repository; execution is structured.
- **Human Role:** Steer intent; evaluate output.
- **Key Asset:** **"Repository-as-Record"** — treating docs/plans as the system's ground truth.

### B. Milvus Harness Engineering (AI Agents)
- **Problem:** Agents are unreliable without structured execution layers.
- **Signal:** Harnessing the environment (permissions, tool constraints).
- **Key Asset:** **"Harness as Infrastructure"** — the layer *around* the model that provides 'hands and eyes.'

### C. MindStudio (Orchestration)
- **Key Concepts:** Subtasks, context pruning, iteration loops, escalation paths.
- **Problem:** Agentic workflows suffer from noise (pollution, runaway loops).
- **Key Asset:** **"Workflow Orchestration"** — defining the loop structure explicitly.

### D. OpenHarness (Open Source Infra)
- **Key Concepts:** Hooks (PreToolUse), Tool Registry, Multi-level Permissions.
- **Problem:** Need for cross-session consistency and safety boundaries.
- **Key Asset:** **"Hooks"** — the ability to intercept the execution cycle to add provenance/observability.

---

## 3. Structural Organ Map

| Organ | External meaning | Structural problem solved | New risk created | Our corresponding concept |
| :--- | :--- | :--- | :--- | :--- |
| **Model** | Intelligence Layer | Lack of reasoning | Non-determinism | LLM Worker |
| **Agent Loop** | Execution Cycle | Task intermittency | Runaway Loops | Observation Loop |
| **Tools** | Hands/Eyes | Capability gap | Capability creep | CLI/Worker Tools |
| **Hooks** | Lifecycle Interception | Lack of provenance | Hook-dependency | Preflight Guard |
| **Permissions** | Governance | Safety breach | Access denial | Sovereign Lock |
| **Memory** | State Persistence | Context loss | Pollution/Drift | Deep Space / Trace |
| **Context Compression**| Volume reduction | Token limits | Information loss | Session Summary |
| **Observation** | Visibility Stack | Legibility gap | Noise/Signal ratio | Observer Surface |

---

## 4. Analysis of External Methods

### Q1. 하네스 엔지니어링이 무엇인가?
- **claim:** Agent harness is the infrastructure layer for reliable AI execution.
- **structure_meaning:** It separates *what* is executed (the model/task) from *how* it is executed safely and traceably.
- **note_for_our_space:** We are building a "Space-Side Harness"—a system that governs the CLI worker's interactions without being an "agent controller."

### Q2. 어떻게 사용하는가?
- **usage_pattern:** Tool-Call/Execution -> Lifecycle Hook -> Observation -> Triage/Lock.
- **structural_role:** The harness sits in the *Observation Layer* between the CLI worker and the human observer.

### Q3. 어떻게 효과적인가?
- **effective_condition:** High-resolution traces coupled with strict Human Sovereign Locks.
- **why_it_matters:** Without hooks, execution is "blind" to provenance. Without locks, it is "uncontrolled."

### Q4. 문제점/위험
- **runaway_loop:** Feedback loops without termination criteria (our Observation Surface must force a HOLD).
- **context_pollution:** Storing transient interaction artifacts as "Memory." (Our solution: Session Summary Grouping).

---

## 5. Structural Re-description

- **User Space:** A Sovereign Universe.
- **Harness:** Not an orchestration engine, but a **Provenance Enforcement Layer**.
- **Observation Layer:** A visibility stack that signals state (`Validated`, `Needs Review`) without owning the system's logic.

## 6. Borrowable Thought Assets
1. **"Lifecycle Hooks":** Triggering the `Structured Footer` and `Preflight Guard` based on execution stages (PreToolUse/PostToolUse).
2. **"Triage Filters":** Sampling residue based on session outcomes (Tail-based).
3. **"Contextual Metadata":** Embedding evidence anchors directly into the summary layer.

## 7. Dangerous Assumptions
1. **"Autonomy = Success":** The external world favors autonomous agents; we prioritize sovereign integrity.
2. **"Standardization = Schema":** Avoiding rigid ontologies by focusing on *process status* signals.
3. **"Automated Oversight":** The external world automates the *oversight*; we automate the *legibility* so the human can provide the oversight.

## 8. Final Judgment

**Verdict:** PASS_WITH_NOTE

**Corrected Cases (Reflected):**
1. **Structure Separation:** Agent loops are workers, not the "Space" itself.
2. **Preflight Guard:** Confirmed as the primary safety gate for high-impact mutation.
3. **Observation Record:** Confirmed as the "Triage Layer" between the Hand (CLI) and the Universe (Space).

**Recommended next step:** 
- Final synthesis of "Space Strategy" into a formal `Interaction Contract`. The logic is sound, and we are ready to move from research to drafting the reference document.

**Do not proceed to implementation yet:** Yes.
