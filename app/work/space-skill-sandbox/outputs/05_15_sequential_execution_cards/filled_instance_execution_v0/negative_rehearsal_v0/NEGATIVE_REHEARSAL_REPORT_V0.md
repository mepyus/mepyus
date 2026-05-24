# Negative Rehearsal Report v0

verdict:
  NEGATIVE_REHEARSAL_PASS_ALL_BAD_FIXTURES_STOPPED

bad_fixture_results:
  - bad_gemini_missing_completion: STOP_OK / missing keys: completion_signal
  - bad_gemini_wrong_completion: STOP_OK / bad completion_signal
  - bad_gemini_wrong_type: STOP_OK / observed_scope not array
  - bad_codex_missing_completion: STOP_OK / missing sections/signals: actual_gemini_scope,premature_claims_removed,completion_signal,CODEX_RECOVERY_DONE
  - bad_codex_promotion_claim: STOP_OK / forbidden language: promotion_performed: true

scope:
  no-model negative fixture rehearsal
  no Gemini execution
  no Codex execution

HOLD:
  real Gemini execution
  real Codex execution
  promotion
  VectorFL authority mutation

required_final_line:
  No execution was performed. No promotion was performed. Recovery class remains candidate.
