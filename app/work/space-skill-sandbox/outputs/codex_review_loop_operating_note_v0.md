# Codex Review Loop Operating Note v0

Status: Operating note / compact memory
Authority: Not baseline / Not official workflow / Not automation

## Core Loop

User sets direction and gives final approval.
ChatGPT validates Codex structure and judgment.
Codex designs the structural frame, writes bounded Gemini prompts, reviews Gemini returns, and sets the next direction.
Gemini performs bounded observation/execution and returns evidence only.

## Codex Review Rule

Gemini output is not accepted as authority by default. Codex must check:

- scope adherence
- role boundary
- evidence vs interpretation separation
- candidate / accepted / hold / invalid status
- sandbox-to-whole-space over-promotion risk
- next safe action

## Instruction Storage Rule

Long Gemini prompts do not need to be saved every time. During active work, store only compact notes when useful. Full prompt/history consolidation can happen later when the user requests a session summary or record cleanup.

## Current Application

Run 140 Gemini result can be treated as readiness for a user gate decision only. It does not approve Package 033, promote Package 033, open Package 036, analyze Package 035, or turn the v1 checklist into baseline/workflow.
