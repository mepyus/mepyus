# Function/Process Formation Prework Candidate v1

## 1. Purpose

Define a minimal prework unit for handling external materials, tool candidates, API candidates, function candidates, workflow claims, or agent candidates before they are attached, implemented, automated, or promoted.

This candidate exists to make prior records reusable as material for the next judgment and execution.

Key principle:

```text
Structure is not organizing records neatly.
Structure is making previous records reusable as material for the next judgment and execution.
```

This document is:

```text
CANDIDATE_REFERENCE
not baseline
not official workflow
not automation
not router/controller
not registry/index/ledger
not formal schema
not permission system
```

Revision note:

```text
v1 keeps the five-part minimum viable unit from v0.
The only structural change is adding retrieval_scope_boundary under Prior Record Retrieval, based on two dry applications.
valid_result_vs_overrun_split remains optional.
```

## 2. Why This Exists

The space already produces many useful records:

```text
external-material intake notes
Gemini execution evidence
Codex closeouts
mistake-memory
watch items
candidate signals
line / axis / lens / camera notes
process-memory-light records
```

If these records are only stored, they become archive.

If they are promoted automatically, they become unsafe.

The missing middle is a small prework unit that can:

```text
read what arrived
retrieve relevant prior records within a bounded scope
record how it was evaluated
turn the evaluation process into a reusable process asset
create retrieval/reuse hooks
return final choice to the User decision gate
```

The purpose is not feature attachment.

The purpose is to form the place where a future feature, function, tool, API, or agent could later attach.

## 3. What Is Being Structured

The object is not a specific tool, API, external material, agent, or function.

The object is:

```text
Function/Process Formation Prework Unit
```

Korean working name:

```text
기능-과정 형성 사전 단위
```

Definition:

```text
A reusable prework unit that lets the space read a possible function/tool/material, connect it to bounded prior records, convert the evaluation process into a process asset, and prepare it for future User-gated reuse.
```

This unit should preserve:

```text
what arrived
why the User brought it in
what role it might play
which prior records matter
which prior records are out of scope
what process evaluated it
what Gemini evidence or validation returned
what Codex structurally reread
what mistake-memory appeared
what watch items emerged
what line / axis / lens / camera effects appeared
what can be reused later
what still requires User decision
```

## 4. Minimum Viable Prework Unit

Use only five components for now:

```text
1. Function Candidate Card
2. Prior Record Retrieval
3. Process Asset Unit
4. Reuse Hook
5. User Decision Gate
```

Do not split these into separate systems yet.

Do not add a sixth required component.

### 4.1 Function Candidate Card

Purpose:

```text
Capture what the external material / function / tool / API / agent candidate is and what role it may play inside the space.
```

Minimum fields:

```text
candidate_name:
candidate_type:
  external_material / tool / API / function / agent / workflow / unknown
original_context:
why_user_brought_it:
possible_space_role:
  worker / lens / camera / validation_tool / memory_reuse_helper / packetizer / comparator / process_aid / operation_reference / other / reject / unknown
related_line_axis_lens_camera:
potential_acceleration_value:
risks:
current_state:
  archive / watch / candidate / test_ready / user_decision_required / hold / reject
authority_status:
  candidate only
what_must_not_be_inferred:
```

Boundary:

```text
Function Candidate Card is not a registry entry.
It does not approve the candidate.
It does not attach the function/tool/API.
```

### 4.2 Prior Record Retrieval

Purpose:

```text
Retrieve relevant prior records before evaluating a new candidate so the space does not start from zero every time.
```

The retrieval must be bounded by the current candidate's role and purpose.

Look for:

```text
related external-material intake records
previous Gemini execution / evidence records
Codex closeouts
mistake-memory
watch items
overrun / candidate signal records
line / axis / lens / camera candidate records
prior process assets
current-position or next-chat summaries when relevant
related tool/function/package records when the candidate concerns attachment
```

Minimum fields:

```text
retrieval_scope:
retrieval_scope_boundary:
  purpose:
  include:
  exclude:
  stop_condition:
  caution:
records_found:
records_not_found:
why_these_records_matter:
retrieval_uncertainty:
records_that_must_not_be_treated_as_authority:
```

`retrieval_scope_boundary` answers:

```text
What kind of prior records should be retrieved?
What should be excluded?
Which role/purpose is this retrieval serving?
When is enough retrieval enough?
What would make retrieval too broad?
```

Boundary:

```text
Prior Record Retrieval is not an automatic router.
It is a prework support step for rereading.
It does not trigger execution.
It should support the current candidate's role/purpose, not pull the whole history of the space.
The goal is enough context for structural rereading, not exhaustive archive search.
```

### 4.3 Process Asset Unit

Purpose:

```text
Record the evaluation process itself as the reusable asset.
```

The process is the asset, not just the output.

Minimum fields:

```text
trigger:
user_intent:
input_material:
prior_records_used:
roles_used:
  User / ChatGPT / Codex / Gemini / CLI
process_route:
evidence_collected:
judgments_made:
mistake_memory:
watch_items:
candidate_signals:
line_axis_lens_camera_effects:
what_can_be_reused_later:
what_requires_user_judgment:
discard_or_hold_reason_if_any:
```

Optional observation:

```text
valid_result_vs_overrun_split may be useful when a case contains both useful output and role/scope overrun, especially in Gemini execution cases, but it is not required for every Function/Process Formation Prework Unit.
```

Boundary:

```text
Process Asset Unit is not a ledger.
It is not proof that the candidate should be adopted.
It records how the space evaluated the candidate.
```

### 4.4 Reuse Hook

Purpose:

```text
Define when and how this prework record should be brought back in future work.
```

Minimum fields:

```text
reusable_when:
related_keywords:
related_user_intents:
related_line_axis_lens_camera:
retrieve_before:
  Gemini execution / Codex reread / User judgment / packet design / implementation planning / integration-engine design
reuse_value:
caution:
do_not_reuse_for:
proposal_trigger_candidate:
required_user_decision:
repeat_risk:
```

Boundary:

```text
Reuse Hook is not a router.
It does not automatically trigger execution.
It only helps future retrieval and proposal readiness.
```

### 4.5 User Decision Gate

Purpose:

```text
Preserve the User as the start and end gate.
```

Possible decisions:

```text
archive
keep_watch
form_candidate
ask_codex_to_structure
ask_gemini_to_validate
prepare_test
hold
reject
approve_later_implementation
```

Minimum fields:

```text
decision_needed_now:
safe_default:
  archive / watch / hold / process_memory_light / candidate_reference_only
what_User_may_choose_later:
what_ChatGPT_may_review:
what_Codex_may_propose_later:
what_Gemini_may_execute_later:
what_requires_explicit_User_approval:
```

Boundary:

```text
ChatGPT/Codex may propose.
Gemini may provide evidence.
But adoption, promotion, implementation, attachment, current-position update, and authority changes require User decision.
```

## 5. Operating Boundaries

Protect:

```text
User decision gate
no automatic baseline promotion
no automatic current-position update
no treating Gemini output as verified truth
no treating Codex rereading as final authority
no turning proposal readiness into hidden automation
no turning every residue into meaningful signal
no turning reuse hook into router
no turning process asset into ledger/registry
no turning candidate card into registry
no direct tool/API/function attachment from candidate usefulness
no external repo/tool/function exploration becoming automatic implementation pressure
```

Discard / hold path must remain available:

```text
not every Gemini overrun is a useful signal
not every repeated watch item is a future rule
not every candidate reference deserves reuse
not every external function should become a tool
not every process trace deserves programization
```

## 6. Program-Readiness Value

This prework matters because future program-supported processing can be faster only if the function/tool/material has already been formed inside the space.

Capture now:

```text
trigger shape
input shape
output shape
state options
role boundaries
retrieval conditions
retrieval scope boundaries
reuse hooks
human judgment gates
mistake-memory fields
watch item fields
line / axis / lens / camera effect fields
```

Semi-automatable later:

```text
prior record search suggestions
similar case retrieval
draft candidate card creation
Gemini packet draft generation
repeated watch item detection
candidate signal clustering
judgment card preparation
state validation against allowed statuses
```

Human-judgment-only:

```text
baseline promotion
current-position update
tool/API/function attachment
final adoption
official workflow creation
authority changes
meaningful line/axis creation
whether a cluster matters
whether a candidate should become a function
```

Never automate:

```text
bypassing User approval
treating Gemini as truth source
treating Codex as final authority
promoting candidates into rules without review
converting proposal readiness into adoption pressure
```

## 7. What This Is Not

```text
not automation
not controller
not router
not registry
not index
not ledger
not formal schema
not official workflow
not baseline
not source-space policy
not tool adoption plan
not API integration plan
not Gemini autonomous run system
not Codex authority expansion
```

## 8. Dry Application Basis

v1 is based on two dry applications:

```text
First dry application:
  Tools Leave Their Maker
  Verdict = FIT_CONFIRMED_WITH_NOTES
  Tested Gemini evidence, overrun, mistake-memory, and candidate signal separation.

Second dry application:
  Space External Tool Repo Attach Exploration
  Verdict = GENERALIZATION_CONFIRMED_WITH_NOTES
  Tested external tool/repo/function attachment prework.
```

Field judgment from dry applications:

```text
valid_result_vs_overrun_split = optional observation
retrieval_scope_boundary = minimal field under Prior Record Retrieval
```

## 9. Recommended Use

Use this candidate when a new external material, tool, API, function, workflow claim, or agent candidate appears and the space needs to read it before attachment.

Use it to ask:

```text
What arrived?
Why did the User bring it?
What role might it play?
Which bounded prior records matter?
What process evaluated it?
What mistake-memory or watch items appeared?
What can be reused later?
What still requires User decision?
```

Do not overfit this candidate to either dry application.

The structure should remain reusable for:

```text
future external materials
tools
APIs
functions
agents
workflow claims
validation utilities
memory reuse helpers
packetizers
comparators
operation references
```

## 10. Watch Items

```text
reuse hook becoming router
process asset becoming ledger
candidate card becoming registry
proposal readiness becoming adoption pressure
Gemini evidence becoming truth
Codex reread becoming authority
every residue being overread as signal
dry application becoming official workflow
external repo/tool/function exploration becoming automatic implementation pressure
retrieval_scope_boundary becoming broad permission to search everything
valid_result_vs_overrun_split being overused where no overrun exists
```

## 11. Do Not Do Yet

```text
do not implement automation
do not create runtime scripts
do not create queue manager
do not create registry/index/ledger
do not create formal schema
do not create official workflow
do not update current-position
do not attach tools/APIs/functions
do not promote external-material pipeline
do not make Gemini autonomous
do not make Codex final authority
do not convert proposal readiness into adoption pressure
do not create folders or persistent runtime state for this yet
do not move packages
do not approve Run 117
do not promote this candidate to baseline
do not begin implementation planning from this revision alone
```

`STATUS: FUNCTION_PROCESS_FORMATION_PREWORK_CANDIDATE_V1_PREPARED`
