# VectorFL Organ Delegation And Handoff Translation v0

이 문서는 Paperclip의 내부 업무 배정/지시/handoff 구조를  
`VectorFL Paper`의 기관 흐름 언어로 처음 번역하는 초안이다.

목적은 Paperclip ontology를 가져오는 것이 아니라,
앞서 읽은 native 구조를 바탕으로  
`VectorFL 기관에 일이 어떻게 놓이고, 어떤 문맥과 지시가 붙고, 어떻게 다음 기관으로 넘어가며, 어떤 요약/trace가 남는가`
를 우리 언어로 명시하는 것이다.

이 문서는 아직 구현 명세가 아니라  
`운용 번역 기준`을 잠그는 문서다.

## 1. Core Sentence

VectorFL Paper의 기관 흐름은
`case-aware work placement`
-> `organ-specific instruction attachment`
-> `bounded organ run`
-> `summary / trace / governance return`
-> `next-organ handoff`
로 읽는 것이 가장 정확하다.

즉 Paperclip의 `issue -> wakeup -> heartbeat -> comment -> session`
구조를 그대로 쓰지 않고,
VectorFL에서는
`case/lane/organ/current-reading/governance/trace`
언어로 다시 소유한다.

## 2. What Counts As A Work Placement In VectorFL

Paperclip의 assignment에 대응하는 VectorFL 구조는  
`current organ responsibility placement`다.

의미:

- 어떤 case가 현재 어떤 기관/lane에 놓였는가
- 이 기관은 읽기 전담인지, 후보 생성인지, 해석인지, 감독인지
- 이 배정이 제안인지, 실제 현재 책임인지

현재 기준에서 이 placement는 최소 아래를 가져야 한다.

- `case_ref`
- `current_organ_ref`
- `current_lane_ref`
- `placement_reason`
- `restriction_flags`
- `next_hop_candidates`

즉 VectorFL에서는 `issue assignee` 대신  
`현재 어느 기관이 이 case를 받고 있는가`가 핵심이 된다.

## 3. Organ-Specific Instruction Attachment

Paperclip의 `instructionsFilePath + promptTemplate` 구조는  
VectorFL에서 `기관별 instruction bundle`로 다시 읽는 것이 맞다.

의미:

- 기관마다 별도 md / instruction 파일이 있을 수 있다
- 그 기관이 어떤 기준으로 읽고 무엇을 반환해야 하는지 붙는다
- instruction은 정적 지시층이다

현재 단계의 번역 규칙:

- `input organ`
  - source/context/split/fallback/intake packet 중심 지시
- `line/state organ`
  - line seed, thickening, reuse, carry 중심 지시
- `translation organ`
  - grammar shift, operating grammar, summary recoding 중심 지시
- `flow interpretation organ`
  - next hop, unresolved edge, reread direction 중심 지시
- `governance organ`
  - hold, caution, observer-only, promotion forbidden 중심 지시
- `trace/memory organ`
  - summary, residue, reentry, append-only carry 중심 지시

즉 기관별 md는 persona decoration이 아니라  
`기관의 읽기 책임과 반환 형식`을 고정하는 장치여야 한다.

## 4. Dynamic Handoff Context

Paperclip의 `wakeup payload + contextSnapshot`은  
VectorFL에서 `handoff packet + current-reading context`로 번역하는 것이 맞다.

의미:

- 정적 instruction만으로는 기관 run이 충분하지 않다
- 매번 현재 case/lane/governance/trace 상황이 같이 붙어야 한다

현재 단계의 최소 handoff context는 아래처럼 읽는다.

- `case summary`
- `current-reading surface excerpt`
- `governance state`
- `relevant intake or source refs`
- `trace/residue carry`
- `question or trigger`
- `expected return type`

즉 기관 전달은 자유 대화형이 아니라,
`shared environment + bounded packet` 구조를 먼저 가져야 한다.

## 5. Bounded Organ Run

Paperclip의 heartbeat run은  
VectorFL에서 `bounded organ run`으로 읽는 것이 맞다.

의미:

- 기관은 무한 자율 상태로 떠다니지 않는다
- 지금 받은 packet과 context 안에서 한 번의 bounded work를 수행한다
- 그 run은 시작 이유와 제한 상태를 같이 가진다

현재 단계에서 bounded organ run에 붙어야 하는 것은 아래다.

- `trigger`
- `current_organ_ref`
- `input_refs`
- `context_snapshot`
- `run_state`
- `result_summary`
- `trace_outputs`
- `handoff_ready`

즉 기관은 “계속 생각하는 존재”보다  
`한 번의 책임 구간을 수행하는 bounded worker`로 읽는 편이 정확하다.

## 6. Return Structure

Paperclip의 `result summary / issue comment / activity`는  
VectorFL에서 `summary return + trace return + governance return`으로 번역하는 것이 맞다.

### 6-1. summary return

- 현재 기관이 무엇을 읽었는지
- 다음 기관이 짧게 이어받을 수 있는 요약

### 6-2. trace return

- residue note
- reentry hint
- unresolved edge
- supporting evidence ref

### 6-3. governance return

- hold candidate
- caution
- release condition
- not-ready reason

즉 기관 결과는 raw output보다  
`다음 기관과 current-reading이 읽기 좋은 반환면`이어야 한다.

## 7. Session Continuity Translation

Paperclip의 `taskKey + session carry`는  
VectorFL에서 `organ continuity` 또는 `case-lane continuity`로 번역하는 것이 맞다.

의미:

- 같은 case/lane/organ 조합은 이전 흔적을 다시 이어받을 수 있다
- 매번 완전히 새 기관처럼 시작하면 안 된다

현재 단계에서 continuity를 읽을 기준은 아래다.

- `case_ref`
- `organ_ref`
- `lane_ref`
- `previous_trace_refs`
- `carry_summary`
- `reentry_condition`

즉 VectorFL 기관 흐름도  
`무조건 fresh-start`보다 `bounded continuity`를 가져야 한다.

## 8. First Organ Translation Candidates

현재 구조에서 먼저 번역하기 좋은 기관 흐름은 아래 셋이다.

### 8-1. input -> translation

- intake packet이 translation organ으로 넘어감
- source/context/weakness가 같이 carry됨

### 8-2. translation -> flow interpretation

- grammar shift summary와 lane hint가 흐름 판독으로 넘어감
- unresolved edge가 다음 hop 판단에 개입함

### 8-3. flow interpretation -> governance / current-reading

- next hop candidate
- caution
- direct readout 보류
- trace/reentry
가 governance/current-reading으로 같이 반환됨

즉 초기에 모든 기관을 다 열기보다,
먼저 `입력 -> 번역 -> 흐름 -> 감독/current-reading`
축을 강하게 읽는 것이 맞다.

## 9. What Must Stay Visible In The Shell

Paperclip 구조를 참고해 VectorFL Paper에서도 아래는 보여야 한다.

- 현재 어느 기관이 이 case를 받고 있는가
- 이 기관은 제안만 하는가, 현재 책임을 가진가
- 다음 기관 후보가 무엇인가
- 왜 아직 거기 못 넘어가는가
- 어떤 trace/residue가 다음 handoff에 붙는가

즉 shell은 단순 결과판이 아니라  
`기관 흐름과 전달 구조가 보이는 operating surface`여야 한다.

## 10. What Is Not Locked Yet

아직 아래는 잠그지 않는다.

- exact organ instruction file layout
- organ execution runtime
- multi-agent concurrency policy
- automatic reassignment rules
- organ-level scheduling UI

즉 지금은 `구조 번역 기준`만 잠근다.

## 11. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Paper는 Paperclip의 assignment, instructions, run, summary, session 구조를 직접 모사하지 않고, case-aware work placement, organ-specific instruction bundle, bounded organ run, summary/trace/governance return, case-lane-organ continuity 구조로 번역해 현재 기관 책임과 다음 기관 handoff가 보이는 운영 제품으로 간다.`
