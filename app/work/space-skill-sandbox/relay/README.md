# Space Skill Sandbox Relay v0

## 1. Purpose
Space Skill Sandbox Relay v0는 사용자와 Gemini 간의 수동 복붙(copy-paste) 병목을 줄이기 위해 도입된 파일 기반의 최소 작업 전달 규약이다.

## 2. What this relay is
- 파일 기반의 비동기 작업 전달 표면.
- 사용자 요청(inbox)과 작업 결과(outbox)의 물리적 분리.
- 샌드박스 가이드(`worker_guide_v0_3_candidate`)를 참조하기 위한 실행 통로.

## 3. What this relay is not
- 자동화 시스템(watch mode, cron 등)이 아님.
- MCP 연결이나 자동화 hook이 아님.
- 실시간 채팅/자동 지시 시스템이 아님.

## 4. Folder roles
- **inbox/**: 사용자가 요청서(`request_template_v0.md` 기반)와 외부 자료를 넣는 곳.
- **prompts/**: Gemini가 요청서를 읽고 샌드박스 규약에 따라 실행하기 위한 지시서 템플릿.
- **outbox/**: Gemini가 작업 완료 후 결과를 남기는 곳(`result_template_v0.md` 기반).
- **review/**: 릴레이 작동의 무결성과 경계 준수를 검토한 기록을 남기는 곳.

## 5. Basic flow
1. 사용자가 `inbox/`에 요청서와 자료를 생성한다.
2. Gemini가 `prompts/gemini_task_packet_template_v0.md`와 `inbox/`의 요청서를 읽는다.
3. Gemini가 샌드박스 가이드에 따라 작업을 수행한다.
4. Gemini가 `outbox/`에 결과를 생성한다.
5. 사용자가 결과를 확인하고 최종 판단을 내린다.

## 6. User role
- 작업 요청 및 자료 제공자.
- 최종 판단 및 source-space promotion 승인자.
- 샌드박스 경계 준수 감시자.

## 7. Gemini worker role
- 요청서 판독 및 가이드 기반 라우팅.
- 샌드박스 내 분석 수행 및 기록 생성.
- 결과 요약 및 위험 보고.

## 8. Stop points
아래 요청은 릴레이에서 수행하지 않고 '사용자 판단 필요'로 격상한다.
- source-space promotion / baseline 생성.
- 자동화 / hook / MCP / watch mode 도입.
- 외부 도구 설치 및 설정 변경.
- 기존 가이드 및 본체 문서 수정.

## 9. Output rule
모든 결과는 `result_template_v0.md` 형식을 따르며, 4줄 footer를 포함해야 한다.

## 10. 4-line footer
status: 완료
summary: Sandbox Relay v0 규약을 정의하여 파일 기반의 안전한 작업 전달 구조를 마련함
risk: 자동화나 watch mode로의 오용을 경계해야 함
next: 실제 inbox 요청을 통한 dry-run 수행
