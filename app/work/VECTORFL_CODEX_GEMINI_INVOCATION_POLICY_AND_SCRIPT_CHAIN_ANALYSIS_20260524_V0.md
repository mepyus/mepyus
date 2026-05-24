# VECTORFL_CODEX_GEMINI_INVOCATION_POLICY_AND_SCRIPT_CHAIN_ANALYSIS_20260524_V0

verdict: PASS_CODEX_GEMINI_ON_DEMAND_POLICY_AND_SCRIPT_CHAIN_ANALYSIS_WITH_HOLD

## 핵심 수정

- Codex default: DO_NOT_CALL
- Gemini default: DO_NOT_CALL
- Codex는 Hermes가 새 원본 처리 중 공간 내부 자료를 새로 참조해야 할 때만 붙인다.
- Gemini는 Hermes가 직접 붙이지 않는다. Codex가 reentry/maturation을 처리하다가 layer/space 분석 필요성을 판단할 때 Codex-side script-chain에서만 붙인다.
- 목록화/검증/반복 테스트는 local deterministic/packet validation으로 처리한다.
- direct API 연결/상시 자동화는 지금 셋업하지 않는다. 나중에 정말 필요해질 때 별도 셋업한다.

## 발견한 기존 구조

1. scripts/run_vectorfl_paper_codex_bridge.py
   - handoff JSON을 읽고 codex exec read-only를 실행해 Codex return JSON을 만든다.
   - provider-backed CLI라 heavy path다.
   - fresh space/worker 판단이 필요할 때만 후보.

2. scripts/run_vectorfl_paper_gemini_crosscheck_bridge.py
   - Codex return JSON을 읽고 gemini CLI에 cross-check prompt를 보내 Gemini review JSON을 만든다.
   - Codex→Gemini script-chain의 실제 후보 구조다.
   - Hermes default 직접 호출 경로로 쓰면 안 된다.

3. gemini_script_runner_boundary_sandbox_v0/scripts/gemini_lens_runner_sim.py
   - Codex-authored request를 읽고 declared local input만 처리하는 no-network simulation.
   - 지금 당장 구조 테스트에는 이쪽이 더 안전하다.
   - 실제 Gemini validation은 아니다.

## 활용 방안

Hermes → Codex → Gemini 구조는 상시 호출이 아니라 on-demand다.

1. Hermes가 사용자 원본을 처리한다.
2. 새 공간 참조가 필요한 경우에만 Codex retrieval packet을 만든다.
3. Codex가 공간자료를 가져오고 selected/rejected/changed_judgment를 반환한다.
4. Hermes가 원본+공간+모델값으로 merge/execute/reentry를 만든다.
5. Codex가 reentry를 읽고 공간 숙성 판단을 한다.
6. Codex가 Gemini 필요성을 판단한 경우에만 Codex-side Gemini request를 만든다.
7. Gemini script-chain은 raw/lite/receipt를 만들고 Codex가 다시 판단한다.
8. Hermes는 Codex 판단을 HOLD evidence로 merge한다.

## 현재 위치

current_position: CODEX_SPACE_MATURATION_MERGED_BY_HERMES_WITH_HOLD
new_position_note: INVOCATION_POLICY_CORRECTED_AND_CODEX_TO_GEMINI_SCRIPT_CHAIN_ANALYZED_WITH_HOLD

## HOLD

- Codex/Gemini default execution: NO
- Hermes direct Gemini: NO
- direct API setup now: NO
- source/authority/current-position/registry/folder mutation: NO
- promotion: HOLD
