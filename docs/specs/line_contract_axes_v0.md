# Line Contract Axes v0

## 1. Purpose

이 문서는 `라인`이라는 표현이 너무 두루뭉술해져서, 사용자면 / 벡터플면 / 엔진면 / CLI / Codex / Gemini가 서로 다른 방식으로 해석하는 문제를 줄이기 위한 첫 축 문서다.

이 문서는 다음 성격을 가진다.

- final schema 아님
- DB 설계 문서 아님
- canonical internal model 문서 아님
- 라인을 설명하기 위한 축 문서
- surface contract와 engine 해석 사이의 중간 기준 문서

목표는 하나다.

라인이라는 말을 버리지 않되, 라인이 최소 어떤 축을 가져야 덜 흔들리는지 설명 가능하게 만드는 것.

---

## 2. One-Line Lock

라인은 공간 안에서 재사용 가능한 읽기/작업 단위다.

다만 `라인`이라는 이름 하나만으로는 부족하므로, 각 line은 최소 아래 4축으로 함께 읽는다.

1. Origin Axis — 어디서 왔는가
2. Meaning Axis — 어떤 의미 종류인가
3. Operating Role Axis — 지금 무엇을 위해 쓰이는가
4. Maturity Axis — 얼마나 숙성된 상태인가

즉 앞으로 `라인`은 단순 문장 조각이 아니라, 원천 + 의미 + 운영 역할 + 성숙도를 가진 단위로 읽는다.

---

## 3. Why This Is Needed

현재 `라인`이라는 말은 너무 많은 것을 동시에 가리킬 수 있다.

예:

- 원문에서 잘라낸 조각
- 해석된 의미문장
- 관계 단위
- 기능 후보
- 검증 결과
- 환류 재투입 후보

이 상태로 두면 아래 문제가 생긴다.

- 사용자 요청이 애매해진다.
- 엔진이 잘못 해석할 수 있다.
- 벡터플면에서 line이 왜 중요한지 흐려진다.
- 구현팀/검증팀/외부서치팀이 서로 다른 “라인”을 상상한다.
- surface object contract도 line meaning이 흔들리게 된다.

즉 line을 더 구조적으로 설명해야 뒤쪽의 팀 흐름과 엔진 처리도 더 안정된다.

---

## 4. Shared Interpretation Rule

### Rule 1. `라인`은 사용자 표면 언어로 유지할 수 있다

사용자에게는 여전히 `라인`이라는 말을 쓸 수 있다.

예:

- 관련 라인을 가져와줘
- 기능 후보 라인을 먼저 보고 싶다
- 검증된 라인만 보고 싶다

이건 사용자 언어로는 여전히 유효하다.

### Rule 2. 내부적으로는 typed line으로 읽어야 한다

다만 surface / engine / CLI / working tools는 line을 단순 문자열로 읽으면 안 된다.

최소한 아래 축을 붙여 읽어야 한다.

- origin
- meaning
- operating_role
- maturity

즉 `라인`은 표면 용어이고, 그 아래에는 typed line interpretation이 있어야 한다.

---

## 5. Axis 1 — Origin Axis

### Role

이 라인이 어디서 왔는가를 설명하는 축이다.

### Why It Matters

이 축이 없으면 provenance가 사라진다. 그러면 엔진은 다음을 구분하지 못한다.

- 외부 원문에서 바로 온 것인지
- 내부 공간에서 이미 생성된 것인지
- 검증 후 다시 들어온 것인지
- 구현 결과에서 파생된 것인지

즉 같은 line처럼 보여도 신뢰도와 쓰임이 달라질 수 있다.

### Candidate Values

- `external_source`
- `internal_space`
- `validation_return`
- `implementation_output`
- `external_search_result`
- `manual_note`

### Example

- `llm wiki` 원문에서 직접 잘라낸 문장 → `external_source`
- 검증팀이 정리해서 다시 넣은 판단 문장 → `validation_return`
- 구현팀이 만든 샘플 코드에서 추출한 기능 설명 → `implementation_output`

### One-Line Lock

Origin Axis는 이 line의 provenance와 초기 신뢰 맥락을 설명하는 축이다.

---

## 6. Axis 2 — Meaning Axis

### Role

이 라인이 무슨 종류의 의미를 담고 있는가를 설명하는 축이다.

### Why It Matters

같은 라인처럼 보여도 실제 의미는 다를 수 있다.

예:

- 어떤 것은 주장이다.
- 어떤 것은 절차다.
- 어떤 것은 질문이다.
- 어떤 것은 기능 후보다.
- 어떤 것은 gap이다.
- 어떤 것은 판단이다.

이걸 구분하지 않으면 외부서치팀이 question line을 claim line처럼 쓰거나, 구현팀이 gap line을 feature spec처럼 오해할 수 있다.

### Candidate Values

- `claim`
- `procedure`
- `relation`
- `question`
- `gap`
- `feature_candidate`
- `judgment`
- `observation`

### Example

- “llm wiki는 context organization에 강하다” → `claim`
- “우리 공간에서 skill처럼 추출할 수 있다” → `feature_candidate`
- “qmd와 결합 시 어떤 단위가 안정적인가?” → `question`
- “기존 line translation 단계와 연결이 약하다” → `gap`

### One-Line Lock

Meaning Axis는 이 line이 현재 어떤 종류의 의미 단위인지 설명하는 축이다.

---

## 7. Axis 3 — Operating Role Axis

### Role

이 라인이 현재 운영에서 무엇을 위해 쓰이고 있는가를 설명하는 축이다.

### Why It Matters

같은 line도 지금 어느 팀/어느 단계에서 쓰이느냐에 따라 성격이 달라진다.

예:

- 내부팀 탐색 재료
- 외부서치 쿼리 재료
- 구현팀 설계 재료
- 검증팀 비교 재료
- 환류 재투입 후보

Meaning만으로는 부족하다. 운영 역할이 붙어야 “지금 왜 이 line을 보고 있는가”가 분명해진다.

### Candidate Values

- `internal_reading_material`
- `external_search_material`
- `implementation_material`
- `validation_material`
- `reingest_candidate`
- `user_summary_material`

### Example

- `llm wiki`의 context 구조 설명 line을 내부팀이 현재 탐색 중 → `internal_reading_material`
- 같은 line을 외부서치팀이 검색 키워드 확장용으로 사용 → `external_search_material`
- 검증팀이 accepted refs로 다시 넣기로 결정 → `reingest_candidate`

### One-Line Lock

Operating Role Axis는 이 line이 지금 어떤 작업 흐름 속에서 어떤 용도로 살아 있는지 설명하는 축이다.

---

## 8. Axis 4 — Maturity Axis

### Role

이 라인이 얼마나 숙성되었는가를 설명하는 축이다.

### Why It Matters

원문 조각과 검증이 끝난 판단 문장이 같은 무게로 다뤄지면 위험하다. 이 축은 line의 현재 상태를 읽게 해준다.

### Candidate Values

- `raw`
- `interpreted`
- `candidate`
- `validated`
- `held`
- `reflux_ready`

### Example

- 방금 외부 원문에서 잘라낸 line → `raw`
- 한 번 해석은 되었지만 아직 검증 전 → `interpreted`
- 구현팀으로 넘기기 좋은 후보 → `candidate`
- 검증팀이 통과시킨 line → `validated`
- 보류 중인 line → `held`
- 다시 공간에 넣을 준비가 된 line → `reflux_ready`

### One-Line Lock

Maturity Axis는 이 line이 현재 얼마나 가공/검증/숙성된 상태인지 설명하는 축이다.

---

## 9. Minimal Typed Line Interpretation v0

지금 단계에서 line을 더 명확히 설명하려면, 최소 아래 네 칸이 있으면 된다.

- `origin`
- `meaning`
- `operating_role`
- `maturity`

문장으로 쓰면:

> 이 line은 어디서 왔고(origin), 어떤 의미 종류이며(meaning), 지금 무엇을 위해 쓰이고 있고(operating_role), 어느 정도 숙성됐는가(maturity).

---

## 10. Example Interpretations

### Example A

문장:

> llm wiki는 context organization에 강하다

해석:

- origin: `external_source`
- meaning: `claim`
- operating_role: `internal_reading_material`
- maturity: `interpreted`

### Example B

문장:

> llm wiki와 qmd를 결합하면 skill-like extraction 흐름을 만들 수 있다

해석:

- origin: `internal_space` 또는 `validation_return`
- meaning: `feature_candidate`
- operating_role: `implementation_material`
- maturity: `candidate`

### Example C

문장:

> qmd 관련 line은 현재 검증 기준이 약하다

해석:

- origin: `validation_return`
- meaning: `gap`
- operating_role: `validation_material`
- maturity: `validated` 또는 `held`

---

## 11. How This Helps Requests

이 축이 생기면 사용자 요청도 더 정교해진다.

예전:

- “llm wiki 관련 라인 좀 뽑아줘”

축 이후:

- “llm wiki 관련 line 중에서 기능 후보 성격의 line을 먼저 보여줘”
- “외부서치에 쓸 거니까 question / relation line 위주로 보여줘”
- “구현팀에 넘길 거니까 validated 또는 candidate maturity line만 보여줘”
- “검증팀 관점에서 hold 상태 line만 따로 묶어줘”

즉 사용자 언어가 엔진이 분류 가능한 요청으로 조금씩 변환 가능해진다.

---

## 12. Surface-Level Use

### User Surface

사용자면에서는 line을 직접 세부 축으로 다 보여주지 않아도 된다. 하지만 목적/팀 instruction을 만들 때 뒤에서는 어떤 종류의 line을 원하는지 구분 가능해야 한다.

예:

- 기능 후보 line 요청
- validation-ready line 요청
- external search material line 요청

### VectorFL Surface

벡터플면에서는 이 축이 가장 중요하다. 현재 line atlas / gap / genealogy가 단순 시각적 구조가 아니라 실제 흐름 의미를 가지려면 line 축이 필요하다.

### Engine Surface

엔진면에서는 ingest / pipeline / validation return과 line 축이 연결된다. 특히 환류나 검증 재투입 시, 어떤 line을 다시 넣고 어떤 line을 hold할지 분명해진다.

---

## 13. Explicitly Excluded For Now

이 문서는 아직 아래를 다루지 않는다.

- 최종 line schema
- DB field name 고정
- line scoring system
- line embedding / vector rule
- line mutation command
- 자동 line 강화/병합/삭제 정책
- line과 paragraph/segment의 최종 관계 설계

즉 지금은 축 문서이지, 구현 명세 문서가 아니다.

---

## 14. Open Questions

- `meaning` 후보를 지금 수준으로 둘지 더 쪼갤지
- `operating_role`을 팀 기준으로 둘지 더 추상화할지
- `maturity`가 validation 중심인지, broader lifecycle 중심인지
- origin과 provenance metadata를 어디까지 분리할지
- surface에 어느 축을 직접 노출하고 어느 축은 내부 해석용으로 둘지

---

## 15. One-Line Final Lock

라인은 더 이상 막연한 단일 표현으로 두지 않고, Origin / Meaning / Operating Role / Maturity의 최소 4축으로 함께 읽는 재사용 가능한 공간 단위로 해석한다.
