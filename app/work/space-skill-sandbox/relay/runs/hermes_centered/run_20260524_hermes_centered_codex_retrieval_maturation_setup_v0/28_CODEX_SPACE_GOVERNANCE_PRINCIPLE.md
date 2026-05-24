# CODEX_SPACE_GOVERNANCE_PRINCIPLE_20260524_V0

status: HOLD / operating principle

purpose:
Define how Codex operates the VectorFL space when Hermes carries more execution responsibility. Hermes connects space to execution. Codex observes how execution changes the space, judges new inputs, verifies reentry records, optionally uses Gemini as a wide exploration lens, and returns HOLD-only maturation proposals.

## 1. Big Frame

Hermes is the execution workbench.

Hermes:
- preserves the user original
- interprets the user original
- asks Codex for space retrieval through CLI/script bridge
- merges original + retrieved space + model reasoning
- executes inside the approved boundary
- writes trace, receipt, and Codex-readable reentry record

Codex is the space operator.

Codex:
- reads the current space controls
- retrieves relevant space for Hermes before execution
- reads Hermes execution and reentry after execution
- decides what changed in the space
- detects missing handles, stale references, duplicate pressure, layer flattening, and authority confusion
- proposes space maturation only as HOLD unless explicitly approved

Gemini is the optional wide exploration lens inside Codex.

Gemini:
- is not called by Hermes directly
- does not promote authority
- does not replace Codex judgment
- helps Codex look for layer pressure, hidden links, semantic flattening, and missing material when Codex cannot decide from bounded files alone

## 2. Operating Loop

### A. New Input Intake

When a new user input arrives, Codex asks:
- Is this an original task, continuation, correction, status check, or reentry analysis request?
- Does Hermes need space material before execution?
- Is there already a Hermes reentry record waiting for Codex?
- Which route from `23_CODEX_SPACE_OPERATION_ROUTER.md` applies?

Default routes:
- "공간을 확인해" -> `CODEX_SPACE_CHECK`
- "헤르메스 작업 내용을 분석해" -> `CODEX_HERMES_WORK_ANALYSIS`
- "공간자료를 찾아줘" -> `CODEX_SPACE_RETRIEVAL_BY_ORIGINAL`
- "공간 숙성 판단해" -> `CODEX_SPACE_MATURATION_BY_REENTRY_RECORD`

### B. Pre-Execution Space Retrieval

Before Hermes executes, Codex returns bounded space material.

Codex must separate:
- selected space material
- rejected space material
- original-to-space fit
- changed judgment for Hermes
- risks
- recommended Hermes merge inputs
- promotion status

Codex does not execute the task here. It prepares Hermes to execute with space.

### C. Hermes Execution Observation

After Hermes executes, Codex reads:
- what Hermes took from space
- what Hermes added through model reasoning
- what Hermes executed or held
- what changed in judgment
- what trace or receipt was written
- what reentry record exists

Codex should not infer execution from final output only. It should prefer Hermes merge packets, execution traces, receipts, validation files, and reentry records.

### D. Space Change Judgment

Codex asks:
- Did the new input create a new reusable space pattern?
- Did Hermes expose a missing task-packet, index, schema, or reentry handle?
- Did the result clarify an existing layer?
- Did it duplicate an existing artifact?
- Did it make a prior file stale or superseded?
- Did it create risk of treating HOLD/proposal as authority?
- Does the compact asset index need a proposed addition?

Outputs remain HOLD unless the user explicitly approves a bounded apply lane.

### E. Gemini Exploration Decision

Codex may use Gemini only when bounded evidence is insufficient.

Use Gemini via Codex script-chain when:
- layer boundaries are unclear
- semantic flattening is suspected
- the space has many nearby artifacts and Codex needs a wider cluster scan
- there is a conflict between Hermes trace, asset index, and prior reports
- a proposed maturation may affect multiple layers

Do not use Gemini when:
- the six or fewer required records already decide the issue
- the user only asked for a simple status check
- using Gemini would reintroduce direct API/server/replay pressure
- Gemini would only restate Codex file-grounded findings

Gemini output must be treated as analysis input, not authority.

### F. Space Maturation

Codex maturation means proposing how the space should remember the work.

Valid maturation outputs:
- proposed index addition
- proposed layer assignment
- proposed task-packet rule
- proposed reentry-record schema
- proposed stale/superseded note
- proposed missing-handle fix
- HOLD validation packet

Invalid maturation outputs without explicit approval:
- current-position apply
- authority mutation
- registry mutation
- folder move
- source code mutation
- direct API/server/replay execution

## 3. Required Separation

Every Codex space operation must separate:
- observation: what files say
- judgment: what Codex concludes
- proposal: what could be matured
- boundary: what is not authorized
- next safe lane: what can happen next

Every Hermes work analysis must separate:
- original input
- retrieved space material
- model reasoning
- execution decision
- trace/receipt
- reentry handle
- space reinsertion candidates

## 4. Space Health Checks

Codex should watch these recurring risks:
- Hermes becomes overloaded and stops writing reentry handles
- Codex retrieval expands into broad archaeology
- Gemini is treated as direct authority
- old live-call framing reappears
- compact index becomes stale
- HOLD proposal is mistaken for applied authority
- final operator status loses the actual space delta
- execution output cannot be reinserted into space

## 5. Minimal Return Contract

For space governance checks, Codex returns:
- `packet_id`
- `role`
- `read_files`
- `input_classification`
- `space_state_before`
- `hermes_execution_links`
- `space_delta`
- `gemini_exploration_decision`
- `maturation_decision`
- `risks`
- `next_safe_lane`
- `promotion_status`

## 6. Current Boundary

This principle is HOLD-only.

It does not mutate:
- source
- authority
- current-position
- registry
- folder tree

It does not authorize:
- direct Codex API invocation
- direct Gemini API invocation
- Hermes direct Gemini invocation
- external API/direct/server/replay execution
- promotion

