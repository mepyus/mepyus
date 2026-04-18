# Integrated Engine Body / Camera / Lens Reread Correction v0

## 1. Verdict

HOLD_PANEL_FIRST_WORK

The user's correction is valid.

Recent implementation treated visible panels as if they were the structure. That is wrong. The structure already exists:

```text
body = fixed 3 surfaces
camera frame = common process / internal structure
lens = current task purpose
```

The next UI work should not add more panels. It should make the existing screen compose the same work package through different surface lenses.

## 2. Source Reread Basis

This correction is based on rereading:

- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/04-17/바디 정리5.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/04-17/통합엔진 구조화 3.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/04-17/패널 정리 1.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/04-17/언어 매핑 2.md`
- `docs/specs/multi_lens_document_reading_v0_architecture_and_operating_state_spec.md`
- `docs/specs/integrated_engine_surface_object_mapping_contract_v0.md`
- `docs/reports/integrated_engine_body_packet_memory_lock_v0.md`
- `docs/reports/integrated_engine_existing_panel_reuse_process_mapping_v0.md`

## 3. Corrected Core Meaning

The screen is not supposed to become:

```text
panel list + many labels + user reads everything
```

It is supposed to become:

```text
one body
one common camera frame
many task lenses
surface-specific projections
```

In simpler terms:

```text
same work package
-> User sees decision / assignment
-> VectorFL sees interpretation / evidence / branch
-> Engine sees process / return / extraction
```

## 4. Body

The body is the fixed three-surface structure.

| body part | role | must not become |
| --- | --- | --- |
| User Surface | organization / assignment / approval / priority / constraints | full engine trace viewer |
| VectorFL Surface | interpretation / mediation / internal-search trigger / route / reflux | generic CLI console or line browser |
| Engine Surface | input / generation / translation / extraction / flow / structure execution | control room or user decision board |

The body is not a visual layout preference. It is the operating skeleton.

## 5. Camera Frame

The camera frame is the common process that every lens should pass through:

```text
instruction intake
-> internal search
-> evidence bundle
-> VectorFL mediation / packetization
-> User organization
-> Engine main processing
-> VectorFL reflux
-> record / sedimentation
```

This is not a checklist to show as eight cards.

It is the camera frame that decides which part of the work package each surface should see at a given moment.

## 6. Lens

The lens is the current task purpose.

Examples:

- Koreanization / translation lens
- validation lens
- implementation lens
- self-learning lens
- structure / alignment lens
- external material analysis lens

The lens does not replace the body.
The lens does not add a new surface.
The lens changes what each surface foregrounds.

## 7. What Was Misread

I treated the work like:

```text
new concern -> new panel or focus block
```

But the correct move is:

```text
new concern -> identify lens
-> pass through common camera frame
-> project into each surface differently
-> reuse existing panels only as local views
```

The current screen is not wrong because the panels are useless.
It is wrong because too many panels are being shown as if they are all equally central.

## 8. Corrected Screen Principle

One work package should be transformed into three surface readings.

### User Projection

Question:

```text
What must I decide, assign, approve, hold, or open?
```

Visible density:

- low to medium
- human-readable first
- internal labels only as badges

Should hide or collapse:

- full evidence bundle
- engine logs
- raw artifact paths
- VectorFL branch reasoning details

### VectorFL Projection

Question:

```text
How should this work be interpreted, grounded, routed, reread, or held?
```

Visible density:

- highest
- evidence / branch / guard / route detail is allowed

Should not become:

- pure CLI console
- full team assignment desk
- line browser as center

### Engine Projection

Question:

```text
What process should run, what returned, what can be extracted or validated?
```

Visible density:

- process-focused
- not user-decision-focused

Should hide or collapse:

- User assignment mechanics
- VectorFL full mediation chain
- global governance / supervisor authority

## 9. Camera-Lens Composition Rule

Before changing UI, do this:

```text
1. identify current lens
2. identify current process stage in the camera frame
3. derive surface projections
4. reuse existing panels only where they serve that projection
5. hide/collapse everything that belongs to another surface's lens
```

This is the missing 5 x 6 explanation.

It is not enough to recite:

```text
User / VectorFL / Engine
purpose / memory / process / decision / sedimentation
packet frame / evidence / guard / trace
```

The UI must show why:

```text
same work package + different surface lens = different visible composition
```

## 10. Immediate Correction Path

The immediate correction is not new code for new panels.

It is a composition pass over the existing screen:

1. choose one active lens, such as `translation / Koreanization`
2. map the current work package through the common camera frame
3. create three surface projection rules
4. reorder/collapse existing panels according to the projection
5. keep shared spine as orientation only

## 11. What Must Not Be Done Next

- do not add a new panel for body/camera/lens
- do not implement multi-work board yet
- do not make every surface show all object fields
- do not turn User into engine trace reader
- do not turn Engine into VectorFL reasoning surface
- do not turn VectorFL into all-purpose dashboard
- do not keep implementing from memory without rereading source materials

## 12. Locked One-Line Correction

```text
The screen must not show all information everywhere.
It must show the same work package through the User, VectorFL, and Engine lenses,
inside the fixed body and common process camera frame.
```

## 13. 2026-04-17 Clarification: Loop Is Not The Point, Lens Is

The language-owner loop on the User surface is an example, not the core structure.

The important reading is:

```text
same loop / same process
-> different lens
-> different object of reading
-> different surface projection
```

For example, the current language-owner loop should not be understood as “a fixed language feature.” It should be understood as a loop/process slot whose object can change:

- language / Koreanization lens: read internal space language and collect Korean operating-language data
- line extraction lens: read the same space for repeated lines and connection candidates
- validation lens: read the same space for drift, weak evidence, and unresolved route state
- implementation lens: read the same space for executable patch material and return boundaries

This matters because the user's wording can change while the intended meaning stays stable, or the user's wording can look similar while the object of the lens changes. The integrated engine must reduce that sync error.

The correct interpretation is:

```text
body = where the engine process is read
camera = how the process is framed and passed through
lens = what object/purpose the process is currently reading
```

Therefore, a UI element such as the language loop should not harden into a single-purpose feature too early. It should be treated as a reusable process slot whose lens and object can be changed after VectorFL reread.

The user-facing problem is not merely Korean translation. The deeper problem is human/Codex sync:

- different user words may point to the same intended axis
- the same user word may point to a different object under a different lens
- internal space language must be interpreted into human-readable lines without flattening the axis

This is why generated artifacts, wrong interpretations, and repeated corrections are data. They help identify where the lens/object sync failed.
