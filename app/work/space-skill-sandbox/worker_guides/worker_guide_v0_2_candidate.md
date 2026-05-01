# Space Skill Sandbox Worker Guide v0.2 Candidate

## 1. Status
- sandbox candidate guide
- not source-space guide / not baseline
- not automation / not production workflow

## 2. What this guide is
샌드박스 작업자가 샌드박스 내 스킬 후보(Candidate Skill) 중 작업 목적에 맞는 도구를 신속하게 판단하고 참조하기 위한 라우팅 지도다.

## 3. What this guide is not
- 본체(source-space) 운영 기준이나 공식 Baseline 아님.
- 자동 라우터, hook, MCP, watch mode 아님.
- 외부 도구(Graphify 등) 설치 지시서 아님.

## 4. Skill routing
작업 목적에 따라 아래 스킬 후보를 참조한다. (수동 선택)

- **외부 자료(URL/파일) 분석 및 비교**
  → `skills/external-material-intake.skill.md`
- **파일 삭제/Baseline 승격/설치/config 변경/권한 변경 시도 전**
  → `skills/preflight-guard.v0_1.skill.md`
- **작업 결과 요약 및 판단 표면(Footer) 작성**
  → `skills/structured-footer.v0_1.skill.md`
- **Graph Layer/Graphify/Provenace/Mini Graph Map 평가**
  → `skills/graph-layer-evaluation.v0_1.skill.md`

## 5. Universal guardrails
- **완료 ≠ 승인/Baseline/Lock**: 샌드박스 완료는 본체 반영이 아님.
- **source-claimed ≠ truth**: 원문 주장이 항상 사실은 아님.
- **inferred-pattern ≠ baseline**: 추론된 패턴은 공식 기준이 아님.
- **ambiguous-link ≠ 무시 가능**: 모호한 연결은 추가 검증 대상임.
- **[[SYNTH]] node ≠ 원문 용어**: 해석 용어와 원문 용어를 섞지 않음.
- **candidate skill ≠ source-space rule**: 후보 스킬은 정식 규칙이 아님.

## 6. Output rule
모든 샌드박스 run 결과는 마지막에 아래 4줄 footer를 반드시 포함한다.
`status` (완료/검증 필요/사용자 판단 필요/보류), `summary`, `risk`, `next`.

## 7. Stop points (Escalate to User)
아래 항목은 작업자가 독단적으로 진행하지 않고 '사용자 판단 필요'로 올린다.
- source-space promotion / 본체 가이드 업데이트 / Baseline 생성.
- Graphify/gstack 등 외부 도구 설치 및 설정 변경.
- hook/MCP/watch mode 추가 / 자동 reingestion.
- 전체 Deep Space graph화 / 공식 ontology/schema 확정.
- 파일 삭제 / 보안·권한·개인정보 영향 작업.

## 8. 4-line footer
status: 검증 필요
summary: worker_guide_v0_2_candidate는 샌드박스 skill 후보들을 짧게 라우팅하기 위한 guide 후보임
risk: 짧은 guide가 본체 기준이나 자동 router처럼 오해되면 안 됨
next: run_010에서 routing/guardrail/길이 제한이 적절한지 검증
