# Run 001: External Material Intake - Graphify

## 0. Declaration

```yaml
run_id: run_001_external_material_intake_graphify
skill_used: external-material-intake.skill.md
test_material: test_materials/graphify_note.md
mode: read-only sandbox run
baseline: false
implementation: false
automation: false
```

## A. External Material Structure Summary

- material_name: Graphify
- location: Obsidian Graphify note, compacted into `test_materials/graphify_note.md`
- maker_problem: help LLMs understand large folders without reading every file every time
- problem_solved: creates a navigable knowledge graph and high-level report so workers can retrieve relevant structure and subgraphs
- core_components: `GRAPH_REPORT.md`, `graph.json`, `graph.html`, `cache/`, query/path/explain access
- operating_flow: raw folder -> extraction -> concept/relation graph -> report/query outputs -> focused context retrieval
- hidden_assumptions: graph extraction quality is good enough; relationships can be separated by evidence strength; generated graph artifacts remain manageable
- risks: graph-as-truth, inferred edge as baseline, sensitive material exposure, whole-space graphification, always-on hook drift, generated-output noise

## B. Internal Criteria References

### Reference 1

- ref: `deep_space_light_cli_observation_transition_judgment_v0`
- reason: establishes that Deep Space can stay deep while workers should receive only light, bounded context and guardrails

### Reference 2

- ref: `lens_based_asset_reading_note_v0`
- reason: Graphify value depends on lens; it can be useful as a graph/context lens while risky as a truth/baseline layer

## C. Structure Comparison

### Same

- Deep Space should not be read in full for every worker task.
- Evidence strength matters; extracted and inferred material should not be collapsed.
- Context injection should be narrow and task-specific.

### Similar but dangerous

- Graph Layer resembles the desired lightweight worker context layer, but it can become a new authority layer if graph output is treated as truth.
- Graph query resembles useful retrieval, but always-on hooks/watch/MCP could become controller-like operation.

### Different

- Graphify is tool-centered and graph-output-centered.
- The user's space is layer/lens/provenance-centered and keeps user lock above tool output.

### Borrow later

- `GRAPH_REPORT.md` as a worker orientation map.
- query/path/explain as focused context extraction.
- `EXTRACTED / INFERRED / AMBIGUOUS` as evidence-strength language.
- `.graphifyignore` style exclusion rules for generated/tool/private material.

### Reject for now

- whole Deep Space graphification
- always-on hook installation
- MCP integration
- automatic reingestion from graph output
- graph result as baseline evidence
- including sensitive/private material in semantic extraction

## D. Small Dry-run

```yaml
dry_run_question: What happens if Graphify is lowered into this sandbox as a Graph Layer Candidate?
dry_run_result: It becomes a candidate lens for finding connections without reading all material, not a tool adoption decision.
risk: The phrase "Graph Layer" may tempt schema/search-system implementation before a small folder read-only test proves value.
```

Tiny translation:

```text
Graphify external concept
-> graph-layer-evaluation lens candidate
-> worker guide hint: "read map first, query only needed subgraph, preserve extracted/inferred/ambiguous"
-> 4-line footer for user decision
```

## E. Self-check

```yaml
implementation_drift: no implementation performed; tool adoption remains held
external_authority_bias: controlled; Graphify is not treated as truth or default search layer
internal_conflict: possible if Graph Layer is promoted before sandbox validation
user_judgment_required: yes before any real Graphify installation, hook, MCP, or whole-space run
recommended_position: borrow_later / graph_layer_candidate / caution_asset
```

## F. 4-line Footer

```text
status: 검증 필요
summary: Graphify는 Deep Space 전체를 매번 읽지 않고 GRAPH_REPORT/query 같은 지도층으로 필요한 맥락만 꺼내게 하는 Graph Layer Candidate로 가치가 있다.
risk: graph 결과를 truth/baseline으로 보거나 전체 공간, 민감자료, always-on hook에 바로 적용하면 공간 오염과 권한 drift가 생길 수 있다.
next: 전체 도입이 아니라 작은 테스트 폴더에서 read-only graph orientation dry-run을 한 번 검증한다.
```

## G. Run Judgment

```yaml
verdict: PASS_WITH_NOTE
skill_too_heavy: no
internal_reference_count: 2
implementation_jump: false
user_burden_reduced: partial
next_packet_candidate: sandbox_review_or_graph_layer_readonly_dry_run
do_not_promote_as:
  - Graphify adoption mandate
  - graph schema
  - search baseline
  - automation plan
  - MCP/hook setup instruction
```
