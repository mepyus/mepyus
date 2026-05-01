# External Thought Asset Research Round 005
# Topic: Manual Stage 0 Event Dry-run Batch

## 0. Dry-run Declaration
- **Mode:** Read-only / No implementation.
- **Scope:** Space reference only; no modification of source-space documents.
- **Status:** Validation of the Round 004 contract candidates.
- **Authority:** All dry-run event candidates remain provisional and were not registered into the space.
- **Date:** 2026-04-26

## 1. Why Round 005
Round 004 proposed a "Minimum Viable Candidate Contract" (MVCC) for reingesting CLI residues. However, a contract's adequacy can only be tested against real data. Round 005 applies this contract to 10 actual research sessions to verify if the fields capture the intended "Resolution" and if the gates effectively filter out "Noise." This batch test is the final check before we define thresholds for human review fatigue.

## 2. Selected Cases
1. **Round 001 Execution:** High-level research on external tools.
2. **Round 001 Review:** The "Layer Reading Review" that established lowering principles.
3. **Round 002 Execution:** Research on residue classification.
4. **Round 003 Execution:** Design of the 8 reingestion gates.
5. **Round 004 Execution:** Definition of the candidate contract.
6. **Lowering Case (Context Injection):** Correcting over-promotion of a candidate.
7. **Terminology Case (Sovereignty):** Clarifying human vs. AI roles.
8. **Lowering Case (MCP):** Moving a tool connector to future-option.
9. **Mismatch Case (ASSETS.md):** The critical discovery of layer/lens mismatch.
10. **Seed Case (Lens-Based Reading):** Establishing the new methodology.

---

## 3. Manual Dry-run Results

### Case 1: Round 001 Execution
- **case_id:** dry_run_001
- **source_interaction:** research_session_20260426_01
- **source_file:** `docs/reports/external_thought_asset_research_round_001.md`
- **domain_event_summary:** Researched external AI memory/workspace tools and mapped them to the user's cosmology.
- **residue_type:** `interaction_trace` / `pattern_candidate`
- **layer_candidate:** `external_comparison`
- **provenance_anchor:** `docs/reports/external_thought_asset_research_round_001.md`
- **novelty_reason:** Established the "Resolution vs. Recall" differentiator.
- **risk_flag:** `technical_log_flooding` (if not filtered)
- **reuse_hint:** `not_needed_in_this_case`
- **pattern_candidate:** AI as Space Builder.
- **human_lock_required:** `true`
- **recommended_next_state:** `residue`
- **do_not_promote_as:** `baseline`
- **gate_results:**
  - tail_based_sampling: `keep_as_candidate`
  - domain_event_gate: `domain_event_candidate`
  - novelty_qualified_gate: `new_signal`
  - provenance_anchor_gate: `anchored_candidate`
  - layer_relevance_gate: `layer_identified`

### Case 2: Round 001 Review (Lowering Principles)
- **case_id:** dry_run_002
- **source_interaction:** review_session_20260426_02
- **source_file:** `docs/reports/external_thought_asset_round_001_layer_reading_review_v0.md`
- **domain_event_summary:** Established the "Lowering" protocol for over-promoted candidates.
- **residue_type:** `promotion_candidate` / `rule`
- **layer_candidate:** `operation`
- **provenance_anchor:** `docs/reports/external_thought_asset_round_001_layer_reading_review_v0.md`
- **novelty_reason:** Defines how to handle layer mismatches in future rounds.
- **risk_flag:** `none`
- **reuse_hint:** Always check the layer before core-fit placement.
- **pattern_candidate:** Layer-Aware Placement.
- **human_lock_required:** `true`
- **recommended_next_state:** `human_review_candidate`
- **do_not_promote_as:** `implementation_spec`
- **gate_results:**
  - human_sovereign_lock_gate: `human_review_candidate`

### Case 3: Round 002 Execution (Residue Class)
- **case_id:** dry_run_003
- **source_interaction:** research_session_20260426_03
- **source_file:** `docs/reports/external_thought_asset_research_round_002_residue_reingestion_v0.md`
- **domain_event_summary:** Defined 10 residue types and the "Tail-based sampling" principle.
- **residue_type:** `pattern_candidate`
- **layer_candidate:** `operation / criteria`
- **provenance_anchor:** `docs/reports/external_thought_asset_research_round_002_residue_reingestion_v0.md`
- **novelty_reason:** Distinguishes "Residue" from "Noise" based on high-resolution intent.
- **risk_flag:** `none`
- **reuse_hint:** Evaluate residue at session end (tail-sampling).
- **pattern_candidate:** Intent-based filtering.
- **human_lock_required:** `true`
- **recommended_next_state:** `human_review_candidate`
- **do_not_promote_as:** `json_schema`
- **gate_results:**
  - domain_event_gate: `domain_event_candidate`
  - novelty_qualified_gate: `new_signal`

### Case 4: Round 003 Execution (Gates)
- **case_id:** dry_run_004
- **source_interaction:** design_session_20260426_04
- **source_file:** `docs/reports/external_thought_asset_research_round_003_reingestion_gate_design_v0.md`
- **domain_event_summary:** Designed 8 provisional gates for filtering residues.
- **residue_type:** `pattern_candidate`
- **layer_candidate:** `operation / criteria`
- **provenance_anchor:** `docs/reports/external_thought_asset_research_round_003_reingestion_gate_design_v0.md`
- **novelty_reason:** Provides the "Filtration Logic" for the reingestion pipeline.
- **risk_flag:** `human_review_fatigue`
- **reuse_hint:** Use multi-layered sieves for high signal.
- **pattern_candidate:** Sovereign Filtration.
- **human_lock_required:** `true`
- **recommended_next_state:** `human_review_candidate`
- **do_not_promote_as:** `automation_code`
- **gate_results:**
  - risk_quarantine_gate: `hold_signal` (on fatigue risk)

### Case 5: Round 004 Execution (Contract)
- **case_id:** dry_run_005
- **source_interaction:** design_session_20260426_05
- **source_file:** `docs/reports/external_thought_asset_research_round_004_stage_0_event_candidate_contract_v0.md`
- **domain_event_summary:** Defined the Minimum Viable Candidate Contract (MVCC) fields.
- **residue_type:** `pattern_candidate`
- **layer_candidate:** `operation / contract`
- **provenance_anchor:** `docs/reports/external_thought_asset_research_round_004_stage_0_event_candidate_contract_v0.md`
- **novelty_reason:** Established the "Information Unit" for transport.
- **risk_flag:** `schema_first_suffocation`
- **reuse_hint:** Split minimum vs extended fields to avoid hallucination.
- **pattern_candidate:** Contract Lowering.
- **human_lock_required:** `true`
- **recommended_next_state:** `human_review_candidate`
- **do_not_promote_as:** `fixed_schema`
- **gate_results:**
  - novelty_qualified_gate: `reinforces_existing_signal`

### Case 6: Context Injection Correction
- **case_id:** dry_run_006
- **source_interaction:** correction_instruction_01
- **source_file:** `docs/reports/external_thought_asset_round_001_layer_reading_review_v0.md`
- **domain_event_summary:** Lowered Context Injection to conditional-gated to mitigate hallucination risk.
- **residue_type:** `risk_memory`
- **layer_candidate:** `risk_memory / philosophy`
- **provenance_anchor:** `user_instruction_01` (Interaction trace)
- **novelty_reason:** Direct user-correction of a dangerous assistant assumption.
- **risk_flag:** `context_hallucination`
- **reuse_hint:** `not_needed_in_this_case`
- **pattern_candidate:** Layer-check gating.
- **human_lock_required:** `true`
- **recommended_next_state:** `risk_memory`
- **do_not_promote_as:** `absolute_exclusion`
- **gate_results:**
  - risk_quarantine_gate: `risk_memory`
  - human_sovereign_lock_gate: `human_review_candidate`

### Case 7: Sovereignty Terminology Correction
- **case_id:** dry_run_007
- **source_interaction:** correction_instruction_02
- **source_file:** `docs/reports/external_thought_asset_round_001_layer_reading_review_v0.md`
- **domain_event_summary:** Corrected terminology: Human is the only Sovereign Observer; AI is the Worker-Observer.
- **residue_type:** `promotion_candidate` / `rule`
- **layer_candidate:** `philosophy`
- **provenance_anchor:** `user_instruction_02`
- **novelty_reason:** Protects the Pillar 5 principle from linguistic drift.
- **risk_flag:** `none`
- **reuse_hint:** AI proposes; Human locks.
- **pattern_candidate:** Sovereign Role Division.
- **human_lock_required:** `true`
- **recommended_next_state:** `human_review_candidate`
- **do_not_promote_as:** `implementation_detail`
- **gate_results:**
  - layer_relevance_gate: `layer_identified` (Philosophy)

### Case 8: MCP Adapter Lowering
- **case_id:** dry_run_008
- **source_interaction:** review_session_20260426_02
- **source_file:** `docs/reports/external_thought_asset_round_001_layer_reading_review_v0.md`
- **domain_event_summary:** Positioned MCP as a "Lens Tool / Future Option" rather than core logic.
- **residue_type:** `quarantine_asset` / `future_option`
- **layer_candidate:** `external_comparison / future_option`
- **provenance_anchor:** `docs/reports/external_thought_asset_round_001_layer_reading_review_v0.md`
- **novelty_reason:** Prevents tool standards from overriding space philosophy.
- **risk_flag:** `tool_dependency`
- **reuse_hint:** `not_needed_in_this_case`
- **pattern_candidate:** `not_needed_in_this_case`
- **human_lock_required:** `false`
- **recommended_next_state:** `future_option`
- **do_not_promote_as:** `baseline`
- **gate_results:**
  - risk_quarantine_gate: `quarantine_asset`

### Case 9: ASSETS.md Mismatch Case
- **case_id:** dry_run_009
- **source_interaction:** historical_mismatch_analysis
- **source_file:** `space_cli_pipeline/cases/assets_md_layer_lens_mismatch_case_v0.md`
- **domain_event_summary:** Identified that internally coherent designs can fail if placed on the wrong layer.
- **residue_type:** `risk_memory` / `pattern_candidate`
- **layer_candidate:** `philosophy / risk_memory`
- **provenance_anchor:** `historical_session_logs`
- **novelty_reason:** The foundational discovery of "Layer-Aware Reading."
- **risk_flag:** `premature_coherence`
- **reuse_hint:** Reread through multiple lenses before adopting.
- **pattern_candidate:** Layer-First vs. Coherence-First.
- **human_lock_required:** `true`
- **recommended_next_state:** `risk_memory / residue`
- **do_not_promote_as:** `registry_mandate`
- **gate_results:**
  - tail_based_sampling: `keep_as_candidate`
  - novelty_qualified_gate: `contradiction_signal` (to previous logic)

### Case 10: Lens-Based Reading Seed
- **case_id:** dry_run_010
- **source_interaction:** historical_seed_creation
- **source_file:** `docs/reports/lens_based_asset_reading_note_v0.md`
- **domain_event_summary:** Established the methodology for multi-lens asset evaluation.
- **residue_type:** `promotion_candidate` / `rule`
- **layer_candidate:** `operation`
- **provenance_anchor:** `docs/reports/lens_based_asset_reading_note_v0.md`
- **novelty_reason:** Formalizes the user's "Reverse Ontology" and "Stratification" philosophy into a reading procedure.
- **risk_flag:** `none`
- **reuse_hint:** Use the 10-lens list for evaluation.
- **pattern_candidate:** Multi-Lens Reading.
- **human_lock_required:** `true`
- **recommended_next_state:** `human_review_candidate`
- **do_not_promote_as:** `automatic_classifier`
- **gate_results:**
  - human_sovereign_lock_gate: `human_review_candidate`

---

## 4. Field Adequacy Review
The "Minimum Viable Candidate Contract" (MVCC) fields were sufficient for all 10 cases. 
- **source_interaction** and **provenance_anchor** are critical for tracing "Why" a fact was proposed.
- **domain_event_summary** is the most valuable field for "Resolution," as it strips away the mechanical log and exposes the intent.
- **layer_candidate** is essential for preventing the "ASSETS.md" failure pattern.

## 5. Extended Field Pressure
There is strong pressure to promote **novelty_reason** and **human_lock_required** to the minimum set.
- Without **novelty_reason**, it is difficult to justify why a candidate isn't just "Noise."
- Without **human_lock_required**, the AI cannot flag items for the "Sovereign Tray," risking auto-promotion or total stagnation.
- **do_not_promote_as** (Lowering constraint) was used in 9/10 cases, suggesting it is a vital safety field to prevent over-structuring.

## 6. Gate Adequacy Review
- **Tail-Based Sampling Gate:** Very useful for Case 1 (filtering a long research session into a single summary).
- **Domain Event Gate:** Success in converting technical actions (`write_file`) into system events (`Designed Gates`).
- **Novelty-Qualified Gate:** Crucial for Case 5 (recognizing reinforcement vs. new signals).
- **Risk / Quarantine Gate:** Essential for Case 6 and 8.

## 7. Noise / Fatigue Findings
- **Noise:** Trivial successful commands (e.g., `read_file`) were correctly discarded by the Domain Event Gate.
- **Fatigue Risk:** If every "Round" results in 5+ "Candidates," the human review queue will grow too fast. 
- **Finding:** We need a **"Aggregation Threshold"**—multiple residues from one session should probably be compressed into a single "Stage 0 Event Candidate" before reaching the user.

## 8. Revised Contract Recommendation

- **keep_minimum:** `source_interaction`, `domain_event_summary`, `residue_type`, `layer_candidate`, `provenance_anchor`.
- **consider_promoting_to_minimum:** `novelty_reason`, `human_lock_required`, `do_not_promote_as`.
- **keep_extended:** `risk_flag`, `reuse_hint`, `pattern_candidate`, `recommended_next_state`.
- **remove_or_delay:** `event_candidate_id` (Redundant if session ID exists), `actor` (Usually implicit).

## 9. Recommended Next Loop
- **Round 006: CLI Interaction Trace Minimum Contract:** Defining what the CLI must "record" during the session (e.g., specific user quotes or decision points) to auto-fill the MVCC fields at the end.
- **Round 006: Stage 0 Candidate Threshold Rules:** Quantifying "Novelty" and "Risk" to automate the discard of noise.
- **Round 006: Human Review Fatigue Threshold:** Designing the UI-less "Sovereign Tray" management logic.

## 10. Closeout
This report is dry-run only.
No source-space document was modified.
No baseline, schema, registry, classifier, dispatcher, controller, automation, MCP prototype, reingestion implementation, UI, or JSON schema was created.
All dry-run event candidates remain provisional and were not registered into the space.
