# VECTORFL_HEAVY_VS_FAST_BUDGET_GATE_POLICY_V0

verdict: PASS_BUDGET_GATED_ACTUAL_MULTI_AGENT_FRESH_TASK_WITH_HOLD

## default
FAST_NO_CALL_LOCAL_VALIDATION

## HEAVY_BUDGETED 사용 조건
- user explicitly asks for actual Hermes/Codex/Gemini participation
- task changes VectorFL operating principle or architecture
- space interpretation is ambiguous across layers
- drift/risk class appears: model-only merge, missing current-position, authority drift, hidden receipt failure, endpoint/API drift
- promotion/authority pressure exists but must remain HOLD
- fresh task requires cross-agent comparison not just artifact validation

## FAST_NO_CALL 사용 조건
- small continuation from known safe lane
- shape/receipt/trace local validation only
- repeatability already passed and no new layer pressure
- operator needs quick status/recovery surface
- no fresh spatial ambiguity and no external agent insight needed


## Budget thresholds

- fast_target_seconds: <5s local validators/artifact writes
- budgeted_heavy_target_seconds: 60-90s using Codex 1 + Gemini 1 + Hermes merge, no post-review unless drift
- full_heavy_expected_seconds: 120s+ when Codex/Gemini post-review both run
- post_review_gate: run one post reviewer only if Codex/Gemini disagree, STOP/HOLD_STOP_REVIEW appears, or reinsertion effect is unclear

## This run timing

- Codex: 43.35s
- Gemini: 40.98s
- post_review: skipped

## HOLD

Evidence/operator policy only. Not authority, not registry, not current-position apply, not promotion.
