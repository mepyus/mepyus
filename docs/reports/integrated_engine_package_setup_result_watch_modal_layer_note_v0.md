# Integrated Engine Package Setup Result Watch Modal Layer Note v0

## verdict
PASS_WITH_NOTE

## purpose

This patch adds a bounded modal layer so package details do not overload the main surface.

The current main surface remains:

```text
package stack
-> active package workbench
-> engine position sidebar
```

The modal layer now handles deeper package-specific views:

- setup
- result
- watch

## implementation

### Package card actions

Selected package cards now expose:

- `setup`
- `result`
- `watch`
- `delete`

### Setup modal

Shows package-start setup material:

- package intent
- executor candidate
- initial route
- context refs
- line / axis watch
- guards

This corresponds to a `CLAUDE.md` / `spec.md` / context-ref-like setup surface, but it is not forced into a markdown-file workflow.

### Result modal

Shows result material from the latest return:

- session id
- status
- route
- return preview
- note that this is not final approval

This gives a deeper result view than the compact right sidebar summary.

### Watch modal

Shows bounded watch material:

- line reaction
- axis reaction
- internal exploration trigger
- redeposit route

The watch modal is explicitly manual-only. It does not auto-trigger internal exploration or package creation.

## current boundaries

This patch does not:

- implement real package automation
- persist modal state
- connect setup to backend package contracts
- auto-run internal exploration
- auto-detect line/axis reactions
- attach Gemini CLI

## validation

- `npm run build` passed in `app/ui/integrated_engine`.

## next valid use

Use the modal layer during real browser trials:

- open `setup` before sending a new package instruction
- open `result` after Codex returns
- open `watch` when line/axis reaction needs manual inspection

If this works in use, bind setup/result/watch data to real runtime package records later.
