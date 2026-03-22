[[A]] [[OBJ:replica_method_spec]] [[ROLE:engine]]

# VECTORFL Replica — 운영 방법 규약 v0.1
# 부제: Codex 학습용 기준 문서

## 0. 목적

이 문서는 Replica에서
"무엇을 쌓을 것인가"가 아니라
"어떻게 쌓을 것인가"를 고정하기 위한 운영 규약이다.

핵심은 단순하다.

우리는 값을 모으는 것이 아니라,
값이 붙고 / 바뀌고 / 반복되고 / 보류되고 / 다시 떠오르는
전체 과정을 축적한다.

즉 Replica는 결과 저장소가 아니라
판정과 변화의 흔적을 보존하는 엔진이다.

이 문서는 특히 Codex가 앞으로 배워야 할
운영법 / 저장법 / 우선순위 / 금지사항을 함께 담는다.

## 1. 최상위 원칙

### 원칙 1. 값보다 흔적이 중요하다
좋은 current 값 하나보다,
그 값이 어떻게 생겼고 왜 바뀌었는지가 더 중요하다.

### 원칙 2. 덮어쓰기보다 누적이 우선이다
가능하면 기존 기록을 지우지 않고
새 사건 / 새 판정 / 새 revision으로 추가한다.

### 원칙 3. 원본은 원본대로 남긴다
원문, 로그, 대화, 스크립트, 메모는
정제 이전 상태도 함께 보존한다.

### 원칙 4. 애매함도 재료다
불확실 / 보류 / 약한 신호 / 연결 실패도
가능하면 observation으로 남긴다.

### 원칙 5. seed는 주입하지 않고 흘려보낸다
앵커 표본은 정답처럼 꽂지 않는다.
shadow로 흘려보내고, 반복되면 나중에 승격한다.

### 원칙 6. Replica는 현재값 저장소가 아니라 변화 추적 엔진이다
current만 맞아도 충분하지 않다.
history와 lineage가 함께 있어야 한다.

## 2. 저장 구조 3분할

Codex는 앞으로 모든 데이터/레코드를 아래 3층 중 하나로 분류해서 다뤄야 한다.

### 2.1 Current
지금 대표로 읽히는 값

예:
- current primary anchor
- current processing values
- current source location
- current projection summary

질문:
- 지금 이 fragment는 현재 어떻게 읽히는가?

### 2.2 History
값이 생기고 변한 이력

예:
- measurement history
- ingest history
- anchor revision history
- processing revision history

질문:
- 이 current는 어떤 과정을 통해 만들어졌는가?

### 2.3 Observation / Hypothesis
아직 확정은 아니지만 관찰한 신호

예:
- ambient anchor probe
- connection observation
- fragment comparison note
- rejected/deferred relation
- provisional judgment

질문:
- 아직 확정은 아니지만 무엇을 봤는가?
- 무엇이 약하게 공명했는가?
- 무엇이 아직 안 붙었는가?

## 3. fragment 운영 규약

### 3.1 fragment는 최소 재료다
fragment는 Replica의 기본 원자 재료다.
절대 가볍게 지우거나 덮어쓰지 않는다.

### 3.2 fragment는 append-only 원칙으로 다룬다
잘못 잘랐다고 기존 fragment를 지우기보다,
새 fragmentation 또는 revision record를 추가한다.

### 3.3 fragment에 반드시 붙어야 하는 최소 필드
- fragment_id
- source_id
- source_type
- source_location
- raw_text
- unit_scale
- created_at
- ingest_batch_id
- ingest_session_id

## 4. anchor 운영 규약

### 4.1 anchor는 값이 아니라 판정 사건이다
anchor를 단순 필드 업데이트로 처리하지 않는다.

항상 아래처럼 사건으로 남긴다.
- 언제 붙었는가
- 누가/무엇이 붙였는가
- 왜 붙였는가
- 이전값은 무엇이었는가
- confidence는 얼마였는가

### 4.2 primary anchor는 snapshot으로 남긴다
current primary만 두지 않는다.
시점별 snapshot 또는 event record로 함께 남긴다.

### 4.3 anchor 층은 최소한 분리한다
- object
- semantic
- structural

필요 시 later layer:
- flow
- fear
- intent
- operation

### 4.4 anchor revision은 사람 판단도 기록한다
나중에 사람이 값을 고쳤다면
이전값 / 새값 / 수정이유 / 수정시각 / 수정주체를 남긴다.

## 5. processing values 운영 규약

### 5.1 processing 값도 current + history로 다룬다
D/I/S, scene, flow, time은 current만 두지 않는다.
anchor와 마찬가지로 snapshot/event로 누적한다.

### 5.2 최소 필드
- D
- I
- S
- scene
- flow
- time
- calculated_at
- calculation_version
- batch_id
- session_id

### 5.3 processing revision도 measurement로 남긴다
값이 달라지면
그냥 update하지 말고
revision measurement 또는 new snapshot으로 남긴다.

## 6. measurement 운영 규약

### 6.1 measurement는 Replica의 핵심 저장층이다
Replica의 진짜 가치는 current 값보다
measurement history에 있다.

### 6.2 measurement는 자동층과 수동층으로 나눈다

#### 자동 measurement
- source_location
- processing_values
- projection
- anchor auto-evaluation
- ambient_anchor_probe raw result

#### 수동/검토 measurement
- revision judgment
- comparison note
- false resonance
- rejected relation reason
- anchor correction rationale

### 6.3 measurement 최소 공통 필드
- measurement_id
- measurement_type
- fragment_id
- source_id
- batch_id
- session_id
- created_at
- revision_of
- operator
- notes

## 7. lineage / batch / session 운영 규약

### 7.1 lineage는 모든 기록의 척추다
fragment, anchor snapshot, processing snapshot, measurement, probe 결과
전부 lineage를 가져야 한다.

### 7.2 최소 lineage 필드
- source_id
- fragment_id
- ingest_batch_id
- ingest_session_id
- created_at

권장 추가:
- revision_of
- derived_from
- parent_id
- operator
- origin_kind

## 8. seed bank / shadow signal 운영 규약

### 8.1 seed는 primary anchor 후보가 아니다
seed는 정답이 아니라 주변 공명 후보이다.

### 8.2 seed는 본문에 넣지 않는다
fragment 본문 오염 금지
raw text 직접 수정 금지
source text와 seed text merge 금지

### 8.3 seed는 sidecar/shadow로만 흐르게 한다
ambient_anchor_probe 또는 유사 measurement로만 먼저 붙인다.

### 8.4 seed stage는 3단만 허용한다
- shadow
- soft
- stable

## 9. 연결 관찰 운영 규약

### 9.1 연결은 붙은 것만 기록하지 않는다
아래 3종을 반드시 분리한다.
- accepted_connection
- rejected_connection
- deferred_connection

### 9.2 이유
연결된 것만 보면 공간을 과대해석하게 된다.
안 붙은 것 / 보류된 것 / false resonance도 중요하다.

## 10. revision judgment 운영 규약

### 10.1 사람이 수정한 순간은 매우 중요하다
사람 수정은 단순 교정이 아니라
Replica 학습 데이터다.

### 10.2 반드시 남길 것
- previous_value
- new_value
- reason
- operator
- revised_at
- related_measurement_id

## 11. fragment comparison 운영 규약

### 11.1 비슷한 fragment를 비교하는 기록도 필요하다
앵커 품질 개선과 분절 개선에 직접 도움된다.

### 11.2 남길 것
- fragment_a
- fragment_b
- similarity_reason
- difference_reason
- comparison_note
- operator
- compared_at

## 12. document-level relation 운영 규약

### 12.1 later layer에서 필요
fragment만 보면 상위 읽기가 어려워질 수 있다.
문서-문서 수준 관계도 나중엔 필요하다.

### 12.2 주의
지금 당장 코어에 밀어 넣지 않는다.
observer layer 또는 later layer로 붙인다.

## 13. 운영 리듬 규약

### 13.1 매 입력 시
- source 저장
- fragment 생성
- current anchor 계산
- current processing 계산
- measurement 자동 저장
- lineage 부착
- ambient probe 부착

### 13.2 매 batch 후
- 반복 seed 집계
- source.* 과잉 점검
- anchor quality 샘플 리뷰
- measurement 누락 점검

### 13.3 주기적 리뷰
- shadow -> soft 승격 후보 검토
- 사람이 수정한 judgment 패턴 정리
- false resonance / missed connection 정리
- fragment boundary 품질 점검

## 14. 하지 말아야 할 것

- current 값만 남기고 history를 생략하는 것
- fragment를 수정본으로 덮어써 원래 흔적을 지우는 것
- seed를 바로 primary anchor로 승격하는 것
- 외부 raw 신호를 본문에 바로 섞는 것
- lineage 없는 measurement를 생성하는 것
- 수정 이유 없이 값만 교체하는 것
- 연결된 것만 보고 안 붙은 것/보류를 버리는 것
- observation/hypothesis를 current처럼 다루는 것

## 15. Codex 전용 학습 요약

- Replica는 결과 저장소가 아니다
- append-only 사고
- current/history/observation 분리
- seed는 그림자다
- lineage는 필수다
- 사람 수정은 학습 데이터다
- 연결 실패도 재료다

## 16. 추천 구현 순서

### Step 1
fragment / current anchor / current processing 구조를
current + history 관점으로 다시 점검

### Step 2
measurement를 모든 주요 판정값의 기본 저장층으로 고정

### Step 3
모든 레코드에 lineage 최소 필드 강제

### Step 4
seed bank + ambient_anchor_probe를 shadow layer로 추가

### Step 5
revision judgment / comparison / connection observation을 observer layer로 추가

### Step 6
later layer에서 document-level relation 추가

## 17. 한 줄 결론

Replica의 운영 핵심은
값 저장이 아니라
fragment를 중심으로 anchor / processing / measurement / lineage / seed signal이
현재값 / 변화이력 / 관찰가설의 세 층으로 계속 누적되게 만드는 것이다.
