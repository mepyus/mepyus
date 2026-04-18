# VectorFL First Organ Instruction Skeletons v0

이 문서는 앞서 잠근 `기관별 instruction bundle`을  
실제 첫 기관 4개에 대해 아주 얇은 skeleton 수준으로 내려서 고정한다.

목적은 구현용 프롬프트를 확정하는 것이 아니라,
원본 Paperclip에서 확인한 `instructionsFilePath + promptTemplate + contextSnapshot + summary return`
구조를 참고하면서
VectorFL 기관이 어떤 책임 문법을 가져야 하는지 흔들리지 않게 하는 것이다.

## 1. Core Rule

기관 instruction은 persona 문서가 아니라  
`읽기 책임 + 반환 형식 + 보수 규칙`을 고정하는 문서여야 한다.

즉 각 기관 skeleton은 최소 아래 세 질문에 답해야 한다.

- 무엇을 먼저 읽는가
- 무엇을 반환해야 하는가
- 어떤 경우 보수적으로 멈추는가

## 2. Input Organ Skeleton

### role sentence

입력기관은 source/context/split/fallback를 보존하면서 후속 기관이 바로 받을 수 있는 intake packet을 만든다.

### accepted inputs

- source ref
- source context
- raw material or normalized material
- fallback/weakness signals

### reading priorities

1. source identity
2. context layers
3. split/block viability
4. weakness / fallback preservation

### output contract

- intake packet
- readiness level
- weakness note
- next lane hint

### caution rules

- line을 확정하지 않는다
- weak/mixed/unresolved 입력을 버리지 않는다
- fallback은 실패가 아니라 caution carry다

## 3. Translation Organ Skeleton

### role sentence

라인번역기관은 intake 또는 current-reading 재료를 현재 case/lane에 맞는 operating grammar로 recode한다.

### accepted inputs

- intake packet
- current surface excerpt
- source/context layers
- weakness note

### reading priorities

1. current case question
2. source/context carry
3. grammar shift necessity
4. lane hint formation

### output contract

- translation summary
- lane hint update
- supporting evidence refs

### caution rules

- final meaning을 닫지 않는다
- direct completion wording을 피한다
- unresolved edge는 다음 기관에 남긴다

## 4. Flow Interpretation Organ Skeleton

### role sentence

흐름해석기관은 translated summary와 trace carry를 바탕으로 next hop, unresolved edge, reread direction을 읽는다.

### accepted inputs

- translation summary
- lane hints
- governance carry
- trace/reentry carry

### reading priorities

1. current lane and next-hop candidates
2. unresolved edge
3. reread direction
4. direct readout vs explanation-first tension

### output contract

- flow reading summary
- next hop candidates
- reentry hint
- caution note

### caution rules

- route choice를 completion으로 과장하지 않는다
- governance restriction을 무시하지 않는다
- next hop은 candidate로 남길 수 있다

## 5. Governance Organ Skeleton

### role sentence

감독기관은 current-reading과 flow 결과를 받아 hold/restriction/release condition을 명시하고, direct action 또는 premature closure를 막는다.

### accepted inputs

- flow reading summary
- next hop candidates
- trace carry
- current surface

### reading priorities

1. hold necessity
2. restriction flags
3. release condition
4. next check trigger

### output contract

- governance caution
- restriction set
- release condition
- current-reading-ready fragment

### caution rules

- approve/release를 쉽게 열지 않는다
- observer-only / promotion forbidden carry를 숨기지 않는다
- trace와 reentry 단서를 current-reading에서 끊지 않는다

## 6. Shared Return Shape

첫 기관 skeleton은 모두 아래 공통 반환 감각을 가진다.

- 짧은 summary
- evidence/support refs
- caution if any
- trace/residue if any
- next handoff readiness

즉 raw output보다 `다음 기관이 읽기 좋은 반환`을 우선한다.

## 7. What This Keeps From Original Reference

Paperclip native 구조에서 유지하는 감각은 아래다.

- 정적 instruction file이 실제 run에 주입됨
- run마다 contextSnapshot이 별도 붙음
- 결과는 다시 읽기 좋은 summary surface로 환원됨

하지만 그대로 들이지 않는 것은 아래다.

- issue/heartbeat wording
- company/agent hierarchy wording
- approval/budget naming

## 8. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL의 첫 기관 instruction skeleton은 input, translation, flow interpretation, governance 네 기관에 대해 읽기 책임, accepted inputs, output contract, caution rules를 최소 문법으로 고정하고, Paperclip의 instruction/context/summary 구조는 참조하되 ontology와 naming은 VectorFL 쪽으로 다시 소유한다.`
