# External Thought Asset Research Round 006
# Topic: CLI Interaction Trace + Aggregation Threshold

## 0. Criteria-only Declaration
- **Mode:** Read-only criteria design report.
- **Scope:** Space reference only; no modification of source-space documents.
- **Status:** No implementation, schema lock, or baseline promotion occurred.
- **Authority:** All trace fields, aggregation thresholds, and event candidate shapes remain provisional thought assets.
- **Date:** 2026-04-26

## 1. Why Round 006
Round 005 revealed a critical bottleneck: **Human Review Fatigue**. Generating 5-10 individual residues per session makes the "Sovereign Tray" unmanageable for the user. We need an **Aggregation Threshold** to compress session-specific residues into a single high-resolution "Stage 0 Event Candidate." 

Simultaneously, we need a **CLI Interaction Trace Minimum Contract** to ensure the CLI records enough data *during* the session to auto-fill the reingestion contract at the *end*.

## 2. CLI Interaction Trace Minimum Contract Candidate
What the CLI must record during a session to satisfy reingestion requirements.

| Trace Field | Purpose | Supports Stage 0 Field | Minimum/Extended |
| :--- | :--- | :--- | :--- |
| **session_id** | Unique identifier for the session. | `source_interaction` | **Minimum** |
| **user_instruction**| The core prompt or correction. | `trigger_input` | **Minimum** |
| **source_files_read**| Files accessed during research. | `provenance_anchor` | **Minimum** |
| **decision_points** | Strategic shifts or rule logic. | `domain_event_summary` | **Minimum** |
| **final_verdict** | Success/Fail/Wait status. | `recommended_next_state`| **Minimum** |
| **residue_candidates**| Early detection of hints/risks. | `residue_type` | **Minimum** |
| **do_not_promote_as**| Immediate user-facing constraints. | `do_not_promote_as` | **Minimum** |
| **errors_encountered**| Technical or logical blockers. | `risk_flag` | Extended |
| **worker_role** | Role assumed (Researcher/Coder). | `actor` | Extended |

---

## 3. Aggregation Threshold (Merge vs. Split)

### 3.1 Conditions for MERGE (Compression)
Multiple signals should be aggregated into one candidate if:
- **Same Intent:** All residues belong to the same high-level task (e.g., "Designing Gates").
- **Sequential Maturation:** A series of steps lead to one final pattern (e.g., Round 001 -> 002 -> 003).
- **Redundant Reinforcement:** Multiple files confirm the same "Reuse Hint."
- **Review Efficiency:** Splitting would cause fatigue without adding distinct resolution.

### 3.2 Conditions for SPLIT (Atomicity)
Residues MUST be split into separate candidates if:
- **Layer Conflict:** One is a `Philosophy` (law) and another is `Implementation` (mechanical).
- **Nature Conflict:** One is a `Risk Memory` (danger) and another is a `Promotion Candidate` (new rule).
- **Source Conflict:** Provenance leads to two unrelated interaction contexts.
- **Sovereignty Requirement:** One item requires a strict Human Lock while the other is a low-risk tactical hint.
- **Contradiction:** New residue contradicts an existing signal in the same session.

---

## 4. Aggregated Event Candidate Shape
*Note: This is a candidate structure for transport, not a fixed schema.*

```text
aggregated_event_candidate:
  source_session: (Link to ID)
  domain_event_summary: (Intent-based summary of the entire session)
  included_residues: [List of raw atoms]
  primary_residue_type: (The most significant type)
  secondary_residue_types: [List of other types]
  layer_candidate: (Unified layer or multi-layer list)
  provenance_anchors: [List of specific file/turn links]
  novelty_reason: (Why the session as a whole adds resolution)
  aggregation_reason: (Why these were merged)
  split_required: (Boolean - did we choose NOT to merge something?)
  human_lock_required: (Boolean - does the aggregated whole need approval?)
  do_not_promote_as: (Unified constraints)
```

---

## 5. Round 005 Re-application (Aggregation Test)

| Case ID | Original Count | Aggregation Possible | Reason | Final Count |
| :--- | :--- | :--- | :--- | :--- |
| **Rounds 001-004** | 5 | **YES** | Sequential maturation of one meta-research task (Gate Design). | 1 |
| **Context/Terminology** | 2 | **NO** | Different Nature: Correction vs. Philosophy. Requires separate review. | 2 |
| **MCP/ASSETS/Lens** | 3 | **NO** | Different Layers: Tool (Future) vs. Risk (Memory) vs. Method (Seed). | 3 |

**Result:** Original 10 candidates compressed to 6. This significantly reduces human review fatigue while preserving high-resolution atomicity for critical corrections and methodology seeds.

---

## 6. Field Promotion Review (MVCC v2)

| Field | Previous Status | New Recommendation | Reason |
| :--- | :--- | :--- | :--- |
| **novelty_reason** | Extended | **Minimum** | Essential for the Novelty Gate to prevent noise. |
| **human_lock_required**| Extended | **Minimum** | Absolute necessity for Pillar 5 (Sovereignty). |
| **do_not_promote_as** | Extended | **Minimum** | Vital for the "Lowering" safety protocol. |
| **recommended_next_state**| Extended | **Aggregation Only** | AI's guess is less important than the summary/layer. |

---

## 7. Risks
- **Over-aggregation:** Merging a critical "Risk" into a "Hint," causing the user to miss the danger.
- **False Unity:** Forcing a single summary on a session that actually had two unrelated breakthroughs.
- **Provenance Loss:** If `provenance_anchors` becomes a long list, the specific link between a "Fact" and its "Source" might blur.
- **Layer Mixing:** Aggregating residues from different layers makes the candidate difficult to position.

## 8. Recommended Next Loop
- **Round 007: Manual Aggregated Event Dry-run:** Test the new "Aggregated Shape" with the compressed Case 1 (Rounds 001-004).
- **Round 007: CLI Interaction Trace v0.1 Specification:** Detailed spec of how the CLI should log `decision_points`.
- **Round 007: Human Review Fatigue Threshold:** Quantifying the "Review Queue" limit.

## 9. Closeout
```text
This report is criteria-only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, MCP prototype, reingestion implementation, UI, or JSON schema was created.
All trace fields, aggregation thresholds, and event candidate shapes remain provisional thought assets.
```
