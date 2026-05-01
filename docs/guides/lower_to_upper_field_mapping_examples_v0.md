# Lower To Upper Field Mapping Examples v0

## Verdict

`PASS_WITH_NOTE`

This guide maps lower artifact fields to upper packet and evidence fields without changing either side's schema. It is a minimum operator guide, not an implementation contract.

## Mapping Modes

| mode | meaning |
| --- | --- |
| `carry` | preserve the lower value directly as a source, pointer, or note |
| `summarize` | compress several lower fields into a short upper reason or constraint |
| `reinterpret` | translate lower process signal into an upper task/search/evidence meaning |
| `hold_lower` | keep the field lower-side until more support exists |
| `do_not_promote` | explicitly block the field from upper use |

## Field Mapping Table

| mapping category | lower artifact field | upper destination field | mapping mode | mapping condition | not-yet-mapped note |
| --- | --- | --- | --- | --- | --- |
| provenance / origin | `source_path`, `input_path`, `generated_from_ref`, origin map path | question packet `search_targets`; exploration `source_ref`; evidence `source_ref` | `carry` | path is stable and readable | do not treat source path alone as packet intent |
| provenance / origin | `run_id`, timestamp, receipt path | exploration `selected_asset_reasons`; reingress `searched_assets_summary` | `summarize` | run id helps explain artifact family or trace | do not use run id as semantic evidence |
| source manifest | `input_id`, `label`, `input_kind`, `detected_profile` | packet `scope`; packet `constraints`; selected asset reason | `summarize` | profile affects how the material should be read | do not promote profile to conclusion |
| source manifest | `split_mode_used`, `unit_count`, `raw_line_count` | exploration `selected_asset_reasons`; evidence `confidence`; `missing_gaps` | `reinterpret` | segmentation quality affects evidence reliability | do not use unit count as line/axis proof |
| split units | `unit_id`, `start_ref`, `end_ref` | evidence `pointer`; structured evidence `path_ref` or local pointer | `carry` | unit has source ref and bounded excerpt | title-only units remain weak evidence |
| split units | `text_excerpt`, `char_count` | evidence `excerpt_or_pointer`; grounded `excerpt_window`; `excerpt_quality` if available | `carry` or `summarize` | excerpt is sufficient and not metadata-only | long units may become search targets rather than evidence |
| processing trace | split route, trace notes, generated files | exploration `supporting_links`; `missing_gaps`; `next_probe_candidates` | `summarize` | trace explains how lower output was produced | trace cannot replace source evidence |
| label packet | label family, anchor, scene, flow, route marker | packet `constraints`; packet `task_mode`; exploration `selected_asset_reasons` | `reinterpret` | label is used as reading aid, not final meaning | generic discourse labels should stay lower unless topic-bearing |
| routing basis | `before_gate.decision`, `after_gate.decision`, `decision_reason` | packet `constraints`; `ambiguity_notes`; `hold_reason_if_any` if hard stop | `reinterpret` | gate states direct ingest vs preprocess risk | route ambiguity does not automatically require user hold |
| routing basis | checkpoint lists, readiness read, check surface | expected output shape; exploration `next_probe_candidates`; reingress `future_probe_note` | `summarize` | checkpoint names a concrete next probe | do not over-promote checklist into answer |
| residue / evidence / ingest signal | readiness level or lower report verdict | upper admission result; merge `final_reasoning_basis` risk note | `reinterpret` | readiness is explicit or inferable from report | inferred readiness must be marked provisional |
| residue / evidence / ingest signal | receipts, logs, repeated runtime views | lower trace context only | `hold_lower` or `do_not_promote` | no source support or bounded semantic unit | can be cited in a report, not upper packet/evidence |

## Category Notes

### Provenance / Origin

Most provenance fields can be carried because upper exploration already understands paths and source refs. The risk is overclaiming: a clear path tells upper where to look, not what to conclude.

### Source Manifest

Manifest fields are best summarized into search target reasons and constraints. They say how the lower organ saw the material, especially profile and split mode.

### Split Units

Split units are the strongest bridge into evidence units when the unit has a meaningful excerpt. Title-only or metadata-only units should stay weak evidence or become a search target for adjacent context.

### Processing Trace

Processing trace fields explain reliability and generation context. They should influence confidence, gaps, and next probes, not become primary evidence.

### Label Packet

Labels and anchors often need reinterpretation because lower labels can be generic. A `review` or `compare` label is useful for routing, but it does not by itself identify the source's meaning-bearing axis.

### Routing Basis

Gate decisions are valuable for upper constraints and ambiguity notes. For example, `preprocess_required` maps to a constraint that direct raw ingestion should not be trusted without preprocessing.

### Residue / Evidence / Ingest Signal

Readiness signals should decide admission level. Receipts and event traces should not cross the bridge unless they explain the provenance of a selected artifact.

## Interpretation

Some lower fields can be carried because they are already identity or pointer fields. Others must be summarized because they describe a process state. Others must be reinterpreted because lower labels and route signals are not the same thing as upper task intent.

Some fields should not be promoted because they would make the upper packet inherit lower residue. The bridge must preserve useful lower material without turning every generated trace into a request-side claim.

## Validation

- Mapping covers provenance, manifest, split units, trace, label, routing, and readiness signal: `PASS`.
- Mapping modes include carry, summarize, reinterpret, hold, and do-not-promote: `PASS`.
- Not-yet-mapped notes are explicit: `PASS`.
- The guide does not require schema changes: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/guides/lower_to_upper_field_mapping_examples_v0.md`
3. What was fixed at the bridge level: field-level mapping modes and conditions.
4. What remains unresolved: checklist and concrete example trials.
5. Whether user decision is required: no.
6. Can Phase 1.12 start after this? not yet; admission checklist and real examples should be added.
7. Recommended next move: write admission checklist and failure modes.
