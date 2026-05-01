# Formation-Movement Interface Package Draft v0

Date: 2026-04-24

Status: `package_candidate` / `PASS_WITH_NOTE-ready`

## 0. no-lock warning

This package is a draft, not a baseline lock.

Do not read this document as:

- final ontology lock
- final schema
- implementation directive
- runtime manifest contract
- promotion rule
- UI requirement

Read it as:

- a package candidate for operating the interface between the formation layer and the movement layer
- a guard against premature promotion
- a practical grammar for provisional objects, sidecars, lifecycle transitions, and validation returns

## 1. purpose

This package defines how provisional objects formed in the formation layer can move into the movement layer and return to the formation layer without being mistaken for final conclusions.

The package exists to preserve:

- intermediate layer
- reread value
- provisional status
- boundary clarity
- validation-return loops
- process residue

Core sentence:

> The formation-movement interface does not export finished conclusions. It grants conditional movement qualification to provisional objects for a current purpose.

## 2. body premise

The system has two bodies, not one.

### Identity body

`space + VectorFL formation layer`

Role:

- preserves reread
- forms intermediate objects
- keeps provisional states alive
- prevents the system from collapsing into ordinary agent orchestration
- carries detours, residue, and memory assets

### Movement body

`engine surface centered movement layer`

Role:

- performs worker handoff
- executes bounded work
- manages expected return, fallback, trust scope, and validation return
- returns movement results as material for further formation

Compressed rule:

> The formation layer makes the system identifiable. The movement layer actualizes that identity as current work.

## 3. three organs

The user surface, VectorFL surface, and engine surface are not just UI tabs. They are operating organs.

### User surface = access organ

Primary work:

- opens the current purpose
- reveals user request and center of gravity
- sets desired output surface
- gives the work its why-now

Core question:

> Why should this system move now?

### VectorFL surface = formation organ

Primary work:

- rereads space traces and current request
- forms intermediate objects
- reads candidate / hold / line / axis / frame
- judges what is still unripe and what can move
- translates between user language and engine language

Core question:

> What is this becoming now?

### Engine surface = movement organ

Primary work:

- converts formed objects into executable units
- performs worker handoff
- manages contract, expected return, fallback, and trust scope
- receives and returns validation material

Core question:

> Under what constraints can this move?

## 4. formation-layer minimum unit

There are two minimum units.

### Ontological minimum

```text
space + VectorFL
```

Reason:

- space alone is a field that holds traces and provisional states
- VectorFL is required to reread those traces and form them as intermediate objects

### Operational minimum

```text
user surface + space + VectorFL
```

Reason:

- actual work needs a current purpose and direction
- the user surface acts as the access aperture for now-this work

Compressed form:

```text
space = field
VectorFL = formation organ
user surface = access aperture
```

## 5. interface conditions

The boundary between the formation layer and movement layer is not a finished/unfinished line.

A provisional object may move only when the following are explicit enough:

- purpose fit: it connects to the current user purpose
- boundary clarity: inclusion and exclusion are visible
- provisional visibility: partial / candidate / hold / note status can remain visible
- misunderstanding control: the next layer should not mistake it for final or promoted truth
- reread return: the result can return to formation for rereading

Core test:

> Is this complete? is the wrong question. Can this move boundedly? is the right question.

## 6. provisional object families

### 6.1 `reread_priority`

Meaning:

An object that should remain inside the formation layer for more reading.

Signals:

- meaningful but boundary is unclear
- weak or unstable connection to current purpose
- subtype / family / role location is unsettled
- sending it forward would force the engine or worker to interpret too much

Examples:

- useful-looking external reference
- material that may be line seed or camera support but is not yet clear
- concept that becomes flat when explained too early

Default move:

```text
next_allowed_move: reread_only
```

### 6.2 `framing_candidate`

Meaning:

An object that has begun to connect to the current purpose but is not yet an action packet.

Signals:

- role candidate is visible
- can serve as comparison frame, principle candidate, or question-set candidate
- promotion or execution is still too early

Examples:

- A as upper precedence principle candidate
- B as spatial organization axis candidate
- T as ripeness ontology candidate
- external reference as B comparison frame candidate

Default move:

```text
next_allowed_move: compare_only
```

### 6.3 `bounded_action_candidate`

Meaning:

A non-final object that can move as a limited action for the current purpose.

Signals:

- actionable question exists
- boundary exists
- expected return form exists
- return hook exists
- guardrail can be attached

Examples:

- Codex one-shot draft
- external reference comparison report task
- three user-surface explanation comparison test
- sidecar minimum-core review package

Default move:

```text
next_allowed_move: prepare_worker_packet
```

### 6.4 `guarded_execution`

Meaning:

An executable object that enters the movement layer with constraints and guardrails.

Signals:

- dry-run / preview / read-only / report-draft-only constraint
- fallback policy exists
- trust scope is limited
- execution result must not be mistaken for promotion

Examples:

- hybrid contract dry-run
- worker-emitted JSON block trial
- Codex report draft only task
- bounded test with no-main-merge condition

Default move:

```text
next_allowed_move: run_bounded_test
```

### 6.5 `validation_return`

Meaning:

A movement-layer return that becomes input for the next formation loop. It is not final by default.

Signals:

- observed result exists
- deviation from expected return is visible
- reread trigger exists
- refinement target exists

Examples:

- Codex result report
- dry-run result
- worker return block
- failed user-surface explanation case
- sidecar policy trial result

Default move:

```text
next_allowed_move: refine / hold / downgrade / archive_as_residue / promote
```

## 7. lifecycle

The lifecycle is not a promotion staircase.

Default flow:

```text
access occurs
-> formation capture
-> reread_priority
-> framing_candidate
-> bounded_action_candidate
-> guarded_execution
-> validation_return
-> refine / hold / downgrade / archive_as_residue / promote
-> return to formation layer
```

Important rule:

> Not every object wants promotion. Refine, hold, downgrade, and residue are normal lifecycle branches.

## 8. transition rules

### 8.1 `reread_priority -> framing_candidate`

Required condition:

```text
repeated_signal
+ current_purpose_connection
+ candidate_role
+ promotion_barrier
```

Meaning:

The object has enough repeated signal and purpose connection to become a candidate frame, but it still needs a clear barrier against promotion.

### 8.2 `framing_candidate -> bounded_action_candidate`

Required condition:

```text
actionable_question
+ boundary
+ expected_return_form
+ return_hook
```

Meaning:

The object can now become a bounded action because a concrete question, boundary, return form, and return path exist.

### 8.3 `bounded_action_candidate -> guarded_execution`

Required condition:

```text
execution_constraint
+ guardrail
+ fallback_policy
+ trust_scope
```

Meaning:

The object can now enter the movement layer only under explicit execution constraints.

### 8.4 `guarded_execution -> validation_return`

Required condition:

```text
observed_result
+ deviation_from_expected
+ reread_trigger
```

Meaning:

Execution has produced material that can be reread, not just accepted.

## 9. validation-return branches

### 9.1 refine

Use when:

- direction remains valid
- correction target is clear
- result does not require full rejection

Examples:

- core direction is right but boundary is weak
- user-facing explanation works but residue is too thin
- JSON contract is useful but missing-field policy is weak

### 9.2 hold

Use when:

- meaning exists
- further movement is risky
- repeated evidence is weak
- T/ripeness is still low

Examples:

- promising but lacks internal reread evidence
- structuring now would flatten the concept
- has not yet been tested across other scenes

### 9.3 downgrade

Use when:

- previous state classification was too high
- the object needed earlier formation work
- boundary was actually unclear
- worker over-interpreted the task

Examples:

- sent as bounded action but should have stayed reread-first
- Codex widened the scope
- expected return form did not hold

### 9.4 archive as residue

Use when:

- not useful for current purpose
- future reread value remains
- failure or detour is diagnostically useful

Examples:

- wrong explanation that becomes an L-failure case
- failed Codex instruction that reveals boundary drift
- currently irrelevant reference that may later become contrast material

### 9.5 promote / lock

Use only when there is strong evidence for:

- repetition
- explanatory force
- relocation force
- boundary clarity
- counterexample handling
- reopen condition

Promotion is not the default route. It is an exception after repetition and validation.

## 10. sidecar metadata

Sidecar metadata is not a heavy schema. It is a small surface that keeps provisionality, movement, and return possible.

### Core 7

```text
object_type
current_purpose
boundary
provisional_status
next_allowed_move
reread_return_hook
source_trace
```

Meanings:

| field | role |
| --- | --- |
| `object_type` | What kind of provisional object this is. |
| `current_purpose` | Why this object is being handled now. |
| `boundary` | What is included and excluded. |
| `provisional_status` | What kind of non-final state this object has. |
| `next_allowed_move` | What may happen next. |
| `reread_return_hook` | Where and how the object should return for rereading. |
| `source_trace` | Where this object came from. |

### Strong optional fields by type

`reread_priority`:

```text
needed_reread_question
instability_reason
```

`framing_candidate`:

```text
candidate_role
promotion_barrier
```

`bounded_action_candidate`:

```text
action_shape
guardrail
expected_return_form
```

`guarded_execution`:

```text
execution_constraint
fallback_policy
trust_scope
```

`validation_return`:

```text
observed_result
deviation_from_expected
reread_trigger
refinement_target
updated_trust_scope
```

## 11. metadata assignment by surface

Metadata should accumulate across surfaces. One actor should not have to fill everything.

### User surface

Usually adds:

```text
current_purpose
why_now
desired_output_surface
initial_boundary
```

Role:

Opens why this object matters now.

### VectorFL surface

Usually adds:

```text
object_type
provisional_status
candidate_role
needed_reread_question
instability_reason
next_allowed_move draft
residue/source_trace draft
```

Role:

Judges what the object is becoming.

### Engine surface

Usually adds:

```text
action_shape
execution_constraint
guardrail
expected_return_form
fallback_policy
trust_scope
```

Role:

Defines how the object may move under constraints.

### Return / validation moment

Usually adds or updates:

```text
observed_result
deviation_from_expected
reread_trigger
refinement_target
updated_provisional_status
updated_trust_scope
```

Role:

Reads what the result demands from the next formation loop.

## 12. physical sidecar principles

Do not force one physical form for all objects.

Core principle:

```text
Markdown-first
JSON-when-motion
Log-on-transition
```

### Markdown-first

Best for:

- `reread_priority`
- `framing_candidate`
- early `bounded_action_candidate`

Forms:

- markdown header
- structured markdown block
- `.sidecar.md`

Reason:

- human-readable
- tolerates low ripeness
- avoids premature schema force

### JSON-when-motion

Best for:

- `bounded_action_candidate`
- `guarded_execution`
- worker handoff object
- runtime tracking object

Forms:

- `.sidecar.json`
- handoff packet
- runtime manifest
- worker return block

Reason:

- field consistency matters during movement
- expected return, fallback, and trust scope need structure

### Log-on-transition

Required when:

- `object_type` changes
- `provisional_status` changes
- `next_allowed_move` changes
- validation return branches
- hold / downgrade / promote decisions occur

Reason:

The later reread needs to know why the state changed.

## 13. sidecar families

### Formation sidecar

Used inside formation layer.

Targets:

- `reread_priority`
- `framing_candidate`

Forms:

- `.sidecar.md`
- markdown header
- structured markdown block

### Handoff sidecar

Used at movement entry.

Targets:

- `bounded_action_candidate`
- `guarded_execution`

Forms:

- `.sidecar.json`
- handoff packet
- runtime manifest preview

### Return sidecar

Used when movement returns.

Targets:

- `validation_return`

Forms:

- worker return block
- validation report
- sidecar update
- transition log

## 14. minimal templates

### 14.1 formation sidecar markdown template

```markdown
---
object_type: reread_priority | framing_candidate | bounded_action_candidate
current_purpose:
boundary:
provisional_status:
next_allowed_move:
reread_return_hook:
source_trace:
---

## type-specific notes

needed_reread_question:
instability_reason:
candidate_role:
promotion_barrier:
action_shape:
guardrail:
expected_return_form:
```

### 14.2 handoff sidecar JSON template

```json
{
  "object_type": "bounded_action_candidate",
  "current_purpose": "",
  "boundary": "",
  "provisional_status": "PASS_WITH_NOTE-ready",
  "next_allowed_move": "prepare_worker_packet",
  "reread_return_hook": "",
  "source_trace": [],
  "action_shape": "",
  "guardrail": "",
  "expected_return_form": "",
  "execution_constraint": "",
  "fallback_policy": "",
  "trust_scope": ""
}
```

### 14.3 return sidecar template

```text
object_type: validation_return
current_purpose:
boundary:
provisional_status:
next_allowed_move:
reread_return_hook:
source_trace:

observed_result:
deviation_from_expected:
reread_trigger:
refinement_target:
updated_trust_scope:
branch: refine | hold | downgrade | archive_as_residue | promote
```

## 15. sample: external reference ingest

Situation:

An external reference says that multi-agent systems create confusion when agents are left too free, so each agent needs clear roles, boundaries, and return formats.

Initial temptation:

Promote it as evidence for B.

Correct handling:

Do not promote directly. Run it through the provisional lifecycle.

### Step 1. `reread_priority`

```text
object_type: reread_priority
current_purpose: judge whether the external reference strengthens B
boundary: no promotion; no B lock; role/location judgment only
provisional_status: still_forming
next_allowed_move: reread_only
reread_return_hook: reread relation to B/A/C on VectorFL surface
source_trace: external_reference_ingest_sample
needed_reread_question: Is this direct evidence for B, or defensive logic that protects B?
instability_reason: anti-agent freedom and role-bearing organization are not yet separated
```

### Step 2. `framing_candidate`

```text
object_type: framing_candidate
current_purpose: use as external comparison frame for B candidate
boundary: no B lock; compare relation to A/C only
provisional_status: candidate
next_allowed_move: compare_only
reread_return_hook: compare against internal CLI/external tool attachment scenes
source_trace: external_reference_ingest_sample
candidate_role: role-bound external worker comparison frame
promotion_barrier: cannot become axis evidence until internal failure/bottleneck records show explanatory and relocation force
```

### Step 3. `bounded_action_candidate`

```text
object_type: bounded_action_candidate
current_purpose: check explanatory force of B in internal CLI/external tool attachment records
boundary: no B lock; compare only three internal records; no promotion judgment
provisional_status: PASS_WITH_NOTE-ready
next_allowed_move: prepare_worker_packet
reread_return_hook: return as validation_return_object for B/A/C relation reread
source_trace: external_reference_ingest_sample + prior B analysis
action_shape: comparative reread report
guardrail: no axis promotion; no baseline update; report draft only
expected_return_form: verdict + compared scenes + B evidence + A/C overlap + unresolved questions
```

### Step 4. `guarded_execution`

```text
object_type: guarded_execution
current_purpose: generate bounded internal comparison report for B candidate
boundary: create report draft only; no baseline/main change
provisional_status: bounded_only
next_allowed_move: run_bounded_test
reread_return_hook: reread created report as validation_return_object on VectorFL surface
source_trace: external_reference_ingest_sample + sidecar lifecycle discussion
action_shape: one-shot instruction
execution_constraint: read_and_report_only
guardrail: no promotion; no operating rule creation; no schema lock
expected_return_form: verdict + created files + evidence table + unresolved risks
fallback_policy: return PASS_WITH_NOTE or INSUFFICIENT_EVIDENCE if internal material is weak
trust_scope: local comparison only; not promotable
```

### Step 5. `validation_return`

```text
object_type: validation_return
current_purpose: reread internal explanatory-force comparison for B candidate
boundary: no B lock; judge only position and limit
provisional_status: PASS_WITH_NOTE
next_allowed_move: refine_B_boundary
reread_return_hook: keep B as spatial organization axis candidate while preserving relation to T/X/R/L
source_trace: guarded_execution_report_on_B
observed_result: B is strong in CLI/external tool attachment scenes but does not cover user-facing explanation or maturation/validation scenes
deviation_from_expected: B was stronger than expected, but not central in L/R/T scenes
reread_trigger: over-expanding B may absorb other candidates
refinement_target: define B as boundary-surface/role-organization principle; separate anti-agent freedom suppression as defensive logic
updated_trust_scope: reusable as package candidate, not locked as axis
branch: refine
```

Sample result:

- external reference is not action material at first contact
- it starts as `reread_priority`
- it may become `framing_candidate`
- it becomes `bounded_action_candidate` only after action question, boundary, expected return, and return hook exist
- execution result returns as `validation_return`, not final
- natural branch is `refine`, not `promote`

## 16. operating guardrails

### Guardrail 1. prevent sidecar overload

Rule:

- keep Core 7 stable
- use type-specific optional fields only when needed
- avoid detailed residue fields unless reread value is concrete

### Guardrail 2. avoid object-type bureaucracy

Rule:

- `object_type` may change
- downgrade and refine are normal
- object-type changes require transition log

### Guardrail 3. avoid premature JSON

Rule:

- markdown-first in formation layer
- JSON only when movement requires field consistency
- runtime manifest is movement-state tracking, not formation-layer SSOT

### Guardrail 4. never treat validation return as final by default

Rule:

- validation return must include `reread_trigger` and `refinement_target`
- observed-result-only reports are incomplete

### Guardrail 5. do not push metadata burden back to the user

Rule:

- user surface opens `current_purpose` / `why_now`
- VectorFL assigns `object_type` / `status` / `next_allowed_move`
- engine or worker returns `observed_result` and deviation material

## 17. relation to nearby documents

This package sits above the earlier short note and below any future implementation.

Related documents:

- `docs/reports/formation_layer_provisional_object_metadata_note_v0.md`
- `docs/reports/integrated_engine_transfer_packet_minimum_slots_v0.md`

Layer split:

- provisional object package = formation-to-movement qualification grammar
- transfer packet minimum slots = carrier grammar across surfaces
- worker return contract = normalized movement-layer return
- implementation/runtime manifest = later materialization only

Do not collapse these layers too early.

## 18. open questions

- Which Core 7 fields must appear in the UI, and which should remain hidden in sidecars/logs?
- Should `reread_priority` and `framing_candidate` have separate visual badges?
- Should C/D interface objects become transfer packets directly, or should there be a separate conversion step?
- What is the smallest transition log entry that preserves reread value without becoming heavy bureaucracy?
- Should user-facing explanation tests be treated as `bounded_action_candidate` or as a separate explanation-surface subtype?
- How should `ripeness` relate to `provisional_status` without forcing a numeric maturity scale too early?

## 19. current package state

If this package is itself treated as a provisional object:

```text
object_type: bounded_action_candidate
current_purpose: draft a formation-movement interface operating package
boundary: document package only; no baseline lock; no schema force; no implementation
provisional_status: PASS_WITH_NOTE-ready
next_allowed_move: apply_to_1_or_2_cases_for_validation_return
reread_return_hook: reread package after sample application and update transition/sidecar rules
source_trace: current conversation deep analysis + formation_layer_provisional_object_metadata_note_v0
action_shape: package draft
guardrail: no implementation; no schema lock; no baseline promotion
expected_return_form: package draft + minimal sidecar template + lifecycle + transition rules + open questions
```

## 20. final compression

The formation-movement interface package is a package candidate for moving provisional objects from the `space + VectorFL` formation layer into the engine-centered movement layer and then recovering them as validation returns. Its center is the provisional object family, Core 7 sidecar metadata, markdown-first / JSON-when-motion / log-on-transition physical principle, lifecycle transition rules, and post-return branching grammar.

## 21. addendum: sidecar maturity and visibility corrections

Status: small correction note. This addendum does not change the package status, does not promote the package to baseline, and does not create a schema or implementation requirement.

### 21.1 sidecar maturity levels

A sidecar is not born as a complete schema. It matures with the provisional object.

Maturity levels:

```text
seed sidecar
-> formed sidecar
-> motion sidecar
-> return sidecar
-> refined sidecar
```

Reading:

- `seed sidecar`: only enough context exists to avoid losing the object.
- `formed sidecar`: the object has a provisional status, rough boundary, and candidate reading.
- `motion sidecar`: the object is close enough to movement that expected return, guardrail, and handoff shape matter.
- `return sidecar`: the movement result has returned and must be reread.
- `refined sidecar`: the return has updated object status, trust scope, or next move.

Correction:

The Core 7 fields are a lifecycle completeness target, not a forced creation-time input form.

### 21.2 logical core vs operational minimum

Logical Core 7:

```text
object_type
current_purpose
boundary
provisional_status
next_allowed_move
reread_return_hook
source_trace
```

Operational minimum at creation:

```text
current_purpose
source_trace
initial_boundary or why_now
```

Creation rule:

- `object_type` may be omitted at seed stage.
- `object_type` may be `unclassified` at seed stage.
- exact object typing should happen only when the VectorFL surface has enough formation evidence.

This prevents early sidecar creation from becoming premature classification.

### 21.3 surface-specific visibility

Do not expose all sidecar information equally on every surface.

User Surface should mainly expose:

```text
current judgment
reason
next move
guardrail
```

VectorFL Surface may expose the full formation sidecar:

```text
object_type
provisional_status
reread questions
candidate role
promotion barrier
source/residue trace
```

Engine Surface should mainly expose movement fields:

```text
action_shape
execution_constraint
guardrail
expected_return_form
fallback_policy
trust_scope
```

Return / Validation Surface should mainly expose return-reading fields:

```text
observed_result
deviation
reread_trigger
recommended branch
refinement_target
```

Correction:

Surface-specific projection is part of the package. A sidecar can be shared as underlying material without becoming the same visible object on every surface.

### 21.4 prepare vs execute distinction

`next_allowed_move` is not immediate permission to execute.

Split:

```text
allowed_to_prepare
allowed_to_execute
```

Rule:

- `prepare_worker_packet` means preparation, not execution.
- Preparation may gather boundary, expected return, and candidate handoff shape.
- Execution requires `execution_constraint`, `guardrail`, `fallback_policy`, and `trust_scope`.

Therefore:

```text
bounded_action_candidate
-> allowed_to_prepare: yes
-> allowed_to_execute: no, unless guarded_execution fields are present
```

This prevents a bounded action candidate from being treated as a ready-to-run object too early.

### 21.5 short vs full validation return

Do not require a full validation return every time.

Short validation return:

```text
observed_result
reread_trigger
next_recommended_state
```

Use when:

- movement was small
- deviation analysis is not yet worth the cost
- the next step is obvious enough for formation reread

Full validation return:

```text
observed_result
deviation_from_expected
reread_trigger
refinement_target
updated_trust_scope
updated_next_allowed_move
```

Use when:

- the return may alter object type or trust scope
- downgrade / hold / promote is possible
- future reread would lose value without explicit deviation and refinement notes

Correction:

Validation return must prevent finalization drift, but it should not become an unnecessarily heavy report requirement for every small movement.

### 21.6 added guardrails

- Do not turn sidecar into a user input form.
- Do not ask the user to fill the full Core 7.
- Do not force `object_type` at seed stage.
- Do not read prepare-ready as execute-ready.
- Do not require full validation return when short validation return is enough.

## 22. addendum unresolved questions

- What should the default `unclassified` seed sidecar look like in markdown?
- When exactly should `object_type` become required: at `formed sidecar`, at `motion sidecar`, or only before handoff?
- Should `allowed_to_prepare` and `allowed_to_execute` be explicit fields, or inferred from `next_allowed_move` and guarded execution fields?
- What is the smallest UI projection for User Surface that still preserves guardrail visibility?
- When should short validation return be auto-upgraded to full validation return?

## 23. validation-informed clarifications from Codex one-shot dry-run

Status: clarification after Codex one-shot validation case. This section reflects `docs/reports/formation_movement_interface_codex_oneshot_validation_case_v0.md`.

Validation source:

- The validation case verdict was `PASS_WITH_NOTE`.
- The dry-run showed that the package can keep user input near three fields, keep `object_type` assignment on the VectorFL surface, and separate prepare from execute.
- This patch is a package-candidate reinforcement, not package finalization, baseline lock, schema enforcement, implementation, or runtime-manifest creation.

### 23.1 unclassified seed sidecar minimum

At seed sidecar stage, do not force `object_type`.

Rules:

- `object_type` may be omitted.
- `object_type` may be `unclassified`.
- The seed sidecar operational minimum remains three fields:
  - `current_purpose`
  - `source_trace`
  - `initial_boundary` or `why_now`
- The user does not choose `object_type`.
- The VectorFL surface attaches `object_type` at the formed sidecar stage after enough reread.

Example:

```yaml
current_purpose: Codex one-shot 지시서 초안 준비
source_trace: current user request / supervisor discussion
initial_boundary: execute 금지, prepare_worker_packet까지만 허용
object_type: unclassified
```

Clarifications:

- `object_type: unclassified` is a temporary seed-state marker, not a Core 7 expansion.
- `unclassified` means the object has not yet reached formed sidecar status.
- An `unclassified` seed cannot move directly to execution.

### 23.2 prepare vs execute field policy

Do not add `allowed_to_prepare` or `allowed_to_execute` to Core 7.

Instead, read them as interpretation categories under `next_allowed_move`.

Useful categories:

```text
allowed_to_reread
allowed_to_compare
allowed_to_prepare
allowed_to_execute
allowed_to_archive
```

Principles:

- `allowed_to_prepare` is not execution permission.
- `prepare_worker_packet` means a worker packet may be prepared, not run.
- `allowed_to_execute` requires at least:
  - `execution_constraint`
  - `guardrail`
  - `fallback_policy`
  - `trust_scope`
  - `expected_return_form`
  - `reread_return_hook`

This preserves the Core 7 while making execution readiness harder to over-read.

### 23.3 when a one-shot draft becomes guarded_execution

A Codex one-shot draft is normally a `bounded_action_candidate` in `allowed_to_prepare` state.

It is not `guarded_execution` until all of the following are explicit:

- actual execution scope is clear
- `execution_constraint` exists
- `guardrail` exists
- `fallback_policy` exists
- `trust_scope` exists
- `expected_return_form` exists
- the result has a hook back into `validation_return`

Additional rule:

- Do not promote prepare state to execute state without user approval or supervisor judgment.

Required sentence:

> `prepare_worker_packet` is not execution. A one-shot draft becomes `guarded_execution` only after execution constraints and return conditions are explicitly attached.

Korean equivalent:

> `prepare_worker_packet`은 실행이 아니다. one-shot 초안은 execution constraint와 return 조건이 명시적으로 붙은 뒤에만 `guarded_execution`이 된다.

### 23.4 trust scope at prepare stage

`trust_scope` is strongly required at `guarded_execution` stage.

At prepare stage:

- Do not force `trust_scope` as a required field.
- If risk is high, use optional `draft_trust_scope` or `trust_scope_note`.
- This is not a Core 7 expansion.

Example:

```yaml
trust_scope_note: prepare-only, not executable, not promotable
```

Cost rule:

- Forcing `trust_scope` too early can increase operator cost.
- In many prepare-stage cases, a boundary or guardrail sentence saying `not executable / not promotable` is enough.

### 23.5 short validation return to full validation return triggers

Short validation return can be enough for low-risk dry-runs or small movement.

Short form:

```text
observed_result
reread_trigger
next_recommended_state
```

Upgrade to full validation return if any of the following appear:

- promotion risk
- baseline risk
- schema enforcement risk
- runtime coupling risk
- worker crosses the boundary
- actual result differs substantially from `expected_return_form`
- `trust_scope` becomes unstable
- return is unclear enough that the user must reinterpret or recover it
- User Surface risks losing residue or flattening the result
- `object_type` change, downgrade, hold, or residue decision is needed

Full validation return fields:

```text
observed_result
deviation_from_expected
reread_trigger
refinement_target
updated_trust_scope
updated_next_allowed_move
```

### 23.6 clarified guardrails

- Do not force `object_type` at seed sidecar stage.
- An `unclassified` seed cannot move directly to execution.
- Do not read `allowed_to_prepare` as `allowed_to_execute`.
- `prepare_worker_packet` is not execution.
- A one-shot draft remains `bounded_action_candidate` until guarded execution conditions are met.
- `trust_scope` is required for `guarded_execution`, but can remain an optional note during preparation.
- Short validation return is allowed only for low-risk cases.
- Promotion, baseline, schema, runtime, or boundary-drift risk requires full validation return.
- Do not add new fields to Core 7.
- This clarification exists to reduce operator cost, not to make the package heavier.

### 23.7 updated unresolved questions

- Is `unclassified` seed sidecar sufficient after repeated use?
- Is keeping `allowed_to_prepare` / `allowed_to_execute` as `next_allowed_move` interpretation enough?
- Is optional `trust_scope_note` enough at prepare stage?
- Are the short-to-full validation triggers too broad in real use?
- Does the one-shot draft become `guarded_execution` through user approval, supervisor judgment, or both?

## 24. validation-informed clarifications from external reference ingest dry-run

Status: clarification after external reference ingest validation case. This section reflects `docs/reports/formation_movement_interface_external_reference_ingest_validation_case_v0.md`.

Validation source:

- The validation case verdict was `PASS_WITH_NOTE`.
- The dry-run showed that external reference ingest can keep user input near three fields, leave `object_type` assignment to the VectorFL surface, avoid Core 7 burden, and block B promotion.
- This patch is a package-candidate reinforcement, not package finalization, baseline lock, schema enforcement, implementation, runtime-manifest creation, external reference movement, or B promotion.
- The clarification exists to reduce operator cost and premature promotion risk in external reference ingest.

### 24.1 when an external reference should remain reread_priority

An external reference can look useful without being ready for `framing_candidate`.

Keep the object as `reread_priority` when:

- the reference touches an internal candidate but its role is unclear
- it is unclear whether the reference is direct evidence, defensive logic, or comparison frame
- A/C/T/X/R/L overlap is strong enough that the main lens is unclear
- current-purpose connection exists, but `candidate_role` is not yet stable
- promotion risk is high
- internal records have not yet shown explanatory force or relocation force
- user-facing explanation would flatten the reference
- it is unclear whether the reference is seed, support, or camera reinforcement

Principles:

- A B-adjacent reference is not B evidence by default.
- First treat it as `reread_priority` or `framing_candidate` candidate.
- B promotion is forbidden at this stage.
- Touching B may mean only that relation checking is needed.

### 24.2 direct evidence / defensive logic / comparison frame

When an external reference touches a candidate, read it through at least three possible roles.

#### A. direct evidence

Definition:

- The external reference directly reinforces a pattern already repeated in internal records.
- It connects to existing internal explanatory force or relocation force.
- The same structure survives across multiple internal scenes, not one isolated scene.

Boundary:

- Direct evidence requires internal reread.
- Do not classify an external reference alone as direct evidence.

#### B. defensive logic

Definition:

- The reference does not prove the principle itself.
- It explains why the principle may be needed or what risk it protects against.
- Example: universal agent freedom is risky, so role boundaries are needed.

Boundary:

- Defensive logic can protect B without becoming B's body.
- Do not promote defensive logic directly into axis evidence.

#### C. comparison frame

Definition:

- The reference is useful as a lens for rereading internal records.
- It is not direct evidence by itself.
- It can help compare scenes such as CLI/external-tool attachment against role-bound worker logic.

Boundary:

- A comparison frame can lead to `bounded_action_candidate`.
- It does not justify lock or promotion by itself.

### 24.3 B-adjacent reference handling rule

B-adjacent reference means a reference that touches the boundary-surface / role-organization principle.

Core rules:

- A B-adjacent reference is not B confirmation evidence by default.
- First classify it as one of:
  - `reread_priority`
  - `defensive_logic_candidate`
  - `comparison_frame_candidate`
  - `framing_candidate`
- Separate B's body from anti-agent-freedom defensive logic.
- Role-bound external worker logic can support B, but it does not replace or confirm B.

Questions:

- Does this reference describe B's body?
- Or does it defend why B is needed?
- Or does it provide a frame for comparing internal CLI/external-tool scenes?
- Is A/C/T/X/R/L overlap stronger than B?
- Would reading this as B absorb other candidates too early?

### 24.4 conditions for framing_candidate elevation

An external reference may move from `reread_priority` toward `framing_candidate` only when:

- it connects to the current purpose
- `candidate_role` can be attached
- `promotion_barrier` can be stated
- its temporary role can be named as direct evidence, defensive logic, or comparison frame
- there is an explicit rule against promotion before internal reread

Example:

```yaml
object_type: framing_candidate
candidate_role: role-bound external worker comparison frame
promotion_barrier: 내부 CLI/외부도구 부착 기록에서 설명력과 재배치력을 확인하기 전까지 B 증거로 승격 불가
next_allowed_move: compare_only
```

Clarification:

- `framing_candidate` does not mean evidence.
- `compare_only` means the reference may organize reread, not decide the result.

### 24.5 B-adjacent comparison short/full validation trigger

Short validation return may be enough when:

- no execution occurred
- no promotion occurred
- no baseline changed
- no schema changed
- the comparison is a simple dry-run
- `trust_scope` did not change
- `object_type` did not change

Use full validation return when:

- B `trust_scope` changes
- B promotion risk appears
- the reference may be read as axis evidence
- A/C/T/X/R/L overlap requires hold or downgrade
- the object enters action while direct evidence / defensive logic / comparison frame remains unclear
- internal reread changes the B boundary
- User Surface loses residue or flattens the reference
- actual result differs substantially from `expected_return_form`
- `object_type` change is required
- a decision is needed about moving from `bounded_action_candidate` to `guarded_execution`

### 24.6 hold conditions for A/C/T/X/R/L overlap

Even when a reference touches B, prefer hold or `reread_priority` when:

- A and B are both strong, making precedence principle and organization axis hard to separate
- C/T are stronger, suggesting maturation, validation, or provisionality is the real issue
- X is stronger, suggesting translation or transformation structure is the real issue
- R is stronger, suggesting process residue or memory asset handling is more appropriate
- L is stronger, suggesting viewpoint or lens shift is required
- one reference tries to absorb too many candidates at once
- explanatory force or relocation force cannot be judged before comparison with at least two internal records

This prevents a B-adjacent reference from becoming a vacuum that absorbs A/C/T/X/R/L.

### 24.7 clarified guardrails

- An external reference is not evidence at first contact.
- A B-adjacent reference is not B promotion ground.
- Do not promote before distinguishing direct evidence, defensive logic, and comparison frame.
- Do not over-promote defensive logic into axis evidence.
- A comparison frame can enable bounded reread, not lock.
- If A/C/T/X/R/L overlap is strong, prefer `reread_priority` or hold over `framing_candidate`.
- If B-adjacent comparison changes B `trust_scope`, use full validation return.
- External reference to operating rule promotion requires a separate promotion gate.
- This clarification does not change Core 7 or the five object families.

### 24.8 updated unresolved questions

- Is `unclassified` seed enough for weak external references?
- Should B-adjacent references default to `reread_priority` before `framing_candidate`?
- Are direct evidence / defensive logic / comparison frame boundaries clear enough under repeated use?
- Should A/C/T/X/R/L overlap hold conditions be made more concrete?
- What should be the default short/full validation setting for B-adjacent comparison?
- How many internal records must be reread before direct evidence can be claimed?
