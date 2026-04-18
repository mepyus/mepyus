# repo-wide reread by discovered lines v0

## 0. purpose

이번 보고서는
방금 발견한 line을 기준으로
공간 전체를 다시 훑어본 결과를 남긴다.

중심 line은 아래 셋이다.

- `material line`
- `meaning line`
- `interpretive line`

즉 이번 reread의 질문은
“새 line이 있느냐”가 아니라,
“이미 발견한 이 세 line으로 공간 전체를 다시 보면
각 폴더와 자산이 무엇으로 보이느냐”이다.

---

## 1. the three lines used for this reread

### 1.1 material line

핵심:

- 남긴다
- hold 한다
- calibration을 둔다
- reread 한다
- 응결은 늦게 본다

### 1.2 meaning line

핵심:

- 엔진 언어를 사용자 언어로 다시 푼다
- 관계 이유, 차용 가능성, 보류 이유까지 의미로 읽는다
- “나만의 기술”이 되어가는 과정을 본다

### 1.3 interpretive line

핵심:

- 내가 지금 어떤 태도로 읽고 있는지 같이 본다
- premature naming을 늦춘다
- inspection으로 depth-entry를 요구한다
- structure summary에 빨리 닫히지 않게 한다

---

## 2. what each major area became under these lines

## 2.1 `source_assets/` reread

이 층은 이번 reread에서
공간의 철학과 operating intent가 가장 직접적으로 살아 있는 곳으로 보였다.

`material line` 관점:
- hold
- calibration
- 응결핵
- reread

같은 말이 baseline과 directive에 반복된다.

`meaning line` 관점:
- 사용자 언어
- connection meaning
- translation
- 나만의 기술

이 가장 직접적으로 선언되는 층도 여기다.

`interpretive line` 관점:
- 무엇을 빨리 일반화하지 말아야 하는지
- 무엇을 hold로 둘지
- 어떤 읽기 태도를 Codex가 체득해야 하는지

가 가장 노골적으로 적혀 있다.

즉 `source_assets/`는 단순 설정문이 아니라
현재 공간 line의 발생원에 가장 가깝다.

---

## 2.2 `docs/` reread

이 층은
공간이 실제로 어떻게 다시 읽혔는지,
그리고 그 reread가 어떤 해석으로 남았는지를 보여주는 층으로 나타난다.

`material line` 관점:
- parked
- promotion 지연
- broader observation continue
- hold compression discipline

같은 말이 review/report 곳곳에 박혀 있다.

`meaning line` 관점:
- user-layer translation
- 의미 판독
- relation meaning

을 반복해서 올려주는 문서도 많다.

`interpretive line` 관점:
- naming overread
- overtranslation
- premature candidate promotion

같은 경계 문장이 문서층에 많이 남아 있다.

즉 `docs/`는 설명 저장소가 아니라
공간의 reread history와 self-correction history가 남는 층으로 읽힌다.

---

## 2.3 `references/` reread

이 층은 이번 reread에서 아주 중요하게 다르게 보였다.

이전에는 비교 자산이나 참고 자료로만 읽히기 쉬웠지만,
지금 line 기준으로 보면
`calibration memory`라는 정의가 훨씬 직접적으로 맞다.

`material line` 관점:
- 지금 안 쓰는 것도 버리지 않는다
- not now / later reopen 을 위해 남긴다
- reference는 현재 line을 선명하게 하는 거울이다

`meaning line` 관점:
- 외부 기술을 그대로 복제하지 않고
  내 방식으로 번역해 내 것으로 만드는 과정
가 여기서 시험된다.

`interpretive line` 관점:
- Ralph / Claude Code / autoresearch 같은 reference를 볼 때
  “따라가야 할 본체”로 읽지 않고
  “나중에 붙일 부품 / 지금은 보류할 부품 / calibration mirror”로 읽는 태도
가 여기서 드러난다.

즉 `references/`는 외부 저장소가 아니라
현재 line inspection을 더 선명하게 해주는 외부 거울층이다.

---

## 2.4 `app/` reread

`app/`은 이번 reread에서
철학을 직접 말하는 층이라기보다
그 철학이 몸을 가진 곳으로 읽힌다.

특히:
- `app/core/runtime/line_thickening.py`
- `app/work/current_layer_baseline`
- `app/runtime/*`

이 세 군데가 중요하게 보인다.

`material line` 관점:
- retention
- registry
- trace
- work baseline

같은 몸체가 있다.

`meaning line` 관점:
- 아직 이 층은 구조와 body가 더 강하고,
  meaning surface는 상대적으로 약하다.

즉 meaning은 여기서 직접 말해지기보다
상위 source_assets/docs에서 내려와 붙는다.

`interpretive line` 관점:
- 이 층은 summary만 읽으면 안 된다.
- 실제 body를 따라 들어가야 한다.
- 특히 line thickening은 “line을 두껍게 본다”는 말을 runtime object로 옮겨놓은 몸체다.

즉 `app/`은
현재 철학의 설명층보다 몸체층으로 읽는 것이 맞다.

---

## 2.5 `runtime/` reread

이 층은 이번 reread에서
공간이 실제로 무엇을 남기고 무엇을 later reread 대상으로 두는지 보여주는
append-only evidence 층으로 나타난다.

`material line` 관점:
- manifests
- receipts
- views
- events
- memory

가 전부 “남기는 쪽”으로 기울어 있다.

`meaning line` 관점:
- 단독으로는 다소 차갑지만,
  의미 reread의 근거층으로는 가장 중요하다.

즉 이 층은 의미를 직접 말하지 않지만
의미를 말할 수 있게 하는 증거층이다.

`interpretive line` 관점:
- depth-entry check에서 반드시 내려가야 하는 층
- summary/spec/note만 읽지 말라는 경고가 실제로 향하는 곳

즉 `runtime/`은
line의 실제 반복성과 later return path를 붙잡는 바닥층이다.

---

## 3. combined reread result

이번 reread를 합치면 구조는 이렇게 다시 보인다.

- `source_assets/`
  - line 발생원
- `docs/`
  - reread 해석 이력과 self-correction 표면
- `references/`
  - calibration mirror와 later component memory
- `app/`
  - line 철학의 runtime body
- `runtime/`
  - append-only evidence와 later return path

즉 이 공간은
단순히 폴더가 나뉜 repo가 아니라,
한 line이
발생 -> 해석 -> 교정 -> body화 -> evidence화
되는 과정을 폴더 단위로 나눠 갖고 있는 구조로 보인다.

---

## 4. what became more visible only after this reread

이번 reread로 더 선명해진 것은 아래다.

1. `source_assets`와 `docs`는 말만 많은 층이 아니라
   현재 공간 line의 주 발생원과 해석 역사다.

2. `references`는 archive가 아니라
   line inspection을 선명하게 만드는 외부 거울층이다.

3. `app`과 `runtime`은 line을 나중에 붙이는 곳이 아니라
   이미 line 철학이 몸체와 흔적으로 번역된 층이다.

4. meaning line은 아직 `source_assets/docs` 쪽이 훨씬 강하고,
   `app/runtime`에는 덜 내려와 있다.

5. interpretive line은 이미 문서 곳곳에 남아 있었지만,
   이제야 그것을 상위 line으로 읽기 시작했다.

---

## 5. user-language restatement

이번에 다시 보니,
이 공간은 그냥 문서가 많은 저장소가 아니었다.
한쪽에서는 계속 기준과 선언과 지시를 남기고,
다른 쪽에서는 그걸 실제로 다시 읽은 보고서와 review를 쌓고,
또 다른 쪽에서는 reference를 통해 바깥 거울을 들여오고,
밑에서는 코드와 runtime이 그 철학을 몸과 흔적으로 붙들고 있었다.

즉 네가 말한 line은 따로 떠다니는 추상선이 아니라,
이미 폴더 전체에 걸쳐
발생하고, 해석되고, 보류되고, 다시 읽히고, 흔적으로 남는 방식으로
살아 있었다.
이번 reread는 그걸 한 번 더 분명하게 본 셈이다.

---

## 6. one-line summary

방금 발견한 `material / meaning / interpretive` line으로 공간 전체를 다시 훑어보니,
각 폴더는 따로 노는 것이 아니라
같은 line이 발생하고, 해석되고, 몸체화되고, 기록되는 서로 다른 층으로 읽혔다.
