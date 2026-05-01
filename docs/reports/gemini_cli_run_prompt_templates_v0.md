# gemini_cli_run_prompt_templates_v0.md

## 목적
Gemini CLI에게 넘길 표준 프롬프트 템플릿.

## Template
```text
[Task Instruction]
목적: {목적 기술}
읽을 파일: {목록}
수정할 파일: {파일}
추가할 섹션: {섹션명}

[가이드라인]
1. repo 전체를 읽지 않는다.
2. 시스템 전체 요약을 하지 않는다.
3. 재료들을 개별 독립 처리한다.
4. Gemini 결과는 반드시 worker_return으로 반환한다.

[기대 결과]
{결과물 기술}

[완료 보고 형식]
Verdict:
Modified file:
Added section:
4-line card:
Batch-level self-check:
```
