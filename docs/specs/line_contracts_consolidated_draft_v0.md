# Line Contracts Consolidated Draft v0

## 목적

이 문서는 라인을 감각적 표현이나 철학적 설명에만 두지 않고, 통합엔진 내부에서 여러 기관이 공통으로 읽고 다룰 수 있는 중간 운용 객체 후보로 다루기 위한 기준 초안이다.

이 문서는 최종 DB 스키마나 실행 규칙이 아니다. 현재 목적은 다음을 얇게 잠그는 것이다.

- 라인의 개념 위상
- 라인의 비정의
- 라인의 핵심 성질과 생애주기
- 통합엔진 각 기관과의 관계
- Line Object Contract v0
- current_stage / maturity_level 전이 기준

---

## 1. 라인 공식 기준문

### 최상위 잠금 문장

라인은 통합엔진 내부에서 원재료와 최종 개념 사이를 매개하며, 여러 단서·관계·공백·압력을 묶어 다음 해석·판단·작업·검증·환류를 유발하는 지속 가능한 중간 운용 형성체다.

### 철학 잠금 문장

라인은 거꾸로 된 온톨로지에서 개념이 위로 떠오르기 전, 여러 재료와 관계와 공백을 묶어 그 상승을 실제로 밀어주는 중간 의미 형성체다.

### 엔진 잠금 문장

라인은 통합엔진의 각 기관이 서로 다른 국면에서 읽고 다루고 보호하고 올리고 다시 부를 수 있는 공통 중심물이다.

### 비정의 잠금 문장

라인은 문장도, chunk도, 문서도, 티켓도, 위키 페이지도, 처음부터 고정된 객체도 아니다.

### 운용 잠금 문장

라인은 의미를 담아두는 저장 단위가 아니라, 다음 처리와 개념 형성을 유도하는 운용 단위다.

### 생애주기 잠금 문장

라인은 신호에서 시작해 포착·형성·명료화·분기·검증·환류를 거치며, 일부는 승격되고 일부는 잔류한다.

### 승격 잠금 문장

라인은 페이지가 되기 전 단계가 아니라, 개념체·페이지·작업 패킷·검증 자산 등 여러 상위 표면으로 분화 가능한 전구체다.

---

## 2. 라인의 핵심 성질

- 중간성: raw도 final도 아닌 사이에 있으며, 그 사이를 매개한다.
- 유발성: 재독해, 비교, 번역, relay, 검증, hold, 환류, 승격 후보화를 유발한다.
- 관계성: 라인은 반드시 무엇과 무엇을 잇는다.
- 공백성: 라인은 연결만이 아니라 공백, 긴장, unresolved 상태도 품는다.
- 방향성: 라인은 다음 어디로 가야 하는지를 어느 정도 품고 있어야 한다.
- 지속성: 라인은 다시 불러질 수 있어야 하고, 새로운 자료와 만나 더 두꺼워질 수 있어야 한다.
- 승격 가능성: 충분히 성숙하면 개념체, 페이지, 작업 패킷, 검증 자산, watchpoint, 운영 규칙 후보 등으로 올라갈 수 있다.

---

## 3. 라인의 최소 존재 조건

어떤 것을 라인이라 부르기 위해 최소한 아래 요소가 필요하다.

- 앵커: 어디에 닿아 있는가
- 압력: 왜 지금 중요해졌는가
- 관계: 무엇과 무엇을 잇는가
- 공백 또는 긴장: 무엇이 아직 비어 있는가
- 방향: 다음 어디로 흘러갈 수 있는가
- 지속 가능성: 다시 호출될 수 있는가
- 승격 잠재성: 나중에 더 높은 표면으로 올라갈 수 있는가

---

## 4. Line Object Contract v0

### 계약 한 줄 정의

Line Object는 원재료와 최종 개념 사이에서 여러 단서·관계·공백·압력을 묶어 다음 해석·판단·작업·검증·환류를 유발하는 지속 가능한 중간 운용 형성체를 구조적으로 담기 위한 계약 객체다.

### 이 계약이 다루는 것

- 이 line이 무엇에 닿아 있는가
- 왜 지금 살아났는가
- 무엇과 무엇을 잇는가
- 어디가 비어 있는가
- 지금 어느 단계인가
- 다음 어디로 갈 가능성이 있는가
- 나중에 무엇으로 승격될 수 있는가
- 어떤 약함/보류/미결 상태를 품고 있는가

### 이 계약이 아직 다루지 않는 것

- 최종 렌더링 UI 구조
- DB 최종 정규화 스키마
- 완성된 ontology object
- final wiki page 내용 구조
- 실제 execution command
- fully locked workflow automation rule

---

## 5. Line Object 최소 필드

- line_id: 이 line을 식별하는 ID
- anchor_refs: 이 line이 닿아 있는 출처/근거 참조들
- activation_pressure: 왜 지금 이 line이 살아났는가를 나타내는 현재 압력
- core_relation: 이 line이 중심적으로 묶고 있는 관계
- gap_profile: 이 line이 품고 있는 공백, 긴장, 미결, 부족함
- current_stage: 이 line의 현재 생애주기 단계
- downstream_options: 이 line이 다음에 갈 수 있는 경로 후보들
- maturity_level: 이 line이 얼마나 성숙했는가를 나타내는 수준
- promotion_targets: 이 line이 나중에 무엇으로 올라갈 수 있는지에 대한 상위 표면 후보
- memory_trace_ref: 이 line과 관련된 판단 흔적, 보류 이유, 재호출 기록과 연결되는 기억 참조

### 보강 필드 후보

- line_label: 현재 line을 임시로 부르는 이름. final object name이 아니다.
- classification_hint: bridge_line, conflict_line, gap_line, concept_rise_line, relay_line, validation_line 등 임시 유형 힌트
- related_line_refs: 다른 line들과의 연결 참조
- confidence_note: 이 line을 현재 강도로 읽는 이유와 한계
- last_transition_reason: 최근 stage 변화 이유

---

## 6. 필드 간 관계 해석

- anchor_refs = line의 발판
- activation_pressure = line의 현재성
- core_relation = line의 중심 연결
- gap_profile = line의 미완성성
- current_stage = line의 시간성
- downstream_options = line의 방향성
- maturity_level = line의 숙성도
- promotion_targets = line의 상승 가능성
- memory_trace_ref = line의 환류 가능성

즉 Line Object는 "이 line이 지금 무엇인가"보다 "이 line이 어디에서 와서, 왜 지금 살아 있고, 무엇을 품고, 어디로 갈 수 있으며, 어떻게 다시 불릴 수 있는가"를 담는 객체다.

---

## 7. current_stage와 maturity_level

### 핵심 분리

- current_stage = 지금 이 line이 생애주기상 어느 국면에 있는가
- maturity_level = 그 line이 얼마나 성숙했는가

즉 stage는 시간축이고, maturity는 숙성축이다. 둘은 같이 움직일 수 있지만 동일하지 않다.

### current_stage 후보

- signal: 아직 공식 line candidate라고 부르기 이르지만 line 가능성이 감지된 상태
- captured: 최소한 line candidate로 붙잡아둘 수 있고 앵커와 압력이 보이기 시작한 상태
- forming: 관계, 공백, 방향이 생기며 구조적 line으로 읽히기 시작한 상태
- articulated: line을 한두 문장으로 설명할 수 있게 된 상태
- routed: 다음 lane 또는 처리 경로를 구체적으로 잡은 상태
- held: 지금 당장 승격/실행/고정시키지 않고 보류하면서 유지하는 상태
- refluxed: 검증, 보류, 실패, 비교 결과를 받아 다시 공간 내부로 돌아간 상태
- promoted: 충분히 성숙해져 상위 표면이나 상위 구조로 올라간 상태

### maturity_level 후보

- weak: 신호는 보이지만 구조가 아직 약함
- emerging: line 형성이 시작되고 관계와 공백이 일부 드러남
- usable: relay / validation / translation / watch 대상으로 삼을 수 있음
- strong: 반복성, 관계 안정성, 공백 구조가 꽤 분명함
- promotion_ready: 상위 표면으로 올려도 될 정도로 성숙했지만 final truth는 아님

### 전이 원칙

- stage가 오른다고 무조건 좋은 것이 아니다.
- promotion이 늦는 것이 실패도 아니다.
- hold는 rejection이 아니라 숙성 보호 상태다.
- reflux는 후퇴가 아니라 재형성 루프다.
- weak / emerging 단계의 line도 신호 자산으로 남길 수 있어야 한다.
- maturity 하향은 실패가 아니라 더 정확한 읽기일 수 있다.

---

## 8. 기본 전이 규칙

### current_stage 기본 흐름

signal → captured → forming → articulated → routed → held 또는 promoted → refluxed → 다시 forming / articulated / routed / promoted 가능

즉 흐름은 단방향이 아니라 순환형이다.

### maturity_level 기본 흐름

weak → emerging → usable → strong → promotion_ready

단, 이 역시 단선 상승이 아니다. 새 자료, 검증, 비교에 따라 하향 전이가 가능하다.

---

## 9. 기관별로 주로 다루는 stage

- 원본 읽기기: signal 중심
- 입력기: signal / captured를 위한 재료 정리
- line/state 생성기: captured / forming 중심
- 라인번역기: forming / articulated 중심
- 흐름해석기: articulated / routed 중심
- 감독기: routed / held / promoted 판단 중심
- 기록기억기: held / refluxed / promoted 이후 흔적 유지 중심
- 표면구성기: promotion_ready / promoted 중심

---

## 10. 실무용 판별 질문

무언가를 보고 “이게 line인가?”를 판단할 때는 아래를 본다.

1. 이건 어디엔가 닿아 있는가
2. 왜 지금 중요해졌는가
3. 무엇과 무엇을 잇는가
4. 무엇이 아직 비어 있는가
5. 다음에 무엇을 유도하는가
6. 다시 불러와 더 두꺼워질 수 있는가
7. 나중에 상위 표면으로 올라갈 가능성이 있는가

이 질문에 대체로 답할 수 있으면 line에 가깝다. 답이 잘 안 되면 아직 신호나 포착물일 가능성이 크다.

---

## 11. 예시 line reading 요약

### Example 1. LLM Wiki ↔ VectorFL line 개념 상승선

- 성격: 개념 상승 line
- 핵심: 외부 참고물이 내부 line 개념을 “raw와 final 사이의 지속 중간층”으로 끌어올리는 흐름
- current_stage: articulated
- maturity_level: strong
- promotion_targets: concept_object, wiki_page, validation_asset
- 주의: line을 wiki-like compiled surface로 너무 빨리 오해하지 말 것

### Example 2. 사용자면 CLI ↔ 엔진면 CLI 역할 분리선

- 성격: 운영 분기 / relay line
- 핵심: 사용자면 운영 CLI와 엔진면 숙성 CLI를 분리해야 한다는 운영 구조 line
- current_stage: routed
- maturity_level: usable
- promotion_targets: work_packet, validation_asset, surface_block
- 주의: handoff contract와 승인 조건은 아직 미정

### Example 3. 검증팀 = pass/fail이 아닌 숙성 기관 선

- 성격: validation line
- 핵심: 검증팀은 결과 판정이 아니라 hold/reflux/re-interpretation으로 공간 숙성을 밀어주는 핵심 기관
- current_stage: promoted
- maturity_level: promotion_ready
- promotion_targets: concept_object, validation_asset, watchpoint, wiki_page
- 주의: 검증 산출물이 line에 어떻게 재주입되는지는 아직 더 정리 필요

---

## 12. 현재 기준 최종 정리

### 철학 기준문

라인은 거꾸로 된 온톨로지에서 개념이 위로 떠오르기 전, 여러 재료와 관계와 공백을 묶어 그 상승을 실제로 밀어주는 중간 의미 형성체다.

### 공식 기준문

라인은 통합엔진 내부에서 원재료와 최종 개념 사이를 매개하며, 여러 단서·관계·공백·압력을 묶어 다음 해석·판단·작업·검증·환류를 유발하는 지속 가능한 중간 운용 형성체다.

### Contract 기준문

Line Object는 line을 최종 개념이나 페이지로 고정하기 전, 앵커·압력·관계·공백·단계·방향·숙성도·승격 가능성·기억 흔적을 구조적으로 담아 여러 기관이 공통으로 읽고 다룰 수 있게 하는 중간 운용 계약 객체다.

### 핵심 잠금 문장

stage는 시간축이고 maturity는 숙성축이다. 둘은 함께 움직일 수 있지만 동일하지 않으며, line 판단은 두 축을 함께 읽어야 한다.

---

## 13. 금지선

- line_id만 있으면 완성된 object라고 생각하지 않는다.
- core_relation을 ontology edge처럼 너무 빨리 고정하지 않는다.
- promotion_targets를 final schema로 오해하지 않는다.
- maturity_level을 점수 게임처럼 쓰지 않는다.
- current_stage를 rigid workflow engine처럼 강제하지 않는다.
- 이 계약은 선언적 기준이지, 아직 강제 실행 모델이 아니다.
