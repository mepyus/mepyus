# Processor Standard v1

목적:
- 동일 원문 입력(source document)을 여러 처리자(Codex, ChatGPT, Gemini)가 같은 기준으로 읽게 한다.
- 결과 차이를 비교하여 입력기/라벨기/앵커기 조정 데이터를 축적한다.
- 정답 판정이 아니라 차이 축적이 목적이다.
- 원문 보존, 애매함 보존, 근거 보존을 우선한다.

이 문서는 `app/work/processor_compare` 비교 파이프라인에서 raw 출력 검증과 normalize/compare의 기준 문서로 사용한다.

## 0. 공통 작업 원칙

- Replica core 로직은 수정하지 않는다.
- raw 출력은 절대 덮어쓰지 않는다.
- normalized와 reports는 raw와 별도 경로에 저장한다.
- 비교 목적은 최고 처리자 선정이 아니라 차이 누적이다.
- 자유 에세이보다 구조화 출력과 비교 가능성을 우선한다.
- ambiguity와 provisional 상태는 제거하지 않는다.

## 1. 처리자 공통 역할 정의

처리자의 역할은 "정답 생성기"가 아니라 아래 3가지를 수행하는 관측기다.

1. 입력 원문을 비교 가능한 fragment들로 자른다.
2. 각 fragment에서 anchor 후보를 잡는다.
3. 동일 schema에 따라 처리값을 산출한다.
4. 짧은 근거를 남긴다.

중요:
- 입력에 없는 내용을 사실처럼 추가하지 말 것
- 애매하면 ambiguity를 높이고 why_short에 짧게 남길 것
- 자유 에세이 금지
- 반드시 지정된 JSON 필드만 출력할 것
- 필드명 변경 금지
- 값이 불충분하면 null 대신 빈 배열, 0~1 점수, 또는 `unknown`을 사용

## 2. 입력 단위 기준

입력 단위 이름: `fragment`

처리자는 먼저 공통 원문(source document)을 읽고, 그 안에서 fragment를 스스로 절단한다.
fragment는 다음 중 하나에 해당하는 비교 가능한 로컬 의미 묶음이다.
- 한 주장 묶음
- 한 설명 묶음
- 한 장면 묶음
- 한 비교 묶음
- 한 문제제기 묶음
- 한 전환 묶음

좋은 fragment 조건:
- 내부에 로컬 의미가 살아 있다
- 하나의 중심 움직임이 있다
- 다른 처리자와 비교 가능하다
- 짧은 근거 구절을 내부에서 뽑을 수 있다
- 과도하게 길지 않다

나쁜 fragment 조건:
- 문장 하나만 남아 의미가 약하다
- 서로 다른 주축 2~3개가 강하게 섞여 있다
- 길어서 하나의 비교 단위로 보기 어렵다
- 지나치게 요약되어 원문 복귀 가치가 없다

입력 메타 필드:
- input_doc_id
- input_bundle_id
- fragment_id
- fragment_text
- source_type
- fragment_version

절단 원칙:
- 문장 개수로 자르지 말고 하나의 로컬 의미 움직임으로 자를 것
- 지나치게 큰 fragment로 여러 주축을 섞지 말 것
- 지나치게 작은 fragment로 의미를 잃지 말 것
- 각 처리자는 자기 기준대로 자를 수 있지만, 원문 바깥 내용을 추가해서는 안 된다

fragment_id 원칙:
- fragment_id는 처리자 내부에서 고유하면 된다
- 여러 처리자 간 fragment_id가 일치할 필요는 없다
- 비교기는 후매칭으로 유사 fragment를 다시 맞춘다

## 3. Anchor 기준

anchor는 fragment가 나중에 다른 fragment와 다시 만날 수 있도록 붙는 정규화된 손잡이다.

anchor 구성:
- anchor_id: 정규화 id
- anchor_label: 읽기 쉬운 이름
- anchor_type: `semantic | structural | object | process`
- anchor_scope: `local | cross_source | provisional`

anchor 선택 원칙:
- 의미 축이 반복될 가능성이 있으면 `semantic`
- 구조, 역할, 연결 방식이면 `structural`
- 사물, 대상, 개체면 `object`
- 동작, 절차, 변환이면 `process`

추가 원칙:
- fragment당 핵심 anchor 1~3개 권장
- 반복 가능성이 있는 것만 anchor로 승격
- 일회성 장식 표현은 anchor로 만들지 말 것
- 애매하면 `provisional` 허용
- 문장 그대로 복붙하지 말고 정규화된 손잡이로 만들 것

## 4. 출력 Schema

출력은 반드시 JSON 객체 하나만 반환한다.
추가 설명 금지.
마크다운 금지.
코드펜스 금지.
필드 순서 고정.

필수 필드:
1. input_doc_id
2. input_bundle_id
3. fragment_id
4. fragment_text
5. source_type
6. fragment_version
7. anchors
8. direction
9. intensity
10. stability
11. scene
12. role
13. semantic_tags
14. structural_tags
15. confidence
16. ambiguity
17. evidence_text
18. why_short
19. processor_notes

anchors 배열 각 원소 필드:
- anchor_id
- anchor_label
- anchor_type
- anchor_scope

제약:
- direction, intensity, stability, confidence, ambiguity 는 `0.0 ~ 1.0` float
- scene, role 는 아래 지정 enum만 허용
- semantic_tags, structural_tags, evidence_text, processor_notes 는 배열
- processor_notes 는 최대 2개
- semantic_tags 와 structural_tags 는 최대 5개
- why_short 는 1문장
- 자유 장문 설명 금지

## 5. 수치값 정의

수치값:
- direction: 어떤 축으로 밀고 가는 힘이 얼마나 분명한가
- intensity: 표현과 주장의 밀도, 응집 압력이 얼마나 강한가
- stability: fragment 내부 의미가 한 방향으로 얼마나 유지되는가
- confidence: 처리자가 자기 판단에 대해 얼마나 자신 있는가
- ambiguity: 해석 여지가 얼마나 큰가

판정 가이드:

### direction
- 0.0 ~ 0.2: 방향 거의 없음
- 0.3 ~ 0.5: 약한 방향
- 0.6 ~ 0.8: 분명한 방향
- 0.9 ~ 1.0: 매우 강한 단일 방향

### intensity
- 0.0 ~ 0.2: 힘이 약함
- 0.3 ~ 0.5: 보통
- 0.6 ~ 0.8: 강함
- 0.9 ~ 1.0: 매우 응축됨

### stability
- 0.0 ~ 0.2: 내부가 흔들림
- 0.3 ~ 0.5: 혼합됨
- 0.6 ~ 0.8: 안정적
- 0.9 ~ 1.0: 매우 안정적

### confidence
- 근거가 직접적이고 명확할수록 높임
- 해석이 많이 섞이면 낮춤

### ambiguity
- 복수 해석 가능성이 크면 높임
- 명확한 정의, 지시, 진술이면 낮춤

주의:
- confidence와 ambiguity는 반비례 경향이 있지만 항상 정확히 반대일 필요는 없다.

## 6. 범주값 정의

scene 허용값:
- discovery
- explanation
- comparison
- evidence
- question
- reflection
- instruction
- transition
- unknown

role 허용값:
- thesis
- support
- bridge
- example
- contrast
- definition
- expansion
- problem
- meta
- unknown

## 7. 태그값 정의

semantic_tags:
- "무엇을 말하는가"를 기록하는 짧은 의미 태그 배열

structural_tags:
- "어떻게 작동하는가 / 어떤 위치를 차지하는가"를 기록하는 짧은 구조 태그 배열

원칙:
- 짧고 반복 가능해야 한다
- 자유로운 긴 문장형 태그 금지
- lower_snake_case 권장

semantic_tags 예:
- space
- anchor
- discovery
- comparison
- projection
- memory
- bias
- learning
- process
- review

structural_tags 예:
- center_candidate
- bridge
- branch
- repeat_axis
- outer_drift
- convergence
- split_point
- support_line
- provisional
- isolated

## 8. 근거값 정의

evidence_text:
- fragment 내부의 짧은 근거 구절 배열
- 최소 1개 이상 권장

why_short:
- 1문장 이유 설명
- 비교 설명용 참고값

processor_notes:
- 최대 2개 짧은 문자열
- 독특한 해석, provisional 판단, 보수적 메모만 남길 것

## 9. 차이 축적 목적에 맞는 판정 원칙

- 애매한 fragment를 억지로 하나로 고정하지 말 것
- 독특한 해석은 버리지 말고 processor_notes에 짧게 남길 것
- 확신이 낮으면 confidence를 낮추고 ambiguity를 올릴 것
- 근거 없는 과잉 해석 금지
- 입력기와 라벨기 조정에 도움이 되도록 why_short를 짧게 남길 것

## 10. 처리자별 추가 주의사항

### ChatGPT
- 의미 확장을 과하게 하지 말 것
- fragment 바깥 맥락 추정 최소화
- evidence_text는 반드시 fragment 내부에서 뽑을 것

### Gemini
- 비유, 연결 상상으로 anchor를 과증식하지 말 것
- anchor 1~3개 원칙 유지
- processor_notes는 짧고 보수적으로 둘 것

### Codex
- 코드, 구조적 해석으로만 치우치지 말 것
- 비구조 의미도 semantic_tags로 보존할 것
- 필드 누락 금지

## 11. 표준 출력 예시

```json
{
  "input_doc_id": "doc_001",
  "input_bundle_id": "bundle_A",
  "fragment_id": "frag_014",
  "fragment_text": "서로 다른 자료를 공간에 배치해 숨은 연결을 본다.",
  "source_type": "chat",
  "fragment_version": "v1",
  "anchors": [
    {
      "anchor_id": "anc_space_discovery",
      "anchor_label": "space_discovery",
      "anchor_type": "semantic",
      "anchor_scope": "cross_source"
    },
    {
      "anchor_id": "anc_connection_search",
      "anchor_label": "connection_search",
      "anchor_type": "process",
      "anchor_scope": "local"
    }
  ],
  "direction": 0.72,
  "intensity": 0.64,
  "stability": 0.58,
  "scene": "discovery",
  "role": "thesis",
  "semantic_tags": ["space", "discovery", "connection"],
  "structural_tags": ["center_candidate", "bridge"],
  "confidence": 0.69,
  "ambiguity": 0.34,
  "evidence_text": ["공간에 배치해", "숨은 연결을 본다"],
  "why_short": "공간을 발견 장치로 규정하며 연결 탐색을 중심 기능으로 둔다.",
  "processor_notes": ["발견 중심 해석", "비교 가능성 높음"]
}
```

## 12. 최종 운영 원칙

이 schema의 목적은 완벽한 의미 판정이 아니다.
목적은 동일 입력에 대한 처리자별 차이를 누적하여 입력기, 라벨기, 앵커기를 정교화하는 것이다.
그러므로 일관성, 근거, 짧은 설명, 동일 필드명이 최우선이다.
