# Claude Code (ECC) Structural DNA Analysis

Date: 2026-04-15
Actor: Gemini-CLI
Source: `references/git_search/everything-claude-code-main/`
Reason: Structural decomposition of Claude Code for selective adoption into VECTORFL.

## 1. Key Structural Axes

### A. Axis of Knowledge Enforceability (Skill-Comply)
- **DNA**: `Specification + Scenario Generation + Trace Capture + Compliance Reporting`.
- **Meaning**: Rules are not just passive text; they are testable requirements.
- **Structural Setting**:
  - `skills/skill-comply/`: An automated system to verify if other skills are followed.
  - It uses "Strictness Levels" (Supportive -> Neutral -> Competing) to test agent resilience.

### B. Axis of Knowledge Layout (SKILL.md Template)
- **DNA**: `Trigger -> Pattern -> Anti-Pattern -> Checklist`.
- **Structural Setting**:
  - `docs/SKILL-DEVELOPMENT-GUIDE.md`: Enforces a consistent layout for all skills.
  - Section `When to Activate` is optimized for LLM context retrieval.

### C. Axis of Contextual Hierarchies (Rules)
- **DNA**: `Global Common Rules + Language-Specific Overlays`.
- **Meaning**: Separation of universal guardrails from tactical implementation details.

## 2. Adoption Strategy for VECTORFL

| Feature to Borrow | Structural Reason | Expected Value in VECTORFL |
| :--- | :--- | :--- |
| **When to Activate** | Efficient Context Management | Prevents "context bloat" by only loading relevant skills based on triggers. |
| **Anti-Patterns Section** | Error Prevention | Explicitly defines what NOT to do, reducing "hallucination-based drift". |
| **Compliance Testing** | Constitutional Integrity | Provides a way to measure if the Gemini/Codex agents are actually following the Constitution. |

## 3. Gemini's Judgment
Claude Code의 구조에서 가장 배울 점은 **"지식을 행동으로 강제하는 기술적 집요함"**입니다. 우리는 특히 `SKILL.md`의 표준 섹션 구성을 차용하여, VECTORFL의 지식 자산(`vectorfl/skills/`)을 더욱 "에이전트 친화적(Agent-friendly)"으로 재구축해야 합니다.

---
*Note: This report is stored in `gemini/external_analysis/` as per the current session protocol. No files outside `gemini/` were modified.*
