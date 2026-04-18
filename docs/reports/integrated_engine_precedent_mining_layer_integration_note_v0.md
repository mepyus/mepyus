# Integrated Engine Precedent Mining Layer Integration Note v0

## Status

PASS_WITH_NOTE

Current status:

```text
eligible for provisional camera candidate, not promoted
```

This note connects the new precedent mining layer to the existing usage/review bundle.
It improves reuse and variation readiness.
It does not promote any camera.

## Why This Layer Is Needed

The current review bundle can tell whether a target is usable, how to run C0-C6, how to attach lenses, and how to rollback.
But before using or varying a camera/lens, the system needs one more earlier step:

```text
mine internal precedent before creating or varying structure
```

Without this layer, the system may:

- create a new camera when a fragment already exists
- invent a lens when an existing lens composition is enough
- mistake naming drift for naming candidate
- discard failed attempts that should become rollback evidence
- overfit an asset-specific pattern into a reusable frame

## Recommended Order

1. precedent mining
2. target-shape / usage boundary check
3. usage procedure
4. probe / review / rollback

Expanded:

```text
intent clarification
-> mining scope selection
-> source set selection
-> fragment extraction
-> fragment classification
-> false precedent check
-> reuse / variation / lens-only / asset-specific / new-candidate decision
-> handoff to usage boundary or usage procedure
-> probe / review / rollback if allowed
```

## Relationship To Existing Bundle

| layer | role |
|---|---|
| precedent mining protocol | Decide what existing internal traces should be considered before new structure. |
| fragment taxonomy | Prevent fragments from becoming full cameras/lenses too early. |
| source shortlist | Keep mining narrow and avoid broad scan. |
| mining-to-decision bridge | Decide reuse / variation / lens-only / asset-specific / new-candidate. |
| excavation discipline | Preserve accepted, rejected, false, unresolved fragments. |
| usage boundary | After mining, decide whether the target can use C0-C6. |
| usage procedure | Run C0-C6 only when boundary permits. |
| rollback integration | Stop, continue partial, or rollback with evidence. |

## When Mining Is Mandatory

Mining is mandatory when:

- user asks for a new camera
- user asks for a lens structure
- a new object type appears
- a previous pattern looks reusable
- a naming candidate appears
- a failed implementation or wrong reading may contain useful data
- target-shape is unclear
- camera variation is being considered

## When Mining May Be Skipped

Mining may be skipped only when:

- the task is a direct application of an already selected camera/lens
- target-shape has already been checked
- no new naming, slot, lens, variation, or precedent claim is being made
- the work is only filling an existing template with known evidence

Even then, status must remain:

```text
not promoted unless separately reviewed
```

## What Not To Do After Mining

Do not jump from mining to:

- camera promotion
- axis promotion
- glossary
- canonical ingestion
- UI implementation
- automation

Mining can hand off to:

- usage boundary
- usage procedure
- decision bridge
- asset-specific note
- optional probe
- hold

## Verification

- mining layer conflicts with usage bundle? no; it sits before it.
- mining can jump to promotion? no.
- mining -> decision bridge -> usage/review flow clear? yes.
- current system remains not promoted? yes.

## Bundle Pointers

- Mining protocol: `docs/reports/integrated_engine_internal_camera_lens_precedent_mining_protocol_v0.md`
- Taxonomy: `docs/reports/integrated_engine_precedent_fragment_taxonomy_v0.md`
- Source shortlist: `docs/reports/integrated_engine_internal_precedent_source_set_shortlist_v0.md`
- Decision bridge: `docs/reports/integrated_engine_precedent_mining_to_decision_bridge_v0.md`
- Excavation discipline: `docs/reports/integrated_engine_precedent_excavation_discipline_v0.md`
- Existing usage boundary: `docs/reports/integrated_engine_provisional_camera_candidate_usage_boundary_v0.md`
- Existing usage procedure: `docs/reports/integrated_engine_provisional_camera_usage_procedure_v0.md`
- Existing review bundle: `docs/reports/integrated_engine_provisional_camera_review_bundle_summary_v0.md`

## Final Self-Check

### 1. Created Docs Check

Created:

- `docs/reports/integrated_engine_internal_camera_lens_precedent_mining_protocol_v0.md`
- `docs/reports/integrated_engine_precedent_fragment_taxonomy_v0.md`
- `docs/reports/integrated_engine_internal_precedent_source_set_shortlist_v0.md`
- `docs/reports/integrated_engine_precedent_mining_to_decision_bridge_v0.md`
- `docs/reports/integrated_engine_precedent_excavation_discipline_v0.md`
- `docs/reports/integrated_engine_precedent_mining_layer_integration_note_v0.md`

Pointers are connected across the package.

### 2. Protocol Order Check

- precedent mining is before usage procedure.
- direct jump to new camera creation is blocked.

### 3. Taxonomy Check

- fragment, camera, lens, false precedent are separated.
- naming candidate and naming drift warning are separated.

### 4. Decision Bridge Check

- reuse branch exists.
- variation branch exists.
- lens-only branch exists.
- new candidate branch exists only as last resort.
- asset-specific branch is a valid endpoint.

### 5. Logging Check

- rejected fragments are logged.
- false precedents are logged.
- unresolved state is allowed.
- failed traces remain data.

## Final Verdict

PASS_WITH_NOTE

Most important verification result:

- camera/lens work must now pass through internal precedent mining before usage/review unless it is a direct application of an already selected camera/lens.

Most dangerous unresolved points:

1. mining could become broad scan if source shortlist is ignored.
2. a well-named fragment could still be overclaimed as a camera/lens.
3. false precedent must be recorded, not silently discarded.

Next valid action:

```text
Use the precedent mining protocol on the next camera/lens-related request before opening usage procedure or review.
```
