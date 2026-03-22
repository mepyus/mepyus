# Comparison Summary

- 총 fragment 수: 4
- 실제 비교 fragment 수: 4
- processor별 유효 출력 수: codex=4, chatgpt=4, gemini=4
- stable / split / hidden_candidate / broken_link 개수: 1 / 1 / 1 / 1

## Divergence Anchors
- input_layer (codex): 1
- label_consistency (codex): 1
- label_consistency (chatgpt): 1
- viewer_deprioritized (chatgpt): 1
- input_layer (gemini): 1
- label_consistency (gemini): 1
- adjustment_data (codex): 1
- adjustment_data (gemini): 1
- label_refinement (gemini): 1
- hidden_axis (codex): 1

## Scene Disagreement Top
- instruction, instruction, reflection: 1

## Role Disagreement Top
- definition, support, thesis: 1

## Tag Mismatch Examples
- frag_002: semantic_overlap=0.5, structural_overlap=0.0
- frag_003: semantic_overlap=0.5, structural_overlap=0.5
- frag_004: semantic_overlap=0.6667, structural_overlap=0.5

## 입력기 조정 후보 포인트
- split fragments with repeated scene or role disagreement
- review fragments where anchor overlap stays low across all processors

## 라벨기 조정 후보 포인트
- tighten scene and role boundary guidance for repeated disagreement clusters
- review semantic tag vocabulary when hidden_candidate tags repeat
