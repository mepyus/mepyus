# watchpoint to engine origin mapping v1

## 1. verdict

현재 watchpoint들은
UI surface 자체의 구현 결함이라기보다,
**process-console payload richness / adapter shaping / intentional baseline suppression / current compare model limitation**
중 하나에서 오는 얇음으로 읽는 편이 맞다.

즉 지금 단계의 핵심은
UI를 더 손보는 것이 아니라,
어떤 얇음이 어느 origin layer에서 오는지 분리해서 보는 것이다.

## 2. watchpoint-to-origin mapping

### 2-1. board grounding absence

#### surface symptom

- board card에 grounding이 직접 surface되지 않는다
- 자연 live path 전반에서 card helper에
  `grounding not surfaced in board card v1`가 반복된다

#### likely origin layer

- `intentional baseline suppression`
- `adapter/model shaping`
- `process-console payload`

#### mapping note

1. process-console builder는 canonical fields에 `grounding_status`를 이미 담는다
   - 즉 engine/process-console 쪽에 grounding 자체가 없는 것은 아니다

2. 하지만 adapter의 `boardItems`는
   - `packetTextureLabel`
   - `maturationLabel`
   - `traceabilityLabel`
   - `emergenceLabel`
   중심으로 잘려 있다

3. 따라서 현재 증상은
   - engine raw의 부재라기보다
   - board surface를 intentional thin selection layer로 유지하기 위한
     adapter/model shaping과 baseline suppression의 결과에 더 가깝다

#### why this is not yet an implementation bug

- grounding이 완전히 사라진 것이 아니다
- detail/state 쪽 canonical reading에는 존재한다
- board에서만 의도적으로 suppress한 상태다

### 2-2. compare candidate thin relation

#### surface symptom

- compare panel은 candidate 존재 여부는 읽히지만
  relation thickness는 얇다
- natural live path에서 `reason`이 거의 비어 있어
  실질적으로 `assetId/title fallback` 중심으로 읽힌다

#### likely origin layer

- `compare model limitation`
- `process-console payload`
- 일부 `adapter/model shaping`

#### mapping note

1. compare builder는 `compare_entry.related_assets`를 생성하지만,
   current first-pass model은 본질적으로 flat하다

2. adapter는 이를 그대로
   - `assetId`
   - `reason`
   수준으로 넘긴다

3. 즉 지금의 thinness는
   UI panel이 덜 만들어져서라기보다
   **current compare model 자체가 hint-level richness에 머무는 것**에 더 가깝다

4. adapter도 title/meta enrichment를 추가로 하지 않으므로
   얇음이 그대로 보인다

#### why this is not yet an implementation bug

- compare panel mini-spec은 first-pass를
  existing `compareCandidates`만으로 제한했다
- 현재 flatness는 spec 위반이 아니라
  spec이 허용한 thinness의 결과다

### 2-3. detail summary blocker/history quietness

#### surface symptom

- blocker/history가 quiet summary 수준으로만 읽힌다
- full detail이나 trace surface처럼 두껍게 나오지 않는다

#### likely origin layer

- `intentional baseline suppression`
- 일부 `adapter/model shaping`

#### mapping note

1. process-console payload는
   `gate_blockers`, `history_summary` 같은 최소 정보는 이미 준다

2. adapter도 이를 selected asset summary model에 싣고 있다

3. 하지만 detail summary panel은
   full explorer가 아니라 read-only summary panel로 intentionally 제한돼 있다

#### why this is not yet an implementation bug

- 필요한 최소 정보는 이미 있다
- 현재 quietness는 data missing보다 surface restraint에 더 가깝다

## 3. origin confidence

### board grounding absence

- confidence: `high`

이유:
- builder 쪽 canonical fields에 grounding이 존재하는 것이 확인된다
- 반면 board-facing adapter model에는 grounding이 없다
- 따라서 suppression/shaping 기여가 크다는 판단의 확신이 높다

### compare candidate thin relation

- confidence: `high`

이유:
- natural live observation에서 reason이 거의 비어 있었고
- adapter도 `assetId + reason` 수준만 전달한다
- current compare model limitation으로 보는 것이 가장 자연스럽다

### detail summary blocker/history quietness

- confidence: `medium`

이유:
- 현재 quietness는 intentional restraint로 읽히지만
- blocker/history가 실제 runtime에서 얼마나 풍부하게 들어오는지에 대한
  장기 관찰은 아직 많지 않다

## 4. intentional suppression vs future engine candidate

### intentional baseline suppression으로 남기는 것이 맞는 것

- board에서 grounding을 바로 싣지 않는 현재 결정
- detail summary를 full explorer로 키우지 않는 현재 제한
- strip/detail/activity 간 책임 분리 유지

### future engine-side candidate가 될 수 있는 것

- board grounding absence
  - 이유: raw engine/process-console에는 grounding이 있는데
    board-facing model에서만 계속 생략되고 있기 때문이다

- compare candidate thin relation
  - 이유: current compare model 자체의 richness가 얇아서
    future engine-side enrichment 후보로 이어질 가능성이 크다

- detail summary blocker/history quietness
  - 현재로선 아직 strong candidate라기보다
    intentional restraint에 더 가깝다

## 5. comparative note

두 주요 watchpoint를 비교하면,

### board grounding absence

- engine raw에는 이미 grounding이 있다
- 따라서 미래 후보가 된다면
  **existing engine/process-console signal을 board-facing model에서 어떻게 제한적으로 surface할지**
  쪽 문제에 가깝다

### compare candidate thin relation

- current compare model 자체가 flat하다
- 따라서 미래 후보가 된다면
  **engine-side compare model richness 자체를 조금 더 올릴지**
  쪽 문제에 더 가깝다

### which is more likely to lead to engine-side enrichment

- 현재로선 `compare candidate thin relation`이
  더 직접적으로 engine-side enrichment 후보로 이어질 가능성이 높다

이유:
- board grounding absence는 existing signal reuse 문제지만
- compare thin relation은 current compare model limitation 자체가 더 직접적이기 때문이다

## 6. recommendation

판정:
- **engine-side candidate note로 넘어감**

이유:
- 이번 mapping에서
  watchpoint가 단순 UI 문제보다 origin layer 얇음에서 온다는 점이 더 분명해졌다
- 특히 compare candidate thin relation은
  future engine-side candidate로 연결될 가능성이 상대적으로 더 높다

중요:
- 이 recommendation은 곧바로 enrichment proposal로 점프하자는 뜻은 아니다
- 다음 단계는 implementation이 아니라
  **engine-side candidate note** 수준의 더 좁은 정리로 가는 것이 맞다

## 7. codex alignment note

- 감독관의 “UI stay watch, engine-origin mapping으로 전환” 판단에 대체로 동의한다.
- 이번 review에서 watchpoint들은 UI-side polish보다 origin layer 얇음과 더 강하게 연결됐다.
- 다만 board grounding absence는 existing signal reuse 문제라,
  future에도 UI-side에서 다시 볼 여지는 남는다.
- resolution:
  - compare thin relation은 engine-origin candidate 쪽으로 더 무게를 두고
  - board grounding absence는 suppression vs reuse 경계로 계속 본다.
