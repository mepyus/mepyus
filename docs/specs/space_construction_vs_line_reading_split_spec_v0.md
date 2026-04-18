# space construction vs line reading split spec v0

## 0. purpose

이 문서의 목적은
현재 공간에서 자꾸 섞이기 쉬운 두 운동을 분리하는 것이다.

분리 대상은 아래 둘이다.

1. 내부 공간을 만드는 운동
2. 그 공간을 읽을 line을 세우고 반복 reread하는 운동

핵심은:
둘은 같은 방향을 보지만 같은 층이 아니다.
이 둘을 분리해서 읽어야

- 공간 생성이 line 판정으로 오해되지 않고
- line 관찰이 구조 고정으로 급히 수렴하지 않으며
- reread loop가 생활화될 수 있다

---

## 1. first split

### A. space construction layer

이 층은 공간의 몸을 만든다.

여기서 다루는 것은:

- 입력 레인
- source asset
- reference / calibration lane
- runtime trace
- observer surface
- hold / provenance / receipt / manifest / view
- 기능 구현
- 변경 이유의 재료화

즉 이 층의 질문은:

- 무엇을 어떻게 넣는가
- 무엇을 어떻게 보존하는가
- 어떤 trace를 남기는가
- 어떤 구조를 추가하는가
- 어떤 기능을 붙이는가

이다.

### B. line reading layer

이 층은 이미 만들어진 공간을 다시 읽는다.

여기서 다루는 것은:

- 어떤 반복이 살아남는가
- 어떤 선이 목적어를 바꿔도 유지되는가
- 어떤 선이 다른 폴더/자료/코드로 옮겨가도 응결하는가
- 어떤 응결이 hub로 떠오르는가
- 어떤 선이 아직 annotation 수준인지
- 어떤 선이 reusable operator 쪽으로 가는지

즉 이 층의 질문은:

- 무엇이 line인가
- 이 line은 어디서 두꺼워지는가
- 같은 line을 어디에 다시 대입해야 하는가
- 무엇이 아직 흔적이고 무엇이 잠정 line인가

이다.

---

## 2. why this split is necessary

현재까지의 문제는 자주 아래처럼 섞였기 때문이다.

- 구조를 조금 만들면 곧바로 line처럼 읽음
- 한두 번 반복되면 hub 후보처럼 이름 붙임
- reread보다 lock이 먼저 붙음
- 기능 구현 결과를 line material로 다시 못 올림

즉 공간 생성과 line 관찰이 섞이면
둘 다 얕아진다.

- 공간 생성은 빨리 규정되고
- line 관찰은 빨리 수렴된다

그래서 먼저 층을 나눠야 한다.

---

## 3. relation between the two layers

이 둘은 분리되지만 단절되지는 않는다.

순서는 아래처럼 읽는 것이 맞다.

1. space construction layer에서 재료/trace/기능/기록이 생성된다
2. line reading layer가 그 생성물을 반복 reread한다
3. reread 결과가 어떤 line을 두껍게 했는지 본다
4. 그 결과가 다시 다음 공간 생성에 반영된다

즉 관계는:

`space construction -> line reading -> reread result -> next space construction`

이다.

이 순환이 있어야 공간이 숙성된다.

---

## 4. what belongs to space construction

아래는 construction layer 쪽으로 먼저 읽어야 한다.

- 새 입력 추가
- reference 정리
- runtime trace 경로 추가
- view / panel / surface 추가
- 기능 구현
- 기능 변경 이유 기록
- provenance / receipt / manifest 보강
- calibration lane 조정

즉 “무엇을 만들었는가”와 “무엇을 남겼는가”는 construction layer다.

---

## 5. what belongs to line reading

아래는 line reading layer 쪽으로 먼저 읽어야 한다.

- 같은 표현/반복/긴장의 재등장
- latent line의 재출현
- 목적어 전환 reread
- cross-folder reread
- cross-code reread
- line thickening 여부
- hub condensation 여부
- philosophy fit / mismatch

즉 “무엇이 살아남는가”와 “무엇이 응결하는가”는 line reading layer다.

---

## 6. operational rule

앞으로는 아래처럼 움직이는 것이 맞다.

### when building

- 먼저 construction layer로 기록한다
- 바로 line verdict를 붙이지 않는다
- 변경 이유까지 재료로 남긴다

### when reading

- construction 결과를 line reading layer에서 다시 본다
- 한 번 읽고 끝내지 않는다
- 같은 line을 다른 목적어와 다른 폴더에 최소 여러 번 대입한다
- 그 뒤에도 남는 것만 잠정 line으로 본다

---

## 7. current practical reading order

현재는 아래 읽기 순서가 맞다.

1. `inputs / source_assets / references / runtime trace`를 construction 결과로 본다
2. `latent line / reread map / external entry`를 line reading 입구로 잡는다
3. 같은 line을 `business / feature / product / implementation` 등으로 다시 읽는다
4. 필요하면 새 기능/새 기록/새 이유 trace를 construction layer에 다시 넣는다

즉 먼저 만들고, 그 다음 reread하고, 그 결과로 다시 만든다.

---

## 8. what this corrects

이 split는 아래를 바로잡기 위한 것이다.

- line을 너무 빨리 선언하는 습관
- lock을 reread보다 먼저 붙이는 습관
- 기능 변경 이유를 코드 diff 뒤에 버리는 습관
- 공간 전체보다 현재 task 목적어만 따라가는 습관

---

## 9. one-line summary

앞으로는
`공간을 만드는 층`과 `그 공간을 읽는 line 층`을 분리해서 본다.

공간 생성은 재료와 흔적과 기능을 남기는 일이고,
line 읽기는 그 생성물을 반복 reread하며
어떤 선이 살아남고 두꺼워지고 응결하는지 보는 일이다.

둘은 다르지만,
계속 서로를 다시 먹이며 순환해야 한다.

