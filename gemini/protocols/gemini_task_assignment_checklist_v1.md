# gemini_task_assignment_checklist_v1.md

## purpose

Gemini CLI에 업무를 넘기기 전에
Codex가 빠르게 안전 여부를 판단하기 위한 체크리스트다.

---

## 1. safe to assign

아래면 대체로 안전하다.

- read-only summary
- diff review
- pointer/path check
- discrepancy note
- surface wording draft
- queue/memory thin briefing

---

## 2. assign only if tightly bounded

아래는 입력/출력 범위를 좁혀야 한다.

- cohort compare read
- attention tendency summary
- anomaly flagging
- policy vs surface mismatch review

조건:

- exact file list 제공
- output shape 제한
- final judgment 금지

---

## 3. never assign

- canonical enum selection
- state append/update
- latest/history write
- queue status change
- policy rewrite
- freeze change
- object promotion
- deletion / merge / compaction approval

---

## 4. required prompt footer

항상 아래 의미를 넣는다.

- read-only only
- no file modification
- no final policy judgment
- no promotion
- no destructive suggestion
- uncertainty must be explicit

---

## 5. handling rule

Gemini output is:

- candidate
- discrepancy
- summary
- check

never:

- final authority
- direct patch
- direct overwrite

---

## 6. prerequisite

업무를 넘기기 전 먼저 본다.

- `resource_capability_boundary_memory_v1.md`

기억할 것:

- 외부 자원은 Codex와 동일한 처리 주체가 아니다
- delegation은 반복 검증 후에만 확장한다
