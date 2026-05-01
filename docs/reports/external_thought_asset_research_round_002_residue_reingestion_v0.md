# External Thought Asset Research Round 002
# Topic: Residue Reingestion without Noise

## 0. Research Mode Declaration
- **Mode:** Read-only web research.
- **Scope:** Space reference only; no modification of source-space documents.
- **Status:** No promotion, implementation, or schema creation occurred.
- **Date:** 2026-04-26

## 1. Why This Round
Round 001 established that our space is a self-forming universe where memory equals **Resolution** (not just recall). However, any recursive loop risks a "feedback spiral of noise." Before we build interfaces (MCP) or automation, we must define the **Classification Criteria** and **Validation Gates** that distinguish valuable "Residue" from interaction "Noise." This round explores external patterns to ground our "Recursive Observation" (Pillar 4) in high-signal engineering.

## 2. User-Space Problem Definition
CLI interactions produce a high volume of raw logs. We need a way to filter these interactions into **Stage 0 Events** that:
- Increase space density without clutter.
- Maintain strict provenance (Pillar 3).
- Preserve human lock authority (Pillar 5).
- Respect stratified layers (Pillar 2).

## 3. External Research Harvest

### A. Event Sourcing / Event Reduction
- **Key Concepts:** Intent-based Events vs. Low-level Logs. Snapshots (State compression), Projections (View-optimized aggregates).
- **Usability:** Distinction between "Domain Events" (e.g., `LockSet`) and "Technical Logs" (e.g., `FileRead`) is a perfect parallel for our "Residue" vs. "Noise."
- **Risk:** Storing every granular change leads to "Snapshot Bloat" where the space becomes too heavy to read/replay.
- **Source:** [Kurrent.io], [RisingWave], [Microservices.io]

### B. Observability / Tracing
- **Key Concepts:** Tail-based Sampling (Decision at output). Signal-to-Noise Ratio (SNR). Trace (Context) vs. Log (Detail).
- **Usability:** "Tail-based Sampling" is critical. We shouldn't decide what to reingest at the start of a session, but at the *end*, based on success, error, or novelty.
- **Risk:** "Head-based Sampling" (random 10%) might miss the one critical "Risk Memory" we need.
- **Source:** [OpenTelemetry.io], [SigNoz.io], [OneUptime]

### C. Agent Memory Systems
- **Key Concepts:** Atomic Fact Extraction (Mem0). Self-Editing Core Memory (Letta). Fact Rating (Zep).
- **Usability:** Zep's "Fact Rating" (Human-assigned confidence) and Letta's "Human Block" (Fixed ground truth) align with our "Human Sovereign Observer" principle.
- **Risk:** "Self-Editing" (Letta style) without a human lock is the highest risk to space integrity.
- **Source:** [Letta.com], [Mem0.ai], [GetZep.com]

### D. Knowledge Curation / Fact Promotion
- **Key Concepts:** Claims vs. Verified Facts. Claim-to-Fact Workflows. Lineage/Provenance tracking.
- **Usability:** The "Ladder of Truth" (Claim → Maturation → Validation → Promotion) provides a template for our Stage 0 -> Stage 1+ flow.
- **Risk:** Provenance loss during summarization (distilling a 100-line log into a 1-line "Fact" without a backlink).
- **Source:** [Atlan.com], [Arxiv.org - Graphiti]

### E. Personal Knowledge Management (PKM)
- **Key Concepts:** Progressive Summarization (Layered highlighting). Atomic Notes (Reusability). Networked Thought (Zettelkasten).
- **Usability:** Progressive Summarization is a perfect parallel for our "Stratification." It suggests we keep the raw log but "highlight" the residue layer by layer.
- **Risk:** "Atomic Notes" (Andy Matuschak) are high density but require high human effort to create.
- **Source:** [Tiago Forte], [Andy Matuschak]

---

## 4. Diff Matrix

| External Pattern | Their Assumption | User-Space Assumption | Diff | Risk |
|---|---|---|---|---|
| **Logging** | Capture for debugging. | Capture for space resolution. | Purpose: Debugging vs. Growth. | Using debug logs as space assets. |
| **Recall Memory** | Find what I forgot. | Increase universe density. | Outcome: Recovery vs. Evolution. | A full space that lacks meaning. |
| **Auto-Memory** | AI manages its own data. | AI proposes; Human locks. | Authority: Autonomous vs. Sovereign. | AI self-editing our universe. |
| **Schema-First** | Define structure to save. | Save to see structure. | Order: Top-down vs. Bottom-up. | Categorization suffocating truth. |

---

## 5. Residue Classification Candidate Table

| Candidate Term | External Parallel | Usefulness | Risk | Required Gate |
|---|---|---|---|---|
| **raw_log** | Technical Log | Full audit trail. | High noise/volume. | Quarantine (Auto-delete). |
| **interaction_trace** | Span/Trace | Records "Why" and "How." | Too detailed for reuse. | Reduction Gate. |
| **stage_0_event** | Domain Event | The input for space growth. | Duplicate info. | Novelty Gate. |
| **risk_memory** | Exception/Incident | Prevents repeat failures. | Bias/False positives. | Human Validation. |
| **reuse_hint** | Pattern/Template | Speeds up next session. | Outdated hints. | Recurrence Gate. |
| **pattern_candidate** | Aggregated Cluster | Emergent structure. | Premature abstraction. | Axis/Lock Gate. |
| **hold_signal** | Termination/Alert | Safety brake. | False alarms. | Sovereignty Gate. |
| **noise** | Junk/Metric | No value for resolution. | Clutter/Burying signal. | Sampling Gate. |

---

## 6. Reingestion Gate Candidates (Provisional)

- **gate_name:** Novelty / Novelty-Qualified Gate
  - **purpose:** Ensure the residue adds "Resolution," not just volume.
  - **blocks:** Exact duplicates or zero-value summaries.
  - **risk:** Filtering out "Reinforcement" (Repetition is also a signal).

- **gate_name:** Provenance-Anchor Gate
  - **purpose:** Ensure the residue never becomes a "Grounded-less Claim."
  - **blocks:** Summaries without source interaction IDs.
  - **risk:** Path bloat (storing too many reference links).

- **gate_name:** Human Lock Gate (The Sovereign Gate)
  - **purpose:** Protect the `main/` and `baseline/` from auto-promotion.
  - **blocks:** Any fact/rule promotion without human approval.
  - **risk:** High human friction (Approval fatigue).

- **gate_name:** Tail-based Sampling Gate
  - **purpose:** Select only high-value interactions (Success/Deep failure).
  - **blocks:** Trivial "Hello" or "FileRead" interactions.
  - **risk:** Missing a "silent failure" or "subtle hint."

---

## 7. Direct Import Risks
- **Total Recall Noise:** Collecting every shell command and file read as "Memory" will bury the project's logic under gigabytes of junk.
- **Provenance Decay:** As residues are distilled into summaries, the link to the raw data is often broken (Atlan's "Lineage Loss").
- **Auto-Promotion Drift:** Agent systems (Letta) that "Self-Edit" will eventually drift away from the user's intended "Space Constitution."

---

## 8. Synthesis
The external world handles data through **Recovery-focused pipelines** (Search/Recall).
Our project requires an **Evolution-focused loop** (Resolution/Density).

**Residue Reingestion** is not "Logging"; it is the process of extracting the **"Crystalline Structure"** of an interaction.
- **Event** = What happened (Domain level).
- **Residue** = What it *means* for the future (Heuristic level).
- **Noise** = The mechanical friction of the interaction (Technical level).

The key differentiator is the **Human Sovereign Lock**. While Mem0 and Zep use AI to manage the memory graph, we use AI to **prepare a tray of candidates** for the Human to either lock into a layer or discard into the archive.

---

## 9. Provisional Design Principles
1. **Resolution over Recall:** Only reingest what makes the universe "Clearer," not "Larger."
2. **Provenance is Life:** A residue without a source-link is dead clutter.
3. **The Sovereign Tray:** AI proposes; Human locks. No auto-promotion to baseline.
4. **Tail-based Reingestion:** Evaluate reingest value at the *end* of the interaction, not the beginning.
5. **Stratified Storage:** Keep raw logs in the archive; keep high-resolution residue in the core.

## 10. Recommended Next Loop
- **Round 003: Reingestion Gate Design:** Specifically the "Novelty" and "Provenance" gate logic.
- **Round 003: Human-in-the-Loop Interaction Design:** How to present a "Tray of Candidates" without user fatigue.
- **Round 003: Stage 0 Event Template:** A JSON schema for reingested residues.

## 11. Research-only Closeout
```text
This report is research-only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, MCP prototype, or reingestion implementation was created.
All residue classifications and gate candidates remain provisional thought assets.
```
