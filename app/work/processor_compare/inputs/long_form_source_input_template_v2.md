# Long Form Source Input Template v2

장문 문서를 처리자에게 줄 때 아래 형식을 사용한다.

```text
[input metadata]
input_doc_id: doc_008
input_bundle_id: bundle_compare_v1
source_type: reference_article
fragment_version: v1

[output constraints]
- source text 전체를 읽고 처리자가 스스로 fragment를 절단한다.
- 출력은 processed fragment 객체들만 담은 JSON 배열 하나여야 한다.
- input_doc_id, input_bundle_id, source_type, fragment_version 는 입력값을 그대로 유지한다.
- fragment_text는 실제 원문 구간을 보존한다. `...` 축약 금지.

[source text]
여기에 장문 원문 전체를 넣는다.
```

권장 사용 순서:

1. `standards/processor_execution_prompt_v2.md`
2. 처리자별 보정 프롬프트 v2
   - ChatGPT: `standards/chatgpt_calibration_prompt_v2.md`
   - Gemini: `standards/gemini_calibration_prompt_v2.md`
3. 위 장문 입력 블록

권장 상황:

- 5개 이상 fragment로 나뉠 수 있는 장문 문서
- 정의, 예시, 문제, 해법, 구조 설명, 결론이 함께 있는 문서
- 철학/문화 장문처럼 사례와 정조가 함께 들어 있는 문서
