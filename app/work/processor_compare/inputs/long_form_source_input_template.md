# Long Form Source Input Template

장문 문서를 처리자에게 줄 때 아래 형식을 사용한다.

```text
[input metadata]
input_doc_id: doc_005
input_bundle_id: bundle_compare_v1
source_type: reference_article
fragment_version: v1

[source text]
여기에 장문 원문 전체를 넣는다.
```

권장 사용 순서:

1. `standards/processor_execution_prompt_v2.md`
2. 처리자별 보정 프롬프트
   - ChatGPT: `standards/chatgpt_calibration_prompt_v1.md`
   - Gemini: `standards/gemini_calibration_prompt_v1.md`
3. 위 장문 입력 블록

권장 상황:
- 5개 이상 fragment로 나뉠 수 있는 장문 문서
- 정의, 예시, 문제, 해법, 구조 설명, 결론이 함께 있는 문서
