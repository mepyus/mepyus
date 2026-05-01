# Space Skill Sandbox Worker Guide v0.3 Candidate

## 1. Status
- sandbox candidate guide
- not source-space guide / not baseline
- not automation / not production workflow

## 2. What this guide is
샌드박스 작업자가 샌드박스 내 스킬 후보(Candidate Skill) 중 목적에 맞는 도구를 신속하게 판단하고 참조하기 위한 짧은 라우팅 지도다.

## 3. Skill routing
작업 목적에 따라 아래 스킬 후보를 수동으로 참조한다.

- **외부 자료(URL/파일) 분석 및 비교**
  → `skills/external-material-intake.skill.md`
- **파일 삭제/Baseline 승격/설치/config 변경/권한 변경 시도 전**
  → `skills/preflight-guard.v0_1.skill.md`
- **작업 결과 요약 및 판단 표면(Footer) 작성**
  → `skills/structured-footer.v0_1.skill.md`
- **Graph Layer/Graphify/Provenace/Mini Graph Map 평가**
  → `skills/graph-layer-evaluation.v0_1.skill.md`
- **Validation note/반복 위험을 가이드 후보 문장으로 변환**
  → `skills/failure-to-guide.v0_1.skill.md`

## 4. Universal guardrails
- **완료 ≠ 승인 / lock / baseline**: 샌드박스 완료는 본체 반영이 아님.
- **source-claimed ≠ truth**: 원문 주장은 사실 확정이 아님.
- **inferred-pattern ≠ baseline**: 추론된 패턴은 공식 기준이 아님.
- **ambiguous-link = 추가 검증 필요**: 모호한 연결은 무시하지 않음.
- **[[SYNTH]] node ≠ 원문 용어**: 해석 용어와 원본 데이터를 섞지 않음.
- **낮은 위험 read-only 확인**: 단순 파일 존재 확인 등은 허용 가능.

## 5. Stop points (Escalate to User)
아래 항목은 독단적으로 진행하지 않고 '사용자 판단 필요'로 올린다.
- source-space promotion / 본체 가이드 업데이트 / Baseline 생성.
- Graphify/gstack 등 외부 도구 설치 및 설정 변경 / 자동화 / Hook 추가.
- 전체 Deep Space graph화 / 공식 ontology 및 schema 확정.
- 파일 삭제 / 보안·권한·개인정보 영향 작업.

## 6. Output rule
모든 샌드박스 run 결과는 마지막에 아래 4줄 footer를 반드시 포함한다.
`status` (완료/검증 필요/사용자 판단 필요/보류), `summary`, `risk`, `next`.

## 7. Failure candidate handling
- failure material은 가이드 후보의 원료일 뿐, 곧바로 baseline이 되지 않는다.
- 가이드 후보 문장은 번들에 먼저 보관하고, 반복성이 확인된 것만 선별 반영한다.

## 8. 4-line footer
status: 검증 필요
summary: worker_guide_v0_3_candidate는 v0.2 라우팅 구조에 failure-to-guide skill과 반복 guardrail 후보를 보강한 sandbox guide 후보임
risk: v0.3 guide가 source-space guide나 자동 router처럼 오해되면 안 됨
next: run_013에서 길이, 라우팅 정확도, failure candidate 선별 적절성을 검증
