# right-column compare panel minispec v1

## 1. verdict

구현 진행 가능.

단, 이 패널은 계속 **guarded extension**으로 취급한다.
즉 구현 자체는 가능하지만,
이 mini-spec에서 잠근 범위를 넘기면 baseline 경계를 흔들 수 있으므로
first-pass는 여기 적힌 범위 안에서만 허용한다.

## 2. panel purpose

한 줄 목적:
- `selected asset` 옆에서 **compare candidate를 얇게 읽게 해주는 read-only comparison aid**

이 패널이 돕는 것:
- selected asset 주변에 어떤 compare candidate가 있는지 읽기
- compare reason을 짧게 확인하기
- compare candidate가 없을 때도 그 부재를 조용히 이해하기

이 패널이 하지 않는 것:
- 새 해석면이 되기
- ranking/recommendation 주기
- full diff explorer 역할 하기
- evidence drilldown 열기
- deep workflow 진입면 되기

## 3. first-pass scope

### 표시 허용

- compare candidate count
- compare candidate asset id
- compare candidate title
  - 단, title이 없으면 asset id fallback 허용
- compare reason
- quiet helper
  - 예: `no compare candidates`
  - 예: `compare candidates unavailable`

### 표시 금지

- full diff rows
- evidence drilldown
- score / rank / priority number
- recommendation wording
- “best match”류 문구
- 과한 CTA
- modal open affordance
- workflow/action button

## 4. panel states

### state A. compare candidates present

구조:
- panel title
- candidate count
- candidate list
  - `title or asset id`
  - `reason`

문구 톤:
- neutral
- descriptive only

예:
- `2 compare candidates`

### state B. compare candidates empty

구조:
- panel title
- quiet helper 한 줄

문구:
- `no compare candidates`

주의:
- “비교할 가치가 없음” 같은 해석 금지

### state C. no selected asset

구조:
- panel title
- helper 한 줄

문구:
- `select an asset to inspect compare candidates`

주의:
- query 오류 설명은 하지 않는다

### state D. live unavailable

구조:
- panel title
- helper 한 줄 또는 panel suppressed

문구:
- `compare candidates unavailable`

주의:
- 주 설명은 control bar / page fallback이 담당한다
- 이 패널이 unavailable의 주 설명면이 되지 않는다

### state E. state unavailable

의미:
- selected asset는 있으나 canonical state가 없음

first-pass 원칙:
- compare panel은 selected asset canonical state가 unavailable이면
  기본적으로 quiet helper만 둔다

문구:
- `compare candidates unavailable`

주의:
- state unavailable 설명 자체는 detail summary가 담당한다

## 5. surface boundary

### vs Selected Detail Summary

- detail summary는 selected asset 자체의 상태 요약
- compare panel은 selected asset 주변의 compare candidate만 보조적으로 표시
- compare reason은 보여줄 수 있지만,
  selected asset의 canonical state 요약을 다시 반복하지 않는다

### vs Activity Panel

- activity panel은 lineage/history hint
- compare panel은 comparison candidate hint
- activity/time/history vocabulary를 compare panel에 섞지 않는다

### why right-column secondary

이 위치가 맞는 이유:
- compare candidate는 board 전역 선택면이 아니라
  selected asset reading 보조층이기 때문이다
- detail summary 바로 아래 또는 activity 위쪽에 놓이면
  “selected asset -> compare candidates -> recent activity” 순서가 자연스럽다
- board 아래 full-width row보다 의미가 덜 퍼진다

## 6. data usage

### first-pass data source

현재 existing model:
- `compareCandidates[]`
  - `assetId`
  - `reason`

### first-pass sufficiency

- yes, 최소 panel은 existing `compareCandidates`만으로 가능하다
- title이 없으면 asset id만으로도 충분하다

### first-pass model rule

adapter untouched 기준 최소 모델:
- `count = len(compareCandidates)`
- each item:
  - `assetId`
  - `displayLabel = reason if needed? no`
  - `title = assetId fallback`
  - `reason`

주의:
- first pass에서는 title enrichment를 요구하지 않는다
- richer title/meta는 이후 guarded review로 분리한다

## 7. interaction policy

### baseline stance

- read-only

### click policy

first-pass 권장:
- 기본은 no-op
- 또는 아주 얕은 navigation only를 future option으로 언급 가능

하지만 this minispec 기준:
- **first pass는 clickable deep workflow를 포함하지 않는다**

이유:
- compare candidate를 recommendation surface처럼 보이게 만들 위험이 있기 때문이다
- panel purpose가 reading aid인지 흐려질 수 있다

## 8. gate check

### why still guarded extension

- 새 panel 추가 자체가 shell 범위를 넓힌다
- detail/activity와 의미 경계가 가까워 overlap risk가 있다
- compare candidate가 recommendation처럼 읽히는 순간 baseline 의미가 변질될 수 있다

### approval points before implementation

1. panel placement를 right-column secondary로 고정할 것
2. first pass는 existing `compareCandidates`만 사용할 것
3. first pass interaction은 no-op/read-only로 제한할 것
4. unavailable/state-unavailable에서는 quiet helper만 둘 것

### maximum allowed first-pass implementation

허용 최대 범위:
- read-only panel 1개
- title + count + simple candidate rows + helper text
- no adapter contract change
- no route/query change
- no click workflow
- no ranking/recommendation language

## 9. recommendation

구현 진행 가능.

이유:
- 범위를 여기까지 좁히면 baseline을 흔들지 않고도 들어갈 수 있다
- existing `compareCandidates`만으로 최소 panel이 가능하다
- right-column secondary로 제한하면 surface responsibility도 유지하기 쉽다

## 10. summary

한 줄로:
- `right-column compare panel`의 first pass는 **selected asset 옆에서 compare candidate를 조용히 읽게 하는 read-only aid**로만 구현 가능하며,
  그 이상은 guarded extension 범위를 넘는다.
