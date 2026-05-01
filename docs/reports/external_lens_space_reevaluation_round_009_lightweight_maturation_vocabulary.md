# External Lens Space Re-evaluation Round 009
# Topic: Lightweight Maturation Vocabulary

## 0. Research Declaration
- **Mode:** Read-only / Criteria design report.
- **Scope:** Space reference only; no modification of source-space documents.
- **Status:** Research report only; no implementation or internal design.
- **Authority:** All findings are provisional external thought assets.
- **Date:** 2026-04-26

## 1. Why Round 009
Round 008 established that "Ambient Signals" are necessary to prevent the "Dark Room" effect. However, these signals require a **Lightweight Vocabulary** that can distinguish maturity levels (e.g., `Draft` vs. `Canonical`) without imposing the weight of a full schema or ontology. We must identify how external systems use minimal sets of status terms to manage lifecycle states without destroying the "Ambiguity-Preserving" nature of their work.

## 2. External Case Harvest

### A. ADR / RFC / Proposal Lifecycle
- **Key Concepts:** Draft, Review, Accepted, Superseded, Deprecated.
- **Their Problem:** Decisions need a clear temporal status so future developers know what is current vs. historical.
- **Vocabulary:** `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded`.
- **Borrowable Asset:** **"Temporal Superseding."** Statuses indicate history (what used to be true) without deleting the past.
- **Dangerous Assumption:** Every thought asset follows a linear lifecycle.

### B. Research / Evidence Maturity
- **Key Concepts:** Hypothesis, Evidence, Finding, Validated Claim.
- **Their Problem:** Distinguishing between a "hunch" and a "proven discovery" to prevent premature conclusion.
- **Vocabulary:** `Hypothesis`, `Provisional`, `Validated`, `Refuted`.
- **Borrowable Asset:** **"Confidence-Gated Status."** State depends on the "Evidence Gate" it has passed.
- **Dangerous Assumption:** Using "Confidence" (0-100%) as a proxy for "Truth."

### C. Product Discovery / Assumption Mapping
- **Key Concepts:** Assumptions, Validated Learning, Discovery, Delivery.
- **Their Problem:** Avoiding "Premature Delivery" based on unvalidated assumptions.
- **Vocabulary:** `Risky`, `Tested`, `Validated`, `Pivoted`.
- **Borrowable Asset:** **"Assumption State."** Tracking how "risky" an assumption is helps triage human attention.
- **Dangerous Assumption:** Assuming "Validation" is a binary state; learning is often continuous.

### D. PKM / Evergreen Notes
- **Key Concepts:** Fleeting, Literature, Permanent, Evergreen.
- **Their Problem:** Preventing "Information Clutter" vs. "Durable Knowledge."
- **Vocabulary:** `Seedling`, `Sapling`, `Evergreen`.
- **Borrowable Asset:** **"Metaphorical Maturation."** Using natural language status that mirrors the note's "growth" (e.g., `Maturing`).
- **Dangerous Assumption:** "Linking is Maturity." A linked note can still be factually shallow.

### E. Software Collaboration Status
- **Key Concepts:** Draft, Review, Approved, Blocked, Done.
- **Their Problem:** Managing coordination flow in multi-human teams.
- **Vocabulary:** `Draft`, `Review`, `Approved`, `Blocked`, `Done`.
- **Borrowable Asset:** **"Interrupt-Driven States."** Only `Review` or `Blocked` interrupts the user.
- **Dangerous Assumption:** Over-formalizing the status (too many states = status bloat).

---

### 3. External Status Vocabulary Matrix

| External System | Status Vocabulary | Transition Trigger | Protects | Failure if Absent | Failure if Overdone | User Space Relevance |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ADR/RFC** | Proposed, Accepted, Deprecated | Consensus | History / Context | Architectural Decay | Rigid Process | ADR-style Lifecycle |
| **Research** | Hypothesis, Provisional, Validated | Evidence Gain | Provenance | Lost Context | Abstract Bloat | Failure Traces |
| **Discovery** | Risky, Tested, Validated | Learning Outcome | Focus | Lost Focus | Premature Delivery | Confidence Triage |
| **Evergreen** | Seedling, Sapling, Evergreen | Refinement | Knowledge Density | Information Clutter | Structural Collapse | Maturation-by-Refinement|

---

### 4. User Space Seen Through Lightweight Maturation Vocabulary Lens
- **The "Dark Room" problem:** Our space lacks any signal. Observers see a binary: "Empty" or "Full."
- **The Solution:** We need 3-4 "Maturation Stages" that signal the *current state* of our self-forming cosmology.
- **The Risk:** If these states are too formal, we lose the "Ambiguity Preservation" that makes the space unique. We must choose words that suggest *growth* rather than *classification*.

---

### 5. External Critique

#### Strengths
- **Provenance-First:** Our lineage-tracking is stronger than external lifecycle tags, as we don't just tag, we link to the *event*.

#### Weaknesses
- **Maturity Opacity:** We lack the common vocabulary to signal "Experimental," "Stable," or "Deprecated" paths.

#### Misunderstanding Risk
- Observers will mistake our lack of lifecycle vocabulary for "lack of process" or "unprofessionalism."

#### Differentiation
- We use vocabulary as an **Observer Signal**, not an **Ontological Classifier**.

#### Borrowable Assets
- **"Provisional":** Signals exploration without finality.
- **"Maturing":** Signals an active formation state (replaces "Chaos").
- **"Canonical":** Signals a Human-Locked law of the universe.
- **"Superseded":** Signals that a prior line of thought was corrected (Provenance preservation).

#### Dangerous Assumptions
- **"Lifecycle Completeness":** Some assets (like "Failure Traces") should never be "Completed" or "Done."

---

### 6. Borrowable Thought Assets
- **"Lifecycle Vocabulary as Signal":** A minimal set of status terms to guide the "Sovereign Tray."
- **"Process Status":** Tracking the *state of maturation* rather than the *type of file*.
- **"Failure Preservation":** Using `Superseded` to record why a path failed, rather than deleting it.

---

### 7. Dangerous Assumptions
- **"Everything needs a Status":** Applying status words to mechanical logs (e.g., `log_001: Accepted`).
- **"Maturity = Linearity":** Thinking research only moves from `Provisional` to `Canonical`. Research often loops.
- **"The Status is the Metadata":** Status should be a "Lens Reading," not an attached field if possible.

---

### 8. Next External Search Questions
- How to implement "status signal" without schema-based tagging (e.g., using ambient file-path markers or non-intrusive header signals)?
- Are there models for "contextual status" where a residue's maturity depends on the lens through which it is read?

---

### 9. Closeout
This report is external-lens research only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, ontology, tag system, status schema, dashboard, UI, reingestion design, UI, JSON schema, CLI trace contract, or aggregation threshold was created.
All findings remain provisional external thought assets.
