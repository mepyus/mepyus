[[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]]
[[A]] [[OBJ:program_operation_upgrade_baseline]] [[SEM:delta_based_program_operation]] [[ROLE:directive]]

# PROGRAM-LEVEL UPGRADE BASELINE + CODEX DIRECTIVE V1
# 주제: 전체 재스캔 중심 운용에서 변화분 중심 프로그램 운용으로 전환

## 0. 선언
이제부터 현재 repo/workspace를 “문서와 스크립트의 묶음”이 아니라
**지속적으로 입력되고, 기록되고, 갱신되고, 확인되는 프로그램 단 운영체계**로 취급한다.

이 선언의 의미는 단순히 파일 수가 늘었다는 뜻이 아니다.

의미는 아래와 같다.

- 구조는 더 이상 임시 조합물이 아니다
- 변경은 우연히 쌓이는 것이 아니라 추적 가능한 사건이어야 한다
- 사람이 읽는 설명문과 시스템이 들고 있는 원장은 분리되어야 한다
- 전체를 매번 다시 읽어 파악하는 방식은 점차 중단해야 한다
- 앞으로의 추가 규칙/폴더/문서는 “변화분 반영 + 국소 갱신” 원칙 위에서 들어와야 한다

한 줄 선언:
**이제부터 우리의 운용 기준은 전체 재독해가 아니라, 변화분 기록과 부분 갱신을 기본으로 하는 프로그램 단 운영이다.**

---

## 1. 현재 판단
현재까지 잠긴 구조는 다음과 같다.

- structured doc routing 안정화
- receipt / board / commands / per-run surface 정리
- provenance hygiene 레이어 추가
- latest pointer surface 정리
- Codex ↔ Gemini 세션 배치 운영 계약 고정
- Gemini observer 로그 위치 고정
- guides / contracts / policies / reports 역할 분리 시작

즉, 현재 상태는 “불안정한 실험 묶음” 단계를 벗어나
**운영 흐름을 가진 프로그램형 작업공간**으로 읽는 것이 맞다.

하지만 아직 남은 약점은 분명하다.

### 현재 약점
- 새로운 폴더/문서/규칙이 생길 때 전체를 다시 읽는 부담이 크다
- folder_status.md류가 원장처럼 오해될 수 있다
- 변화가 append-only로 남는 구조가 폴더 단위로는 아직 얇다
- “현재 상태”와 “변화 이력”과 “사람이 읽는 설명”이 완전히 분리되지 않았다

따라서 다음 단계는 기능 확장이 아니라
**프로그램 단 안정 운용을 위한 변화분 관리 레이어**를 추가하는 것이다.

---

## 2. 최상위 기준
앞으로 폴더/규칙/문서/상태 갱신은 아래 기준을 따른다.

### 기준 1 — 전체 재스캔을 기본으로 하지 않는다
- 전체 폴더를 매번 다시 읽는 방식은 예외 상황에서만 허용한다
- 기본은 변화분 append + 국소 갱신이다

### 기준 2 — 원장과 사람이 보는 문서를 분리한다
- 원장 = json/jsonl manifest/change log
- 사람이 보는 문서 = md status/guide/summary
- 사람이 보는 문서는 원장이 아니라 렌더된 읽기면이다

### 기준 3 — 새 사실은 append-only change log에 먼저 남긴다
새로 생긴 폴더/문서/규칙/자산은 먼저 사건으로 기록된다.

예:
- folder_created
- doc_created
- rule_added
- rule_updated
- asset_registered
- folder_renamed

### 기준 4 — 현재 상태는 inventory manifest로 유지한다
각 폴더/영역의 현재 상태는 inventory manifest가 든다.
이 manifest는 구조적 현재 상태 스냅샷이다.

### 기준 5 — status 문서는 manifest에서 렌더한다
folder_status.md 같은 문서는 직접 원장이 아니다.
inventory와 change log를 보고 다시 그리는 얇은 문서다.

### 기준 6 — 갱신 범위는 바뀐 폴더와 부모 몇 단계만
- 변경이 생기면 해당 폴더 inventory 갱신
- 필요시 부모 1~2단계 inventory 갱신
- 전체 repo 재빌드는 기본 금지

### 기준 7 — 프로그램화 우선
앞으로 새 구조를 추가할 때는 “설명문 하나 더”보다
“어떤 변화가 생겼고 어디를 갱신해야 하는가”를 먼저 구조화한다.

---

## 3. 프로그램 단 운용 구조
이제부터 아래 3층을 명확히 나눈다.

### A. 변화 이력층 (change layer)
무슨 일이 생겼는지 append-only로 기록한다.

예상 위치:
- `runtime/manifests/folder_changes/folder_change_log.jsonl`

이 층의 역할:
- 사건 기록
- 변경의 순서 보존
- 감사/복기 가능성 유지

### B. 현재 상태층 (inventory layer)
각 폴더/영역의 현재 상태를 구조적으로 유지한다.

예상 위치:
- `runtime/manifests/folder_inventory/`

예상 파일 예:
- `docs.guides.json`
- `docs.contracts.json`
- `runtime.observer.gemini.json`
- `runtime.views.json`

이 층의 역할:
- 현재 자산 목록
- 최근 변경 시각
- 부모/자식 관계
- 관련 문서/자산/규칙 메타

### C. 사람용 읽기층 (status/render layer)
사람이 읽기 쉽게 보여주는 상태 문서다.

예:
- `folder_status.md`
- 요약 문서
- 가이드 문서 일부 상태 섹션

이 층의 역할:
- 읽기
- 탐색
- 빠른 이해

중요:
**읽기층은 원장이 아니라 렌더 결과다.**

---

## 4. Codex 작업 원칙
앞으로 Codex는 새 폴더/문서/규칙이 생길 때 아래 원칙을 따른다.

### 4.1 새 사실 발생 시 먼저 사건으로 남긴다
예:
- 문서 생성
- 폴더 생성
- 규칙 추가
- 계약 문서 추가
- 운영 가이드 추가

이런 변화가 있으면 먼저 change log 관점으로 읽는다.

### 4.2 해당 영역 inventory를 갱신한다
예:
- `docs/guides/quick_start.md` 생성 시
  - `docs.guides.json` 갱신
  - 필요시 `docs.json` 갱신

### 4.3 사람용 status/render 문서를 갱신한다
필요한 범위의 folder_status.md 또는 상태 문서를 렌더한다.

### 4.4 전체 재스캔은 하지 않는다
정상 흐름에서는 바뀐 폴더와 부모만 갱신한다.

---

## 5. Codex에게 내리는 이번 지시
이번 턴의 목적은 “변화분 중심 프로그램 운용”을 실제 작업공간 기준으로 시작하는 것이다.

### 반드시 할 일
아래를 우선 설계/생성/고정한다.

#### 5.1 folder change log 레이어 추가
생성 대상 예:
- `runtime/manifests/folder_changes/`
- `runtime/manifests/folder_changes/folder_change_log.jsonl`

최소 이벤트 타입 예:
- folder_created
- doc_created
- doc_updated
- rule_added
- rule_updated
- asset_registered
- folder_renamed

#### 5.2 folder inventory manifest 레이어 추가
생성 대상 예:
- `runtime/manifests/folder_inventory/`

최소 manifest 예:
- `docs.guides.json`
- `docs.contracts.json`
- `runtime.observer.gemini.json`

각 manifest 최소 필드 예:
- folder_key
- folder_path
- child_folders
- documents
- assets
- last_updated
- parent_folder
- related_status_files

#### 5.3 sync 스크립트 방향 전환
대상 예:
- `scripts/folder_status_sync.py`

변경 방향:
- 전체 스캔기 → 변화분 반영기 + status renderer

즉, 새 이벤트나 새 자산 입력 시:
- change log append
- 관련 inventory 갱신
- 관련 status 문서 재생성

#### 5.4 folder_status.md 해석 고정
folder_status.md는 원장이 아니라 읽기면이라는 점을
문서/코드/주석 수준에서 분명히 잠근다.

#### 5.5 guides/계약/observer 쪽 최소 실험 적용
최소 1~2개 실제 폴더를 대상으로
변화분 반영 흐름이 작동하는지 검증한다.

권장 대상:
- `docs/guides`
- `runtime/observer/gemini`

---

## 6. 이번 턴에서 하지 말 것
아래는 지금 하지 않는다.

- repo 전체 재구성
- 기존 모든 폴더 status 완전 재작성
- 대규모 schema generalization
- 분산 시스템 수준 동기화 설계
- DB 도입
- watcher/daemon 자동화
- UI 편입

즉 이번 턴은
**작동 가능한 최소 변화분 관리 레이어를 붙이는 턴**이다.

---

## 7. 최소 성공 기준
이번 턴이 성공으로 판정되려면 최소 아래를 만족해야 한다.

### required minimum
- change log 파일/폴더가 생긴다
- folder inventory manifest 구조가 생긴다
- 특정 폴더에 대한 inventory 파일이 최소 2개 이상 생성된다
- sync 스크립트가 전체 스캔기가 아니라 변화분 반영기로 해석 전환된다
- folder_status.md가 원장이 아니라 render 문서라는 기준이 명확해진다

### strong success
- 새 문서 1개 추가 시 change log append 확인
- 해당 폴더 inventory만 갱신됨
- 부모 폴더 inventory가 제한 범위로 갱신됨
- 사람용 status 문서가 재렌더됨
- 전체 repo 재스캔 없이 흐름이 끝남

---

## 8. 추천 테스트 시나리오
Codex는 아래 같은 최소 시나리오를 돌려 확인한다.

### 시나리오 A — guides 문서 추가
- `docs/guides/` 아래 새 문서 생성
- change log에 `doc_created` append
- `docs.guides.json` 갱신
- 필요시 `docs.json` 갱신
- 관련 status 문서 갱신
- 전체 재스캔 없음 확인

### 시나리오 B — gemini observer 문서 추가
- `runtime/observer/gemini/` 아래 새 session 로그 생성
- change log append
- `runtime.observer.gemini.json` 갱신
- observer 관련 읽기면 갱신 가능 여부 확인

---

## 9. 운영 철학 잠금
이 기준은 단순히 파일 정리 편의를 위한 것이 아니다.

앞으로 우리는 다음 관점으로 간다.

- 작업공간은 누적되는 프로그램이다
- 변화는 사건으로 기록된다
- 현재 상태는 구조적 inventory로 유지된다
- 사람이 읽는 문서는 그 위에 얹힌 얇은 렌더다
- 안정성은 전체를 반복해서 읽는 데서 오지 않고, 변화를 구조적으로 받는 데서 온다

한 줄로:
**이제부터 우리는 “파일 묶음 관리”가 아니라 “변화분 기반 프로그램 운용”을 한다.**

---

## 10. 최종 잠금 문장
가장 중요한 문장은 아래다.

**전체를 매번 다시 읽지 말고,  
변화는 append하고, 현재 상태는 inventory로 유지하며,  
사람이 보는 상태 문서는 그 결과를 얇게 렌더하라.**

최종 한 줄:
**이제부터 프로그램 단 안정 운용의 기준은 전체 재독해가 아니라 변화분 기록 + 부분 갱신 + 읽기면 렌더다.**
