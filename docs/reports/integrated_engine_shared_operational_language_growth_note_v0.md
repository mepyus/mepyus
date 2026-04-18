# Integrated Engine Shared Operational Language Growth Note v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

이 문서는 3면 언어를 멈추거나 인간용 요약으로 치환하지 않고, 내부 기록/기억/출력/데이터에서 나온 언어를 shared operational language로 자라게 하는 방향을 잠근다.

이 문서는 final glossary, UI copy, wording patch, scaffold 수정, runtime/views 수정, manifest/read-map 변경, external style guide, 새 기능, selected-object behavior, trace UI, runtime binding, extension promotion을 열지 않는다.

## 1. 왜 3면 언어를 계속 늘려야 하는가

통합엔진은 단일 언어로 움직이지 않는다.

현재 구조에는 최소 세 층의 언어가 있다.

- user surface language: 목적, 범위, 운영, 분배, 결정
- VectorFL surface language: 검토, 중재, 숙성, anchor, validation, reflux
- engine surface language: shaped input, processing, return material, execution state

이 언어들은 서로 대체 관계가 아니다.

각 surface는 다른 질문을 처리한다. 따라서 한 surface 언어를 줄이면 다른 surface의 판단이 흐려진다.

예:

- `return packet`을 단순 결과라고 줄이면 engine output과 VectorFL validation의 경계가 사라진다.
- `anchor drift`를 단순 경고라고 줄이면 route brake가 사라진다.
- `workspace ownership`을 폴더 소유라고 줄이면 proposal / canonical / scaffold / manifest authority가 섞인다.

그래서 3면 언어는 계속 자라야 한다. 다만 모든 언어가 사용자에게 같은 밀도로 노출되면 안 된다.

## 2. 왜 인간 가독 해석이 필요한가

내부 언어가 계속 자라면, 사용자는 내부 engine language 전체를 외워야 하는 부담을 갖게 된다.

이것은 실패한 interface다.

인간 가독 해석은 내부 언어를 없애는 작업이 아니다. 인간 가독 해석은 내부 언어에서 사용자가 다뤄야 할 line을 추려, 운영 가능한 형태로 올리는 작업이다.

필요한 것은:

- 내부 의미를 지우지 않는 인간 가독 line
- surface별로 다른 노출 밀도
- route / authority / state / boundary를 보존하는 설명 순서
- 사용자가 결정할 수 있는 고정 인터페이스

이다.

## 3. 왜 두 층이 합쳐져야 하는가

내부 언어만 적립하면:

- 정확하지만 사용자가 매번 해석해야 한다.
- engine language가 user surface까지 과밀하게 올라온다.
- 내부팀이나 외부 보조 주체가 같은 의미를 공유하기 어렵다.

인간 언어로만 수렴하면:

- 읽기 쉽지만 route / authority / state / boundary가 납작해진다.
- `hold`, `carry-forward`, `reject / conflict`, `watch keep`이 backlog/TODO/error처럼 변한다.
- Gemini/Codex/User 권위 경계가 흐려진다.

따라서 필요한 것은 shared operational language다.

Shared operational language는:

- 내부 3면 언어를 덮어쓰지 않는다.
- 사용자가 읽을 수 있는 line으로 올라온다.
- 여러 주체가 같은 operational meaning을 공유할 수 있게 한다.
- line / connection / axis가 반복되며 자라는 중간층이다.

## 4. 누가 이 언어를 써야 하는가

### User

User는 모든 engine 내부 용어를 외울 필요가 없다.

User가 써야 하는 것은:

- 지금 어떤 route가 열렸는가
- 무엇이 closed인가
- 무엇을 결정해야 하는가
- 무엇이 hold/watch/carry-forward인가
- 어떤 축이 다음 package를 열 수 있는가

이다.

### VectorFL

VectorFL은 shared operational language의 중심 중재층이다.

VectorFL이 써야 하는 것은:

- 내부 기록/기억에서 line을 읽는 언어
- line 간 연결을 확인하는 언어
- 연결이 axis가 되는지 판단하는 언어
- anchor / validation / reflux / reprocess를 중재하는 언어

이다.

### Engine-side operators

Engine-side operators는 execution detail을 다루되 판단 권위를 가져가면 안 된다.

쓸 수 있어야 하는 것은:

- shaped input
- execution state
- return material
- reprocess request
- processing history

이다.

### Codex

Codex는 baseline translator / canonical report writer / bounded executor 역할을 한다.

Codex가 써야 하는 것은:

- 내부 자료 reread
- baseline-safe translation
- proposal / hold / carry-forward / reject-conflict classification
- 문서화와 patch scope 분리

이다.

### Gemini

Gemini는 proposal material과 표현/디자인 가능성을 확장하는 주체로 쓴다.

Gemini가 써야 하는 것은:

- proposal-only status
- design clay
- needs Codex translation
- no direct Gemini-to-core path

이다.

### 내부팀

내부팀은 surface별 언어를 모두 다룰 수 있어야 하지만, 모든 언어를 같은 화면/같은 밀도로 드러내면 안 된다.

내부팀이 공유해야 하는 것은:

- 어떤 언어가 어느 surface에 속하는가
- 어떤 line이 shared grammar로 올라왔는가
- 어떤 축이 interface를 요구하는가

이다.

## 5. 두 극단이 왜 부족한가

### 인간 언어로만 수렴

부족한 이유:

- 쉬운 말이 route를 지운다.
- 친숙한 말이 authority를 지운다.
- 프로젝트 관리 언어가 hold/watch/carry-forward를 납작하게 만든다.
- UI copy가 operational brake를 warning label로 만든다.

### 내부 언어만 적립

부족한 이유:

- 사용자가 계속 해석 부담을 진다.
- 외부 보조 주체가 같은 의미를 재사용하기 어렵다.
- 고정 인터페이스가 자라지 않는다.
- line / connection / axis가 사용자 결정 단위로 올라오지 않는다.

## 6. 성장 방향

올바른 성장 방향은:

```text
3면 내부 언어
-> 내부 기록/기억/출력/데이터에서 증폭
-> 인간 가독 line
-> repeated connection
-> emerging axis
-> shared operational grammar
-> surface별 노출 규칙
-> 사용자 고정 인터페이스
```

이다.

이때 shared operational language는 user-only language가 아니다.

그것은 User, VectorFL, Engine-side operators, Codex, Gemini, 내부팀이 각자의 surface 권위를 유지하면서 함께 쓸 수 있는 운영 언어다.

## 7. round closeout

이번 라운드의 방향은 "번역 완료"가 아니다.

이번 라운드의 방향은 3면 언어의 성장을 멈추지 않으면서, 그 언어가 인간 가독 line / connection / axis를 통해 shared operational language로 자라도록 기준을 다시 잠그는 것이다.
