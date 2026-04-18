# Integrated Engine Precedent Excavation Discipline v0

## Status

PASS_WITH_NOTE

This document defines how precedent mining sessions are logged.
It does not promote cameras, lenses, axes, glossary terms, or canonical records.

## Logging Principle

Precedent mining must leave a recoverable trace.
Rejected fragments, false precedents, and unresolved questions are part of the data.

## Required Excavation Fields

- excavation session id
- current task intent
- source set used
- extracted fragments
- rejected fragments
- false precedent notes
- reuse / variation / new / asset-specific provisional decision
- unresolved questions
- rollback destination
- handoff target document

## Minimal Excavation Log Template

```text
excavation_session_id:
date:
current_status: eligible for provisional camera candidate, not promoted

current_task_intent:
- new camera candidate needed? yes/no/unclear
- existing camera variation likely? yes/no/unclear
- new lens candidate needed? yes/no/unclear
- existing lens reuse likely? yes/no/unclear
- asset-specific reading only? yes/no/unclear

source_set_used:
- source:
  - reason:
  - source class: high-priority / supporting / boundary

extracted_fragments:
- fragment:
  - taxonomy type:
  - evidence source:
  - confidence: weak / usable / strong
  - use:

rejected_fragments:
- fragment:
  - why rejected:
  - false precedent? yes/no
  - keep as data? yes/no

false_precedent_notes:
- apparent match:
- why false:
- risk prevented:

provisional_decision:
- reuse existing camera
- vary existing camera
- reuse or attach lens only
- asset-specific reading
- truly new candidate needed
- not enough precedent yet

unresolved_questions:
- question:
  - needed evidence:

rollback_destination:

handoff_target_document:

not_promoted_boundary:
- camera promotion closed
- axis promotion closed
- glossary closed
- canonical ingestion closed
```

## Precedent Confidence Scale

| confidence | meaning | allowed use |
|---|---|---|
| weak | suggestive but not enough for branch decision. | keep as note; do not decide alone. |
| usable | enough to support reuse/variation/lens/asset-specific decision with other evidence. | use in decision bridge. |
| strong | repeated or highly explicit evidence with clear boundary. | can anchor decision, still not promotion. |

## Overclaim Warning

Do not overclaim when:

- one fragment is named well but has little evidence
- a support rule looks like a camera slot
- a target-specific pattern repeats only inside one asset
- a false precedent uses the same vocabulary but different role
- mining found no contradiction but also no positive evidence

## Not Enough Precedent Yet Rule

End with `not enough precedent yet` when:

- source set is too thin
- fragments are mostly weak
- false precedents outnumber usable fragments
- target-shape is unclear
- decision would require inventing a new slot or lens

This is a valid endpoint.

## Verification

- log records judgment, not just reading? yes.
- false precedent is recorded, not erased? yes.
- unresolved state is allowed? yes.
- rejected fragments remain data? yes.

## Pointers

- Protocol: `docs/reports/integrated_engine_internal_camera_lens_precedent_mining_protocol_v0.md`
- Taxonomy: `docs/reports/integrated_engine_precedent_fragment_taxonomy_v0.md`
- Decision bridge: `docs/reports/integrated_engine_precedent_mining_to_decision_bridge_v0.md`
