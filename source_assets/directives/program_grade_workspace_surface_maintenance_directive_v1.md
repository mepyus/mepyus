# Program-grade workspace 기준면 유지/갱신 운영 지시서 v1

## 0. 문서 성격
이 문서는 **코어 로직 수정 지시서가 아니다.**
이번 턴의 목적은 이미 잠긴 7개 기준 자산 + 보강 선언 1개를 기준으로,
앞으로 repo를 읽고 갱신할 때 **운영 기준면이 다시 흐트러지지 않도록 유지하는 것**이다.

즉 이번 지시의 핵심은:
- 새 기능 추가
- 코어 알고리즘 개조
- 페이지 확장
- 구조 재설계

가 아니라,

**입력 기준 / workspace 기준 / folder 기준 / shared reality / current state / recent delta / next phase direction**
이 7개 축을 실제 변경 속에서도 짧고 정확하게 유지하는 운영 습관을 고정하는 것이다.

---

## 1. 잠긴 기준 자산

### 1-1. 핵심 7개
1. `docs/policies/engine_input_lane_baseline_v1.md`
2. `docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md`
3. `docs/specs/folder_role_table_v1.md`
4. `source_assets/baselines/repo_shared_reality_pack_v1.md`
5. `runtime/views/repo_shared_reality_pack_index_v1.md`
6. `runtime/views/current_asset_map_v1.md`
7. `runtime/views/repo_delta_log_latest_v1.md`

### 1-2. 보강 선언 1개
- `source_assets/declarations/program_grade_next_phase_declaration_v1.md`

---

## 2. 이번 작업을 어떻게 읽어야 하는가

이번 작업은 **코어 로직 수정이 아니라 repo 읽기 기준면 수정**이다.

정확히는 아래를 잠근 것이다.

- **입력 해석 기준**
  - `engine_input_lane_baseline_v1`
  - 입력을 어떤 lane 체계로 받을지 고정

- **작업공간 해석 기준**
  - `codex_baseline_program_grade_workspace_upgrade_v1`
  - 이 repo를 단순 폴더 묶음이 아니라 program-grade workspace로 읽는 상위 기준 고정

- **폴더 책임 기준**
  - `folder_role_table_v1`
  - 무엇을 어디에 두는지 명세 고정

- **구조 현실 공유 기준**
  - `repo_shared_reality_pack_v1`
  - `repo_shared_reality_pack_index_v1`
  - shared reality를 어떤 세트와 어떤 입구로 공유할지 고정

- **현재 상태 판독 기준**
  - `current_asset_map_v1`
  - 지금 무엇이 기준 자산인지 고정

- **최근 변화 판독 기준**
  - `repo_delta_log_latest_v1`
  - 최근 무엇이 왜 바뀌었는지 고정

- **다음 단계 방향 기준**
  - `program_grade_next_phase_declaration_v1`
  - 코어 보존 → intake/shared reality 안정화 → read-only operation view → pages 순서를 고정

---

## 3. 절대 흔들지 말 것

아래는 이번 턴에서 **건드리지 않는 영역**이다.

### 3-1. 코어 금지
다음은 이번 지시 범위 밖이다.

- core logic 재설계
- ontology 재해석
- ingest/registry/event spine 변경
- page/view 새 구현
- 엔진을 다시 전체 재정의하는 문서 추가

### 3-2. 문서 역할 혼합 금지
아래 역할은 다시 섞지 않는다.

- `repo_shared_reality_pack_v1` = 정의/구성
- `repo_shared_reality_pack_index_v1` = 공식 입구/참조 경로
- `current_asset_map_v1` = 현재 기준 자산 지도
- `repo_delta_log_latest_v1` = 최근 변경 압축 기록

### 3-3. latest surface 남용 금지
`latest` 문서는 누적 장문 보고서가 아니다.
길어지면 latest가 아니라 archive가 된다.

---

## 4. 운영 원칙

### 원칙 1. 새 변경이 생기면 “전체를 다시 설명”하지 말고 기준면만 짧게 갱신한다
변경이 생길 때마다 전체 repo 설명서를 다시 쓰지 말고,
해당 변경이 어느 기준면에 걸리는지만 판단해서 필요한 자산만 짧게 갱신한다.

### 원칙 2. current와 delta를 분리한다
- `current_asset_map_v1`에는 **지금 기준이 무엇인지**
- `repo_delta_log_latest_v1`에는 **왜/언제 그렇게 되었는지**
를 남긴다.

둘을 섞지 않는다.

### 원칙 3. shared reality는 full tree dump 대체물이어야 한다
shared reality pack과 index는
“전체 트리 재독 없이도 지금의 공통 현실을 빠르게 공유할 수 있는 입구”
역할을 해야 한다.

### 원칙 4. 새 자산은 folder 기준과 input 기준을 함께 본다
새 파일을 어디에 둘지 애매하면,
반드시 아래 두 축을 같이 본다.

- `folder_role_table_v1`
- `engine_input_lane_baseline_v1`

즉 “무엇인가?”와 “어느 lane에서 읽히는가?”를 분리하지 않는다.

### 원칙 5. 다음 단계 우선순위를 어기지 않는다
잠긴 우선순위는 아래다.

1. 코어 보존
2. intake/shared reality 안정화
3. read-only operation view
4. pages

page 욕심 때문에 상위 우선순위를 거꾸로 뒤집지 않는다.

---

## 5. 변경 발생 시 처리 규칙

## 5-1. 새 스크립트/엔트리포인트가 생겼을 때
해야 할 것:
- `current_asset_map_v1`에서 entrypoint 반영 여부 점검
- 필요 시 `repo_delta_log_latest_v1`에 해당 변경 한 줄 추가

하지 말 것:
- 곧바로 shared reality pack 전체를 다시 쓰기
- unrelated baseline 문서까지 함께 수정하기

### 예시
상황:
- `scripts/` 아래에 새로운 운영 스크립트가 추가됨
- 기존 실행 경로 또는 공식 진입점에 영향이 있음

좋은 처리:
- `current_asset_map_v1`에서 현재 기준 실행 entrypoint를 갱신
- `repo_delta_log_latest_v1`에 “entrypoint surface adjusted due to new script path” 수준으로 짧게 기록

나쁜 처리:
- repo 전체 구조 설명을 다시 장문으로 덮어쓰기
- shared reality pack/index/current/delta를 한 번에 모두 장문 수정

---

## 5-2. shared reality 세트가 바뀌었을 때
해야 할 것:
- **정의 변경이면** `repo_shared_reality_pack_v1`
- **입구/참조 변경이면** `repo_shared_reality_pack_index_v1`
만 우선 수정

하지 말 것:
- pack과 index 양쪽에 같은 설명을 중복 장문으로 복사

### 예시
상황:
- shared reality pack에 포함할 기준 문서 세트가 조금 바뀜

좋은 처리:
- `repo_shared_reality_pack_v1`에서 세트 정의 수정
- `repo_shared_reality_pack_index_v1`에는 그 세트를 참조하는 공식 입구만 맞춤 조정

나쁜 처리:
- pack에도 설명, index에도 같은 설명을 거의 복붙
- 둘 다 “정의+입구+운영 이유”를 한꺼번에 장문 수록

---

## 5-3. 최근 변경 기록이 누적될 때
해야 할 것:
- `repo_delta_log_latest_v1`는 최근성 유지
- 오래된 내용은 archive나 별도 surface로 밀어내고 latest는 짧게 유지

하지 말 것:
- latest를 장기 연혁 문서처럼 키우기

### 예시
좋은 상태:
- 최근 3~7개 정도의 실제 변경만 남아 있음
- 각각이 왜 중요한지 짧게 보임

나쁜 상태:
- 수십 개 변화가 누적되어 현재성보다 역사서처럼 변함

---

## 5-4. legacy latest surface가 남아 있을 때
해야 할 것:
- no-longer-primary 표기
- current 기준 surface와 혼동되지 않도록 역할 명확화

하지 말 것:
- 옛 latest surface를 조용히 방치
- current asset map과 충돌하게 두기

### 예시
상황:
- 과거에 “latest”였던 문서가 아직 살아 있음

좋은 처리:
- 문서 또는 주변 기준 문서에 “no-longer-primary” 성격 명시
- 현재 공식 surface가 무엇인지 `current_asset_map_v1`에서 분명히 보이게 유지

비조치:
- old latest 문서를 아무 표기 없이 계속 공식처럼 방치 금지

---

## 5-5. inputs/external_cases 안의 mixed residue 정리
해야 할 것:
- 과거 혼합 md 흔적은 즉시 대공사하지 말고
- “현재 canonical input / 현재 공식 파생물 / 잔존 residue”를 분리 판독
- residue는 점진 정리 대상으로 둔다

하지 말 것:
- legacy residue 정리 핑계로 현재 운영 기준을 다시 흔들기

### 예시
상황:
- `inputs/external_cases` 내부에 과거 혼합형 md가 남아 있음

좋은 처리:
- 현재 SSOT 입력 자산과 legacy residue를 구분 표기
- 필요 시 `repo_delta_log_latest_v1`에 cleanup note를 짧게 남김

나쁜 처리:
- residue를 이유로 전체 외부사례 파이프라인 문서를 새로 재설계
- canonical source 기준까지 다시 흔들기

---

## 6. 판단 규칙: 무엇을 어느 문서에 반영할 것인가

### A. 입력 해석 체계가 바뀌는가?
- 예: lane 추가, lane 정의 변경, 입력 문서 성격 변경
- 반영 우선:
  - `engine_input_lane_baseline_v1.md`

### B. 이 repo를 읽는 상위 작업공간 철학/운영 기준이 바뀌는가?
- 예: program-grade workspace 해석 축 수정
- 반영 우선:
  - `codex_baseline_program_grade_workspace_upgrade_v1.md`

### C. 파일/폴더의 배치 책임이 바뀌는가?
- 예: 폴더 책임 조정, 역할 재배치
- 반영 우선:
  - `folder_role_table_v1.md`

### D. 공통 현실 세트 정의가 바뀌는가?
- 예: shared reality set 구성 변경
- 반영 우선:
  - `repo_shared_reality_pack_v1.md`

### E. 공통 현실 공식 입구가 바뀌는가?
- 예: index가 가리키는 공식 경로 변경
- 반영 우선:
  - `repo_shared_reality_pack_index_v1.md`

### F. 지금 무엇이 기준인지 달라졌는가?
- 예: current official surfaces / entrypoint / primary assets 변경
- 반영 우선:
  - `current_asset_map_v1.md`

### G. 최근 변화 한 줄 설명이 필요한가?
- 예: 이번 변경이 왜 생겼는지 짧은 설명 필요
- 반영 우선:
  - `repo_delta_log_latest_v1.md`

### H. 다음 단계 우선순위가 달라졌는가?
- 예: operation view 이후 바로 pages가 아니라 다른 단계가 선행돼야 함
- 반영 우선:
  - `program_grade_next_phase_declaration_v1.md`

---

## 7. 권장 작업 순서

변경이 생겼을 때 아래 순서로 판단한다.

1. 이 변경이 코어 수정인가, 기준면 수정인가?
2. 기준면 수정이라면 어느 축인가?
   - input
   - workspace
   - folder
   - shared reality definition
   - shared reality entry
   - current
   - delta
   - next phase
3. 가장 직접 관련된 문서 1~2개만 먼저 갱신한다
4. current/delta 충돌이 없는지 확인한다
5. latest 성격이 무너지지 않았는지 확인한다
6. 불필요한 장문 재서술을 하지 않는다

---

## 8. 검증 체크리스트

아래 질문에 “예”가 나오면 이번 지시를 잘 따른 것이다.

- 이번 변경이 코어가 아니라 기준면인지 먼저 구분했는가?
- 수정 대상 문서를 1~2개로 좁혔는가?
- `current_asset_map_v1`와 `repo_delta_log_latest_v1` 역할을 섞지 않았는가?
- `repo_shared_reality_pack_v1`와 `repo_shared_reality_pack_index_v1`를 중복 장문으로 만들지 않았는가?
- latest surface를 짧고 최근성 있게 유지했는가?
- legacy surface를 current official surface처럼 보이게 두지 않았는가?
- 다음 단계 우선순위를 코어 보존 → intake/shared reality → read-only view → pages 순으로 유지했는가?

---

## 9. 짧은 실행 예시 묶음

### 예시 1. 새 운영 스크립트 추가
상황:
- `scripts/` 아래 새 운영 스크립트가 생겼다
- 공식 실행 entrypoint 판단에 영향이 있다

조치:
- `current_asset_map_v1` 갱신
- `repo_delta_log_latest_v1`에 짧게 반영

비조치:
- shared reality pack 전체 재작성 금지
- workspace baseline 전면 수정 금지

---

### 예시 2. shared reality 공식 입구 정리
상황:
- shared reality를 읽는 공식 참조 경로를 더 간단히 만들었다

조치:
- `repo_shared_reality_pack_index_v1` 갱신
- 정의 세트 자체가 바뀌지 않았다면 `repo_shared_reality_pack_v1`는 건드리지 않음

비조치:
- index에 pack 정의를 장문 중복 수록 금지

---

### 예시 3. old latest 문서가 current와 충돌
상황:
- 과거 latest 문서가 아직 남아 있어서 current 판단을 흐린다

조치:
- no-longer-primary 표기
- `current_asset_map_v1`에서 현재 공식 기준 surface를 더 분명히 보이게 조정

비조치:
- old latest 문서를 아무 표기 없이 계속 공식처럼 방치 금지

---

### 예시 4. external case residue 발견
상황:
- `inputs/external_cases` 아래 옛 mixed md가 남아 있다

조치:
- canonical input / current derived / residue 분리 판독
- 필요 시 delta에 cleanup note만 짧게 남김

비조치:
- residue 정리 명목으로 external case 전체 파이프라인 재설계 금지

---

## 10. 최종 운영 문장

이번 턴 이후 CODEx는
**“무언가가 바뀌면 전체 repo를 다시 설명하는 방식”**이 아니라,

**“바뀐 사실이 어느 기준면에 속하는지 먼저 판정하고, 해당 기준 자산만 짧고 정확하게 갱신하는 방식”**
으로 움직여야 한다.

한 줄로 잠그면:

> 코어는 보존하고, 외곽 운영 기준면은 역할별로 분리 유지하며, 변경이 생길 때마다 current/delta/shared reality를 짧고 정확하게 갱신하라.
