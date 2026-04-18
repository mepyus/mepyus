# external_case_first_pass_saltlux_secondary_summary_v1

## 1. 사례 개요
- 사례명: Saltlux agentic AI ontology secondary summary
- source_ref: `saltlux_agentic_ai_ontology_secondary_summary_v1`
- source_type: `external_case_secondary_summary`
- source_origin: `youtube_talk_based_secondary_summary_by_claude`
- source_status: `secondary_reconstruction_not_verified_transcript`
- secondary summary로 취급한 이유:
  - 원문 transcript가 아니라 강연 기반 2차 정리문이다.
  - 따라서 구조/개념/운영 힌트를 관측하는 재료로 읽고, 사실 주장과 수치는 즉시 채택하지 않는다.

## 2. 이 사례에서 실제로 관측한 것
- 온톨로지를 `semantic interoperability / data fabric` 관점으로 읽는 실무 프레임이 드러난다.
- LLM 단독보다 grounding + symbolic expression layer 결합을 강조한다.
- agentic AI를 reasoning + planning + tool use + multi-agent coordination 흐름으로 묘사한다.
- 제품 성과 수치, 할루시네이션 제로, 소버린 AI 우위 같은 강한 주장도 함께 섞여 있다.
- 구조 프레임, 시장 포지셔닝, 실무 조언이 한 문서 안에 같이 들어 있어 분리 판독이 필요하다.

## 3. 우리 엔진 기준으로 바로 유효한 요소
- 구조/마케팅/사실 주장을 분리해서 읽어야 한다는 점
- 온톨로지를 추론엔진 자체보다 상호운용/연결 프레임으로 보는 관점
- LLM 단독이 아니라 grounding과 symbolic layer 결합 필요성을 “구조 힌트”로 관측하는 방식
- agentic AI를 구성 요소 묶음으로 읽는 설명 프레임

## 4. 아직 보류할 요소
- 할루시네이션 제로 주장
- 사용자 수 / 운영비 / 도입 규모 수치
- 특정 경쟁사 우위/열위 단정
- 소버린 AI 가능/불가의 강한 결론
- 브랜드 중심 시장 포지셔닝 결론

## 5. core / outer / defer / observer_only 1차 판독

### 후보 1. 온톨로지를 semantic interoperability / data fabric 관점으로 읽는 프레임
- status: `outer_candidate`
- reason:
  - 우리 엔진의 연결/재배치/분리 읽기와 닿는 설명 프레임이다.
  - 하지만 아직 코어 축으로 잠그기보다 외부 사례 비교축과 설계 설명축으로 반복 검증하는 편이 안전하다.

### 후보 2. grounding + symbolic expression layer 결합 필요 프레임
- status: `outer_candidate`
- reason:
  - LLM 단독 한계와 구조적 보강 필요성은 우리 문서와 닿는다.
  - 다만 secondary summary 기반이라 강한 채택보다 외곽 참조 프레임으로 두는 것이 맞다.

### 후보 3. agentic AI = reasoning + planning + tool use + multi-agent coordination 프레임
- status: `outer_candidate`
- reason:
  - 설명 프레임으로는 유효하지만 현재 우리 엔진 코어에 바로 넣을 독립 축으로 보기엔 아직 이르다.
  - guide/report/observation에서 반복 재사용하며 검증하는 편이 적절하다.

### 후보 4. 제품 성과 수치 / 할루시네이션 제로 / 소버린 AI 우위 주장
- status: `defer`
- reason:
  - 강한 사실 주장과 마케팅성 결론이 섞여 있다.
  - secondary summary 전제상 검증 없이 채택하면 위험하다.

### 후보 5. 팔란티어 vs 솔트룩스 비교를 통한 시장 포지셔닝 프레임
- status: `observer_only`
- reason:
  - 현재는 시장 포지셔닝 읽기와 비교 맥락 참고용으로만 충분하다.
  - 코어 승격 판단 대상이라기보다 외곽 관찰 재료다.

## 6. refinement trigger 관점 현재 상태
- status: `watch`
- reason:
  - 외부 사례 5건 누적 상태는 아니므로 `external_case_accumulated_ge_5`는 아직 아니다.
  - 하지만 relation slot과 구조/분리/보류 패턴이 여러 사례 문서에서 반복되기 시작했다.
  - 지금 바로 refinement를 열 정도는 아니지만 다음 1~2건 누적 후 repeated pattern을 다시 보는 것이 적절하다.

## 7. 다음 액션 힌트
- 다른 외부 사례 1~2건을 더 넣어 `outer_candidate`로 남긴 구조 프레임이 실제로 반복되는지 본다.
- 그다음 `semantic interoperability/data fabric`, `grounding+symbolic layer`, `agentic 구성 프레임` 중 무엇이 계속 살아남는지 정련 패스로 재판독한다.
