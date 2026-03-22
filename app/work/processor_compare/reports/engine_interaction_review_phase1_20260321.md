# Engine Interaction Review Phase 1

## 1. review scope
- 날짜: 2026-03-21
- 기준:
  - viewer는 Phase 1 freeze 상태로 본다
  - `/` = operator shell
  - `/atlas` = region / bridge inspector
  - `/source` = canonical / weak rejection / lineage evidence
  - `/dust` = relation / disagreement evidence
- 이번 review 목적:
  - 현재 엔진이 정말 원본을 공간 재료로 번역해 상호작용 가능성과 전이 가능성을 여는지 점검
  - viewer가 아니라 engine 가설을 검토

## 2. cases reviewed
- case_001
  - `processor_compare/doc_004.txt`
  - local space: `lsp_00018441d497`
  - region label: `doc_004`
- case_002
  - `processor_compare/doc_005.txt`
  - local space: `lsp_2dde7aef787a`
  - region label: `doc_005`
- case_003
  - `processor_compare/doc_006.txt`
  - local space: `lsp_4eadb2fe7a96`
  - region label: `doc_006`
- case_004
  - `manual/test_live_space_sync_20260321.txt`
  - local space: `lsp_3eaef4e0c6dc`
  - region label: `test_live_space_sync_20260321`
- case_005
  - `manual/test_canonical_ingest_20260321.txt`
  - local space: `lsp_3630ca5d8a22`
  - region label: `test_canonical_ingest_20260321`

## 3. viewer freeze exceptions
- 없음
- 이번 턴에서는 viewer 예외 수정 없이 artifact / payload / runtime data만 검토했다

## 4. question-set results

### A. 입력은 실제로 “공간 재료”로 번역되고 있는가
- 판정: `yes`
- 근거:
  - 새 입력은 실제로 `local_space_ids`를 생성한다
  - latest intake 예시:
    - `source_ref = operator_phase1_test_20260321_fix`
    - `local_space_ids = ['lsp_b07e02748619']`
  - local space payload에는 실제로
    - `representative_anchors`
    - `supporting_anchors`
    - `bridge_trace_refs`
    - `state`
    가 저장된다
  - bridge trace에도 canonical shared anchor가 직접 들어간다
    - 예: `brg_c84da4760249` → `shared_anchors = Graph RAG`
- 판정 근거 file / artifact:
  - [graph_view.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/graph_view.py)
  - [live_input.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input.py)
  - [runtime/core/local_spaces](/Users/sungsookim/universe/vectorfl_replica/runtime/core/local_spaces)
  - [runtime/core/bridge_traces](/Users/sungsookim/universe/vectorfl_replica/runtime/core/bridge_traces)
- 설명:
  - anchor / observer / lineage가 단순 표시용 메타는 아니다
  - 최소한 local space 형성과 bridge 노출에 실제로 관여한다

### B. local space는 결과 저장소인가, 상호작용 장인가
- 판정: `partial`
- 관찰 예시:
  - `lsp_00018441d497 (doc_004)`
    - `state = bridge_exposed`
    - `bridge_trace_refs = 6`
  - `lsp_2dde7aef787a (doc_005)`
    - `state = bridge_exposed`
    - `bridge_trace_refs = 9`
  - `lsp_3eaef4e0c6dc (test_live_space_sync_20260321)`
    - `state = bridge_exposed`
    - `bridge_trace_refs = 1`
- 관련 input/source_ref:
  - `processor_compare/doc_004.txt`
  - `processor_compare/doc_005.txt`
  - `manual/test_live_space_sync_20260321.txt`
- 설명:
  - local space는 단순 보관함은 아니다
  - 새 입력이 들어오면 실제로 새로운 local space가 생기고 bridge가 노출된다
  - 하지만 현재 `state`, `coexistence_mode`, `pressure_axes`, `interpretation`은
    - 동적인 상호작용 계산 결과라기보다
    - 형성 이후를 설명하는 사후 라벨 성격이 강하다
  - 즉 “장”의 성격은 일부 있으나, 아직 “상태 전이 장”으로 충분히 설득되지는 않는다

### C. bridge는 단순 overlap인가, 실제 가능성 노출인가
- 판정: `partial`
- bridge 예시:
  - `doc_004 -> doc_005`
    - `Ontology`, `Foundry`, `Link`, `Action Type`
    - `brg_e4d1fa10fa46`
  - `doc_005 -> doc_006`
    - `모델 LLM`, `LLM`, `AI`, `Property`
    - `brg_f30a3a351a8b`
  - `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`
    - `Graph RAG`
    - `brg_c84da4760249`
- why it matters:
  - bridge가 생기면 atlas/source/dust로 새로운 관찰 경로는 열린다
  - 즉 단순 overlap 표시는 아니다
  - 하지만 bridge trace payload를 보면
    - `state = candidate`
    - `reason = None`
    - `strength = None`
    - `shared_anchors`와 `note` 위주다
  - 따라서 현재 bridge semantics의 본체는 여전히 canonical overlap과 그 요약 설명에 가깝다

### D. region은 진짜 의미 지대인가, 요약 카드인가
- 판정: `partial`
- region 예시:
  - `doc_004`
    - representative: `Ontology`, `Object`, `Foundry`
    - supporting: `Property`, `Link`
  - `doc_005`
    - representative: `Palantir`, `Ontology`, `개체`, `Object`
  - `doc_006`
    - representative: `Property`, `Graph RAG`, `Graph DB`
- anchor / evidence 근거:
  - atlas payload에는 representative/supporting anchors, landmarks, bridge reasons가 모두 있음
  - region 읽힘은 안정적이다
- 부족한 점:
  - region은 현재 “좋은 판독 단위”이긴 하지만
  - region 안에서 원본들이 서로를 다시 읽게 만드는 힘이 강하게 계산되는 것은 아니다
  - 즉 의미 지대의 읽힘은 있으나, 상호작용 장으로서의 엔진 깊이는 아직 약하다

### E. 원본-원본 만남이 실제로 새로운 view를 여는가
- 판정: `partial`
- 실제 예시:
  - `doc_004`와 `doc_005`
    - Ontology / Foundry 축으로 재만남
  - `doc_005`와 `doc_006`
    - 모델 LLM / LLM / Property 축으로 재만남
  - `test_live_space_sync_20260321`와 `test_canonical_ingest_20260321`
    - Graph RAG 축으로 재만남
- 병목 위치:
  - `bridge semantics`
  - `local space interaction depth`
  - `observer merge shallowness`
  - `synthetic evidence depth`
- 설명:
  - 현재 operator는 atlas/source/dust를 통해 “이 원본이 저 원본과 이런 축으로 만난다”는 건 읽을 수 있다
  - 하지만 “저 원본 때문에 이 원본이 새롭게 다시 보인다”는 강한 재독해 감각은 아직 약하다
  - 즉 새 view가 열리긴 하지만, 그것이 아직 engine-driven transformation보다 reviewer-driven interpretation에 더 가깝다

### F. 현재 엔진은 “가능성 중심”인가, 아직 “판정 중심”인가
- possibility-centered parts:
  - canonical anchor 기반 bridge 노출
  - local space 간 연결 가능성 표시
  - atlas/source/dust drill-down으로 새로운 관찰 경로가 열리는 점
- judgment-centered parts:
  - local space `state` 설명
  - bridge `reason_line`
  - region 대표 anchor 선정
  - observer merged placeholder 위주의 evidence
- why:
  - 현재 엔진은 가능성 중심 요소를 일부 갖고 있지만
  - 전체 인상은 아직 “판정된 결과를 예쁘게 판독하게 하는 파이프라인” 쪽이 더 강하다

## 5. per-case evidence notes

### case_001 / case_002 / case_003
- `doc_004`, `doc_005`, `doc_006`은 bridge가 실제로 존재하고 atlas에서 재만남 축이 선명하다
- 하지만 source/dust evidence는 대부분 `material_backed_source`, `material_backed_dust`
- observer disagreement는 대체로 `not available yet`
- 즉 region/bridge 읽힘은 강하지만, interaction depth는 얕다

### case_004 / case_005
- manual live pair는 `Graph RAG` 하나만으로도 bridge가 열리고 local space가 즉시 연결된다
- 이건 공간 재료 번역과 전이 가능성 노출이 실제로 일어남을 보여준다
- 반면 evidence는 합성 fallback에 많이 의존한다

### live input operator_phase1_test_20260321_fix
- latest intake -> local space 형성은 실제로 된다
- `/source`, `/dust` evidence도 now available
- 하지만 lineage/canonical은 읽히고 disagreement/rejection depth는 얕다

## 6. current engine reading

### what already feels like space interaction
- 새 입력이 local space와 bridge를 실제로 만든다
- canonical anchor가 region/bridge 축을 안정화한다
- atlas/source/dust를 오가며 원본 간 만남을 판독할 수 있다
- live input과 기존 문서가 같은 축으로 다시 만난다

### what still feels like pipeline output
- local space state 해석
- bridge reason line
- region anchor summary
- source/dust synthetic fallback evidence
- observer compare merged placeholder

## 7. final judgment
- 판정: `partially holds`

설명:
- 현재 엔진은 부분적으로 이미 공간 엔진처럼 작동한다
- 특히 입력이 공간 재료로 번역되고, canonical anchor를 매개로 bridge와 region이 노출되는 점은 실제다
- 하지만 local space / bridge / region의 상호작용 깊이는 아직 충분히 설득적이지 않다
- 현재 읽힘의 상당 부분은 engine이 만든 “가능성 장”이라기보다,
  engine이 만든 판정 결과를 operator가 해석하는 방식에 기대고 있다

## 8. next engine questions
- live input / imported doc의 synthetic evidence를 더 깊게 만들려면 어떤 lineage를 material 단계에서 직접 보존해야 하는가
- bridge는 shared anchor 설명을 넘어 어떤 상호작용 상태를 가져야 하는가
- local space `state`와 `interpretation`은 사후 설명이 아니라 실제 전이 상태로 어떻게 강화할 수 있는가
- observer merged placeholder를 넘어서 disagreement가 실제 상호작용 장에 어떤 변화를 만드는지 계산할 수 있는가

## 9. required final lines
1. **현재 엔진에서 이미 공간적으로 읽히는 부분**
   - 입력이 local space와 bridge를 실제로 만들고, canonical anchor가 region/bridge 축을 안정화하는 부분
2. **아직 단순 파이프라인처럼 보이는 부분**
   - local space state 해석, bridge reason line, region summary, synthetic fallback evidence
3. **원본-원본 상호작용이 실제로 열리는 지점**
   - `doc_004 <-> doc_005`, `doc_005 <-> doc_006`, `test_live_space_sync_20260321 <-> test_canonical_ingest_20260321`
4. **다음 우선순위가 viewer가 아니라 engine이어야 하는 이유**
   - viewer는 이미 Phase 1 workbench로 충분히 읽히고, 현재 병목은 evidence depth와 interaction semantics이기 때문
