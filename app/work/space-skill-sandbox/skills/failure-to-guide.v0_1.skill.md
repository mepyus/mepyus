# failure-to-guide.v0_1.skill

## Status
- sandbox candidate skill
- not source-space rule
- not baseline
- not automation

## Trigger
- validation 결과가 PASS_WITH_NOTE일 때.
- 반복적인 위험 패턴이나 보정 지침이 발견될 때.
- 클로즈아웃 카드에 '아직 하면 안 되는 것'이 구체화되었을 때.
- 작업자 가이드에 추가할 짧고 명확한 경고문이 필요할 때.

## Inputs
- 샌드박스 validation note 및 run 기록.
- 클로즈아웃 카드 및 샌드박스 리뷰 문서.

## Procedure
1. **Material Scan**: validation note 또는 실패 사례를 읽고 핵심 문제를 파악한다.
2. **Classification**: 실패 유형(Truth-overreach, Implementation drift 등)을 분류한다.
3. **Risk Analysis**: 이 실패가 반복될 경우 발생할 수 있는 시스템 오염이나 비용 문제를 정의한다.
4. **Candidate Synthesis**: 다음 작업자가 즉각적으로 수행하거나 주의할 수 있는 짧은 가이드 문장(Guide Candidate)을 작성한다.
5. **Self-Correction**: 생성된 문장이 Baseline이나 절대적 규칙처럼 표현되지 않았는지 확인한다.
6. **Disposition**: 가이드 후보를 Borrow (보관) / Hold (보류) / Reject (기각)로 분류한다.
7. **Reporting**: 4줄 footer와 함께 결과를 반환한다.

## Conversion Rules
각 변환 결과는 아래 형식을 따른다.
- **failure_material**: 입력된 실패/위험 소재.
- **risk_if_repeated**: 반복 시 발생할 위험.
- **guide_candidate**: 제안되는 가이드 문장.
- **status**: candidate / hold / reject / needs_user_judgment.
- **action**: 후속 조치 (보관, 검증 필요 등).

## Forbidden Drift
- 단일 실패를 전체 시스템의 Baseline으로 자동 승격하지 말 것.
- 가이드 후보 문장을 정식 운영 규칙(source-space rule)으로 명명하지 말 것.
- 본체 가이드(source-space guide)를 작업자 독단으로 수정하지 말 것.
- 가이드 생성을 자동화하거나 reingestion과 연결하지 말 것.

## Output Format
- 변환 요약 테이블
- Borrow / Hold / Reject 분류 결과
- 4줄 Footer

## 4-line Footer
status: [완료 / 검증 필요 / 사용자 판단 필요]
summary: [한 문장 요약]
risk: [핵심 위험 요소]
next: [다음 행동]
