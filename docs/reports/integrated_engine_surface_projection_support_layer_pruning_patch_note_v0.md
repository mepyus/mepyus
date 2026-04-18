# Integrated Engine Surface Projection Support-Layer Pruning Patch Note v0

## 1. Verdict

PASS_WITH_NOTE.

This round continued the previous surface projection correction. It did not add new capability. It reduced front-surface density by moving previously generated but still useful UI material into support layers.

## 2. Why This Patch Was Needed

The prior screen still carried too much information at the same visibility level. That made the integrated engine feel like a mixed board of panels rather than one work package being read through three different surface lenses.

The correction target was not removal. The generated panels remain data. They show intention, misread, reusable fragments, and partial structure. The fix is to preserve them while lowering their exposure when they are not the front reading of the current surface.

## 3. What Changed

### User Surface

The internal team / role configuration grid is now inside a collapsed support section:

- `support: team / role configuration`

The front User reading remains:

- current work-package assignment viewpoint
- assignment / decision / hold
- operating log
- assignment candidates

This keeps team and role structure available without making the User surface look like a generic team console.

### VectorFL Surface

The evidence line atlas and selected-line inspection are now collapsed support sections:

- `support: evidence line atlas`
- `support: selected line inspection`

VectorFL still keeps the densest reading role, but the front path now favors:

- current object focus
- mediation process
- CLI host control / packet formation
- validation / reread queue

Line and inspection material remains available as support evidence, not the central body.

### Engine Surface

The previous generated engine mock is now inside:

- `support: legacy engine mock / generated design clay`

The Engine front remains:

- request candidate
- process boundary
- return material
- validation / record candidate

This preserves the generated mock as design/material data while preventing it from competing with the actual Engine surface process reading.

## 4. What Was Preserved

- Existing generated UI material was not discarded.
- Existing User / VectorFL / Engine surface split was not changed.
- Existing CLI on-top structure was not changed.
- Existing internal team modal and language loop control remain available.
- Existing VectorFL line material remains available.
- Existing engine mock remains available as support/design clay.

## 5. What This Corrects

This patch corrects a visibility error:

- before: too many artifacts were front-facing at once
- after: each surface exposes only the material that belongs to its lens, while keeping other generated material as support

This is the concrete version of the body / camera / lens correction:

- body stays fixed
- camera/process stays common
- lens controls what is front, support, or hidden

## 6. Verification

Passed:

- `npm run build` in `app/ui/integrated_engine`
- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py app/core/runtime/viewer_server.py`

## 7. Remaining Watchpoints

1. If too many support sections accumulate, the screen can still feel like a panel archive.
2. If User surface needs frequent team editing, the collapsed team section may need a better compact assignment affordance, not a full re-expansion.
3. If VectorFL support evidence is always opened during real use, the evidence bundle/front relation needs another composition pass.

## 8. Next Smallest Step

Use one real current object and inspect the three surfaces:

- User: can the user assign/hold/decide without reading all internal evidence?
- VectorFL: can the user inspect evidence and route without losing the packet path?
- Engine: can the user read request/process/return without seeing all design clay?

If the answer is still no, the next step should be another exposure-budget pass, not new functionality.
