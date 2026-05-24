# VECTORFL_NEXT_WORK_AFTER_ACTUAL_MULTI_AGENT_FRESH_TASK_BUDGET_GATE_20260524_V0

NEXT_SAFE_LANE: APPLY_BUDGET_GATE_TO_NEXT_REAL_VECTORFL_TASK_WITH_FAST_FIRST_MODE_V0

purpose:
Use the budget gate on the next real VectorFL task. Start fast-first, then escalate only if the gate triggers.

Do:
1. Pick/receive a concrete task.
2. Run Hermes original interpretation + space read.
3. Apply budget gate.
4. If no heavy trigger: fast no-call local validation.
5. If heavy trigger: Codex1 + Gemini1 + Hermes merge/execute.

Do not:
- mutate authority/registry/current-position
- promote Program Alpha
- run endpoint replay/server/API-direct
