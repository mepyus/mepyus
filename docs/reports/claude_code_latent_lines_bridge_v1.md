# claude_code latent lines bridge v1

## 1. 이 문서의 목적

이 문서는 `claude_code` 계열을 요약하기 위한 문서가 아니다.

목적은 `claude_code` 안에서 우리 공간으로 직접 이어질 수 있는 잠복 선 3개를 분리해 두고, 앞으로 새 observation이 들어올 때 어디가 더 짙어지는지 관찰할 수 있게 하는 것이다.

즉 이 문서는 모델 소개가 아니라 하네스/정렬/흡수 구조를 읽는 bridge note다.

## 2. claude_code를 어떻게 읽어야 하는가

이 계열은 "좋은 모델"을 설명하는 자료로만 읽으면 핵심이 빠진다.

더 맞는 읽기는 다음 세 가지다.

1. 모델보다 하네스/구조/운영 레이어가 본체라는 읽기
2. 결과물보다 내 일을 흡수해서 재사용 가능한 장치로 만드는 읽기
3. 완전 자동화보다 먼저 정렬과 제어 가능성을 세우는 읽기

`claude_code.txt`는 startup, query loop, tool pipeline, permissions, CLAUDE.md, skills, plugins, modes를 함께 묶어 읽게 하고,
`claude_code_index.txt`는 CLAUDE.md, trigger keyword, plan mode, skill template, team sharing을 통해 같은 방향을 더 노골적으로 보여준다.

## 3. 잠복 선 3개 정의

### 3.1 harness_over_model

- 정의:
  - 모델 자체보다 모델을 감싸는 결정론적 하네스 / 구조 / 운영 레이어가 더 중요하다는 선
- 왜 중요한가:
  - 우리 공간도 "좋은 모델"보다 "좋은 읽기 구조 / 제어 구조"를 먼저 세우려 한다.
  - 그래서 control plane, preflight gate, candidate watch 쪽과 직접 연결된다.
- claude_code evidence:
  - startup에서 model 선택보다 먼저 auth, settings, feature gates, Git status, CLAUDE.md를 모은다.
  - tool pipeline, permission classifier, mode filtering이 모델 출력보다 먼저 결과를 모양낸다.
  - `claude_code_index.txt`는 root-level CLAUDE.md와 폴더별 CLAUDE.md로 하네스를 분리한다.

### 3.2 work_absorption_harness

- 정의:
  - 결과물을 바로 뽑기보다, 내 일을 빨아들이고 반복 생성하게 하는 장치를 먼저 만든다는 선
- 왜 중요한가:
  - 우리 공간이 라인보다 라인 생성 구조를 먼저 보려는 방향과 강하게 맞닿아 있다.
  - `input_to_reading_organ`과 바로 이어진다.
- claude_code evidence:
  - custom command / trigger keyword / skill / plugin이 반복 작업을 시스템 안으로 흡수한다.
  - `claude_code_index.txt`는 `CLAUDE.md`에 트리거 키워드를 등록해 반복 workflow를 묶는 방식을 강조한다.
  - skills를 재사용 가능한 작업 템플릿으로 설명하고, 팀 공유가 가능한 구조로 만든다.

### 3.3 alignment_before_autonomy

- 정의:
  - 완전 자동 처리보다 먼저 사람-도구 사이의 정렬과 제어 가능성을 세운다는 선
- 왜 중요한가:
  - 우리 공간의 `pre_read_eye`, `drift_guard`, mode-first reading과 직접 연결된다.
  - 읽기 전에 먼저 align을 잡는 감각이다.
- claude_code evidence:
  - shift-tab으로 plan mode와 accept mode를 나누고, 쓰기 전에 먼저 계획을 보게 한다.
  - 무거운 작업은 즉시 실행보다 plan-first로 비용과 오류를 줄인다.
  - command / skill / trigger는 “알아서 다 한다”보다 “어디까지 할지 먼저 정렬한다”는 쪽에 가깝다.

## 4. 우리 공간의 기존 잠복 선과의 연결

### 4.1 harness_over_model -> pre_read_eye / transition_over_surface

- 연결 이유:
  - 읽기 전에 무엇을 볼지 정하는 제어가 핵심이기 때문이다.
  - 모델보다 외곽 하네스가 결과를 규정하는 구조는, 우리 공간에서 전이/역할/허브를 먼저 읽는 태도와 닿는다.
- 우리 공간 쪽 evidence:
  - runtime preflight gate
  - control plane
  - breadcrumbs가 read 전에 first entry를 남기는 구조

### 4.2 work_absorption_harness -> input_to_reading_organ

- 연결 이유:
  - `claude_code`는 반복 업무를 command / skill / trigger / shared config로 흡수한다.
  - 우리 공간도 입력/기록/관찰이 단순 저장이 아니라 판단 기관의 재료가 되게 만들려 한다.
- 우리 공간 쪽 evidence:
  - observation registry
  - candidate scope summary
  - second candidate watch rule
  - watch rule auto connection

### 4.3 alignment_before_autonomy -> pre_read_eye

- 연결 이유:
  - 읽기 전에 먼저 정렬과 제어를 세우는 방식이기 때문이다.
  - 자동화보다 모드/국면/드리프트 경계를 먼저 두는 감각은 우리 공간의 preflight와 같다.
- 우리 공간 쪽 evidence:
  - `selected_mode`
  - `current_phase`
  - `drift_guard`
  - append 전에 평가되는 watch result

## 5. 각 선의 관찰 체크포인트

### 5.1 harness_over_model

- 모델 설명보다 outer deterministic layer가 강조되는가
- 같은 모델이라도 하네스가 바뀌면 결과가 달라진다고 읽히는가
- 제품/기관의 본체가 모델이 아니라 감싸는 구조로 표현되는가

### 5.2 work_absorption_harness

- 결과물보다 setup / command / skill / trigger / memory document가 먼저 강조되는가
- 내 일이 시스템 내부의 재사용 가능한 장치로 흡수되는가
- 단발 작업보다 반복 가능한 작업 구조를 만드는 감각이 드러나는가

### 5.3 alignment_before_autonomy

- 자동 처리보다 먼저 정렬/질문/선택지가 세워지는가
- controllability가 full autonomy보다 앞서는가
- plan-first / gate-first / ask-first 패턴이 반복되는가

## 6. 현재 evidence와 아직 부족한 evidence

### 6.1 harness_over_model

- 현재 evidence:
  - `claude_code.txt`는 model 선택보다 startup harness, tool pipeline, permissions, CLAUDE.md 수집을 먼저 놓는다.
  - `claude_code_index.txt`는 root/pfolder CLAUDE.md, skill, plugin, command 구조를 하네스로 다룬다.
- 아직 부족한 evidence:
  - 이 구조가 다른 `claude_code` 관련 새 자료에서도 자동 반복되는지 더 볼 필요가 있다.

### 6.2 work_absorption_harness

- 현재 evidence:
  - trigger keyword, custom command, skill template, team sharing이 반복된다.
  - 작업을 시스템 내부 장치로 흡수하는 감각이 강하다.
- 아직 부족한 evidence:
  - 이 선이 실제 내부 기관으로 승격될 만큼 다양한 가족 자료에서 반복되는지는 아직 얇다.

### 6.3 alignment_before_autonomy

- 현재 evidence:
  - plan mode가 먼저 세워지고 accept/edit가 뒤따른다.
  - 무거운 작업 전에 먼저 설계/정렬을 한다.
- 아직 부족한 evidence:
  - 자동화 자체를 부정하는 것이 아니라 controllability 우선임을 더 다양한 표면에서 확인할 필요가 있다.

## 7. 앞으로 새 observation에서 무엇을 보면 이 선이 짙어진다고 볼 수 있는가

- harness_over_model
  - 하네스/컨텍스트/권한/운영 레이어가 모델보다 먼저 서술되면 짙어진다.

- work_absorption_harness
  - command / skill / trigger / shared config가 반복 작업을 흡수하는 구조로 보이면 짙어진다.

- alignment_before_autonomy
  - plan-first, ask-first, gate-first, mode-first가 자동화보다 우선하면 짙어진다.

## 8. 이 bridge 문서가 필요한 이유

- `claude_code`를 모델 소개로 축소하지 않고, 우리 공간으로 이어질 구조 선으로 읽기 위해서다.
- 앞으로 새 observation이 들어올 때, 그게 단순 기능 설명인지 아니면 하네스 / 흡수 / 정렬 선을 강화하는지 판정하기 위해서다.
- 기존 잠복 선(`pre_read_eye`, `transition_over_surface`, `input_to_reading_organ`)과 직접 접붙인 상태로 남겨 두기 위해서다.

## 9. 한 줄 결론

> `claude_code`는 좋은 모델의 소개가 아니라, 하네스가 본체가 되고, 작업이 시스템에 흡수되며, 자동화보다 정렬과 제어가 먼저 서는 구조를 보여주는 자료이고, 이 성질은 우리 공간의 `pre_read_eye`, `transition_over_surface`, `input_to_reading_organ`과 직접 연결된다.

