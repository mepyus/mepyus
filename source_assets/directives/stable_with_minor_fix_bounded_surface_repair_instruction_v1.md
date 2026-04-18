[[A]] [[OBJ:codex_directive]] [[SEM:stable_with_minor_fix_bounded_surface_repair_instruction]]

# CODEx 지시서 — STABLE_WITH_MINOR_FIX 기준면 보수 지시서 v1

## 0. 목적
이번 턴의 목적은 새 구조를 만들거나 코어를 손보는 것이 아니다.

현재 체크리스트 판정은 아래와 같다.

- overall verdict: `STABLE_WITH_MINOR_FIX`
- 즉, 기준면은 살아 있으나 일부 surface가 현재 repo 현실과 조금 어긋나 있거나,
  latest 성격이 앞으로 흐려질 위험이 있다.

따라서 이번 턴의 목표는 오직 2개다.

1. `docs/specs/folder_role_table_v1.md`
   - 현재 repo 현실과 더 정확히 맞춘다
2. `runtime/views/repo_delta_log_latest_v1.md`
   - recent 중심으로 더 짧고 선명하게 압축한다

한 줄로 말하면:

> 이번 작업은 코어 수정이 아니라, `STABLE_WITH_MINOR_FIX` 상태를 `LOCKED` 쪽으로 밀기 위한 bounded surface repair다.

---

## 1. 현재 잠금 상태

### 이미 PASS로 잠긴 축
- `docs/policies/engine_input_lane_baseline_v1.md`
- `docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md`
- `source_assets/baselines/repo_shared_reality_pack_v1.md`
- `source_assets/declarations/program_grade_next_phase_declaration_v1.md`
- `source_assets/directives/program_grade_workspace_surface_maintenance_directive_v1.md`

### REVIEW_REQUIRED로 나온 축
- `docs/specs/folder_role_table_v1.md`
- `runtime/views/repo_shared_reality_pack_index_v1.md`
- `runtime/views/current_asset_map_v1.md`
- `runtime/views/repo_delta_log_latest_v1.md`

하지만 이번 턴은 범위를 넓히지 않는다.

---

## 2. 이번 턴 범위

## 2-1. 수정 대상
반드시 아래 2개만 우선 보수한다.

1. `docs/specs/folder_role_table_v1.md`
2. `runtime/views/repo_delta_log_latest_v1.md`

## 2-2. 필요 시 연동 점검만 허용
아래는 **읽기/점검만 허용**한다.

- `runtime/views/current_asset_map_v1.md`
- `runtime/views/repo_shared_reality_pack_index_v1.md`

즉, 이번 턴에서 저 두 문서는 원칙적으로 수정 대상이 아니다.
다만 실제로 2개 보수 후 충돌 여부 확인은 할 수 있다.

---

## 3. 절대 금지

이번 턴에서 아래는 금지다.

- 코어 로직 수정
- ingest / registry / event / provenance spine 수정
- shared reality 정의 전체 재작성
- current asset map 전면 재작성
- repo 전체 구조 장문 재설명
- page / read-only operation view 확장
- 새 기준 문서 다량 추가
- 문제를 이유로 전체 baseline 철학을 다시 쓰는 것

이번 턴은 **bounded repair**여야 한다.

---

## 4. 작업 1 — folder_role_table 현실화

대상:
- `docs/specs/folder_role_table_v1.md`

## 4-1. 목적
이 문서는 “이 자산을 어디에 두는가”에 대한 현실 기준표여야 한다.
이번 보수의 목적은 이 표를 현재 실제 repo 운영 현실과 더 정확히 맞추는 것이다.

## 4-2. 중점 점검 항목
아래를 기준으로 현재 표를 다시 본다.

- source asset
  - baseline
  - directive
  - declaration
- docs asset
  - policy
  - spec
  - report
  - guide
- runtime asset
  - current view
  - delta/latest view
  - receipt
  - raw log
- inputs asset
  - canonical input
  - derived artifact와의 분리
  - legacy residue와 current official input의 구분

## 4-3. 반드시 보강해야 할 읽기
아래 차이를 문서 안에서 더 현실적으로 드러내야 한다.

### A. source vs docs vs runtime 차이
- `source_assets/*` 는 운영 입력/기준 자산
- `docs/*` 는 정책/명세/리포트
- `runtime/views/*` 는 현재 읽기면
- `runtime/receipts/*` 는 실행 흔적
- `runtime/logs/*` 는 raw append-only 기록

### B. active guidance와 보고서의 차이
- directive/declaration은 기준 입력 자산이다
- report는 결과 보고다
- report가 기준을 대체하면 안 된다

### C. official surface와 residue의 차이
- 현재 공식 기준 자산
- 과거 흔적/잔존 자산
- no-longer-primary 성격 자산

이 셋이 한 덩어리로 읽히지 않게 해야 한다.

---

## 5. 작업 2 — repo_delta_log_latest recent 중심 압축

대상:
- `runtime/views/repo_delta_log_latest_v1.md`

## 5-1. 목적
이 문서는 “최근 변화”를 보여주는 latest surface여야 한다.
지금의 목적은 이 문서를 장기 연혁 문서가 아니라 **진짜 recent delta surface**로 더 선명하게 만드는 것이다.

## 5-2. 압축 원칙

### 원칙 A. recent만 남긴다
- 최신성에 직접 관련 있는 변화만 유지
- 오래된 묶음 설명은 줄이거나 제거
- 상세 연혁은 `runtime/logs/repo_delta_log.jsonl` 쪽을 근거로 남기고,
  latest는 요약만 유지

### 원칙 B. current 설명을 복사하지 않는다
- `current_asset_map_v1.md`가 말해야 할 내용을 delta에 장문으로 중복하지 않는다
- delta는 “왜/무엇이 바뀌었는가”에 집중한다

### 원칙 C. added asset / must-know / follow-up를 짧게 유지한다
- asset 추가 사실
- 그 변화의 의미
- 바로 알아야 할 운영 원칙
만 남긴다

---

## 6. 작업 순서

1. 현재 체크리스트 결과 다시 확인
2. `folder_role_table_v1.md` 현실화 보수
3. `repo_delta_log_latest_v1.md` recent 중심 압축
4. 수정 후 아래 2개를 읽기 점검
   - `runtime/views/current_asset_map_v1.md`
   - `runtime/views/repo_shared_reality_pack_index_v1.md`
5. 역할 충돌이 없으면 종료
6. 필요 시 delta/raw log에 짧게 기록

---

## 7. 출력물

### 필수
- 수정된 `docs/specs/folder_role_table_v1.md`
- 수정된 `runtime/views/repo_delta_log_latest_v1.md`

### 선택
- 짧은 점검/결과 보고 1개
- receipt / raw delta 기록

### 금지
- 새 철학 문서 다량 생성
- current asset map 전체 재설명 보고서
- shared reality 전면 개정 문서

---

## 8. 최종 운영 문장

이번 턴 이후 CODEx는
**“무언가가 바뀌면 전체 repo를 다시 설명하는 방식”**이 아니라,

**“바뀐 사실이 어느 기준면에 속하는지 먼저 판정하고, 해당 기준 자산만 짧고 정확하게 갱신하는 방식”**
으로 움직여야 한다.

한 줄로 잠그면:

> 코어는 보존하고, 외곽 운영 기준면은 역할별로 분리 유지하며, 변경이 생길 때마다 current/delta/shared reality를 짧고 정확하게 갱신하라.
