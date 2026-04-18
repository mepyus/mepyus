# Integrated Engine Package Stack Shell Patch Note v0

## verdict
PASS_WITH_NOTE

## purpose

This patch adds the first bounded package-stack shell around the current active conversation workbench.

The intent is to prepare the UI for multiple work packages without pretending that real parallel execution exists yet.

## changed implementation

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
  - Added `PackageCard` model.
  - Added `packageStackSeed` with four sample package states:
    - active
    - returned
    - hold
    - queued
  - Added `PackageStack` left rail.
  - Added selected package state.
  - Reframed the center header as `Active Package Workbench`.
  - The center still shows one selected package at a time.

## current visible model

```text
left rail
  Package Stack
  active / queued / returned / hold counts
  selectable package cards

center
  Active Package Workbench
  selected package title / status / stage / executor
  Integrated Engine chat

right rail
  Engine Position
  Structure Reading
  latest return
```

## what this proves

The current page does not need to stretch one chat area to hold every future task.

The safer model is:

```text
many packages in stack
one selected active package in center
selected package's engine position on right
```

## what this does not prove

- It does not implement parallel execution.
- It does not start multiple Codex or Gemini sessions.
- It does not isolate worktrees.
- It does not persist package stack state yet.
- It does not make package cards authoritative runtime records.

## validation

- `npm run build` passed in `app/ui/integrated_engine`.

## next valid action

Use the current stack shell visually. If it feels right, the next step is to connect package cards to real runtime package records or CLI session groups, not to add more front panels.
