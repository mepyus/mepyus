# Integrated Engine Internal Camera / Lens Precedent Mining Protocol v0

## Status

PASS_WITH_NOTE

Current system status:

```text
eligible for provisional camera candidate, not promoted
```

This protocol sits before the existing usage/review bundle.
It does not promote a camera, create an axis, write a glossary, canonicalize, implement UI, or automate anything.

## Purpose

Before creating a new camera, varying an existing camera, or structuring a new lens, mine internal records for existing fragments.
The goal is to decide whether the work should reuse, vary, attach a lens, remain asset-specific, or only then become a new candidate.

## Protocol Sequence

| stage | stage purpose | input | action | output | failure signal | rollback destination | advance condition |
|---|---|---|---|---|---|---|---|
| 1. intent clarification | Name what kind of structure is being requested before mining starts. | user task, current work object, current status. | Classify intent as camera, camera variation, lens, lens reuse, asset-specific, or unclear. | intent verdict. | jumping straight to naming a camera/lens. | process recovery checklist; mark intent unclear. | intent class is explicit. |
| 2. mining scope selection | Keep mining narrow and relevant. | intent verdict. | Choose same-domain, cross-shape, correction, rollback, probe, review, or usage docs. | bounded mining scope. | broad scan, too many sources, source chosen by title only. | source shortlist; reduce to high-priority set. | scope is narrow and justified. |
| 3. source set selection | Pick concrete internal documents to inspect. | mining scope. | Select source docs from shortlist. | source set. | intake-note-only or metadata-only used as main precedent source. | source set gate; move them to support-only. | source set has content-bearing precedent value. |
| 4. precedent extraction | Pull fragments without overclaiming. | source set. | Extract camera/lens/failure/rollback/naming/support fragments. | fragment list with evidence. | fragment becomes full camera/lens immediately. | fragment taxonomy; downgrade to fragment. | fragments are typed and evidence-backed. |
| 5. fragment classification | Sort what kind of fragment each item is. | extracted fragments. | Classify by taxonomy. | typed fragment table. | naming candidate, drift warning, false precedent mixed together. | taxonomy check. | each fragment has exactly one primary type. |
| 6. false-friend / misleading precedent check | Prevent bad reuse. | typed fragments. | Check false precedent, context mismatch, naming drift, support inflation. | rejected/qualified fragment list. | attractive name used despite weak evidence. | excavation discipline; record false precedent. | false friends are named or absent. |
| 7. reuse vs variation vs new vs asset-specific decision | Turn mining into a safe next path. | classified fragments + false-friend check. | Choose reuse, vary, lens-only, asset-specific, or new candidate. | provisional decision. | "new camera" becomes default. | decision bridge. | branch has required evidence. |
| 8. handoff to usage/review bundle | Connect mining result to existing procedure. | provisional decision. | Send to target-shape gate, usage boundary, usage procedure, or hold. | handoff target. | mining result jumps to promotion. | usage/review boundary. | handoff does not exceed status. |
| 9. record / redeposit | Preserve the attempt as data. | final mining result. | Save excavation log with accepted/rejected fragments. | runlog / report / note. | rejected fragments disappear; unresolved is hidden. | excavation discipline. | next reader can restart from log. |

## Intent Clarification Branches

Choose one before mining:

- `new camera candidate needed?`
- `existing camera variation likely?`
- `new lens candidate needed?`
- `existing lens reuse likely?`
- `asset-specific reading only?`
- `unclear / insufficient case?`

If unclear:

- do not create a camera
- do not name a lens
- mine only for scope, comparable fragments, and failure traces
- stop with `not enough precedent yet` if evidence remains thin

## Mining Scope Selection Menu

Allowed narrow scopes:

- same-domain precedents
- cross-shape precedents
- correction notes
- rollback notes
- probe results
- review notes
- usage boundary / usage procedure / matrix documents
- failed attempts or partial matches

Disallowed:

- broad scan
- title-only source picking
- mining every report because one useful source was found

## Mandatory Verification

- Is this protocol placed before usage procedure? yes.
- Does it block jumping directly to new camera creation? yes.
- Can failure return to asset-specific reading? yes.
- Are rejected/false precedents recorded? yes, through excavation discipline.

## Pointers

- Fragment taxonomy: `docs/reports/integrated_engine_precedent_fragment_taxonomy_v0.md`
- Source shortlist: `docs/reports/integrated_engine_internal_precedent_source_set_shortlist_v0.md`
- Decision bridge: `docs/reports/integrated_engine_precedent_mining_to_decision_bridge_v0.md`
- Excavation discipline: `docs/reports/integrated_engine_precedent_excavation_discipline_v0.md`
- Integration note: `docs/reports/integrated_engine_precedent_mining_layer_integration_note_v0.md`
