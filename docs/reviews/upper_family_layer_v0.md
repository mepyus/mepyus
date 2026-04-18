# Upper Family Layer v0

## 목적

이 문서는 `bounded functional space` 위에서
line family의 계보, same-root 판정, projection 분화,
route grouping을 관리하는 상위 층을 정의한다.

핵심은 아래다.

- 아래층은 `space` 가 현재 issue-root를 받아 운용한다
- 위층은 그 운용에서 나온 line family를 조직하고 연결한다

즉 upper family layer는
실행 공간을 대체하지 않고,
실행 공간들 위에서 `family 질서`를 유지하는 층이다.

## 왜 필요한가

현재 space만으로는 아래를 일관되게 관리하기 어렵다.

- 어떤 line들이 같은 root에서 나온 것인지
- 어떤 projection이 같은 family의 다른 면인지
- 어느 route가 같은 family 안의 변형인지
- 어떤 residue가 다음 family 분기점인지
- 서로 다른 space에서 생긴 line이 사실 same root인지

즉 space는 local operation에는 강하지만,
family lineage에는 약하다.

upper family layer는 이 약한 부분을 맡는다.

## upper family layer의 역할

### 1. root family organization

새 issue-root 또는 안정화된 line cluster를
어느 root family에 두는지 정리한다.

### 2. same-root tracking

표면 절차나 UI가 달라도
같은 invariant를 공유하면 같은 family로 묶는다.

### 3. projection lineage management

reading / structural / decision / residue line처럼
다른 층위의 projection이 같은 root에서 나왔는지 추적한다.

### 4. route grouping

family 내부의 route variants를 묶고,
언제 어떤 route가 활성화되는지 상위에서 읽을 수 있게 한다.

### 5. cross-space linking

서로 다른 bounded space 안에서 나온 line이라도
same-root면 연결해 준다.

### 6. residue return control

space에서 나온 residue가
같은 family를 두껍게 하는지,
새 family 분기점이 되는지,
혹은 그냥 local residue로 남는지를 가른다.

## upper family layer가 관리하는 핵심 객체

### 1. root_line_family

family의 가장 상위 단위

최소 필드:

- `family_id`
- `family_name`
- `problem_field`
- `core_distinction`
- `transition_logic`
- `judgment_question`
- `completion_criterion`

### 2. projection_line

같은 family에서 나온 다른 line 투영면

최소 필드:

- `projection_id`
- `family_id`
- `projection_role`
- `projection_layer`
- `line_type`
- `changed_facet`

### 3. route_signature

family 내부에서 어떤 route가 있는지 나타내는 단위

최소 필드:

- `route_id`
- `family_id`
- `route_name`
- `mode_class`
- `activation_conditions`
- `exclusion_conditions`
- `current_position_schema`
- `next_decision_points`

### 4. cross_space_link

서로 다른 space가 같은 family를 공유하거나
상하류 관계에 있을 때 연결하는 단위

최소 필드:

- `link_id`
- `source_space_id`
- `target_space_id`
- `family_id`
- `link_kind`

## 상위 판단 규칙

### rule 1. same-root 판정은 invariant 우선이다

표면 process, UI, 파일 위치보다
아래 다섯 invariant를 우선 본다.

- `problem_field`
- `core_distinction`
- `transition_logic`
- `judgment_question`
- `completion_criterion`

### rule 2. projection은 차이를 적되 root를 끊지 않는다

projection이 다르다는 이유만으로
새 family를 만들지 않는다.

먼저 아래를 확인한다.

- changed facet만 다른가
- route만 다른가
- bounded space만 다른가

그렇다면 projection으로 남긴다.

### rule 3. residue는 family thickening과 family branching을 구분한다

residue가 늘었다고 무조건 새 family가 되는 것은 아니다.

질문은 둘 중 하나다.

- 기존 family의 같은 질문을 더 두껍게 하는가
- 아예 다른 judgment question으로 갈라지는가

전자는 thickening,
후자는 branching이다.

### rule 4. space는 local, family는 cross-space다

space 안에서만 보이는 line과
space를 넘는 family를 혼동하지 않는다.

## 현재 메인 공간에 대한 1차 upper family map

## A. input-to-reading upper family

### family_id

`fam_input_to_reading`

### invariant

- `problem_field`: raw input becoming readable operating material
- `core_distinction`: raw input vs readable structured entry
- `transition_logic`: ingest -> split/shape -> readable entry
- `judgment_question`: 이 입력을 어떤 경로로 읽기 가능한 단위로 진입시킬 것인가
- `completion_criterion`: 입력이 traceable하고 readable한 entry로 전환됨

### linked spaces

- `input_ingest_space`
- `external_input_preprocess_space`

### representative projections

- ingest visibility projection
- preprocess shaping projection
- raw-return preservation projection

### representative routes

- direct ingest
- registry ingest
- compare-first preprocess
- regroup-first preprocess

## B. transition-thickening upper family

### family_id

`fam_transition_thickening`

### invariant

- `problem_field`: transition/reentry blockage and thickening
- `core_distinction`: simple pass/fail vs active transition condition
- `transition_logic`: observed blockage -> reread -> thickening or closure decision
- `judgment_question`: 이 전환은 왜 막혔고 지금 thickening/closure 중 어디에 있는가
- `completion_criterion`: active transition line의 상태와 next decision point가 설명 가능함

### linked spaces

- `transition_validation_space`
- `operating_readout_space`

### representative projections

- preflight latent-line projection
- corridor validation projection
- closure review projection
- operator readout projection

### representative routes

- preflight reread
- stage corridor probe
- residue robustness validation
- reconstruction supervisor readout

## C. operator-readout upper family

### family_id

`fam_operator_readout`

### invariant

- `problem_field`: current engine/process state becoming operator-readable
- `core_distinction`: raw state payload vs operator-facing readout
- `transition_logic`: state/update payload -> adapted model -> board/detail/search route
- `judgment_question`: 현재 상태를 어떤 readout route로 보여주고 조작하게 할 것인가
- `completion_criterion`: operator가 현재 상태와 다음 조작점을 읽을 수 있음

### linked spaces

- `operating_readout_space`

### representative projections

- readonly board projection
- activity strip projection
- selected detail projection
- internal search projection

### representative routes

- readonly board
- activity panel
- selected detail summary
- internal search

## 현재 cross-space link 초안

### 1. input_ingest_space -> external_input_preprocess_space

- `link_kind`: same-family adjacent route
- shared family: `fam_input_to_reading`

의미:

- direct ingest로 충분하지 않을 때
  preprocess shaping route로 옮겨 간다.

### 2. external_input_preprocess_space -> transition_validation_space

- `link_kind`: downstream validation handoff
- shared family: `fam_input_to_reading` to `fam_transition_thickening`

의미:

- shaped input이 실제 transition/reentry reading에서 어떻게 작동하는지
  다음 family에서 검증한다.

### 3. transition_validation_space -> operating_readout_space

- `link_kind`: explanation/readout projection
- shared family: `fam_transition_thickening`

의미:

- transition line에서 나온 판단이
  operator-facing readout route로 투영된다.

## stack order

현재 스택은 아래처럼 읽는 것이 맞다.

1. `bounded functional space`
   - local issue-root가 들어와 실제로 작동하는 구역

2. `upper family layer`
   - 서로 다른 space 위에서 family invariant, projection lineage, route grouping을 관리

3. `host-coupled maturation strategy`
   - 이 family/route 구조를 외부 host 위에서 실전 숙성시키고 회수하는 전략

4. `LLM sidecar`
   - 이후에야 이 구조를 탐색/호출/표현하는 부품으로 붙음

## 아직 약한 부분

### 1. family invariant가 아직 서술형이다

다음에는 schema로 더 압축해야 한다.

### 2. projection_line 객체가 아직 실제 registry 형태로 없다

현재는 문서상 정의 수준이다.

### 3. route_signature도 아직 초안이다

route별 activation/exclusion을 더 명시적으로 써야 한다.

## 결론

upper family layer는
space 위에 덧붙는 설명 문서가 아니라,
VectorFL이 `낱개 line 저장소`로 흐르지 않게 막아주는 상위 조직층이다.

이 층이 있어야

- same-root family를 추적하고
- 다른 projection을 같은 계보로 묶고
- residue를 thickening과 branching으로 가르고
- 서로 다른 bounded space를 하나의 공간 질서 안에서 다시 연결할 수 있다.
