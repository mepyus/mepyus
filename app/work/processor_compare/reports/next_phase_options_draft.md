# next phase options draft

## 1. current checkpoint

- 현재 엔진은 `space app`이 아니라 `연결 층위 엔진`으로 정의되어 있다.
- `canonical 승인`과 `space 인정`은 이미 분리됐다.
- `doc_006`은 `canonical`은 아니지만 `space pre-entry review candidate`다.
- `doc_005`, `doc_004`는 현재 `translation_missing` exploration control이다.
- weak / blocked / review / proposal trace는 보류 자산으로 유지된다.
- `policy / fixture / surface / lifecycle / timestamp / ledger / runner` 경계가 1차로 확보됐다.
- 따라서 다음은 더 많은 판정 필드를 더하는 단계가 아니라, 어떤 작업축을 Phase로 열 것인지 선택하는 단계다.

## 2. current diagnosis

- 지금 엔진의 가장 큰 병목은 “필드 부족”이 아니다.
- 가장 큰 병목은 `승인 정책이 아직 완전히 잠기지 않았다`는 점이다.
- 특히 `doc_006`은 translation / processing / observer / same-local_ref multi-family support까지는 충분하지만, `direct canonical overlap`을 어떤 규칙으로 승인할지 정책이 아직 phase-level로 정리되지 않았다.
- 반면 lifecycle / ledger / fixture 운영 접합부는 최소 의미를 가지기 시작했다.
- 모델 부착은 아직 review/canonical 정책이 더 잠기기 전이라 인터페이스를 고정하기 이르다.

## 3. phase A — approval policy phase

### purpose
- direct canonical overlap 승인 규칙을 잠근다.
- direct / derived / translated / token-supported evidence의 인정 범위를 정리한다.
- family 가중치와 `same-local-ref 내부 지지` vs `cross-path 직접 겹침` 관계를 정책으로 정리한다.

### why needed now
- `doc_006`의 다음 병목은 운영 부재가 아니라 승인 기준 부재다.
- 현재 엔진은 “왜 아직 canonical이 아닌가”를 충분히 설명할 수 있지만, “무엇이 더 있으면 canonical로 인정할 것인가”는 아직 정책 phase로 고정되지 않았다.

### what it gives if opened now
- review candidate와 canonical 사이의 승인 문법을 명확히 잠글 수 있다.
- `space pre-entry` 이후를 더 파더라도 코어 판정이 흔들리지 않게 된다.
- 이후 운영 자동화나 모델 부착이 기대는 기준점이 생긴다.

### risk if not opened now
- 이후 automation이 약한 임시 규칙 위에 올라간다.
- 모델 부착 시 unstable policy를 feature/interface로 굳히게 된다.
- `live_input_space.py` 밖으로 뺀 policy boundary가 있어도 정책 기준 자체가 계속 미정 상태로 남는다.

### entry criteria
- 구조 완성선 도달: 완료
- review lane / fixture / lifecycle / ledger 안정화: 완료
- control reading 고정: 완료
- 따라서 **지금 바로 열 수 있다**

### no-go
- translation 확대 금지
- processing refinement 재개 금지
- canonical threshold 완화 금지
- viewer 작업 금지

## 4. phase B — operation automation phase

### purpose
- hot / warm / cold 이동 규칙을 실제로 굴린다.
- revisit scheduling, warm downgrade, cold archive 후보 규칙을 도입한다.
- state_signature drift를 기반으로 운영 자동화를 붙인다.

### why needed
- trace가 계속 누적되기 때문에 운영 자동화는 장기적으로 필요하다.
- 지금은 ledger와 runner가 최소 운영 의미를 가지기 시작했기 때문에 다음 단계로 연결 가능하다.

### what it gives if opened now
- blocked control과 active review candidate를 운영적으로 다르게 관리할 수 있다.
- revisit, downgrade, archive 후보를 자동으로 분류할 수 있다.
- 이후 state explosion 위험을 완화할 접합부가 생긴다.

### risk if not opened now
- trace가 계속 hot/warm 상태에 머무르며 장기적으로 과포화 위험이 있다.
- 운영 판단이 계속 수동 보고서에 의존한다.

### risk if opened too early
- 승인 정책이 덜 잠긴 상태에서 automation을 먼저 넣으면 임시 판정을 운영 규칙으로 고정해버릴 수 있다.
- wrong temperature movement가 이후 해석을 오염시킨다.

### entry criteria
- lifecycle semantics 고정: 완료
- ledger / runner 운영 접합부: 완료
- approval policy 잠금: **미완료**
- 따라서 **지금 열 수는 있지만 1순위는 아님**

### no-go
- pruning 자동화부터 먼저 시작 금지
- policy behavior 변경 금지
- 아직 unstable한 review rule을 temperature rule로 고정 금지

## 5. phase C — model attachment readiness phase

### purpose
- processing / review / state vector를 향후 예측/시나리오/학습 모델이 붙을 수 있는 인터페이스로 정리한다.
- history / transition / snapshot schema를 모델 입력 관점에서 정리한다.
- export layer와 feature surface를 만든다.

### why needed later
- 이 엔진의 장기 목적은 “정답 기계”가 아니라 가능성 조합을 펼쳐보는 엔진이므로, 나중에 모델 부착은 중요한 phase다.
- 하지만 지금은 정책과 approval grammar가 아직 충분히 잠기지 않았다.

### what it gives if opened
- 예측 / 시뮬레이션 / 학습 모델이 붙을 표준 인터페이스가 생긴다.
- review vector와 state transition을 모델이 소비할 수 있게 된다.

### risk if not opened now
- 단기적 위험은 크지 않다.
- 다만 이후 interface 설계가 늦어질 수 있다.

### risk if opened too early
- unstable review/canonical 정책을 그대로 feature로 굳힌다.
- 나중에 policy가 바뀔 때 model interface도 연쇄적으로 흔들린다.
- 잘못된 state semantics 위에 예측기를 얹어 과적합을 유발할 수 있다.

### entry criteria
- approval policy 잠금: 필요
- lifecycle semantics와 ledger semantics 안정화: 필요
- feature/export grammar 정의: 필요
- 따라서 **지금은 열면 안 된다**

### no-go
- unstable review state를 그대로 model feature로 고정 금지
- canonical approval policy 미잠금 상태에서 export schema 고정 금지
- viewer surface를 model API처럼 오용 금지

## 6. entry criteria summary

### phase A
- 지금 바로 열 수 있는가: `yes`
- 준비된 것:
  - review lane 충분
  - fixture/control 안정
  - lifecycle/ledger 기본 안정화
- 아직 부족한 것:
  - direct canonical overlap 승인 정책 자체

### phase B
- 지금 바로 열 수 있는가: `partial`
- 준비된 것:
  - lifecycle semantics 고정
  - ledger / runner / state signature 존재
- 아직 부족한 것:
  - approval policy finalization

### phase C
- 지금 바로 열 수 있는가: `no`
- 준비된 것:
  - rich review state와 process trace
- 아직 부족한 것:
  - approval policy stability
  - export/value grammar stability

## 7. risks if opened too early

### phase A too early
- 현재는 이미 entry criteria를 만족하므로 “너무 이르다”보다 “지금 열어야 한다”에 가깝다.

### phase B too early
- 잘못된 review/canonical 기준을 automation으로 굳힌다.
- warm/cold movement가 policy 대신 운영 편의 기준으로 먼저 굳을 수 있다.

### phase C too early
- unstable state grammar를 feature interface로 박아버린다.
- policy가 바뀔 때 model layer도 함께 붕괴한다.

## 8. recommended order

1. **Phase A — 승인 정책 Phase**
   - 이유: 현재 가장 큰 병목은 운영이 아니라 승인 기준 자체다.
   - `doc_006`의 다음 병목도 automation이 아니라 direct canonical overlap 승인 정책이다.

2. **Phase B — 운영 자동화 Phase**
   - 이유: lifecycle / ledger 접합부는 이미 생겼고, approval policy가 잠긴 뒤에는 automation이 자연스럽게 따라온다.

3. **Phase C — 모델 부착 준비 Phase**
   - 이유: 지금은 policy가 아직 흔들릴 수 있어서 인터페이스를 모델 쪽에 고정하기 이르다.

## 9. final recommendation

- **recommended_next_phase: Phase A — approval policy phase**
- **why_now**
  - 현재 병목은 direct canonical overlap 승인 규칙이다.
  - `doc_006`은 운영상으로는 충분히 읽히지만 approval policy는 아직 final grammar가 없다.
- **why_not_yet**
  - Phase B는 policy를 잘못 고정할 위험이 있다.
  - Phase C는 unstable policy를 feature interface로 굳히게 된다.
- **next_after_that**
  - Phase B — operation automation phase

## 10. final sentence

- 지금은 더 많은 판정 필드를 쌓을 때가 아니라,
- `approval policy -> operation automation -> model attachment readiness`
순으로 Phase를 여는 것이 맞다.
- 따라서 **다음으로 열어야 할 Phase는 승인 정책 Phase** 다.
