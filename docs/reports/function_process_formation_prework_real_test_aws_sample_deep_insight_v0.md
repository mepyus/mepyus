# Function/Process Formation Prework Real Test — AWS sample-deep-insight v0

## 1. Status
**STATUS: FORMATION_PREWORK_REAL_TEST_COMPLETE**

## 2. Test target
- **Target Name:** AWS sample-deep-insight
- **Source:** `https://github.com/aws-samples/sample-deep-insight`
- **Candidate Type:** Repo / Architectural Reference

## 3. Why this target was suitable or unsuitable
- **Suitability:** **HIGH.** This repository provides a concrete implementation of "Harness-Orientation" through its Planner/Supervisor split and explicit Human-in-the-loop (HITL) gates. It allows us to test if our Formation Prework v1 can extract reusable "worker orchestration" patterns without adopting the specific AWS/Strands SDK technical stack.

## 4. Function Candidate Card
- **candidate_name:** AWS sample-deep-insight
- **candidate_type:** repo / architectural_reference / agent_workflow_reference
- **original_context:** A hierarchical multi-agent framework for data analysis (PDF, Excel, Code execution).
- **why_user_brought_it:** To compare its Planner/Supervisor/Agent split and HITL implementation with our internal role boundaries (User/Codex/Gemini).
- **possible_space_role:** operation_reference / planner_reference / supervisor_reference / HITL_reference
- **Resource_or_Tool_or_Both:** **Both.**
  - **Resource:** The documentation and architectural patterns.
  - **Tool:** The specialized agent functions (execution units).
- **possible_project_reading:** A map of how high-level "Planning" translates to "Execution" under a "Supervisor" harness.
- **related_line_axis_lens_camera:** Harness-Orientation, User as Judge, Plan before Execution.
- **potential_acceleration_value:** High potential for refining our "Codex (Designer) vs Gemini (Executor)" packet flow.
- **risks:** Architecture drift (copying AWS-specific logic), over-structuring simple tasks, and bypassing the local User gate for AWS "Coordinator" logic.
- **current_state:** candidate

## 5. Prior Record Retrieval
- **retrieval_scope_boundary:**
  - **purpose:** Contextualize AWS patterns within our role boundaries and previous "Tool as Affordance" work.
  - **include:** MCP real test (`run_231`), Space Roles Reference (`v0`), Harness-Orientation axis references.
  - **exclude:** historical repo crawls, AWS SDK documentation.
  - **stop_condition:** When the Planner/Supervisor roles are mapped to our Codex/Gemini roles.
  - **caution:** Do not treat AWS's "Coordinator" as a replacement for our "User-as-Judge" gate.
- **prior_records_used:** `docs/reports/function_process_formation_prework_real_test_mcp_v0.md`, `app/work/space-skill-sandbox/outputs/space_roles_reference_candidate_v0.md`, `app/work/space-skill-sandbox/outputs/line_axis_synthesis_report_candidate_v0.md`.
- **prior_records_not_used:** None.
- **why_retrieval_was_enough:** The Roles Reference provided the authority baseline, while the MCP test provided the Resource/Tool comparison lens.
- **what_remains_unclear:** The specific data-passing mechanism (Strands SDK) vs our file-based re-entry entries.

## 6. Process Asset Unit
- **trigger:** User instruction for a real test of Prework v1 on a second candidate.
- **user_intent:** Verify if Prework v1 can "form" a role for a structurally complex repository reference.
- **input_material:** AWS sample-deep-insight README and architecture overview.
- **roles_used:**
  - **User:** Approved the candidate and intent.
  - **Gemini:** Executed the bounded analysis and v1 application.
- **process_route:** Retrieval -> External Content Analysis -> Internal Comparison -> 5-part Unit Application.
- **evidence_collected:** The "Coordinator -> Planner -> Supervisor -> Agent" hierarchical split.
- **judgments_made:** AWS "Planner" maps to our "Codex Design" (A-layer); AWS "Supervisor" maps to our "Harness/Boundary" (B-layer); AWS "Agent" maps to "Gemini Execution."
- **mistake_memory:** None during this run.
- **watch_items:** "Supervisor" logic becoming an automated router rather than a structural harness.
- **candidate_signals:** **"Step-wise HITL"**—Moving from a single "Approval" to specific "Phase 1: Plan Review" and "Phase 2: Execution Result Review."
- **what_can_be_reused_later:** The "Planning vs Execution" phase distinction as a packet-design aid.
- **what_requires_user_judgment:** Whether to explicitly adopt a "Planner" phase in our worker-packet templates.

## 7. Reuse Hook
- **reusable_when:** Designing multi-step worker pipelines or "Supervisor" level harnesses.
- **related_keywords:** Planner, Supervisor, HITL, Multi-agent, Orchestration.
- **related_user_intents:** "Manage complex tasks," "Add a review gate," "Split design from action."
- **related_line_axis_lens_camera:** Harness-Orientation, Plan before Execution.
- **retrieve_before:** worker-supervisor design / HITL design / packet design / integration-engine design.
- **reuse_value:** Provides a mature vocabulary for "Phase-based" human-in-the-loop gates.
- **caution:** Reference only; no adoption of the technical coordinator logic.

## 8. User Decision Gate
- **User decision required before:** 
  - Adopting "Coordinator" or "Supervisor" naming.
  - Automating the transition from Planning to Execution.
  - Integrating any "Strands-like" SDK logic.
  - Changing the Codex/Gemini role definitions based on this reference.
- **Safe default:** `operation_reference` / `watch`

## 9. Formation Prework vs Reusable Setting check
- **Status:** **STILL IN FORMATION PREWORK.**
- **Why:** The architectural shapes are highly relevant but have not yet been "proven" through repeated reuse in our repository's local context. They are in the "Incubator" phase.
- **Potential:** The "Planner -> HITL -> Execution" pattern is a strong candidate for a future **"Reusable Pipeline Setting."**

## 10. Comparison focus results
- **Planner / Supervisor role:** AWS splits planning from execution oversight. Our Codex role currently combines both (Packet design + Result packaging). **Inspiration:** Codex could produce a "Plan Packet" first for User review before producing the "Execution Packet."
- **HITL boundary:** AWS uses a visual Web UI for HITL. Our space uses "User-facing cards" and "Handoff summaries." **Fit:** User as Judge is perfectly consistent.
- **Resource vs Tool boundary:** AWS "Agents" are tools; the data they process are resources. **Observation:** This reinforces the MCP lens applied in Run 231.
- **Process asset possibility:** The "Analysis Plan Review" step is a clear process asset candidate.
- **Adoption pressure check:** The Strands SDK and AWS stack look powerful but must remain **HOLD** to avoid implementation drift and dependency lock-in.

## 11. Program-readiness without implementation
- **trigger_shape:** User request for complex data/structural analysis.
- **input_shape:** CSV/PDF/Data + Intent.
- **output_shape:** Phase 1: Plan -> Phase 2: Report.
- **role_boundaries:** Coordinator (User), Planner (Codex-Design), Supervisor (Codex-Review), Agent (Gemini).
- **retrieval_boundary:** `retrieval_scope_boundary` for prior plans.
- **reuse_hook:** `reusable_when` multi-step.
- **human_only_judgment:** Approval of the "Analysis Plan."
- **never_automate:** Final "Output" acceptance.
- **current_program_readiness:** **seed** (The roles are mapped, but the handoff files are not yet templated).

## 12. Structural fit judgment
- **Fit:** **REAL_TEST_FIT_CONFIRMED_WITH_NOTES**
- **Most useful part:** The `Comparison Focus` section. It forced me to look for *what to borrow* vs *what to avoid*, preventing the "Whole-repo adoption" trap.
- **Heavy part:** Mapping the 4-tier AWS hierarchy (Coordinator/Planner/Supervisor/Agent) to our 4-role model (User/ChatGPT/Codex/Gemini) required significant conceptual effort.
- **Archive prevention:** Successfully converted an external repo into a "Planning-phase" inspiration signal.
- **Premature adoption prevention:** Strongly reinforced by the `Do not do yet` list and `Candidate` status.

## 13. Watch items
- **candidate becoming adoption pressure:** High (The AWS model is very polished).
- **external repo becoming architecture:** Danger of treating AWS logic as our "Final Design."
- **planner/supervisor reference becoming role law:** Keep roles as flexible orientations.
- **HITL reference becoming hidden permission system:** Preserve the manual User gate.
- **Reuse Hook becoming router:** No autonomous phase transitions.
- **Gemini evidence becoming truth:** This report is worker evidence for User review.

## 14. Do not do yet
- NO implementation of AWS stack or SDKs.
- NO automation or scripts.
- NO registry/index/ledger.
- NO formal schema.
- NO official workflow.
- NO current-position update.
- NO package movement.
- NO baseline promotion.
- NO tool/API/function attachment.
- NO repo architecture adoption.
- NO Gemini autonomous authority.
- NO implementation planning from this test alone.

## 15. Final status
**STATUS: FORMATION_PREWORK_REAL_TEST_COMPLETE**
