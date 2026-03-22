[[A]] [[OBJ:codex_impl_spec]] [[SEM:semantic_terrain_map_handoff]]

맞습니다.
지금 코덱스가 만든 게 “terrain처럼 보이는 그림”은 될 수 있어도, **왜 저 부분이 ridge인지 / 왜 저 구역이 basin인지 / 어떤 데이터가 저 표현을 만들었는지**를 당신이 확인할 수 없으면 실패입니다.

핵심 문제는 이겁니다.

* 지금 구현이 **renderer-first**
* 당신이 필요한 건 **semantic-field-first**

즉, 먼저 비트맵을 칠하는 게 아니라,

1. **의미 데이터 → 파생 지형 데이터층**
2. **파생 지형 데이터층 → inspectable geometry**
3. **geometry → terrain-like UI**

순서로 가야 합니다.

또한 브라우저에서 **Canvas는 비트맵 기반의 저수준 절차형 렌더링이고 built-in scene graph가 없어서**, 디버깅 가능한 “의미 오브젝트”를 직접 다루기엔 불리합니다. 반면 **SVG는 DOM/CSS/JS와 잘 결합되는 벡터 그래픽**이라 라벨, 경계선, 능선, 툴팁 같은 inspectable overlay에 적합합니다. 그래서 **기저 히트맵/필드 렌더는 Canvas**, **등고선/경계선/물길/라벨/hover는 SVG**로 나누는 게 맞습니다. 또한 D3의 `d3-contour`는 **격자값에서 marching squares로 contour polygon을 계산**하고, `d3-delaunay`는 **2D 점 집합의 Voronoi 분할**을 계산할 수 있어 지역 셀 생성과 등고선 생성에 잘 맞습니다. ([MDN 웹 문서][1])

아래 내용을 그대로 코덱스에게 주면 됩니다.

````md
# CODEx 지시서 — Semantic Terrain Map Viewer 구현 명세

## 0. 목적

지금 필요한 것은 “terrain처럼 보이는 이미지”가 아니다.

반드시 아래 조건을 만족하는 **semantic terrain map viewer**를 구현하라.

- 문서/대화/메모 기반 의미 공간을 “지형도”처럼 보여준다.
- 모든 주요 시각 요소는 **파생 데이터 이름**으로 설명 가능해야 한다.
- 사용자가 hover / click / inspector를 통해:
  - 왜 이곳이 region인지
  - 왜 이 선이 ridge인지
  - 왜 이곳이 basin인지
  - 왜 이 흐름이 water/current인지
  를 확인할 수 있어야 한다.
- 순수 bitmap-only 결과물 금지
- 의미 해석 불가능한 noise terrain 금지
- “보기 좋은 procedural terrain”보다 “검증 가능한 semantic terrain”을 우선한다.

---

## 1. 현재 데이터(입력)

현재 raw input에는 아래 값이 있다.

- fragment
- material
- local_space
- anchors
- scene
- observer_role
- observer_ambiguity
- observer_signals
- D
- I
- S

정의:
- D = direction
- I = intensity
- S = stability

현재 의미 대응:
- I -> elevation
- S -> terrain stability
- ambiguity -> fog
- scene -> biome
- role -> feature function
- signals -> wind / fault hints
- shared anchors -> water flow

---

## 2. 현재 실패 원인

현재 접근은 renderer-first이다.

즉:
- raw 값을 받아
- bit/pixel 단위로 terrain처럼 채색하고
- 결과적으로 사용자는 시각 결과만 보고
- 의미 중간층을 확인할 수 없다

이 방식은 금지한다.

반드시 아래 순서를 지켜라.

1. raw semantic data
2. derived terrain fields
3. inspectable geometry objects
4. layered rendering
5. inspector / legend / debug view

즉 **semantic-field-first pipeline** 로 재구성하라.

---

## 3. 구현 원칙

### 3.1 렌더링 원칙
아래 2계층 렌더링을 사용하라.

- Base field layer: Canvas
  - heat / fog / biome wash / density fill
- Semantic overlay layer: SVG
  - contour
  - region boundary
  - ridge
  - valley
  - basin outline
  - water/current line
  - fault line
  - labels
  - hover hit target

금지:
- 모든 것을 canvas pixel만으로 처리하는 구조
- hover 시 원인 데이터가 안 나오는 구조
- 지형은 있는데 파생 필드가 없는 구조

### 3.2 데이터 원칙
모든 시각 요소는 아래 3단계를 거쳐야 한다.

- raw fields
- derived fields
- geometry objects

예:
- ridge line을 그릴 때
  - 그냥 밝은 선을 그리지 말고
  - `ridge_axis_score` 를 계산한 후
  - threshold / trace 해서
  - `RidgeSegment[]` geometry로 변환한 뒤
  - SVG path로 렌더하라

### 3.3 검증 원칙
모든 geometry는 inspector에서 아래를 보여줘야 한다.

- geometry type
- derived field name
- contributing raw fields
- calculation summary
- value / threshold / neighbors
- related fragments / anchors / local_space ids

---

## 4. 필수 파생 데이터층

아래 7개는 1차 구현 필수다.

### A. region_identity_signature
- 목적:
  - 이 셀이 어떤 성질의 지역인지 정의
- source:
  - scene
  - observer_role
  - anchors
  - D/I/S
  - material
  - local_space
- 계산:
  - 셀 또는 local_space 단위 집계
  - dominant scene
  - dominant role
  - top anchors
  - mean D/I/S
  - material density
  - 위 값들을 묶어 지역 시그니처 생성
- 출력:
  - cell.regionIdentity
  - region clustering input

### B. region_boundary_score
- 목적:
  - 지역 경계 강도 계산
- source:
  - region_identity_signature
  - scene
  - observer_role
  - anchors
  - ambiguity
  - D/I/S
- 계산:
  - 인접 셀 간 차분
  - scene divergence
  - role divergence
  - shared anchor drop
  - ambiguity gradient
  - DIS gradient
  - weighted sum
- 출력:
  - edge.regionBoundaryScore

### C. ridge_axis_score
- 목적:
  - 능선 축 감지
- source:
  - I
  - S
  - region_boundary_score
  - anchors
  - D
- 계산:
  - 높은 I
  - 높은 S
  - 좌우 방향으로 flow split
  - 주변 대비 local maximum
- 출력:
  - cell.ridgeScore
  - traced RidgeSegment[]

### D. valley_channel_score
- 목적:
  - 골짜기 / 통로 감지
- source:
  - I
  - anchors
  - D
  - scene
  - observer_signals
- 계산:
  - 주변 대비 local minimum
  - shared anchor convergence
  - scene transition corridor
- 출력:
  - cell.valleyScore
  - traced ValleySegment[]

### E. basin_retention_score
- 목적:
  - 체류/축적/분지 감지
- source:
  - I
  - S
  - ambiguity
  - anchors
  - scene
- 계산:
  - low elevation
  - low outflow
  - internal anchor circulation
  - high retention / trapped ambiguity
- 출력:
  - cell.basinScore
  - BasinRegion[]

### F. anchor_flow_field
- 목적:
  - 물길/전류/흐름
- source:
  - anchors
  - shared anchors
  - D
  - scene
  - observer_role
- 계산:
  - 인접 셀 간 shared anchor strength
  - D continuity
  - role/scene traversal continuity
  - edge vector 생성
- 출력:
  - edge.flowMagnitude
  - edge.flowDirection
  - CurrentLine[]

### G. climate_zone_signature
- 목적:
  - 기후대/환경권 해석
- source:
  - scene
  - ambiguity
  - S
  - observer_signals
  - anchor_flow_field
  - I
- 계산:
  - biome + humidity/fog + terrain stability + turbulence + elevation band
  - 규칙 기반 zone 분류
- 출력:
  - region.climateZone
  - climate texture / tint / weather overlay

---

## 5. 고급 파생 데이터층(2차)

아래 3개는 2차 구현으로 넣되 구조는 미리 열어둬라.

### H. fault_line_score
- 목적:
  - 급격한 의미 단절선
- source:
  - scene
  - role
  - anchors
  - signals
  - D/I/S
- 계산:
  - anchor continuity 급락
  - scene/role 급변
  - D 방향 급반전
  - signal spike
  - stress accumulation
- 출력:
  - FaultLine[]

### I. wind_pressure_field
- 목적:
  - ambiguity / signal pressure
- source:
  - ambiguity
  - observer_signals
  - D
  - scene
- 계산:
  - ambiguity gradient
  - signal gradient
  - D variance
  - turbulence score
- 출력:
  - cell.windPressure
  - PressureStream[]

### J. landmark_score
- 목적:
  - 기억점 / 기준점
- source:
  - I
  - S
  - anchors
  - scene
  - role
  - ambiguity
- 계산:
  - prominence
  - uniqueness
  - symbolic role weight
  - visibility / distinctiveness
- 출력:
  - Landmark[]

---

## 6. 데이터 구조 설계

### 6.1 raw input 타입
```ts
type RawFragment = {
  id: string;
  fragment: string;
  material?: string;
  local_space?: string | null;
  anchors: string[];
  scene?: string | null;
  observer_role?: string | null;
  observer_ambiguity?: number | null; // 0~1
  observer_signals?: string[];
  D?: number | null; // 0~1 or normalized
  I?: number | null; // 0~1
  S?: number | null; // 0~1
  x?: number | null; // optional projected position
  y?: number | null; // optional projected position
};
````

### 6.2 spatial cell 타입

```ts
type TerrainCell = {
  id: string;
  x: number;
  y: number;
  fragments: string[];

  meanD: number;
  meanI: number;
  meanS: number;

  dominantScene: string | null;
  dominantRole: string | null;
  topAnchors: string[];

  ambiguityMean: number;
  signalDensity: number;
  materialDensity: number;

  regionIdentity: {
    sceneMix: Record<string, number>;
    roleMix: Record<string, number>;
    anchorWeights: Record<string, number>;
    disVector: [number, number, number];
  };

  elevation: number;
  terrainStability: number;
  fog: number;

  ridgeScore: number;
  valleyScore: number;
  basinScore: number;
  windPressure?: number;
  climateZone?: string | null;
  landmarkScore?: number;
};
```

### 6.3 edge 타입

```ts
type TerrainEdge = {
  sourceCellId: string;
  targetCellId: string;

  sharedAnchorStrength: number;
  sceneDifference: number;
  roleDifference: number;
  ambiguityGradient: number;
  disDifference: number;

  regionBoundaryScore: number;

  flowMagnitude: number;
  flowDirection: [number, number];

  faultScore?: number;
};
```

### 6.4 geometry 타입

```ts
type RegionPolygon = {
  id: string;
  cellIds: string[];
  polygon: [number, number][];
  climateZone?: string | null;
  label: string;
};

type RidgeSegment = {
  id: string;
  points: [number, number][];
  meanScore: number;
  sourceCellIds: string[];
};

type ValleySegment = {
  id: string;
  points: [number, number][];
  meanScore: number;
  sourceCellIds: string[];
};

type BasinRegion = {
  id: string;
  polygon: [number, number][];
  score: number;
  sourceCellIds: string[];
};

type CurrentLine = {
  id: string;
  points: [number, number][];
  magnitude: number;
  sourceEdgeIds: string[];
};

type FaultLine = {
  id: string;
  points: [number, number][];
  score: number;
  sourceEdgeIds: string[];
};

type Landmark = {
  id: string;
  x: number;
  y: number;
  label: string;
  score: number;
  sourceCellIds: string[];
};
```

---

## 7. 계산 파이프라인

### STEP 1. spatial substrate 만들기

입력 fragment를 그냥 점으로 찍지 말고, 먼저 **공간 셀(cell)** 을 만들어라.

선택지:

* 입력에 x/y가 있으면 grid cell로 bucket
* x/y가 없으면 projected space 생성 후 bucket
* 이후 Voronoi 또는 regular grid로 cell 구조 생성

권장:

* 초기는 regular grid
* 이후 Voronoi optional

출력:

* `TerrainCell[]`
* `TerrainEdge[]`

### STEP 2. raw -> cell aggregate

각 cell에 fragment들을 모아 아래를 계산하라.

* mean D/I/S
* dominant scene
* dominant role
* anchor frequency
* ambiguity mean
* signal density
* material density

### STEP 3. derived fields 계산

필수 7종 계산:

* region_identity_signature
* region_boundary_score
* ridge_axis_score
* valley_channel_score
* basin_retention_score
* anchor_flow_field
* climate_zone_signature

### STEP 4. geometry extraction

derived fields를 바로 그리지 말고, geometry로 뽑아라.

예:

* boundary score threshold -> boundary polyline
* ridge score + local maxima tracing -> ridge path
* basin score flood-fill -> basin polygon
* flow vectors tracing -> current line
* climate classification -> region fill

### STEP 5. layered rendering

아래 순서로 렌더하라.

1. biome base wash
2. elevation shading
3. fog
4. climate tint
5. contour lines
6. region boundaries
7. ridges
8. valleys
9. basins
10. currents
11. faults
12. landmarks
13. labels
14. hover highlight

---

## 8. 렌더링 규칙

### 8.1 base layers (Canvas)

Canvas에는 아래만 그려라.

* elevation raster
* biome tint
* fog
* climate wash
* optional stability texture

이유:

* 넓은 면 fill은 canvas가 효율적

### 8.2 semantic overlays (SVG)

SVG에는 아래를 그려라.

* contour lines
* region boundary lines
* ridge paths
* valley paths
* basin outlines
* current paths
* fault lines
* landmark symbols
* labels
* hover hit areas

이유:

* inspectable object가 필요하기 때문

### 8.3 contour

반드시 등고선을 넣어라.

* elevation field에서 threshold별 contour 생성
* contour는 raw bitmap stroke가 아니라 geometry여야 한다

### 8.4 label

반드시 label anchor를 두어라.

* region center
* basin center
* ridge name anchor
* landmark label anchor

---

## 9. 인터랙션 요구사항

### 9.1 hover

hover 시 아래 정보 표시:

* object type
* object id
* derived metric name
* main score
* source cell ids
* key anchors
* dominant scene / role
* related fragments count

예:

* `RidgeSegment ridge_03`
* ridgeAxisScore=0.82
* based on cells: c12,c13,c14
* meanI=0.78, meanS=0.84
* topAnchors=["water","memory","transition"]

### 9.2 click inspector

오른쪽 패널에 아래 표시:

* raw input summary
* derived fields
* geometry generation rule
* threshold used
* neighbor comparison
* related fragments list

### 9.3 layer toggle

반드시 아래 토글 제공:

* elevation
* fog
* biome
* region boundary
* ridge
* valley
* basin
* current
* climate zone
* fault
* landmark
* labels
* debug grid
* debug cells
* debug scores

### 9.4 debug mode

필수다.
켜면 각 cell 내부에 아래를 그려라.

* cell id
* mean I
* mean S
* ridge score
* valley score
* basin score
* climate zone

---

## 10. UI 레이아웃

### 왼쪽

* 지도 viewport

### 오른쪽

* inspector panel
* selected object detail
* raw / derived / geometry tabs

### 상단

* layer controls
* threshold sliders
* legend

### 하단

* object summary strip
* hovered / selected object quick info

---

## 11. 시각 매핑 규칙

### elevation

* source: I
* effect: 고도 음영 + contour 기준값

### terrain stability

* source: S
* effect: 거친 정도 / 균열 여부 / slope persistence

### fog

* source: ambiguity
* effect: 안개 밀도, visibility 감소

### biome

* source: scene
* effect: 지역 기본 색/텍스처

### feature function

* source: observer_role
* effect: 특정 지형 특징의 기능적 강조

  * 예: gateway / archive / transition / observer 등

### water/current

* source: shared anchors + D continuity
* effect: 흐름선 / 하천 / current path

### wind/fault hints

* source: observer_signals
* effect:

  * pressure particles
  * fault glow
  * turbulence

---

## 12. 절대 금지사항

* raw value를 바로 color noise로 뿌리는 방식
* ridge/valley/basin을 이름만 붙이고 실계산 안 하는 방식
* hover 시 “pixel”만 잡히고 의미 object가 없는 방식
* 경계선이 단지 색 차이 결과일 뿐 score/geometry가 없는 방식
* inspector 없이 결과만 보여주는 방식
* “terrain generator” 스타일 procedural noise에 의존하는 방식
* node-link graph를 살짝 꾸며서 terrain인 척하는 방식

---

## 13. 권장 구현 파일 구조

```txt
src/
  terrain/
    types.ts
    constants.ts

    pipeline/
      buildCells.ts
      buildEdges.ts
      aggregateCells.ts

    derive/
      regionIdentity.ts
      regionBoundary.ts
      ridgeAxis.ts
      valleyChannel.ts
      basinRetention.ts
      anchorFlow.ts
      climateZone.ts
      faultLine.ts
      windPressure.ts
      landmark.ts

    geometry/
      extractContours.ts
      extractRegionPolygons.ts
      extractRidges.ts
      extractValleys.ts
      extractBasins.ts
      extractCurrents.ts
      extractFaults.ts
      extractLandmarks.ts

    render/
      drawBaseCanvas.ts
      renderSvgOverlay.tsx
      legend.tsx

    ui/
      TerrainMapView.tsx
      TerrainControls.tsx
      TerrainInspector.tsx
      TerrainObjectTooltip.tsx
      TerrainDebugPanel.tsx

    hooks/
      useTerrainPipeline.ts
      useTerrainSelection.ts

    utils/
      scales.ts
      tracing.ts
      thresholds.ts
      labels.ts
```

---

## 14. 구현 순서

### Phase 1

필수:

* cell generation
* aggregate
* elevation/fog/biome canvas
* contour svg
* debug cell overlay
* inspector

### Phase 2

필수:

* region boundary
* ridge
* valley
* basin
* current

### Phase 3

추가:

* climate zone
* landmark
* threshold tuning UI

### Phase 4

고급:

* fault line
* wind pressure
* animation

---

## 15. 최소 동작 예시

최소한 아래 흐름이 동작해야 한다.

1. sample raw fragments load
2. cell grid build
3. aggregate cell metrics
4. derived fields compute
5. contour + region boundary + ridge + valley + basin + current render
6. hover object
7. inspector shows:

   * object type
   * source fields
   * calculation basis
   * related fragments

---

## 16. 실제 계산 초안

### 16.1 elevation

```ts
cell.elevation = normalize(cell.meanI);
```

### 16.2 fog

```ts
cell.fog = clamp01(cell.ambiguityMean);
```

### 16.3 region boundary

```ts
edge.regionBoundaryScore =
  w1 * sceneDifference +
  w2 * roleDifference +
  w3 * (1 - sharedAnchorStrength) +
  w4 * ambiguityGradient +
  w5 * disDifference;
```

### 16.4 ridge

```ts
cell.ridgeScore =
  a * localElevationMaxness(cell) +
  b * cell.terrainStability +
  c * flowSplitScore(cell) -
  d * basinNeighborhoodScore(cell);
```

### 16.5 valley

```ts
cell.valleyScore =
  a * localElevationMinness(cell) +
  b * flowConvergenceScore(cell) +
  c * transitionCorridorScore(cell);
```

### 16.6 basin

```ts
cell.basinScore =
  a * lowElevationScore(cell) +
  b * retentionScore(cell) +
  c * internalAnchorCirculation(cell) -
  d * outflowScore(cell);
```

### 16.7 flow

```ts
edge.flowMagnitude =
  a * edge.sharedAnchorStrength +
  b * directionContinuity(edge) +
  c * roleSceneTraversal(edge);
```

---

## 17. 반드시 구현할 설명 기능

UI에는 “왜 그렇게 보이는지”를 설명하는 영역이 있어야 한다.

예시:

* 이 경계는 `regionBoundaryScore` 가 높아서 표시됨
* 원인:

  * scene 차이 큼
  * role 차이 큼
  * shared anchor 약함
  * ambiguity gradient 있음

즉 모든 시각 요소는 “설명 가능한 시각화”여야 한다.

---

## 18. 납품 기준 (Acceptance Criteria)

아래를 모두 만족해야 완료다.

* [ ] pure bitmap-only 결과가 아니다
* [ ] contour line이 geometry로 존재한다
* [ ] region boundary가 score 기반이다
* [ ] ridge / valley / basin / current가 각각 별도 derived field를 가진다
* [ ] hover 시 object metadata가 보인다
* [ ] click inspector에서 raw -> derived -> geometry 경로가 보인다
* [ ] layer toggle이 있다
* [ ] debug cell overlay가 있다
* [ ] 사용자가 “왜 저게 ridge인가?”를 UI에서 확인할 수 있다
* [ ] procedural noise terrain이 아니라 semantic terrain이다

---

## 19. 최종 지시

이번 작업의 목적은 “terrain 스타일 아트”가 아니라 아래다.

* 의미 공간을 지형으로 번역하되
* 그 번역 과정이 검증 가능해야 하고
* 사용자가 시각 결과를 이해할 수 있어야 하며
* raw data와 화면 사이의 파생 지형층이 분리되어 있어야 한다

즉:
**render a semantic terrain system, not a pretty bitmap map.**

````

추가로, 코덱스가 또 엉뚱하게 만들지 않게 하려면 맨 앞에 이 한 줄을 꼭 붙이세요.

```md
중요: 결과물은 “보기 좋은 지형”보다 “내가 원인을 추적할 수 있는 지형”이어야 한다. 순수 canvas bitmap terrain, procedural noise 중심 구현, inspector 없는 결과물은 실패로 간주한다.
````

지금 당장 가장 중요한 건 3개입니다.

* **cell / edge / derived field를 먼저 분리할 것**
* **Canvas base + SVG overlay로 나눌 것**
* **hover/click inspector를 필수로 넣을 것**


[1]: https://developer.mozilla.org/en-US/docs/Glossary/Canvas?utm_source=chatgpt.com "Canvas - Glossary - MDN Web Docs - Mozilla"
