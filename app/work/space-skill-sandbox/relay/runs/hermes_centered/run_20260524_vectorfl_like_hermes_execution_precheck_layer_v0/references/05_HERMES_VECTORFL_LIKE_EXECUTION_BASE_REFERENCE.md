# HERMES_VECTORFL_LIKE_EXECUTION_BASE_REFERENCE_V0

status: HOLD_REFERENCE_LAYER_ONLY

Principle:
Hermes execution should start in a VectorFL-like way for non-trivial work:

USER_ORIGINAL
→ SPACE_ORIENTATION
→ MODEL_REASONING_OVER_ORIGINAL_PLUS_SPACE
→ EXECUTION_SHAPE / WORKLIST
→ BUDGET + CALL GATE
→ HERMES EXECUTION
→ TRACE / RECEIPT / DELTA
→ CODEX-READABLE REENTRY

This is a reference layer, not runtime mutation.

Mandatory habit:
Before worklist or execution, write or mentally satisfy a precheck card:
- request_type
- execution_form
- space_reference_mode
- read_handles
- why_these_handles
- changed_judgment_from_space or NO_CHANGED_JUDGMENT
- budget_gate_decision
- codex_needed_now
- authority_boundary

Codex role:
Codex matures Hermes outputs later. Hermes does not call Codex unless fresh unknown space reference may change judgment.

HOLD:
No runtime mutation, no skill install, no authority/current-position mutation.
