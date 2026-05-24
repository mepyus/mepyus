# Relation-first Light Compression Rule v0

## 1. Status
**STATUS: RELATION_FIRST_LIGHT_COMPRESSION_RULE_CANDIDATE_COMPLETE**

## 2. Executive summary
이 압축 규칙은 Relation-first 입력기의 구조를 유지하되, 모든 작업에 동일한 강도의 패킷 작성을 강제하지 않기 위한 **'운영 조절 장치'**입니다. 자료의 복잡도와 위험도에 따라 Compact, Standard, Heavy 모드로 나누어 불필요한 의식(Ceremony)을 줄이고 실질적인 맥락 보존과 연결성에 집중합니다.

## 3. Mode Classification Table

| Component | Compact | Standard | Heavy | Note |
| :--- | :---: | :---: | :---: | :--- |
| **Source Bundle** | Yes | Yes | Yes | 원본 흐름 보존 |
| **Source-level Reading** | Yes | Yes | Yes | 최소 문맥 유지 |
| **Meaning Block** | - | Yes | Yes | 거시적 단위 |
| **Relation Map** | - | - | Yes | 구조적 관계 |
| **Evidence / Provenance Label**| Yes | Yes | Yes | 증거 신분 확인 |
| **Placement** | Yes | Yes | Yes | 현재 인지 상태 |
| **Line / Axis Pressure** | - | Yes | Yes | 구조적 긴장 확인 |
| **Selective Segmentation** | - | - | Yes | 깊은 분절 필요 시 |
| **Input Report Card** | Yes | Yes | Yes | 판단 요약 |
| **Re-entry Signal** | Yes | Yes | Yes | 세션 연결성 |
| **Watch / Hold** | Yes | Yes | Yes | 안전 보류 |
| **User Gate** | Yes | Yes | Yes | 최종 판단 |

## 4. Mode Selection Definitions

### 4.1 Compact Mode
- **Use when:** 1회성 확인, 저위험 입력, 빠른 정렬.
- **Goal:** 최소한의 맥락 보존 및 판단 기록.
- **Fields:** Source Identity, User Intent, Placement, Next Action, Re-entry Signal.

### 4.2 Standard Mode
- **Use when:** 재사용 가능성이 있는 외부 자료, 기존 라인과의 연결성 검토 필요 시.
- **Goal:** 원본 맥락 보존 및 구조적 연결 확인.
- **Fields:** Compact + Meaning Block, Evidence Label, Linkage Status.

### 4.3 Heavy Mode
- **Use when:** 도구/API 도입, 워크플로우 변경, 고위험 판단이 필요한 경우.
- **Goal:** 전체 구조적 압력 분석 및 잠재적 리스크 심층 검토.
- **Fields:** All fields + Drift Analysis, Old/New comparison.

## 5. Key Design Principles
1. **Compact에서 경계를 생략하지 않음:** 정보의 양은 줄여도, `do-not-infer`나 `User Gate` 같은 안전 경계는 1줄로라도 남겨야 합니다.
2. **증거 추적의 미니멀화:** `Evidence trace`는 필수로 남기되, Compact 모드에서는 (Source, Key Judgment, Next Action) 형태의 미니 추적으로 압축합니다.
3. **Hook의 수동성:** 훅(Hook)은 자동 블로커가 아니라 '판단을 위한 수동 정지 신호'로 사용합니다.
4. **Invocation Context:** 스킬은 로더를 만들지 말고, 어떤 맥락에서 수동으로 꺼내 쓸지(Invocation Context)를 기록하여 사용합니다.

## 6. Structural problem list

| Problem | Severity | Why it matters | Suggested handling | Do not do |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ceremony Drift** | MEDIUM | 모든 작업을 풀버전으로 작성함 | 모드별 필드 차등 적용 | 무조건 Standard/Heavy 작성 |
| **Authority Drift** | HIGH | 워커의 해석이 사실로 굳어짐 | User Gate 강화 | Gemini 증거를 Truth로 승격 |
| **Registry Drift** | HIGH | 후보들이 온톨로지로 고착됨 | '후보' 상태 보존 | 레지스트리 생성 |

## 7. Recommended next state
**KEEP_AS_RELATION_FIRST_LIGHT_COMPRESSION_RULE_CANDIDATE_WITH_WATCH**

## 8. Watch items
*   소프트웨어적 도구(Graphify/Karpathy)가 곧바로 우리 공간의 아키텍처가 되는 압박.
*   연결 확인(Linkage)이 자동화된 라우터로 변질되는 것.
*   User 게이트가 실질적인 판단 없이 '통과 의식'으로 전락하는 것.
*   모드별 필드 정의가 다시 고정된 스키마로 굳어지는 것.

## 9. Do not do yet
- NO implementation, automation, or runtime script creation.
- NO registry, index, ledger, router, controller.
- NO formal schema or official workflow.
- NO current-position update or baseline promotion.
- NO tool/API/function attachment.
- NO ontology creation.
- NO forced pipeline creation.
- NO integrated engine implementation from this rule alone.
- NO Gemini verified-truth authority.
- NO Codex final authority.
