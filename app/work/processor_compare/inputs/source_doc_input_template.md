# Source Doc Input Template

아래 형식으로 처리자에게 원문 하나를 전달한다.

```text
[input metadata]
input_doc_id: doc_001
input_bundle_id: bundle_compare_v1
source_type: planning_note
fragment_version: v1

[source text]
여기에 원문 전체를 넣는다.
```

권장 사항:
- 한 번에 source document 하나씩 전달한다.
- 세 처리자는 같은 원문과 같은 입력 메타를 사용한다.
- 각 처리자는 자기 방식대로 fragment를 자르되, 원문 바깥 내용을 추가하면 안 된다.
