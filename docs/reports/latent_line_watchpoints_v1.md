# latent line watchpoints v1

## 1. 목적

이 문서는 새 candidate를 만들기 위한 문서가 아니다.

목적은 장기 형성사 재독해에서 드러난 잠복 선들을 관찰 대상으로 세워,
앞으로 새 observation이 들어올 때 어떤 선이 더 짙어지고 있는지 먼저 볼 수 있게 하는 것이다.

## 2. 잠복 선 4개 정의

### 2.1 raw 복귀 / 원본 보존 선

- 정의:
  - raw / first-pass / report / provenance가 분리되어 있고
  - interpretation이 raw를 대체하지 않으며
  - 다시 raw로 돌아갈 손잡이가 유지되는 선
- 왜 중요한가:
  - 이 선이 짙어질수록 공간은 요약 저장소가 아니라 재독해 가능한 공간이 된다.

### 2.2 표면보다 전이를 읽는 선

- 정의:
  - 페이지 / 문서 / 코드를 정적 표면이 아니라 전이 허브, 운영 허브, 역할 허브로 읽는 선
- 왜 중요한가:
  - 이 선이 짙어지면 공간은 UI나 파일 목록 중심이 아니라 흐름과 역할 중심으로 읽히기 시작한다.

### 2.3 입력 구조가 읽기 기관으로 자라는 선

- 정의:
  - 입력 / 기록 구조가 단순 저장이 아니라 나중에 판단 / 관찰 / 후보 감시에 재사용되는 선
- 왜 중요한가:
  - 이 선이 짙어질수록 fragment / anchor / provenance / observer / report가 단순 저장물이 아니라 기관의 재료가 된다.

### 2.4 눈을 나중이 아니라 먼저 세우는 선

- 정의:
  - 읽기 전에 모드 / 국면 / 드리프트를 먼저 정하고, 관찰 유입 순간에 얇은 판정을 먼저 수행하려는 선
- 왜 중요한가:
  - 이 선이 짙어질수록 공간은 “나중에 사람이 정리”하는 곳이 아니라 “먼저 분기하고 먼저 가볍게 판단”하는 곳이 된다.

## 3. 관찰 체크포인트

### 3.1 raw 복귀 / 원본 보존 선

- raw anchor가 유지되는가
- report / trace를 거쳐도 raw 복귀 경로가 명확한가
- breadcrumb의 first_read_ref / next_hop이 raw 복귀 가능성을 잃지 않는가
- interpretation / summary가 raw 위에 얹히는 방식으로 남는가

### 3.2 표면보다 전이를 읽는 선

- “이게 무엇인가”보다 “어디서 어디로 넘기는가”가 먼저 보이는가
- role / transition / process 같은 표현이 반복되는가
- breadcrumb의 next_hop이 단순 다음 파일이 아니라 전이 지점으로 남는가
- 서로 다른 문서 / 코드에서도 비슷한 transition spine이 보이는가

### 3.3 입력 구조가 읽기 기관으로 자라는 선

- 새 기록 구조가 단순 보관용인지, 나중 판단에 쓰이는지 구분되는가
- breadcrumbs / observation registry / watch rule이 새 자료에서도 같은 방식으로 작동하는가
- 입력 단위가 candidate / boundary / seed watch 같은 판단면으로 연결되는가
- 기록된 것이 실제 다음 읽기나 watch result에 재사용되는가

### 3.4 눈을 나중이 아니라 먼저 세우는 선

- selected_mode / current_phase / drift_guard가 읽기 전에 먼저 작동하는가
- 새 observation이 append될 때 사람이 나중에 보지 않아도 watch_result가 먼저 붙는가
- same family라도 mode가 바뀌면 같은 path로 보지 않는 경계 판단이 남는가
- 후보를 억지로 만들지 않고 boundary / collapse / no_seed 상태가 유지되는가

## 4. 강해지는 신호

- raw 복귀 / 원본 보존 선
  - "요약 잘됨"보다 "원본으로 다시 돌아갈 수 있음"이 자주 기록됨
  - raw anchor retention이 반복적으로 보임

- 표면보다 전이를 읽는 선
  - "이건 화면이다"보다 "이건 전이 허브다 / 운용 허브다"가 반복됨
  - 같은 유형의 흐름 독법이 다른 case에서도 재사용됨

- 입력 구조가 읽기 기관으로 자라는 선
  - 같은 입력 구조가 여러 번 재사용되며 기관처럼 행동함
  - 새 observation append 시 watch rule 같은 얇은 판정이 자동으로 붙음

- 눈을 나중이 아니라 먼저 세우는 선
  - 사람이 나중에 판정하는 양이 줄고, append 시점 자동 판정이 늘어남
  - second seed가 없을 때도 억지 naming 없이 no_new_seed_yet이 유지됨

## 5. 현재 evidence와 아직 부족한 evidence

### 5.1 raw 복귀 / 원본 보존 선

- 현재 evidence:
  - `runtime/preflight_last_decision.json`에서 reflection이어도 raw requested anchor를 유지하는 패턴이 보인다.
  - `pipeline_candidate_scope_summary.json`가 reflection에서 raw anchor retention을 명시한다.
  - breadcrumbs가 next_hop을 잃지 않는다.
- 아직 부족한 evidence:
  - 더 다양한 case family에서 raw 복귀가 반복적으로 확인되지는 않았다.

### 5.2 표면보다 전이를 읽는 선

- 현재 evidence:
  - WashTank / officeout를 transition hub로 읽는 노트가 있다.
  - `process_reread_map_v1`와 `deep_internal_reread_long_arc_map_v1`가 page보다 transition / role을 먼저 읽는 흐름을 설명한다.
- 아직 부족한 evidence:
  - 이 독법이 더 많은 외부/내부 사례에서 자동 재사용되는지까지는 아직 얇다.

### 5.3 입력 구조가 읽기 기관으로 자라는 선

- 현재 evidence:
  - observation registry가 family / mode / first_read_ref / next_hop / boundary_note를 가진다.
  - candidate summary가 registry를 한 장으로 읽게 한다.
  - watch rule auto connection이 append 시점 판정을 남긴다.
- 아직 부족한 evidence:
  - interpretation / lineage / multi-lens까지 이어지는 완전한 기관화는 아직 아니다.

### 5.4 눈을 나중이 아니라 먼저 세우는 선

- 현재 evidence:
  - runtime preflight gate가 실제로 읽기 전에 mode와 drift를 먼저 정한다.
  - breadcrumb가 preflight decision과 연결된다.
  - reflection과 space_reading이 서로 다른 entry surface를 만든다.
- 아직 부족한 evidence:
  - 전역 middleware 수준으로 일반화되지는 않았다.

## 6. 새 observation을 읽을 얇은 판정 기준

- raw 복귀 / 원본 보존 선에 가까운가?
  - raw anchor 유지, first_read_ref 유지, reverse path 유지가 보이면 이 선으로 먼저 본다.

- 표면보다 전이를 읽는 선에 가까운가?
  - role / transition / hub / flow가 먼저 보이면 이 선으로 먼저 본다.

- 입력 구조가 읽기 기관으로 자라는 선에 가까운가?
  - registry / breadcrumb / watch result처럼 재사용되는 관찰면이 붙으면 이 선으로 먼저 본다.

- 눈을 나중이 아니라 먼저 세우는 선에 가까운가?
  - preflight / mode / drift guard가 읽기 전에 작동하면 이 선으로 먼저 본다.

## 7. 현재 가장 강해 보이는 선

- 현재 가장 강하게 보이는 선:
  - 눈을 나중이 아니라 먼저 세우는 선
  - raw 복귀 / 원본 보존 선

이유:
- preflight와 breadcrumb가 실제 append/read 전에 작동한다.
- reflection에서도 raw requested anchor retention이 유지된다.

## 8. 아직 가장 약하고 잠복적인 선

- 현재 가장 잠복적인 선:
  - 입력 구조가 읽기 기관으로 자라는 선

이유:
- registry / candidate summary / watch rule는 이미 살아 있지만,
  interpretation / lineage / multi-lens까지 기관화된 완전한 읽기 장기에는 아직 도달하지 않았다.

## 9. 왜 이 문서가 필요한가

- 앞으로 새 observation이 들어올 때 candidate 이전에 latent line 차원에서 먼저 볼 수 있게 하기 위해
- 장기 형성사 속에서 어떤 선이 짙어지고 있는지 추적하기 위해
- 최근 장치들을 “최근 공사”가 아니라 “잠복 선의 응축”으로 읽기 위해

