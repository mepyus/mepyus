# Component Chain Mode Selection Rule Candidate v0

## 1. Status
**STATUS: COMPONENT_CHAIN_MODE_SELECTION_RULE_CANDIDATE_COMPLETE**

## 2. Executive summary
이 모드 선택 규칙(Mode Selection Rule)은 우리 공간의 구조적 실행 부품들을 1회성 작업부터 고위험 판단까지 유연하게 다룰 수 있도록 돕는 **'운영의 경량화 도구'**입니다. 체인의 모든 단계를 매번 강제하는 대신, 상황의 복잡도와 위험도에 따라 Compact, Standard, Heavy 세 가지 모드로 나누어 불필요한 의식(Ceremony)을 줄이고 실질적인 판단에 집중합니다. 이는 워크플로우를 만드는 것이 아니라, **'공간을 어떻게 가볍게 운영할지'에 대한 판단 문법**입니다.

## 3. Mode map

| Mode | Use when | Minimum fields | Avoid | Current state |
| :--- | :--- | :--- | :--- | :--- |
| **Compact** | 1회성 / 저위험 / 빠른 확인 | input, intent, next_action | formal workflow | candidate_usage_rule |
| **Standard** | 재사용 가능 / 후보 자료 / 도구/API 검토 | intake, boundary, linkage, re-entry | registry, schema | candidate_usage_rule |
| **Heavy** | 고위험 / 권한 분리 / 구조적 변경 가능성 | 모든 필드 + authority_risk, User_gate | implementation planning | candidate_usage_rule |

## 4. Mode selection questions (결정 시퀀스)
1. 이것은 1회성인가, 재사용 가능한 후보인가?
2. 구현/도입 위험이 있는가? (Tool attachment, Workflow change 등)
3. Resource/Tool 구분이 필요한가?
4. 계획 검토가 먼저 필요한가? (Plan Packet)
5. 이전 기록과의 연결이 필요한가?
6. 사용자 승인이 필수적인가?

- **대부분 NO → Compact**
- **일부 YES → Standard**
- **고위험 YES → Heavy**

## 5. Templates

### 5.1 Compact Template
```markdown
# Compact Component Chain Check
- input:
- user intent:
- expected output:
- do-not-infer:
- next safe action:
```

### 5.2 Standard Template
```markdown
# Standard Component Chain Check
## 1. Intake
- input:
- user intent:
- one-time or reusable:
- Resource / Tool / Both:
- Plan needed?:

## 2. Retrieval boundary
- prior records:
- include:
- exclude:
- stop condition:
- caution:

## 3. Linkage
- possible connection:
- state:
- evidence:
- missing evidence:

## 4. Return
- watch items:
- user decision needed:
- next safe action:
```

### 5.3 Heavy Template
```markdown
# Heavy Component Chain Check
## 1. Intake
- input:
- user intent:
- one-time or reusable:
- Resource / Tool / Both:
- Plan needed?:

## 2. Risk boundary
- implementation risk:
- authority risk:
- automation risk:
- external architecture risk:
- do-not-do-yet:

## 3. Retrieval boundary
- prior records:
- include:
- exclude:
- stop condition:
- caution:

## 4. Linkage
- possible connection:
- state:
- line candidate?:
- axis candidate?:
- evidence:
- missing evidence:
- axis naming premature?:

## 5. Re-entry
- current safe state:
- preserved signal:
- next natural trigger:
- not current-position update:
```

## 6. Relation to existing chain
- **Modifying Usage:** 이 모드 규칙은 기존 부품(Intake, Linkage 등)을 교체하는 것이 아니라, 상황에 따라 **"어디까지 꺼내 쓸지"**를 결정하는 상위 조절 장치입니다.
- **Boundaries:** 각 모드는 내부적으로 여전히 모든 'Do not do yet' 경계를 준수합니다.

## 7. Ceremony risk reduction
- **필드 선별:** 모든 입력에 Heavy 양식을 강제하지 않습니다.
- **의식화 방지:** 모드 판단 자체가 일종의 의식이 되지 않도록, 판단은 오직 '도구 후보'가 들어올 때만 합니다.
- **판단 유예:** 모드를 확정짓지 말고, 상황에 따라 유연하게 결정합니다.

## 8. Recommended next state
**KEEP_REFINED_COMPONENTS_AS_CANDIDATES**

이 규칙은 시스템의 법이 아니라 우리의 '운영 감각'입니다. 자연스럽게 상황이 올 때까지 유지합니다.

## 9. Do not do yet
- NO implementation.
- NO automation.
- NO runtime script.
- NO registry, index, or ledger.
- NO formal schema.
- NO official workflow.
- NO current-position update.
- NO baseline promotion.
- NO tool/API/function attachment.
- NO ontology creation.
- NO forced pipeline creation.
- NO integrated engine implementation from this rule alone.
- NO Gemini verified-truth authority.
- NO Codex final authority.

## 10. Final Status
**STATUS: COMPONENT_CHAIN_MODE_SELECTION_RULE_CANDIDATE_COMPLETE**
