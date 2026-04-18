# Integrated Engine Precedent Fragment Taxonomy v0

## Status

PASS_WITH_NOTE

This taxonomy classifies mined internal traces.
It is not a glossary and does not promote fragments into cameras or lenses.

## Boundary Rule

```text
fragment is not yet camera/lens
```

A fragment is evidence.
It can support reuse, variation, hold, rollback, or later review.
It must not be generalized into a full frame only because its name is attractive.

## Taxonomy

| fragment type | definition | how to recognize it | useful for | can be confused with | do not overclaim | store/reference |
|---|---|---|---|---|---|---|
| camera-frame fragment | A partial reusable process shape across assets. | Repeated sequence or role pattern appears in multiple records. | camera reuse/variation review. | full camera. | Do not call it promoted camera. | probe result, review note, frame candidate log. |
| camera-slot fragment | A recurring role like scope, tension, mechanism, support. | One segment role appears clearly in an asset. | slot naming and slot boundary refinement. | whole frame. | Do not infer all C0-C6 from one slot. | slot review table. |
| lens fragment | A repeated reading purpose or interpretive angle. | The same object can be read differently under purpose. | lens draft and routing. | final lens registry. | Do not finalize name or usage. | lens draft / mining log. |
| lens-slot compatibility hint | Evidence that a lens fits or weakly fits a slot. | A lens repeatedly reads one slot well. | compatibility matrix. | universal lens. | Do not let one lens cover all slots. | lens-slot matrix note. |
| target-shape rule | A rule about what asset shapes can or cannot be probed. | Content-bearing vs intake-only distinction appears. | usage boundary and probe gate. | content taxonomy. | Do not judge asset value, only probe suitability. | usage boundary / target gate. |
| support placement rule | Evidence that support must attach to a core segment. | Guard, contrast, limitation, or decision aid needs a host segment. | C6 discipline. | support as new center. | Do not promote support to core. | support placement check. |
| rollback rule | A rule for stopping or returning safely. | A failure condition has a named rollback destination. | recovery checklist and procedure. | rejection. | Rollback is not deletion. | rollback discipline. |
| failure signal trace | A concrete trace of frame forcing, drift, or mismatch. | A prior attempt went wrong or partial. | detection and prevention. | proof of uselessness. | Do not discard; keep as data. | failure/rollback log. |
| naming candidate | A possible name that improves neutrality or clarity. | Name reduces domain-specific residue. | candidate naming review. | glossary. | Do not final-label it. | naming note. |
| naming drift warning | A name that risks overclaiming or wrong scope. | Name sounds final, too broad, or content-specific. | preventing glossary/camera drift. | naming candidate. | Keep separate from naming candidate. | drift warning note. |
| false precedent | A source that looks relevant but would mislead reuse. | Same word appears but role/shape differs. | avoiding wrong reuse. | weak precedent. | Do not silently drop; record why false. | rejected fragment log. |
| asset-specific pattern | A useful pattern that belongs only to one asset or shape. | It works locally but fails transferability. | asset-specific reading. | reusable camera fragment. | Do not generalize. | asset-specific note. |
| review-stage boundary clue | Evidence about what review may do but promotion may not. | "eligible, not promoted" or similar status boundary appears. | status discipline. | promotion permission. | Do not treat as use approval. | review bundle summary. |
| promotion blocker clue | Evidence that promotion remains unsafe. | Missing usage procedure, target-shape boundary, rollback attachment. | blocker list. | failure. | Blocker may be actionable, not fatal. | review note / blocker table. |

## Fragment Handling Rules

1. Extract the fragment with evidence.
2. Assign one primary type.
3. Add secondary notes only if needed.
4. Check false-friend risk.
5. Decide reuse / variation / lens-only / asset-specific / new-candidate.
6. Record rejected and unresolved fragments.

## Naming Candidate vs Naming Drift Warning

Naming candidate:

- improves content neutrality
- reduces domain-specific residue
- helps distinguish lens/camera/slot

Naming drift warning:

- sounds final
- sounds canonical
- hides asset-specific content as frame
- turns support into core
- turns lens into glossary

Keep them separate.

## False Precedent Rule

False precedent must be logged when:

- the same term appears but function differs
- a support note looks like a core frame
- an intake note looks like content-bearing material
- a naming match hides target-shape mismatch

False precedent is still useful because it prevents repeated mistakes.

## Verification

- Fragment taxonomy is not a glossary: yes.
- Naming candidate and naming drift warning are separated: yes.
- False precedent is explicitly classified: yes.
- Fragment cannot become camera/lens by itself: yes.

## Pointers

- Mining protocol: `docs/reports/integrated_engine_internal_camera_lens_precedent_mining_protocol_v0.md`
- Decision bridge: `docs/reports/integrated_engine_precedent_mining_to_decision_bridge_v0.md`
- Excavation discipline: `docs/reports/integrated_engine_precedent_excavation_discipline_v0.md`
