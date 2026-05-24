# Formation Prework Next Real Test Candidate Selection v0

## 1. Purpose
The purpose of this document is to select the next best candidate for a real `Function/Process Formation Prework v1` test. Following the successful closure of the MCP test as an `operation_reference`, we now seek a candidate that continues to test the maturity of our "Prework" incubator structure without triggering premature implementation or adoption.

## 2. Current State
```text
MCP real test is closed as operation_reference.
Next step is to select a different candidate for Formation Prework v1.
No implementation or attachment is approved.
```

## 3. Candidate Shortlist

### Candidate: AWS sample-deep-insight
- **Type:** Repo / Architectural Reference
- **Resource_or_Tool_or_Both:** Both
- **Possible Space Role:** `operation_reference` / `lens`
- **Why it may be useful:** It provides a mature model for planner/supervisor roles and human-in-the-loop (HITL) gates. This allows us to test if our prework can extract complex "role-based coordination" patterns without adopting the specific AWS technical stack.
- **Why it may be risky:** High risk of "Architecture Drift"—misreading their specific supervisor model as our project's final design.
- **Expected Prework Value:** Clarification of the "Supervisor-Agent" boundary vs. our "Codex-Gemini" boundary.
- **What not to do:** No AWS stack installation; no copying their specific state-machine logic.

### Candidate: Warp (terminal / operating surface)
- **Type:** Terminal Tool / CLI Interface
- **Resource_or_Tool_or_Both:** Tool
- **Possible Space Role:** `operation_reference` / `operating_surface`
- **Why it may be useful:** It emphasizes the "durable file context before chat history" philosophy, which aligns with our "File before Chat" principle. It tests if prework can form a role for an "Interface philosophy" candidate.
- **Why it may be risky:** Temptation to adopt specific UI features or "Warp-specific" workflows into our space.
- **Expected Prework Value:** Definition of "Operating Surface" affordances for future CLI attachment.
- **What not to do:** No Warp tool adoption; no implementation of Warp-like AI features.

## 4. Recommended Candidate
**Recommended Candidate: AWS sample-deep-insight**

**Why it is safest and most useful:**
This candidate is "structurally thick." Unlike MCP, which is a protocol, `sample-deep-insight` is a concrete application of roles and traces. Testing it through `Formation Prework v1` will challenge the incubator's ability to separate **architectural inspiration (Inspiration-only)** from **technical requirements (Tool)**. It is the safest next step because it remains a "reference repo" that we have already used in our connection maps, reducing the risk of "Source Invention."

## 5. User Decision Gate
The User must choose whether to:
- **Approve AWS sample-deep-insight for Gemini Formation Prework real test**
- **Choose Warp or another candidate**
- **Hold**
- **Reject**

## 6. Watch Items
- Candidate selection becoming implicit implementation pressure.
- MCP vocabulary (Resource/Tool) becoming a rigid, forced ontology for non-protocol candidates.
- Formation Prework becoming a heavy, mandatory ceremony for simple references.
- Codex's recommendation being treated as an automatic "Go" for implementation.
- External repo references being misread as adoption plans.

## 7. Do Not Do Yet
- NO implementation of any selected tool or repo.
- NO automation or runtime script creation.
- NO baseline promotion of candidates.
- NO tool/API/function attachment.
- NO Gemini broad execution beyond the approved prework worklist.
- NO Codex autonomous movement beyond this selection.

STATUS: NEXT_FORMATION_PREWORK_TEST_CANDIDATE_SELECTION_PREPARED
