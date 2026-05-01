# Relay Inbox Request 005 - Run Record Review

## 1. Request Title
샌드박스 런 기록 종합 분석 및 가이드 후보 패턴 추출

## 2. Input Material
- Path/URL: 
  - `app/work/space-skill-sandbox/runs/` (모든 run 기록)
  - `app/work/space-skill-sandbox/review/` (모든 validation 기록)

## 3. User Intent
- run_011~022 기록을 종합 분석하여 반복되는 실패/위험 패턴 추출
- Failure-to-Guide 렌즈를 통해 가이드 후보로 변환
- 반복 패턴과 해결된 위험을 대조하여 시스템 오염 방지 근거 마련
- 4줄 footer 반환

## 4. Expected Sandbox Route
- **Main**: `Run Record Review Skill` (신규/후보)
- **Support**: `failure-to-guide.v0_1.skill.md`

## 5. Constraints
- no installation
- no automation
- no source-space promotion
- no baseline
- no existing file modification

## 6. Stop Points
- 추출된 패턴을 정식 운영 규칙이나 Baseline으로 승격하는 시도

## 7. Requested Output
- 분석 보고서 (`review/run_record_patterns_v0.md`)
- 릴레이 결과 (`relay/outbox/result_005_run_record_review.md`)
- 4-line footer

## 8. 4-line footer expectation
status: 완료
summary: 런 기록을 분석하여 반복 실패 패턴을 가이드 후보로 추출 완료
risk: 반복 패턴을 성급하게 전역 가이드로 승격할 위험
next: 추출된 후보군을 기존 Failure Guide Bundle과 통합 검토
