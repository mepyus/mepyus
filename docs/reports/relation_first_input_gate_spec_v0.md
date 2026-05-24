# Relation-first Input Gate Spec v0

## 1. Document Status

```text
Document = Relation-first Input Gate Spec v0
Status = CANDIDATE_OPERATION_SPEC
Authority = orientation / usage support
Not baseline
Not schema
Not ontology
Not official workflow
Not automation
Not registry/index/ledger
Not current-position update
Not implementation plan
```

Purpose:

```text
Clarify what the Relation-first / Compact-first input operating frame is, what it does, what it does not do, which components it uses, and where it stops.
```

This document specifies the current shape of the candidate operating frame.

It does not make the frame official.

It does not create a runtime input processor.

## 2. Name

Recommended name:

```text
Relation-first Input Gate
관계우선 입력 관문
```

User-facing name:

```text
외부 자료를 공간에 넣어보기 위한 인지적 입구
```

Operational alternate:

```text
Compact-first External Material Reading Frame
```

Why "Gate":

```text
This frame does not automatically ingest materials.
It checks, routes, holds, rejects, or escalates materials before they enter deeper project handling.
```

## 3. One-sentence Definition

```text
Relation-first Input Gate는 외부 자료를 바로 요약·구현·자동화·자산화하지 않고,
먼저 자료의 전체 흐름, 우리 공간과의 연결 압력, 위험, 보존 여부를 판단하여
Compact / Standard / Heavy Watch / Hold / Reject 중 하나로 분기하는
사용자 판단 보조용 입력 운영 틀이다.
```

Simpler wording:

```text
외부 자료가 들어왔을 때 "이걸 우리 공간에 어떻게 넣을지"를 먼저 가볍게 판단하는 문이다.
```

## 4. Core Essence

### 4.1 Relation-first

Before splitting a source into many fragments, read the whole flow and its relationship pressure.

Questions:

```text
What kind of material is this?
What is it trying to move?
Which existing concern in the space does it touch?
Does it bring a function, an operating grammar, a watch signal, or only background context?
```

### 4.2 Compact-first

Do not begin with a large report.

Start with:

```text
쓸 수 있나?
왜?
다음엔?
조심할 점은?
```

Then route:

```text
If insufficient -> Standard
If risky -> Heavy Watch
If low value -> Reject
If unclear -> Hold
```

### 4.3 No-file Default

Do not create a file just because external material arrived.

Default:

```text
judge in conversation
preserve the key boundary
do not file unless needed
```

File creation may be considered only when:

```text
reuse value is high
the material must be found later
it should be preserved as a risk case
several materials should be handled in a batch report
```

## 5. Three Layers

### 5.1 Reading Layer

```text
Relation-first reading
reads the material's flow, relation, and pressure before segmentation.
```

### 5.2 Operation Layer

```text
Compact / Standard / Heavy Watch / Hold / Reject
decides how deeply the material should be handled.
```

### 5.3 Safety Layer

```text
Evidence Label / Placement / User Gate / No-file default
prevents material from sliding into authority, automation, implementation, baseline, workflow, registry, or ontology.
```

## 6. Component Specification

### 6.1 Source Bundle

Role:

```text
Capture the external material together with User intent.
```

Questions:

```text
What is this material?
Why did the User bring it now?
From what angle should this be read?
```

Boundary:

```text
Source Bundle is not a storage unit.
It does not require file creation.
```

### 6.2 Source-level Reading

Role:

```text
Read the source's whole flow before cutting it into parts.
```

Questions:

```text
What is the source trying to say?
What is its internal movement?
Is it a tool description, operating case, risk case, or background note?
```

Boundary:

```text
This is flow reading, not mere summary.
```

### 6.3 Meaning Block

Role:

```text
Group the material into meaning-level blocks when it is long or complex.
```

Use when:

```text
the material is long
the material is composite
Standard or Heavy handling is needed
```

Boundary:

```text
Meaning Block is optional in Compact mode.
Too many meaning blocks can recreate segmentation-first behavior.
```

### 6.4 Relation Reading

Role:

```text
Read the connection pressure between the material and the space.
```

Questions:

```text
Which project problem does this touch?
Does it offer a function?
Does it offer operating grammar?
Does it offer a risk case?
Does it offer a comparison lens?
```

Boundary:

```text
Relation Map is not ontology.
It is not an official graph.
It is not an automated router.
```

### 6.5 Evidence / Provenance Label

Role:

```text
Mark the status of the information.
```

Labels:

```text
EXTRACTED: directly in the source
INTERPRETED: interpretation from reading the source
INFERRED: inference made by connecting to our space
WATCH: risk or drift signal
USER_JUDGED: explicit User judgment is included
PROCESS_TRACE: trace of how the work happened
```

Boundary:

```text
Evidence Label is not truth score.
EXTRACTED does not mean important.
INFERRED does not mean false.
It only marks provenance/status.
```

### 6.6 Placement

Role:

```text
Decide where the signal should sit for now.
```

Common placements:

```text
Light Reference
Worker-facing Context Reference
Source-facing Context Reference
Process Asset Candidate
Tool Risk Case
Heavy Watch
Hold
Reject
Residue
```

Boundary:

```text
Placement is not registry state.
Process Asset Candidate is not official asset registration.
Watch is not a task queue.
Hold is not failure.
Reject means "do not preserve," not "ignore all meaning forever."
```

### 6.7 Mode Selection

Role:

```text
Decide how deeply to handle the material.
```

Default:

```text
Compact-first
```

Modes:

```text
Compact
Standard
Heavy Watch
Hold
Reject
```

Boundary:

```text
Mode selection is not workflow.
It is a temporary operating lever for judgment.
```

### 6.8 Compact Card

Role:

```text
Return the minimum useful judgment for User re-entry.
```

Shape:

```text
쓸 수 있나?
왜?
다음엔?
조심할 점은?
Placement: optional
```

Boundary:

```text
Compact is not shallow analysis.
Compact is low-cost judgment.
Compact results are no-file by default.
```

### 6.9 Re-entry Signal

Role:

```text
Leave a small signal for how this material may be found or reread later.
```

Examples:

```text
worker-facing context reference
tool attachment risk case
sandbox execution safety watch
source-facing context comparison lens
```

Boundary:

```text
Re-entry Signal is not current-position update.
It is not official state update.
It is not automatic retrieval trigger.
```

### 6.10 User Gate

Role:

```text
Keep final use, preservation, escalation, adoption, and promotion under User judgment.
```

Boundary:

```text
AI worker output is decision support.
Codex/Gemini/ChatGPT output must not become final truth or system authority.
```

## 7. Operation Specification

### 7.1 Basic Principles

```text
1. External material is not automatically accepted.
2. External material is not implemented directly.
3. External tools are not adopted directly.
4. External cases are first read as relation pressure and risk.
5. Start Compact-first.
6. File creation is not default.
7. Reject / Hold are normal outcomes.
8. Heavy Watch is risk isolation, not adoption planning.
9. User Gate is always preserved.
```

### 7.2 Input Handling Flow

```text
external material
-> Compact 4-line card
-> mode judgment
```

Routes:

```text
A. Low value
-> Reject / No preserve / No file

B. Light reference
-> Compact / Light Reference / No file

C. Reusable value
-> Standard-light / Reference Candidate / include in batch if needed

D. Risk pressure
-> Heavy Watch / Risk Case / no adoption

E. Signal but insufficient evidence
-> Hold / No file or batch note
```

### 7.3 Compact Stay Conditions

Stay Compact when:

```text
one-pass judgment is enough
no implementation pressure
no automation pressure
no tool attachment pressure
no baseline / registry / workflow pressure
User can understand it through the 4-line card
no separate file is needed
```

### 7.4 Standard Escalation Conditions

Escalate to Standard when:

```text
there is repeated connection value with the space
the material is worker-facing context
the material is source-facing context
the material is guideline / review burden
the material may be useful as operating grammar reference
later retrieval may matter
Compact is too thin for the context
```

### 7.5 Heavy Watch Escalation Conditions

Escalate to Heavy Watch when:

```text
implementation temptation is strong
automation temptation is strong
MCP / API / tool attachment pressure exists
agent harness / autonomous loop pressure exists
security / credential / OAuth / runtime / sandbox risk exists
User Gate may weaken
external structure pressures the project to copy it
```

### 7.6 Reject Conditions

Reject when:

```text
it is general background only
there is no special relation pressure to the space
it repeats known material without adding useful pressure
preservation cost is higher than value
```

### 7.7 Hold Conditions

Hold when:

```text
there is signal but evidence is weak
source or repo confidence is low
implementation pressure exists but reference value is unclear
it is too early to judge
```

## 8. What This Is Not

Relation-first Input Gate is not:

```text
automatic ingest pipeline
document classification system
ontology
knowledge graph
registry
workflow controller
tool integration layer
MCP connection plan
Codex/Gemini autonomous operating device
baseline candidate
truth promotion device
```

It sits before those.

It is a judgment gate for whether and how external material should be brought into the space.

## 9. Current Maturity

```text
Concept: fairly clear
Components: basic components exist
Operation: Compact-first / No-file default / Heavy Watch route confirmed
Repetition: Batch 001 provided first repeated operation check
Safety: first-layer drift defenses are working
```

Still weak:

```text
long-term repeated operation stability
worker misunderstanding tests
status-name accumulation risk
legacy re-read repetition
operating cost measurement
negative control coverage
```

Current maturity judgment:

```text
Not a finished system.
Concrete enough as an operating frame candidate.
Specific enough for repeated use with watch.
```

## 10. Central Specification Sentence

```text
Relation-first Input Gate는 외부 자료를 우리 공간에 자동 편입시키는 시스템이 아니라,
자료의 흐름과 연결 압력을 먼저 읽고,
그 자료를 버릴지, 보류할지, 가볍게 참고할지, 재사용 후보로 둘지, 위험 사례로 격리할지를
사용자가 판단할 수 있게 돕는 Compact-first 인지 관문이다.
```

## 11. Current Operating State

```text
Current State:
RELATION_FIRST_REPETITION_OPERATION_BATCH001_COMPLETE_WITH_WATCH

Next State:
WAIT_FOR_NEXT_REAL_INPUT_COMPACT_FIRST_WITH_NO_FILE_DEFAULT

Operating Rule:
Compact-first.
No-file default.
Reject/Hold allowed.
Escalate only when needed.
User Gate preserved.
```

## 12. Watch Items

```text
Relation-first Input Gate becoming official workflow
Compact / Standard / Heavy becoming rigid schema
Placement becoming registry state
Relation Map becoming ontology
Evidence Label becoming truth score
Re-entry Signal becoming current-position update
Heavy Watch becoming implementation planning
Compact becoming boundary omission
No-file default being ignored
User Gate becoming ceremony
Gemini evidence becoming verified truth
Codex packaging becoming final authority
```

## 13. Do Not Do Yet

```text
no implementation
no automation
no runtime script
no registry/index/ledger
no formal schema
no official workflow
no current-position update
no baseline promotion
no tool/API/function attachment
no MCP attachment
no ontology creation
no input processor runtime
no broad legacy migration
no dashboard implementation
no Gemini verified-truth authority
no Codex final authority
no per-material file by default
```

## 14. User-facing Output Rule

Default user-facing output should not expose the full internal chain.

Default Compact output:

```text
쓸 수 있나?
왜?
다음엔?
조심할 점은?
Placement: optional
Mode result: optional
```

Internal components such as Source Bundle, Source-level Reading, Evidence Label, Relation Reading, Placement, and Re-entry Signal may guide the judgment, but they do not need to be fully printed unless the material escalates to Standard or Heavy Watch.

Compact output must stay readable for the User.

Do not turn the internal component list into a mandatory visible template.

## 15. Final Status

```text
STATUS: RELATION_FIRST_INPUT_GATE_SPEC_V0_PREPARED_AS_CANDIDATE
```
