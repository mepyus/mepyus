# process reread map v1

## 1. 이 문서의 목적

이 문서는 결과 요약이 아니라 과정 재독해용 내부 지도다.

목적은 다음을 나중에 다시 따라 읽게 하는 것이다.

- 우리가 무엇을 만들려고 했는지
- 왜 자꾸 어긋났는지
- 어떤 전환점을 지나 지금의 내부 장치가 생겼는지
- 어떤 것들이 실제로 살아 있고 무엇이 아직 관찰 단계인지

즉 이 문서는 "무엇이 끝났는가"보다 "무엇이 어떻게 발생했는가"를 다시 볼 수 있게 만드는 지도다.

## 2. 시작 질문

처음의 문제는 단순 기능 부족이 아니었다.

문제는 자료가 없어서가 아니라, 추론이 올라설 바닥이 없어서 자꾸 눈앞 해결로 좁아졌다는 점이었다.

그래서 질문은 자연스럽게 바뀌었다.

- 답변 잘하는 시스템이 아니라 무엇을 읽고 어떻게 축적하는 구조가 필요한가
- 기억을 많이 먹여 보정하는 게 아니라 내부 장기를 먼저 만들 수 있는가
- LLM이 나중에 붙더라도, 그 전에 공간 내부에서 읽기 흔적과 경로가 자랄 수 있는가

이 질문이 "내 공간 위에서 추론"으로 이어졌다.

## 3. 주요 전환점

### 3.1 공간만 보고 있었고 눈이 없었다는 자각

공간은 있었지만, 읽기 전에 모드/국면/드리프트를 선행 제어하는 시야가 없었다.

이때 필요한 것은 더 많은 설명이 아니라, 읽기 시작 전에 방향을 정하는 눈이었다.

### 3.2 감독 렌즈 형성

active asset 판정 과정에서 다음 순서가 잠겼다.

`binding closed -> semantic fidelity -> output-worthiness -> meaning-context sufficiency -> detector -> widening trigger`

이 렌즈가 생기면서, 닫힘 여부와 의미 충실도를 분리해 읽게 되었다.

### 3.3 제어면 필요성 등장

읽기 전에 mode와 drift를 먼저 정해야 했다.

그래서 control plane이 생겼다.

- `space_kernel`
- `turn_router`
- `drift_guard`
- `current_phase`

제어면은 설명문이 아니라 pre-read gate가 되었다.

### 3.4 breadcrumbs 필요성 등장

읽은 결과만 남기면 왜 그 경로를 탔는지 잃는다.

그래서 breadcrumbs가 생겼다.

이 층은 단순 로그가 아니라 판단 이동 경로를 남기는 장치가 되었다.

### 3.5 제어면만으로는 부족하다는 자각

제어면이 모드를 정해도, 아직 해석과 계보가 비어 있었다.

그래서 interpretation packets, decision lineage, multi-lens views의 바닥을 얇게 깔기 시작했다.

### 3.6 candidate / boundary / watch rule가 생긴 이유

raw_to_first_pass_to_report 같은 경로는 반복되었지만, 처음부터 lock할 수는 없었다.

그래서:

- candidate summary
- boundary note
- watch rule

로 나눠서 관찰하게 되었다.

핵심은 억지로 후보를 만드는 것이 아니라, 어디까지가 같은 경로인지 경계부터 확인하는 것이었다.

### 3.7 “후보를 억지로 만들지 않는다”는 원칙

두 번째 candidate는 쉽게 만들어지지 않았다.

그 대신:

- existing candidate와 boundary note로 접히는지
- mode-scoped boundary인지
- 아직 seed가 아닌지

를 먼저 확인하는 방식이 생겼다.

## 4. 실제 생긴 내부 장치

### 4.1 control plane

- 무엇인가: 읽기 전에 mode, phase, drift를 정하는 제어면
- 왜 생겼는가: 자료를 먼저 읽고 나중에 모드를 붙이는 드리프트를 막기 위해
- 무엇을 보완하는가: pre-read 분기, drift guard, current phase 고정
- 현재 상태: 실제 preflight gate로 작동
- 한계: 아직 파일/스크립트 수준의 gate이며 전역 middleware는 아님

### 4.2 runtime preflight gate

- 무엇인가: control plane을 읽고 first read target을 정하는 실행 전 분기
- 왜 생겼는가: mode/selection/guard가 실제 읽기 전에 작동하는지 확인하기 위해
- 무엇을 보완하는가: selected_mode, selected_artifact_group, first_read_ref, guard_actions
- 현재 상태: family-cross validation까지 PASS
- 한계: 아직 observation-only 경로 위주

### 4.3 breadcrumbs

- 무엇인가: 왜 읽었는지, 무엇을 봤는지, 다음으로 왜 이동했는지 남기는 판단 이동 로그
- 왜 생겼는가: 결과만 남기면 경로를 잃기 때문
- 무엇을 보완하는가: path recovery, drift repair, next hop traceability
- 현재 상태: gate-level breadcrumb가 실제로 쌓임
- 한계: 아직 thick lineage는 아님

### 4.4 pipeline observation registry

- 무엇인가: raw_to_first_pass_to_report 같은 경로 후보를 observation으로 누적하는 얇은 기록면
- 왜 생겼는가: 반복을 세되 lock은 하지 않기 위해
- 무엇을 보완하는가: family/mode/first_read_ref/next_hop/boundary_note 기록
- 현재 상태: observation-only
- 한계: 승격 전 상태라 lock candidate 아님

### 4.5 pipeline candidate scope summary

- 무엇인가: registry row를 한 장으로 읽는 mode-scoped summary
- 왜 생겼는가: registry 전체를 뒤지지 않고 후보의 성립 조건과 경계를 보기 위해
- 무엇을 보완하는가: intended_mode_scope, valid_artifact_groups, divergent_modes, boundary_notes
- 현재 상태: raw_to_first_pass_to_report에 대해 존재
- 한계: candidate 선언문이 아니라 scope 설명면

### 4.6 second candidate watch rule

- 무엇인가: 두 번째 reading path candidate가 언제 발생했다고 부를지 정하는 얇은 감시 규칙
- 왜 생겼는가: 억지 후보 생성을 막고, seed 발생 시점만 늦게 잡기 위해
- 무엇을 보완하는가: current_clear_candidates, minimum_repeat_requirement, disqualifiers
- 현재 상태: append observation path에 연결됨
- 한계: 아직 second seed는 없음

### 4.7 watch rule auto connection

- 무엇인가: 새 observation이 들어올 때 watch rule을 자동 평가하는 연결
- 왜 생겼는가: 사람이 매번 따로 판정하지 않아도 boundary/collapse/seed 여부가 남게 하려는 것
- 무엇을 보완하는가: watch_rule_evaluated, watch_result, collapse_target, triggered_seed_name, watch_reason
- 현재 상태: reflection 쪽 observation에서 boundary_only_variation을 기록
- 한계: 실제 second seed는 아직 trigger되지 않음

## 5. 현재 살아 있는 최소 기관

다음은 실제로 살아 있다고 볼 수 있는 최소 기관들이다.

- preflight가 읽기 전에 mode를 먼저 정한다
- breadcrumb가 판단 이동을 남긴다
- raw_to_first_pass_to_report가 mode-scoped observation candidate로 관찰된다
- watch rule이 append 시점에 collapse/boundary/seed 여부를 얇게 평가한다
- candidate summary가 registry를 한 장으로 읽게 한다

이들은 모두 완성형 기관은 아니지만, 이미 작동하고 있다.

## 6. 아직 관찰 단계인 것

아직 아닌 것은 분명하다.

- weak pipeline 아님
- locked pipeline 아님
- second seed 없음
- interpretation packets는 아직 두껍지 않음
- decision lineage는 아직 얇은 바닥 수준
- multi-lens는 본격 확장 전

즉 내부 장치가 생기기는 했지만, 대부분은 아직 관찰/게이트 단계다.

## 7. 이 자료로 무엇을 다시 볼 수 있는가

이 문서는 나중에 다음을 다시 읽게 해준다.

- 왜 처음엔 단순 기능 개선으로는 부족했는가
- 왜 제어면과 breadcrumbs가 먼저 생겼는가
- 왜 observation / boundary / watch rule로 나뉘었는가
- 왜 후보를 억지로 만들지 않았는가
- 어떤 장치가 실제로 살아 있고 어떤 것은 아직 관찰 단계인가

즉 이 문서는 결과 목록이 아니라, 내부 장치가 어떻게 발생했는지 다시 따라갈 수 있는 지도다.

