# gemini_task_dispatch_policy_v1.md

## 1. purpose

이 문서는 Gemini CLI에 업무를 넘길 때
무엇을 안전하게 넘길 수 있고,
무엇은 절대로 넘기면 안 되며,
어떤 형식으로 제한을 걸어야 급발진을 막을 수 있는지 고정한다.

핵심은 단순 역할 분리가 아니다.

**Gemini CLI는 업무 종류별 허용 범위와 출력 형식이 잠겨 있어야만 안전하다.**

---

## 2. top rule

Gemini CLI는 기본적으로 아래 세 부류 중
`A`와 일부 `B`만 맡는다.

### A. safe read-only support

안전하게 맡길 수 있는 후단 읽기/요약/비교/점검 업무

### B. bounded review support

엄격한 입력/출력 제한이 있어야만 맡길 수 있는 보조 검토 업무

### C. forbidden core-touch work

절대로 맡기면 안 되는 업무

---

## 3. safe task classes

## 3-1. summary / briefing

Gemini에 맡겨도 좋은 일:

- receipt 요약
- operation board 요약
- process console 상태 브리핑
- latest/history/diff 읽기 쉬운 요약문 생성
- cohort 보고서 초안 요약

출력 조건:

- facts only
- 최대 5~10줄 요약
- 새로운 판단 추가 금지

---

## 3-2. read-only diff review

Gemini에 맡겨도 좋은 일:

- changed files 요약
- 코어 경로 touched 여부 표시
- 위험 후보 의심 지점 표시
- 확인 필요 포인트 체크리스트 생성

출력 조건:

- 반드시 `의심`, `가능성`, `확인 필요` 언어 사용
- 수정 제안 금지
- 삭제/병합 제안 금지

---

## 3-3. pointer / path / surface consistency check

Gemini에 맡겨도 좋은 일:

- latest vs per-run pointer 구조 점검
- 링크 경로 존재 여부 확인
- latest/history/diff/queue/memory surface 혼선 여부 점검
- compacted surface가 raw history를 truth처럼 읽히게 하는지 검사

출력 조건:

- 정상 / 의심 / 문제
- 근거 경로 포함
- 수정 금지

---

## 3-4. discrepancy note

Gemini에 맡겨도 좋은 일:

- policy 문서와 실제 surface가 어긋나는 의심 지점 표시
- compare table과 prose summary의 불일치 표시
- process console payload와 report wording의 어긋남 표시

출력 조건:

- discrepancy note만
- 해결책 강요 금지
- Codex review required 문구 유지

---

## 3-5. log drafting support

Gemini에 맡겨도 좋은 일:

- 사람이 읽기 쉬운 로그 문장 초안
- receipt summary 초안
- batch run bullet summary 초안

출력 조건:

- 초안은 가능
- 실제 반영은 Codex만

---

## 4. bounded review support

아래는 맡길 수는 있지만, packet이 좁아야 한다.

## 4-1. cohort compare read

허용:

- 이미 존재하는 compare table을 읽고
- 공통 패턴 후보를 2~3개 제시

제한:

- final cohort judgment 금지
- canonical overwrite 제안 금지

## 4-2. attention pattern read

허용:

- queue / memory surface를 읽고
- 반복 attention 경향을 요약

제한:

- priority 조정 제안 금지
- resolution 상태 변경 제안 금지

## 4-3. state anomaly flagging

허용:

- 특정 asset state가 cohort 안에서 이례적인지 표시

제한:

- canonical value 재판정 금지
- 자동 수정 방향 제시 금지

---

## 5. forbidden work

아래는 절대로 Gemini CLI에 넘기지 않는다.

### 5-1. canonical state work

- canonical enum 선택
- state append/update
- latest overwrite
- history write
- blocker summary 최종 결정
- carryover / grounding / maturation 최종 판정

### 5-2. policy/core work

- schema 변경
- update policy 변경
- store 로직 변경
- runtime bridge 변경
- queue lifecycle 규칙 변경
- freeze 경계 변경

### 5-3. experimental promotion

- naming-heavy 해석을 canonical로 올리기
- object promotion
- high-level meaning object 승격
- compare-only 결과를 baseline으로 채택

### 5-4. destructive suggestion

- 삭제
- 병합
- compaction 승인
- raw history 정리
- “비슷하니 합치자”식 구조 변경

---

## 6. assignment packet rule

Gemini에 일을 넘길 때는 항상 아래 packet 형식을 따른다.

### required fields

- task_name
- role reminder: `read-only backend support only`
- exact input files
- forbidden actions
- expected output shape
- uncertainty rule
- output destination

### required forbidden line

아래 문구를 항상 포함한다.

`Do not modify files. Do not finalize policy. Do not promote meaning objects. Return only candidates, discrepancies, summaries, or checks.`

---

## 7. output destination rule

Gemini의 지속 기록은 `gemini/` 아래에만 남긴다.

예:

- `gemini/reviews/...`
- `gemini/checks/...`
- `gemini/briefings/...`
- `gemini/logs/...`

절대 금지:

- `docs/specs` 직접 수정
- `docs/reports` 직접 수정
- `runtime/views` 직접 수정
- `runtime/state` 직접 수정

---

## 8. handoff checklist

Gemini에 넘기기 전 Codex가 확인할 것:

1. 이 일이 read-only인가?
2. canonical 최종 판단이 필요한가?
3. core/derived/surface/experimental 경계를 건드리는가?
4. 출력이 summary/check/discrepancy 수준으로 충분한가?
5. 결과를 바로 반영하지 않고 review artifact로 받을 수 있는가?

하나라도 `아니오`면 Gemini에 넘기지 않는다.

---

## 9. return handling rule

Gemini 출력은 항상 아래 단계로만 쓴다.

1. Gemini output received
2. Codex review
3. Codex decides adopt / ignore / partial reflect
4. only then real project artifact update

즉 Gemini 결과는 언제나 **candidate layer**다.

---

## 10. prerequisite memory

업무 위임 전에는 반드시 아래 문서를 먼저 기준으로 본다.

- `resource_capability_boundary_memory_v1.md`

의미:

- Gemini를 Codex와 동등한 처리 주체로 가정하지 않는다
- 반복 검증 없이 위임 범위를 넓히지 않는다
- 능력 차이와 실패 위험 기록이 없는 상태에서는 delegation expansion을 금지한다

## 11. one-line lock

Gemini CLI에는 읽기/요약/비교/점검만 맡기고, canonical 판정·구조 변경·승격·반영은 끝까지 Codex가 맡는다.
