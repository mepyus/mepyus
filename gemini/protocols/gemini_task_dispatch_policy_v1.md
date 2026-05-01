# gemini_task_dispatch_policy_v1.md

## 1. purpose

이 문서는 Gemini CLI에 업무를 넘길 때의 허용 범위와 출력 형식을 잠그기 위한 정책이다. 핵심은 Gemini를 **Bounded Worker**로 유지하여 공간의 중심 구조를 보호하는 것이다.

---

## 2. top rule: Default No-Write

Gemini CLI는 기본적으로 **no-write / draft-only** 모드로 동작한다. 모든 출력은 `worker_return`으로 간주되어 User/Codex의 검산을 거쳐야 한다.

---

## 3. safe task classes (Bounded)

## 3-1. summary / briefing / draft

Gemini에 맡겨도 좋은 일 (Default 허용):

- receipt / operation board 요약
- process console 상태 브리핑
- 초안(draft) 및 리스트(listing) 생성
- latest/history/diff 요약문 생성

출력 조건:

- **Candidates Only:** 모든 제안은 후보군으로만 표시
- 새로운 canonical 판단 및 구조 설계 금지

---

## 3-2. verification / comparison / test-reading

Gemini에 맡겨도 좋은 일 (Default 허용):

- 테스트 결과 판독 및 검증 (Verification)
- 데이터 일관성 비교 (Comparison)
- 확인 필요 포인트 체크리스트 생성

출력 조건:

- 수정/삭제 제안 금지
- 결과는 `evidence`로만 보고

---

## 4. restricted & forbidden work

## 4-1. restricted tasks (Requires Explicit Assignment)

아래 업무는 기본적으로 금지되며, User/Codex가 **정확한 대상 파일과 허용 범위**를 지정한 경우에만 예외적으로 수행한다.

- **Mechanical Cleanup / Edits:** 반복적인 문서 업데이트 등.
- **Surgical Edits:** 명시적으로 승인된 특정 파일의 국소적 수정.

제한 조건:
- 수정 전후의 `worker_return` 리뷰가 필수임.
- 코어 코드/스키마/런타임 수정은 절대 금지.

## 4-2. forbidden work (Absolute)

아래는 절대로 Gemini에 넘기지 않으며, Gemini가 스스로 수행해서도 안 된다.

- **Self-Role Expansion:** 스스로 역할을 확장하거나 "업그레이드"되었다고 선언하는 행위.
- **Baseline Authority:** canonical enum 선택, 최종 상태 판정, 정책 확정.
- **Core Edits:** 스키마, 컨트롤러, 런타임 브리지, 엔진 내부 로직 수정.
- **Destructive Suggestion:** 삭제, 병합, 압축 승인.

---

## 5. assignment packet rule

Gemini에 일을 넘길 때는 항상 아래 문구를 포함해야 한다.

`Do not modify core files. Do not finalize policy. Do not promote meaning objects. Gemini output must be reviewed as worker_return. Default mode is no-write.`

---

## 6. return handling rule

Gemini의 모든 출력은 **Candidate Layer**로 취급한다.

1. Gemini output received as `worker_return`.
2. Codex/User review and validation.
3. Only Codex performs the actual space/baseline update.

---

## 7. one-line lock

**Gemini must not broaden its own role. Gemini must not declare itself upgraded. Gemini is a bounded worker for draft, test, and verification only.**

---

**Incident note:**
A prior wording pass over-promoted Gemini from bounded verification worker to active assistant/code-editing layer. The accepted correction is to keep Gemini as a bounded worker. Any Gemini output is evidence, not decision. Any Gemini role expansion requires user approval and Codex review.
