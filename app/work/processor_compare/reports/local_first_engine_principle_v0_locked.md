# local-first engine principle v0
## offline core + optional amplifier constitution

## 0. one-line definition

엔진의 코어는 인터넷과 외부 AI 없이도 로컬에서 성립해야 하며, 외부 연결은 본체가 아니라 선택적으로 부착되는 증폭기여야 한다.

## 1. core meaning

이 원칙은 단순한 오프라인 대응이 아니다.
핵심은 엔진의 생명선이 외부 연결 상태에 묶이지 않도록 하는 것이다.

원하는 상태:

1. 연결이 끊겨도 엔진은 멈추지 않는다.
2. 기록, 상태, 보류, 재판독은 로컬에서 계속 유지된다.
3. 외부 AI나 인터넷은 있으면 강해지지만, 없어도 코어 논리는 성립한다.
4. 해석의 주도권은 외부 모델이 아니라 엔진 구조와 사용자에게 남는다.

따라서 이 원칙은 기술 제약 대응이 아니라,
엔진의 정체성을 외부 서비스로부터 분리하는 구조 원칙이다.

## 2. absolute boundary between core and attachments

### 2.1 core

로컬만으로 반드시 성립해야 하는 영역:

- 입력 수집
- 입력 분해
- local_ref 생성 및 보존
- anchor / handle / processing value 기록
- ledger 기록
- layer 상태 관리
- blocker / proposal / revisit 기록
- local workbench 판독
- 기본 review surface 생성
- 기본 graph / space / timeline projection 생성
- 로컬 파일 기반 lifecycle 유지

즉 core는
입력이 들어오고, 흔적이 남고, 상태가 유지되고, 다시 읽힐 수 있는 구조여야 한다.

### 2.2 optional amplifier

있으면 강해지지만 없어도 엔진은 계속 돌아가야 하는 영역:

- 외부 LLM 판독 보강
- 인터넷 검색
- 외부 지식 주입
- 대규모 생성
- 교차 검증
- 요약 / 재서술 / 확장 보조
- 외부 API 호출
- 외부 센서 / 외부 시스템 enrichment

즉 optional amplifier는
core의 결과를 바꾸는 주체가 아니라,
core 위에 추가 정보나 확장 해석을 공급하는 보조 수단이다.

## 3. why this matches the engine direction

현재 엔진의 강점은 외부에서 답을 빨리 가져오는 데 있지 않다.
오히려 아래에 있다.

- 약한 신호를 버리지 않음
- 애매한 가능성을 살아남게 함
- 보류 상태를 유지함
- 다시 읽힐 수 있게 남김
- 미세한 연결을 오래 붙잡음
- 지금 확정 못 하는 것도 미래 자산으로 둠

이건 외부 모델 접속 여부보다,
저장 구조 / 상태 구조 / 재판독 구조와 더 관련이 깊다.

따라서 local-first는 편의 기능이 아니라
엔진 해석 방식과 맞는 철학이다.

## 4. technical restatement

### 4.1 ledger

로컬에서 반드시 유지되어야 하는 기억층이다.

질문:

- 무엇이 들어왔는가
- 어떤 값이 생성되었는가
- 무엇이 보류되었는가
- 왜 아직 확정되지 않았는가
- 무엇을 다시 봐야 하는가

핵심:
ledger는 외부 연결이 없어도 흔적을 잃지 않게 하는 최소 기억 장치다.

### 4.2 layer

로컬에서 반드시 유지되어야 하는 상태층이다.

질문:

- 지금 어디에 있는가
- 어느 층위에 머무르는가
- 왜 못 넘어가는가
- revisit가 필요한가
- archived/cold로 내려가야 하는가

핵심:
layer는 해석의 존재 상태를 보존하는 장치다.

### 4.3 local workbench

로컬에서 실제 판단이 일어나는 국소 현장이다.

질문:

- 왜 이 후보가 여기까지 왔는가
- 왜 여기서 막혔는가
- 어떤 local_ref가 핵심 근거인가
- residual은 무엇인가
- 다음에 어디를 다시 봐야 하는가

핵심:
workbench는 외부 AI가 없어도 후보를 해부하고 재판독할 수 있어야 한다.

### 4.4 projection

로컬에서 읽을 수 있어야 하는 투영면:

- graph view
- space view
- timeline view
- review surface

핵심:
projection은 본체가 아니라 읽기면이다.

## 5. operating disciplines

### rule 1. core must survive independent of external connectivity

인터넷이 끊겨도,
AI 호출이 실패해도,
외부 API가 죽어도,
다음은 멈추면 안 된다.

- 입력 저장
- ledger 기록
- layer 업데이트
- blocker 보존
- revisit 등록
- local workbench 생성
- 로컬 projection 생성

### rule 2. external results are not first truth

외부 AI나 인터넷 검색 결과는 바로 canonical truth가 되면 안 된다.

반드시 아래 중 하나로 들어와야 한다.

- proposal
- enrichment
- external hint
- review candidate
- support evidence

즉 외부 결과는 곧바로 본체 판정이 아니라,
본체가 다시 읽어야 하는 재료다.

### rule 3. state confirmation happens only through local ledger + layer transition

외부 모델이 좋다고 말해도,
외부 검색이 확실해 보여도,
최종 확정은 항상 아래를 거쳐야 한다.

- ledger entry 기록
- evidence 연결
- evaluator/policy source 명시
- layer transition 반영

즉 외부는 제안할 수 있지만,
확정은 core만 한다.

### rule 4. external connections are boosters, not life-support

이 원칙이 깨지면 엔진은 로컬 코어가 아니라
외부 모델 프론트엔드로 전락한다.

우리가 원하는 것은 반대다.

- 코어는 스스로 산다
- 외부는 필요할 때만 붙는다
- 붙으면 강해진다
- 떨어져도 죽지 않는다

## 6. practical reading

### 6.1 minimum runtime loop

아무 외부 연결이 없어도 다음은 가능해야 한다.

- 텍스트/메모/로그 입력
- fragment/local_ref 단위 분해
- anchor/handle 생성
- processing values 저장
- ledger update
- layer assignment
- workbench candidate 생성
- blocker/revisit 기록
- review surface 출력

즉 최소 엔진은 입력-기록-상태-재판독 루프를 로컬에서 닫아야 한다.

### 6.2 when external connection exists

외부 연결이 붙으면 다음이 강화될 수 있다.

- 해석 다양성 증가
- 빠른 요약/변환
- 외부 사실 교차 검증
- 검색 기반 enrichment
- 추가 candidate 제안
- weak trace 보강
- 장기 패턴 비교 보조

하지만 이것들은 전부 core 바깥 확장이다.

### 6.3 failure-tolerant structure

외부 부착물은 실패할 수 있다.
그러므로 실패 시에도 다음 원칙을 따른다.

- 실패 기록은 ledger에 남긴다
- 기존 상태는 보존한다
- 외부 부착물 실패가 core lifecycle을 깨면 안 된다
- 실패 결과는 blocker 또는 `external_unavailable`로만 남긴다

## 7. why this is strong

### 1. it preserves structural control

외부 모델이 바뀌어도,
인터넷 환경이 바뀌어도,
엔진의 철학과 운영 규율이 유지된다.

### 2. it uses the strength of scripts

단순한 스크립트는 화려하지 않지만 강하다.

- 반복 가능
- 예측 가능
- 디버깅 가능
- 파일로 남음
- 운영 통제 가능
- 오프라인 지속 가능

즉 단순하지만 강한 스크립트는
엔진 코어를 구성하기에 매우 적합하다.

### 3. it preserves human interpretation better

사람의 생각은 늘 불완전하게 들어온다.
초기에 필요한 것은 외부 지식의 화려함보다
약한 신호를 죽이지 않는 로컬 보존 구조다.

### 4. it lasts longer

특정 API, 특정 모델, 특정 서비스에 종속된 구조는 빠르게 낡는다.
반면 local-first core는 외부 도구가 바뀌어도 살아남는다.

## 8. design tests

앞으로 어떤 기능을 붙일 때는 항상 아래 질문으로 판별한다.

### q1. 이 기능이 없으면 core lifecycle이 멈추는가?

- 멈춘다면 core여야 한다.
- 안 멈춘다면 optional amplifier일 가능성이 크다.

### q2. 이 기능이 상태를 확정하는가, 아니면 보조 정보를 주는가?

- 상태 확정이면 core 경계 안에서 다뤄야 한다.
- 보조 정보면 optional amplifier다.

### q3. 외부 연결이 끊겼을 때 이 기능이 완전히 무의미해지는가?

- 그렇다면 core가 아니다.
- 없어도 대체 흐름이 남아야 core와 결합 가능하다.

### q4. 이 기능이 로컬 기록 없이 결과만 던지는가?

- 그렇다면 엔진형 기능이 아니다.
- ledger/layer와 결합되어야 엔진 내부 자산이 된다.

## 9. implementation lock

### core implementation defaults

- 로컬 파일 기반
- 텍스트/JSON 중심
- 상태 전이 명시
- ledger append 중심
- layer board 분리 유지
- workbench는 local_ref 중심
- projection은 read-only surface

### external amplifier defaults

- adapter 형태로 부착
- 결과는 proposal/enrichment/support로만 유입
- 실패 허용
- 비연결 시 graceful degradation
- core state 직접 변경 금지

즉 구조적으로는

- core -> stable
- adapter -> replaceable

로 간다.

## 10. final definition

우리는 외부 AI나 인터넷이 있어야만 움직이는 시스템을 만들지 않는다.
우리는 로컬에서 생각의 흔적을 저장하고, 상태를 붙잡고, 다시 읽고, 다시 연결할 수 있는 코어를 만든다.
외부 AI와 인터넷은 그 코어를 대체하는 본체가 아니라,
필요할 때 붙는 선택적 증폭기다.

## 11. final locked sentences

### lock 1

엔진의 본체는 로컬에서 살아야 한다.

### lock 2

외부 AI와 인터넷은 코어가 아니라 증폭기다.

### lock 3

연결이 끊겨도 기록, 상태, 재판독은 계속되어야 한다.

### lock 4

외부 결과는 즉시 진실이 아니라, 로컬 본체가 다시 읽어야 할 제안 자산이다.

### lock 5

단순하지만 강한 스크립트는 이 엔진의 약점이 아니라 가장 중요한 강점이다.

## 12. final sentence

오프라인에서도 도는 엔진을 만들면,
우리는 외부 지식 의존형 시스템이 아니라
사람의 해석 구조를 로컬에서 붙잡고 자라게 하는 진짜 엔진을 갖게 된다.
