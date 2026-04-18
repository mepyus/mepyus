# Integrated Engine Input Folder Role Map v0

## 1. Verdict

PASS_WITH_NOTE

The current input-side folder structure is legible if read as overlapping layers, not as one clean pipeline. Some folders are source/input front layers, some are runtime transformation layers, some are display/view layers, and some are older ingest support zones that still carry real evidence.

No folder move or cleanup is proposed here.

## 2. Folder Role Map

| folder / zone | primary input-side role | surface / subsystem leaning | asset kind | zone type | confusion risk |
| --- | --- | --- | --- | --- | --- |
| `app/ui/integrated_engine/` | Current integrated-engine 3-surface operating UI | User / VectorFL / Engine shell | TSX components, UI state, shell panels | display / operation zone | Can be mistaken for the whole input system because it is visible; it is only the surface-side operating layer |
| `app/input_layer/` | Intake and fragmentization front layer | Legacy/deeper input front feeding engine | segmenter, labeler, anchorizer, source locator modules | source / transformation zone | Can be over-read as complete ingest truth; several parts are experimental or contract-first |
| `app/input_layer/segmenter/` | Splits source material into fragment candidates | Input front | experimental segmenters | transformation zone | Experimental files can be mistaken for stable production split engine |
| `app/input_layer/labeler/` | Normalizes external routing labels into core intake labels | Input front / normalization | labeler module | transformation zone | Can be over-expanded into all labeling; current role is narrower |
| `app/input_layer/anchorizer/` | Assigns anchor handles to input/fragments | Input front / provenance handle | anchorizer code | transformation zone | Anchor can be reduced to keyword tagging if its source-stabilizing role is missed |
| `app/input_layer/source_locator/` | Connects fragments back to source/origin | Input front / provenance ingress | locator and origin-map helper | source / support zone | Origin map helper is lightweight; it is not a full provenance graph |
| `app/work/observer_ingest_min/` | Minimal ingest execution path for raw/registry input | Older/deeper ingest support | runner, contracts, examples, generated outputs | source / transformation / trace zone | Not the whole engine; it is easy ingest + visible split + readable trace only |
| `app/work/observer_ingest_min/generated/` | Concrete generated input artifacts | Older/deeper active input surface | manifests, split units, processing traces, readable boards, summaries | active surface / replayable residue | Large volume makes it look canonical; retention map says some are active surface, some replayable residue |
| `app/runtime/` | Active execution and projection layer | Engine/runtime | runtime bridge, observer, reporting, view builders, API | transformation / display / support zone | Root `app/runtime` can be confused with root `runtime/` artifact store |
| `app/runtime/ingest/` | Intended runtime ingest slice | Engine/runtime | currently empty folder | placeholder / support zone | Empty folder should not be overclaimed as implemented ingest subsystem |
| `app/runtime/source_view/` | Builds source-readable runtime views | Engine/runtime source surface | builder/render code | display / transformation zone | Builder/render only; entrypoints may live in scripts or API |
| `runtime/` | Runtime artifact root | Runtime artifact layer | manifests, reports, contracts, logs, sessions, language loops | ledger / active surface / residue zone | Can be mistaken for implementation code; it mostly stores current and generated artifacts |
| `runtime/manifests/` | Manifest and latest state surfaces | Runtime ledger / active state | latest JSONs, registries, inventories | ledger / active surface | Some manifests are ledger-like and should not be rewritten; some are current surfaces |
| `runtime/contracts/` | Packet/return templates and live instances | Process camera contract layer | JSON templates and packet/return instances | contract / instance zone | These are not final automation schemas; they are bounded packetization assets |
| `runtime/reports/` | Rendered views and smoke reports | Runtime report/view layer | HTML, JSON, MD reports | display / report zone | `folder_status.md` says this is a reading surface, not source of truth |
| `references/` | External/reference material and imported reference engines | Support reference zone | reference source material | source / support zone | External reference should not become engine-ingest-ready without mediation |
| `scripts/` | Command-line entrypoints for runtime/build/review helpers | Support execution zone | scripts | execution support zone | Scripts are execution arms, not canonical input objects |
| `docs/specs/` | Contract/spec layer | Documentation / bounded contract | schema, surface, input, packet specs | support / contract zone | Specs can be mistaken for implemented state; many are locks or candidates |
| `docs/reports/` | Decision, audit, closeout, validation records | Documentation / supervision | reports and notes | record / supervision zone | Reports preserve decisions; they are not automatically runtime state |
| `docs/reviews/` | Review and policy notes | Documentation / review support | retention maps, route policies, signal taxonomies | support / review zone | Review assets can guide but should not be treated as direct implementation |

## 3. Layered Reading

### User surface leaning

- `app/ui/integrated_engine/CommandHeaderPanel.tsx`
- `app/ui/integrated_engine/useUserSurfaceState.ts`
- User sections of `docs/specs/integrated_engine_surface_object_contracts_v0.md`

These are about purpose, scope, assignment, team/role, and decision.

### VectorFL surface leaning

- `app/ui/integrated_engine/CliHostControlPanel.tsx`
- `docs/reports/integrated_engine_internal_search_evidence_bundle_gate_patch_note_v0.md`
- `docs/specs/integrated_engine_execution_packet_schema_v0.md`
- execution packet instances under `runtime/contracts/`

These are about interpretation, evidence bundle, work packet, route/mark, CLI handoff readiness, and validation/reread.

### Engine surface leaning

- `app/runtime/vectorfl_integrated_engine_api.py`
- `docs/specs/integrated_engine_return_record_schema_v0.md`
- return record instances under `runtime/contracts/`
- Engine-side contract sections in `docs/specs/integrated_engine_surface_object_contracts_v0.md`

These are about ingest, process, validation, return material, and redeposit candidate material.

### Legacy/deeper pipeline leaning

- `app/input_layer/`
- `app/work/observer_ingest_min/`
- `app/runtime/source_view/`
- `runtime/manifests/`
- `runtime/reports/`

These are not obsolete. They provide source processing, fragmentization, trace, readable input boards, and downstream reading surfaces.

## 4. Phase 2 Validation

- Role legibility check: passed. Major folders now have source/transformation/display/support roles instead of a flat tree.
- Mixed-zone preservation check: passed. `app/runtime`, `runtime/`, and `observer_ingest_min/generated` are explicitly marked mixed/transitional rather than cleaned into a fake single role.
- Folder-move claim check: passed. No folder move or rename is recommended as fact.

