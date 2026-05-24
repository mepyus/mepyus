# AIFRONTIER_EP96_OVERLAP_LACL_TEST_V0

source: https://aifrontier.kr/ko/episodes/ep96/
title: EP 96: LLM 추론 인프라와 토큰 경제학 | AI Frontier
verdict: PASS_AIFRONTIER_EP96_OVERLAP_LACL_TEST_WITH_HOLD
execution: HERMES_LOCAL_ONLY_WEB_FETCH_PLUS_SPACE_FILE_READ
codex_executed: NO
gemini_executed: NO
promotion: HOLD

## 1. 테스트 질문

EP96를 실제로 가져와서, 이미 공간에 있는 EP97 자료와 겹치는 층위/부족(lack 또는 lacl/layer collision) 압력이 생기는지 확인했다.

## 2. EP96 핵심

EP96는 LLM 추론 인프라와 토큰 경제학이다.
핵심은 context/KV cache/prefill/decode/batch/HBM/memory-bound/200K tier/cache TTL이 실제 provider-backed call의 비용과 latency를 만든다는 점이다.

## 3. EP97 기존 공간자료와의 겹침

EP97은 T_brain/operator-load, mind-sized bite, slow-AI guard, maintainability debt를 공간 압력으로 추가했다.
EP96는 그 아래쪽 원인층을 제공한다.

겹치는 층위:
- L2 inference infra / budget: EP96 primary
- L5 budget governance: EP96와 EP97 강하게 결합
- L3 harness/control layer: Claude Code/Codex/tool call/context management에서 결합
- L4 operator surface/T_brain: EP97의 human-load와 EP96의 model-load가 결합

## 4. 생긴 lack/lacl 후보

1. LACK_INFRA_COST_LENS_CARD
   - KV cache/prefill/decode/batch/memory-bound를 VectorFL budget gate와 연결하는 lens card가 부족하다.

2. LACK_CONTEXT_ECONOMICS_FIELD
   - packet/report에 context footprint, read-first size, expected prefill pressure field가 필요해진다.

3. LACK_MODEL_LOAD_OPERATOR_LOAD_PAIRING
   - EP97의 T_brain/operator-load와 EP96의 model-serving-load를 함께 보는 paired gate가 필요하다.

4. LACK_CODEX_GEMINI_ON_DEMAND_REASON_FIELD
   - Codex/Gemini 호출 필요성을 fresh space reference / layer ambiguity / explicit approval로 분류하는 reason field가 필요하다.

## 5. space_reference_delta

- EP96는 EP97의 slow-AI/operator-load 판단을 뒤집지 않고 강화한다.
- 단, EP97이 human-load 중심이었다면 EP96는 infra-load/context-cost 원인층을 추가한다.
- 따라서 Codex/Gemini provider-backed call을 default로 쓰지 말아야 한다는 판단은 timeout 회피가 아니라 VectorFL budget governance의 구조 원칙으로 강화된다.

## 6. 결론

EP96가 공간에 들어가면 겹치는 층위와 lack/lacl이 실제로 생긴다.
가장 중요한 결합은:

EP96 infra/context economics
→ EP97 T_brain/operator-load
→ VectorFL budget gate / on-demand Codex-Gemini policy

현재는 적용이 아니라 HOLD evidence다.
