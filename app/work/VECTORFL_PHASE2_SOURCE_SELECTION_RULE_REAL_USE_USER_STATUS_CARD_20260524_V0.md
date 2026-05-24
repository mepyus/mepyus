# VECTORFL_PHASE2_SOURCE_SELECTION_RULE_REAL_USE_USER_STATUS_CARD_20260524_V0

DONE: Phase2 source-selection rule candidate 실제 적용 완료.

verdict: PASS_PHASE2_SOURCE_SELECTION_RULE_REAL_USE_WITH_HOLD

핵심:
공간참조는 많이 읽는 것이 아니라, 판단을 바꾸는 참조를 고르는 것.
각 ref는 path/exist/sha뿐 아니라 used_for + changed_judgment를 가져야 함.

default max refs:
4

Codex/Gemini 신규 호출:
NO_SKIPPED_BY_BUDGET_GATE

검증:
- checks: 11
- negative_cases: 5
- active_hits: 0
- elapsed: 0.0009540830069454387s

현재 위치:
PHASE2_SOURCE_SELECTION_RULE_REAL_USE_PASSED_WITH_HOLD

HOLD 유지.
