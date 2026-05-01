# External Thought Asset Research Round 002 Plan
# Topic: Residue Reingestion without Noise

## 0. Research-only Declaration
- **Mode:** Read-only research loop.
- **Scope:** Space reference only; no implementation or modification of existing files.
- **Status:** Planning phase for next research cycle. No baseline promotion.

## 1. Why Round 002
Round 001 identified that external tools focus on "Recall" (Human recovery), while our space focuses on "Resolution" (Space density). To achieve higher resolution, we need Pillar 4 (Recursive Observation), but we must avoid the "Total Recall" trap (collecting everything) which leads to noise. We must solve the "Noise vs. Residue" problem before building tool adapters like MCP.

## 2. Core Problem
How do we turn a CLI/Agent interaction into a Stage 0 Event?
- **The Question:** What counts as a *valuable residue* versus what is just *interaction noise*?
- **The Goal:** Define criteria for extracting `risk_memory`, `reuse_hint`, `pattern_candidate`, and `hold_signal` from raw session logs.

## 3. User-Space Criteria
- **Layer-Awareness:** Does the residue belong to a specific layer (e.g., governance vs. logic)?
- **Provenance:** Can the reingested event trace back to the exact session and prompt?
- **Stratification:** Does the reingestion add a new layer of meaning or just duplicate old data?
- **Human Lock:** How is the AI-proposed residue presented to the user for "Locking" (promotion to canonical)?

## 4. External Research Targets
1. **Event Sourcing Patterns:** Investigate how append-only logs use "Event Reduction" and "Snapshots" to manage state growth.
2. **Observability (OpenTelemetry):** Look for "Sampling" and "Signal-to-Noise" techniques in high-volume trace/log environments.
3. **Agent Memory Models (Mem0, Letta, Zep):** Specifically, how they decide which "Facts" to extract from a conversation and how they handle "Contradictions" (New layer vs. Replacement).
4. **Knowledge Curation (Evergreen/Atomic Notes):** Study how raw information is "lowered" into distilled, atomic assets.

## 5. Comparison Questions (The Lens)
- **What counts as an event?** (Log vs. Fact vs. State Change)
- **What gets reduced?** (Filtering techniques)
- **What gets promoted?** (Candidate -> Canonical criteria)
- **Who approves promotion?** (Human-in-the-loop patterns)
- **How is noise prevented?** (Automatic vs. Manual gates)
- **How is resolution increased?** (Does memory make the system "smarter" or just "fuller"?)

## 6. Expected Merge Candidate Types
- **Residue Filter:** A gate to catch session waste.
- **Event Reduction Gate:** A rule-based system to consolidate small events.
- **Promotion Candidate:** A structure for AI to propose "Lock" items to the user.
- **Contradiction Note:** A layer for recording when new observations conflict with old ones.
- **Hold Signal:** A marker to pause reingestion when a layer conflict is detected.

## 7. Do Not Do
- Do not implement any code.
- Do not create schemas or database tables.
- Do not modify `CONSTITUTION.md` or any baseline.
- Do not let the AI self-lock facts during research.
- Do not treat "Total Capture" as a valid memory strategy.

## 8. Output Format for Actual Round 002
The next loop should produce:
1. **Residue Extraction Criteria:** A set of questions/rules to identify valuable interaction residue.
2. **Reingestion Flowchart (Conceptual):** From raw log to Stage 0 Event.
3. **Noise Reduction Matrix:** Common noise types and their prevention strategies.
4. **Human-Lock Checkpoint Design:** How the AI should present reingest candidates.
