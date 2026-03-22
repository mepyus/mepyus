# probe delta compare round1 vs round2

## 1. reading counts
- round1 canonical: `3`
- round2 canonical: `3`
- round1 mixed: `3`
- round2 mixed: `3`

## 2. repeated anchor top groups
- round1 top: ai_business, harness_agent, health_human, model_compute, organization_ax
- round2 top: ai_business, harness_agent, health_human, model_compute, organization_ax
- shared anchors: ai_business, harness_agent, health_human, model_compute, organization_ax

## 3. strongest surviving flow compare
- round1은 OpenClaw / harness / model / bundle-unbundle 축이 강했다.
- round2는 Backend.AI:GO / harness / agent coding / startup opportunity 축이 강하게 살아남았다.

## 4. weakest transition compare
- round1은 기술 설명 -> 사업/조직 판단 전환부가 mixed hold로 남았다.
- round2도 제품 설명 -> 산업 판단, 기술 -> 조직 적응, 실전 데모 -> 사업 전략 전환부가 mixed hold로 남았다.

## 5. repeated failure pattern
- repeated mixed gaps: technical -> business passage stays active but closure remains transition-led
- repeated anchor는 충분한데 closure가 transition-led라 stable reading으로 안 닫히는 패턴이 두 번 다 보인다.

## 6. repeated success pattern
- straight flow로 이어지는 제품/하네스/모델 설명은 두 번 다 canonical로 비교적 잘 닫힌다.
- 반복 앵커가 강하고 전환 밀도가 낮은 window는 stable_reading으로 남는다.

## 7. 새로 드러난 것 / 여전히 반복된 것
- 새로 드러난 것: round2는 product demo / automation pipeline / startup thesis가 하나의 흐름으로 더 선명하게 잡힌다.
- 여전히 반복된 것: transition-led closure weakness와 mixed hold necessity는 round1과 동일하게 반복된다.
