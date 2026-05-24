# Execution Lane State Machine v0

verdict:
  EXECUTION_LANE_STATE_MACHINE_PREPARED_WITH_EXECUTION_HOLD

purpose:
  Make it impossible to confuse structure build-up, model-only reasoning, and space-mediated model execution.

## States

S0_DRY_RUN_PROOF:
  meaning: validated dry-run exists and is preserved.
  model_execution: no
  space_use: proof artifact only
  current: completed

S1_EXECUTION_STRUCTURE_PREP:
  meaning: packet, prompts, contracts, outputs dir, receipt/report contracts exist.
  model_execution: no
  space_use: artifact/contract surface
  current: completed

S2_REVIEW_ONLY_PREFLIGHT:
  meaning: local static preflight and review-only Codex prompt exist.
  model_execution: no external Codex review by Hermes
  space_use: validation surface
  current: completed

S3_EXECUTION_HARNESS_READY:
  meaning: guarded runner, validator, materializer, approval gate, runbook exist.
  model_execution: no
  space_use: future execution lane prepared
  current: completed

S4_APPROVAL_GATE_WAITING:
  meaning: everything is ready up to the gate, but packet approval remains no.
  model_execution: blocked
  space_use: waiting state
  current: active

S5_GEMINI_SPACE_MEDIATED_RUN:
  entry_requirements:
    EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
    APPROVED_PROMOTION: no
    static validator passes
    operator acknowledgement env present
  action:
    run Gemini through declared prompt
    capture raw stdout to outputs/gemini_raw_output.txt
    materialize outputs/gemini_lite_output.json
  model_execution: yes, Gemini
  space_use: model output captured into declared space
  current: not entered

S6_CODEX_SPACE_MEDIATED_RECOVERY:
  entry_requirements:
    S5 complete
    gemini_raw_output.txt exists
    gemini_lite_output.json valid
    Codex 4-input contract intact
  action:
    run Codex recovery prompt
    write outputs/codex_combined_bridge_recovery_return.md
  model_execution: yes, Codex recovery
  space_use: recovery output captured into declared space
  current: not entered

S7_HERMES_RECEIPT_REPORT_CLOSEOUT:
  entry_requirements:
    S6 complete
  action:
    write HERMES_EXECUTION_RECEIPT_V0.json
    write HERMES_EXECUTION_REPORT_V0.md
  model_execution: no new model required
  space_use: receipt/report closure
  current: not entered

S8_VECTORFL_RECOVERY_GATE:
  entry_requirements:
    S7 complete
    separate VectorFL recovery decision
  action:
    classify receipt/residue/candidate/STOP
  authority_mutation: still no unless separately approved
  promotion: still no unless separately approved
  current: not entered

## Current Active State

```text
S4_APPROVAL_GATE_WAITING
```

## Important Distinctions

```text
S1/S2/S3/S4 = structure and space preparation, no bridge model execution.
S5/S6 = actual space-mediated model execution.
Model-only reasoning in chat is outside this lane and cannot satisfy S5/S6.
```

## Transition Guard

S4 -> S5 is forbidden until explicit user approval changes the packet approval field to yes.
S5 -> S6 is forbidden until Gemini raw/lite outputs exist and validate.
S6 -> S7 is forbidden until Codex recovery return exists and completion signal is present.
S7 -> S8 is not promotion; it is only recovery gate input.

required_final_line:
  No execution was performed. No promotion was performed. Recovery class remains candidate.
