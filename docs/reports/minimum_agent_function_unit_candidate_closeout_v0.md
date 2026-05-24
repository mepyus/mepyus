# Minimum Agent Function Unit Candidate Closeout v0

## 1. Verdict
**VIBE_TRADING_PACKAGED_AS_STRUCTURE_REFERENCE_WITH_WATCH**
(Refined to: **STATUS: MINIMUM_AGENT_FUNCTION_UNIT_CANDIDATE_CLOSED_WITH_BOUNDARY_FIXES**)

## 2. What was fixed
*   **Compact Mode Guard:** Compact mode must not omit boundaries, only compress them. 
*   **Evidence Trace:** Always required, but miniaturized (source/judgment/next action) for Compact mode.
*   **Hook Downshift:** Defined as a manual pause/check signal, explicitly blocking automatic triggers or hidden routers.
*   **Skill Invocation Context:** Removed "skill loader" phrasing; replaced with "invocation context / usage condition" to avoid registry-like implications.

## 3. Corrected MAFU shape
*   **Identity:** `name`, `type` (Skill/Hook/Harness/Hybrid), `mode` (Compact/Standard/Heavy).
*   **Input:** `input material`, `prior references`, `user intent`.
*   **Scope:** `allowed work`, `forbidden work`, `retrieval boundary`.
*   **Execution frame:** `worker action`, `tool surface`, `stop condition`, `User Gate`.
*   **Output:** `result`, `evidence trace`, `watch/hold`, `next safe action`, `re-entry signal`.
*   **Boundary:** `must_not_become` (System law/Workflow/Registry).

## 4. Corrected minimal field set

| Field | Required? | Why | Can omit when | Risk |
| :--- | :--- | :--- | :--- | :--- |
| **name/type/mode** | required | Identify candidate | - | Role ambiguity |
| **user_intent** | required | Alignment | - | Intent drift |
| **scope/boundary** | required | Safe operation | Compact mode (compressed) | Boundary excess |
| **stop_condition** | required | Safety | - | Loop runaway |
| **evidence_trace** | required | Transparency | Compact mode (mini) | Blackbox judgment |
| **next_safe_action** | required | Worker guidance | - | Direction loss |
| **User_gate** | required | Authorization | - | Ceremony drift |

## 5. Corrected Skill / Hook / Harness fit

| Candidate | Fit | Corrected reading | Thin part | Watch |
| :--- | :--- | :--- | :--- | :--- |
| **External Repo Reading Skill** | FIT | Skill-type MAFU (needs invocation context) | Skill loader identity | Registry drift |
| **Source Contamination Hook** | FIT | Hook-type MAFU (manual pause/check) | Automatic trigger | Hard blocker |
| **External Repo Reading Harness** | FIT | Harness-type MAFU (bounded worker frame) | Workflow confusion | Automation pressure |

## 6. Current state
**KEEP_AS_MINIMUM_AGENT_FUNCTION_UNIT_CANDIDATE**
**WAIT_FOR_NEXT_NATURAL_TRIGGER**

## 7. Watch items
*   MAFU becoming mandatory ceremony.
*   "Standard/Heavy" fields becoming mandatory schema.
*   "Process Asset" becoming formal ledger.
*   Gemini/Codex output being treated as verified truth.
*   "Harness" or "Hook" labels becoming hidden system architecture.
*   Manual invocation being mistaken for "Tool Attachment."

## 8. Do not do yet
- NO implementation, automation, or runtime script creation.
- NO registry, index, ledger, router, controller, formal schema.
- NO official workflow declaration.
- NO current-position update or baseline promotion.
- NO tool/API/function attachment.
- NO ontology creation.
- NO forced pipeline creation.
- NO integrated engine implementation from this spec alone.
- NO Gemini verified-truth authority.
- NO Codex final authority.

## 9. Final status
**STATUS: MINIMUM_AGENT_FUNCTION_UNIT_CANDIDATE_CLOSED_WITH_BOUNDARY_FIXES**
