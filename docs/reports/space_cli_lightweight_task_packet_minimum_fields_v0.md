# Space-CLI Lightweight Task Packet Minimum Fields v0

## 1. premise

This document is not a schema.

This document is not a JSON design.

This document is not an implementation instruction.

This document is a thought-experiment note for the minimum fields a space-referenced CLI task packet may need.

The goal is to give the CLI enough context to work without feeding it the whole space or transferring final judgment authority.

## 2. minimum field candidates

## request_summary

Role:

Compress the user request into one to three sentences.

Use it to tell the CLI what the current task is without attaching the entire conversation.

Caution:

Do not include the full user conversation.

Field grade:

```text
required
```

## source_surface

Role:

Mark what kind of material the current input is.

Candidates:

- `conversation_material`
- `external_material_file`
- `generated_report`
- `worker_return`
- `runtime_event`
- `program_artifact`

Caution:

If uncertain, keep it as `candidate` or `uncertain`.

Do not force a source surface just to make the packet look complete.

Field grade:

```text
required
```

## user_goal

Role:

State what the user is actually trying to get.

This is not just the command text. It should preserve purpose.

Caution:

Avoid turning the user's goal into an implementation permission.

Field grade:

```text
required
```

## relevant_lines

Role:

Provide only one to three space lines needed for this work.

Caution:

Do not include long line explanations or unrelated lineage.

Field grade:

```text
recommended
```

## relevant_axis

Role:

Provide one to two axes needed for judgment.

Caution:

If the axis is weak, mark it as `candidate`.

Field grade:

```text
recommended
```

## guardrails

Role:

Provide three to seven hard boundaries for this task.

Examples:

- no baseline lock
- no controller implementation
- do not confuse source surfaces
- do not auto-execute `next_move_candidate`
- do not treat PASS as proof
- do not expand external material into doctrine
- stop if file modification is required outside scope

Field grade:

```text
required
```

## memory_cards

Role:

Provide only compressed prior reflux memories needed now.

Caution:

These should be short memory cards, not full source text.

Field grade:

```text
recommended
```

## source_pointers

Role:

Provide source locations that can be opened only if needed.

Caution:

Do not paste all source contents into the task packet.

Field grade:

```text
recommended
```

## cli_role

Role:

Limit what the CLI is allowed to do in this task.

Examples:

- `draft-only`
- `verification helper`
- `implementation worker`
- `reviewer`
- `formatter`

Caution:

The role must not transfer final space judgment to the CLI.

Field grade:

```text
required
```

## expected_output

Role:

Specify what the CLI should return.

Caution:

Separate user-facing card from internal check notes.

Field grade:

```text
required
```

## stop_conditions

Role:

Tell the CLI when to stop or return HOLD.

Examples:

- source surface is uncertain
- guardrail conflict appears
- file modification is needed
- implementation pressure appears
- output would require schema/controller/runtime design

Field grade:

```text
required
```

## return_surface

Role:

Mark how the CLI result will likely re-enter the space.

Examples:

- `worker_return`
- `generated_report`
- `runtime_event`

Caution:

This is a reading expectation, not a final classification.

Field grade:

```text
recommended
```

## reflux_candidate

Role:

Predict what kind of memory the result may become after reread.

Examples:

- `note_only`
- `reuse_hint`
- `risk_memory`
- `pattern_candidate`
- `hold_signal`
- `next_move_candidate`
- `deeper_probe_needed`

Caution:

This is only a candidate. It is not automatic memory promotion.

Field grade:

```text
optional
```

## 3. field grade summary

Required:

- `request_summary`
- `source_surface`
- `user_goal`
- `guardrails`
- `cli_role`
- `expected_output`
- `stop_conditions`

Recommended:

- `relevant_lines`
- `relevant_axis`
- `memory_cards`
- `source_pointers`
- `return_surface`

Optional:

- `reflux_candidate`

Only when needed:

- detailed source excerpt
- native-vs-space comparison prompt
- expanded internal diff axes
- deeper probe question

## 4. what must not be included

Do not include:

- full conversation transcript
- full space onboarding
- all related documents
- whole old baseline
- unused philosophy explanation
- automation implementation instruction
- bridge design instruction
- schema or JSON design instruction
- sentence that gives the CLI final judgment authority

## 5. minimum packet example A. Codex worker_return check

Purpose:

Read a Codex return as `worker_return` and judge whether it can move to a next bounded step.

This is a markdown thought example, not JSON.

```text
request_summary:
Check whether this Codex return can be used as next-step material.

source_surface:
worker_return

user_goal:
Avoid treating a neat PASS or created-file list as final completion.

guardrails:
- Do not baseline lock.
- Do not treat PASS_WITH_NOTE as completion.
- Start with expected-vs-observed.
- Do not propose scripts or bridge work.
- Return HOLD if evidence is too thin.

memory_cards:
- risk_memory: PASS_WITH_NOTE can be overread as system completion.
- reuse_hint: Codex returns should be reread as worker_return.

source_pointers:
- pointer to the Codex return
- pointer to the task request

cli_role:
reviewer / draft-only

expected_output:
- 4-line user card
- internal expected-vs-observed note
- risk
- next_move_candidate if any

stop_conditions:
- expected task is unclear
- observed work cannot be tied to requested work
- result suggests baseline lock

return_surface:
worker_return

reflux_candidate:
risk_memory / reuse_hint / next_move_candidate
```

## 6. minimum packet example B. external_material_file handling

Purpose:

Read external material as bounded reference and prevent over-promotion.

This is a markdown thought example, not JSON.

```text
request_summary:
Read this external material for possible local relevance without importing it as doctrine.

source_surface:
external_material_file

user_goal:
Find what can be borrowed, what must not be borrowed, and what risk should remain.

guardrails:
- Do not turn external material into baseline.
- Do not create controller or automation proposal.
- Separate borrow from do-not-borrow.
- Keep source claims as external reference.
- Use PASS_WITH_NOTE if relevance is partial.

memory_cards:
- risk_memory: external material can be over-promoted into doctrine.
- reuse_hint: read external material as one core claim plus guardrail pointer plus borrow / do-not-borrow split.

source_pointers:
- pointer to external material
- pointer to current local flow note if needed

cli_role:
draft-only bounded reader

expected_output:
- 4-line user card
- borrow / do-not-borrow / risk / residue note

stop_conditions:
- external claim requires local structure change
- material suggests automation before local validation
- source surface becomes confused

return_surface:
worker_return

reflux_candidate:
risk_memory / reuse_hint / hold_signal
```
