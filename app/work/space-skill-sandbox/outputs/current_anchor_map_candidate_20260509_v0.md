# Current Anchor Map Candidate — 2026-05-09

## 0. Status

- candidate only
- live-use with watch
- not baseline
- not registry
- not schema
- not automation
- not production workflow

## 1. Purpose

This map exists to reduce rediscovery cost for future ChatGPT, Codex, Gemini, Hermes, and QMD work.

It names the current first-read anchors for the live-use candidate stack and records what each file is for, when to read it, what not to assume from it, and what parent or neighbor context should travel with it.

This is a first-read candidate map only. It does not decide authority, promote status, enforce schema, or replace user judgment.

## 2. Anchor Table

| Anchor ID | Path | Role | Current Status | Read When | Do Not Use As | Parent Context | Neighbor Context | Evidence Type |
|---|---|---|---|---|---|---|---|---|
| A01 | `app/work/space-skill-sandbox/outputs/result_oriented_operating_stack_closeout_20260508_v0.md` | Current result-oriented operating stack closeout: Boundary Check -> Shape Check -> Result Usefulness Gate -> LACL Placement -> User Judgment | live candidate with watch | First read for the current operating flow and role split | baseline, standard, production workflow, automation | Package M-Q sequence | Package Q routing card; Package O Result Contract; Package M Usefulness Gate; Package L Hermes boundary | observed file |
| A02 | `app/work/space-skill-sandbox/outputs/user_facing_routing_card_v0_candidate_20260508.md` | User-facing Korean trigger routing card, including overloaded-term handling for "정리해줘" | live candidate with watch | Read when interpreting user phrases or deciding smallest sufficient route | command registry, UI standard, automation dispatcher | Package P/Q and Package S live-use candidate patch | Package R closeout; Result Contract; Space Boundary Trigger Flow | observed file |
| A03 | `app/work/space-skill-sandbox/outputs/mission_packet_result_contract_v0_candidate_20260508.md` | Expected Useful Result / Result Contract for future mission packets | candidate | Read before drafting Gemini, Hermes, or external worker packets | schema, mandatory scoring system, baseline | Package M Usefulness Gate and Package N audit lesson | Worker Return Intake; Package R flow; routing card | observed file |
| A04 | `app/work/space-skill-sandbox/outputs/result_usefulness_gate_v0_candidate_20260508.md` | Recovery-stage gate separating safe/shape-compliant output from useful judgment | candidate | Read when deciding Return-to-Space, Watch, Raw Trace, Hold, or Discard | scoring engine, automation, replacement for user judgment | Package M structuring | Result Contract; Memory Hygiene; Worker Return Packaging | observed file |
| A05 | `app/work/space-skill-sandbox/outputs/package_l_hermes_carrier_sizing_boundary_closeout_20260508_v0.md` | Hermes carrier sizing and boundary closeout; observed 1-5 explicit active surface range | candidate with watch | Read before routing any bounded file-reading task to Hermes | proof of reliability, standard carrier interface, Hermes integration | Package F-K Hermes sequence | Routing card; Worker Return Intake; Result Contract | observed file |
| A06 | `app/work/space-skill-sandbox/outputs/vectorfl_memory_record_hygiene_rule_20260508_v0.md` | Memory and record hygiene rule: remember reusable operating judgment, not every run | candidate with watch | Read before deciding what belongs in assistant memory vs project files vs raw trace | deletion policy, final memory schema, automation | Package R closeout | Result Usefulness Gate; RUNLOG; Movement Records | observed file |
| A07 | `app/work/space-skill-sandbox/outputs/worker_return_packaging_candidate_setting_compact_v0.md` | Compact 10-field Worker Return Intake candidate and raw trace boundary | candidate | Read when packaging external worker output into recoverable space material | final schema, registry, baseline return format | Package A-E external execution recovery setting | Result Usefulness Gate; Movement Record Template; Package L Hermes returns | observed file |
| A08 | `app/work/space-skill-sandbox/outputs/qmd_carrier_candidate_operating_setting_compact_v0.md` | QMD as bounded evidence pointer access carrier, not memory or authority | candidate | Read before using QMD for known material family / evidence pointer access | memory system, search authority, full corpus indexer | QMD trial/recovery sequence | Routing card Card 5; Worker Return Packaging; Movement Records | observed file |
| A09 | `docs/indexes/lacl_candidate_synthesis_matrix_seed_v0.md` | LACL seed matrix for line, axis, camera, lens_gate, PV, overlap, missing data | candidate seed | Read when placing a result by LACL/PV or checking line/axis/camera/lens terms | mature LACL registry, ontology, baseline | LACL regrounding and Plan from Space work | Plan from Space map; Space Boundary maps; Package R LACL placement | observed file |
| A10 | `docs/indexes/space_boundary_material_flow_map_v0.md` | Space-boundary material intake flow: source surface, camera, lens rack, lookup, movement decision, return | candidate map | Read when handling "material enters" / space-boundary intake | controller, runtime manifest, writer, automation | Space Boundary Trigger Flow family | Trigger Flow catalog; relation-first input; routing card Card 1 | observed file |
| A11 | `docs/reports/space_boundary_trigger_flow_surface_catalog_package_v0.md` | "공간에 넣어보기" trigger flow, source-surface coverage, 4-line card | candidate / normal-use ready with watch | Read when user says "이거 공간에 넣어봐" or similar material-intake trigger | final controller spec, schema, writer implementation | Space Boundary Material Flow Map | Routing card Card 1; Result Usefulness Gate; Movement Records | observed file |
| A12 | `docs/reports/evidence_provenance_classification_candidate_v0.md` | Evidence/provenance labels: EXTRACTED, INTERPRETED, INFERRED, AMBIGUOUS, USER_JUDGED, PROCESS_TRACE | candidate | Read when separating file evidence, inference, user judgment, model output, and process trace | truth engine, provenance registry, formal schema | relation-first input and provenance work | Origin map; Packet Provenance; Result Usefulness Gate | observed file |
| A13 | `docs/specs/package_record_minimum_v0.md` | Minimal package record fields for intake/digestion/review/memory packages | candidate spec | Read when comparing package-level records or designing minimal package metadata | lifecycle automation, storage engine, package registry | phase-1 package work | RunRecord enrichment; Movement Record Template; space-skill packages | observed file |
| A14 | `docs/specs/integrated_engine_runrecord_enrichment_boundary_v0.md` | Candidate RunRecord enrichment fields for continuation-friendly run reading | candidate boundary | Read when converting coarse run summaries into continuation fields | artifact viewer, dashboard, worker orchestration, UI redesign | integrated-engine package continuity work | RUNLOG; `app/work/space-skill-sandbox/runs/`; Worker Return Packaging | observed file |
| A15 | `RUNLOG.jsonl` | Concise append trace for recent actions, outputs, boundaries, and verdicts | raw process trace | Read to confirm whether an action happened and where outputs were written | complete memory, proof of semantic correctness, final authority | project-level process history | Recovery notes; raw outputs; memory hygiene rule | observed process trace |
| A16 | `CURRENT.md` | Runtime/engine current baseline around fragments, anchors, measurements, observer layer | historical / supporting context | Read when current task touches runtime engine/fragment/observer baseline | current result-oriented operating stack authority | runtime/fragment engine layer | `vectorfl_status.md`; integrated-engine reports | observed file |
| A17 | `vectorfl_status.md` | Broad integrated-engine pointer and current working background map | historical / supporting context; authority unclear for current stack | Read when orienting integrated-engine materials and older working baseline language | replacement for Package R live candidate stack, promotion authority | integrated-engine current PASS baseline context | CURRENT.md; docs/reports integrated-engine files; Package R for current stack correction | observed file |
| A18 | `GEMINI.md` | Compact Gemini/external-tool operating guide candidate | candidate reference | Read when calibrating Gemini or other external workers before package execution | constitutional authority, baseline, permanent guide | SESSION_47 / Plan from Space / Anchor Stack context | Codex/Gemini/User role boundary; Package R role lock; Result Contract | observed file |

## 3. Minimal Active Bundles

### A. Result-Oriented Core Bundle

purpose:
- Understand the current Package R/Q/O/M/L live-use candidate stack.
- Use when deciding route, expected useful result, recovery decision, or role boundary.

files:
- `app/work/space-skill-sandbox/outputs/result_oriented_operating_stack_closeout_20260508_v0.md`
- `app/work/space-skill-sandbox/outputs/user_facing_routing_card_v0_candidate_20260508.md`
- `app/work/space-skill-sandbox/outputs/mission_packet_result_contract_v0_candidate_20260508.md`
- `app/work/space-skill-sandbox/outputs/result_usefulness_gate_v0_candidate_20260508.md`
- `app/work/space-skill-sandbox/outputs/package_l_hermes_carrier_sizing_boundary_closeout_20260508_v0.md`

max recommended surfaces:
- 5 files.

what context is missing:
- Package N and Package P standalone files were not located in this anchor pass; their lessons are represented through Package O/R and RUNLOG references.

watch item:
- Do not turn the bundle into baseline or standard operating procedure.

### B. Provenance / Record Structure Bundle

purpose:
- Understand how results, records, traces, and judgments should be separated.
- Use when designing or reviewing recovery records, run records, package records, or provenance labels.

files:
- `app/work/space-skill-sandbox/outputs/vectorfl_memory_record_hygiene_rule_20260508_v0.md`
- `app/work/space-skill-sandbox/outputs/worker_return_packaging_candidate_setting_compact_v0.md`
- `docs/reports/evidence_provenance_classification_candidate_v0.md`
- `docs/specs/package_record_minimum_v0.md`
- `docs/specs/integrated_engine_runrecord_enrichment_boundary_v0.md`
- `RUNLOG.jsonl`

max recommended surfaces:
- 5-6 files. If token budget is tight, omit `RUNLOG.jsonl` unless process trace is required.

what context is missing:
- Movement Record Template may be needed as a neighbor when writing or reviewing actual Movement Records.

watch item:
- Provenance labels are candidate reading aids, not a truth engine.

### C. User Re-entry / Routing Bundle

purpose:
- Understand how user-facing phrases map into internal routes without exposing internal jargon.
- Use when the user says "정리해줘", "이거 공간에 넣어봐", "이 파일들만 보고 정리해줘", or similar.

files:
- `app/work/space-skill-sandbox/outputs/user_facing_routing_card_v0_candidate_20260508.md`
- `docs/reports/space_boundary_trigger_flow_surface_catalog_package_v0.md`
- `docs/indexes/space_boundary_material_flow_map_v0.md`
- `app/work/space-skill-sandbox/outputs/result_usefulness_gate_v0_candidate_20260508.md`
- `app/work/space-skill-sandbox/outputs/mission_packet_result_contract_v0_candidate_20260508.md`

max recommended surfaces:
- 5 files.

what context is missing:
- For LACL/PV placement, add `docs/indexes/lacl_candidate_synthesis_matrix_seed_v0.md`.

watch item:
- User phrases are intents, not rigid commands. Route by purpose, not keyword alone.

## 4. Known Gaps

- Package S standalone note not found in this anchor pass; Package S appears in `RUNLOG.jsonl` and in the Package Q overloaded-term patch context.
- Tool profile / telemetry exists only as scattered role contracts, recovery notes, RUNLOG entries, and package evidence.
- No single policy mutation log was found; behavior changes are scattered across closeouts and RUNLOG reasons.
- No unified external reference translation record was found, though external reference merge and intake protocols exist.
- `vectorfl_status.md` contains integrated-engine current/baseline language and can be mistaken for current result-oriented authority. For the current live-use result-oriented stack, read Package R first.
- `RUNLOG.jsonl` entry shape is mixed across dates and should be treated as process trace, not semantic memory.
- Current anchors are distributed across `outputs/`, `docs/`, root files, and RUNLOG; this map does not resolve authority conflicts.

## 5. Watch Items

- Candidate map becoming baseline.
- Candidate map becoming a registry or schema by habit.
- Over-reading old baseline/current docs as authority for the current result-oriented stack.
- Small active surfaces losing parent context.
- Model inference treated as file evidence.
- User judgment flattened into model-written status.
- Codex over-structuring.
- Gemini over-abstracting.
- ChatGPT explaining instead of observing.
- Hermes 1-5 active surface success overgeneralized into broad reading reliability.
- QMD evidence pointers mistaken for memory or authority.

## 6. Final Note

This file is a first-read candidate map only.

It should be revised after 2-3 real uses.

It should not be treated as the final space map.

