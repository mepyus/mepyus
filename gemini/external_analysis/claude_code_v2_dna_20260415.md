# Everything-Claude Code Structural DNA Analysis

Date: 2026-04-15
Actor: Gemini-CLI
Source: `references/git_search/everything-claude-code-main/`
Reason: Multi-agent persona and layered rule architecture for VECTORFL expansion.

## 1. Key Structural Axes

### A. Axis of Persona (The Agent Definition)
- **DNA**: `Role-based Instructions (agents/*.md) + Shared Skill Registry`.
- **Meaning**: The same engine, multiple distinct agent faces (e.g., Architect, Reviewer, Planner).

### B. Axis of Contextual Guardrails (Layered Rules)
- **DNA**: `Global Common Rules + Language/Task Overlays`.
- **Meaning**: Guardrails are not global/flat; they are stackable (e.g., Python + Security + Git-Workflow).

## 2. Adoption Strategy for VECTORFL

| Pattern | Structural Axis | Recommended VECTORFL Application |
| :--- | :--- | :--- |
| **Persona Registry** | Multi-Agent | Implement `vectorfl/agents/` to define Gemini personas (Architect/Reviewer/Executor). |
| **Layered Rules** | Guardrails | Move from flat constitutional rules to a stacked `rules/` system. |

## 3. Gemini's Judgment
Everything-Claude Code의 핵심은 **"역할에 따른 프롬프트 최적화"**입니다. 우리는 엔진의 정합성을 지키면서도, 사용자의 작업 목적에 따라 '건설적 모드', '분석적 모드', '검증적 모드'로 에이전트 인격을 전환하는 구조를 도입해야 합니다.

---
*Note: This analysis is stored in `gemini/external_analysis/` as per the current session protocol. No files outside `gemini/` were modified.*
