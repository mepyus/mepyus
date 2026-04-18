# youtube_03_29 and claude_code common latent lines comparison v1

## 1. 이 문서의 목적

이 문서는 `youtube_03_29.md`와 `claude_code.txt`를 각각 따로 요약하기 위한 문서가 아니다.

목적은 두 자료를 하나의 비교면으로 묶어서,
같은 잠복 선이 원칙층(youtube_03_29)과 구현층(claude_code)에서 어떻게 다르게 나타나는지를 한 장으로 읽게 하는 것이다.

## 2. 왜 이 둘을 함께 읽어야 하는가

- `youtube_03_29.md`는 원칙면이다.
  - 무엇을 먼저 세워야 하는지, 어떤 정렬과 제어가 필요한지 말한다.
- `claude_code.txt`는 구현면이다.
  - 그 원칙이 실제 startup / pipeline / command / mode / skill / trigger / plugin으로 어떻게 내려가는지 보여준다.

즉 둘은 같은 선의 서로 다른 층이다.

## 3. 공통 잠복 선 3개 비교

### 3.1 alignment_before_autonomy

- youtube_03_29:
  - plan mode, evaluation, semi-formal language, controllability를 반복적으로 강조한다.
  - 완전 자동화보다 먼저 정렬과 제어 가능성을 세우는 원칙이 강하다.
- claude_code:
  - shift-tab으로 plan mode / accept mode를 나누고, write보다 먼저 plan을 둔다.
  - 무거운 작업을 바로 실행하지 않고 gate / mode / permission을 먼저 세운다.
- 차이:
  - youtube_03_29는 "왜 그렇게 해야 하는가"를 말한다.
  - claude_code는 "그것을 어떤 모드와 권한으로 구현하는가"를 말한다.
- 우리 공간 연결:
  - `pre_read_eye`

### 3.2 harness_over_model

- youtube_03_29:
  - `program.md가 manifest`
  - `Claude를 대학원생처럼 지도한다`
  - `AI 과학 블로그`, `vibe physics`, `harness` / `evaluator` / `multi-agent`가 전면에 온다.
  - 모델보다 그것을 감싸는 하네스가 더 중요하다는 원칙이 강하다.
- claude_code:
  - startup에서 auth, settings, feature gates, Git status, CLAUDE.md를 먼저 모은다.
  - tool pipeline, permission classifier, mode filtering이 모델 출력보다 앞선다.
- 차이:
  - youtube_03_29는 하네스의 철학을 말한다.
  - claude_code는 하네스의 실제 운영 구조를 보여준다.
- 우리 공간 연결:
  - `pre_read_eye`
  - `transition_over_surface`

### 3.3 work_absorption_harness

- youtube_03_29:
  - program / manifest / agent / evaluator / research loop로 작업을 흡수하는 방향을 말한다.
  - 연구와 논문, agent-as-student, 반복 최적화가 핵심이다.
- claude_code:
  - custom command, trigger keyword, skill, plugin, shared config가 반복 작업을 command화한다.
  - `CLAUDE.md`를 반복 workflow의 흡수 장치로 만든다.
- 차이:
  - youtube_03_29는 작업 흡수의 방향성과 가치 판단을 말한다.
  - claude_code는 작업 흡수를 실제 command/skill/trigger 체계로 구현한다.
- 우리 공간 연결:
  - `input_to_reading_organ`

## 4. 공통점

- 둘 다 모델 자체보다 외곽 구조를 더 본다.
- 둘 다 자동화보다 정렬과 검증을 먼저 둔다.
- 둘 다 반복 작업을 시스템 내부 장치로 흡수하는 감각이 있다.
- 둘 다 인간의 역할을 수행자에서 설계자/감독자 쪽으로 이동시킨다.

## 5. 차이점

- `youtube_03_29.md`
  - 원칙층이다.
  - manifest, semi-formal, controllability, evaluation을 중심으로 방향을 세운다.
  - 왜 그런 구조가 필요한지 말한다.

- `claude_code.txt`
  - 구현층이다.
  - startup, CLAUDE.md, mode filtering, command, skill, trigger, plugin으로 실제 하네스를 보여준다.
  - 그 원칙이 어떻게 시스템에 내려오는지 말한다.

## 6. 우리 공간 연결점

- `alignment_before_autonomy -> pre_read_eye`
- `harness_over_model -> pre_read_eye / transition_over_surface`
- `work_absorption_harness -> input_to_reading_organ`

우리 공간에서 이 비교가 중요한 이유는,
원칙층과 구현층을 따로 보지 않고 같은 선의 응축 단계로 읽을 수 있게 해주기 때문이다.

## 7. 이번 비교로 새롭게 선명해진 것

- `youtube_03_29.md`는 "정렬과 검증이 먼저"라는 원칙을 준다.
- `claude_code.txt`는 그 원칙을 실제 mode / harness / command / skill 구조로 내려준다.
- 따라서 둘은 비슷한 참고자료가 아니라,
  **원칙면 ↔ 구현면** 관계로 읽는 것이 맞다.

## 8. 한 줄 결론

> `youtube_03_29.md`는 하네스와 정렬의 원칙을 먼저 세우는 문서이고, `claude_code.txt`는 그 원칙을 startup / mode / CLAUDE.md / command / skill / trigger로 구현한 문서다. 둘은 같은 잠복 선을 공유하지만, 전자는 원칙층, 후자는 구현층이다.

