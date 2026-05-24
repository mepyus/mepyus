# INFRA_COST_CONTEXT_ECONOMICS_LENS_CARD_HOLD_ONLY_V0

verdict: PASS_INFRA_COST_CONTEXT_ECONOMICS_LENS_CARD_WITH_HOLD

## 왜 생겼나

EP96는 LLM 추론 인프라와 토큰 경제학을 통해 context/KV cache/prefill/decode/batch/HBM/memory-bound/200K tier가 실제 비용·latency를 만든다는 원인층을 보여줬다.
EP97은 T_brain/operator-load/slow-AI/maintainability guard를 줬다.

둘이 겹치면서 VectorFL budget gate에는 인간 부담뿐 아니라 model/context infra 부담도 같이 봐야 하는 lack가 생겼다.

## lens 정의

질문:
이 작업은 fresh space reference 또는 layer ambiguity를 해소할 만큼 provider-backed model/context cost를 정당화하는가?

primary layer:
- L5_budget_governance

secondary:
- L2_inference_infra_budget
- L3_harness_control_layer
- L4_operator_surface_tbrain

## 필수 후보 fields

- fresh_space_reference_needed
- layer_ambiguity_requires_codex_or_gemini
- context_footprint_class
- expected_prefill_pressure
- operator_load_delta
- on_demand_reason
- read_first_file_count
- raw_corpus_available_but_not_default
- lite_output_required
- provider_backed_call_budget

## gate rule

- 상태확인/목록화/반복검증: Hermes local deterministic only
- fresh space reference 필요: Codex retrieval packet 먼저
- Codex maturation 중 layer ambiguity: Codex-side Gemini request 가능
- large raw corpus: read-first/index/lite output 먼저
- operator-load만 늘고 changed_judgment가 없으면 heavy call reject

## 현재 상태

HOLD evidence/proposal only.
실제 schema/registry/current-position/folder tree 적용 아님.
