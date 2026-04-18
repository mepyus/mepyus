# external_case_first_pass_andrewng_stanford_v1

## 1. 사례 개요
- 사례명: `andrewng_stanford_raw_transcript_v1`
- source_ref: [andrewng_stanford.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/andrewng_stanford.txt)
- source_type: `external_case_primary_transcript`
- source_origin: `raw_talk_or_keynote_transcript`
- source_status: `primary_transcript_with_asr_noise`
- raw transcript로 취급한 이유:
  - 강연형 1차 전사본으로, 구조 프레임과 강한 생산성 주장과 동기 부여 수사가 함께 섞여 있기 때문이다.
  - 그래서 polished summary보다 운영 슬롯이 구조와 주장과 수사를 실제로 분리하는지 확인하는 것이 우선이다.

## 2. 원문에서 실제로 관측한 구조
- AI를 단일 모델이 아니라 `LLM + RAG + agentic workflow + voice + deep learning` 같은 빌딩 블록 조합으로 읽는다.
- 구현 그 자체보다 `무엇을 만들 것인가`와 `의도를 AI가 오해 없이 실행 가능한 명세로 바꾸는 일`이 병목으로 이동했다.
- 코드를 만드는 루프를 `사용자 피드백을 반영하는 제품 관리 루프`로 재정의한다.
- 엔지니어와 PM의 역할 경계가 약해지고, 사용자 공감과 기획 감각을 갖춘 product engineer 쪽이 더 중요해진다고 읽는다.
- 최신 도구를 지속적으로 갈아타는 적응 속도와 정보 네트워크가 실전 우위를 만든다는 감각이 강하다.

## 3. outer로 둔 프레임
- agentic AI building blocks frame
- decision bottleneck / product management shift frame
- product feedback loop as creation frame
- product engineer merge frame
- latest tool adaptation cadence frame

## 4. defer로 보낸 강한 주장
- AI가 해결 가능한 작업 시간이 7개월마다 2배, 코딩은 70일마다 2배라는 강한 성장 주장
- 최신 도구를 3~6개월 놓치면 생산성이 회복 불가능하게 떨어진다는 단정
- 지금이 역사상 유례 없는 골드러쉬라는 강한 시황성 판단
- 특정 커리어 승자/패자를 너무 빠르게 일반화하는 발언

## 5. observer_only로 남긴 수사 / 감상
- 강연자의 이력 소개와 권위 부여 서사
- 네트워크와 캠퍼스 정보 우위에 대한 동기 부여성 표현
- “그냥 가서 뭐라도 만드십시오” 같은 호소형 문장
- 개인적 낙관과 시대적 기회 강조 문장

## 6. core / outer / defer / observer_only 1차 판독 결과

### 후보 1. AI 빌딩 블록을 조합형 agentic workflow로 읽는 프레임
- status: `outer_candidate`
- reason:
  - 생성기 자체보다 workflow와 도구 조합을 더 중요하게 읽는다는 점에서 기존 외부 사례들과 반복된다.
  - 다만 강연 맥락의 도구 예시가 빠르게 변하므로 현재는 코어보다 외곽 비교축이 적절하다.

### 후보 2. 구현보다 제품 결정과 명세화가 새 병목이라는 프레임
- status: `outer_candidate`
- reason:
  - aifrontier와 enterprise에서 반복된 `intent/spec` 축과 강하게 닿는다.
  - 현재 엔진의 문서-실행-피드백 구조와도 간접적으로 맞닿지만 아직 코어 승격보다 외곽 운영 프레임이 안전하다.

### 후보 3. 사용자 피드백을 반영하는 product loop가 개발의 핵심이라는 프레임
- status: `outer_candidate`
- reason:
  - 구현이 싸지고 빨라질수록 피드백과 재설계 루프가 중심이 된다는 읽힘은 재사용 가치가 높다.
  - 다만 강연 서사와 섞여 있어 반복 확인 전까지는 outer 유지가 맞다.

### 후보 4. product engineer merge / PM ratio inversion 프레임
- status: `outer_candidate`
- reason:
  - 역할 경계 재배치에 대한 강한 운영 힌트로 남길 가치가 있다.
  - 하지만 현재는 career/organization reading에 가까워 코어보다 외곽 설명축이 적절하다.

### 후보 5. AI 성장률 / 생산성 / 골드러쉬 관련 강한 주장
- status: `defer`
- reason:
  - 속도, 생산성, 시대 판정은 시점 의존성과 과장 가능성이 크다.
  - 구조 프레임과 분리해 defer 유지가 맞다.

### 후보 6. 강연자의 권위 서사 / 동기 부여 / 네트워크 감상
- status: `observer_only`
- reason:
  - 분위기 이해에는 도움되지만 엔진 규칙이나 코어 승격 후보로 보기엔 이르다.

## 7. 기존 사례와 반복된 구조
- `agentic_workflow_orchestration_frame`
  - saltlux: reasoning + planning + tool use + multi-agent coordination
  - aifrontier: harness, guardrail, agentic tool use, batch/orchestration usability
  - oh_my_opencode: 멀티모델/멀티에이전트 하네스, 병렬 작업, 역할 분담형 실행
  - enterprise: RAG를 도구로 낮추고 agent가 더 넓은 실행을 수행하며 spec/plan/feedback 루프로 일을 조직함
  - andrewng: LLM, RAG, agentic workflow 같은 빌딩 블록 조합으로 일을 조직함
- `intent_to_spec_amplification_frame`
  - aifrontier: 짧은 본질 설명이 spec으로 증폭됨
  - enterprise: tech spec / requirement / plan으로 구체화됨
  - andrewng: 구현보다 의도를 AI가 오해 없이 실행 가능한 명세로 바꾸는 일이 병목으로 읽힘

## 8. 이번 사례에서 새로 뜬 구조
- decision bottleneck / product management shift frame
- product engineer merge frame
- latest tool adaptation cadence frame
- network and information edge as operating advantage frame

## 9. 기존 사례에는 강했지만 이번 사례에서는 약한 프레임
- ontology direct frame
- semantic interoperability / data fabric direct frame
- regulated enterprise control layer frame
- harsh environment reliability frame

## 10. refinement trigger 현재 상태
- status: `refinement_candidate`
- reason:
  - canonical raw/primary 외부 사례가 5건에 도달했고, `agentic workflow`, `intent/spec`, `strong-claim defer` 패턴이 누적되기 시작했다.
  - 그래도 바로 refinement를 열기보다 한 사례 더 확인하거나 정련 패스 후보를 좁히는 편이 안전하다.

## 11. 다음 액션 힌트
- 다음 외부 사례 1건을 더 넣어 반복 축이 유지되는지 본다.
- 아니면 지금까지 나온 `intent/spec/product loop` 축을 정련 후보로 좁힌다.
