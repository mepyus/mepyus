# Integrated Engine Today / Body / Camera / Lens / Space Reread v0

## 1. Verdict

PASS_WITH_NOTE.

Today's work was useful, but the first half approached the problem too much as UI construction. The corrected reading is that today's visible patches were only a surface symptom of a deeper operating model:

```text
fixed body
+ reusable camera
+ selected lens
+ space records
-> surface-specific projection
-> record back into space
```

## 2. What Was Wrong In The Early Approach

The early work treated new pressure as new visible UI:

- CLI pressure -> CLI panel
- language pressure -> language 담당 loop panel
- assignment pressure -> team/role panel
- engine return pressure -> engine return panel
- shared-object pressure -> shared spine

Those pieces are not useless. They are data. But the early approach made too many of them front-facing at once.

The real problem was not lack of panels. The real problem was not enough separation between:

- fixed body
- reusable process camera
- applied lens
- space material
- surface projection

## 3. Corrected Reading Of Today's Work

### CLI On-Top Work

Wrong early reading:

```text
Add a CLI panel so the user can run Codex.
```

Corrected reading:

```text
CLI is a tool layer that can be called inside a camera, usually mediated through VectorFL, and its result must re-enter the fixed 3-surface body.
```

### Language 담당 Loop

Wrong early reading:

```text
Build a language loop feature.
```

Corrected reading:

```text
The language loop is one lens-applied instance of a reusable process slot.
The loop matters less than the lens and object it reads.
```

With a different lens, the same loop slot can become:

- Koreanization / language sync
- line extraction
- validation / drift reread
- implementation material extraction
- flow reading

### Shared Spine

Wrong early reading:

```text
Show shared state everywhere.
```

Corrected reading:

```text
Show only enough common identity to keep the work package from disappearing across surfaces.
The detailed reading belongs to the current surface lens.
```

### Generated Panels

Wrong early reading:

```text
If the panel is not directionally right, ignore it or overwrite it.
```

Corrected reading:

```text
Generated panels are evidence. They show intention, misread, reusable material, overexposure, and support-layer candidates.
```

## 4. Engine Three-Surface Reread

### User Surface

Current corrected role:

- purpose
- assignment
- decision
- hold
- team/role operation

What it should not carry:

- full evidence atlas
- engine internals
- full VectorFL mediation reasoning
- raw CLI trace

Today's correction moved User closer to this by collapsing team/role configuration into support and keeping assignment/decision reading in front.

### VectorFL Surface

Current corrected role:

- lens recognition
- evidence bundle reading
- route / guard / mediation
- reread / reflux
- deciding whether a work package is formed enough to move

What it should not become:

- generic CLI console
- line browser as center
- all-purpose dashboard

Today's correction moved VectorFL closer to this by lowering line atlas/inspection to support and foregrounding mediation, packet formation, and reread.

### Engine Surface

Current corrected role:

- request material
- process boundary
- return material
- validation/extraction/deposit candidate

What it should not become:

- user decision board
- VectorFL reasoning surface
- control room
- broad return feed

Today's correction moved Engine closer to this by demoting the legacy generated mock into support/design clay and keeping request/process/return/validation in front.

## 5. Space Reread

Space is where lines, connections, axes, records, failures, and generated artifacts accumulate.

Today's key correction:

```text
Do not treat space as content to dump into all surfaces.
Treat space as the source material that cameras and lenses reread.
```

Space growth means:

- more lines
- more connections
- more axes
- more records
- more sedimented traces
- more generated artifacts to reread

Engine growth means:

- more reusable cameras
- more camera variations
- more lenses
- better lens-to-surface projection rules

The two growth modes should not be collapsed.

## 6. Camera / Lens Reinterpretation Of Today's UI Patches

| today's patch/work | corrected classification | reuse implication |
| --- | --- | --- |
| support-layer pruning | surface exposure camera variation | reuse when front/support/hidden density drifts |
| surface language exposure patch | human-readable exposure lens/camera | reuse when internal labels dominate first-pass reading |
| current work package projection refactor | shared object projection camera | reuse before multi-work board or persisted state work |
| candidate route label exposure patch | authority/route surface-language lens | reuse when marks become action wording |
| VectorFL reread queue wording patch | mediation action exposure lens | reuse when tool wording hides process meaning |
| language 담당 loop | lens-applied work slot | do not hard-code; vary by lens/object |

## 7. New Operating Frame Candidate

The user described the main mechanism as:

```text
CLI/User instruction
-> VectorFL organizes / translates / packetizes
-> Engine processes: line generation / line translation / line extraction / flow reading
-> VectorFL reads / judges / classifies / reorganizes / reinserts
-> User team/role receives work, acts, records, and requests back if needed
-> all surfaces record and redeposit into space
-> repeated loop
```

This is not a separate feature. It is the main integrated-engine operating frame candidate.

It should be treated as:

```text
Integrated Engine Lens-Applied Operating Camera
```

Potential camera stages:

1. instruction intake
2. lens/object recognition
3. internal search / evidence bundle
4. VectorFL packetization
5. Engine processing
6. VectorFL reread / classification / route decision
7. User assignment / decision / team work
8. record / sedimentation into space
9. re-entry when needed

## 8. Lens Examples For The Same Camera

| lens | object read | likely engine process |
| --- | --- | --- |
| language_sync | user/Codex meaning mismatch | internal language line extraction, bridge-note harvest, ambiguity classification |
| Koreanization | internal space language -> Korean operating language | phrase harvest, operating-language candidate, preservation boundary |
| line_extraction | raw/generated records -> lines/connections | line generation, relation/gap extraction, axis candidate |
| flow_reading | work records -> process flow | route reading, bottleneck, reflux path |
| validation | return/output -> fit/drift | anchor comparison, weak evidence, reprocess/hold |
| implementation | instruction -> bounded patch | file scope, do/do-not guard, return note |

## 9. What Should Be Done Next

The next work should not be another UI patch by default.

First create/lock a small mechanism spec:

```text
Integrated Engine Lens-Applied Operating Camera v0
```

It should define:

- camera stages
- lens slot
- object slot
- body projection rule
- space redeposition rule
- reuse-before-create rule
- example instance: language_sync / Koreanization loop

Then the existing User language 담당 loop can be reinterpreted as the first instance of that frame, not as a fixed feature.

## 10. What Must Remain Closed

- No fourth surface.
- No hard-coded new loop per task.
- No multi-work board until single work-package projection remains stable.
- No final glossary.
- No automatic canonical ingestion.
- No new camera without existing-data reread.
- No new lens without checking whether a current lens variation works.

## 11. One-Line Close

Today should be reread as the day the work moved from “building panels for CLI and loops” to “treating the engine as a fixed body whose cameras and lenses grow by rereading space.”
