# Tool Profile Record Candidate — 2026-05-09

## 0. Status

- candidate only
- live-use with watch
- not baseline
- not schema
- not registry
- not automation
- not final routing authority
- not replacement for user judgment

## 1. Purpose

This document exists to stop treating ChatGPT, Codex, Gemini, Hermes, QMD, and future external tools as generic interchangeable workers.

It records observed or candidate tool roles, strengths, drifts, safe scopes, and next-use corrections so future routing and mission-packet design can start from known behavior rather than repeated rediscovery.

Every profile remains provenance-aware. A tool profile is not a tool identity, a routing registry, or a final authority. It is a candidate memory aid for deciding which worker is useful for which purpose, under what limits, and with what correction.

## 2. Minimal Tool Profile Fields

Use this compact shape when a future worker needs to update or review a tool profile. It is a candidate shape, not a schema.

```text
tool:
current_role:
safe_scope:
observed_strength:
observed_drift:
required_companion_context:
stop_condition:
best_used_when:
do_not_use_when:
evidence_refs:
provenance_label:
next_use_correction:
watch:
```

Field notes:

- `current_role` describes the current operating use, not the tool's permanent identity.
- `observed_strength` should be grounded in file evidence, process trace, experiment result, or clearly marked supervisor/user judgment.
- `observed_drift` should not be used as blame; it marks correction needed before next use.
- `required_companion_context` should name anchor files, result contracts, provenance notes, or active-surface limits.
- `provenance_label` should use labels from the Judgment Provenance Record trial where useful.

## 3. Tool Profile — ChatGPT / Supervisor

```text
tool:
ChatGPT / Supervisor

current_role:
Intent reading, ambiguous routing, principle alignment, user-language framing, next package framing, and overclaim detection.

safe_scope:
Read the user's purpose, choose the smallest sufficient route, frame Expected Useful Result, separate observed evidence from inference, and keep user-facing answers understandable.

observed_strength:
Can translate internal VectorFL operating logic into user-facing routing language and detect overclaim/promotion risk.

observed_drift:
May explain the space conceptually instead of observing current anchors before answering.

required_companion_context:
- current_anchor_map_candidate_20260509_v0.md
- judgment_provenance_record_template_and_trial_20260509_v0.md
- result_oriented_operating_stack_closeout_20260508_v0.md
- user_facing_routing_card_v0_candidate_20260508.md

stop_condition:
Stop if the answer depends on current repo state that has not been read, or if the route is ambiguous enough that user judgment is needed.

best_used_when:
User intent, routing, downshift, role selection, next-step framing, or user-language explanation is needed.

do_not_use_when:
Do not use as file-evidence source without reading files. Do not let supervisor inference become observed repo evidence.

evidence_refs:
- Package R role boundary names ChatGPT / Supervisor for ambiguous routing, principle alignment, user-language explanation, next package framing, and overclaim detection.
- Package Q routing card says ChatGPT / Supervisor reads purpose first and routes by task nature, not keyword alone.
- Judgment Provenance Trial Record C marks "explaining instead of observing" as a watch.

provenance_label:
CHATGPT_SUPERVISOR_INFERENCE + USER_CURRENT_INPUT + OBSERVED_FILE_EVIDENCE where cited.

next_use_correction:
Read the current anchor map first, label source type, then answer from observed anchors before adding conceptual explanation.

watch:
Do not replace user judgment or file observation with smooth explanation.
```

## 4. Tool Profile — Codex

```text
tool:
Codex

current_role:
Structure recovery, file-grounded inspection, downshift, closeout, packet design, routing-card drafting, and candidate document creation.

safe_scope:
Read repo files, inspect paths, structure observed material, create requested candidate notes, and separate evidence / inference / watch / do-not-promote boundaries.

observed_strength:
Strong at repo structure recovery, exact file path handling, anchor-map drafting, provenance trial drafting, and downshifting worker results into candidate-with-watch language.

observed_drift:
May over-structure low-value material, turn candidates into formal-looking structures too early, or create too many notes.

required_companion_context:
- current_anchor_map_candidate_20260509_v0.md
- judgment_provenance_record_template_and_trial_20260509_v0.md
- result_oriented_operating_stack_closeout_20260508_v0.md
- worker_return_packaging_candidate_setting_compact_v0.md

stop_condition:
Stop if work requires broad execution/testing, final promotion judgment, baseline change, or repeated internal micro-runs.

best_used_when:
The task asks to inspect files, recover structure, draft a candidate note, downshift claims, prepare a mission packet, or close out a package.

do_not_use_when:
Do not use as broad executor, autonomous promoter, final judge, or replacement for Gemini broad-bounded execution.

evidence_refs:
- Package R defines Codex for recovery, downshift, structure, closeout, packet design, and routing card drafting.
- Worker Return Packaging says Codex downshifts claims, separates evidence/gap, extracts reusable judgment, and avoids micro-run proliferation.
- Current anchor and provenance trial files were created by Codex as candidate documents with no baseline promotion.

provenance_label:
OBSERVED_FILE_EVIDENCE + CODEX_OBSERVATION + USER_CURRENT_INPUT when user requested the structure.

next_use_correction:
Always include user purpose, layer, no-promotion boundary, and whether a full note is necessary or raw trace is enough.

watch:
Avoid making every useful observation into a document. Use Result Usefulness Gate before recovery.
```

## 5. Tool Profile — Gemini

```text
tool:
Gemini

current_role:
Broad-bounded execution, verification, testing, usefulness audit, larger synthesis, and package-level result production.

safe_scope:
Read larger active bundles, compare multiple materials, run broad-bounded trials, produce one package-level synthesis, and expose gaps and watch items.

observed_strength:
Useful for meaning, philosophy, broad synthesis, multi-material comparison, usefulness audit, and larger execution/testing packages.

observed_drift:
May over-abstract, produce elegant synthesis without enough file anchors, use high-confidence/proof/validation language, or blur synthesis into authority.

required_companion_context:
- GEMINI.md
- result_oriented_operating_stack_closeout_20260508_v0.md
- mission_packet_result_contract_v0_candidate_20260508.md
- judgment_provenance_record_template_and_trial_20260509_v0.md

stop_condition:
Stop if Gemini claims baseline, proof, validation, stable status, final authority, or expands beyond the active surfaces and mission packet.

best_used_when:
The task requires broad-bounded execution, verification, testing, usefulness audit, long-context synthesis, or comparative interpretation.

do_not_use_when:
Do not use for final operating frame, baseline declarations, schema/registry decisions, or self-promoted authority.

evidence_refs:
- Package R defines Gemini for broad-bounded execution, verification, testing, usefulness audit, larger synthesis, and one package-level result.
- GEMINI.md requires Plan From Space, evidence pointers, non-inspected scope, and raw-trace packaging.
- Judgment Provenance labels Gemini output as GEMINI_SYNTHESIS, not structural proof.

provenance_label:
GEMINI_SYNTHESIS + EXPERIMENT_RESULT when tied to trials; not OBSERVED_FILE_EVIDENCE unless file anchors are explicitly cited.

next_use_correction:
Require an explicit file-anchor bundle, Expected Useful Result, provenance note, not-inspected scope, and do-not-promote clause in every Gemini packet.

watch:
Meaning synthesis is valuable, but it must return to Codex/Supervisor/User for recovery and judgment.
```

## 6. Tool Profile — Hermes

```text
tool:
Hermes

current_role:
Small bounded active-surface reader and lineage synthesis carrier candidate.

safe_scope:
One-shot `hermes -z` tasks over 1-5 explicit, non-sensitive active surfaces, no write, no memory, no skill, no config, Worker Return Intake return.

observed_strength:
Candidate evidence from Package H/I/J/K shows minimal return-shape, one-target reading, three-surface synthesis, and five-surface limited synthesis under controlled conditions.

observed_drift:
Small-surface success may be overgeneralized into broad repo reliability, standard carrier interface, or Hermes integration. Memory / skill_manage / curator authority drift remains watch.

required_companion_context:
- package_l_hermes_carrier_sizing_boundary_closeout_20260508_v0.md
- worker_return_packaging_candidate_setting_compact_v0.md
- mission_packet_result_contract_v0_candidate_20260508.md
- current_anchor_map_candidate_20260509_v0.md

stop_condition:
Stop when more than 5 surfaces are needed, surfaces are unclear, broad search is needed, not_inspected_scope is missing, Worker Return Intake shape degrades, or Hermes suggests memory/skill/config edits.

best_used_when:
The task is explicit 1-5 file reading, lineage synthesis, small status synthesis, or bounded carrier evidence collection.

do_not_use_when:
Do not use for broad repo search, full space interpretation, config/memory/skill edits, promotion decisions, or tasks needing Gemini broad synthesis.

evidence_refs:
- Package L records H/I/J/K candidate observations and sets 5 explicit active surfaces as the current soft upper bound.
- Worker Return Packaging defines required return shape and raw trace boundary.

provenance_label:
EXPERIMENT_RESULT + OBSERVED_FILE_EVIDENCE for recovered Package L evidence; WATCH for broader reliability.

next_use_correction:
Cap surface count, require explicit active surfaces, require not-inspected scope, and recover Hermes output through Codex/Supervisor before reuse.

watch:
Do not call Hermes a standard carrier or integration path. Keep carrier neutrality.
```

## 7. Tool Profile — QMD

```text
tool:
QMD

current_role:
Bounded evidence pointer access carrier candidate.

safe_scope:
Known material family, selected active surfaces, candidate pointer discovery, exact URI multi-get, and evidence support only.

observed_strength:
Useful when exact evidence pointers are needed and material family is already known.

observed_drift:
QMD score, body bundle, docid, URI, snippet, or pointer bundle may be mistaken for memory or authority.

required_companion_context:
- qmd_carrier_candidate_operating_setting_compact_v0.md
- worker_return_packaging_candidate_setting_compact_v0.md
- current_anchor_map_candidate_20260509_v0.md
- result_oriented_operating_stack_closeout_20260508_v0.md

stop_condition:
Stop on full corpus indexing, default embed/query/rerank, MCP startup, parser/schema/automation pressure, registry/baseline pressure, or tool-output authority drift.

best_used_when:
The user asks for "근거만 찾아줘" or a future package needs bounded evidence pointers from a known material family.

do_not_use_when:
Do not use for broad interpretation, memory, anchor authority, full corpus indexing, or final synthesis.

evidence_refs:
- QMD compact setting says QMD is bounded evidence access only, with 3-7 active surfaces when the active material family is known.
- Worker Return Packaging lists QMD score/docid/URI/snippet/body bundle as raw trace until recovered.

provenance_label:
PROCESS_TRACE + OBSERVED_FILE_EVIDENCE for QMD setting; RAW_TRACE_ONLY for raw QMD output until recovered.

next_use_correction:
Define material family, active surfaces, return placement, and whether QMD output is raw trace, routing hint, or evidence support before use.

watch:
QMD is not memory and not authority. Evidence pointers still need recovery.
```

## 8. Cross-Tool Routing Notes

| Task Type | Preferred Tool | Required Companion Context | Watch |
|---|---|---|---|
| current repo / anchor inspection | Codex | Current Anchor Map; provenance trial | avoid broad execution; stay file-grounded |
| broad meaning synthesis | Gemini | file-anchor bundle; Result Contract; provenance note | over-abstraction and proof language |
| bounded 1-5 file reading | Hermes | explicit active surfaces; Package L; Worker Return Intake | no broad search; require not-inspected scope |
| evidence pointer retrieval | QMD | known material family; QMD compact setting; raw trace boundary | QMD score/body not memory |
| mission packet drafting | Codex | Result Contract; role profile; no-promotion boundary | don't execute the packet while drafting |
| provenance classification | Codex / Supervisor | provenance trial; current anchor map | don't turn labels into truth engine |
| external reference translation | Gemini for broad read, Codex for recovery | Expected Useful Result; external reference translation candidate when available | don't import external source as doctrine |
| user-facing summary / next-chat handoff | ChatGPT / Supervisor | Routing card; memory hygiene rule; current anchors | keep concise; don't create package by default |

## 9. Telemetry Fields for Future Trials

Optional trial telemetry, not a mandatory metric system:

```text
tool:
task_id:
input_active_surfaces:
input_size_estimate:
output_size_estimate:
result_type:
strength_observed:
drift_observed:
user_correction_needed:
recovered_judgment:
return_placement:
next_policy_change:
```

Use telemetry only when it changes future routing, packet design, active-surface sizing, or recovery decisions. Do not collect it for every ordinary answer.

## 10. Known Limits

- This is based on current observed/candidate records only.
- Tool behavior may change with model, version, runtime, prompt, or context.
- Profiles should be revised after 2-3 real uses.
- These profiles describe current operating roles, not permanent tool identities.
- These profiles are not routing authority and do not replace user judgment.
- Some judgments are supervisor/user inference rather than direct file evidence.
- Hermes and QMD evidence is bounded and should not be generalized.
- Gemini behavior should be checked against actual future package results.
- Codex behavior should be checked against whether its structures remain useful.

## 11. Watch Items

- tool profile becoming doctrine.
- tool profile becoming routing registry.
- Codex over-structuring.
- Gemini over-abstracting.
- Hermes overgeneralized.
- QMD treated as memory.
- ChatGPT explaining instead of observing.
- model/version changes invalidating old profile.
- telemetry becoming fake precision.
- user judgment being replaced by tool profile.
- drift labels becoming blame instead of routing correction.

## 12. Final Note

This document is a tool-profile trial only.

It should be revised after 2-3 real uses.

It should not be treated as a final routing system.

