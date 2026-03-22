# Comparison Summary

- 총 문서 수: 8
- 총 raw fragment 수: 177
- 실제 비교 기준 fragment 수: 65
- processor별 유효 출력 수: codex=65, chatgpt=66, gemini=46
- processor별 후매칭 실패 fragment 수: chatgpt=17, gemini=7
- stable / split / hidden_candidate / broken_link 개수: 0 / 35 / 0 / 30

## Divergence Anchors
- ontology_definition (codex): 2
- ontology (chatgpt): 2
- graph_rag (codex): 2
- graph_db (chatgpt): 2
- graph_rag (chatgpt): 2
- knowledge_representation (codex): 1
- semantic_web_expression (codex): 1
- knowledge_representation (chatgpt): 1
- semantic_web_formalization (chatgpt): 1
- knowledge_representation (gemini): 1

## Calibration Signals
- mechanism_value_boundary_candidate: 10
- meta_overreach_candidate: 5
- mid_granularity_candidate: 48
- overmerged_candidate: 54
- oversegmentation_candidate: 12
- problem_solution_boundary_candidate: 6
- summary_definition_boundary_candidate: 10

## Scene Disagreement Top
- explanation, missing, missing: 8
- evidence, explanation, missing: 5
- explanation, explanation, missing: 5
- explanation, explanation, reflection: 4
- evidence, explanation, explanation: 2
- comparison, explanation, explanation: 2
- explanation, explanation, instruction: 2
- evidence, missing, missing: 2
- comparison, comparison, missing: 2
- missing, missing, reflection: 2

## Role Disagreement Top
- missing, missing, support: 3
- example, example, missing: 3
- expansion, support, support: 3
- contrast, contrast, missing: 3
- expansion, missing, missing: 3
- definition, definition, support: 2
- bridge, expansion, thesis: 2
- definition, definition, thesis: 2
- definition, definition, missing: 2
- definition, definition, expansion: 2

## Tag Mismatch Examples
- doc_001_frag_001: semantic_overlap=0.375, structural_overlap=0.0
- codex_doc_002_frag_001: semantic_overlap=0.0, structural_overlap=0.0
- codex_doc_002_frag_002: semantic_overlap=0.0, structural_overlap=0.0
- codex_doc_002_frag_003: semantic_overlap=0.0, structural_overlap=0.0
- codex_doc_002_frag_004: semantic_overlap=0.0, structural_overlap=0.0
- codex_doc_003_frag_001: semantic_overlap=0.6667, structural_overlap=0.0
- codex_doc_003_frag_002: semantic_overlap=0.0, structural_overlap=0.0
- codex_doc_003_frag_003: semantic_overlap=0.0, structural_overlap=0.0
- codex_doc_003_frag_004: semantic_overlap=0.5, structural_overlap=0.3333
- codex_doc_003_frag_005: semantic_overlap=0.0, structural_overlap=0.0

## 입력기 조정 후보 포인트
- split fragments with repeated scene or role disagreement
- review fragments where anchor overlap stays low across all processors
- review summary_definition_boundary, problem_solution_boundary, and mechanism_value_boundary patterns

## 라벨기 조정 후보 포인트
- tighten scene and role boundary guidance for repeated disagreement clusters
- review semantic tag vocabulary when hidden_candidate tags repeat
- report scene_schema_violation and meta_overreach explicitly during calibration review
