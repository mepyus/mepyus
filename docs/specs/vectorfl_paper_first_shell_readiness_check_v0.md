# VectorFL Paper First Shell Readiness Check v0

이 문서는 `git_search/paperclip` 껍데기를 활용한 첫 VectorFL Paper shell 프로토타입 전에  
무엇이 준비되었고 무엇이 아직 비어 있는지 점검하는 readiness check다.  
구현 문서가 아니라, 바로 다음 단계로 내려갈 수 있는지 확인하는 점검표다.

## 1. Goal

첫 shell 프로토타입의 목표는 아래로 잡는다.

- Paperclip ontology를 들이지 않는다
- VectorFL core canonical object를 shell에 view model로 올린다
- 첫 중심면은 `Current Reading`
- `Inputs / Intake`, `Cases / Queue`는 주변 진입면으로 둔다

## 2. Ready Items

### structure readiness

- 3층 구조 잠금 완료
- handoff boundary 잠금 완료
- 외부 source / host 필요성 잠금 완료

### object readiness

- canonical object ownership 잠금 완료
- minimum field schema 잠금 완료

### shell readiness

- current-reading adapter contract 잠금 완료
- inputs / intake adapter contract 잠금 완료
- cases / queue adapter contract 잠금 완료
- Paperclip shell extraction boundary 잠금 완료
- canonical object -> shell mapping 잠금 완료

## 3. Still Missing Before Confident Build

### adapter gaps

- `Programs / Connections adapter contract`
- `History / Trace panel adapter contract`

### implementation gaps

- mock JSON or fixture set for canonical objects
- shell-only prototype scope boundary
- current-reading first screen composition sketch

### decision gaps

- 첫 프로토타입에서 linked program panel을 포함할지 여부
- trace/history를 current-reading strip까지만 둘지 별도 panel까지 열지 여부

## 4. Safe First Build Scope

현재 기준으로 가장 안전한 첫 구현 범위는 아래다.

### include

- `Current Reading shell`
- 최소 `Inputs / Intake shell`
- 최소 `Cases / Queue shell`

### exclude for now

- live program action
- bidirectional control
- company/issue naming
- full orchestration layer
- agent runtime management UI

## 5. Recommended Build Order

1. `Current Reading mock shell`
2. `Inputs / Intake detail shell`
3. `Cases / Queue shell`
4. `History / Trace panel`
5. `Programs / Connections panel`

## 6. Readiness Verdict

현재 상태는 `structure-ready, adapter-mostly-ready, implementation-not-started`로 읽는 것이 가장 정확하다.

즉:

- 구조 기준은 충분히 잠겼다
- 첫 shell 프로토타입을 시작할 수 있다
- 다만 live integration이나 full shell까지 곧바로 가기보다
  `Current Reading 중심 mock/view-model shell`부터 여는 것이 맞다

## 7. Final Note

현재 준비도는 첫 구현을 막는 상태는 아니다.  
다음 단계는 새로운 구조 논의보다, `Current Reading first shell`을 mock/view-model 기준으로 작게 시작하는 쪽이 가장 자연스럽다.
