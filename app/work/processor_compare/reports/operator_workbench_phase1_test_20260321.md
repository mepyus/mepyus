# Operator Workbench Phase 1 Test

## 1. 테스트 환경
- 날짜: 2026-03-21
- 작업 경로: `/Users/sungsookim/universe/vectorfl_replica`
- 기준 상태:
  - `/` = operator shell
  - `/atlas` = region / bridge inspector
  - `/source` = canonical / weak rejection / lineage evidence
  - `/dust` = relation / disagreement evidence
- 제약:
  - 현재 Codex sandbox에서는 로컬 viewer HTTP 접근이 안정적으로 되지 않아, 이번 테스트는
    - runtime builder 함수
    - render 코드
    - 생성된 report JSON/HTML
    - 실제 `ingest_live_input()` 호출
    기준으로 검증했다.
  - 즉 브라우저 수동 클릭 대신, 실제 runtime 경로와 렌더 결과를 함수 수준으로 확인했다.

## 2. 실행한 시나리오 목록
- A. 새 live input 투입 후 `/` 판독
- B. `/atlas`에서 region 판독 후 bridge evidence 이동
- C. `/source` 판독
- D. `/dust` 판독
- E. 왕복 문맥 유지

## 3. 시나리오별 PASS / PARTIAL / FAIL

### 시나리오 A — 새 live input 투입 후 `/` 판독
- 판정: `PASS`
- 근거:
  - 초기 상태에서는 `ingest_live_input()`가 `local_space_ids`를 채우지 않아 시나리오가 사실상 깨져 있었다.
  - 즉시 수정 후에는 `local_space_ids`가 실제로 생성됨:
    - `lsp_b07e02748619`
  - `/`용 graph data에서 최신 intake와 local space는 정상 확인됨:
    - `latest_intake.source_ref = operator_phase1_test_20260321_fix`
    - `latest_intake.local_space_ids = ['lsp_b07e02748619']`
  - 선택된 node의 compact / inspector 본문에 필요한 값도 존재:
    - representative anchors 있음
    - dropped weak state 있음
    - observer compare placeholder 있음
  - 새 live input 기준 evidence drill-down도 복구됨:
    - `/source`에 `operator_phase1_test_20260321_b`, `operator_phase1_test_20260321_fix` source row가 실제로 나타남
    - `/dust`에도 같은 source_ref 기준 material-backed dust node가 나타남
- 마찰 포인트:
  - live input evidence는 현재 fragment-backed가 아니라 material-backed synthetic row/node로 보강된 상태라 evidence depth가 기존 runtime fragment보다 얕다

### 시나리오 B — `/atlas`에서 region 판독 후 bridge evidence 이동
- 판정: `PASS`
- 근거:
  - atlas payload는 충분히 읽힘:
    - `region_count = 12`
    - `bridge_count = 32`
    - `reason_line`, `anchor_hints`, `source_links`, `dust_links` 구조 존재
  - top-level bridge row와 inspector bridge row의 문법도 거의 일치
  - 실제 bridge sample:
    - `doc_005 -> doc_006`
    - `reason_line = doc_005와 모델 LLM / LLM 축으로 연결`
    - `source_links` 존재
    - `dust_links`도 material-backed dust id 기준으로 실제 채워짐
- 마찰 포인트:
  - source/dust jump는 이제 둘 다 가능하지만, bridge evidence는 여전히 material-backed fallback 위주라 fragment-level relation depth는 일정하지 않다

### 시나리오 C — `/source` 판독
- 판정: `PASS`
- 근거:
  - compact strip 자체는 읽힘:
    - `canonical_promotion`
    - `dropped_weak`
    - `observer_disagreement`
    - `ingest_lineage`
  - 상태 문법과 `+N more`도 반영됨
  - `fragment > source > global` 우선순위는 render 코드에서 확인됨
  - query target not-found도 명시됨
  - live input 기준 source row도 실제로 나타남:
    - `SOURCE_MATCH operator_phase1_test_20260321_b = 1`
    - `SOURCE_MATCH operator_phase1_test_20260321_fix = 1`
- 마찰 포인트:
  - live input source evidence는 `material_backed_source`로 합성된 행이라 observer disagreement 같은 일부 필드는 `not available yet`로 남는다

### 시나리오 D — `/dust` 판독
- 판정: `PASS`
- 근거:
  - compact strip은 읽힘:
    - `observer_compare`
    - `observer_disagreement`
    - `edge_reason`
  - dust query status / not-found 문법도 render 코드에 있음
  - live input source에 대응하는 dust row도 실제로 나타남:
    - `DUST_MATCH operator_phase1_test_20260321_b = 2`
    - `DUST_MATCH operator_phase1_test_20260321_fix = 1`
  - 현재 dust summary는 기존 fragment graph 기준으로는 잘 동작:
    - `dust_count = 874`
    - 기존 fragment-backed와 material-backed dust가 함께 렌더됨
- 마찰 포인트:
  - live input dust evidence는 존재하지만 observer compare는 대부분 merged placeholder 수준이다

### 시나리오 E — 왕복 문맥 유지
- 판정: `PASS`
- 근거:
  - `from=atlas|operator`뿐 아니라
    - `return_href`
    - `return_label`
    - `origin_route`
    - `origin_local_space_id`
    - `origin_region_label`
    - `origin_bridge_id`
    - `origin_source_ref`
    - `origin_fragment_id`
    - `origin_dust_id`
    쿼리 문맥이 실제로 source/dust 쪽에 전달됨
  - `/source`, `/dust`는 상단에서 이 object-level context를 chip으로 읽는다
  - query string route 처리 문제는 즉시 수정함
  - `/`는 `?local_space_id=...`가 오면 해당 node를 다시 선택한다
  - `/atlas` evidence jump도 `return_href=/atlas?local_space_id=...`를 사용해 선택된 region 문맥으로 돌아갈 수 있다
- 마찰 포인트:
  - bridge row highlight 자체를 복원하는 수준까지는 아니지만,
    Phase 1 기준으로는 operator가 “어디서 내려왔는지”를 잃지 않는 수준까지는 올라왔다

## 4. 발견 이슈 목록

### `READABILITY`
- compact summary 문법은 대체로 읽히지만, `/`의 compact shelf와 `/source` `/dust`의 compact strip은 여전히 약간 다른 문장 밀도를 가진다

### `NAVIGATION`
- `return_href`, `return_label`, `origin_*`까지 붙으면서 object-level 복귀 문맥은 Phase 1 기준 usable 수준으로 올라왔다

### `FOCUS`
- `/source`의 fragment/source/global 우선순위는 맞고 live input source도 나타난다
- `/dust`도 live input dust 항목이 나타나지만 material-backed dust는 fragment-backed보다 포커스 근거가 얕다

### `MISSING_DATA`
- live input의 source/dust evidence 연결은 복구됐지만, 일부는 synthetic fallback이라 observer disagreement / rejected weak detail이 비어 있다

### `STATUS_GRAMMAR`
- 전반적으로 많이 맞아졌지만 `/`의 `none rejected`와 다른 페이지의 `none`은 아직 미묘한 차이를 가진다

### `LINKING`
- query route는 수정 전에는 깨져 있었음
- 수정 후 live input evidence 링크는 실제로 연결되지만, 일부 atlas bridge의 dust evidence는 여전히 비어 있다

### `EVIDENCE_DEPTH`
- atlas bridge evidence는 source/doc/dust 수준까지는 내려가지만, dust 측 evidence는 material-backed fallback이라 깊이가 일정하지 않다

## 5. 즉시 고친 작은 문제들

### fix_001
- 파일: [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)
- 내용:
  - `urlparse(self.path).path`를 쓰도록 수정
  - `/source?fragment_id=...`, `/dust?dust_id=...`, `/atlas?local_space_id=...` 같은 query route가 더 이상 404로 깨지지 않음

### fix_002
- 파일: [live_input.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input.py)
- 내용:
  - `ingest_live_input()`가 실제로 `form_live_input_local_space()`를 호출하게 수정
  - 결과에 `cell_ids`, `local_space_ids`, `bridge_ids`, `space_result`를 채움
  - 시나리오 A 핵심 경로 복구

### fix_003
- 파일: [builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/source_view/builder.py)
- 내용:
  - fragment store에 없는 live input material을 `material_backed_source` synthetic row로 보강
  - 새 live input source도 `/source` evidence view에서 직접 읽을 수 있게 함
  - 시나리오 A, C의 live input source evidence 경로 복구

### fix_004
- 파일: [dust_field.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/dust_field.py)
- 내용:
  - fragment-backed dust 외에 material-backed dust node fallback을 추가
  - 새 live input source도 `/dust` evidence view에서 직접 읽을 수 있게 함
  - 시나리오 A, D의 live input dust evidence 경로 복구

### fix_005
- 파일: [region_atlas.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/region_atlas.py)
- 내용:
  - atlas `dust_links` 생성 규칙을 `fragment_id` 단일 의존에서
    `dust_input_id -> material_id -> fragment_id` fallback으로 보강
  - top-level bridge / side inspector bridge row 모두 dust evidence link가 실제로 채워지게 함
  - 시나리오 B의 atlas dust evidence 경로 복구

## 6. 남긴 ticket 목록

### `opwb_evd_004`
- route: `/source`, `/dust`
- scenario: A, C, D
- symptom: live input evidence는 now available이지만 material-backed synthetic fallback이어서 observer disagreement / weak rejection detail이 얕다
- why_it_matters_for_operator: 새 입력 검증은 가능해졌지만, 기존 fragment-backed evidence만큼 깊은 판독은 아직 어렵다
- severity: `P1`
- tags: `EVIDENCE_DEPTH`, `MISSING_DATA`
- suggested_next_move: live input material에서 canonical rejection / observer disagreement를 더 직접 보존하는 최소 lineage 필드 검토

### `opwb_read_001`
- route: `/`, `/source`, `/dust`
- scenario: A, C, D
- symptom: compact summary 상태 문법은 비슷하지만 완전히 같은 언어는 아님 (`none`, `none rejected` 등)
- why_it_matters_for_operator: 페이지를 왕복할수록 판독 언어가 미세하게 달라지는 느낌을 준다
- severity: `P2`
- tags: `READABILITY`, `STATUS_GRAMMAR`
- suggested_next_move: compact state label을 공통 helper 기준으로 한 번 더 정리

## 7. 최종 판정
- 판정: `부분 사용 가능`

### 이유
- `/`에서 새 입력 이후 local space 판독은 가능해졌다
- `/atlas`에서 bridge reason과 source/dust evidence jump는 usable하다
- `/source`, `/dust`의 compact summary도 기존 runtime evidence 기준으로는 읽힌다
- 새 live input도 이제 `/source`, `/dust` evidence 층까지 직접 내려간다
- page-level이 아니라 object-level 복귀 문맥도 Phase 1 기준 usable하게 보강됐다

하지만 아직 핵심 병목이 남아 있다.
- live input evidence는 synthetic fallback이라 깊이가 얕은 구간이 있다

한 줄 결론:
- **Phase 1은 기존 runtime 자료뿐 아니라 live input까지 포함해 부분 사용 가능**
- **하지만 synthetic evidence depth는 아직 추가 수술이 필요하다**
