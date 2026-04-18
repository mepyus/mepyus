# vectorfl line bundle attachment notes v0

## purpose

이 문서는 `VectorFL Paper`에서
line / routing / lane comparison에
internal recall evidence bundle을 어떻게 붙였는지 기록한다.

핵심은
근거 묶음을 page 장식으로 나열하는 것이 아니라,
`왜 지금 이 line에 이 근거를 붙였는가`
를 다시 설명 가능한 상태로 남기는 것이다.

---

## current attachment rule

### line default spine

모든 generated line에는 우선 아래 두 묶음을 기본으로 붙인다.

- `bundle_01_raw_intake_middle_layer_gap`
- `bundle_05_visible_split_to_recall_surface`

이유:
- line을 너무 빨리 납작하게 만들지 않기 위해서는
  intake가 남긴 segmentation / role / relation 구조를 계속 들고 가야 한다.
- line이 사람이 읽을 수 있는 surface가 되려면
  visible split / readable input board / early linked segment가 함께 보여야 한다.

### line-specific third bundle

세 번째 묶음은 line의 말결에 따라 갈린다.

- recall / record / internal reopening 쪽 line이면
  `bundle_02_reentry_survival_without_promotion`
- 나머지 line은 우선
  `bundle_03_meaning_vs_format_disentangle`

현재 구현은 first pass라
정교한 semantic classifier 대신
line index parity와 recall-oriented wording을 같이 본다.
이건 임시 규칙이며,
다음엔 line dossier / family / role hints를 같이 읽는 쪽으로 바꿔야 한다.

---

## routing attachment rule

`Routing`에는 아래 묶음을 붙인다.

- `bundle_02_reentry_survival_without_promotion`
- `bundle_04_business_corridor_subaxis_mix`
- `bundle_01_raw_intake_middle_layer_gap`

이유:
- 다시 붙었다고 곧바로 넘기면 안 되므로
  reentry와 promotion을 분리해서 읽어야 한다.
- business처럼 평평한 흐름은
  실제론 여러 축으로 나뉠 수 있으므로
  한 번에 한 팀으로 넘기지 않게 하는 근거가 필요하다.
- intake 구조가 얇으면 routing도 성급해진다.

---

## lane comparison attachment rule

`Lane Runs`에는 아래 묶음을 붙인다.

- `bundle_01_raw_intake_middle_layer_gap`
- `bundle_03_meaning_vs_format_disentangle`
- `bundle_04_business_corridor_subaxis_mix`

이유:
- lane 차이는 결국 어떤 입력 재료를 들고 시작했는지에 크게 좌우된다.
- meaning / format disentangle는
  lane별로 무엇을 뜻으로 읽고 무엇을 형식 echo로 읽는지 비교하게 한다.
- business sub-axis mix는
  lane별 세분화 품질을 비교하게 한다.

---

## what this means for paper

이 규칙이 들어가면서
`VectorFL Paper`는 단순히 bundle을 나열하지 않고,

- 왜 이 line에 이 근거가 붙는지
- 왜 이 routing에 이 근거가 필요한지
- 왜 lane 비교가 그냥 모델 비교가 아닌지

를 표면에서 바로 읽게 된다.

즉 bundle은 decorate block이 아니라
`읽기 근거의 번역기`로 취급해야 한다.

---

## known limits

- 아직 line별 bundle selection이 heuristic에 가깝다.
- dossier의 declaration/directive/past-conversation linkage를
  실제 bundle id와 자동 연결하는 단계는 아직 아니다.
- family / role hints / uncertainty block을 더 읽으면
  line별 bundle matching은 더 좋아질 수 있다.

---

## next hardening

- line dossier 안의 linkage 항목과 bundle id를 직접 매핑하기
- stage3 / stage5 generated artifact를 더 깊게 읽어
  bundle 후보를 5개에서 8~10개 수준으로 늘리기
- selected line이 바뀌면
  Inspector / Routing / Lane Runs의 evidence selection도 함께 달라지게 만들기
