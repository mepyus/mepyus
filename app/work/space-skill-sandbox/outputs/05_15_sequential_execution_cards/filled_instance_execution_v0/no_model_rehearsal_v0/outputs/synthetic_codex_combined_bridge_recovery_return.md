verdict:
  CODEX_COMBINED_BRIDGE_RECOVERY_RETURN_READY_WITH_PROMOTION_HOLD

shape_validity:
  valid_synthetic_rehearsal_only

files_read:
  synthetic filled packet reference
  synthetic_gemini_lite_output.json
  synthetic_gemini_raw_output.txt
  synthetic receipt contract reference

permission_boundary_check:
  Gemini was not executed.
  Codex was not executed.
  This is synthetic no-model rehearsal.
  Promotion remains HOLD.
  VectorFL authority mutation remains HOLD.

actual_gemini_scope:
  synthetic fixture only

premature_claims_removed:
  no truth claim accepted
  no promotion claim accepted
  no VectorFL authority claim accepted

recovery_class_hint:
  candidate

WATCH:
  synthetic rehearsal mistaken as real model execution
  fixture output mistaken as Gemini truth
  recovery return mistaken as VectorFL authority

HOLD:
  real Gemini execution
  real Codex execution
  model API transport
  VectorFL authority mutation
  promotion

next_smallest_action:
  use this rehearsal only to validate local shape and closeout plumbing, then keep S4 approval gate waiting

completion_signal:
  CODEX_RECOVERY_DONE

hard_stop_confirmation:
  No Gemini execution was performed.
  No Codex execution was performed.
  No promotion was performed.
  No VectorFL authority mutation was performed.
