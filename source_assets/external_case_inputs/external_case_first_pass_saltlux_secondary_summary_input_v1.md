[[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]]
[[A]] [[OBJ:external_case_first_pass_secondary_summary]] [[SEM:saltlux_secondary_summary_first_pass]]

# CODEx 입력문 — Saltlux Secondary Summary First Pass v1
# 목적: "솔트룩스 이경일 대표 강연 정리"를 외부 사례 1건으로 투입하여
# exploration observation layer / core promotion checklist / refinement trigger rules가
# 실제로 작동하는지 1차 판독한다.

## 0. 입력 성격 고정
이번 입력은 "원문 transcript"가 아니다.

- case_name: `saltlux_agentic_ai_ontology_secondary_summary_v1`
- source_type: `external_case_secondary_summary`
- source_origin: `youtube_talk_based_secondary_summary_by_claude`
- source_status: `secondary_reconstruction_not_verified_transcript`
- stance: `observe_and_separate_before_adopt`

즉 이 사례는:
- 실제 강연을 바탕으로 한 2차 정리문
- 원문 사실 전체를 바로 채택하는 입력이 아님
- 구조/개념/운영 힌트를 관측하고 분리 판독하는 재료

로 다룬다.

## 1. 이번 턴 목표
이번 턴의 목표는 솔트룩스 내용을 믿거나 반박하는 것이 아니다.

목표는 오직 아래 3개다.
1. exploration observation layer에 실제 기록 1세트를 남긴다
2. 사례 안의 요소들을 core_candidate / outer_candidate / defer / observer_only로 나눈다
3. refinement trigger rules 기준에서 현재 상태를 읽는다

## 2. 입력 본문

### 제목
솔트룩스 이경일 대표 강연 정리
"에이전틱 AI, 온톨로지로 완성되다"

### 본문
1. AI의 역사적 흐름
1943~45년 퍼셉트론 개념 정립과 폰노이만 방식 컴퓨터가 AI의 출발점입니다. 이후 1980년대 로지컬 AI 붐, 머신러닝과 온톨로지 태동, 그리고 두 번의 AI 윈터를 거치며 발전해왔습니다.
현재의 흐름은 세 단계로 정리됩니다.
- 제너레이티브 AI: 트랜스포머 기반, 크게 만들수록 좋은 결과 생성
- 에이전틱 AI (현재): 리즈닝 + 플래닝 + 도구 호출 + 에이전트 간 협력
- 피지컬 AI (미래): 뉴로모픽 칩, 퀀텀 등 완전히 새로운 방식

2. 에이전틱 AI란?
에이전트의 핵심 정의는 "스스로 의사결정을 내리고 행동해 목표에 도달하는 개체" 입니다.
에이전틱 AI 작동 방식은 딥리서치를 예로 들면 다음과 같습니다.
질문 분석 -> 다각도 검색(벡터+키워드+다국어) -> 문서 수집 및 정독 -> 부족한 부분 재질문 -> 답변 구조 플래닝 -> 최종 답변 생성
여러 AI들이 협력하려면 조직과 연결 구조가 필요하고, 이를 위해 MCP와 A2A가 등장했습니다.

3. 온톨로지란?
기원은 아리스토텔레스로, "내 지식을 어떻게 다른 사람에게 정확히 전달할까"라는 고민에서 프리디케이트 로직과 온톨로지 개념이 탄생했습니다.
핵심 구조는 다음과 같습니다.
- 개념(Class) + 관계(Relation) + 속성(Property) + 인스턴스(Instance)
- 공리와 제약 조건을 추가하면 -> 스스로 추론 가능
예: "홍길동은 솔트룩스 직원이고, 직원은 사람이고, 사람은 법적 존재다" 같은 의미적 관계망

4. 왜 지금 온톨로지인가? — 뉴로심볼릭 AI
DARPA는 AI를 세 가지 물결로 설명합니다.
- 1st Wave: 기호적(온톨로지·로직) / 추론 잘함, 학습 못함
- 2nd Wave: 비기호적(딥러닝·LLM) / 학습 잘함, 추론 약함
- 3rd Wave: 뉴로심볼릭(둘의 결합) / 설명 가능한 AI
LLM 단독의 문제점은 벡터 근사 표현의 한계와 확률적 생성 방식으로 인한 할루시네이션이며, 온톨로지 기반 Knowledge Grounding으로 이를 제로로 만든 사례가 있다고 주장합니다.
또한 아무리 뛰어난 지능도 지식을 공유하고 절차를 표현하려면 심볼이 반드시 필요하다고 강조합니다.

5. 구버(Goover)와 루시아(Luxia) — 실제 적용 사례
구버는 LLM + 온톨로지 + 에이전틱 프로세스를 결합한 AI 딥서치 서비스입니다.
- 출시 3개월 만에 누적 사용자 140만 명 달성
- AI가 자동 생성한 리포트·팟캐스트 85만 개
- 월 운영비 2천만 원
- 국가기록원 도입 결정
루시아 3.0은 어댑티브 CoT를 핵심 기능으로 하며, 온톨로지를 생성하고 읽을 수 있는 기능을 내장했다고 설명합니다.

6. 팔란티어 vs 솔트룩스 — 소버린 AI의 필요성
팔란티어의 온톨로지 활용 핵심 목적은 데이터 사일로를 유지하면서도 의미적으로 통합하는 것입니다.
데이터를 한곳에 모으지 않고 필요한 데이터만 온톨로지로 연계하는 데이터 패브릭/매시업 방식입니다.
그러나 팔란티어의 문제점으로 아래를 제시합니다.
- 한국 국방부에 연간 3천억 원 요구
- 온프레미스 LLM 미지원 -> 소버린 AI 구현 불가
이에 대한 대안으로 솔트룩스는 루시아 LLM + 온톨로지 + MCP + 구버 엔터프라이즈 어플라이언스를 제시합니다.

7. 실무 조언 6가지
- 온톨로지는 "추론"이 아닌 semantic interoperability / data fabric 관점으로 접근할 것
- 에이전틱 AI + 온프레미스 파운데이션 모델 결합 필수
- 각 데이터 소스마다 MCP 체계 구성
- 플랫폼보다 문제 정의부터 시작할 것
- 구축 비용보다 총운영비용(TCO) 최적화가 더 중요
- 4개월 단위 소규모 빠른 프로젝트 + 팔란티어 도입 시 내부 섀도 프로젝트 병행

핵심 한 줄 요약:
LLM의 생성 능력과 온톨로지의 추론·지식 표현 능력을 결합한 뉴로심볼릭 AI가 에이전틱 AI 시대의 핵심이며, 이를 자체 기술로 구현하는 것이 소버린 AI의 본질이다.

## 3. observation layer 기록 지시
아래 기준으로 observation 1세트를 남긴다.

### 필수 메타
- exploration_id
- session_id
- run_id
- observed_at
- source_ref = `saltlux_agentic_ai_ontology_secondary_summary_v1`
- source_type = `external_case_secondary_summary`
- source_origin = `youtube_talk_based_secondary_summary_by_claude`

### observation_type
- pattern_seen
- outer_only_reading
- defer_needed
- reusable_translation

### 반드시 남길 항목
- candidate_slots
- kept_as_core_candidate
- kept_as_outer_candidate
- deferred_items
- deferred_reason
- future_use_hint
- next_action_hint
- notes

## 4. 판독 원칙
이번 입력 전체를 한 덩어리 채택하지 말고, 최소 4개 층으로 나눠 본다.

### A. 구조적으로 유효한 요소
우리 엔진에 바로 관측 가치가 있는 운영 원리 / 구조 프레임

### B. 외곽에 두기 좋은 요소
바로 코어로 올릴 단계는 아니지만 반복 참조/설명 프레임으로 유용한 요소

### C. 보류해야 할 요소
강한 수치 주장 / 검증 필요 사실 / 브랜드 중심 비교 / 과잉 일반화 위험 요소

### D. 관측 전용 요소
강연 수사 / 포지셔닝 / 미래 전망 / 당장 엔진 구조에 직접 붙이지 않을 요소

## 5. core promotion checklist 실제 적용 지시
반드시 아래 항목으로 판독 흔적을 남긴다.

- repeat_frequency
- cross_context_reappearance
- cross_session_or_run_presence
- actual_reuse_evidence
- outer_only_sufficiency
- explanatory_axis_role
- premature_generalization_risk

### 판독 대상 후보 예시
- 후보 1:
  `온톨로지를 추론엔진보다 semantic interoperability / data fabric 관점으로 읽는 프레임`
- 후보 2:
  `LLM 단독이 아니라 grounding + symbolic expression layer 결합이 필요하다는 프레임`
- 후보 3:
  `에이전틱 AI = reasoning + planning + tool use + multi-agent coordination 프레임`
- 후보 4:
  `제품 성과 수치 / 할루시네이션 제로 / 소버린 AI 우위 같은 강한 주장들`
- 후보 5:
  `팔란티어 vs 솔트룩스 비교를 통한 시장 포지셔닝 프레임`

## 6. 이번 입력에서 특히 주의할 점
- 강한 주장 분리
- 구조와 마케팅 분리
- 개념과 사례 분리

## 7. refinement trigger 읽기 지시
이번 사례 1건만으로 아래 상태를 읽는다.
- no_trigger
- watch
- refinement_candidate
- refinement_recommended

## 8. 산출물 형식
- `docs/examples/external_case_first_pass_saltlux_secondary_summary_v1.md`
- `runtime/observer/exploration/json/external_case_first_pass_saltlux_secondary_summary_v1.json`
- `runtime/observer/exploration/md/external_case_first_pass_saltlux_secondary_summary_v1.md`
- `runtime/contracts/core_promotion_reading_saltlux_secondary_summary_v1.json`
- `runtime/contracts/refinement_trigger_reading_saltlux_secondary_summary_v1.json`

## 9. 한 줄 요약
이번 입력은 솔트룩스 강연 기반 2차 정리문을
`external_case_secondary_summary`로 취급하여,
구조는 관측하고 주장/수치는 보류하며,
core/outer/defer/observer_only 분리를 실제로 시험하는 1차 판독 턴이다.
