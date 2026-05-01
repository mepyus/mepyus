# Failure-to-Guide Lens

## 1. Lens Name
Failure-to-Guide Lens

## 2. Purpose
샌드박스 작업 중 발생한 실패, 위험 신호, PASS_WITH_NOTE, 검증 노트를 분석하여 다음 작업자가 반복하지 않도록 가이드 후보 문장으로 변환하기 위한 분석 관점을 제공한다.

## 3. What counts as failure material
- **Truth-overreach**: 추론을 사실로, 주장을 진실로 오해하는 경향.
- **Source anchor missing**: 근거 없이 주장만 남기는 행위.
- **Candidate promotion**: 후보(Candidate)를 정식 기준(Baseline)으로 착각하는 행위.
- **Approval misread**: '완료' 상태를 '승인'이나 'Lock'으로 오해하는 행위.
- **Implementation drift**: 연구 단계에서 설치나 자동화로 미끄러지는 현상.
- **Over-blocking**: 낮은 위험의 읽기 작업까지 과하게 차단하여 작업 흐름을 방해하는 행위.
- **[[SYNTH]] conflation**: 해석 용어를 원문 고유 용어와 혼동하는 행위.

## 4. What should be extracted
- 반복되는 실수 패턴.
- 검증 단계에서 공통적으로 지적된 보정 사항.
- 클로즈아웃 카드에 명시된 '아직 하면 안 되는 것'들의 실무적 경고문.

## 5. What must not be over-promoted
- 개별 실패 사례를 곧바로 프로젝트 전체의 Baseline으로 격상하지 않는다.
- 가이드 후보 문장을 정식 운영 규칙(source-space rule)으로 선언하지 않는다.

## 6. Failure-to-Guide conversion frame
- **Input**: 실패/위험 소재 (Failure Material)
- **Transformation**: 위험 인지 -> 실무적 경고문(Guide Candidate) 생성.
- **Output**: Borrow (보관 및 가이드화) / Hold (추가 관찰) / Reject (과잉 일반화 방지).

## 7. User-language summary
실패는 버리는 데이터가 아니라, 다음 작업자가 밟지 말아야 할 '지뢰 위치'를 알려주는 소중한 원료입니다. 이 렌즈는 실패 기록을 단순히 보관하는 데 그치지 않고, 작업자가 즉시 이해하고 행동을 수정할 수 있는 짧고 명확한 경고문으로 바꾸는 것을 목표로 합니다.

## 8. 4-line footer
status: 완료
summary: 실패와 보정 신호를 가이드 후보로 전환하기 위한 Failure-to-Guide Lens를 정의함
risk: 실패 소재를 과도하게 일반화하여 불필요한 제약을 만들 위험이 있음
next: failure-to-guide.v0_1.skill.md 작성
