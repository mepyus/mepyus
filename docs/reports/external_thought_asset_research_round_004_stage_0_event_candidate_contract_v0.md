# External Thought Asset Research Round 004
# Topic: Stage 0 Event Candidate Contract

## 0. Research / Contract-Candidate Mode Declaration
- **Mode:** Read-only contract-candidate report.
- **Scope:** Space reference only; no modification of source-space documents.
- **Status:** No implementation, schema lock, or baseline promotion occurred.
- **Authority:** All contract fields, gate mappings, and dry-run examples remain provisional thought assets.
- **Date:** 2026-04-26

## 1. Why Round 004
Round 003 established the functional logic of the **Reingestion Gates**. However, logic requires a medium of transport. To perform a manual dry-run and eventually automate reingestion, we need a **Stage 0 Event Candidate Contract**. 

This contract defines the "Minimum Information Unit" that the CLI must prepare at the end of a session to be evaluated by the gates. By keeping this a "Candidate Contract" rather than a fixed JSON schema, we avoid **Schema-First Suffocation** and allow the information requirements to mature through manual dry-runs.

## 2. Stage 0 Event Candidate Definition

**What it is:**
- A high-level, intent-based domain event candidate produced at the end of a CLI/Assistant interaction.
- A bundle of residue, metadata, and provenance intended for space resolution enhancement.
- A "Candidate" that remains provisional until it passes all gates and (if necessary) receives a Human Sovereign Lock.

**What it is NOT:**
- `raw_log`: It is not a sequential list of shell commands or file reads.
- `technical_log`: It is not a record of mechanical success/failure.
- `interaction_trace`: It is not a full play-by-play of the session.
- `locked_fact`: It is not a truth until the Human Sovereign turns the key.

## 3. Minimum Viable Candidate Contract (MVCC)
These are the fields absolutely required to satisfy the core pillars of **Provenance**, **Layering**, and **Sovereignty**.

1.  **source_interaction:** (Reference to the session/prompt)
2.  **domain_event_summary:** (The intent-based "What happened")
3.  **residue_type:** (Classification: hint, risk, pattern, etc.)
4.  **layer_candidate:** (Contextual axis proposal)
5.  **provenance_anchor:** (Link back to the mechanical source)
6.  **novelty_reason:** (Why this is resolution, not noise)
7.  **human_lock_required:** (Boolean: Does this target the baseline?)
8.  **do_not_promote_as:** (Lowering requirement/Constraint)

## 4. Extended Candidate Fields
Fields that provide higher resolution but carry a higher risk of **Field Hallucination** if forced prematurely.

1.  **event_candidate_id:** (Temporary ID for candidate tracking)
2.  **actor:** (Who performed the action)
3.  **created_at:** (Timestamp of the event)
4.  **reuse_hint:** (Specific heuristic for future turns)
5.  **pattern_candidate:** (Hypothesis of a repeating structure)
6.  **risk_flag:** (Type/Severity of identified risk)
7.  **recommended_next_state:** (AI's proposal for the gate outcome)

---

## 5. Field Candidate Details

| Field Name | Purpose | Risk if Over-specified | Required/Optional |
| :--- | :--- | :--- | :--- |
| **source_interaction** | Ties residue to a specific session. | AI might invent a fake session ID. | **Required** |
| **domain_event_summary** | Converts logs to system events. | AI over-summarizes, losing critical nuance. | **Required** |
| **residue_type** | Categorizes the nature of knowledge. | Rigid enums might miss novel residue types. | **Required** |
| **layer_candidate** | Identifies the contextual axis. | AI guesses layers it doesn't understand. | **Required** |
| **provenance_anchor** | Ensures traceability (Pillar 3). | Path bloat or broken reference links. | **Required** |
| **novelty_reason** | Justifies space resolution gain. | AI produces "filler" reasons for noise. | **Required** |
| **human_lock_required** | Protects Sovereignty (Pillar 5). | AI might default to 'false' to bypass review. | **Required** |
| **do_not_promote_as** | Prevents over-structuring. | AI misses subtle "lowering" requirements. | **Required** |
| **risk_flag** | Flags dangers for future turns. | AI becomes overly "paranoid" or misses signals. | Optional |
| **reuse_hint** | Provides tactical "Skills." | Outdated or turn-specific heuristics. | Optional |

---

## 6. Gate-to-Field Mapping

| Gate (from Round 003) | Required Field Candidate | Why | Risk if Absent |
| :--- | :--- | :--- | :--- |
| **Tail-Based Sampling Gate** | `domain_event_summary` | Evaluates if the *outcome* has value. | Mechanical noise flooding the space. |
| **Domain Event Gate** | `domain_event_summary` | Checks if it's an intent or just a log. | Space becomes a graveyard of `git status`. |
| **Novelty-Qualified Gate** | `novelty_reason` | Ensures we are adding resolution. | Resolution-neutral volume bloat. |
| **Provenance-Anchor Gate** | `provenance_anchor` | Validates the "Pillar of Provenance." | Floating claims without evidence. |
| **Layer-Relevance Gate** | `layer_candidate` | Prevents cross-layer contamination. | Context hallucination in future turns. |
| **Risk / Quarantine Gate** | `risk_flag`, `do_not_promote_as` | Safeguards the space from over-structuring. | Premature baseline promotion. |
| **Human Sovereign Lock Gate** | `human_lock_required` | Flags the need for final authority. | AI self-locking its own proposals. |

---

## 7. Manual Dry-run Examples

### Example 1: Round 003 Results (Provisional Gates)
- **raw_trace_summary:** Assistant researched 5 external sources and proposed 8 gates for reingestion.
- **domain_event_summary:** Round 003 established provisional gates for filtering CLI interaction residue before Stage 0 reingestion.
- **residue_type:** `pattern_candidate`
- **layer_candidate:** `operation / criteria`
- **provenance_anchor:** `docs/reports/external_thought_asset_research_round_003_reingestion_gate_design_v0.md`
- **novelty_reason:** Moves from "What to store" to "How to decide," defining the filtration logic.
- **risk_flag:** `none`
- **human_lock_required:** `true` (Targets operational criteria)
- **recommended_next_state:** `human_review_candidate`
- **do_not_promote_as:** `implementation_spec`

### Example 2: Context Injection 하향 보정 (Lowering)
- **raw_trace_summary:** User corrected the placement of Context Injection from core-fit to conditional.
- **domain_event_summary:** Context Injection was lowered from core-fit to conditional-gated due to prompt stuffing and context hallucination risk.
- **residue_type:** `risk_memory`
- **layer_candidate:** `risk_memory / philosophy`
- **provenance_anchor:** `docs/reports/external_thought_asset_round_001_layer_reading_review_v0.md`
- **novelty_reason:** Records a specific failure case of "coherent design on the wrong layer."
- **risk_flag:** `context_hallucination`
- **human_lock_required:** `true` (Updates the placement baseline candidate)
- **recommended_next_state:** `residue / risk_memory`
- **do_not_promote_as:** `total_exclusion_signal`

---

## 8. Direct Risks

- **Schema-first suffocation:** Forcing a JSON structure now might prevent us from discovering a new field (e.g., `lens_used`) during manual dry-runs.
- **Field hallucination:** If we make `event_candidate_id` mandatory, the AI might invent IDs that don't match the space's actual event sequence.
- **Provenance decay:** If the `provenance_anchor` is just a filename without a line number or interaction context, the "Pillar" is weakened.
- **Technical log flooding:** AI might try to put the entire `git diff` into the `domain_event_summary`.
- **Human review fatigue:** If the `human_lock_required` flag is set to `true` for every minor residue, the user will eventually ignore the Sovereign Tray.

## 9. Open Questions
- Should `layer_candidate` be a fixed list (Enum) or an open-ended suggestion?
- How do we handle `provenance_anchor` when the source is a transient terminal output?
- Is `event_candidate_id` necessary if we have the `source_interaction` ID?
- How many manual dry-runs are required before the "Contract" can be hardened into a "Schema"?

## 10. Recommended Next Loop
- **Round 005: Manual Stage 0 Event Dry-run Batch:** Perform 5-10 manual conversions of recent sessions into these candidate fields to test for friction.
- **Round 005: Human Review Fatigue Threshold:** Research when to auto-archive candidates vs. when to demand a Human Lock.
- **Round 005: Weak Signal / Quarantine Handling:** How to store "low-resolution" residues for future re-evaluation.

## 11. Closeout
This report is contract-candidate only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, MCP prototype, reingestion implementation, UI, or JSON schema was created.
All contract fields, gate mappings, and dry-run examples remain provisional thought assets.
