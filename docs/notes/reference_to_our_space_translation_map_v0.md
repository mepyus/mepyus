# Reference To Our Space Translation Map v0

## Purpose

This note maps the reference repo types into our own spaces.

The key rule is:

- do not import by feature name first
- import by **structural type**
- then decide which of our spaces can hold that structural type without distortion

## Our Main Spaces

For the current problem family, the important spaces are:

- `docs/specs`
- `docs/notes`
- `app/work`
- `app/core`
- `runtime/views`

Two reminders from our own status surfaces matter here:

- [app/work/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/work/folder_status.md) says this is a mixed experimental/workbench space and that the status file is not the ledger but a rendered reading surface.
- [runtime/views/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/folder_status.md) says this is also not the ledger but a reading surface.

So:

- `app/work` is a bench
- `runtime/views` is a presentation/readout surface

Neither should be mistaken for core doctrine or core runtime logic.

## Translation Rule

When reading a reference, ask:

1. Is this a doctrine/policy/contract reference?
2. Is this an experiment loop reference?
3. Is this a bounded package-local engine reference?
4. Is this a shared operating-layer reference?
5. Is this a product/control-plane decomposition reference?

Then translate by space.

## Space Mapping

### `docs/specs`

Use this space for:
- normative reading contracts
- bounded rule locks
- future patch scope constraints
- canonical judgment vocabulary

Best-matching references:
- `everything-claude-code-main` when it provides policy or contract docs
- `claw-code-main` when it clarifies runtime separations worth formalizing
- `openclaw-main` when it clarifies control-plane separation at the concept level

Examples:
- `everything` `SESSION-ADAPTER-CONTRACT` belongs conceptually here
- `everything` `SKILL-PLACEMENT-POLICY` also behaves like this

What should not land here:
- small loop shell tricks
- one-off plugin packaging details
- experiment-only heuristics

### `docs/notes`

Use this space for:
- landscape memory
- import ledgers
- structure readings
- comparison notes
- translation maps like this one

Best-matching references:
- all of them

This is where reference repos can be preserved without prematurely forcing them into product truth.

### `app/work`

Use this space for:
- experiments
- bounded reread loops
- validation harnesses
- audit surfaces
- small operator prototypes

Best-matching references:
- `ralph-main`
- `autoresearch-master`
- `claude-code-main`
- selected pieces of `everything-claude-code-main`

Why:

#### `ralph-main`

Its structure is:
- fresh loop
- external memory
- small state artifacts

This belongs in `app/work` because it is an experimental repetition discipline, not a core runtime substrate.

#### `autoresearch-master`

Its structure is:
- fixed eval
- one editable lane
- keep/discard discipline

This is also `app/work` material because it helps us tighten experimental corridors before touching the core.

#### `claude-code-main`

Its strongest import value is:
- plugin-local small engines
- lightweight hooks
- bounded local state files

Those are excellent prototypes for:
- small validators
- guard experiments
- narrow workbench operators

But they are usually too local/package-shaped to be our immediate doctrine layer.

#### `everything-claude-code-main`

Selected pieces map here when they are still exploratory or operator-facing:
- workspace audit patterns
- orchestration snapshots used for bench observation
- inspection/report ideas used before full core adoption

### `app/core`

Use this space for:
- actual runtime logic
- reusable reader core
- normalized internal traces
- cross-run stable invariants

Best-matching references:
- `claw-code-main`
- `everything-claude-code-main`
- selected decomposition ideas from `openclaw-main`

Why:

#### `claw-code-main`

It gives:
- structured session concepts
- hook/core separation
- permission/fallback reason separation
- compaction/continuation treatment

These are core-runtime imports.

#### `everything-claude-code-main`

It gives:
- shared adapter ideas
- canonical snapshot contracts
- state-store/query layer thinking
- inspection on normalized records

These belong in `app/core` only when we decide the pattern should become reusable internal infrastructure, not just a workbench tool.

#### `openclaw-main`

It gives:
- domain decomposition
- session/routing/security separation
- composition from small explicit domains

These are `app/core` references at the structural level, especially when our core risks becoming blob-like.

### `runtime/views`

Use this space for:
- readouts
- operation boards
- rendered artifacts
- thin inspection surfaces

Best-matching references:
- the output side of `everything-claude-code-main`
- small presentation/report aspects of `openclaw-main`

Important rule:

Reference patterns should land here only as **surface rendering**.
Do not import evaluation logic, core judgment logic, or experiment loop logic directly into this space.

This follows our own self-description:
- `runtime/views` is a reading surface, not the ledger

## Repo-by-Repo Mapping

### `claude-code-main`

Primary translation target:
- `app/work`

Secondary target:
- `docs/notes`

Rare direct target:
- `app/core`, but only after a plugin-local engine has been generalized

Reason:
- its main strength is small packaged engines and focused hook logic
- this is better for prototyping and bounded guard layers than for immediate core doctrine

### `everything-claude-code-main`

Primary translation targets:
- `docs/specs`
- `app/core`
- `docs/notes`

Secondary target:
- `app/work`

Reason:
- it already thinks in shared contracts, adapters, state, inspection, and operating surfaces
- that makes it valuable for both doctrine and reusable infrastructure

### `claw-code-main`

Primary translation target:
- `app/core`

Secondary targets:
- `docs/specs`
- `docs/notes`

Reason:
- it is a runtime substrate reference
- its value is strongest where we need stable internal separations

### `openclaw-main`

Primary translation targets:
- `app/core`
- `docs/specs`

Secondary target:
- `runtime/views`, but only for operator-surface shape, not logic

Reason:
- it is a product/control-plane decomposition reference
- it helps at the large-shape level, not usually for small bench experiments

### `ralph-main`

Primary translation target:
- `app/work`

Secondary target:
- `docs/notes`

Reason:
- it is a repetition discipline reference
- it should stay as bounded experiment logic unless proven and generalized

### `autoresearch-master`

Primary translation target:
- `app/work`

Secondary target:
- `docs/notes`

Reason:
- it is a narrow experimental discipline reference
- it sharpens mutation/eval lanes before core adoption

## Practical Import Rule

If a reference is:

- **small-package local engine**
  -> start in `app/work`

- **shared adapter / snapshot / state infrastructure**
  -> consider `app/core`

- **policy / contract / placement rule**
  -> `docs/specs`

- **landscape / comparison / translation memory**
  -> `docs/notes`

- **rendered board / summary / operator display**
  -> `runtime/views`

## Current Most Important Implication

For our current sentence-connection problem family:

- `claude-code-main` style imports should usually start as `app/work` experiments or narrow guards
- `everything-claude-code-main` style imports are the ones most likely to matter for `docs/specs` and later `app/core`
- `runtime/views` should remain thin and should not become the place where imported logic quietly accumulates

That keeps us from importing a good idea into the wrong layer and then mistaking the layer for the idea itself.
