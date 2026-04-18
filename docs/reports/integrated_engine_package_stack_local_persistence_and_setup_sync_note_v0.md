# Integrated Engine Package Stack Local Persistence And Setup Sync Note v0

## verdict
PASS_WITH_NOTE

## purpose

This patch adds the minimum structural stability needed to keep using the current surface while iterating:

- package stack survives browser refresh through localStorage
- selected package is remembered
- selected package initializes the central engine setup/prompt area

This is still not a backend runtime package registry.

## implementation

### `VectorFLIntegrationShell.tsx`

Added localStorage keys:

- `integrated_engine_package_stack_v0`
- `integrated_engine_selected_package_v0`

The package stack now loads from localStorage when available and writes changes back when packages are added or deleted.

The selected package is passed into `CliHostControlPanel`.

### `CliHostControlPanel.tsx`

Added `activePackage` prop.

When the active package changes, the panel now:

- sets `purpose` from the selected package title/summary
- sets `promptPayload` from selected package stage/executor/summary
- adds a local transcript turn labeled `package selected`
- adds an engine position event labeled `package selected`

## current interpretation

The left rail is now:

```text
user-side work assignment
-> package stack
-> selected package controls central workbench
```

The `engine setup / package controls` area is now:

```text
CLAUDE.md / spec.md / context-ref-like setup area
-> reading lens
-> package purpose / instruction
-> engine context refs / spec inputs
```

## boundaries

This patch does not:

- persist packages to runtime contracts
- create durable package records
- run packages in parallel
- attach Gemini CLI
- start real package lifecycle automation

## validation

- `npm run build` passed in `app/ui/integrated_engine`.

## next valid use

Use the current browser surface for small work trials. If package stack behavior feels right, the next step is to bind package creation to a real runtime contract instead of localStorage.
