# Re-entry Compression Note Operating Principle
# 2026-05-13 Candidate v0

## 1. Status

Document:
  candidate operating principle note

Authority:
  orientation and cost-control support only

Not:
  workflow
  registry
  schema
  ontology
  baseline
  current-position
  output_manifest
  automation plan
  official memory system

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH

---

## 2. Core Problem

VectorFL can lose time and tool quota when a task is executed from repo context alone.

Observed failure shape:

1. User gives a high-level purpose.
2. Codex reads internal repo affordances.
3. A convenient implementation path appears.
4. The path is executed before the task type is fully interpreted.
5. User correction is needed.
6. Work must be undone, reinterpreted, and rebuilt.

This can be manageable for a small local task.
It becomes expensive when the task involves Gemini, external tools, long context, or quota-limited execution.

---

## 3. Recovered Judgment

Enough of the process must be recorded so the next run does not need to reread everything.

But the record must stay thin enough that it does not become a registry, workflow, schema, baseline, or current-position.

Short rule:

다시 깊게 읽지 않을 만큼만 남기고,
권위가 될 만큼은 남기지 않는다.

English rule:

Enough to avoid rereading.
Not enough to become authority.

---

## 4. Operating Shape

Before execution, attach an interpretation layer to the existing vessel and pipeline.

Stable structure:
  vessel / cup
  intake
  processing path
  recovery outlet
  re-entry surface

Thin interpretation:
  lens
  LACL-like reading
  external reference
  surface language guardrail
  task-type judgment

Execution:
  Codex / Gemini / CLI / user action

Return:
  recovered judgment
  WATCH
  HOLD
  placement
  next small action
  re-entry compression note when useful

Short rule:

Structure stays.
Lens changes.
Execution reuses the same recovery path.

---

## 5. What A Re-entry Compression Note Should Capture

A re-entry compression note should answer only the questions needed to prevent expensive rereading or wrong re-execution.

Minimum fields:

Task:
  what this work was

Final reading:
  what kind of work this turned out to be

Reuse:
  existing vessel / pipeline / lens / files that can be reused

Do not repeat:
  reading, searching, or implementation attempts that are already settled

Avoid:
  repo affordances, external frames, or tool paths that previously pulled the task off course

Execution shape:
  what form the next execution should take

WATCH:
  still-risky interpretation or promotion points

HOLD:
  boundaries that remain closed

Next smallest action:
  one bounded continuation step

---

## 6. Operating Board v0 Example

Task:
  create VectorFL Operating Board v0

Final reading:
  one-input judgment recovery surface, not app feature, not product dashboard

Reuse:
  standalone HTML output
  today work return note
  trace / interrupt / human gate / recovered judgment framing

Do not repeat:
  broad app route exploration
  treating existing React app structure as the default target
  redoing the full AgentOps search unless the external landscape changes

Avoid:
  app route attachment too early
  production dashboard drift
  approval-machine language
  brand imitation from style references

Execution shape:
  edit standalone preview only
  keep mock/manual state
  test whether one input still recovers judgment clearly

WATCH:
  style becoming product architecture
  trace surface becoming observability platform
  HITL becoming approval system

HOLD:
  automation
  live Gemini / Codex wiring
  backend / database / auth
  workflow / registry / schema / ontology
  current-position update
  output_manifest update

Next smallest action:
  change one input example and check whether the board still shows current state, pause reason, recovered judgment, WATCH, HOLD, and next action

---

## 7. Gemini / External Tool Cost Control Use

Before sending a long task to Gemini or another external tool, prefer sending the compression note first.

The note should tell the external tool:

- what is already decided
- what must not be reopened
- what lens should be attached
- what context is sufficient
- what output shape is needed
- where to stop

This reduces the chance that one bad packet consumes a long quota window.

Important:
  The compression note is not a substitute for user judgment.
  It is a guard against repeated rereading and wrong execution shape.

---

## 8. WATCH

- Compression notes becoming a registry.
- Compression notes becoming official memory.
- Compression notes becoming current-position.
- Compression notes becoming a workflow checklist.
- Too many notes causing more reading instead of less.
- Notes becoming authority instead of orientation.
- External references becoming structure authority.
- Lens selection becoming schema.

---

## 9. HOLD

- automation
- registry / schema / ontology creation
- workflow promotion
- baseline promotion
- current-position update
- output_manifest update
- automatic Gemini execution
- broad repo read by default
- treating compression notes as official history

---

## 10. Do Not Promote

- compression note ≠ registry
- compression note ≠ workflow
- compression note ≠ schema
- compression note ≠ ontology
- compression note ≠ baseline
- compression note ≠ current-position
- compression note ≠ official memory
- lens ≠ structure
- external reference ≠ authority
- cost control ≠ automation approval

---

## 11. Next Use

Use this principle when:

- a task may involve Gemini or quota-limited external tools
- a prior attempt already produced a useful correction
- the next run should avoid broad rereading
- repo affordance may pull execution in the wrong direction
- the user wants one task to continue without rebuilding the whole context

Recommended next use:
  Before the next nontrivial operating-board task, create or read the smallest relevant compression note and execute from that note plus the target artifact.

