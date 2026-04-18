# Integrated Engine Lower To Upper Bridge Required Upper Context Fields v0

## 1. Verdict

PASS_WITH_NOTE

Lower bundles do not carry upper packet intent by themselves. A bridge packet requires explicit upper-added context.

## 2. Mandatory Upper-Added Fields

| field | why mandatory | must never be presented as lower-derived |
| --- | --- | --- |
| current purpose | lower artifacts say what exists, not why this bridge exists | yes |
| scope boundary | lower artifacts do not define package limits | yes |
| authority boundary | lower artifacts do not authorize or forbid actions | yes |
| allowed actions | lower artifacts do not grant worker actions | yes |
| forbidden actions | lower artifacts do not block overread by default | yes |
| expected output shape | lower artifacts do not define the return format | yes |
| next route candidate | lower artifacts do not choose future route | yes |

## 3. Optional But Strong Upper-Added Fields

| field | why useful |
| --- | --- |
| selected lens | makes the translation perspective explicit |
| why this path was chosen | records bundle selection reasoning |
| bridge strength hypothesis | helps compare examples later |
| stop-rule scan result | shows blockers were checked |
| field origin map | preserves lower-derived vs upper-added separation |

## 4. Fields That May Be Lower-Derived

These may come directly from the lower bundle:

- source identity
- source path
- run id
- split mode
- unit count
- routing labels
- runmode
- priority
- ticket id
- receipt status
- generated output paths
- processing stage
- origin/source span

But these fields still do not create packet status without the mandatory upper-added fields.

## 5. False Presentation Blocks

Do not present the following as lower-derived:

- "purpose of this bridge test"
- "worker authorization"
- "next route"
- "canonical status"
- "line readiness"
- "upper/lower unification readiness"
- "automation permission"

## 6. Phase 1 Validation

- Upper-added protection check: passed. Mandatory fields are named and blocked from false lower derivation.
- Lower-derived scope check: passed. Lower fields are limited to evidence/trace/route/source data.
- Packet overread check: passed. Lower-derived fields are not sufficient for packet status alone.

