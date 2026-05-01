# External Material Microspace Index v0

## 1. status

```yaml
index_status: microspace_index_candidate
space_name: external_material_microspace
based_on:
  - docs/reports/formation_movement_interface_external_material_reemergence_reread_merge_v0.md
  - docs/reports/formation_movement_interface_goscrapy_external_material_pipeline_note_v0.md
purpose: keep ingested external materials findable, mergeable, and reusable without promoting them into baseline doctrine
baseline_lock: false
schema_enforcement: false
implementation: false
runtime_manifest: false
```

## 2. one-line purpose

This microspace exists so external materials can mature together and re-emerge naturally when a related line, lens, workflow, or Codex handoff question appears.

It is not a doctrine repository.

It is a small reread space.

## 3. why a microspace is needed

Recent friction:

```text
외부자료는 들어왔고 분석도 되었지만,
나중에 다시 찾고 머지하고 적용할 때 사용자가 기억해야 하는 부담이 너무 큼.
```

The right correction is not a heavier package.

The right correction is:

```text
external material
→ microspace entry
→ line/lens placement
→ cluster merge
→ re-emergence trigger
→ bounded compare / hold / refine
```

## 4. microspace boundary

This microspace stores:

- external material aliases
- source traces
- analysis reports
- current provisional state
- closest internal lines
- active lenses
- safe next moves
- promotion barriers
- cluster membership

This microspace does not store:

- baseline rules
- enforced schemas
- imported external workflows
- implementation decisions
- direct evidence locks
- automatic Codex execution permissions

## 5. current external clusters

| Cluster | Included materials | Current state | Primary use | Guardrail |
| --- | --- | --- | --- | --- |
| governance-architecture cluster | agent-skills, Flutist | framing_candidate | bounded preparation, architecture boundary, validation gate | not direct evidence for A/B/C |
| Codex workflow/runtime cluster | OMX / oh-my-codex / team-ralph | framing_candidate | workflow controller, role elevation, stage/artifact/verification return | do not import OMX runtime |
| formation-to-movement cycle cluster | LLM-Wiki, autoresearch | framing_candidate | formation-side accumulation and movement-side constrained execution | do not collapse into wiki or optimization doctrine |
| data extraction pipeline cluster | GoScrapy | framing_candidate | external ingest, staged data movement, return/export surface | do not import scraper architecture as package schema |
| AI architecture hype / verification-path cluster | OpenMythos sheepwave | framing_candidate | README / AI summary / architecture narrative vs mechanism / operational path separation | do not treat README, AI reaction, or public narrative as validation |

## 6. material cards

### 6.1 agent-skills

```yaml
alias: agent-skills
source_trace:
  - references/git_search/agent-skills-main
  - docs/reports/formation_movement_interface_agent_skills_external_reference_validation_case_v0.md
  - docs/reports/formation_movement_interface_agent_skills_bounded_comparison_note_v0.md
current_state: strong_defensive_logic / comparison_frame
cluster: governance-architecture cluster
closest_lines:
  - Codex prepare / execution gate
  - validation gate / review-return
  - external ingest / comparison-frame
primary_lens: process-first
safe_next_move: compare_only
promotion_barrier: not direct evidence for Core 7 or package ontology
```

### 6.2 Flutist

```yaml
alias: Flutist
source_trace:
  - docs/reports/formation_movement_interface_flutist_external_reference_validation_case_v0.md
current_state: framing_candidate
cluster: governance-architecture cluster
closest_lines:
  - boundary / role organization
  - architecture surface
  - check-without-mutate validation
primary_lens: boundary-role
safe_next_move: compare_only
promotion_barrier: not direct B evidence without internal reread
```

### 6.3 OMX / oh-my-codex / team-ralph

```yaml
alias: OMX / oh-my-codex / team-ralph
source_trace:
  - references/git_search/oh-my-codex-main
  - docs/reports/formation_movement_interface_single_real_input_pipeline_dry_run_v2.md
  - docs/reports/formation_movement_interface_omx_controller_bounded_comparison_note_v0.md
current_state: framing_candidate
cluster: Codex workflow/runtime cluster
closest_lines:
  - workflow controller
  - Codex interpreter/output mode vs bounded worker-role elevation
  - stage transition
  - artifact passing
  - verification return
primary_lens: process-first / movement orchestration
safe_next_move: compare_only
promotion_barrier: do not import OMX pipeline, command surface, or team runtime as baseline
```

### 6.4 LLM-Wiki + autoresearch

```yaml
alias: LLM-Wiki + autoresearch
source_trace:
  - inputs/external_cases/andrej_karpathy_llm_wiki_medium_note_v0.md
  - references/git_search/autoresearch-master
  - docs/reports/formation_movement_interface_llm_wiki_autoresearch_complete_cycle_note_v0.md
current_state: framing_candidate
cluster: formation-to-movement cycle cluster
closest_lines:
  - formation-side accumulation
  - movement-side constrained execution
  - schema-guided workflow
  - validation gate / keep-discard loop
primary_lens: formation-vs-movement
safe_next_move: compare_only
promotion_barrier: do not collapse the package into wiki doctrine or autonomous optimization doctrine
```

### 6.5 GoScrapy

```yaml
alias: GoScrapy
source_trace:
  - https://news.hada.io/topic?id=28862
  - https://github.com/tech-engine/goscrapy
  - docs/reports/formation_movement_interface_goscrapy_external_material_pipeline_note_v0.md
current_state: framing_candidate
cluster: data extraction pipeline cluster
closest_lines:
  - external ingest / extraction pipeline
  - workflow controller / stage boundary
  - return / export line
  - boundary / replaceable layer line
primary_lens: movement-pipeline
safe_next_move: compare_only
promotion_barrier: not direct package evidence; do not import scraper architecture as schema
```

### 6.6 OpenMythos sheepwave

```yaml
alias: OpenMythos sheepwave
source_trace:
  - https://news.hada.io/topic?id=28853
  - https://flamehaven.space/writing/the-sheepwave-has-a-new-shape-openmythos-and-the-rise-of-architecture-hype/
  - https://flamehaven.space/writing/openmythos-v050-code-review---audit-report/
  - inputs/external_cases/openmythos_sheepwave_original_material_v0.md
  - docs/reports/space_boundary_openmythos_sheepwave_live_intake_analysis_v0.md
current_state: framing_candidate
cluster: AI architecture hype / verification-path cluster
closest_lines:
  - external material intake
  - source-level verification
  - validation return
  - weak-signal direct evidence vs comparison frame
  - Codex interpreter/output mode vs verification evidence
primary_lens: narrative-mechanism-operational path / risk / residue
safe_next_move: compare_only
promotion_barrier: do not treat README, AI assistant reaction, public hype, or architecture vocabulary as proof of operational capability
```

## 7. re-emergence triggers

Use this microspace first when the user asks:

```text
외부자료를 공간에 넣어봐.
이 자료랑 비슷한 라인이 있어?
이 자료가 Codex 작업 흐름에 도움이 돼?
이 자료를 실행/비교/보류 중 어디로 둬야 해?
이전에 넣은 외부자료 다시 찾아서 머지해봐.
```

Default response flow:

```text
1. find closest material or cluster in this microspace
2. reread the new material against existing lines/lenses
3. assign provisional state
4. decide safe next move
5. return a 4-line card
6. update or create a bounded report only if needed
```

## 8. default line/lens map

| User / material signal | First line to check | Likely lens |
| --- | --- | --- |
| skill, workflow discipline, quality gate | Codex prepare / execution gate | process-first / validation-return |
| architecture boundary, dependency graph, rules-as-code | boundary / role organization | boundary-role |
| stage, worker, artifact, verification | workflow controller / role elevation | movement orchestration |
| wiki, accumulated artifact, durable knowledge | formation-side accumulation | formation-vs-movement / residue |
| benchmark, metric, keep/discard loop | movement-side constrained execution | validation-return |
| scraper, crawler, request/response/pipeline | external ingest / extraction pipeline | movement-pipeline / translation |
| AI architecture claim, README-heavy repo, assistant-generated repo summary | source-level verification / validation return | narrative-mechanism-operational path / risk / residue |

## 9. state policy

Default safe states:

- `unclassified` at first contact
- `reread_priority` when role is unclear
- `framing_candidate` when comparison role is clear
- `bounded_action_candidate` only when there is a concrete internal comparison target

Do not use:

- new object family
- weak-signal-only type
- direct evidence lock
- baseline promotion
- implementation permission

## 10. healthy use pattern

Example:

```text
Input: 새 외부자료 URL
Microspace check: similar to GoScrapy / OMX / agent-skills?
Line check: external ingest / workflow controller / validation return?
State: framing_candidate
Next move: compare_only
Output: 4-line card + optional note
```

This is the intended replacement for the earlier fragmented flow.

## 11. user-facing card template

```text
현재 판정:
이유:
다음 이동:
금지선:
```

The user should not need to see the whole microspace unless they ask.

## 12. current verdict

```yaml
verdict: PASS_WITH_NOTE
what_this_solves:
  - external material findability
  - repeated reclassification
  - scattered report/source paths
  - lack of natural re-emergence
what_it_does_not_solve_yet:
  - automatic indexing
  - deciding when to update the microspace
  - real UI/runtime integration
  - automatic source fetching
next_allowed_move:
  - use this index as the default external material reread entrypoint
  - only add entries when a material has actually been read and placed
```
