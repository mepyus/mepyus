# repo_shared_reality_pack_index_v1

## 0. 목적

이 문서는 repo 전체 폴더 트리를 매번 다시 보지 않아도
사용자 / 어시스턴트 / 코덱스가 **같은 구조 현실**을 보며 작업하게 만드는
`repo_shared_reality_pack_v1` 의 **인덱스 문서**다.

즉 이 문서는 개별 기준문을 대체하지 않는다.
대신 아래를 한 번에 보여준다.

- 어떤 문서들이 shared reality pack을 이루는가
- 각 문서의 역할은 무엇인가
- 무엇을 먼저 읽어야 하는가
- 무엇이 바뀌면 어떤 문서를 갱신해야 하는가

## 1. pack 구성 문서

### 1-1. intake 기준문
- path: `docs/policies/engine_input_lane_baseline_v1.md`
- 역할: 입력 lane 정의 / 입력 분류 혼잡 방지 / 미분류 허용 기준
- 한 줄: 입력이 늘어나도 intake가 무너지지 않게 하는 기준

### 1-2. workspace 승격 기준문
- path: `docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md`
- 역할: repo를 파이프라인 묶음이 아니라 프로그램형 작업공간으로 읽는 상위 기준
- 한 줄: 기능 추가보다 구조 고정을 먼저 하게 만드는 기준

### 1-3. 폴더 역할표
- path: `docs/specs/folder_role_table_v1.md`
- 역할: 폴더 책임 / 파일 배치 / 금지 혼합 규칙
- 한 줄: 새 파일과 새 폴더가 어디에 가야 하는지 판단하는 표

### 1-4. current asset map
- path: `runtime/views/current_asset_map_v1.md`
- 역할: 지금 repo를 어떻게 읽어야 하는지 보여주는 공식 현재 현실면
- 한 줄: 지금 기준으로 무엇이 SSOT이고 무엇이 핵심인지 알려주는 지도

### 1-5. delta log latest
- path: `runtime/views/repo_delta_log_latest_v1.md`
- 역할: 최근 구조 변화와 읽기 우선순위 변화 요약
- 한 줄: 최근 무엇이 바뀌었고 이제 무엇을 먼저 읽어야 하는지 알려주는 변화면

### 1-6. operating layer freeze
- path: `docs/specs/engine_operating_layer_freeze_v1.md`
- 역할: 현재 engine stack의 authoritative core / derived / surface / experimental 경계를 공식 고정
- 한 줄: 무엇이 원장이고 무엇이 파생층인지 흔들리지 않게 잠그는 기준

### 1-7. operating layer manifest
- path: `runtime/views/engine_operating_layer_manifest_v1.json`
- 역할: 현재 operating layer 분할과 hierarchy를 machine-readable하게 보여주는 manifest
- 한 줄: process console stack의 현재 구조를 빠르게 확인하는 manifest

### 1-8. engine memory spine
- path: `runtime/views/engine_memory_spine_v1.json`
- 역할: 철학 방향성 / 사용자 문제 인식 / 자원 경계 / 에피소드 기억 / current reality를 어떤 층으로 외부화해 기억하는지 보여주는 memory spine
- 한 줄: 메모리 한계가 있어도 엔진이 같은 철학과 문제 인식으로 복귀하게 만드는 기억 spine

## 2. pack 전체 한 줄 읽기

이 pack은
**정책 기준문 + 배치 기준 + 현재 구조 지도 + 최근 변경 요약 + operating layer freeze + memory spine**
을 묶어서
full tree dump 없이도 셋이 같은 repo 현실을 공유하게 만드는 최소 문서 세트다.

## 3. 읽기 순서

### 3-1. 사용자 기본 읽기 순서
1. `runtime/views/repo_shared_reality_pack_index_v1.md`
2. `runtime/views/current_asset_map_v1.md`
3. `runtime/views/repo_delta_log_latest_v1.md`
4. `docs/specs/engine_operating_layer_freeze_v1.md`
5. `runtime/views/engine_memory_spine_v1.json`
6. 필요 시 `docs/policies/engine_input_lane_baseline_v1.md`
7. 필요 시 `docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md`
8. 배치가 헷갈리면 `docs/specs/folder_role_table_v1.md`

### 3-2. 어시스턴트 기본 읽기 순서
1. `repo_shared_reality_pack_index_v1`
2. `current_asset_map_v1`
3. `repo_delta_log_latest_v1`
4. `engine_operating_layer_freeze_v1`
5. `engine_memory_spine_v1`
6. 충돌 시 intake baseline
7. 충돌 시 workspace baseline
8. 경로/배치 판단 시 folder role table

### 3-3. 코덱스 기본 운용 순서
1. 실제 폴더/파일 수정
2. 구조 영향 판단
3. `current_asset_map_v1.md` 갱신
4. `repo_delta_log_latest_v1.md` 갱신
5. 기억 구조가 바뀌면 `engine_memory_spine_v1.json` 갱신
6. layer 경계가 바뀌면 `engine_operating_layer_freeze_v1.md` 또는 manifest 갱신
7. 필요 시 policy/spec 문서 갱신

## 4. 문서별 질문

### engine_input_lane_baseline_v1.md 가 답하는 질문
- 이 입력은 무슨 lane인가
- 미분류도 받을 수 있는가
- 외부자료는 어떻게 받아야 하는가
- 입력 증가와 core 승격은 어떻게 분리하는가

### codex_baseline_program_grade_workspace_upgrade_v1.md 가 답하는 질문
- 지금 repo를 어떤 작업공간으로 봐야 하는가
- 왜 구조 고정이 기능 추가보다 먼저인가
- 어떤 변경은 허용되고 어떤 변경은 보류되는가

### folder_role_table_v1.md 가 답하는 질문
- 새 파일을 어디에 둬야 하는가
- 어떤 폴더에 무엇을 두면 안 되는가
- 원본 / latest / work / 정책 문서를 어떻게 분리하는가

### current_asset_map_v1.md 가 답하는 질문
- 지금 기준으로 무엇이 SSOT인가
- 지금 핵심 entrypoint는 무엇인가
- 지금 locked / work / caution zone은 어디인가
- 지금 무엇을 먼저 읽어야 하는가

### repo_delta_log_latest_v1.md 가 답하는 질문
- 최근 무엇이 바뀌었는가
- 이 변경은 구조 영향이 큰가 작은가
- 이제 무엇을 더 이상 primary로 읽지 말아야 하는가

### engine_operating_layer_freeze_v1.md 가 답하는 질문
- 무엇이 authoritative core인가
- 무엇이 derived operating layer인가
- process console은 어떤 위상인가
- experimental은 왜 격리되는가

### engine_memory_spine_v1.json 이 답하는 질문
- 무엇을 어디에 외부화해 기억해야 하는가
- 컨텍스트가 흔들릴 때 어떤 순서로 복귀해야 하는가
- 철학 / 문제 인식 / 자원 경계 / run 기억 / current reality가 어떤 층으로 나뉘는가

## 5. update trigger

아래 중 하나가 생기면 shared reality pack 갱신을 검토한다.

### trigger A. 핵심 정책/명세 문서 추가
예:
- 새로운 baseline 추가
- intake 규칙 변경
- 폴더 책임 변경

### trigger B. 핵심 entrypoint 변경
예:
- intake 스크립트 변경
- runtime view 생성 경로 변경
- registry/provenance 핵심 경로 변경

### trigger C. primary current view 변경
예:
- 새로운 current map 도입
- 기존 latest view 퇴역
- current read order 변경

### trigger C-2. operating layer boundary 변경
예:
- core / derived / surface / experimental 경계 변경
- process console의 본체 위치 변경
- derived artifact의 권한 변경

### trigger D. 역할 이동
예:
- 파일 이동
- 폴더 역할 변경
- latest/raw/work 경계 재배치

### trigger E. 구조 오해 가능성 발생
예:
- 사용자나 어시스턴트가 이전 구조를 계속 믿으면 오해가 생길 상황

### trigger F. memory recovery path 변경
예:
- 철학 방향성 기억 위치 변경
- 사용자 문제 인식 기억 추가/변경
- 외부 자원 위임 기준 기억 추가
- context recovery order 변경

## 6. update responsibility

### 코덱스
- 실제 수정 담당
- 수정 후 current_asset_map / delta_log 갱신
- 기억 spine 변화가 있으면 memory spine 갱신
- 구조 기준이 바뀌면 policy/spec도 갱신
- operating layer boundary가 바뀌면 freeze spec / manifest도 갱신

### 사용자
- full tree를 매번 올리지 않아도 됨
- shared reality 문서가 갱신되었는지만 확인하면 됨
- 큰 방향/기준 충돌 시 policy 문서 재확인

### 어시스턴트
- 구조 판단 시 shared reality pack을 공식 현실면으로 취급
- 이전 대화 기억보다 current map / delta log 우선
- 새 제안 시 기존 pack과 충돌 여부 먼저 확인

## 7. maintenance routine

### 최소 유지 루틴
1. 코덱스 수정
2. delta log 갱신
3. current asset map 갱신
4. layer 경계 영향 있으면 freeze spec / manifest 갱신
5. policy/spec 영향 있으면 기준문 갱신
6. 사용자와 어시스턴트는 current map 기준으로 재정렬

### 권장 원칙
- 모든 수정 뒤 full tree 공유를 요구하지 않는다
- 구조가 바뀐 경우 shared reality pack만 갱신한다
- current map은 “지금 기준”
- delta log는 “왜 이렇게 됐는가”
- policy/spec는 “어떤 원칙으로 유지되는가”
- freeze/manifest는 “어느 층이 authoritative인가”

## 8. 현재 pack의 위상

이 pack은 보조 문서 묶음이 아니다.
이 pack은 앞으로 다음 역할을 한다.

- 코덱스와 사용자와 어시스턴트의 공통 구조 지도
- 폴더를 직접 못 보더라도 같은 방향을 보게 하는 현실면
- 입력 증가와 구조 정리를 함께 버티게 하는 최소 장치

즉 shared reality pack이 없으면
실제 repo와 대화 속 repo가 서서히 분리될 가능성이 높다.

## 9. 운용 금지선

### 금지 1
pack 문서를 안 갱신한 채 실제 구조만 바꾸지 않는다

### 금지 2
current_asset_map 없이 old latest 문서를 current primary처럼 쓰지 않는다

### 금지 3
delta log 없이 구조 변경을 “대화로만” 넘기지 않는다

### 금지 4
새 기준문을 만들고 pack index에 반영하지 않은 채 흩뿌리지 않는다

## 10. 최종 잠금

`repo_shared_reality_pack_v1` 은
repo 전체를 매번 다시 보여주지 않아도
사용자 / 어시스턴트 / 코덱스가 같은 구조 현실을 공유하게 만드는 최소 문서 세트다.

그리고 이 `repo_shared_reality_pack_index_v1.md` 는
그 문서 세트를 한 번에 가리키는 **공식 입구 문서**다.

한 줄로 잠그면:

**앞으로 repo 구조 현실은 full tree dump가 아니라, shared reality pack index와 그 하위 문서들을 통해 공유한다.**

현재 addendum 한 줄:

**이 pack은 이제 state-first process console 엔진의 `current map + delta + layer freeze`를 함께 묶어 공유하는 공식 구조 현실면이다.**
