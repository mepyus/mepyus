# space three-axis operating loop and material intake spec v0

## 0. purpose

이 문서의 목적은
이미 분리한 3축

- `space construction`
- `line reading`
- `line inspection`

을 실제 운영 루프로 구조화하는 것이다.

핵심은 아래다.

- 사용자는 외부 자료와 문제를 계속 넣는다
- 공간은 construction 축에서 재료와 흔적을 만든다
- line reading 축에서 line을 반복 reread한다
- human-language meaning reread 축면에서 그 line을 사용자 언어의 의미 연결로 다시 푼다
- line inspection 축에서 premature 해석을 검점한다
- 그 결과가 다시 다음 construction과 다음 intake 기준이 된다

즉 이 문서는 선언이 아니라
`반복 가능한 협업/운영 루프`를 고정한다.

---

## 1. role split

### 1.1 user side

사용자 쪽 주 역할은 아래다.

- 외부 자료 투입
- 내부에서 다시 보고 싶은 문제 제시
- reference 코드 / 기존 프로그램 / business 사례 제공
- 어떤 층위에서 읽고 싶은지 방향 제시
- 현재 판단이 맞는지 감각 피드백 제공

즉 사용자는
공간에 새 재료와 새 문제를 계속 밀어 넣는 쪽이다.

### 1.2 codex side

Codex 쪽 주 역할은 아래다.

- 재료를 construction axis로 정리
- line reading axis로 반복 reread
- line inspection axis로 검점
- premature naming / premature hub calling 억제
- reread 결과를 다시 기록 자산으로 남기기

즉 Codex는
`내부 loop operator` 역할을 맡는다.

---

## 2. base loop

기본 운영 루프는 아래다.

### step 1. material intake

입력:

- 외부 자료 1건 이상
- 내부에서 다시 보고 싶은 기존 자산
- reference 코드/프로그램/문서

목표:

- 무엇을 construction 대상으로 넣는지 결정
- provenance와 entry point를 분명히 함

### step 2. construction pass

하는 일:

- 입력 저장
- source/reference lane 배치
- trace / receipt / note / report 최소 흔적 생성
- 필요시 기능 변경 이유도 reason material로 남김

결과:

- 공간 안에서 reread 가능한 재료가 생김

### step 3. line reading pass

하는 일:

- 입력에서 line 후보를 먼저 본다
- 같은 line을 다른 목적어로 읽는다
- 같은 line을 다른 폴더/코드/runtime/view에 대입한다
- latent line과의 접촉을 본다

결과:

- 잠정 line
- 반복 응결 조짐
- cross-objective contact

### step 3.5. human-language meaning reread pass

하는 일:

- 방금 읽은 line을 구조 언어로만 두지 않는다
- line끼리 어떤 의미 연결을 만드는지 본다
- 그 연결이 사용자 언어에서 어떤 생각/감각/판단으로 이어지는지 다시 푼다
- 쉬운말 치환이 아니라 `line이 이어지는 인간 언어 설명`으로 내려본다
- 구조 reread와 의미 reread가 서로 어긋나는지 확인한다

결과:

- 사용자 언어 의미 서술 초안
- 구조적 line과 의미적 line의 접속 지점
- 아직 구조만 보이고 의미 연결은 약한 부분

### step 4. line inspection pass

하는 일:

- reread 횟수 충분성 확인
- unrelated/cross line interference 확인
- human-language meaning reread가 실제 의미 연결까지 내려갔는지 확인
- 구조 요약을 사용자 언어로만 바꾼 가짜 재독해는 아닌지 확인
- strong/weak 본질화 방지
- hub naming이 너무 빠른지 확인
- philosophy fit / mismatch 확인

결과:

- 살아남는 잠정 line
- 아직 흔적인 것
- 다음 reread 필요 축

### step 5. return to construction

하는 일:

- inspection 결과를 다시 space material로 남김
- 필요시 새로운 기능/문서/trace/실험을 construction axis에 넣음

결과:

- 다음 루프의 재료가 더 두꺼워짐

즉 기본 순환은:

`material intake -> construction -> line reading -> human-language meaning reread -> line inspection -> next construction`

이다.

---

## 3. reread minimum rule

한 번 읽고 끝내지 않는다.

최소 원칙은 아래다.

- 같은 line을 최소 여러 번 reread한다
- 목적어를 바꿔 읽는다
- 폴더를 바꿔 읽는다
- 코드/문서/runtime/view를 교차한다
- 가능하면 무관해 보이는 line도 일부러 섞어 본다

즉 single-pass reading은 line confirmation 근거가 아니다.

---

## 4. output discipline

각 루프는 아래를 구분해서 남긴다.

### construction output

- 무엇이 들어왔는가
- 어디에 저장되었는가
- 어떤 trace가 생겼는가

### line reading output

- 어떤 line이 먼저 보였는가
- 어디서 반복되었는가
- 어떤 응결 조짐이 있었는가

### human-language meaning output

- 그 line이 사용자 언어에서 어떤 의미로 이어졌는가
- 어떤 연결은 실제로 살아 있었고 어떤 연결은 아직 비어 있었는가
- 구조 언어와 의미 언어가 어디서 서로 만났는가

### inspection output

- 무엇이 premature했는가
- 무엇이 계속 살아남았는가
- 무엇을 다음 loop에서 다시 봐야 하는가

즉 결과도 3축으로 나눠 남겨야 한다.

---

## 5. when to lock and when not to lock

### lock allowed

- reread가 충분히 반복된 뒤
- inspection에서 premature naming 위험이 낮고
- 이후 운영 기준으로 재사용할 가치가 분명할 때

### lock not allowed

- 한 번 읽은 line
- 아직 unrelated cross-check가 없는 line
- 아직 응결보다 흔적 수준인 line
- construction 결과만 있고 reread가 얇은 상태

즉 lock은 loop의 끝에서만 허용된다.

---

## 6. why this helps both sides

이 구조가 있으면:

### codex

- 무엇을 먼저 할지 분명해진다
- 잠금 쪽으로 과속하는 걸 줄일 수 있다
- 내부 reread loop를 지속적으로 돌릴 수 있다

### user

- 외부 자료를 어디에 넣어야 할지 분명해진다
- 지금이 construction 턴인지 reread 턴인지 알 수 있다
- 결과가 단순 요약인지 실제 line reread 결과인지 구분할 수 있다

---

## 7. immediate working posture

당분간은 아래처럼 움직이는 것이 맞다.

1. 사용자는 외부 자료/레퍼런스/문제 축을 계속 넣는다
2. Codex는 construction axis로 먼저 재료를 정리한다
3. reread loop를 반복한다
4. 사용자 언어 의미 reread까지 내려간다
5. inspection으로 premature 해석을 걷어낸다
6. 잠금은 꼭 필요할 때만 한다

즉 지금의 주력은
새 구조 발명보다
이 루프를 생활화하는 것이다.

---

## 8. one-line summary

앞으로 공간은
사용자가 재료를 넣고,
Codex가 `construction -> line reading -> human-language meaning reread -> line inspection`
루프를 반복하며,
그 결과를 다시 다음 재료와 다음 구현에 먹이는 방식으로 운용한다.

이 구조가 있어야 공간은 문서 저장소가 아니라
반복 숙성과 반복 reread가 가능한 작업장으로 자란다.
