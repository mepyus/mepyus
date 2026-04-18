[[A]] [[OBJ:codex_directive]] [[SEM:middle_layer_role_resolution_refinement_pass_v1]]

# CODEx 지시서 — middle layer role resolution refinement pass v1

## 0. 목적
이번 턴의 목적은 middle layer를 새로 설계하는 것이 아니다.

이미 확인된 것은 다음과 같다.

- discourse anchor dominance reduced = YES
- topic-bearing anchor uplift observed = YES
- case block aggregation improved = YES
- provisional frame sketch visible = YES
- compare-ready packet produced = YES

즉 현재 문제는
**“middle layer가 작동하느냐”** 가 아니라
**“packet 안의 frame role이 아직 too coarse 하다”** 는 점이다.

따라서 이번 턴의 목표는 오직 하나다.

> **middle layer v0 packet의 frame role resolution을 한 단계 더 세분화해서, 인터뷰 3건이 compare-ready를 넘어 compare-meaningful 상태에 가까워지게 만드는 것**

이번 턴은 **Layer 3 + Layer 4 refinement 턴**이다.

## 1. 현재 잠금 상태

### 이미 확인된 것
- raw intake 그대로일 때보다 middle layer probe가 더 낫다
- generic discourse가 일부 눌렸다
- topic-bearing signal이 올라오기 시작했다
- case block와 provisional frame sketch가 보이기 시작했다
- compare-ready packet v0 생성 가능

### 아직 부족한 것
- 세 인터뷰 케이스의 frame role이 너무 coarse 하다
- Dario / Andrej / Alex 차이가 packet 단계에서 충분히 날카롭게 안 선다
- compare-ready는 되었지만 compare-meaningful까진 아직 부족하다

### 현재 읽기
- middle layer 존재 증명 = 통과
- role resolution = 추가 refinement 필요

## 2. 이번 턴에서 정확히 풀 문제

이번 턴은 아래 질문에 답해야 한다.

### Q1. 지금 packet 안의 role은 왜 너무 coarse 한가?
예:
- 너무 넓은 frame bucket만 있어서
  서로 다른 case가 비슷한 구조로 뭉개지는가?
- case block는 생겼지만 block role naming이 충분히 분화되지 않았는가?

### Q2. topic-bearing signal을 어떤 역할 층으로 더 잘 나눌 수 있는가?
이번 턴에서는 최소한 아래 수준의 role resolution 후보를 다룬다.

- 문제/제약 제시 역할
- 핵심 메커니즘 설명 역할
- 운영/검증/배치 역할
- 반성/갭/한계 역할
- observer-only 전환 역할

### Q3. 세 인터뷰가 이 역할 조합에서 더 다르게 보이게 만들 수 있는가?
예상 방향:
- Dario → scaling / verification / deployment governance 계열
- Andrej → RL / reflection gap / limitation inquiry 계열
- Alex → control / deployment / operationalization 계열

단, 이건 final fix가 아니라 **role resolution candidate** 수준으로만 본다.

## 3. 이번 턴의 최상위 원칙

### 원칙 1. Layer 1/2는 확장하지 않는다
이번 턴은 generic discourse를 더 세게 누르는 턴이 아니다.
핵심은 이미 올라온 signal을 더 나은 role로 배치하는 것이다.

### 원칙 2. Layer 3 + Layer 4만 bounded refinement 한다
- Layer 3: case block aggregation refinement
- Layer 4: provisional frame sketch / packet role refinement

### 원칙 3. source identity는 끝까지 유지한다
role refinement 때문에 문서 고유성이 약해지면 안 된다.

### 원칙 4. promotion은 여전히 금지다
이번 턴의 성공은 role separation 개선이지,
승격 수 증가가 아니다.

### 원칙 5. current/shared reality/core는 건드리지 않는다
이번 턴은 middle layer refinement 턴이지
기준면 개정 턴이 아니다.

## 4. 수정 대상과 비수정 대상

## 4-1. 수정 대상
우선순위 수정 대상은 아래다.

- `scripts/run_middle_layer_interview_probe.py`
- `docs/specs/middle_layer_layered_implementation_note_v1.md`
- 새 step2 결과 리포트 1건
- compare-ready packet v1 예시 1건

## 4-2. 비수정 대상
아래는 건드리지 않는다.

- promotion logic
- `runtime/views/current_asset_map_v1.md`
- shared reality / baseline 문서
- core engine
- `inputter.py`
- `labeler.py`

## 5. refinement 방향

## 5-1. Layer 3 refinement — case block role sharpening
현재 block aggregation은 존재하지만,
block의 의미 역할이 너무 넓게 잡혀 있을 수 있다.

이번 턴에서는 block를 단순 topic 묶음이 아니라
**case-bearing role block** 수준으로 약간 더 선명하게 만든다.

예시 후보:
- verification-oriented block
- reflection-gap block
- deployment/control block
- mechanism-grounding block
- transition/observer-only block

주의:
- block 종류를 과도하게 늘리지 않는다
- ontology처럼 굳히지 않는다
- 문서별 dominant role mix가 보이게만 하면 충분하다

## 5-2. Layer 4 refinement — provisional frame role resolution
packet 안의 frame sketch를 아래처럼 한 단계 더 분리한다.

현재 v0가
- broad frame summary
- coarse role cluster
수준이라면,

이번 v1에서는
- dominant role 1~2개
- secondary role 1~2개
- defer / observer-only role
정도까지 보이게 한다.

예시 packet 필드 후보:
- `dominant_roles`
- `secondary_roles`
- `observer_only_roles`
- `role_evidence_terms`
- `case_specific_signals`
- `caution_notes`

주의:
- final schema 확정 금지
- v1 experimental packet으로만 둔다

## 6. 권장 역할 분해 기준

이번 턴에서 사용할 role 분해 기준은 아래 정도로 제한한다.

### A. problem_or_constraint_role
- 한계, 병목, 제약, 문제 정의 쪽

### B. mechanism_role
- 구조, 작동 원리, 핵심 메커니즘 설명 쪽

### C. verification_or_evaluation_role
- 검증, 평가, scaling check, reliability check 쪽

### D. control_or_deployment_role
- 운영, 배치, 제어, 실사용 전개 쪽

### E. reflection_or_gap_role
- 반성, 미흡함, 사고 갭, 한계 인식 쪽

### F. observer_or_transition_role
- 발화 전환, 수사, 연결, 강조, 진행 정리 쪽

주의:
- 이 role set은 이번 턴용 bounded working set이다
- baseline이나 ontology로 승격하지 않는다

## 7. 구현 방식

## 7-1. read-only refinement 유지
이번 턴도 read-only / experimental 형태로 간다.

가능한 위치:
- `scripts/run_middle_layer_interview_probe.py`
- `app/work/middle_layer_experiments/...`

## 7-2. before/after를 반드시 남긴다
이번 턴은 refinement이므로
v0 대비 무엇이 달라졌는지 보여야 한다.

반드시 비교할 것:
- coarse role vs refined role
- case별 dominant role 차이
- generic discourse 억제 유지 여부
- packet readability 개선 여부

## 7-3. packet v1 예시 생성
최소 1개 이상의 compare-ready packet v1 예시를 생성한다.
가능하면 기존 3케이스 전체를 다시 돌려서
v0와의 차이를 드러내는 것이 좋다.

## 8. 검증 기준

## 8-1. 1차 검증
- generic discourse dominance가 다시 심해지지 않았는가
- source identity가 유지되는가
- topic-bearing anchors가 계속 보이는가

## 8-2. 2차 검증
- Dario / Andrej / Alex의 dominant role 조합이 서로 달라지는가
- review / compare flattening이 v0보다 더 줄어드는가
- block aggregation이 case별로 더 다른 형태를 보이는가

## 8-3. 3차 검증
- packet이 “있다” 수준을 넘어 “비교할 만하다” 수준으로 가는가
- role_evidence_terms가 이해 가능하게 보이는가
- defer / observer-only 구역이 명확한가

## 9. 성공 기준

아래가 되면 성공이다.

- frame role resolution이 v0보다 선명해진다
- 문서별 dominant role mix가 다르게 보인다
- compare-ready packet v1이 생성된다
- v0보다 case-specific frame 읽기가 쉬워진다
- current/shared reality/core untouched 유지
- promotion still untouched 유지

## 10. 실패 신호

아래가 보이면 실패 또는 drift warning이다.

- role 종류를 과도하게 늘려 해석이 더 어려워짐
- packet이 복잡해졌는데 문서 차이는 더 안 보임
- source identity가 희미해짐
- generic discourse 억제가 무너짐
- refinement가 곧바로 기준 승격처럼 변함
- current/baseline을 건드리기 시작함

## 11. 권장 산출물

### 구현/실험
- `scripts/run_middle_layer_interview_probe.py` refinement 반영
- `app/work/middle_layer_experiments/generated/...packet_v1...`

### 문서
- `docs/reports/middle_layer_thickening_step2_result_v1.md`
- 필요 시 `docs/specs/middle_layer_layered_implementation_note_v1.md` 보강

### 운영 흔적
- receipts
- `runtime/logs/repo_delta_log.jsonl`
- 필요 시 `runtime/views/repo_delta_log_latest_v1.md` 짧은 반영

### 금지
- current asset map 수정
- baseline/shared reality 수정
- promotion logic 수정
- raw inputter/labeler 본체 패치

## 12. 결과 보고 형식

```markdown
# middle layer role resolution refinement result

## 1. refined scope
- layer 3: YES/NO
- layer 4: YES/NO

## 2. what changed
- [짧게]

## 3. verification
- discourse anchor dominance still reduced: YES/NO
- topic-bearing anchor uplift retained: YES/NO
- case-specific dominant roles more visible: YES/NO
- defer/observer-only roles clearer: YES/NO
- compare-ready packet v1 produced: YES/NO

## 4. untouched
- promotion logic: YES
- current asset map: YES
- shared reality/baseline: YES
- core engine: YES

## 5. optional note
- later promotion still premature: YES/NO
- one more refinement useful: YES/NO

## 6. result
- status: PASS | PASS_WITH_NOTE | REVIEW_REQUIRED

## 7. one-line summary
- [한 줄]
```
