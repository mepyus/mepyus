# Integrated Engine Surface Slot Architecture v0

## 1. Verdict

PASS_WITH_NOTE

The integrated-engine UI now uses a shared slot logic:

```text
center slot -> support slot -> inspector slot
```

The slot logic is shared across User / VectorFL / Engine, but the visible content differs by surface.

## 2. Shared Slot Rule

### Center slot

The center slot answers the surface's first question.

It must stay small enough that the user can tell what the surface is for without opening details.

### Support slot

The support slot helps the current judgment.

It may include status cards, warnings, event summaries, compact session controls, and route hints. It should not become the main reading.

### Inspector slot

The inspector slot is x-ray detail.

It may include trace, provenance, full route/log history, packet formation detail, asset inventory, bridge reasoning, lower-input residue, and legacy mock detail.

## 3. Surface First Questions

| surface | first question |
| --- | --- |
| User | What am I trying to do, where am I, and what is the next valid action? |
| VectorFL | What is the currently interpreted package/object, in what state, with what evidence/blocker, and where can it route next? |
| Engine | What has the engine received, how far has processing gone, and what is being returned or redeposited? |

## 4. User Slot Contract

Center:

- current purpose
- scope
- current target
- current status
- next valid action

Support:

- current object focus
- material context summary
- recent changes summary
- decision signal
- lightweight assignment candidate

Inspector:

- full team routing detail
- full role configuration
- lower-input trace
- bridge reasoning
- packet origin detail
- route/log history

## 5. VectorFL Slot Contract

Center:

- selected package/object identity
- current interpreted state
- hold / usable / pending / review-needed
- concise evidence summary
- blocker/open edge summary
- next route hint

Support:

- compact session strip
- latest session result summary
- selected lens summary
- bridge diagnostic summary
- lower-derived / upper-added summary
- expanded evidence summary

Inspector:

- full evidence bundle
- recent turns
- latest return detail
- packet formation detail
- provenance / trace detail
- stop-rule reasoning
- lower-input residue detail

## 6. Engine Slot Contract

Center:

- ingest target
- current process stage
- validation state
- return / redeposit state
- output summary

Support:

- current object focus
- compact event or return metadata
- what was not done summary
- compact artifact summary

Inspector:

- full return record
- gate result detail
- runtime trace
- asset tree / manifest detail
- deeper validation rationale
- legacy engine mock

## 7. Boundaries

This architecture does not authorize:

- second-handler expansion
- team dashboard construction
- automation
- upper/lower unification
- generic task board growth
- treating lower-derived evidence as a complete upper packet

## 8. Validation

- Each surface has a cleaner first question.
- Center / support / inspector are distinct in the current shell.
- Same-process/same-projection confusion is reduced by slot labels and surface-specific projection.

