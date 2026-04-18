# paperclip native vs vectorfl principles comparison v0

## 1. verdict

Paperclip를 native하게 다시 읽고 나서 우리 공간의 잠금 문서들과 비교해 보면, 둘 사이에는 `구조적 접점`은 분명히 있지만 `중심 ontology`는 다르다.

짧게 말하면 이렇다.

- Paperclip는 `업무 배정과 기관 운용이 가능한 회사 운영 제품`이다.
- VectorFL은 `current-reading / governance / trace를 중심으로 case와 lane을 숙성시키는 해석 공간`이다.

따라서 맞는 결론은 아래다.

- Paperclip에서 그대로 가져와야 하는 것은 `operable pages`, `assignment line`, `detail + inspector`, `instruction/config editability`, `activity audit`, `spatial org class`다.
- VectorFL에서 계속 지켜야 하는 것은 `current-reading first`, `governance first-class`, `trace/memory retention`, `core canonical ownership`이다.
- 둘을 섞을 때 가장 위험한 것은 `Paperclip의 issue/agent/company ontology를 그대로 VectorFL canonical object처럼 받아들이는 것`이다.

## 2. why this comparison

이 비교가 필요한 이유는 지금까지의 drift가 명확했기 때문이다.

- Paperclip를 먼저 제품 자체로 읽지 않으면, shell만 가져오고 native page class는 놓치게 된다.
- VectorFL 원칙만 먼저 밀어넣으면 Paperclip의 operable surfaces가 사라지고, 결과가 그래프뷰 변형처럼 보이게 된다.
- 반대로 Paperclip를 그대로 들이면 VectorFL의 current-reading / governance / trace 질서가 밀린다.

그래서 이번 문서의 목적은 `무엇이 맞고 무엇이 안 맞는지`를 원칙 단위로 가르는 것이다.

## 3. direct fits

### 3-1. paperclip list/detail/inspector 구조는 host shell 참조로 강하게 맞는다

Paperclip native line의 중심은

- `Issues list`
- `IssueDetail`
- `IssueProperties`

였다.

이 구조는 우리 쪽의 `paperclip-ref host shell layer`와 잘 맞는다.  
왜냐하면 shell 층은 원래

- case queue
- current-reading console
- governance panel
- trace/history panel
- program connection 화면

같은 operator-facing surface를 담당하도록 잠겨 있기 때문이다.

근거:

- [paperclip_native_product_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/paperclip_native_product_reading_v0.md)
- [vectorfl_three_layer_structure_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_three_layer_structure_lock_v0.md)

판정:

- `fit: strong`

### 3-2. paperclip operable agent detail는 우리 organ 운용면 필요와 강하게 맞는다

Paperclip의 `AgentDetail`은 단순 관찰면이 아니라

- instructions
- configuration
- skills
- runs
- budget

을 직접 수정하는 기관 운용면이다.

이건 우리 공간에서 잠긴 `기관` 개념과 비교할 때 중요하다.  
우리도 이미 기관 후보를 읽었고, 기관별 instruction bundle / handoff / caution / return 문법까지 잠갔다.  
즉 기관이 단순히 보이는 대상이 아니라 `운용 대상`이어야 한다는 필요와 정확히 맞닿는다.

근거:

- [paperclip_native_product_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/paperclip_native_product_reading_v0.md)
- [space_operating_organ_registry_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/space_operating_organ_registry_v0.md)

판정:

- `fit: strong`

### 3-3. activity/audit page는 trace-first 원칙과 잘 맞는다

Paperclip의 `Activity`는 append-only audit page class다.  
이건 우리 쪽의 `Trace / Memory Record`, `기록기억기`, `trace/history preview`와 직접 접점이 있다.

근거:

- [paperclip_native_product_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/paperclip_native_product_reading_v0.md)
- [vectorfl_canonical_object_ownership_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_canonical_object_ownership_lock_v0.md)
- [space_operating_organ_registry_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/space_operating_organ_registry_v0.md)

판정:

- `fit: strong`

### 3-4. inbox/routines는 case intake와 progression surface로 참조 가능하다

Paperclip의 `Inbox`는 triage page고, `Routines`는 recurring work allocation page다.  
이건 우리 쪽 `입력기`, `case queue`, `lane progression`, `next-hop visibility`와 구조적으로 접점이 있다.

다만 naming을 그대로 들이는 것은 아니다.

근거:

- [paperclip_native_product_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/paperclip_native_product_reading_v0.md)
- [vectorfl_three_layer_structure_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_three_layer_structure_lock_v0.md)

판정:

- `fit: usable`

## 4. partial fits

### 4-1. paperclip issue line과 vectorfl case/lane line은 구조는 닮았지만 의미는 다르다

Paperclip의 핵심 operational line은

`Issues list -> IssueDetail -> IssueProperties`

이고, 우리 쪽 core line은

`intake -> case -> lane -> current-reading / governance / trace`

다.

둘은 모두 `work unit -> detail -> control/inspector` 구조를 갖지만, 의미는 다르다.

- Paperclip는 task assignment/control plane
- VectorFL은 interpretation/governance/trace plane

즉 구조는 참조 가능하지만, issue를 case와 동일시하면 안 된다.

근거:

- [paperclip_native_product_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/paperclip_native_product_reading_v0.md)
- [vectorfl_canonical_object_ownership_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_canonical_object_ownership_lock_v0.md)

판정:

- `fit: partial`

### 4-2. paperclip org chart는 spatial page class로는 유효하지만, vectorfl의 중심면은 아니다

Paperclip는 관계를 보여줄 때 `OrgChart`라는 전용 spatial page class를 쓴다.  
이건 나중에 VectorFL에서도 `관계/흐름을 공간적으로 보여주는 면`이 필요해질 때 좋은 기준이다.

하지만 우리 잠금 문서 기준으로 VectorFL의 중심은 여전히 `current-reading`이다.  
즉 spatial page는 보조적 확장이지 중심이 아니다.

근거:

- [paperclip_native_product_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/paperclip_native_product_reading_v0.md)
- [vectorfl_external_source_and_host_need_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_external_source_and_host_need_lock_v0.md)

판정:

- `fit: partial`

## 5. direct mismatches

### 5-1. paperclip ontology는 vectorfl canonical object와 직접 맞지 않는다

우리 문서에서는 이미 아래 naming을 canonical로 잠그지 않기로 했다.

- company
- issue
- project
- heartbeat
- approval / budget naming

이 판단은 이번 native reading 이후 더 강해졌다.  
왜냐하면 이 naming들은 Paperclip 제품의 자기 ontology이기 때문이다.

즉 Paperclip를 제대로 읽을수록, 그 ontology를 그대로 들이지 말아야 한다는 우리의 non-mixing rule이 더 정당화된다.

근거:

- [paperclip_native_product_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/paperclip_native_product_reading_v0.md)
- [vectorfl_three_layer_structure_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_three_layer_structure_lock_v0.md)

판정:

- `mismatch: strong`

### 5-2. paperclip는 current-reading first가 아니다

Paperclip의 중심은 work management와 company orchestration이다.  
VectorFL의 중심은 `current-reading`, `governance`, `trace carry`다.

즉 Paperclip는 `assignment-first`이고, VectorFL은 `reading-first`다.

이 차이를 무시하면, VectorFL이 결국 task manager처럼 축소된다.

근거:

- [paperclip_native_product_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/paperclip_native_product_reading_v0.md)
- [vectorfl_external_source_and_host_need_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_external_source_and_host_need_lock_v0.md)

판정:

- `mismatch: strong`

### 5-3. paperclip의 governance는 company operation governance이고, vectorfl governance는 reading protection governance다

Paperclip에서 governance는 approval, board action, budgets, pause/resume, hard stop과 가깝다.  
우리 쪽 governance는

- hold
- observer-only
- promotion 금지
- mixed corridor
- release condition

처럼 `성급한 확정과 평탄화를 막는 reading protection`에 더 가깝다.

구조적으로는 둘 다 stop points를 갖지만, 지키는 대상이 다르다.

근거:

- [paperclip_native_product_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/paperclip_native_product_reading_v0.md)
- [vectorfl_handoff_boundary_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_handoff_boundary_lock_v0.md)
- [space_operating_organ_registry_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/space_operating_organ_registry_v0.md)

판정:

- `mismatch: strong`

## 6. what paperclip reveals about our own principles

이번 비교를 통해 우리 문서들 중 맞게 잠긴 것과 보정이 필요한 것이 분명해졌다.

### 6-1. 맞게 잠긴 것

- `Paperclip는 shell 참조다`
- `canonical object ownership은 core에 남는다`
- `shell은 display/adaptation layer다`
- `trace / memory는 first-class다`
- `외부 앱은 운영 구조 표본이다`

이 다섯 판단은 이번 native reading 이후 더 강해졌다.

### 6-2. 보정이 필요한 것

`paperclip-ref host shell layer`라는 표현은 너무 얇다.  
지금 native reading 기준으로 보면 Paperclip에서 필요한 것은 단순 shell tone이 아니라

- operable list page class
- operable detail page class
- right-side inspector class
- operable organ detail class
- activity audit class
- spatial org class

다.

즉 우리 문서의 `shell` 표현은 유지 가능하지만, 실제 참조 대상은 `page class + operability`까지 포함한다고 더 명시돼야 한다.

## 7. what this means before any more ui work

지금 이 비교가 말하는 건 간단하다.

더 이상 `graph-like VectorFL output`을 먼저 놓고 Paperclip 스타일을 씌우면 안 된다.  
먼저 Paperclip native line을 기준으로 페이지 class를 다시 잡아야 한다.

우선순위는 아래처럼 읽힌다.

1. `work list page`
2. `work detail page`
3. `right-side inspector`
4. `operable organ detail page`
5. `activity audit page`
6. `spatial org page`는 나중

그리고 그 위에서만 VectorFL core object를 어디에 얹을지 판단해야 한다.

## 8. final judgment

Paperclip와 VectorFL은 적이 아니지만, 같은 제품도 아니다.

- Paperclip는 `회사 운영 제품`
- VectorFL은 `해석/보호/기억 공간`

따라서 둘을 결합할 때의 원칙은 아래 한 문장으로 정리된다.

`Paperclip에서 가져올 것은 operable page class와 assignment/detail/inspector 구조이고, VectorFL에서 유지할 것은 current-reading/governance/trace의 canonical 질서다. Paperclip의 ontology를 들이지 않은 채, 그 page class 위에만 VectorFL core를 얹는 것이 맞다.`

## appendix. compared documents

- [paperclip_native_product_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/paperclip_native_product_reading_v0.md)
- [vectorfl_three_layer_structure_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_three_layer_structure_lock_v0.md)
- [vectorfl_handoff_boundary_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_handoff_boundary_lock_v0.md)
- [vectorfl_external_source_and_host_need_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_external_source_and_host_need_lock_v0.md)
- [vectorfl_canonical_object_ownership_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_canonical_object_ownership_lock_v0.md)
- [space_operating_organ_registry_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/space_operating_organ_registry_v0.md)
