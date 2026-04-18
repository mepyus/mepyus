# repo_shared_reality_pack_v1

- source_asset_group: `baselines`
- source_asset_path: `source_assets/baselines/repo_shared_reality_pack_v1.md`

## 0. 목적

이 문서 묶음의 목적은 하나다.

**코덱스는 실제 폴더를 보고 수정하고,
사용자와 어시스턴트는 전체 트리를 매번 직접 보지 못하는 조건에서도
셋이 같은 구조 현실을 보며 작업하게 만드는 것**

즉 이 pack은
“전체 폴더 트리를 매번 덤프하지 않고도”
현재 repo의 구조 상태와 핵심 자산 위치를 공유하기 위한
**공통 현실면(shared reality surface)** 이다.

## 1. 왜 필요한가

현재 문제는 기능 부족이 아니다.

문제는 다음과 같다.

- 코덱스는 실제 폴더를 본다
- 사용자와 어시스턴트는 매번 전체 폴더를 보지 않는다
- 그래서 같은 repo를 두고도 서로 다른 현실을 상상할 수 있다

이 상태가 길어지면:

- 기준문은 맞는데 실제 위치가 다르고
- 실제 파일은 이동했는데 대화 기준은 옛 구조에 머물고
- 폴더 역할은 정리됐는데 변경 내역이 공유되지 않아
- 셋이 같은 방향이라 생각해도 실제로는 조금씩 어긋난다

따라서 앞으로는
**full tree 공유**보다
**작고 고정된 구조 현실 문서 세트**를 유지하는 방식으로 간다.

## 2. pack의 핵심 구성

이 pack은 최소 5개 문서로 고정한다.

### A. intake 기준문
- `docs/policies/engine_input_lane_baseline_v1.md`

### B. workspace 승격 기준문
- `docs/policies/codex_baseline_program_grade_workspace_upgrade_v1.md`

### C. 폴더 역할표
- `docs/specs/folder_role_table_v1.md`

### D. current asset map
- `runtime/views/current_asset_map_v1.md`

### E. delta log
- `runtime/views/repo_delta_log_latest_v1.md`

## 3. 운영 원칙

- 실제 수정은 코덱스가 한다.
- 수정 후 현실 설명은 `current_asset_map` 과 `delta_log` 에 남긴다.
- 사용자와 어시스턴트는 full tree 대신 shared reality pack을 우선 현실면으로 본다.

## 4. 최종 잠금

앞으로는 full tree dump를 공통 현실로 삼지 않는다.

대신
**정책 기준문 + 폴더 역할표 + 현재 자산 지도 + 최근 변경 로그**
이 네 축을 유지해서
코덱스와 사용자와 어시스턴트가 같은 repo 현실을 바라보게 만든다.

한 줄로 잠그면:

**repo_shared_reality_pack_v1은 “전체 폴더를 매번 다시 보여주지 않아도 셋이 같은 구조 현실을 공유하게 만드는 최소 문서 세트”다.**
