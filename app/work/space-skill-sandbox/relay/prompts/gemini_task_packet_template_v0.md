# Gemini Task Packet Template v0

## 1. Task Declaration
*이 패키지는 사용자의 inbox 요청을 기반으로 샌드박스 가이드를 수행하는 실행 지침입니다.*

## 2. Read First
- `app/work/space-skill-sandbox/worker_guides/worker_guide_v0_3_candidate.md`
- `app/work/space-skill-sandbox/relay/inbox/[USER_REQUEST_FILE]`

## 3. Input Request
*inbox의 요청서 내용을 읽고 분석 목표를 확인하십시오.*

## 4. Routing Instruction
먼저 `worker_guide_v0_3_candidate.md`를 읽고, 사용자의 요청이 5개 스킬 후보 중 어디에 해당하는지 판단하십시오. 여러 스킬을 복합 참조해야 할 경우 가이드의 라우팅 지침을 따르십시오.

## 5. Required Skill Consultation
판단된 라우팅에 따라 아래 스킬 중 필요한 것을 참조하십시오.
- `skills/external-material-intake.skill.md`
- `skills/preflight-guard.v0_1.skill.md`
- `skills/structured-footer.v0_1.skill.md`
- `skills/graph-layer-evaluation.v0_1.skill.md`
- `skills/failure-to-guide.v0_1.skill.md`

## 6. Forbidden Actions
- source-space promotion 금지.
- baseline / schema / ontology 생성 및 확정 금지.
- 외부 도구 설치 및 설정 변경 금지.
- 자동화 / hook / MCP / watch mode 생성 금지.
- 기존 가이드 및 본체 문서 직접 수정 금지.

## 7. Files to Create
- `runs/run_[NUMBER]_[NAME].md`
- `review/validation_round_[NUMBER].md`
- `relay/outbox/[RESULT_NAME].md`

## 8. Validation Requirements
모든 작업은 샌드박스 경계를 준수했는지, 가이드의 라우팅을 정확히 따랐는지 검증되어야 합니다.

## 9. Final Report Format
결과는 `relay/outbox/result_template_v0.md` 형식을 사용하여 보고하십시오.

## 10. Closeout Sentence
This is a sandbox task executed via Relay Protocol v0. No source-space promotion or automation was performed.
