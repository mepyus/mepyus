# phase2 adjacent-surface candidate framing v1

## package status

complete for this turn

## premise

This framing starts from frozen `phase1`.

That means:

- no phase1 feature expansion
- no phase1 boundary rewrite
- no recommendation semantics
- no compare-track restart
- no hidden taxonomy hardening

The goal is only to narrow the next adjacent surface candidates to what most naturally follows phase1 without reopening it.

## candidate 1

### name

operating history / replay / trace reading surface

### 1. why it is needed

Phase1 is intentionally present-tense and thin.

It can show current run, recent activity, saved path, and seed context, but it does not provide a dedicated place to read longer lineage, replay path shifts, or inspect how current operating state formed over time. That gap is real, and it becomes more visible once phase1 is frozen rather than endlessly expanded.

### 2. why phase1 should not own it

If phase1 absorbs replay/history reading, `Operating` will drift from thin observation into dashboard bloat.

That would directly violate the frozen contract that keeps phase1 focused on current observation, path authoring, direct access, explicit saved path selection, and seed-based local re-query.

### 3. one-line role

A separate time-axis reading surface for lineage, replay, and traceability around the current operating state.

### 4. contact point with phase1

- `Operating` can hand off current asset or current run context
- `Memory` or `Similar` can hand off a saved path or seed context as a trace-reading anchor
- phase1 stays the entry surface; history/replay becomes the drill-down companion

### 5. non-intrusion guardrail

- do not move history reading into `Operating`
- do not let replay mutate phase1 shared spine by default
- do not turn trace reading into recommendation or workflow guidance
- do not let this surface redefine phase1 wording or state ownership

### 6. build readiness

Candidate-ready, but not immediate implementation-ready.

It is mature enough for a separate candidate note/package because the need is structurally clear and existing history/trace specs already exist. It still needs a narrow role lock before implementation so it does not become a giant general-purpose console.

### intrusion risk

Medium.

The main risk is that history/replay could swallow `Operating` and re-centralize too much reading into one large surface.

## candidate 2

### name

saved-path curation surface

### 1. why it is needed

Phase1 `Memory` is deliberately compact and selection-oriented.

As saved paths accumulate, there will likely be a need for a separate place to reread, sort lightly, cluster loosely, and curate explicit saved paths without forcing that work into `Memory` or `Similar`.

### 2. why phase1 should not own it

If phase1 `Memory` grows into a curation workspace, it stops being a compact saved-path selector and starts behaving like a larger working-memory application.

That would blur the distinction between:

- saved path selection
- seed activation
- broader rereading and curation

### 3. one-line role

A separate rereading and curation surface for explicit saved paths after they leave phase1’s compact Memory role.

### 4. contact point with phase1

- takes explicit saved paths from `Memory`
- can return a chosen saved path or curated subset back into `Memory` or `Similar`
- can preserve the rule that only explicit saved paths, not residue or search imports, enter the curation layer

### 5. non-intrusion guardrail

- do not let `Memory` become the curation surface
- do not auto-promote Similar results into curation
- do not turn curation into ontology or taxonomy design
- do not let curation redefine sticker, seed, or residue semantics

### 6. build readiness

Needs more maturation before promotion.

The need is plausible, but current saved-path volume and phase1 usage evidence are still thin. Promoting this too early risks building a surface for anticipated accumulation rather than observed pressure.

### intrusion risk

High.

The main risk is re-expanding `Memory` semantics and accidentally creating a heavier memory system before the need is proven.

## why this order after phase1

These two candidates follow most naturally because they address the two visible post-freeze pressures without reopening phase1:

- time-axis reading pressure
- saved-path accumulation pressure

The first is already backed by existing operating/history lineage material and has clearer structural pressure. The second is a plausible next pressure, but it depends more on future accumulation.

## why other candidates are not yet preferred

### richer Similar outside phase1

Not preferred yet because current `Similar` weakness is acknowledged, but expanding it too early risks recommendation drift and semantic overclaim. The boundary is locked, but the adjacent surface case is not yet clearer than the history/replay case.

### object-centered deep detail surface

Not preferred yet because it risks collapsing back into exploration detail expansion or a larger object viewer before there is a stable reason to separate that role.

### runtime source inspection companion surface

Not preferred yet because current provenance visibility already covers the user-facing need inside phase1. A separate source inspection companion would currently lean too close to debugging-panel proliferation.

## recommendation

Priority 1:

- operating history / replay / trace reading surface

Reason:

- it answers the clearest post-phase1 gap
- it has the strongest separation from phase1
- it already has adjacent spec material in the repo
- it is less likely than memory curation to create premature semantic expansion

## package incomplete

No.

This package is complete for its stated goal: narrowing phase2 adjacent-surface candidates to two or fewer and selecting one priority.
