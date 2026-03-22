# Processor Compare Pipeline

이 작업 폴더는 동일 원문 입력에 대한 `codex / chatgpt / gemini` 출력값을 저장하고 비교하기 위한 sidecar 파이프라인이다.

핵심 원칙:
- raw 출력은 절대 덮어쓰지 않는다
- Replica core는 수정하지 않는다
- 비교 목적은 정답 판정이 아니라 입력기/앵커기/라벨기 조정 데이터 축적이다
- `doc_005`는 calibration 문서로 우선 취급한다

## 구조

- `standards/processor_standard_v1.md`: 처리자 공통 schema 기준
- `standards/processor_execution_prompt_v2.md`: ChatGPT/Gemini용 실행 프롬프트
- `standards/doc_005_learning_pack_v0_1.md`: doc_005 기반 calibration 기준선
- `standards/calibration_guardrails_v0_1.md`: 입력기/라벨기/점수/anchor 세부 guardrail
- `standards/scene_role_decision_table_v0_1.md`: scene/role 빠른 판정표
- `standards/long_form_calibration_set_v0_1.md`: doc_005/doc_006 장문 calibration 세트
- `standards/philosophy_culture_guardrails_v0_1.md`: 철학/문화 장문 calibration 기준
- `standards/calibration_taxonomy_v0_1.md`: 문서 타입별 calibration taxonomy
- `standards/conversation_transcript_guardrails_v0_1.md`: 대화 기록 장문 calibration 기준
- `standards/label_score_focus_v0_1.md`: 축값/라벨기 중심 calibration 기준
- `standards/boundary_case_generation_prompt_v1.md`: 경계 사례 생성 프롬프트
- `standards/boundary_case_calibration_loop_v0_1.md`: 경계 사례 기반 calibration loop
- `standards/chatgpt_calibration_prompt_v1.md`: ChatGPT 장문 보정 프롬프트
- `standards/gemini_calibration_prompt_v1.md`: Gemini 장문 보정 프롬프트
- `standards/chatgpt_calibration_prompt_v2.md`: ChatGPT 장문 보정 프롬프트 v2
- `standards/gemini_calibration_prompt_v2.md`: Gemini 장문 보정 프롬프트 v2
- `inputs/source_docs/`: 공통 원문 보관 위치
- `inputs/sample_fragments.jsonl`: 고정 fragment 샘플
- `inputs/source_doc_input_template.md`: 처리자 입력 메타 템플릿
- `inputs/long_form_source_input_template.md`: 장문 문서 입력 템플릿
- `inputs/long_form_source_input_template_v2.md`: 장문 문서 입력 템플릿 v2
- `inputs/boundary_case_request_template_v1.md`: 경계 사례 생성 요청 템플릿
- `inputs/naming_convention.md`: 파일명과 fragment_id 규칙
- `inputs/doc_fragment_sheet_template.md`: 문서별 fragment 고정 시트
- `inputs/processor_request_packet_template.md`: 처리자 요청/저장 템플릿
- `processor_outputs/raw/<processor>/`: 처리자별 원본 출력
- `processor_outputs/normalized/<processor>/`: 정규화 출력
- `reports/`: 비교 결과와 summary
- `scripts/`: validate, normalize, compare, runner

## 사용 순서

1. `inputs/source_docs/`에 공통 원문을 넣고, 같은 원문을 각 처리자에게 준다.
2. 각 처리자가 자율적으로 fragment를 자른 raw JSON 또는 JSONL 파일을 `processor_outputs/raw/codex`, `chatgpt`, `gemini` 에 넣는다.
3. 아래 명령을 실행한다.

```bash
app/work/processor_compare/scripts/run_compare_pipeline.sh
```

4. 결과는 `reports/` 아래에서 확인한다.

주요 결과물:
- `comparison_summary.json`
- `comparison_summary.md`
- `stable.jsonl`
- `split.jsonl`
- `hidden_candidate.jsonl`
- `broken_link.jsonl`
