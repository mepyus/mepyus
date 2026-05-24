# Package T Active Bundle Candidate — 2026-05-09

## 0. Status

- candidate only
- Package T preparation only
- active-bundle trial setup only
- not baseline
- not schema
- not registry
- not automation
- not final routing rule
- not replacement for user judgment

## 1. Purpose

This file exists to define the exact parameters for the first manual active-bundle trial (Package T). It tests whether a worker can recover a high-quality judgment capsule by reading a specifically curated small set of files rather than performing a broad repository search.

The trial aims to:
- verify if small active bundles can effectively reduce token cost while preserving decision quality
- ensure that the selected files contain enough interlinked context (parent/neighbor) to be useful
- test the conceptual maturation chain (Trace -> Capsule) in a controlled environment
- provide a clear mission for Gemini without requiring Codex to perform the actual synthesis

## 2. Trial Question

Can a worker recover a useful judgment about the current result-oriented operating stack by reading only a 3-file active bundle?

## 3. Selected 3-File Active Bundle

The following three files form the "Result-Oriented Core Bundle" for this trial.

### 1. `app/work/space-skill-sandbox/outputs/result_oriented_operating_stack_closeout_20260508_v0.md`
- **role_in_bundle:** Core Operating Closeout
- **why_included:** It defines the current role split, the final flow candidate, and the core status of the stack.
- **what_it_should_help_recover:** The overall objective and current "live candidate" state of the VectorFL system.
- **risk_if_omitted:** The worker may lose the big-picture context of why the stack was created.

### 2. `app/work/space-skill-sandbox/outputs/result_usefulness_gate_v0_candidate_20260508.md`
- **role_in_bundle:** Recovery Filter
- **why_included:** It defines the "Result Usefulness Gate" and the criteria for deciding whether a result is worth recovering.
- **what_it_should_help_recover:** The principle that "Space recovers usable judgment, not just results that followed principles."
- **risk_if_omitted:** The worker might default to "procedural compliance" rather than "practical utility" judgment.

### 3. `app/work/space-skill-sandbox/outputs/mission_packet_result_contract_v0_candidate_20260508.md`
- **role_in_bundle:** Input Contract
- **why_included:** It defines the shift from "Read and summarize" to "Synthesize to enable decision."
- **what_it_should_help_recover:** The specific behavior changes required for future mission packets.
- **risk_if_omitted:** The worker may fail to identify the concrete shift in instruction design.

## 4. Excluded Context

The following files are intentionally excluded to test the limits of the 3-file bundle:

- `current_anchor_map_candidate_20260509_v0.md`: Excluded to see if the worker can find its way without the primary map.
- `judgment_provenance_record_template_and_trial_20260509_v0.md`: Excluded to see if provenance discipline is maintained without the template.
- `tool_profile_record_candidate_20260509_v0.md`: Excluded to test if tool-specific roles can be inferred from the closeout.
- `policy_mutation_record_candidate_20260509_v0.md`: Excluded to see if the worker can identify a "need for change" without the mutation log.
- `judgment_capsule_reentry_surface_candidate_20260509_v0.md`: Excluded to ensure the worker drafts a *new* capsule rather than copying the sample.
- `RUNLOG.jsonl`: Excluded to test if semantic docs are sufficient without process traces.
- `user_facing_routing_card_v0_candidate_20260508.md`: Excluded to focus on the internal operating logic rather than user surface.

## 5. Expected Useful Result for Future Gemini Trial

The future Gemini trial must produce a **Candidate Judgment Capsule** that answers:

“What does the result-oriented operating stack require future workers to change in their behavior?”

The output must include:
- **one recovered judgment:** A single, atomic, reusable decision.
- **provenance note:** Using labels like `OBSERVED_FILE_EVIDENCE` or `GEMINI_SYNTHESIS`.
- **parent context:** Identifying the Lineage/Package.
- **neighbor context:** Identifying which files should be read alongside this judgment.
- **use_when:** Practical application condition.
- **do_not_use_when:** Clear boundary/risk condition.
- **return_placement_candidate:** Where this judgment should live in the Space.
- **watch:** Immediate risk or uncertainty.

## 6. Success Criteria

The trial succeeds if Gemini:
- identifies the shift from "safe output" to "decision-enabling judgment"
- correctly links the "Expected Useful Result" section in packets to the "Result Usefulness Gate" in recovery
- maintains "candidate-only" framing throughout
- identifies at least one "missing context" item (e.g., "Missing user routing card context")
- produces a capsule that is more useful than a simple summary

## 7. Failure Criteria

The trial fails if Gemini:
- treats any of the 3 files as "baseline" or "standard"
- simply summarizes the files without extracting a reusable judgment
- fails to identify that the result must support a user decision
- claims to understand the "whole repo" based on these 3 files
- requires a broad repository search to answer the question

## 8. Trial Prompt for Gemini

```markdown
# GEMINI TASK — Package T: Active Bundle Trial 004

## 0. Role
You are performing a Gemini-heavy synthesis trial over a small active bundle.

## 1. Task
Read only the following 3 files:
1. app/work/space-skill-sandbox/outputs/result_oriented_operating_stack_closeout_20260508_v0.md
2. app/work/space-skill-sandbox/outputs/result_usefulness_gate_v0_candidate_20260508.md
3. app/work/space-skill-sandbox/outputs/mission_packet_result_contract_v0_candidate_20260508.md

## 2. Objective
Recover a useful judgment answering:
“What does the result-oriented operating stack require future workers to change in their behavior?”

## 3. Required Output
Produce exactly one Judgment Capsule following this shape:
- capsule_id: [CANDIDATE_ID]
- title:
- judgment: [The atomic reusable decision]
- layer:
- source_trace_or_package: [Cite the 3 files]
- provenance: [Label the source of your claims]
- parent_context:
- neighbor_context:
- use_when:
- do_not_use_when:
- return_placement:
- watch:
- missing_context: [What was not in the 3 files but felt needed?]

## 4. Constraints
- Do not search the repo.
- Do not read other files.
- Do not promote anything to baseline.
- If you infer anything not in the 3 files, mark it as GEMINI_SYNTHESIS.
```

## 9. Relation to Existing Setup

- **current_anchor_map:** This bundle is a subset of the "Result-Oriented Core Bundle" (A01, A03, A04).
- **judgment_provenance_record:** The trial requires explicit provenance labeling.
- **judgment_capsule_reentry_surface:** The trial produces a "Judgment Capsule" as its output unit.
- **Space Maturation Synthesis Audit 001:** This trial tests the "Lineage -> Future Active Bundle" link identified as the weakest in the audit.

## 10. Watch Items

- **Context Loss:** 3 files may be too thin for a high-level operating stack judgment.
- **Over-Abstraction:** Gemini might ignore the concrete file details in favor of general AI reasoning.
- **False Precision:** The "capsule" format might look more mature than the 3-file evidence supports.
- **Navigation Rot:** Gemini might identify "missing context" that is actually in the bundle but overlooked.

## 11. Final Note

This is an active-bundle trial setup only. It should be tested once before creating more active bundles. It should not be treated as retrieval policy or routing authority.

## 12. Restrictions

No other files were modified, no RUNLOG updates were made, and no implementation was attempted.
