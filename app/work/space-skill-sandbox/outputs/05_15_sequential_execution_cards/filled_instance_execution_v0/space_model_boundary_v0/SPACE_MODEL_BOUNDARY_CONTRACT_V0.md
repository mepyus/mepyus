# Space / Model Boundary Contract v0

verdict:
  SPACE_MODEL_BOUNDARY_CONTRACT_PREPARED_WITH_EXECUTION_HOLD

purpose:
  Separate three things that are often confused:
    1. structure completion
    2. model-only use
    3. space-mediated model use

current_state:
  structure is being completed
  model execution is HOLD
  space-mediated model execution is not yet performed
  promotion is HOLD

## 1. Definitions

structure_completion:
  Meaning:
    Files, prompts, contracts, validators, gates, runbooks, receipts, and output paths exist.
  Does not mean:
    Gemini ran.
    Codex ran.
    model API transport occurred.
    VectorFL accepted anything.
    promotion occurred.

model_only_use:
  Meaning:
    A model is asked directly and returns an answer.
    The model may reason, summarize, or judge in the current conversational/model context.
  Risk:
    It can look smart but is not anchored as recoverable space evidence.
    The output may not be tied to packet path, declared inputs, output dir, receipt, STOP/HOLD, or recovery class.
  VectorFL status:
    residue at most, unless recovered through a declared packet/receipt lane.

space_mediated_model_use:
  Meaning:
    A model is invoked through a declared space artifact path with exact input/output contracts.
    The model output is captured as raw evidence.
    A lite/return artifact is materialized.
    A receipt records negative evidence and boundaries.
    Codex/VectorFL recovery can inspect the artifacts without relying on hidden chat state.
  Required anchors:
    packet path
    declared input files
    declared output directory
    exact command or invocation rule
    raw output capture
    lite/recovery output
    receipt/report
    WATCH/HOLD
    recovery class

## 2. Current Work Classification

current Hermes work:
  type: structure_completion
  space utilization: yes, filesystem artifact preparation under declared sandbox output directory
  model execution for bridge: no
  Gemini execution: no
  Codex recovery execution: no
  external Codex review execution by Hermes: no
  VectorFL authority mutation: no
  promotion: no

why this is space utilization:
  The work creates and validates named artifacts in a stable output space.
  The artifacts are inspectable by separate Codex/Gemini lanes later.
  The outputs are not just conversational advice; they are packetized files and receipts.

why this is not model-mediated bridge execution yet:
  No Gemini command has been run.
  No Codex recovery command has been run.
  No model API transport for bridge execution occurred.
  Future model outputs are declared but not materialized.

## 3. Required Distinction Table

```text
Question: Is the structure complete?
Answer: partially/mostly yes, up to approval gate and harness.
Evidence: packet, prompts, contracts, runbook, scripts, validators, receipts.

Question: Did Gemini run?
Answer: no.
Evidence: future outputs missing; guard blocks approval=no.

Question: Did Codex recovery run?
Answer: no.
Evidence: codex_combined_bridge_recovery_return.md missing by design.

Question: Was a model used only as conversational reasoning?
Answer: Hermes model helped prepare artifacts in this session.
Boundary: that is not the same as bridge Gemini/Codex execution.

Question: Was the VectorFL space used?
Answer: yes, as artifact space and contract surface.
Boundary: not as authority mutation or promotion.

Question: Was the space used to run models through the packet lane?
Answer: no, not yet.
Needed: explicit approval + guarded runner + raw/lite/receipt materialization.
```

## 4. Space-Mediated Execution Readiness Criteria

Before saying “we used the space to run the model,” all must be true:

```text
1. Packet approval says yes.
2. The invocation uses the packet-declared prompt path.
3. Raw model output is written to the declared output file.
4. Lite or recovery output is written to the declared output file.
5. Receipt records the exact files and negative evidence.
6. The output can be re-read from disk without hidden chat context.
7. WATCH/HOLD/recovery_class are present.
8. Promotion remains separately gated.
```

## 5. Current Boundary Verdict

```text
STRUCTURE_COMPLETION: yes
SPACE_ARTIFACT_UTILIZATION: yes
MODEL_ONLY_REASONING_IN_THIS_CHAT: yes, for artifact design by Hermes
SPACE_MEDIATED_GEMINI_EXECUTION: no
SPACE_MEDIATED_CODEX_RECOVERY: no
VECTORFL_AUTHORITY_USE: no
PROMOTION: no
```

## 6. STOP Conditions

```text
saying Gemini ran when only prompt/contract exists
saying Codex recovered when only review prompt/contract exists
treating chat reasoning as VectorFL recovered evidence
treating file creation as VectorFL authority mutation
treating receipt as approval
treating execution approval as promotion approval
running Gemini/Codex outside declared output capture
running model without raw/lite materialization
```

required_final_line:
  No execution was performed. No promotion was performed. Recovery class remains candidate.
