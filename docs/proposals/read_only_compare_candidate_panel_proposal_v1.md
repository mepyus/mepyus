# read-only compare candidate panel proposal v1

## 1. verdict

조건부 추천.

`read-only compare candidate panel`은 현재 v1 baseline에 바로 포함할 safe refinement는 아니고,
**guarded extension**으로 다루는 것이 맞다.

이유:
- 새 read-only panel 추가에 해당한다
- 현재 `Selected Detail Summary`와 `Activity Panel` 사이의 책임 경계를 흔들 수 있다
- adapter/model contract touch 가능성이 있다

즉:
- 구현 자체가 금지 대상은 아니지만
- 구현 전에 surface responsibility와 contract 영향 범위를 먼저 잠가야 한다

## 2. proposal summary

현재 shell은 아래는 충분히 읽힌다.
- 어떤 asset를 보고 있는가
- 그 asset의 latest/diff/attention/memory는 어떤가
- 최근 activity/history hint는 무엇인가

하지만 아직 비어 있는 부분은 있다.
- selected asset와 연관된 compare candidate가 무엇인지
- compare candidate가 단순 related asset인지, 비교 근거가 있는 reading aid인지
- 선택 대상 주변의 비교 맥락이 어디까지 안전하게 읽힐 수 있는지

따라서 compare candidate panel은
**새 해석면**이 아니라
`selected asset` 읽기를 보조하는
**read-only comparison aid**
로만 제안되어야 한다.

## 3. why this panel may be needed

현재 shell의 빈 지점:
- `Selected Detail Summary`는 compare candidate를 top-3 summary 정도로만 얇게 포함한다
- `Activity Panel`은 lineage/activity hint만 담당한다
- `Asset State Board`는 전체 대상 선택면이지 compare 관계 요약면이 아니다

즉 compare candidate panel이 추가되면:
- selected asset를 읽을 때
- 왜 이 asset 옆에 어떤 candidate가 같이 보이는지
- 비교 근거가 있는 candidate가 있는지
를 더 명확하게 읽을 수 있다

하지만 이 패널은:
- compare explorer가 아니다
- diff browser가 아니다
- recommendation engine이 아니다

## 4. surface responsibility

### may show

- compare candidate asset id / title
- compare reason label
- candidate count
- selected asset 대비 “compare available” 정도의 helper
- compare candidate가 없을 때의 empty helper

### should not show

- full diff rows
- evidence drilldown
- candidate selection algorithm 설명
- ranking narrative
- recommendation wording
- “better/worse/more important” 같은 평가성 language

### responsibility boundary

#### vs Selected Detail Summary
- detail summary는 selected asset의 상태 요약면이다
- compare candidate panel은 selected asset 주변의 비교 후보만 보조적으로 읽게 한다
- detail summary 안의 `compareSummary`를 더 풍부하게 분리한 panel이지,
  detail summary 자체를 대체하지 않는다

#### vs Activity Panel
- activity panel은 lineage/history hint면이다
- compare candidate panel은 비교 맥락면이다
- activity panel 안에 compare를 확장해서 넣지 않는다

## 5. placement comparison

### option A. right column, detail below

구성:
- 우측 상단: Selected Detail Summary
- 우측 중단: Compare Candidate Panel
- 우측 하단: Activity Panel

장점:
- selected asset 읽기 흐름 안에 자연스럽게 붙는다
- board와 detail/activity의 3영역 shell 논리를 해치지 않는다
- compare candidate를 selected asset 보조층으로 유지하기 쉽다

단점:
- 우측 column이 길어질 수 있다
- activity panel 가시성이 약해질 수 있다

### option B. board 아래 full-width secondary row

구성:
- 상단/좌측/우측 기존 유지
- board 아래 또는 page 하단에 compare candidate row

장점:
- detail/activity 영역을 덜 건드린다
- candidate 목록이 길어져도 배치 부담이 적다

단점:
- selected asset 보조층이라는 성격이 약해진다
- board/selected reading의 시선 흐름이 분리된다

### recommended option

추천:
- **option A**

이유:
- compare candidate는 board의 전역 정보가 아니라
  `selected asset` 읽기 보조층으로 읽히는 편이 더 자연스럽다
- 따라서 우측 column 내부의 secondary panel이 baseline shell과 가장 덜 충돌한다

## 6. data contract impact

### what already exists

현재 adapter/model에는 이미 아래가 있다.
- `compareCandidates`
  - `assetId`
  - `reason`

즉 **최소 panel** 수준이라면 지금도 data는 있다.

### what is still thin

현재 부족한 점:
- title/label fallback richness 부족
- candidate count/section summary 부재
- candidate가 현재 selected asset와 어떤 관계인지 설명하는 meta 부재

### contract touch judgment

현재 제안 기준:
- **v1 proposal에서는 adapter contract touch 없이 시작 가능**
- panel이 정말 필요해지면 first pass는 existing `compareCandidates`만 사용
- 이후 panel이 너무 빈약하면 guarded adapter touch를 별도 review로 분리

즉:
- 구현 1차는 no-contract-touch 가능
- richer version은 contract touch 검토 필요

## 7. gate judgment

### why not safe refinement

- 새 panel 추가 자체가 baseline surface 범위를 넓힌다
- detail/activity와 역할 충돌 가능성이 있다
- compare candidate가 “읽기 보조”를 넘어서 “새 해석면”으로 비대화할 위험이 있다

### why not baseline-changing work

- write/action capability를 도입하지 않는다
- state axis/vocabulary를 바꾸지 않는다
- raw payload direct read를 도입하지 않는다
- read-only shell 내부에서의 추가 panel이기 때문이다

### approval points needed before implementation

1. compare candidate panel을 read-only comparison aid로 제한할 것
2. right column secondary panel로 둘지 확정할 것
3. first implementation은 existing `compareCandidates`만 사용할지 결정할 것
4. contract touch가 필요하면 별도 review로 분리할 것

## 8. implementation risk preview

### route/query contract impact

- 기본적으로 없음
- panel open/close query를 새로 만들면 그 순간 guarded risk가 올라간다

### builder/adapter touch

- minimum version은 adapter touch 없이 가능
- richer version은 adapter field 확장 필요 가능

### vocabulary/semantics pollution risk

- compare candidate를 recommendation처럼 보이게 만들면 안 된다
- `selected asset`과 `compare candidate`의 우선순위를 섞으면 안 된다
- `activity`와 `compare` 책임을 섞으면 shell이 무거워진다

### unavailable/empty state risk

- `compareCandidates=[]`일 때 quiet empty helper가 필요하다
- `live_unavailable`에서는 panel 자체를 설명하지 말고 page/control fallback에 따르는 편이 안전하다
- `state_unavailable`에서는 compare panel을 과도하게 빈 패널로 만들지 않도록 조건부 숨김 또는 neutral helper가 필요하다

## 9. recommendation

조건부 추천.

추천 이유:
- 현재 shell의 빈 지점을 메우는 데는 유의미하다
- 하지만 baseline에 그냥 붙이기엔 responsibility overlap risk가 있다
- 따라서 다음 단계로 바로 구현보다,
  먼저 `right column secondary compare panel`이라는 제한된 형태로
  별도 mini-spec을 한 번 더 잠근 뒤 들어가는 편이 맞다

## 10. summary

한 줄로:
- `read-only compare candidate panel`은 baseline을 깨는 작업은 아니지만,
  **selected asset 읽기 보조층으로 엄격히 제한하지 않으면 의미가 쉽게 비대해지는 guarded extension**이다.
