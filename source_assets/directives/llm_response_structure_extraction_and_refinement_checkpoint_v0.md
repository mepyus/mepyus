[[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]]
[[A]] [[OBJ:llm_response_structure_extraction]] [[SEM:engine_distillation]]

# LLM 답변 구조 추출 기준문 v0
## 목적
이 문서는 LLM 자체를 엔진에 넣는 것이 아니라,
LLM 답변에서 반복적으로 드러나는 판단 구조 / 의미 전개 / 관계 판독 방식을
내 엔진의 값과 기록 형식으로 증류(distill) 하기 위한 기준문이다.

핵심은 단순하다.

- 나는 LLM의 거대한 내부 엔진을 갖고 싶지 않다.
- 나는 LLM의 답변에서 드러나는 생각의 구조를 내 엔진 언어로 뽑아내고 싶다.
- LLM은 외부 보조자다.
- 내 엔진은 느리고 무거워도 내 구조화를 견디며 축적되어야 한다.
- 따라서 관심사는 "좋은 답변"이 아니라 좋은 답변을 만드는 구조를 값과 기록으로 남길 수 있는가이다.

## 1. 최상위 선언

### 선언 1
내가 원하는 것은 LLM을 엔진에 담는 것이 아니라,
LLM 답변 구조를 엔진이 견딜 수 있는 값과 기록으로 증류하는 것이다.

### 선언 2
LLM은 내 엔진의 주 판단자나 기억 저장소가 아니다.
LLM은 외부에서
- 비교하고
- 검색하고
- 보조 설명을 만들고
- 부족한 맥락을 채운 뒤
다시 공간으로 되돌려주는 보조자다.

### 선언 3
내 엔진은 똑똑하지 않아도 된다.
대신
- 느리더라도 버텨야 하고
- 구조를 유지해야 하고
- 기록을 남겨야 하고
- 다시 회수할 수 있어야 하고
- 반복적으로 증류된 판단 구조를 축적할 수 있어야 한다.

### 선언 4
따라서 지금 필요한 것은
새 부품 설계보다 먼저
LLM 답변에서 반복되는 판단 슬롯을 채굴하는 작업이다.

## 2. 내가 추출하려는 것은 무엇인가
나는 LLM 답변의 문장 자체를 가져오려는 것이 아니다.
나는 답변에서 반복적으로 나타나는 구조적 슬롯을 가져오려는 것이다.

즉 관심 대상은:
- 무엇을 먼저 규정하는가
- 어떤 순서로 판단하는가
- 어떤 종류의 관계를 읽는가
- 왜 그렇게 읽었다고 말하는가
- 어디까지 허용하고 어디서 경계를 긋는가
- 다음 행동을 어떻게 제안하는가

같은 판단의 뼈대다.

## 3. LLM 답변에서 반복적으로 채굴할 판단 슬롯

### 3-1. 대상 규정 슬롯
- `focus_object`
- `input_type`
- `material_role`
- `scope_note`

### 3-2. 현재 상태 판정 슬롯
- `current_reading`
- `maturity_state`
- `priority_note`
- `overreach_risk`

### 3-3. 관계 판독 슬롯
- `relation_kind`
- `same_meaning_hint`
- `same_context_hint`
- `different_flow_hint`
- `structure_borrowable`
- `weak_link_note`
- `hold_reason`
- `separated_reason`

### 3-4. 이유 서술 슬롯
- `relation_reason`
- `borrow_reason`
- `not_adopted_reason`
- `boundary_reason`
- `evidence_trace_hint`

### 3-5. 사용 가능성 슬롯
- `future_use_hint`
- `applicable_layer`
- `possible_feature_seed`
- `prompt_material_hint`
- `engine_refinement_hint`

### 3-6. 경계 설정 슬롯
- `boundary_note`
- `do_not_adopt`
- `do_not_lock`
- `observer_limit`

### 3-7. 다음 단계 슬롯
- `next_action_hint`
- `attachment_strategy`
- `defer_note`
- `bounded_next_step`

### 3-8. 사용자 언어 번역 슬롯
- `user_language_summary`
- `plain_readout`
- `interpretation_note`

## 4. 현재 엔진에 우선 붙여볼 수 있는 값 후보
- `focus_object`
- `input_type`
- `material_role`
- `current_reading`
- `relation_kind`
- `relation_reason`
- `same_meaning_hint`
- `same_context_hint`
- `different_flow_hint`
- `structure_borrowable`
- `not_adopted_reason`
- `boundary_note`
- `future_use_hint`
- `next_action_hint`
- `uncertainty_or_hold`
- `user_language_summary`

## 5. 현재 엔진에서 먼저 탐색해야 할 질문
- 위 슬롯 중 무엇이 현재 엔진의 값 / 라벨 / 앵커 / 문서 / observer log / pointer/evidence/provenance 구조로 이미 흡수 가능한가
- 무엇은 sidecar / runtime observation artifact / exploration note / 보고서 문서 형태로는 붙일 수 있는가
- 무엇은 지금은 절대 코어에 넣지 말아야 하는가
- 사용자 언어 번역 슬롯은 기존 선언문/기준문/지시서 어디에서 이미 반쯤 구현되어 있는가
- LLM 답변 구조와 사용자가 만든 표준 문서 구조가 어떤 슬롯에서 겹치고 어떤 슬롯에서 다르게 나타나는가

## 6. 선언문 / 기준문 / 지시서에서 이미 추출 가능한 구조

### 선언문
- `why_this_exists`
- `top_direction`
- `what_to_protect`
- `what_not_to_become`
- `value_axis`
- `future_use_orientation`

### 기준문
- `current_state_reading`
- `allowed_vs_forbidden`
- `relation_rule`
- `operation_principle`
- `boundary_note`
- `lock_level`

### 지시서
- `purpose`
- `scope`
- `review_questions`
- `expected_outputs`
- `forbidden_actions`
- `success_condition`
- `next_action_hint`

## 7. LLM의 올바른 역할
LLM은 엔진 안의 중심 지능이 아니다.

### LLM이 할 일
- 공간 탐색 결과의 빈칸 보강
- 부족한 비교축 제안
- 외부 기술 검색 / 요약 / 비교
- 관계 이유 서술 보강
- 사용자 언어 요약
- 표준 문서 초안 생성
- 관찰면 설명문 생성

### LLM이 하면 안 되는 일
- 엔진 코어 대체
- 공간의 주 판단자
- 기억 저장소 자체
- 구조의 최종 소유자
- relation_kind 최종 잠금자
- 코어 의미 체계의 독점 판사

## 8. 현재 추천 접근
1. 내 답변에서 반복되는 판단 슬롯을 모은다.
2. 사용자가 작성한 선언문/기준문/지시서에서 반복되는 슬롯을 모은다.
3. 두 집합의 겹침 / 차이 / 공백을 정리한다.
4. 현재 엔진의 값/라벨/앵커/문서/observer 구조 중 어디에 어떤 슬롯을 우선 붙일 수 있는지 본다.
5. 코어 변경 없이 붙일 수 없는 것은 sidecar / runtime artifact / exploration note로 먼저 붙인다.

## 9. 초기 산출물 권장 형식
- 답변 구조 슬롯 목록
- 표준 문서 구조 매핑표
- 엔진 부착 가능성 표

## 10. 현재 잠금
1. 나는 LLM 자체를 엔진에 넣고 싶은 것이 아니다.
2. 나는 LLM 답변에서 반복되는 판단 구조를 증류하고 싶다.
3. 증류 대상은 문장 표면이 아니라 판단 슬롯이다.
4. 선언문/기준문/지시서에도 같은 구조가 이미 녹아 있다.
5. 새 부품 설계보다 먼저 현재 엔진에서 흡수 가능한 슬롯을 탐색해야 한다.
6. 코어가 느리고 무거워도 괜찮다. 구조를 견디고 기록을 남길 수 있으면 된다.
7. LLM은 외부 보조자이며, 공간의 중심은 항상 내 엔진이다.

## 11. 최종 한 줄
나는 LLM을 엔진에 담고 싶은 것이 아니라, LLM 답변에서 반복적으로 드러나는 판단 구조·의미 전개·관계 판독 방식을 추출해 내 엔진의 값과 기록 형식으로 증류하고 싶다. 내 엔진은 느리고 무거워도 그 구조화를 견디며 성장해야 하고, LLM은 그 구조를 보강해 다시 공간으로 재료를 넣는 외부 보조자여야 한다.

---

[[A]] [[OBJ:refinement_checkpoint_declaration]] [[SEM:periodic_clarification_and_core_compaction]]

# 선언문
## 엔진 옆의 참조 점검기와 주기적 정련에 대한 선언

나는 엔진을 무한히 크게 만들고 싶은 것이 아니다.
나는 의미와 맥락과 과정과 기억을 풍부하게 담아낼 수 있는 공간을 만들고 싶지만,
그 풍부함이 매번 코어를 비대하게 만들기를 원하지는 않는다.

## 1. 확장과 정련은 함께 가야 한다
내 공간은 새로운 재료, 기술, 문서, 연결, 관계 판독이 들어오며 풍부해질 수 있다.
그러나 풍부해진다는 것은 코어가 계속 비대해진다는 뜻이 아니다.

나는
- 확장 패스
- 정련 패스

를 분리해서 본다.

즉 내 엔진은 풍부하게 자라되, 주기적으로 다시 또렷해져야 한다.

## 2. 선언문/기준문/지시서는 코어를 대신하는 것이 아니라 참조 점검기다
이 문서들은 엔진 옆에 두는 참조 점검기다.

이 점검기의 역할은:
- 현재 엔진이 어디까지 벗어났는지 확인
- 무엇이 코어에 남아야 하는지 다시 판독
- 무엇이 외곽층으로 빠져야 하는지 확인
- 무엇이 아직 가능성으로만 남아야 하는지 확인
- 의미는 살리고 구조는 단단하게 재정렬

## 3. 참조 점검기는 상시 통제 장치가 아니라 주기적 정련 장치다
- 평소에는 공간이 자라도록 둔다
- 기록과 기억은 계속 쌓는다
- 일정 시점마다 참조 점검기를 흘려보낸다
- 그때 무엇이 또렷해졌고 무엇이 과해졌는지 점검한다
- 코어와 외곽층을 다시 나눈다

## 4. 선언문도 구조를 또렷하게 하는 정련 재료다
- 백과사전은 의미를 또렷하게 한다
- 선언문은 구조를 또렷하게 한다
- 기준문은 경계를 또렷하게 한다
- 지시서는 다음 행동을 또렷하게 한다

## 5. 정련 패스의 핵심 목적
1. 코어를 다시 작게 만든다
2. 외곽층으로 빼야 할 것을 분리한다
3. 계속 남겨야 할 기록 축을 확인한다
4. 해석은 풍부하게 유지하되 구조는 가볍게 만든다
5. 반복해서 등장하는 판단 구조만 남긴다
6. 일시적 흥분이나 과한 확장은 외곽으로 밀어낸다

## 6. 코어에 남아야 하는 것과 외곽으로 빠져야 하는 것

### 코어에 남아야 하는 것
- 값
- 라벨
- 앵커
- 기본 관계 축
- 기록의 버팀 구조
- session / run / pointer 같은 회수 구조
- 반복해서 살아남는 최소 판단 슬롯

### 외곽으로 빠져야 하는 것
- 긴 해석 문장
- 풍부한 비교 설명
- 외부 기술 사례 상세 분석
- 사용자 언어 브리핑 전체
- 후구조화 보강 기록의 상세본
- observer readout의 장문 결과
- 참조 재료를 통한 의미 강화 상세 로그

## 7. 정련 패스는 삭제가 아니라 재배치다
정련은 삭제가 아니라 재배치에 의한 경량화다.

## 8. 정기 점검에서 물어야 할 질문
- 최근 쌓인 것 중 무엇이 코어에 남을 만큼 반복되었는가
- 무엇은 아직 가능성은 있지만 코어에 넣기엔 이른가
- 무엇은 외곽 observation layer로 빼는 것이 맞는가
- 무엇은 선언문/기준문과 충돌하는가
- 무엇은 실제로 계속 쓰이고 무엇은 일회성 흥분이었는가
- 무엇이 구조를 또렷하게 하고 무엇이 구조를 흐리게 하는가
- 이번 정련 후 코어는 더 작아졌는가, 아니면 설명만 늘었는가

## 9. 내가 원하는 엔진의 성장 방식
상시 강통제가 아니라
축적 -> 참조 점검 -> 정련 -> 재배치
다.

## 10. 최종 선언
평소에는 공간이 자라게 두고,
기록과 기억과 연결을 축적하게 두며,
정기적으로 이 점검기를 흘려보내
구조를 다시 또렷하게 만들고
코어를 다시 작고 단단하게 정련한다.

즉 내 엔진은
풍부하게 자라되, 주기적 정련을 통해
해석은 외곽에서 풍부하게 유지하고
코어는 계속 작고 단단하게 남는 엔진이어야 한다.
