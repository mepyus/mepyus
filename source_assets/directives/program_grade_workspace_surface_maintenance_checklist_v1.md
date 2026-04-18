[[A]] [[OBJ:codex_checklist]] [[SEM:program_grade_workspace_surface_maintenance_checklist_v1]]

# CODEx 체크리스트 — Program-grade workspace 기준면 유지 점검표 v1

## 0. 목적
이 체크리스트는 새 구조를 설계하기 위한 문서가 아니다.
목적은 이미 잠근 기준면이 실제 변경 속에서도 흐트러지지 않았는지,
CODEx가 **짧고 반복 가능하게 점검**할 수 있도록 만드는 것이다.

이 체크리스트는 두 가지를 동시에 만족해야 한다.

1. **CODEx가 기계적으로 점검 가능해야 한다**
2. **사용자가 읽어도 현재 상태와 부족한 점을 한눈에 이해할 수 있어야 한다**

즉, 이번 문서는 단순 선언문이 아니라
**운영 점검 + 보고 + 다음 액션 결정**까지 같이 가능한 읽기 쉬운 점검표다.

---

## 1. 점검 대상 기준 자산

### 1-1. 기준 7개
- `docs/policies/engine_input_lane_baseline_v1.md`
- `docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md`
- `docs/specs/folder_role_table_v1.md`
- `source_assets/baselines/repo_shared_reality_pack_v1.md`
- `runtime/views/repo_shared_reality_pack_index_v1.md`
- `runtime/views/current_asset_map_v1.md`
- `runtime/views/repo_delta_log_latest_v1.md`

### 1-2. 보강 선언/지시
- `source_assets/declarations/program_grade_next_phase_declaration_v1.md`
- `source_assets/directives/program_grade_workspace_surface_maintenance_directive_v1.md`

---

## 2. 이 체크리스트가 점검하는 핵심 질문

이 체크리스트는 아래 질문에 답하기 위해 존재한다.

1. 이번 변경은 **코어 수정**인가, **기준면 유지/갱신**인가?
2. 기준면 유지/갱신이라면 **어느 문서 1~2개만 고치면 되는가?**
3. current / delta / shared reality / next phase 역할이 다시 섞이지 않았는가?
4. latest surface가 장기 보고서처럼 비대해지지 않았는가?
5. legacy surface가 current official surface처럼 오해될 위험은 없는가?
6. 다음 단계 우선순위가 여전히 유지되는가?

---

## 3. 최상위 판정 규칙

## 3-1. 먼저 이것부터 판정
### Q1. 이번 변경은 코어 로직 수정인가?
- [ ] 예
- [ ] 아니오

판정:
- **예**면 이 체크리스트는 보조 참고만 하고, 별도 코어 변경 절차로 넘긴다.
- **아니오**면 이 체크리스트를 끝까지 수행한다.

### Q2. 이번 변경은 기준면 유지/갱신인가?
- [ ] 예
- [ ] 아니오

판정:
- **예**면 원칙적으로 관련 문서 **1~2개만** 수정해야 한다.
- **아니오**면 왜 기준면 문서를 건드리는지 근거를 다시 점검한다.

---

## 4. 기준면별 점검 체크리스트

## 4-1. 입력 기준면 점검
대상:
- `docs/policies/engine_input_lane_baseline_v1.md`

질문:
- [ ] 입력을 읽는 lane 기준이 현재도 이 문서와 일치하는가?
- [ ] 새 입력 유형이 생겼다면 기존 lane 해석과 충돌하지 않는가?
- [ ] 새 입력 자산이 생겼을 때 folder 기준과 함께 읽히도록 유지되고 있는가?
- [ ] input 기준 변경이 필요한데 current/delta 문서에만 반영하고 끝내지 않았는가?

이상 신호:
- 새 입력 유형이 생겼는데 lane 문서가 그대로다
- input 의미가 바뀌었는데 `current_asset_map_v1`에만 반영되어 있다
- input 기준이 folder 기준과 분리되어 설명된다

판정:
- 모두 예면 `PASS`
- 하나라도 아니오면 `REVIEW_REQUIRED`

---

## 4-2. workspace 기준면 점검
대상:
- `docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md`

질문:
- [ ] 이 repo를 program-grade workspace로 읽는 상위 기준이 유지되고 있는가?
- [ ] 최근 변경이 이 상위 기준과 충돌하지 않는가?
- [ ] repo를 단순 폴더 집합처럼 다시 설명하는 문장/운용이 생기지 않았는가?
- [ ] 새 변화가 생겨도 “전체 repo 재서술” 대신 관련 surface만 갱신하는 원칙이 유지되는가?

이상 신호:
- 새 변화가 생길 때마다 repo 전체를 다시 설명한다
- workspace 상위 기준보다 개별 변경이 우선 해석된다
- current/delta가 상위 기준을 대체하려 한다

판정:
- 모두 예면 `PASS`
- 하나라도 아니오면 `REVIEW_REQUIRED`

---

## 4-3. folder 책임 기준면 점검
대상:
- `docs/specs/folder_role_table_v1.md`

질문:
- [ ] 새 파일/폴더의 배치가 folder role 기준과 맞는가?
- [ ] 비슷한 성격의 자산이 여러 위치에 중복 배치되지 않았는가?
- [ ] source / runtime / docs / inputs 역할이 다시 섞이지 않았는가?
- [ ] 애매한 자산이 생겼을 때 folder 기준에 따라 판정했는가?

이상 신호:
- 같은 역할 문서가 여러 계층에 중복 저장됨
- directive와 baseline과 runtime view가 섞여 있음
- “일단 여기 넣고 보자” 식 배치가 누적됨

판정:
- 모두 예면 `PASS`
- 하나라도 아니오면 `REVIEW_REQUIRED`

---

## 4-4. shared reality 정의면 점검
대상:
- `source_assets/baselines/repo_shared_reality_pack_v1.md`

질문:
- [ ] shared reality에 포함되는 기준 세트 정의가 분명한가?
- [ ] 이 문서는 “정의/구성” 역할에 머물고 있는가?
- [ ] 공식 입구 설명이 이 문서 안에서 과도하게 중복되지 않는가?
- [ ] full tree dump를 대체하는 현실 공유 세트라는 목적이 유지되는가?

이상 신호:
- pack 문서가 index 역할까지 같이 하려 함
- 정의와 입구 설명이 장문으로 중복된다
- shared reality pack이 사실상 또 다른 전체 설명서가 된다

판정:
- 모두 예면 `PASS`
- 하나라도 아니오면 `REVIEW_REQUIRED`

---

## 4-5. shared reality 입구면 점검
대상:
- `runtime/views/repo_shared_reality_pack_index_v1.md`

질문:
- [ ] 현재 공식 입구로서 참조 경로가 분명한가?
- [ ] index 문서가 pack 정의를 장문 중복하지 않는가?
- [ ] 사용자가 full tree 대신 이 문서로 공통 현실에 들어갈 수 있는가?
- [ ] 현재 기준면과 연결이 자연스러운가?

이상 신호:
- index가 pack과 거의 같은 문장이 됨
- 공식 입구가 아니라 또 하나의 정의 문서처럼 변함
- 참조 경로보다 장황한 설명이 더 많음

판정:
- 모두 예면 `PASS`
- 하나라도 아니오면 `REVIEW_REQUIRED`

---

## 4-6. 현재 기준면 점검
대상:
- `runtime/views/current_asset_map_v1.md`

질문:
- [ ] 지금 무엇이 current official surface인지 분명한가?
- [ ] 새 지시서/선언문/핵심 surface가 생기면 active guidance에 적절히 반영되는가?
- [ ] current 문서가 “현재 기준 지도” 역할에 머물고 있는가?
- [ ] recent delta 설명이나 장기 배경 설명이 과도하게 들어오지 않았는가?

이상 신호:
- current 문서가 장기 보고서처럼 길어진다
- delta 설명이 current 문서 안으로 침투한다
- 새 기준 자산이 생겼는데 active guidance에 반영되지 않는다

판정:
- 모두 예면 `PASS`
- 하나라도 아니오면 `REVIEW_REQUIRED`

---

## 4-7. 최근 변화면 점검
대상:
- `runtime/views/repo_delta_log_latest_v1.md`
- `runtime/logs/repo_delta_log.jsonl`

질문:
- [ ] latest surface가 최근 변화만 짧게 담고 있는가?
- [ ] added asset / must-know / follow-up가 현재성 있게 유지되는가?
- [ ] raw delta log와 latest surface 사이에 최소한의 연결성이 있는가?
- [ ] latest가 장기 연혁/역사서처럼 커지지 않았는가?

이상 신호:
- latest 문서가 너무 길어져 recent 감각이 사라짐
- raw delta에는 있는데 latest에는 반영이 전혀 안 됨
- latest에 오래된 변동이 계속 쌓여 current 판독을 방해함

판정:
- 모두 예면 `PASS`
- 하나라도 아니오면 `REVIEW_REQUIRED`

---

## 4-8. 다음 단계 방향면 점검
대상:
- `source_assets/declarations/program_grade_next_phase_declaration_v1.md`

질문:
- [ ] 다음 단계 우선순위가 여전히 유지되는가?
- [ ] 코어 보존 -> intake/shared reality 안정화 -> read-only operation view -> pages 순서가 살아 있는가?
- [ ] page 확장 욕심이 상위 우선순위를 뒤집고 있지 않은가?
- [ ] 최근 변화가 next phase declaration과 충돌하지 않는가?

이상 신호:
- 바로 pages로 점프하려는 움직임
- shared reality 정리 전 view 확장 시도
- 코어 보존 원칙을 무시한 재구조화 압력

판정:
- 모두 예면 `PASS`
- 하나라도 아니오면 `REVIEW_REQUIRED`

---

## 4-9. 유지 운영 지시서 점검
대상:
- `source_assets/directives/program_grade_workspace_surface_maintenance_directive_v1.md`

질문:
- [ ] 변경이 생겼을 때 전체 repo 재서술 대신 관련 기준면 1~2개만 갱신했는가?
- [ ] directive가 실제 current/delta에 반영된 상태로 운영되고 있는가?
- [ ] 예외 상황 없이 유지 원칙이 반복 적용되고 있는가?
- [ ] 이번 변화도 이 지시서대로 처리되었는가?

이상 신호:
- 작은 변경인데 다시 전체 설명서를 쓴다
- directive는 있는데 실제 반영 습관이 없다
- 기준면 유지 대신 새 기준 문서를 계속 추가한다

판정:
- 모두 예면 `PASS`
- 하나라도 아니오면 `REVIEW_REQUIRED`

---

## 5. 교차 점검 체크리스트

## 5-1. current / delta 역할 분리
- [ ] `current_asset_map_v1`는 “지금 기준이 무엇인가”를 말한다
- [ ] `repo_delta_log_latest_v1`는 “왜/무엇이 바뀌었는가”를 말한다
- [ ] 두 문서가 서로 역할을 침범하지 않는다

### 실패 예시
- current 문서에 변화 연혁이 장문으로 들어감
- delta 문서가 현재 기준 전체를 다시 설명함

---

## 5-2. pack / index 역할 분리
- [ ] `repo_shared_reality_pack_v1`는 정의/구성이다
- [ ] `repo_shared_reality_pack_index_v1`는 공식 입구/경로다
- [ ] 둘이 거의 같은 문장이 되지 않는다

### 실패 예시
- pack에도 index 설명, index에도 pack 정의를 중복 장문으로 넣음

---

## 5-3. active guidance 최신성
- [ ] 새 directive / declaration / 기준면 자산이 생기면 current 문서에 반영한다
- [ ] current에서 지금 따라야 할 active guidance가 한눈에 보인다

### 실패 예시
- 새 운영 지시서가 source asset에는 있는데 current 문서엔 없음

---

## 5-4. legacy surface 정리
- [ ] 과거 latest/current 성격 문서가 아직 공식처럼 보이지 않게 정리되어 있다
- [ ] 필요 시 `no-longer-primary` 성격이 분명하다

### 실패 예시
- 예전 latest 문서가 지금도 공식 current처럼 보인다

---

## 5-5. latest 비대화 방지
- [ ] latest 문서는 짧고 최근성 있게 유지된다
- [ ] 오래된 변화는 archive/log로 밀어낸다

### 실패 예시
- latest가 사실상 연대기 문서가 된다

---

## 6. 최종 판정 등급

### A. LOCKED
조건:
- 핵심 기준면 전부 `PASS`
- 교차 점검에도 큰 충돌 없음
- current / delta / pack / index / next phase 역할이 선명함

의미:
- 기준면 운영 상태 양호
- 추가 작업 없이 유지 가능

### B. STABLE_WITH_MINOR_FIX
조건:
- 핵심 구조는 맞음
- 일부 문서 갱신 누락/중복/길이 문제만 존재

의미:
- 구조는 유지되고 있음
- 관련 surface 1~2개만 짧게 보수하면 됨

### C. DRIFT_WARNING
조건:
- 역할 혼합 시작
- latest 비대화
- current/delta 중복
- legacy/current 혼동 증가

의미:
- 아직 붕괴는 아니지만 기준면 drifting 시작
- 즉시 짧은 정리 필요

### D. REBASE_REQUIRED
조건:
- 기준면 역할이 크게 붕괴
- 전체가 다시 섞여 current 판독이 어려움
- 어느 surface가 공식인지 모호해짐

의미:
- 단순 maintenance로는 부족
- 기준면 재정렬 턴 필요

---

## 7. CODEx 출력 형식 템플릿

아래 형식으로 점검 결과를 출력한다.

```markdown
# Program-grade workspace surface maintenance check

## 1. overall verdict
- status: LOCKED | STABLE_WITH_MINOR_FIX | DRIFT_WARNING | REBASE_REQUIRED

## 2. checked assets
- engine_input_lane_baseline_v1: PASS | REVIEW_REQUIRED
- codex_baseline_program_grade_workspace_upgrade_v1: PASS | REVIEW_REQUIRED
- folder_role_table_v1: PASS | REVIEW_REQUIRED
- repo_shared_reality_pack_v1: PASS | REVIEW_REQUIRED
- repo_shared_reality_pack_index_v1: PASS | REVIEW_REQUIRED
- current_asset_map_v1: PASS | REVIEW_REQUIRED
- repo_delta_log_latest_v1: PASS | REVIEW_REQUIRED
- program_grade_next_phase_declaration_v1: PASS | REVIEW_REQUIRED
- program_grade_workspace_surface_maintenance_directive_v1: PASS | REVIEW_REQUIRED

## 3. cross-check
- current_vs_delta: PASS | REVIEW_REQUIRED
- pack_vs_index: PASS | REVIEW_REQUIRED
- active_guidance_freshness: PASS | REVIEW_REQUIRED
- legacy_surface_separation: PASS | REVIEW_REQUIRED
- latest_surface_compactness: PASS | REVIEW_REQUIRED

## 4. must-fix now
- item 1
- item 2

## 5. safe to defer
- item 1
- item 2

## 6. recommended next action
- update only [document A]
- update only [document B]
- do not rewrite the whole repo explanation

## 7. one-line summary
- current surface discipline is preserved / drifting / needs bounded repair
```

---

## 8. 사용자도 바로 읽을 수 있는 짧은 요약 규칙

CODEx는 점검 후 반드시 아래 3줄 요약도 함께 준다.

### 형식

- **지금 상태:** 한 문장
- **당장 고칠 것:** 1~2개
- **건드리지 말 것:** 1줄

### 예시

- 지금 상태: 기준면은 대체로 잠겨 있고, current/delta 분리도 유지되고 있다.
- 당장 고칠 것: `current_asset_map_v1` active guidance 최신화, `repo_delta_log_latest_v1` 길이 압축
- 건드리지 말 것: 코어와 shared reality 정의 전체 재서술

---

## 9. 실제 예시

## 예시 A. 좋은 점검 결과

상황:
- directive 추가 후 current/delta에 반영됨
- latest도 짧음
- active guidance도 갱신됨

출력 요지:
- overall verdict: `LOCKED`
- must-fix now: 없음 또는 매우 작음
- next action: 유지

---

## 예시 B. 가벼운 drifting

상황:
- 새 지시서는 추가됐는데 current 문서 active guidance에 빠짐
- delta는 지나치게 길어짐

출력 요지:
- overall verdict: `STABLE_WITH_MINOR_FIX` 또는 `DRIFT_WARNING`
- must-fix now:
  - `current_asset_map_v1` active guidance 보강
  - `repo_delta_log_latest_v1` recent 중심으로 압축
- next action:
  - 위 두 문서만 수정
  - 전체 repo 재설명 금지

---

## 예시 C. 역할 혼합

상황:
- pack/index/current/delta가 서로 중복 장문으로 커짐
- official surface가 무엇인지 모호함

출력 요지:
- overall verdict: `REBASE_REQUIRED`
- must-fix now:
  - pack/index 역할 재분리
  - current/delta 역할 재분리
- next action:
  - 기준면 재정렬 턴 필요
  - 코어 변경은 하지 않음

---

## 10. 최종 잠금 문장

앞으로 CODEx는 변경이 생길 때마다
**“무엇이 바뀌었는가”보다 먼저 “어느 기준면이 영향을 받았는가”를 판정**해야 한다.

그리고 판정 결과가 기준면 유지/갱신이라면,
**전체 repo를 다시 설명하지 말고 관련 문서 1~2개만 짧고 정확하게 수정**해야 한다.

한 줄로 잠그면:

> 기준면 점검은 구조 발명이 아니라 drift 감지와 역할 유지의 문제이며, current/delta/shared reality/next phase를 섞지 않는 짧은 maintenance가 정답이다.
