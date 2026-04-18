# operating ui payload / adapter adequacy review v1

## 1. verdict

현재 `process-console payload -> OperatingUiPayloadAdapter -> read-only operating shell` 경로는
**v1 baseline을 지탱하기에는 충분하다**.

다만 이 충분성은
- 기능적으로 충분하다는 뜻이지
- 모든 surface가 정보적으로 풍부하다는 뜻은 아니다.

즉 지금 상태는:
- baseline read-only shell에는 adequate
- guarded extension과 future richer surface에는 아직 intentionally thin

## 2. surface adequacy summary

### 2-1. Live Control Bar

#### 현재 데이터로 충분한 것

- `requested asset`
- `current shown asset`
- `selection_query_state`
- `live_availability`
- selectable asset list

즉 control bar는
현재 selection source와 fallback 여부를 설명하는 데 필요한 최소 데이터는 이미 갖고 있다.

#### 얇지만 허용 가능한 것

- asset list가 `id/title` 수준에 머문다
- source meta는 `live` / `process_console_payload` 정도의 얇은 표기다

이건 현재 목적이 제어와 상태 설명이지
탐색/검색/운용 분류가 아니므로 허용 가능하다.

#### 앞으로 확장 시 부족해질 것

- asset grouping
- richer source/origin meta
- selection provenance history

하지만 이건 baseline 범위를 벗어난다.

### 2-2. Derived State Strip

#### 현재 데이터로 충분한 것

- latest preview
- diff summary
- attention summary
- memory summary
- selected asset canonical badge 일부

즉 strip은 “지금 선택한 대상의 핵심 상태를 한 줄로 읽기” 목적엔 충분하다.

#### 얇지만 허용 가능한 것

- diff는 `diffClass / changed count / provenance only` 수준에 머문다
- attention은 selected asset 기준 한 항목 요약만 있다
- memory는 `summary / density / dominant shifts`의 얇은 read model이다

이건 strip이 detail surface가 아니라는 점에서 허용 가능한 얇음이다.

#### 앞으로 확장 시 부족해질 것

- richer diff lineage
- attention lifecycle nuance
- memory trend over time

### 2-3. Asset State Board

#### 현재 데이터로 충분한 것

- asset id/title
- packet texture
- maturation
- traceability
- emergence
- updatedAt

즉 board는 “무엇을 선택할지”를 고르는 최소 surface로는 충분하다.

#### 얇지만 허용 가능한 것

- grounding이 기본 surface에 없다
- compare/attention hint를 기본 card에 싣지 않는다

이건 board가 선택면이지 해석면이 아니라는 baseline 절제와 맞는다.

#### 앞으로 확장 시 부족해질 것

- board-level grouping/filter semantics
- grounding visibility
- richer selection rationale

### 2-4. Selected Detail Summary

#### 현재 데이터로 충분한 것

- title/subtitle
- canonical rows
- latest summary
- diff/attention/memory 요약
- compare summary 일부
- updated meta

즉 modal 없이도 selected asset 상태를 조금 더 풍부하게 읽게 하는 현재 목적에는 충분하다.

#### 얇지만 허용 가능한 것

- `createdAt`은 없다
- evidence refs는 summary panel에서 거의 쓰이지 않는다
- dependency / blocker / history는 quiet summary 수준이다

이건 detail summary가 full explorer가 아니므로 허용 가능하다.

#### 앞으로 확장 시 부족해질 것

- richer blocker semantics
- scope/dependency explanation depth
- evidence trace surface

### 2-5. Compare Candidate Panel

#### 현재 데이터로 충분한 것

- compare candidate 존재 여부
- candidate asset id
- compare reason

즉 “selected asset 주변에 compare candidate가 붙어 있다”는 보조 힌트 수준은 유지된다.

#### 얇지만 허용 가능한 것

- title richness가 없다
- count는 있으나 정보 밀도를 크게 높이지 않는다
- reason이 짧으면 의미도 얇다

이 얇음은 현재 panel을 guarded extension으로 두는 핵심 근거다.

#### 앞으로 확장 시 부족해질 것

- candidate title/meta richness
- why-this-candidate relation thickness
- richer compare context

중요:
- 이 부족함은 지금 당장 UI를 더 만들어야 한다는 뜻이 아니라
  panel이 왜 아직 baseline이 아닌지를 설명하는 근거다.

### 2-6. Activity Panel

#### 현재 데이터로 충분한 것

- recent activity rows
- latest lineage summary
- recent trigger/reason hint
- history unavailable fallback

즉 activity는 “최근 무슨 일이 있었는지”를 읽는 목적엔 충분하다.

#### 얇지만 허용 가능한 것

- compare index는 있지만 deep drilldown은 없다
- activity row는 reason/trigger 중심으로 얇다
- diff hint도 summary 수준이다

이건 read-first panel이라는 목적과 맞는다.

#### 앞으로 확장 시 부족해질 것

- richer time formatting
- grouped activity semantics
- diff lineage threading

## 3. payload / adapter adequacy summary

### 3-1. 현재 adapter/model이 shell을 무리 없이 지탱하는가

판정:
- yes

이유:
- adapter가 raw process-console payload를
  shell이 실제로 소비하는 read model로 잘 잘라냈다
- component들은 raw payload를 직접 읽지 않는다
- fallback/null normalization도 일관된다

즉 현재 UI의 안정성은
payload richness보다도 **adapter boundary 안정성**에서 더 많이 나온다.

### 3-2. 어디서 payload richness 부족이 얇음으로 드러나는가

주요 지점:

1. `boardItems`
- packet/maturation/traceability/emergence 정도만 있어
  board가 intentional thin selection surface로 유지된다

2. `selectedAsset`
- summary panel에는 충분하지만
  full detail surface로 보기엔 일부 meta가 얇다

3. `compareCandidates`
- 현재 `assetId + reason`만 있어
  compare panel이 보조 힌트 수준에 머무른다

4. `activityPanel`
- read-first recent activity에는 충분하지만
  thread-like exploration에는 부족하다

### 3-3. compareCandidates가 왜 보조 힌트 수준에 머무는가

핵심 이유:

- existing model이 `assetId`와 `reason` 중심이다
- relation richness가 얇다
- candidate title/meta를 별도로 주지 않는다
- ranking/score 없이 deliberately flat하다

즉 compare panel이 얇은 이유는
단순히 UI가 덜 만들어져서가 아니라,
현재 engine/process-console payload 쪽 compare candidate surface가
**의도적으로 hint-level richness**에 머물러 있기 때문이다.

## 4. intentional thinness vs future enrichment

### intentional thinness로 보는 것이 맞는 것

- board card의 grounding 생략
- strip의 diff/attention/memory 얇은 요약
- detail summary의 modal 미승격 상태
- compare panel의 `assetId + reason` 수준
- activity panel의 read-first recent history tone

이건 지금 baseline의 절제와 맞다.

### future enrichment 후보로 볼 수 있는 것

- compare candidate title/meta richness
- board-level grounding visibility
- history lineage summary thickness

중요:
- 이 후보들은 지금 당장 구현해야 할 부족함이 아니라
  엔진 쪽에서 later-stage enrichment가 가능할 수 있는 위치다.

## 5. candidate engine-side enrichments

후보는 3개 이하로만 남긴다.

### candidate 1. compare candidate label enrichment

- 현재 `assetId + reason` 외에
  selected asset 옆에서 읽기 좋은 최소 display label/meta를
  engine/process-console 쪽에서 제공할 수 있는지 검토 후보

### candidate 2. board-facing grounding hint

- board baseline을 해치지 않는 선에서
  grounding을 full row가 아니라 quiet hint 수준으로 surface할 수 있는지 검토 후보

### candidate 3. history lineage compact richness

- activity panel이 deep explorer로 커지지 않으면서도
  latest lineage summary를 조금 더 안정적으로 읽게 할 수 있는 compact enrichment 후보

## 6. recommendation

추천 중심축:
- **payload/model observation 계속**이 먼저다

이유:
- 현재 baseline shell은 already adequate 하다
- 지금 부족해 보이는 것 중 많은 부분은
  실제로는 baseline 절제의 일부다
- 따라서 다음 단계는 즉시 engine-side proposal로 뛰기보다,
  어떤 얇음이 intentional인지, 어떤 얇음이 실제로 자주 문제를 만드는지
  observation memory를 더 쌓는 편이 맞다

즉:
- 바로 engine-side enrichment proposal로 넘어가기보다
- **운용 관찰을 한 번 더 누적한 뒤**
  정말 필요한 enrichment만 좁게 제안하는 순서가 더 적절하다

## 7. concise lock

한 줄로:
- 현재 process-console payload와 adapter는 operating UI v1 baseline을 지탱하기엔 충분하고, 지금 보이는 얇음의 상당수는 결함이 아니라 **의도된 baseline 절제**이며, future enrichment는 observation 누적 후 좁게 검토하는 편이 맞다.
