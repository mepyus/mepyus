# Process Memory Operating Layer Candidate v0

## 1. Status

- status: candidate only
- source_lens: `agent-work-mem`
- use: operating-principle candidate for reusable process memory
- baseline: false
- implementation_plan: false
- automation_instruction: false
- folder_migration: false
- install_instruction: false

This document does not install `AIMemory/`, create a new memory root, replace `RUNLOG`, or promote an external protocol into VectorFL law. It records what this project can borrow from `agent-work-mem` as an operating grammar.

## 2. Reading of the external material

The useful part of `agent-work-mem` is not its folder shape. The useful part is its convention for shared working memory across changing AI sessions and agents:

- read a small entry point before reading old history
- separate current, recent, and old memory
- preserve append-only traces
- use structured handoff artifacts instead of chat-only summaries
- declare capability before accepting work
- detect unfinished work before continuing
- avoid heavy ceremony for trivial work

For VectorFL, this becomes a candidate for a Process Memory Operating Layer.

## 2.1 Current VectorFL frame

This candidate should be read against the actual ongoing work:

```text
space rereading
-> lens / camera testing
-> sandbox experiments
-> Gemini / Codex role validation
-> failure and interruption recovery
-> sandbox operating-principle rereading
-> return signals to integrated engine / line-axis / CLI attachment / process memory
```

The sandbox is not the destination. It is a small proving ground for how the larger space can be read, how workers can be bounded, and how failed or partial work can return as signal without being over-promoted.

The central question is:

```text
How can a large accumulated space of documents, records, failures, judgments,
lenses, and candidate rules be reread and reused by changing AI workers
without losing direction, overreading evidence, or depending on chat memory?
```

This is why process memory matters here. The problem exposed by restart or session loss is not only that an agent forgets a task. The deeper problem is that current position, trust point, accepted / hold / invalid state, and next allowed action were not durable enough as a first-read operating surface.

## 3. Borrow / Hold / Reject

### Borrow

- entry-point memory role
- hot / warm / cold reading temperature
- append-only correction discipline
- structured handoff type vocabulary
- capability-aware routing
- orphan / unfinished-work detection
- explicit non-goals
- convention-over-enforcement posture

### Hold

- any `AIMemory/` folder installation
- any repo-wide markdown migration
- any replacement of `RUNLOG`, runtime receipts, package records, or sandbox records
- any automatic archive / cold digest machinery
- any claim that the external protocol is a baseline

### Reject

- putting all AI-authored markdown in one new top-level folder
- granting all agents equivalent write authority
- treating `PROJECT_OVERVIEW` as the single truth document
- using the external protocol as an agent controller
- promoting every worker result, closeout, or watch item into a task

## 4. VectorFL translation

### 4.1 Entry-point memory

VectorFL needs an entry role, not necessarily an `INDEX.md` file.

The entry role should answer:

```text
Where are we?
What changed recently?
What cluster should be read?
What is baseline / candidate / watch / orphaned?
Where should older material be found?
```

This is a reading entrance, not a total archive.

Minimum current-position fields:

```text
current_position
last_trusted_point
accepted_state
hold_state
invalid_or_orphaned_state
principles_to_preserve
forbidden_moves
next_allowed_action
```

This is the smallest reboot surface. It should prevent a new CLI, Codex session, Gemini worker, or ChatGPT thread from treating the whole space as unreadable or starting from the wrong local run.

### 4.2 Memory temperature

The space should not read all markdown with equal weight.

```text
HOT:
current package, current trust point, recent invalid/orphan state, next decision point

WARM:
recent closeouts, accepted sequence, lens/camera trials, sandbox operating-principle audits

COLD:
older philosophy, harvested thought assets, old experiments, long-term external lens records
```

Temperature is an access strategy, not cleanup or deletion.

### 4.3 Append-only correction

The rule:

```text
Preserve the record.
Separate authority.
Append the correction.
```

Invalid runs, orphaned observations, voided claims, and quarantined materials should remain findable but must not become sequence evidence or baseline proof.

### 4.4 Role-aware handoff types

VectorFL should not import the external AICP vocabulary unchanged. It should use role-shaped handoff types:

```text
DESIGN_BRIEF:
ChatGPT -> Codex. Direction, lens, boundary, validation criteria.

STRUCTURE_PACKET:
Codex -> Gemini. Bounded scope, target files, output shape, forbidden moves.

OBSERVATION_REPORT:
Gemini -> Codex / ChatGPT. Evidence, uncertainty, result, watch signals.

REVIEW_RESPONSE:
Codex or ChatGPT -> User. Interpretation, risk, next possible direction.

DECISION_RELAY:
User decision, approval, rejection, hold, or direction change.

BLOCKER_RAISED:
Worker cannot continue because capability, authority, file access, or context is missing.
```

These types are vocabulary candidates, not schema.

### 4.5 Capability-aware routing

The working role split should stay explicit:

```text
Design / lens / direction -> ChatGPT
Structure / files / review / packets -> Codex
Execution / observation / long reading -> Gemini
Approval / promotion / direction change -> User
```

In the current operating posture, ChatGPT also validates Codex's structural framing before larger direction changes.

Codex token and role discipline:

```text
Codex should conserve tokens by reading narrowly, judging structurally, and preparing bounded packets.
Gemini should be the first route for long reads, repeated observation, and execution when capability allows.
Codex should execute only when Gemini is blocked, when local file changes are specifically needed, or when the user explicitly assigns execution to Codex.
```

If an agent lacks the required capability or authority, it should raise a blocker rather than improvise across role boundaries.

This routing is also a drift guard:

- ChatGPT should not collapse into tiny execution instructions when design framing is needed.
- Codex should not become the unreviewed execution worker when it is supposed to structure, review, and preserve file-level continuity.
- Gemini should not become the designer, approver, or promotion authority.
- User approval remains required for direction, promotion, and high-impact transitions.

### 4.6 Unfinished-work detection

Before continuing a package, run, pilot, or handoff, check for:

- unclosed package
- unclosed run
- invalid analysis
- missing approved artifact
- target reset needed
- hold state
- user approval gate

Unfinished work should not auto-continue. It should first be surfaced as current position.

This is the VectorFL version of orphan work detection:

```text
Do not resume merely because an artifact exists.
First classify whether it is accepted, hold, invalid, orphaned, or reference-only.
```

### 4.7 Non-goals

Do not:

- index every markdown file at once
- promote every Gemini execution into official evidence
- convert every failure into a new rule
- convert every watch item into a task
- promote every sandbox helper into a core tool
- read every closeout as baseline
- create a controller, schema, ledger, graph, ontology, or automation from this candidate

## 5. Relation to existing VectorFL records

This candidate extends these existing local patterns:

- `app/work/space-skill-sandbox/outputs/continuous_process_position_memory_rule_v0.md`
- `docs/reports/session_memory_loss_failure_analysis_pipeline_v0.md`
- `docs/reports/space_cli_memory_card_retrieval_minimum_v0.md`
- `docs/reports/interaction_contract_v0_1_operating_principles_candidate.md`
- `docs/reports/cli_side_space_operating_model_v0_1_draft.md`
- `gemini/readme.md`
- `gemini/reports/gemini_upgrade_report_20260426.md`

It should be read as a bridge between current-position memory, memory-card retrieval, role-aware handoff, and Gemini bounded-worker discipline.

The session-memory-loss analysis adds one important operational consequence: failures should enter a small pipeline before being forgotten or over-promoted.

```text
stop / hold
-> classify
-> preserve raw trace
-> separate authority
-> analyze cause
-> update next handoff
-> record current position
-> return signal to the larger direction
```

## 6. Candidate closeout

Current candidate:

```text
Process Memory Operating Layer
= entry-point memory
+ memory temperature
+ structured handoff vocabulary
+ append-only correction
+ capability-aware routing
+ unfinished-work detection
+ non-goals
```

The next useful move is not installation. The next useful move is to use this candidate as a reading lens when preparing future handoff, package, or sandbox closeout records.

One-line summary:

```text
Process memory is the operating layer that lets the space survive session loss,
worker handoff, failed runs, and partial sandbox evidence without deleting the
record or granting false authority.
```
