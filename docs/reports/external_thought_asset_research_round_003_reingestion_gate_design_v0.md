# External Thought Asset Research Round 003
# Topic: Reingestion Gate Design

## 0. Research / Criteria Mode Declaration
- **Mode:** Read-only criteria design report.
- **Scope:** Space reference only; no modification of source-space documents.
- **Status:** No implementation, schema lock, or baseline promotion occurred.
- **Authority:** All gates, classifications, and fields remain provisional thought assets.
- **Date:** 2026-04-26

## 1. Why Round 003
Round 002 established that we must distinguish between "Technical Logs" (mechanical noise) and "Domain Events" (high-resolution residues). However, knowing the distinction is not enough; we need a functional set of **Gates** to filter raw interactions before they reach Stage 0. 

Round 003 moves from "What to store" to "How to decide." Defining these gates prevents **Schema-First Suffocation** (forcing structure too early) and **Total Recall Noise** (storing everything). We are building the "Sovereign Filtration Logic" that precedes any UI (Sovereign Tray) or JSON contract.

## 2. Core Principle
- **Not every log becomes an event.** (Filtering mechanical noise)
- **Not every event becomes memory.** (Filtering transient actions)
- **Not every memory becomes rule.** (Filtering provisional vs. canonical)
- **AI may propose residue, but human locks promotion.** (Protecting Sovereignty)

## 3. Gate Candidate Overview
The proposed gates act as a multi-layered sieve, moving from technical sampling to philosophical alignment:
1. **Tail-Based Sampling Gate:** Is this session worth keeping?
2. **Domain Event Gate:** What actually happened in human/system terms?
3. **Novelty-Qualified Gate:** Does this add new resolution?
4. **Provenance-Anchor Gate:** Is the lineage intact?
5. **Layer-Relevance Gate:** Where does this belong?
6. **Risk / Quarantine Gate:** Is this safe to hold?
7. **Pattern Candidate Gate:** Is this a repeat signal?
8. **Human Sovereign Lock Gate:** Is this ready for the baseline?

---

## 4. Detailed Gate Candidates

### 4.1 Tail-Based Sampling Gate
- **Purpose:** Decide if the interaction produced anything of value at the end of the session.
- **Input:** Raw session logs and execution results.
- **Questions:** 
  - Did the session achieve a milestone, encounter a critical risk, or discover a new pattern?
  - Was this a trivial interaction (e.g., just reading files without decisions)?
- **Output States:** `keep_as_candidate`, `raw_log_only`, `discard_as_noise`.
- **Blocks:** Redundant shell commands, successful but empty "no-op" sessions.
- **Risk:** High-value subtle signals might be discarded if the "value" threshold is too high.

### 4.2 Domain Event Gate
- **Purpose:** Translate technical friction into system-level events.
- **Input:** Sampled interaction traces.
- **Questions:** 
  - Can this interaction be summarized as an "Intent-based Event" (e.g., `LockRuleSet`) rather than a "Mechanical Action" (e.g., `write_file`)?
  - Does it affect the "Space Cosmology" or its "Laws"?
- **Output States:** `domain_event_candidate`, `technical_log_only`.
- **Blocks:** Granular file edits, intermediate search results.
- **Allows:** Decisions, strategic shifts, confirmed facts.

### 4.3 Novelty-Qualified Gate
- **Purpose:** Ensure "Resolution over Recall."
- **Input:** Proposed Domain Events.
- **Questions:** 
  - Does this residue clarify, expand, or contradict existing space knowledge?
  - Is it a 1:1 duplicate of an existing "Residue"?
- **Output States:** `new_signal`, `reinforces_existing`, `duplicate_noise`, `contradiction_signal`.
- **Blocks:** Repetitive re-confirmation of already "locked" facts.

### 4.4 Provenance-Anchor Gate
- **Purpose:** Protect the "Pillar of Provenance" (Pillar 3).
- **Input:** Novel residues.
- **Questions:** 
  - Is there a clear link to the source session, prompt, and decision file?
  - Can the human trace this "fact" back to its raw mechanical evidence?
- **Output States:** `anchored_candidate`, `quarantine_low_provenance`.
- **Blocks:** Summaries that have lost their "Why" or "Where."

### 4.5 Layer-Relevance Gate
- **Purpose:** Ensure the residue is placed on the correct contextual axis.
- **Input:** Anchored residues.
- **Questions:** 
  - Which layer does this belong to (Philosophy, Operation, Implementation)?
  - Is there a layer mismatch (e.g., an implementation detail trying to become a philosophy)?
- **Output States:** `layer_identified`, `layer_mismatch_hold`.
- **Blocks:** Cross-layer contamination.

### 4.6 Risk / Quarantine Gate
- **Purpose:** Safeguard the space from over-structuring or hallucination risks.
- **Input:** All candidates that trigger "risk" flags.
- **Questions:** 
  - Does this residue promote "Auto-automation" or "Premature Schema"?
  - Could this hint lead to context hallucination in the next turn?
- **Output States:** `risk_memory`, `quarantine_asset`, `hold_signal`.
- **Allows:** Keeping a "memory of a danger" without letting that danger become a "rule."

### 4.7 Pattern Candidate Gate
- **Purpose:** Identify emergent structure before it is locked.
- **Input:** Repeated or related residues.
- **Questions:** 
  - Is this a one-off event or a repeating behavior?
  - Should this be grouped into a "Pattern Candidate" for human review?
- **Output States:** `one-off_residue`, `pattern_candidate`.
- **Risk:** Premature abstraction based on insufficient data (coincidence vs. pattern).

### 4.8 Human Sovereign Lock Gate
- **Purpose:** Final authority gate.
- **Input:** Any candidate proposed for `main/`, `baseline/`, or `rule` status.
- **Questions:** 
  - Does the human approve this as a "Canonical Rule"?
  - Does it conflict with the user's current line or axis?
- **Principle:** AI *proposes* the lock; Human *turns* the key.

---

## 5. Residue Classification Candidate Table

| Term | Definition | Must Pass Gate | Possible Next State | Example |
|---|---|---|---|---|
| **raw_log** | Unfiltered technical output. | N/A (Archive) | `discarded` | `ls -R` output. |
| **interaction_trace** | Chronological "How & Why". | Tail-Sampling | `residue` | Flow: Research -> Strategy -> Exec. |
| **domain_event** | System-level intent. | Domain Event Gate | `stage_0_candidate` | "Term 'AI Sovereignty' corrected." |
| **risk_memory** | Record of a danger/fail. | Risk/Quarantine | `hold_signal` | "Avoid auto-schema promotion." |
| **reuse_hint** | Tactical heuristic. | Novelty-Qualified | `pattern_candidate` | "Use tail-sampling at session end." |
| **pattern_candidate** | Emergent rule proposal. | Pattern Gate | `promotion_candidate` | "Recurring Layer-Reading mismatch." |
| **promotion_candidate**| Ready for baseline. | Human Sovereign Lock| `locked_rule` | A new established "Design Rule." |
| **noise** | Mechanical friction. | Any Gate | `discarded` | Redundant file reads. |

---

## 6. Stage 0 Event Template Candidate Fields
*Note: This is not a schema. These are fields under research for their necessity/risk.*

- **domain_event_summary:** (Necessity: High) Essential for resolution. (Risk: AI over-summarizing/loss of detail).
- **residue_type:** (Necessity: High) Guides the next worker. (Risk: Misclassification).
- **layer_candidate:** (Necessity: High) Prevents layer mismatch. (Risk: AI guessing the wrong layer).
- **provenance_anchor:** (Necessity: Critical) Link to source interaction. (Risk: Broken links over time).
- **novelty_reason:** (Why keep this?) (Risk: Bloat if novelty is too low).
- **risk_flag:** (Alert signal).
- **human_lock_required:** (Boolean gate flag).
- **do_not_promote_as:** (Lowering requirement - e.g., "Do not use as baseline").

---

## 7. Gate Flow Draft (Conceptual)
`raw_log` -> `Tail-Based Sampling` -> `Domain Event Gate` -> `Novelty Gate` -> `Provenance Gate` -> `Layer Relevance Gate` -> **[Classification into Residue/Risk/Hint/Pattern]** -> `Promotion Candidate` -> `Human Sovereign Lock`.

---

## 8. Direct Risks
- **Technical Log Flooding:** If the Domain Event Gate is too weak, the space becomes a graveyard of `git status` logs.
- **Context Hallucination:** Using "Residue" from the wrong layer for "Prompt Anchoring."
- **Provenance Decay:** Summaries becoming "floating claims" without evidence.
- **Human Review Fatigue:** Proposing too many "Candidates" for the Human Lock Gate.
- **Schema-First Suffocation:** Locking the JSON template before the gate logic is battle-tested.

## 9. Open Questions
- What is the minimum metadata required for a "Domain Event" to remain high-resolution?
- At what point does a "Pattern Candidate" become "Ready for Review"?
- How long should a "Weak Signal" stay in `hold` before being archived or discarded?

## 10. Recommended Next Loop
- **Round 004: Stage 0 Event Candidate Contract:** Defining the interaction between CLI and Space for the first reingest attempt.
- **Round 004: Human Sovereign Review Tray Criteria:** Specifically, how to present these candidates to reduce user fatigue.
- **Round 004: CLI Interaction Trace Minimum Contract:** What must the CLI record during the session to satisfy the gates later.

## 11. Closeout
This report is criteria-only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, MCP prototype, reingestion implementation, UI, or JSON schema was created.
All gates, classifications, and template fields remain provisional thought assets.
