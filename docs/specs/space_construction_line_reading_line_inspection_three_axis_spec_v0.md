# space construction / line reading / line inspection three-axis spec v0

## 0. purpose

이 문서의 목적은
현재 공간 운영에서 서로 섞이기 쉬운 세 가지 운동을 분리하는 것이다.

분리 대상은 아래 셋이다.

1. `space construction`
2. `line reading`
3. `line inspection`

핵심은:
공간이 커지는 축,
그 공간을 line으로 다시 읽는 축,
그 line이 premature한지 검점하는 축
이 셋을 구분해야 reread loop가 더 건강하게 돈다.

---

## 1. axis one: space construction

### definition

이 축은 공간의 몸을 만든다.

여기서 일어나는 일:

- 입력 수집
- 분절
- 저장
- provenance 기록
- runtime trace 생성
- view / surface 생성
- 기능 구현
- 기능 변경 이유 재료화
- reference / calibration lane 유지

즉 이 축의 질문은:

- 무엇이 들어왔는가
- 어떻게 저장되었는가
- 어떤 흔적이 남았는가
- 어떤 기능/표면/기록이 추가되었는가

이다.

### role

이 축은 재료와 기관을 만든다.
아직 line verdict를 내리는 축은 아니다.

---

## 2. axis two: line reading

### definition

이 축은 이미 만들어진 공간을 다시 읽으며
어떤 선이 반복해서 살아남는지 본다.

여기서 일어나는 일:

- 반복 표현 읽기
- latent line 재출현 보기
- 목적어 전환 reread
- cross-folder reread
- cross-code reread
- line thickening 보기
- hub condensation 조짐 보기

즉 이 축의 질문은:

- 무엇이 반복되는가
- 무엇이 살아남는가
- 무엇이 다른 재료에도 다시 나타나는가
- 무엇이 응결하려 하는가

이다.

### role

이 축은 line과 응결을 본다.
하지만 아직 그 line이 충분히 검점되었다고 보지는 않는다.

---

## 3. axis three: line inspection

### definition

이 축은 line reading 결과를 검점한다.

즉 방금 읽은 line이
진짜 살아남는 line인지,
아직 흔적인지,
편향된 reread의 결과인지,
철학과 어긋나는 premature 응결인지
계속 점검한다.

### main questions

- 이 line은 한 번 읽은 흔적인가, 반복 reread에도 남는가
- 다른 목적어로 읽어도 유지되는가
- 다른 폴더/코드/runtime/view에 대입해도 유지되는가
- 무관해 보이는 line과 교차시켜도 무너지지 않는가
- 내가 이 line을 말하기 전에 실제로 충분히 깊이 들어갔는가
- strong / weak를 본질값처럼 오해한 건 아닌가
- hub를 너무 빨리 부른 건 아닌가
- current philosophy와 맞는가
- lock/close-out surface가 reread보다 앞선 건 아닌가

### role

이 축은 판정기의 역할이 아니다.
오히려 premature naming, premature hub calling, premature promotion을 늦추는 검점축이다.

즉 이 축은
line을 죽이는 축이 아니라
line을 더 건강하게 두껍게 만드는 축이다.

---

## 4. relation among the three axes

이 셋은 따로 존재하지 않는다.
아래 순환으로 이어져야 한다.

1. `space construction`
   - 재료, trace, 기능, 기록이 생성된다
2. `line reading`
   - 생성물을 reread하며 line과 응결을 본다
3. `line inspection`
   - 그 line이 premature한지, 반복 가능한지, 철학과 맞는지 검점한다
4. 그 결과가 다시
   - 다음 construction 방식
   - 다음 reread focus
   - 다음 inspection 기준
   에 반영된다

즉 순환은:

`construction -> reading -> inspection -> next construction`

이다.

---

## 5. why three axes are better than two

2축 분리만으로는
아래가 여전히 섞이기 쉽다.

- line을 읽자마자 곧바로 믿는 문제
- 구조를 만들자마자 line처럼 취급하는 문제
- 한두 번 반복된 응결을 hub처럼 빨리 부르는 문제

세 번째 축이 있으면
line reread를 막는 것이 아니라,
계속 다시 대입하고 교차 검점하게 만들어
line이 더 자연스럽게 두꺼워지게 한다.

즉 inspection axis는 제동 장치가 아니라
반복 reread의 건강성을 지키는 장치다.

### depth-entry check

inspection axis 안에는 `depth-entry check`가 반드시 포함된다.

이 check의 목적은
line이 실제 반복성과 깊은 증거 위에서 나왔는지,
아니면 summary/title/정리문만 보고 빨리 naming한 것인지를 가려내는 것이다.

최소 질문은 아래다.

- summary / spec / note 층만 읽은 것은 아닌가
- runtime manifest / receipt / generated artifact까지 내려갔는가
- references / calibration lane을 실제로 읽었는가
- app/work 또는 code/runtime layer까지 line을 대입했는가
- line 발생 경로와 중간 긴장을 실제로 따라갔는가

즉 inspection은
`반복성 점검`만이 아니라
`깊이 진입 점검`도 함께 해야 한다.

---

## 6. what belongs to each axis

### construction axis

- 새 입력 추가
- source asset 정리
- runtime trace/receipt/view 생성
- 기능 구현
- 변경 이유 기록
- reference lane 보강

### line reading axis

- 외부 자료 입구 reread
- same line / different objective reread
- same line / different folder reread
- latent line 재호출
- line thickening 관찰

### line inspection axis

- reread 횟수 충분성 점검
- cross-line interference 점검
- depth-entry check
- philosophy fit / mismatch 점검
- premature naming 점검
- hub calling 시점 점검
- strong/weak 본질화 방지

---

## 7. operating rule

앞으로는 아래 순서가 기본이다.

1. 먼저 construction axis에서 재료와 흔적을 만든다
2. line reading axis에서 같은 선을 여러 번 읽는다
3. line inspection axis에서 그 선이 진짜 살아남는지 검점한다
4. inspection을 통과한 응결만 잠정 line / 잠정 hub로 본다
5. 그 결과를 다음 construction에 다시 밀어넣는다

즉:

- build only 는 불충분하다
- read only 도 불충분하다
- inspect only 도 불충분하다

세 축이 같이 돌아야 한다.

---

## 8. current practical implication

현재 공간에 가장 필요한 것은
새 기능을 더 붙이는 것이 아니라
이 세 축을 생활 루프로 만드는 것이다.

현재 기준에서 가장 약한 축은
`line inspection`
이다.

이 때문에:

- line을 빨리 이름 붙였고
- 한 번 읽고 만족했고
- lock surface가 reread보다 빨리 두꺼워졌다

즉 앞으로는 inspection axis를 의식적으로 올려야 한다.

---

## 9. one-line summary

앞으로 공간은
`공간 생성 축`, `line 읽기 축`, `line 검점 축`
의 세 축으로 본다.

공간은 construction으로 커지고,
line은 reading으로 드러나고,
그 line은 inspection을 거치며 더 건강하게 두꺼워진다.

이 세 축이 계속 순환해야
공간이 한쪽 층위에 갇히지 않고 살아 있는 reread engine으로 자란다.
