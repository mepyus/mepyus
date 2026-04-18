# Integrated Engine Lens-Applied Operating Camera v0

## 1. Verdict

PASS_WITH_NOTE.

This document locks a small mechanism frame, not a new feature. The integrated engine body remains fixed. The camera is the reusable operating process. The lens decides what the camera reads.

## 2. Purpose

The purpose of this frame is to avoid hard-coding a new loop, panel, or route for every new task.

Instead, a task should be read as:

```text
fixed body
+ selected camera
+ selected lens
+ selected object
+ space evidence
-> surface-specific projection
-> records back into space
```

This lets the engine reuse existing process frames before inventing new ones.

## 3. Fixed Body

The body is fixed:

- User surface
- VectorFL surface
- Engine surface

No camera or lens creates a fourth surface.

### User Surface

Primary responsibility:

- purpose
- assignment
- decision
- approval / hold
- team / role operation

### VectorFL Surface

Primary responsibility:

- lens/object recognition
- evidence bundle reading
- mediation / route / guard
- reread / reflux
- deciding whether the work package can move

### Engine Surface

Primary responsibility:

- request material
- processing boundary
- line generation / translation / extraction / flow reading, when applicable
- return material
- validation / extraction / deposit candidate

## 4. Camera Definition

A camera is a reusable operating process frame.

It is not:

- a visible panel
- a new surface
- a one-off feature
- a checklist that must be fully displayed everywhere

It is:

- the path material passes through
- the rule for what each surface needs to see
- the mechanism by which a lens becomes work

## 5. Lens Definition

A lens is the interpretive purpose applied to a camera.

It answers:

```text
What are we reading this material as?
```

A lens can change without changing the body or camera.

Example:

```text
same camera + language_sync lens -> meaning-sync material
same camera + line_extraction lens -> line/connection material
same camera + validation lens -> drift/weak-evidence material
same camera + implementation lens -> bounded patch/return material
```

## 6. Object Slot

The object slot says what the lens is reading.

Examples:

- today's generated patch notes
- CLI turn return
- internal language harvest
- line candidate records
- user's latest instruction
- engine return material
- misread / correction trace

The same lens can read different objects. The same object can be read through different lenses.

This is the sync-critical point: different user words may point to the same axis, and the same word may point to a different object under a different lens.

## 7. Default Camera Stages

This v0 frame uses the current integrated operating camera:

1. Instruction intake
2. Lens / object recognition
3. Internal search / space reread
4. Evidence bundle formation
5. VectorFL packetization
6. Engine processing
7. VectorFL reread / classification / route decision
8. User assignment / decision / team work
9. Record / sedimentation into space
10. Re-entry if needed

This is a camera, not a required ten-card UI.

## 8. Stage Responsibilities

| stage | primary owner | what happens |
| --- | --- | --- |
| instruction intake | User / VectorFL | user or CLI instruction is received |
| lens/object recognition | VectorFL | decide what lens and object are active |
| internal search / space reread | VectorFL | find existing camera/lens/evidence before making new structure |
| evidence bundle formation | VectorFL | attach source refs, memory, generated artifacts, and known locks |
| VectorFL packetization | VectorFL | turn purpose/evidence/guard/expected return into work packet |
| Engine processing | Engine | execute line generation, extraction, translation, flow reading, validation support, or implementation work depending on lens |
| VectorFL reread / classification | VectorFL | classify return, decide hold/reprocess/reflux/route |
| User assignment / decision | User | assign to team/role, approve, hold, or request another mediation pass |
| record / sedimentation | all surfaces | User, VectorFL, and Engine each record their own trace back into space |
| re-entry | VectorFL | if needed, reopen as a new packet with prior records as evidence |

## 9. Projection Rule

The same work package must project differently.

| surface | should foreground | should keep as support |
| --- | --- | --- |
| User | purpose, assignment, decision, hold, team/role action | evidence detail, engine internals, full route trace |
| VectorFL | lens, object, evidence, guard, route, reread, mediation | raw tool logs unless needed |
| Engine | request, process boundary, return, extraction, validation/deposit candidate | user assignment mechanics, full VectorFL reasoning |

The shared spine should carry only enough common identity to avoid losing the current work.

## 10. Space Redeposition Rule

Each surface records a different kind of material back into space.

### User Records

- task decision
- assignment / hold
- team/role activity
- user-facing confusion or decision note

### VectorFL Records

- lens/object interpretation
- evidence bundle
- route/guard decision
- reread classification
- reflux / reprocess reason

### Engine Records

- processing input
- line generation / line translation / line extraction / flow reading output
- return material
- validation/extraction/deposit candidate
- failure or uncertainty note

These records are not final truth. They become space material for future reread.

## 11. Reuse-Before-Create Rule

Before creating a new camera:

1. Search existing docs/reports/specs/patch notes for a similar process frame.
2. If the camera exists, reuse it.
3. If the camera mostly fits, vary it.
4. If only the purpose changes, keep the camera and change the lens.
5. If no camera fits, create a new candidate camera and mark it as candidate.

Before creating a new lens:

1. Search existing language/line/validation/implementation/feedback material.
2. If the lens exists, reuse it.
3. If it is too broad, narrow the object.
4. If the reading object is genuinely new, create a lens candidate.
5. Do not promote the lens until real use proves it.

## 12. First Instance: Language 담당 Loop

The current User-surface language 담당 loop should be reinterpreted as:

```text
Integrated operating camera
+ language_sync / Koreanization lens
+ internal space language object
```

It should not be read as a hard-coded language feature.

### What It Reads

- internal space language
- user/Codex meaning mismatch
- generated misreads
- correction traces
- Korean operating-language candidates

### What Engine May Do Under This Lens

- language line extraction
- phrase/meaning candidate harvest
- ambiguity classification
- bridge note generation
- preservation-boundary detection

### What VectorFL Does

- decide whether the meaning was preserved
- classify confusion, drift, or useful line
- decide whether another reread is needed
- route to User team, Engine reprocess, hold, or space deposition

### What User Surface Does

- attach the work to language 담당 or another role
- decide whether to use, hold, or request another pass
- record the process as team/role activity

## 13. Other Lens Instances

| lens | same camera reads | engine process tendency |
| --- | --- | --- |
| line_extraction | generated records, source material, patch notes | line candidate generation, relation/gap extraction |
| flow_reading | operation logs and work records | route/bottleneck/reflux path detection |
| validation | return material and anchor/lock references | drift check, weak evidence classification, reprocess candidate |
| implementation | scoped instruction and repo evidence | bounded edit, return summary, verification note |
| external_support | missing evidence or expression gap | external material request candidate, not automatic browsing |

## 14. What Must Not Happen

- Do not add a new surface.
- Do not create one hard-coded loop per lens.
- Do not make every camera stage visible as a panel.
- Do not treat User as full evidence reader.
- Do not treat VectorFL as generic CLI console.
- Do not treat Engine as governance/control room.
- Do not turn space material into a raw dump on every page.
- Do not create a new camera/lens before rereading existing data.

## 15. Status

This is a v0 operating frame.

It is usable as a working interpretation guide, not a runtime schema.

It should guide:

- future UI composition
- language loop reinterpretation
- CLI-on-top route decisions
- generated artifact reread
- next camera/lens inventory expansion

It should not yet be used as:

- manifest schema
- database object
- final workflow automation
- final glossary

## 16. One-Line Lock

The integrated engine body is fixed; cameras are reusable operating frames; lenses decide what the camera reads; space supplies and receives the material; and every new task must reuse or vary existing cameras/lenses before inventing new structure.
