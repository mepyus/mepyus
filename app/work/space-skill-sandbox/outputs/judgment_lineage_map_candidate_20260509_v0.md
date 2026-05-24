# Judgment Lineage Map Candidate — 2026-05-09

## 0. Status

- candidate only
- lineage map candidate only
- live-use with watch
- not baseline
- not schema
- not registry
- not graph database
- not automation
- not final authority
- not replacement for user judgment

## 1. Purpose

This document defines a minimal lineage map for current space-observation structures.

It exists to preserve why a judgment or policy changed, prevent isolated capsules, and connect:

```text
trace -> capsule -> policy mutation -> tool profile -> future active bundle
```

The goal is low-token re-entry and relationship awareness, not graph tooling. Relationships are navigation and re-entry aids, not proof.

## 2. Minimal Relationship Types

| Relationship | Meaning | Example | Risk if overused | Status |
|---|---|---|---|---|
| `derived_from` | A judgment, capsule, or mutation was recovered from a source package, trace, or record. | Package R core sentence `derived_from` Package R closeout. | Treating derivation as proof. | candidate only |
| `observed_in` | A claim or boundary is directly visible in a read file or process trace. | Hermes 1-5 limit `observed_in` Package L closeout. | Extending observed scope beyond the file. | candidate only |
| `changed_by` | A future operating condition changed because of a result or correction. | Mission packet wording `changed_by` Package N/O lesson. | Promoting one trial into permanent policy. | candidate only |
| `requires_context` | A small surface needs parent or neighbor context to be used safely. | Capsule `requires_context` Result Usefulness Gate. | Creating heavy link burden. | candidate only |
| `neighbor_of` | Two records should be read together for safe re-entry. | Provenance record `neighbor_of` current anchor map. | Every file becoming linked to every file. | candidate only |
| `supersedes` | A newer candidate condition should be preferred over older wording for a narrow use. | Result-oriented stack `supersedes` boundary/shape-only launch habit. | Erasing older historical context. | candidate only |
| `warns_against` | A record marks a drift, misuse, or overclaim to avoid. | Tool profile `warns_against` Gemini over-abstraction. | Watch items becoming doctrine. | candidate only |
| `used_by_tool` | A surface or rule is used by a role/tool under bounded conditions. | Result Contract `used_by_tool` Gemini packets. | Turning use relation into routing registry. | candidate only |
| `returns_as` | A result can return as a placement category after checks. | Micro-run trace `returns_as` WATCH or RETURN_TO_SPACE_VALUE_WITH_WATCH. | Placement before Usefulness Gate. | candidate only |
| `review_after` | A candidate should be revisited after a stated number of uses or trials. | Policy mutation `review_after` 2-3 uses. | Review schedule becoming fake precision. | candidate only |

This is not a full graph ontology.

## 3. Lineage Map Scope

This first map is narrow. It maps only the current result-oriented / space-observation setup sequence:

```text
Package L Hermes boundary
-> Package M Result Usefulness Gate
-> Package O Mission Packet Result Contract
-> Package Q Routing Card
-> Package R Result-Oriented Closeout
-> 2026-05-09 Space Observation setup docs
```

Package N, Package P, and Package S are referenced through later recovery context and user-provided summaries where not directly located in this pass. They should be marked referenced / not directly inspected, not missing as an absolute truth.

## 4. Textual Lineage Map

### Chain A — Hermes Active Surface Boundary

```text
[Package L Hermes carrier sizing boundary closeout]
  --observed_in / OBSERVED_FILE_EVIDENCE-->
[Hermes 1-5 explicit active surface candidate limit]
  --derived_from / OBSERVED_FILE_EVIDENCE-->
[tool_profile_record Hermes profile]
  --used_by_tool / OBSERVED_FILE_EVIDENCE + CHATGPT_SUPERVISOR_INFERENCE-->
[future active_bundle route for bounded 1-5 surface reading]
```

watch:
- Do not treat Hermes as broad repo reader.
- Do not promote 1-5 range to baseline or standard.
- Carrier neutrality remains watch.

### Chain B — Usefulness Gate

```text
[Package M Result Usefulness Gate]
  --changed_by / GEMINI_SYNTHESIS + CHATGPT_SUPERVISOR_INFERENCE where Package N is referenced-->
[safe/shape output is insufficient; result must be useful]
  --derived_from / OBSERVED_FILE_EVIDENCE when Package R is read-->
[Package R core sentence]
  --derived_from / OBSERVED_FILE_EVIDENCE + USER_LONG_TERM_CONTEXT-->
[JC_PACKAGE_R_CORE_SENTENCE_20260509_A]
  --changed_by / OBSERVED_FILE_EVIDENCE-->
[PMR_RESULT_CONTRACT_SHIFT_20260509_A]
```

watch:
- The core sentence can become slogan-like if not tied to concrete recovery decisions.
- Package N audit is referenced through recovery context unless a standalone file is found.

### Chain C — Mission Packet Result Contract

```text
[Package O Mission Packet Result Contract]
  --changed_by / OBSERVED_FILE_EVIDENCE + GEMINI_SYNTHESIS-->
["Read X" replaced by "Synthesize X to enable decision Y"]
  --derived_from / OBSERVED_FILE_EVIDENCE-->
[PMR_RESULT_CONTRACT_SHIFT_20260509_A]
  --used_by_tool / CHATGPT_SUPERVISOR_INFERENCE + OBSERVED_FILE_EVIDENCE-->
[future Gemini/Hermes/Codex packets]
```

watch:
- Decision language must not become authority claim.
- Expected Useful Result is candidate packet discipline, not schema.

### Chain D — User Routing / "정리해줘"

```text
[Package Q routing card and Package S live-use context]
  --derived_from / OBSERVED_FILE_EVIDENCE + PROCESS_TRACE or USER_CURRENT_INPUT depending on source read-->
[user-facing routing card]
  --neighbor_of / OBSERVED_FILE_EVIDENCE-->
[current_anchor_map User Re-entry / Routing Bundle]
  --warns_against / OBSERVED_FILE_EVIDENCE + CHATGPT_SUPERVISOR_INFERENCE-->
[overloaded "정리해줘" keyword routing without purpose read]
```

watch:
- Package S standalone note was not found in the anchor pass; treat Package S as referenced context unless located later.
- User phrases are intents, not rigid commands.

### Chain E — Space Observation Setup

```text
[current_anchor_map_candidate_20260509_v0.md]
  --neighbor_of / OBSERVED_FILE_EVIDENCE-->
[judgment_provenance_record_template_and_trial_20260509_v0.md]
  --neighbor_of / OBSERVED_FILE_EVIDENCE-->
[tool_profile_record_candidate_20260509_v0.md]
  --derived_from / OBSERVED_FILE_EVIDENCE + USER_CURRENT_INPUT-->
[space_observation_structural_setup_pack_20260509_v0.md]
  --requires_context / OBSERVED_FILE_EVIDENCE-->
[micro_run_trace_record_candidate_20260509_v0.md]
  --changed_by / OBSERVED_FILE_EVIDENCE + USER_CURRENT_INPUT + GEMINI_SYNTHESIS]-->
[policy_mutation_record_candidate_20260509_v0.md]
  --requires_context / OBSERVED_FILE_EVIDENCE + CHATGPT_SUPERVISOR_INFERENCE-->
[judgment_capsule_reentry_surface_candidate_20260509_v0.md]
  --neighbor_of / OBSERVED_FILE_EVIDENCE + CHATGPT_SUPERVISOR_INFERENCE-->
[judgment_lineage_map_candidate_20260509_v0.md]
```

watch:
- This chain describes setup order, not authority order.
- Relationships are candidate navigation aids only.

## 5. Provenance Requirement for Relationships

Every relationship should mark one of:

```text
OBSERVED_FILE_EVIDENCE
PROCESS_TRACE
CODEX_OBSERVATION
CHATGPT_SUPERVISOR_INFERENCE
GEMINI_SYNTHESIS
USER_JUDGED
MISSING_EVIDENCE
```

Do not silently infer relationships.

If a relationship is logical but not file-observed, mark it as inference. If a referenced package is only available through later context or user summary, mark it as referenced / not directly inspected.

Relationship provenance does not replace judgment provenance. It only describes why the link is present.

## 6. Candidate Validity / Supersession Note

Some candidate conditions may supersede older conditions for a narrow use, but this map does not delete or hide history.

- current result-oriented stack should not erase older baseline/current docs
- older docs may remain historical/supporting context
- no validity window is final yet
- supersession is candidate and scoped
- this map must not be used to remove files, rewrite history, or promote new structures

## 7. Minimal Lineage Card Template

Use this compact future template only when a relationship needs to be reusable.

```text
lineage_id:
from:
relationship:
to:
why_it_matters:
provenance:
status:
use_when:
do_not_use_when:
watch:
review_after:
```

This is a candidate shape, not a schema.

## 8. Degradation Watch

- graph becoming hidden authority
- every record becoming node
- every sentence becoming edge
- inferred relation treated as evidence
- relationship replacing provenance
- current_anchor_map mistaken as graph homepage
- Codex over-structuring graph folders
- Gemini over-abstracting graph theory
- user language disappearing
- token cost increasing through link traversal
- relationship map used before usefulness is proven
- LACL placement being replaced by graph positioning
- Graphiti / GraphRAG import becoming implementation pressure

## 9. Relation to Existing Setup

### current_anchor_map

- supplies first-read anchors and small active bundles
- should not become graph root, homepage, registry, or authority

### judgment_provenance_record

- supplies source labels for lineage relationships
- prevents inferred relation from being treated as observed evidence

### tool_profile_record

- receives relationship effects when a policy mutation changes how a tool should be used
- prevents tool roles from becoming permanent identities

### micro_run_trace_record

- provides trace material that can produce capsule, watch, policy mutation, telemetry, or raw trace
- should not become memory by default

### policy_mutation_record

- records when lineage changes future operating conditions
- links judgment changes to next packet/route conditions

### judgment_capsule_reentry_surface

- provides reusable judgment units and user-facing re-entry surfaces
- depends on parent/neighbor/provenance to avoid context loss

### Package R result-oriented flow

- remains the current candidate flow for Boundary Check, Shape Check, Usefulness Gate, LACL Placement, Return-to-Space placement, and User Judgment
- graph/lineage is a supporting relationship surface only

## 10. Known Limits

- not tested
- no graph database
- no automation
- not full lineage of the repo
- only a narrow candidate map
- may omit important historical context
- should be revised after 2-3 real uses
- relationships may be too coarse or too many
- Package N/P/S were not directly inspected as standalone files in this task

## 11. Final Note

This document is a judgment lineage map candidate only.

It should be tested manually before any graph, wiki, or script implementation.

It should not be treated as final architecture, schema, registry, graph system, or automation.
