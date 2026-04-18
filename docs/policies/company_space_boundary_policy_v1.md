# company_space_boundary_policy_v1

## 1. 목적
이 정책은 새 회사 시나리오에서 회사 raw, 개인 장기 공간, 외부 LLM 전송 가능 범위를 섞지 않기 위한 최소 경계 슬롯을 정의한다.

## 2. 기본 층

### A. company_raw
- 내부 문서 원문
- 업무 메모 원본
- 실제 고객/주문/직원 식별 정보
- 외부 LLM 전송 금지 기본값

### B. company_abstracted
- 민감정보 제거/가명화
- 흐름/병목/문제 구조만 남긴 설명층
- 제한적 외부 사용 가능 후보

### C. private_synthesis
- 개인 판단
- 장기 전략 메모
- 회사 raw 와 섞이지 않도록 provenance 필요

### D. external_llm_safe_subset
- 익명화 완료
- 계약/보안 정책 검토 완료
- 전송 가능 범위 명시

## 3. 코드 공유 경계
- 내부 코드 전체를 외부에 그대로 보내지 않는다.
- 문제 구조를 추상화한 safe subset 부터 만든다.
- 코드 reference asset 에는 boundary level 을 함께 남긴다.

## 4. 필수 슬롯
- `company_namespace`
- `boundary_level`
- `anonymization_status`
- `llm_shareable`
- `reviewed_by`
- `notes`

## 5. 운영 규칙
- 기본값은 deny-first 다.
- raw 를 abstracted 로 옮길 때 익명화 근거를 남긴다.
- private synthesis 는 company raw 를 직접 포함하지 않도록 주의한다.
- 외부 LLM 사용 시 safe subset 여부를 먼저 판정한다.

## 6. 현재 저장소에 필요한 후속 슬롯
- namespace by company/project
- boundary markers on code reference assets
- anonymization checklist placeholder

## 7. 잠금 문장
회사 시나리오에서 가장 위험한 것은 정보 부족이 아니라, 서로 다른 경계층의 자료가 provenance 없이 섞이는 것이다.
