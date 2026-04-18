# Integrated Engine Package Stack Add/Delete And Setup Control Patch Note v0

## verdict
PASS_WITH_NOTE

## purpose

This patch makes the left package stack minimally operable and clarifies the role of the package control area.

The intended interpretation is:

```text
left package stack = user-side work assignment / package queue
center workbench = selected package instruction and CLI handoff
support setup = CLAUDE.md / spec.md / context-ref-like engine wrapper setup
right sidebar = selected package engine/process/structure reading
```

## changed implementation

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
  - Package stack is now React state, not only a static seed.
  - Added `Add package`.
  - Added selected-package `delete`.
  - New packages enter as:
    - `status`: queued
    - `stage`: purpose intake
    - `executor`: codex-ready
  - Selecting a package changes the center `Active Package Workbench` header.

- `app/ui/integrated_engine/CliHostControlPanel.tsx`
  - Renamed `support: packet controls` to `support: engine setup / package controls`.
  - Added explanatory copy:
    - this area is analogous to `CLAUDE.md` / `spec.md` / context refs
    - it sets the purpose, reading lens, and engine context before CLI handoff
  - Renamed fields:
    - `lens` -> `reading lens`
    - `purpose` -> `package purpose / instruction`
    - `bounded context refs` -> `engine context refs / spec inputs`

## current behavior

The user can now create a package from the left rail, select it, and delete the selected package.

This is still local UI state. It is not persisted to runtime package records yet.

## boundary

This patch does not:

- implement parallel execution
- create multiple Codex/Gemini sessions
- persist package stack entries
- bind new package creation to backend runtime contracts
- auto-read engine docs on package creation

## next valid action

If this interaction shape feels right, the next step is to bind `Add package` to a runtime package record and initialize the engine setup controls from that package's purpose.
