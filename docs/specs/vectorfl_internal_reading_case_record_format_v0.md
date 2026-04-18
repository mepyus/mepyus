# vectorfl internal reading case record format v0

## purpose

이 문서는 내부 공간을 깊게 읽을 때
매번 같은 깊이와 같은 보수 규칙으로 기록하기 위한
case record 형식을 잠근다.

핵심은 요약이 아니라 다음 네 가지를 분리해 남기는 것이다.

- raw first reading
- confidently recognized material
- inferred but not yet secured material
- unread or still-blind material

이 형식은
VectorFL Paper가 이후 보여줘야 할
`source -> line -> recall -> gap -> next action`
흐름의 원재료가 된다.

## one-line rule

case 하나를 읽을 때는
`원본 먼저 읽기 -> 확실한 인식 -> 추정 -> 미독해 -> 왜 중요한지 -> 다음 확인`
순서로 기록한다.

## required fields

### 1. case id
- 예: `case_01_work_map_entry`

### 2. source materials
- 실제로 읽은 파일 경로
- status 문서와 본문 문서를 함께 적는다

### 3. raw first reading
- 아직 VectorFL 언어로 과하게 환원하기 전
- 이 재료가 겉으로 무엇을 하고 있는지 한두 문장으로 적는다

### 4. what i can confidently recognize
- 원문 근거가 충분히 있는 판단만 적는다
- 해석보다 구조와 계약을 우선 적는다

### 5. what i am inferring
- 원문에 암시되지만 직접 문장으로 잠기지 않은 것
- 내 해석 개입이 들어간 부분

### 6. what i still cannot read
- 이 자료만으로는 판단 불가한 것
- 다음에 다른 파일이나 generated artifact가 필요한 것

### 7. linked status or generated artifacts
- 이 case를 더 두껍게 읽기 위해 함께 봐야 하는 status/generated 결과

### 8. why it matters for vectorfl paper
- 이 case가 나중에 어떤 page class 또는 line recall 흐름에 연결되는지

### 9. next verification or recall
- 다음에 무엇을 더 봐야 하는지
- 추가 compare, generated ledger, receipt, runlog 후보

### 10. recognition level
- `clear`
- `usable`
- `partial`
- `thin`

## writing rules

### rule 1
- 예쁜 요약보다 근거가 있는 구조 설명을 먼저 적는다.

### rule 2
- `무엇을 못 읽었는지`를 반드시 남긴다.

### rule 3
- line이나 family 언어로 옮기고 싶어도
  raw first reading을 먼저 적는다.

### rule 4
- status 문서는 entrypoint로,
  본문/spec/generated 문서는 실제 근거로 구분한다.

### rule 5
- case 하나가 곧바로 교리나 결론이 되면 안 된다.
  case는 다음 recall을 위한 관찰 단위다.

## minimal output shape

아래 순서를 유지한다.

1. `case_id`
2. `source_materials`
3. `raw_first_reading`
4. `what_i_can_confidently_recognize`
5. `what_i_am_inferring`
6. `what_i_still_cannot_read`
7. `linked_status_or_generated_artifacts`
8. `why_it_matters_for_vectorfl_paper`
9. `next_verification_or_recall`
10. `recognition_level`

## one-line lock

internal reading case record는
`내가 무엇을 읽었다`를 자랑하는 문서가 아니라
`내가 어디까지 읽을 수 있었고 어디서부터 추정과 blindness가 시작되는지`
를 남기는 보수 기록이다.
