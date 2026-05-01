# Run 002: External Material Intake - Graphify with Skill v0.1

## Declaration

```yaml
run_id: run_002_external_material_intake_graphify_v0_1
skill_used: external-material-intake.v0_1.skill.md
lens_used: external-material-intake-lens.md
worker_guide_used: worker_guide_v0.md
test_material: test_materials/graphify_note.md
mode: read-only sandbox rerun
baseline: false
implementation: false
automation: false
```

## material

Graphify turns a folder into a knowledge graph and produces `GRAPH_REPORT.md`, `graph.json`, `graph.html`, cache, and query/path/explain access.

Its useful idea is "read a map first, then retrieve only the subgraph needed for the current question."

## internal_refs

1. `deep_space_light_cli_observation_transition_judgment_v0`
   - Deep Space can stay deep while workers receive only minimal guardrails and context.
2. `lens_based_asset_reading_note_v0`
   - A tool can be useful in one lens and risky in another.

## same

- Avoid feeding the whole space to every worker.
- Preserve evidence strength instead of treating all relations as truth.
- Use focused context extraction.

## similar_but_dangerous

- Graph Layer can help worker context, but it can also become an accidental authority layer.
- Query/path/explain can reduce context load, but hook/MCP/watch mode can drift toward controller behavior.

## different

- Graphify is graph-tool centered.
- The user's space is user-lock, layer/lens, and provenance centered.

## borrow_later

- `GRAPH_REPORT.md` as orientation map.
- focused subgraph query as context injection candidate.
- `EXTRACTED / INFERRED / AMBIGUOUS` as evidence-strength vocabulary.
- ignore/exclusion rules for generated, private, or tool files.

## reject_for_now

- whole-space Graphify run
- sensitive/private material extraction
- hook/MCP/watch setup
- graph output as baseline
- automatic reingestion from graph output

## tiny_dry_run

```text
Question:
What connects worker guide to external material intake?

Expected graph-layer use:
Read a small report/map first.
Extract only the concepts around worker guide, external intake, evidence, and implementation drift.
Return a 4-line footer instead of raw graph output.
```

## self_check

```yaml
implementation_drift: false
external_authority_bias: false
internal_conflict: possible only if graph layer is promoted before validation
user_judgment_required: true before any installation, hook, MCP, whole-space run, or sensitive material processing
recommended_position: borrow_later / graph_layer_candidate / caution_asset
```

## footer

```text
status: 검증 필요
summary: Graphify는 Deep Space와 Worker 사이에 "지도 먼저, 필요한 subgraph만"이라는 Graph Layer Candidate를 제안한다.
risk: graph output을 truth/baseline으로 보거나 hook/MCP/전체 공간 처리로 바로 가면 controller화와 공간 오염 위험이 있다.
next: Graphify 도입이 아니라, 작은 테스트 폴더에서 read-only graph orientation 질문 1개만 검증한다.
```

## run_result

```yaml
verdict: PASS_WITH_NOTE
why_not_ok: next step still requires one more sandbox review to confirm the shorter skill reduced burden
skill_lines: 46
internal_reference_count: 2
footer_clear: true
implementation_jump: false
user_decision_clear: true
```
