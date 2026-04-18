# VectorFL integrated engine three-surface reframe v0

## verdict

- implemented as a bounded surface-role reframe
- not a full UI rewrite
- not an engine-surface completion
- not a new worker orchestration pass

## surfaces

### user surface

Route:

- `/vectorfl-engine/operate`

Role:

- direct operating desk
- user writes purpose, team, assignee, worker/session, and execution path
- the primary question is: what should be assigned, who should own it, and where should it go next?

Kept here:

- purpose input
- team name
- team purpose
- assignee
- worker selection
- launch draft and execution controls
- human event feed

Not primary here:

- deep engine inventory
- manifest-first truth view
- line genealogy internals
- freshness gate as hero content

### VectorFL surface

Route:

- `/vectorfl-engine/vectorfl`

Role:

- line-first surface reader
- shows how the current operating material appears as line, relation, gap, genealogy, export, and reflux
- team/assignee/worker are not the primary axis here; they remain provenance when needed

Added units:

- line summary strip
- Line Atlas
- Selected Line Inspector
- Line Genealogy
- Relation Web
- Line Event Stream

Data source:

- prefers `latest_internal_read_report.line_seeds`
- also reads `latest_synthesis_report.confirmed_lines`
- falls back to current operating purpose/work packet only when no line seeds exist

### engine surface

Route:

- `/vectorfl-engine/engine`

Role:

- placeholder only in this pass
- reserved for internal material inventory and space status

Reserved units:

- inventory
- space status
- script / md / json access
- maintenance

## TSX mock alignment

Reference mock:

- `runtime/views/vectorfl_dual_surface.tsx`

Reason:

- the previous mock content already used TypeScript types, stateful arrays, modal draft state, and React component structure
- it is treated as the TSX reference surface for the user/vectorfl/engine split
- the live viewer still renders through the Python shell until a dedicated app build path is introduced

## implementation notes

Changed:

- `app/runtime/vectorfl_integrated_engine_shell.py`
  - added conservative line-surface view builders
  - added `vectorfl` and `engine` page modes
  - added surface switch for user / VectorFL / engine
  - kept existing operate execution and freshness gate behavior intact
- `app/core/runtime/viewer_server.py`
  - added `/vectorfl-engine/vectorfl`
  - added `/vectorfl-engine/engine`
- `runtime/views/vectorfl_dual_surface.tsx`
  - TSX reference asset retained under TSX extension

Intentionally not changed:

- no Gemini roundtrip validation
- no team/assignee first-class registry promotion
- no page/component build migration
- no engine inventory implementation
- no slot replacement or gate close logic

## why this split

The prior operating desk and rear-summary work made the engine operational, but it still risked letting engine-state language dominate every surface. This pass separates the reading lens:

- user surface: action and assignment
- VectorFL surface: line reaction and spatial reading
- engine surface: internal inventory and maintenance, deferred

This prevents the user-facing desk from becoming an engine status page and prevents the VectorFL surface from becoming a team/worker operations board.

## verification

- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_shell.py app/core/runtime/viewer_server.py`
- `/vectorfl-engine/operate` renders the user surface and keeps current freshness result labels
- `/vectorfl-engine/vectorfl` renders the line-first VectorFL surface
- `/vectorfl-engine/engine` renders placeholder inventory/status/script/maintenance blocks

## next

- add the mismatched completed execution freshness regression fixture before expanding the three-surface structure further
