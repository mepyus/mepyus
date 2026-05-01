# Session-level Observation Aggregation Guideline v0
# Topic: Reducing Observer Fatigue via Session-level Grouping

## 0. Declaration
- **Mode:** Guideline synthesis only.
- **Scope:** Read-only / No source-space modification.
- **Status:** Strategic reference material only; no implementation or internal design.
- **Authority:** All grouping rules remain provisional thought assets.
- **Date:** 2026-04-26

## 1. Why This Guideline Exists
Individual CLI interactions can produce dozens of "Observation Records." Surfacing all of them to the human observer leads to severe review fatigue. This guideline defines the criteria for aggregating session-specific residues into a single high-resolution "Session Summary Candidate," allowing the user to triage at the session level rather than at the individual interaction level, while preserving full provenance access.

## 2. Aggregation Logic Principles
1. **Primary Event vs. Secondary Residue:** Group residues by intent; surface the primary event (the "Aha! moment") and collapse secondary evidence.
2. **Review-Safety:** Never aggregate `HUMAN_REVIEW_REQUIRED` items into a summary that might be auto-dismissed.
3. **Lossless Collapse:** Collapsing evidence is a UI/View decision; the underlying `Observation Record` must remain accessible via provenance links.
4. **Sovereignty Protection:** Aggregation should never hide a "Locking" decision; the human must see critical proposals clearly.

## 3. When to Aggregate (The MERGE Condition)
Multiple records should be grouped if:
- **Same Intent:** All residues serve the same session goal (e.g., "Refactoring login module").
- **Sequential Maturation:** A chain of edits leading to one final state.
- **Redundant Reinforcement:** Multiple files confirm the same "Reuse Hint."
- **Review Efficiency:** Splitting would cause fatigue without adding distinct layer-alignment clarity.

## 4. When to Keep Atomic (The SPLIT Condition)
Residues MUST remain split if:
- **Layer Conflict:** One is `Philosophy` (law) and another is `Implementation` (mechanical).
- **Nature Conflict:** One is a `Risk Memory` (warning) and another is a `Promotion Candidate` (new rule).
- **Sovereignty Requirement:** One item requires a Human Lock while others are low-risk tactical hints.
- **Contradiction:** New residue contradicts an existing signal in the same session.

## 5. Primary Event / Secondary Residue Definition
- **Primary Event:** The high-level intent-based system event (e.g., `Button Label Refactored`). This surfaces as the "Subject" of the session.
- **Secondary Residue:** The "Failure Trace," logs, diffs, and mechanical steps. These are preserved for provenance but collapsed by default.

## 6. Session Summary Candidate Structure
*Note: This is a proposed candidate structure for transport/review, not a finalized schema.*

```text
session_summary_candidate:
  session_id: 
  primary_event_summary: (The 'Aha!' moment)
  records_count: (Total interactions)
  validation_required_count: 
  human_review_required_count: 
  risk_highlights: [List of high-impact risks]
  representative_source_ref: (Primary anchor)
  evidence_refs: [List of collapsed source anchors]
  next_packet_candidate: 
  human_lock_required: (True if any constituent record requires review)
```

## 7. Operational Guidelines for Worker
- **Do not group across intents:** If a session changes from "Research" to "Implementation," start a new aggregation candidate.
- **Prioritize the Review-Flag:** If a single record within an aggregated candidate triggers `HUMAN_REVIEW_REQUIRED`, the entire summary candidate must inherit that status.
- **Transparency:** The summary candidate must always provide a way to "Expand All" to see individual `Observation Records`.

## 8. Risks of Aggregation
- **False Convergence:** Treating two separate issues as one root cause, leading to incorrect validation.
- **Provenance Decay:** Summarizing 50 residues into one line loses the specific file-line context.
- **Alert Blindness:** If we group everything, we risk hiding a subtle "Risk Memory" behind a "Successful Completion" summary.

## 9. Remaining Ambiguities
- **Dynamic Thresholding:** How do we decide when a session is "too large" and must be split before session-end?
- **Nested Evidence Access:** How do we expose the collapsed evidence list in a CLI-only context (e.g., `show <session_id>`)?
- **Identity:** Should the `Session Summary` be a unique ID or a derivative of the interaction?

## 10. Closeout
This guideline is strategy-only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, verification UI, drill-down design, evidence schema, event grouping design, suppression logic, status schema, dashboard, UI, reingestion design, JSON schema, CLI trace contract, aggregation threshold, or agent architecture was created.
All findings remain provisional strategic reference material.
