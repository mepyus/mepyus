# Gemini-Codex File Handoff Protocol v0

## 1. 목적
사용자의 중계 없이 Gemini CLI와 Codex 간의 작업 결과를 파일 기반으로 교환하여 병목을 제거하고 효율을 극대화함.

## 2. 작업 폴더 구조 (Sandbox)
모든 작업은 `runtime/gemini_sandbox/<case_id>/`에서 수행함.
- `instruction.md`: Codex가 작성 (Gemini 작업 지시)
- `result.md`: Gemini가 작성 (작업 결과)
- `self_audit.md`: Gemini가 작성 (자기 검증)
- `codex_review.md`: Codex가 작성 (Gemini 결과 검산/리뷰)
- `next_packet.md`: Codex가 작성 (다음 Gemini 지시)

## 3. 원칙
- 모든 파일은 독립적이며 파일 단위로 관리됨.
- Codex는 `worker_return`을 기준으로 파일을 읽고 평가함.
- Gemini는 sandbox 영역 밖의 파일을 절대 수정/생성하지 않음.
- 사용자는 `case_id`만 전달하여 워크플로우를 트리거함.

## 4. 재분류 정책 (Correction Patch)
- Gemini의 분류가 부적절한 경우, Codex가 `codex_review.md`를 통해 직접 보정하고 `CLOSED` 처리함.
- 외부 자료와 내부 자산의 혼동(Source Role Confusion)은 Codex가 관리함.
