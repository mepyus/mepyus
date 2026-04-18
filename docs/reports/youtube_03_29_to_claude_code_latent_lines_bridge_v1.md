# youtube_03_29 to claude_code latent lines bridge v1

## 1. 이 문서의 목적

이 문서는 `youtube_03_29.md`를 먼저 읽고, 그 읽기 기준으로 `claude_code.txt`를 다시 보는 역방향 bridge note다.

목적은 두 입력이 같은 잠복 선을 어떻게 공유하는지, 그리고 어느 쪽이 더 개념적이고 어느 쪽이 더 운영형인지 보는 것이다.

## 2. 먼저 youtube_03_29.md를 읽으면 보이는 것

`youtube_03_29.md`는 `claude_code`를 직접 다루기 전에 이미 다음 세 선을 먼저 드러낸다.

### 2.1 alignment_before_autonomy가 가장 강하다

- `plan mode`를 먼저 세운다.
- `검증 가능해야 자동화된다`는 프레임을 반복한다.
- `semi-formal language`와 `controllability`를 autonomy보다 앞에 둔다.

즉 이 입력은 자동화보다 먼저 정렬과 제어 가능성을 세워야 한다는 쪽으로 읽힌다.

### 2.2 harness_over_model이 그 다음으로 강하다

- `program.md가 manifest`
- `Claude를 대학원생처럼 지도한다`
- `AI 과학 블로그`, `vibe physics`, `GAN에서 영감받은 Anthropic의 멀티 에이전트 하네스 설계 가이드`

이 입력은 모델 능력보다 그것을 감싸는 manifest/harness/loop/evaluator를 더 본다.

### 2.3 work_absorption_harness는 보이지만 상대적으로 약하다

- 작업을 시스템으로 흡수하는 감각은 있지만,
- `claude_code.txt`처럼 command / skill / trigger가 전면에 오지는 않는다.

즉 `youtube_03_29.md`는 정렬과 하네스의 개념을 먼저 세우는 입력이다.

## 3. 같은 잠복 선을 claude_code.txt로 다시 읽으면

`claude_code.txt`는 같은 선을 더 직접적이고 운영형으로 보여준다.

### 3.1 harness_over_model

- `main.tsx`, `query.ts`, `tool pipeline`, `permissions`, `feature gates`, `mode filtering`이 모델 설명보다 먼저 서술된다.
- `CLAUDE.md`를 root-level / folder-level로 나눠 하네스를 분리한다.
- 즉 `youtube_03_29.md`가 concept-level harness를 보여준다면, `claude_code.txt`는 실제 시스템 구조로 하네스를 보여준다.

### 3.2 work_absorption_harness

- custom command, trigger keyword, skill, plugin, team sharing이 명확하다.
- 반복 작업이 command/skill/trigger로 시스템에 흡수된다.
- `CLAUDE.md`가 단순 지침이 아니라 반복 작업을 흡수하는 운영 장치가 된다.
- 즉 `youtube_03_29.md`의 추상적 "harness"가 `claude_code.txt`에서는 실제 command/skill 구조로 내려온다.

### 3.3 alignment_before_autonomy

- plan mode와 accept mode가 분리된다.
- write 권한을 늦게 열고, 먼저 계획을 검토한다.
- 무거운 작업은 plan-first로 시작한다.
- 즉 `youtube_03_29.md`가 말한 정렬 우선이 `claude_code.txt`에서는 실제 실행 모드로 구현된다.

## 4. 두 입력을 함께 읽을 때 보이는 차이

### 4.1 youtube_03_29.md

- 더 개념적이다.
- AI 시대, manifest, 오토리서치, semi-formal language, human-AI hybrid 같은 상위 언어가 많다.
- 선의 방향을 잡는 문서에 가깝다.

### 4.2 claude_code.txt

- 더 운영형이다.
- startup, query loop, tool pipeline, CLAUDE.md, skills, commands, modes 같은 실제 하네스 구성요소가 많다.
- 선을 시스템으로 내린 문서에 가깝다.

## 5. 우리 공간의 기존 잠복 선과 연결하면

### 5.1 harness_over_model -> pre_read_eye / transition_over_surface

- `youtube_03_29.md`는 이 선을 개념적으로 보여준다.
- `claude_code.txt`는 실제 운영 구조로 보여준다.
- 둘 다 모델보다 바깥 레이어가 본체라는 점에서 우리 공간의 preflight / transition-first reading과 맞는다.

### 5.2 work_absorption_harness -> input_to_reading_organ

- `youtube_03_29.md`는 작업 흡수의 철학을 보여준다.
- `claude_code.txt`는 command / skill / trigger / plugin으로 그 철학을 실제 장치로 만든다.
- 우리 공간에서는 입력 / 기록 / 관찰이 읽기 기관 재료가 되는 흐름과 같다.

### 5.3 alignment_before_autonomy -> pre_read_eye

- `youtube_03_29.md`는 plan-first / verify-first를 말한다.
- `claude_code.txt`는 shift-tab plan mode, accept mode, mode filtering으로 이를 구현한다.
- 우리 공간의 selected_mode / current_phase / drift_guard와 같은 축이다.

## 6. 이 역방향 읽기에서 특히 중요한 문장들

- `youtube_03_29.md`:
  - `모든 것은 검증 가능해야 자동화된다`
  - `Claude를 대학원생처럼 지도한다`
  - `program.md가 manifest`

- `claude_code.txt`:
  - `Collect Git status + CLAUDE.md`
  - `tool pipeline`
  - `skill commands`
  - `mode filtering`

이 둘을 함께 보면, 개념적 정렬이 실제 운영 레이어로 내려오는 구조가 보인다.

## 7. 현재 가장 강한 선

- 가장 강한 선:
  - `alignment_before_autonomy`

이유:
- `youtube_03_29.md`는 정렬 우선의 원칙을 먼저 세우고,
- `claude_code.txt`는 그것을 plan mode / accept mode / mode filtering으로 구현한다.

## 8. 그다음으로 강한 선

- `harness_over_model`

이유:
- `youtube_03_29.md`가 manifest/harness를 개념으로 드러내고,
- `claude_code.txt`가 그걸 실제 startup / permissions / tool pipeline으로 구현한다.

## 9. 아직 상대적으로 약한 선

- `work_absorption_harness`

이유:
- 두 입력 모두 작업 흡수를 보여주지만,
- `claude_code.txt`에서 더 강하고 `youtube_03_29.md`에서는 개념 쪽이 앞선다.
- 즉 선은 분명하지만, 다른 두 선보다 덜 전면적이다.

## 10. 앞으로 새 observation에서 무엇을 보면 이 선이 짙어진다고 볼 수 있는가

- `youtube_03_29.md` 계열에서:
  - plan / verify / semi-formal / controllability가 더 강화되면 `alignment_before_autonomy`가 짙어진다.

- `claude_code.txt` 계열에서:
  - command / skill / trigger / CLAUDE.md / mode filtering이 반복되면 `work_absorption_harness`가 짙어진다.

## 11. 한 줄 결론

> `youtube_03_29.md`는 하네스·정렬·흡수의 원칙을 먼저 보여주고, `claude_code.txt`는 그 원칙을 startup / tool pipeline / command / skill / mode filtering으로 운영화한다. 따라서 두 입력은 같은 잠복 선을 공유하되, 전자는 개념적, 후자는 운영적이다.

