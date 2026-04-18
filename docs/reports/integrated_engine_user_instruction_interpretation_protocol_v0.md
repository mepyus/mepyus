# Integrated Engine User Instruction Interpretation Protocol v0

## 1. Verdict

PASS_WITH_NOTE.

This protocol locks the current 3-surface / camera / lens interpretation as a work-start rule. It does not introduce a new concept, schema, panel, camera, or automation layer.

## 2. Purpose

When a user gives a task, Codex should not immediately implement, add panels, scan broadly, or invent a new route.

Codex should first convert the instruction into:

```text
fixed body
+ object scope
+ lens
+ existing camera or camera variation
+ guard
+ expected return
+ surface projection
+ record/redeposit plan
```

This keeps the integrated engine stable while allowing new work to be handled through existing cameras and lenses.

## 3. Minimum Work-Start Protocol

### Step 1. Confirm Fixed 3-Surface Body

Always start from the fixed body:

- User surface
- VectorFL surface
- Engine surface

Check:

- Does this task require a fourth surface? If yes, reject that reading.
- Can it be projected through the existing three surfaces? If yes, continue.

Rule:

```text
No user instruction creates a new surface by default.
```

### Step 2. Decide Object Scope

Identify what material the instruction allows you to read.

Possible scopes:

- current user instruction only
- current CLI turn
- selected input documents
- space input texts only
- generated patch notes
- current runtime artifacts
- existing reports/specs
- explicit file list

Check:

- Is broad space scan allowed?
- Is the scope limited by words like `only`, `먼저`, `현재`, `입력문만`, `이 파일만`?
- Is the user asking for data extraction, validation, implementation, translation, or reread?

Rule:

```text
Object scope limits evidence. Do not exceed it without explicit need.
```

### Step 3. Decide Lens

Identify what the object should be read as.

Common lens candidates:

- `language_sync`
- `Koreanization`
- `engine_language_extraction`
- `line_extraction`
- `flow_reading`
- `validation`
- `implementation`
- `surface_exposure`
- `authority_route`
- `feedback_memory`

Check:

- Is the task asking for meaning sync?
- Is it asking for engine-operating terms?
- Is it asking for line / connection / axis candidates?
- Is it asking for drift / weak evidence / conflict?
- Is it asking for bounded implementation?

Rule:

```text
Lens determines what the object becomes, not what surface is created.
```

### Step 4. Search Existing Camera

Before creating a new camera, search current known cameras:

- Integrated operating camera
- Surface exposure camera
- Multi-lens document reading camera
- Feedback memory camera
- Line lifecycle camera
- Current work package projection camera
- Support-layer / exposure-budget camera
- Human-readable exposure camera

Check:

- Does one existing camera already match the process?
- Can a current camera handle the task if the lens changes?
- Is only a stage variation needed?

Rule:

```text
Reuse before variation. Variation before new camera. New camera only as candidate.
```

### Step 5. Decide Camera Reuse / Variation

Choose one:

- `reuse`: existing camera fits
- `lens-swap`: same camera, new lens/object
- `minor variation`: one stage needs adjustment
- `candidate camera needed`: no camera fits

Allowed only with evidence:

- `candidate camera needed`

Rule:

```text
Do not create a candidate camera unless reuse and variation both fail.
```

### Step 6. Set Guard

Define what must not happen.

Common guard items:

- no broad space scan
- no UI / panel change
- no new camera
- no new lens promotion
- no final glossary
- no runtime binding
- no canonical ingestion
- no external search
- no implementation
- explicit input scope only

Rule:

```text
Guard prevents the lens from becoming expansion.
```

### Step 7. Define Expected Return

Define the output shape before work starts.

Possible return shapes:

- candidate list
- candidate + evidence
- usable / hold / needs reread classification
- conflict check
- route decision material
- extraction table
- dry-run interpretation
- implementation note
- closeout note

Rule:

```text
Expected return controls completion. Do not silently expand it.
```

### Step 8. Define 3-Surface Projection

For the chosen work, define what each surface should receive.

User surface:

- decision / assignment / hold summary
- what the user can do next
- what should remain hidden/support

VectorFL surface:

- lens/object reading
- evidence bundle
- route / guard / reread classification
- whether re-entry is needed

Engine surface:

- processing input
- extraction / generation / validation material
- return material
- uncertainty / failure note

Rule:

```text
Same work package, different surface projection.
```

### Step 9. Define Record / Redeposit Items

Decide what should go back into space.

Possible records:

- lens used
- camera used
- object scope
- evidence refs
- candidate list
- classification
- guard
- uncertainty / hold reason
- reusable camera/lens observation
- next reread candidate

Rule:

```text
Every meaningful run should leave reusable space material.
```

## 4. Work-Start Checklist

Before executing, answer these in order:

1. Fixed 3 surfaces confirmed?
2. What is the object scope?
3. What lens is active?
4. Which existing camera applies?
5. Is this reuse, lens-swap, or minor variation?
6. What guards are active?
7. What is the expected return shape?
8. What does User surface receive?
9. What does VectorFL surface receive?
10. What does Engine surface receive?
11. What records should redeposit into space?

If any answer is unclear:

- keep the work as dry-run
- do not implement
- do not broaden scope
- report the ambiguity as a VectorFL reread point

## 5. Dry-Run Example

### User Instruction

```text
공간의 입력문만 들여다보고 엔진 언어로 추출 가능한 데이터만 뽑아줘.
```

### 1. Applied Lens

`engine_language_extraction`

Why:

- The instruction asks for data that can be extracted as engine language.
- It does not ask for final Korean translation.
- It does not ask for line maturity, UI patch, or glossary.

### 2. Used Camera

`Integrated operating camera` with a light `multi-lens / line-extraction` reuse.

Camera reading:

```text
instruction intake
-> lens/object recognition
-> internal search limited to input texts
-> evidence bundle
-> engine-language candidate extraction
-> VectorFL classification
-> User-readable dry-run return
-> record/redeposit candidates
```

Camera decision:

- `reuse`
- not a new camera
- no camera promotion

### 3. Input Scope

Object scope:

```text
space input texts only
```

Allowed evidence:

- user-provided input texts
- explicitly scoped input records
- direct phrases inside those inputs

Excluded evidence:

- broad repo scan
- all reports/specs
- UI source code
- generated patch notes unless explicitly included as input texts
- external material

### 4. Guard

Active guards:

- no broad space scan
- no new UI / panel
- no new camera
- no final glossary
- no external search
- no implementation
- no canonical ingestion
- input text scope only
- output candidates only

### 5. Extraction Candidate Categories

Candidate categories to extract:

| candidate category | what counts |
| --- | --- |
| route language | request, return, reflux, re-entry, route, handoff |
| state language | hold, watch, candidate, not promoted, validation target, not canonical |
| authority language | who may decide, who may process, who may validate, who may promote |
| boundary language | guard, do-not, scope, no broad scan, no finalization |
| processing language | line generation, line translation, line extraction, flow reading, classification |
| space language | record, memory, trace, line, connection, axis, sedimentation |

### 6. Candidate / Evidence / Classification Dry-Run

Because this is a bounded dry-run, the table below uses the example instruction itself as the only evidence.

| candidate | evidence | classification |
| --- | --- | --- |
| `object_scope` | “공간의 입력문만” | usable |
| `engine_language_extraction` | “엔진 언어로 추출 가능한 데이터” | usable |
| `candidate_only_return` | “데이터만 뽑아줘” and dry-run guard | usable |
| `no_broad_space_scan` | “입력문만” | usable |
| `no_final_glossary` | instruction asks extraction, not final naming | hold |
| `line_or_axis_candidate_possible` | “추출 가능한 데이터” may include line/axis terms, but not explicitly requested | needs reread |
| `space_redeposit_candidate` | extraction result should return to space, but instruction does not explicitly request record writing | needs reread |

### 7. Usable / Hold / Needs Reread

Usable:

- object scope = input texts only
- lens = engine-language extraction
- return = candidate/evidence/classification
- guard = no broad scan

Hold:

- final glossary
- UI wording patch
- canonical term replacement
- new camera creation

Needs reread:

- whether extracted candidates should become line candidates
- whether the run should write an actual record into space or only return record candidates
- which input texts are included if the user does not provide explicit refs

### 8. 3-Surface Projection Summary

User surface:

- show a short decision summary
- “these are extractable engine-language candidates”
- let user decide use / hold / ask another pass

VectorFL surface:

- show applied lens
- show object scope
- show guards
- show candidate/evidence/classification table
- decide whether line/axis reread is needed

Engine surface:

- show extraction input boundary
- show extracted candidate categories
- show uncertainty and failure notes
- do not claim final glossary or canonical memory

### 9. Record / Redeposit Candidates

Record candidates:

- lens: `engine_language_extraction`
- camera: `Integrated operating camera` reuse
- object scope: `space input texts only`
- guard: `no broad scan / no final glossary / candidate only`
- candidate table
- unresolved reread points

Redeposit status:

```text
record candidate only
not canonical
not final glossary
needs user or VectorFL decision before write-back
```

## 6. One-Line Lock

User instructions must be interpreted through fixed 3 surfaces, scoped object, selected lens, existing camera reuse, explicit guard, expected return, surface projection, and record/redeposit candidates before execution expands.
