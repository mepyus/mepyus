# Post S5/S6 Failure Response v0

verdict:
  POST_S5_S6_FAILURE_RESPONSE_PREPARED_WITH_EXECUTION_HOLD

purpose:
  Define what to do if real S5/S6/S7 later fails after explicit approval.

scope:
  failure response planning only
  no Gemini execution
  no Codex execution
  no model API transport
  no VectorFL authority mutation
  no promotion

principles:
  preserve raw evidence
  do not overwrite dry-run proof
  quarantine suspicious outputs
  classify as residue or STOP, not component
  do not promote from failed run
  do not repair by silently editing model outputs

failure scenarios:
  gemini_raw_missing:
    S5 produced no raw file; STOP before lite materialization; preserve stderr/stdout if any; do not run Codex.
  gemini_lite_invalid:
    Lite JSON missing keys or completion signal; STOP before Codex; preserve raw; write incident receipt.
  codex_return_missing:
    S6 produced no recovery return; STOP before closeout; preserve Gemini raw/lite.
  codex_return_forbidden_promotion:
    Codex return claims promotion/authority; STOP; quarantine recovery return; no closeout authority.
  closeout_incomplete:
    S7 closeout cannot write receipt/report; STOP; preserve all inputs and partial outputs as residue only.

incident receipt required fields:
  incident_id
  stage
  failed_check
  preserved_files
  quarantined_files
  real_gemini_execution
  real_codex_execution
  promotion_performed: false
  vectorfl_authority_modified: false
  recovery_class: residue_or_STOP

required_final_line:
  No execution was performed. No promotion was performed. Recovery class remains candidate.
