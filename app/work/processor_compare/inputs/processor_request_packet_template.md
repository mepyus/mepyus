# Processor Request Packet Template

아래 순서대로 사용한다.

1. `standards/processor_execution_prompt_v2.md` 전체를 처리자에게 먼저 준다.
2. 그 다음 아래 source document 입력 블록 하나를 붙여 넣는다.
3. 반환된 JSON 배열을 해당 처리자 raw 폴더의 문서 파일에 저장한다.

## 단일 source document 요청 블록

```text
[input metadata]
input_doc_id: doc_001
input_bundle_id: bundle_compare_v1
source_type: planning_note
fragment_version: v1

[source text]
여기에 원문 전체를 넣는다.
```

## 저장 예시

- ChatGPT 응답 저장: `processor_outputs/raw/chatgpt/doc_001.jsonl`
- Gemini 응답 저장: `processor_outputs/raw/gemini/doc_001.jsonl`
- Codex 응답 저장: `processor_outputs/raw/codex/doc_001.jsonl`

각 파일은 JSON 배열 또는 JSONL 형식 모두 허용한다.

```json
[
  {"input_doc_id":"doc_001","input_bundle_id":"bundle_compare_v1","fragment_id":"chatgpt_doc_001_frag_001","fragment_text":"...","source_type":"planning_note","fragment_version":"v1","anchors":[],"direction":0.0,"intensity":0.0,"stability":0.0,"scene":"unknown","role":"unknown","semantic_tags":[],"structural_tags":[],"confidence":0.0,"ambiguity":1.0,"evidence_text":["..."],"why_short":"...","processor_notes":[]},
  {"input_doc_id":"doc_001","input_bundle_id":"bundle_compare_v1","fragment_id":"chatgpt_doc_001_frag_002","fragment_text":"...","source_type":"planning_note","fragment_version":"v1","anchors":[],"direction":0.0,"intensity":0.0,"stability":0.0,"scene":"unknown","role":"unknown","semantic_tags":[],"structural_tags":[],"confidence":0.0,"ambiguity":1.0,"evidence_text":["..."],"why_short":"...","processor_notes":[]}
]
```
