# VectorFL Vessel / Contents Separation Spec
# 2026-05-13 Candidate v0

## 1. Status

Document:
  candidate vessel / contents separation spec

Authority:
  orientation and bounded operating support only

Not:
  final framework
  baseline
  workflow
  registry
  schema
  ontology
  automation plan
  current-position
  output_manifest
  product architecture

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH

---

## 2. Core Metaphor

A coffee shop cup can hold many drinks.

The drink can change.
The cup should remain stable enough to manage the contents.

In VectorFL:

Vessel / Cup:
  the stable large frame

Contents / Drink:
  the materials, traces, returns, judgments, maps, ledgers, cycles, packets, experiments, and operating-principle tests that enter the frame

Core rule:
  Contents may grow.
  The vessel should not change every time contents grow.

Failure:
  If every new content creates a new vessel, the space becomes cluttered and hard to operate.

---

## 3. Core Operating Sentence

원본은 깊게,
표면은 얇게,
샌드박스는 가볍게,
회수는 정확하게.

Interpretation:

원본은 깊게:
  the original space / reservoir should preserve accumulated judgment, trace, failure, process, and candidate memory

표면은 얇게:
  re-entry surfaces should stay compact and should not become full inventories or registries

샌드박스는 가볍게:
  trials and derivatives should happen in bounded spaces without polluting the original vessel

회수는 정확하게:
  raw outputs should return as recovered judgments, WATCH/HOLD, placement, and next owner, not as truth or baseline

---

## 4. Vessel Definition

The vessel is the stable large frame that holds contents.

The vessel includes:

- Big Frame / Common Growth Frame
- layer-aware operating principle
- user judgment gate
- provenance / trace preservation
- sandbox separation
- recovery requirement
- WATCH / HOLD boundary
- candidate-with-watch posture

The vessel is not:

- a workflow
- a registry
- a schema
- an ontology
- a baseline
- a dashboard
- a product architecture
- an automation engine

The vessel fails if:

- contents become baseline automatically
- tool returns become truth
- maps become workflow
- ledgers become current-position
- cycle / packet / pool becomes automation
- the user becomes a relay worker again
- new operating principles create new structures by default

---

## 5. Contents Definition

Contents are materials inside the vessel.

Content examples:

- user thought traces
- external materials
- internal memos
- Codex results
- Gemini observations
- run records
- cycle returns
- recovered judgments
- structural gaps
- WATCH items
- HOLD items
- candidate maps
- progress ledgers
- packets
- cycles
- request queues
- new operating-principle tests

Contents may grow.

Growth is acceptable if:

- each content keeps provenance
- each content has placement
- each content does not become authority by default
- each content can be re-entered through a thin surface
- each content can be classified as part of the existing vessel

Contents must not become:

- registry
- baseline
- official memory
- final truth
- automatic next task
- new vessel without approval

---

## 6. Handling Parts

Not everything is either vessel or content.

Some assets are handling parts.

Classify handling parts as:

### Inlet / Intake

How new material enters the vessel.

Examples:
  user prompt, external link, pasted text, Codex return, Gemini return, worker output, run result, failure report

Must answer:
  - What is the material?
  - Why is it entering?
  - What is the smallest sufficient context?
  - Which Camera / Lens might apply?
  - What should not be read?
  - What is the approval scope?

---

### Processing Mechanism

How contents are worked on inside the vessel.

Examples:
  Manual Cycle Relay, bounded operating thread, work_order, request_queue, sandbox derivation

Must not become:
  automation
  fixed workflow
  product pipeline
  hidden authority

---

### Recovery Outlet

How processed material returns as usable judgment.

Examples:
  cycle_return, recovered judgment, Return-to-Space Card, placement, WATCH/HOLD

Must not become:
  current-position update
  automatic memory injection
  truth validation
  baseline promotion

---

### Re-entry Surface

How the user or CLI returns later without reading everything.

Examples:
  Big Frame Candidate Map, Progress Ledger, Active Re-entry Surface, anchor list, closeout card

Must remain:
  thin
  candidate with watch
  not registry
  not current-position
  not workflow

---

### Safety Lid / Guardrail

How the vessel prevents overpromotion.

Examples:
  Approval Scope, WATCH, HOLD, Do Not Promote, User Judgment Gate

Must prevent:
  compressed approval becoming blanket approval
  candidate becoming baseline
  return becoming truth
  ledger becoming authority
  autonomy becoming automation

---

### Label / Status Marker

How contents are marked.

Examples:
  candidate, draft, watch, hold, returned, closed, ready, blocked

Must not become:
  approval
  baseline
  current-position
  official state machine

---

## 7. Current Asset Classification

| Asset | Classification | Why | Risk if misread |
|---|---|---|---|
| Big Frame | Vessel / container | Holds the common growth frame, user judgment gate, sandbox separation, recovery requirement, and candidate-with-watch posture | May be mistaken for final framework or product architecture |
| 6 genealogy layers | Contents | Provide historical and structural support layers for the vessel | May be mistaken for ontology or required layer schema |
| Big Frame Candidate Map | Re-entry surface | Thin orientation heatmap for entering the large frame | May be mistaken for final framework, workflow, or registry |
| Manual Cycle Relay Progress Ledger | Re-entry surface | Thin progress view of what cycle tests have proven and not proven | May be mistaken for current-position, backlog, or authority ledger |
| Lane Contract | Safety lid / guardrail | Separates ChatGPT, Codex, Gemini, and User responsibilities | May be mistaken for hierarchy, workflow, or role registry |
| Operating Term Disambiguation Table | Safety lid / guardrail | Prevents overloaded terms from collapsing across layers | May be mistaken for ontology, schema, glossary authority, or registry |
| Manual CLI Relay | Processing mechanism | Lets paths and bounded packets replace long prompt relay | May be mistaken for automation or workflow |
| Manual Cycle Relay | Processing mechanism | Moves one bounded cycle through brief, work order, request queue, checkpoint, and return | May be mistaken for automatic execution pipeline |
| Approval Scope | Safety lid / guardrail | Records what was and was not approved | May be mistaken for approval registry or blanket permission |
| Operating Thread 001 | Contents | First actual bounded input and closeout evidence | May be mistaken for baseline proof that all threads can run automatically |
| Operating Thread 002 | Inlet / intake | Waiting slot for one real bounded material after retarget | May be mistaken for already approved Gemini execution |
| cycle / packet / checkpoint / request queue | Processing mechanism | Handling parts for bounded relay and structure-gap return | May be mistaken for workflow, backlog, or automation queue |
| Gemini observation | Contents | External observation and evidence return | May be mistaken for truth or final meaning authority |
| Codex return | Recovery outlet | Repo-side structure result and recovered judgment packaging | May be mistaken for approval or final placement authority |
| recovered judgment | Recovery outlet | Usable value recovered from material, trace, failure, or return | May be mistaken for baseline or verified truth |
| Bounded Space-Hinted Autonomy Trial | Autonomy support | Candidate evidence that high-level purpose plus anchors can support bounded execution | May be mistaken for automation approval |

---

## 8. New Operating Principle Test Rule

When a new operating principle appears:

1. Do not create a new vessel immediately.
2. Treat it first as content inside the existing vessel.
3. Classify it as one or more of:
   - content
   - inlet / intake
   - processing mechanism
   - recovery outlet
   - re-entry surface
   - safety lid / guardrail
   - label / status marker
   - autonomy support
4. Test whether the existing vessel can hold it.
5. Reuse existing cycle / packet / pool / recovery structures if possible.
6. Create a new structure only if the existing vessel repeatedly fails.
7. User approval is required before creating a new vessel-level structure.

Short rule:

새 원칙은 먼저 내용물로 테스트한다.
그릇은 반복 실패할 때만 바꾼다.

---

## 9. Misread Risk Table

| Misread | Why dangerous | Correct reading | Guardrail |
|---|---|---|---|
| Big Frame Candidate Map mistaken as final framework | Freezes a candidate orientation surface into authority | Candidate re-entry map only | Keep `Not: final framework / baseline / workflow / registry` visible |
| Progress Ledger mistaken as current-position | Turns progress memory into official present state | Thin proof/progress view only | Require separate explicit current-position approval |
| Term Table mistaken as ontology/schema | Converts clarification into rigid model | Disambiguation aid only | Keep layer-specific meaning and Do Not Promote notes |
| Manual Cycle Relay mistaken as workflow | Makes bounded manual relay into fixed process | Processing mechanism for bounded cycles | Require user approval before any workflow promotion |
| Approval Scope mistaken as approval registry | Treats scoped approval records as standing permission | Per-cycle guardrail only | Record raw instruction, interpreted scope, not-approved items, stop condition |
| Gemini return mistaken as truth | Lets broad observation become authority | Worker evidence / observation material | Codex or ChatGPT must downshift to recovered judgment with WATCH/HOLD |
| Codex structure mistaken as approval | Treats file creation as user-approved meaning | Repo-side implementation only | User remains promotion authority |
| recovered judgment mistaken as baseline | Freezes one return into permanent rule | Candidate value recovered from one material | Placement remains RETURN_TO_SPACE_VALUE_WITH_WATCH unless explicitly promoted |
| operating thread mistaken as automation | Lets one bounded thread imply automatic next execution | Manual bounded intake slot | Gemini execution and material processing require separate approval |
| autonomy readiness mistaken as automation approval | Converts structural signal into execution permission | Autonomy support candidate only | Require explicit user approval for automation or pool execution |

---

## 10. CLI Use Rule

Codex and Gemini may use this spec as a first anchor.

CLI may:

- identify whether a new material is vessel, content, inlet, process, recovery, re-entry, guardrail, label, autonomy support, or mixed
- choose smallest sufficient context
- create candidate notes or request entries
- return recovered judgments
- mark WATCH / HOLD

CLI may not:

- create a new vessel-level structure without approval
- promote content to baseline
- update current-position
- update output_manifest
- create registry / schema / ontology
- create automation
- treat this spec as final authority
- execute the next pool automatically

CLI must return to User / ChatGPT when:

- authority shift is implied
- new vessel is proposed
- baseline promotion is implied
- HOLD release is needed
- scope expansion is needed
- approval ambiguity appears

---

## 11. Failure Conditions

This spec fails if:

- it becomes a workflow
- it becomes a registry
- it becomes a schema
- it becomes an ontology
- it becomes a baseline
- it becomes an automation plan
- it causes every new idea to be overclassified
- it prevents actual operation
- it makes the user manage more documents instead of fewer
- it encourages new structures instead of reusing the vessel

---

## 12. Do Not Promote

- spec != baseline
- spec != schema
- spec != registry
- spec != workflow
- spec != ontology
- spec != automation
- vessel map != final framework
- contents classification != official asset registry
- autonomy support != automation approval
- new operating principle test != new structure approval

---

## 13. Next Use

This spec may be used as:

- first anchor for bounded CLI autonomy pool trials
- check before creating new structures
- guide for classifying new operating principles
- guide for reducing space clutter

Do not use it as:

- final authority
- automatic execution permission
- product architecture
- registry
- schema
- baseline

Recommended next use:
  Give Codex or Gemini a large-frame purpose, this spec as anchor, and a small set of materials.
  Ask whether the new material fits inside the existing vessel before creating any new structure.

