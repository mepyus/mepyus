# FAST_FIRST_OPERATOR_ROUTE_CARD_V0

verdict: FAST_FIRST_MODE_SELECTED_WITH_HOLD

이번 "응 계속"은 heavy 명시 요청이 아니라 budget gate 적용 continuation으로 판정.

## route
- 1 preserve user original
- 2 read budget gate policy and latest operator surface
- 3 check heavy triggers before invoking Codex/Gemini
- 4 if no heavy trigger, run fast no-call local validation
- 5 if drift/ambiguity appears, escalate to HEAVY_BUDGETED
- 6 write receipt/trace as evidence only

## escalate if
- user explicitly asks for actual Hermes/Codex/Gemini participation
- task changes VectorFL operating principle or architecture
- space interpretation is ambiguous across layers
- drift/risk class appears: model-only merge, missing current-position, authority drift, hidden receipt failure, endpoint/API drift
- promotion/authority pressure exists but must remain HOLD
- fresh task requires cross-agent comparison not just artifact validation

## HOLD
authority/registry/current-position/promotion 없음.
