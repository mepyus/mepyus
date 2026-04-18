# Paperclip Agent Configuration And Instruction Surface Reading v0

이 문서는 Paperclip UI에서 `agent detail`이 어떻게 구성되어 있는지 읽고,  
기관별 설정 / instruction / run return surface가 어떤 식으로 한 자리에 모이는지 native하게 정리한다.

목적은 VectorFL Paper에서 기관별 md 편집과 기관 흐름 표시를 설계하기 전에,  
원본이 `기관 상세면`을 어떻게 다루는지 먼저 파악하는 것이다.

## 1. Verdict

Paperclip의 agent detail은 단순 프로필 페이지가 아니다.  
실제로는 아래 네 면이 한 자리에 모인다.

- configuration surface
- instructions / prompt surface
- skills surface
- runs / activity surface

즉 Paperclip는 agent를 단순 조직도 노드가 아니라,  
`설정 가능하고, 지시를 받고, 실행 흔적을 남기는 runtime node`로 다룬다.

## 2. Core Evidence

- [AgentDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/AgentDetail.tsx)
- [AgentConfigForm.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/AgentConfigForm.tsx)
- [agent-config-primitives.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/agent-config-primitives.tsx)
- [PathInstructionsModal.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/PathInstructionsModal.tsx)
- [codex-local/config-fields.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/adapters/codex-local/config-fields.tsx)

## 3. What The Surface Actually Shows

### 3-1. configuration surface

- adapter type
- runtime config
- environment/config values
- run policy / heartbeat-related settings

즉 agent는 실제 실행 설정을 가진다.

### 3-2. instruction surface

- `instructionsFilePath`
- `promptTemplate`
- markdown editor / path picker

즉 agent 지시는 별도 파일 또는 prompt surface로 편집 가능하게 드러난다.

### 3-3. skills surface

- desired skills
- synced skills
- runtime-injected skill state

즉 agent detail은 능력/도구 층도 같이 가진다.

### 3-4. runs surface

- run status
- run cost/tokens
- transcript / live run / recent runs

즉 agent detail은 실행 반환과 흔적도 같이 읽게 한다.

## 4. Structural Reading

Paperclip agent detail을 구조적으로 읽으면 아래와 같다.

### static setup layer

- adapter type
- adapter config
- runtime config

### instruction layer

- md file path
- prompt template

### capability layer

- skills / injected tools

### runtime evidence layer

- recent runs
- transcripts
- runtime state

즉 원본은 이미 `기관 상세면 = 설정 + 지시 + 능력 + 실행 흔적` 구조를 가진다.

## 5. What VectorFL Should Notice Later

이 문서에서 나중에 참고할 가치가 큰 것은 아래다.

- 기관마다 별도 instruction 편집면이 필요할 수 있다
- 기관 설정과 instruction은 current-reading 면과 분리된 상세면으로 둘 수 있다
- 기관 실행 흔적은 설정 상세 안에서도 다시 읽을 수 있어야 한다
- 즉 `기관 상세면`은 존재 가치가 있다

## 6. What Must Not Be Imported Directly

아래는 그대로 들이면 안 된다.

- agent/persona naming
- adapter-specific wording을 canonical organ wording으로 쓰는 것
- skills surface를 바로 VectorFL ontology로 올리는 것
- cost/run metrics를 중심면으로 올리는 것

즉 구조 감각은 유효하지만, 의미체계는 다시 써야 한다.

## 7. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`Paperclip의 agent detail은 configuration, instructions, skills, runs를 한 자리에 모은 runtime node 상세면으로 읽는 것이 맞고, VectorFL Paper도 나중에 기관별 md 편집과 실행 흔적을 다루려면 이 구조 감각은 참조하되 agent ontology와 adapter wording은 다시 재의미화해야 한다.`
