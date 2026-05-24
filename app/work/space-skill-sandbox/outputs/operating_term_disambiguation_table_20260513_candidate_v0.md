# Operating Term Disambiguation Table
# 2026-05-13 Candidate v0

## 1. Status

Document:
  candidate term disambiguation table

Authority:
  orientation / clarification only

Not:
  glossary authority
  ontology
  schema
  registry
  baseline
  workflow

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH

## 2. Purpose

Separate recurring terms by operating layer so Codex, Gemini, ChatGPT, and User do not collapse different meanings into one.

## 3. Term Table

## Term: Pipeline

Core distinction:
  Pipeline names a flow shape, not a single fixed meaning.
  Its meaning depends on the layer, Camera, and Lens used to read it.

Meaning Layer:
  thought / judgment transformation flow

Principle Layer:
  not a fixed workflow unless explicitly approved

Structure Layer:
  packet / cycle / request queue connection

Execution Layer:
  Gemini task bundle or observation route

Recovery Layer:
  raw return -> recovered judgment -> placement flow

Re-entry Layer:
  next usable path shown thinly

Do Not:
  use one pipeline meaning for all layers

Watch:
  pipeline becoming workflow by accident

### Thought Flow Pipeline

Layer:
  Meaning Layer

Meaning:
  the movement of user thought, judgment, hesitation, correction, and reinterpretation over time

Used for:
  reading how an idea changes and becomes recoverable judgment

Do Not Use As:
  execution workflow
  file routing path
  automation chain

Watch:
  thought flow must not be flattened into process steps

### Relay Pipeline

Layer:
  Structure Layer / Execution Support Layer

Meaning:
  the manual file-based movement between ChatGPT, Codex, Gemini, and User

Used for:
  packet paths, cycle work orders, request queues, supervisor checkpoints

Do Not Use As:
  automation
  tool authority
  final workflow

Watch:
  relay path must not make User a relay worker again

### Recovery Pipeline

Layer:
  Recovery Layer

Meaning:
  the transformation from raw return into recovered judgment, placement, WATCH/HOLD, and next pull

Used for:
  return-to-space recovery, cycle_return, recovery records

Do Not Use As:
  automatic memory injection
  truth validation
  baseline promotion

Watch:
  recovery chain must not become heavy ceremony

### Execution Pipeline

Layer:
  Execution Layer

Meaning:
  bounded task route Gemini follows inside a work_order

Used for:
  observation tasks, evidence return, structural gap detection

Do Not Use As:
  broad repo read permission
  autonomous execution approval
  product implementation plan

Watch:
  execution must remain bounded by the cycle work_order

### Pipeline != Workflow

A pipeline describes a flow shape.
A workflow prescribes a repeated operating procedure.

In VectorFL, a pipeline must remain layer-aware.
It becomes unsafe when it is treated as a fixed workflow without explicit user approval.

## Term: Surface

Meaning Layer:
  visible face of a deeper space

Principle Layer:
  surface should stay thin

Structure Layer:
  board / checkpoint / active file / skeleton

Execution Layer:
  file Gemini reads to orient execution

Recovery Layer:
  recovered return made visible for review

Re-entry Layer:
  thin next-session view

Do Not:
  treat surface as dashboard or authority

Watch:
  surface becoming current-position

## Term: Sandbox

Meaning Layer:
  protected experiment space

Principle Layer:
  sandbox is light and reversible

Structure Layer:
  bounded cycle / trial folder / candidate output

Execution Layer:
  Gemini or Codex works inside constrained scope

Recovery Layer:
  results return only after judgment

Re-entry Layer:
  sandbox result appears only if still relevant

Do Not:
  treat sandbox as product architecture

Watch:
  sandbox output becoming fake authority

## Term: Recovery

Meaning Layer:
  preserving usable judgment from activity

Principle Layer:
  recovery should be accurate

Structure Layer:
  cycle_return / recovery file / run record

Execution Layer:
  Gemini returns evidence for recovery

Recovery Layer:
  raw return becomes recovered judgment with placement

Re-entry Layer:
  only recovered judgment returns to thin surface

Do Not:
  treat recovery as summary

Watch:
  recovery ceremony becoming too heavy

## Term: Map

Meaning Layer:
  cognitive orientation view

Principle Layer:
  map guides but does not command

Structure Layer:
  candidate markdown orientation file

Execution Layer:
  Gemini may inspect or dry-fill a map skeleton

Recovery Layer:
  map output requires placement and WATCH/HOLD

Re-entry Layer:
  map may inform but must not become current-position

Do Not:
  treat map as current-position

Watch:
  map clarity becoming authority

## Term: Packet

Meaning Layer:
  bounded intent carrier

Principle Layer:
  packet narrows scope

Structure Layer:
  file under relay/packets or cycle work_order

Execution Layer:
  Gemini / Codex executes only within packet bounds

Recovery Layer:
  packet return is recovered before placement

Re-entry Layer:
  packet path may appear as next manual transfer

Do Not:
  treat packet as execution approval

Watch:
  packet becoming hidden workflow

## Term: Cycle

Meaning Layer:
  larger arc of related work

Principle Layer:
  cycle reduces relay fatigue

Structure Layer:
  cycle_brief / work_order / queue / checkpoint / return

Execution Layer:
  Gemini executes one cycle-level task

Recovery Layer:
  cycle return captures recovered judgment

Re-entry Layer:
  cycle state informs next manual transfer

Do Not:
  treat cycle as automation

Watch:
  cycle becoming too large or workflow-like

## Term: Gate

Meaning Layer:
  judgment point

Principle Layer:
  gate preserves authority boundaries

Structure Layer:
  HOLD / approval note / checkpoint decision

Execution Layer:
  Gemini stops at gate and returns evidence

Recovery Layer:
  gate prevents raw return from becoming approval

Re-entry Layer:
  gate appears as manual next decision

Do Not:
  treat gate as user judgment replacement

Watch:
  gate becoming automatic blocker

## Term: Camera

Meaning Layer:
  way of looking at the space

Principle Layer:
  camera is an interpretive guide only

Structure Layer:
  may be represented as a lens note or prompt section

Execution Layer:
  Gemini can observe through the camera but not define truth

Recovery Layer:
  camera results need recovered judgment

Re-entry Layer:
  camera may inform next view

Do Not:
  treat camera as schema

Watch:
  camera becoming fixed ontology

## Term: Lens

Meaning Layer:
  focused interpretive angle

Principle Layer:
  lens helps read without replacing judgment

Structure Layer:
  packet section / map axis / checkpoint note

Execution Layer:
  Gemini applies lens to bounded read

Recovery Layer:
  lens output is candidate material

Re-entry Layer:
  useful lens may stay as thin orientation

Do Not:
  treat lens as schema

Watch:
  lens becoming doctrine

## Term: Line

Meaning Layer:
  emerging continuity in thought

Principle Layer:
  line is candidate, not proof

Structure Layer:
  growth trace / map note / recovery candidate

Execution Layer:
  Gemini may identify line evidence

Recovery Layer:
  line is recovered only with placement

Re-entry Layer:
  active line may appear as next pull

Do Not:
  treat line as workflow path

Watch:
  line becoming forced narrative

## Term: Axis

Meaning Layer:
  recurring dimension of interpretation

Principle Layer:
  axis is a reading lens, not ontology

Structure Layer:
  candidate axis section / map column

Execution Layer:
  Gemini can test an axis against evidence

Recovery Layer:
  axis becomes usable only with WATCH boundaries

Re-entry Layer:
  active axis may guide next observation

Do Not:
  treat axis as schema

Watch:
  axis becoming fixed taxonomy

## Term: Judgment

Meaning Layer:
  user-led decision sense

Principle Layer:
  judgment is preserved over outcome

Structure Layer:
  recovered judgment / placement / gate note

Execution Layer:
  Gemini provides evidence, not judgment authority

Recovery Layer:
  return becomes useful only as recovered judgment

Re-entry Layer:
  thin surface carries judgment, not raw data pile

Do Not:
  outsource final judgment to CLI

Watch:
  fluent output masquerading as judgment

## Term: Return

Meaning Layer:
  something brought back from execution or thought

Principle Layer:
  return is not truth

Structure Layer:
  cycle_return / relay return / run record

Execution Layer:
  Gemini returns observation or evidence

Recovery Layer:
  raw return -> recovered judgment -> placement

Re-entry Layer:
  only selected return material appears next

Do Not:
  treat return as truth

Watch:
  return becoming memory automatically

## Term: Memory

Meaning Layer:
  durable remembered judgment or context

Principle Layer:
  memory requires recovery and placement

Structure Layer:
  candidate recovery file or current-position only when explicitly updated

Execution Layer:
  Gemini does not write memory

Recovery Layer:
  memory candidate emerges after review

Re-entry Layer:
  memory is represented thinly, not dumped

Do Not:
  treat run record as memory

Watch:
  storage becoming remembered truth

## Term: Baseline

Meaning Layer:
  accepted foundation

Principle Layer:
  candidate != baseline

Structure Layer:
  only explicit approved baseline files count

Execution Layer:
  Gemini cannot create baseline

Recovery Layer:
  recovery record cannot promote itself

Re-entry Layer:
  baseline informs but is not inferred from active surface

Do Not:
  treat candidate as baseline

Watch:
  repeated use becoming accidental baseline

## Term: Current-position

Meaning Layer:
  explicit re-entry anchor

Principle Layer:
  anchor is explicit, not automatic

Structure Layer:
  current-position file only when approved

Execution Layer:
  Gemini should not update current-position

Recovery Layer:
  placement does not update current-position

Re-entry Layer:
  current-position is a special anchor, not every active surface

Do Not:
  treat map as current-position

Watch:
  board / checkpoint replacing current-position

## Term: Next Pull

Meaning Layer:
  possible next thread to pull

Principle Layer:
  next pull is manual and optional

Structure Layer:
  checkpoint / cycle return / board note

Execution Layer:
  Gemini may suggest, not trigger

Recovery Layer:
  next pull is recovered as candidate

Re-entry Layer:
  next pull may appear on thin surface

Do Not:
  treat next pull as automatic next task

Watch:
  suggestions becoming implicit queue

## 4. Required Distinctions

- pipeline != workflow
- surface != dashboard
- sandbox != product architecture
- recovery != summary
- map != current-position
- packet != execution approval
- cycle != automation
- gate != user judgment replacement
- camera/lens != schema
- return != truth
- memory != run record
- baseline != candidate
- next pull != automatic next task

## 5. Do Not Promote

- term table != ontology
- term table != registry
- term table != policy
- term table != baseline
- term table != final vocabulary
