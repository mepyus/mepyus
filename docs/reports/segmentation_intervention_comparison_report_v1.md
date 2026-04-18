[[A]] [[OBJ:segmentation_intervention_comparison_report_v1]] [[SEM:before_after_comparison_for_minimal_segmentation_support_probe]]

# segmentation intervention comparison report v1

## 1. purpose

- 이번 비교의 목적은 segmentation support가 실제로 2차 판독 생존 조건을 바꾸는지 보는 것이다.
- 즉 이 보고서는 `개선 자랑`이 아니라 `1순위 가설 검증` 문서다.

## 2. intervention summary

- input_asset: `inputs/external_cases/claude_code_index.txt`
- baseline:
  - 기존 `run_dialogue_asset_probe.py` 분절
- intervention:
  - `--segment-assist index_support`
  - 짧은 제목줄 + 타임스탬프를 segmentation hint로 사용
- unchanged:
  - pointer handling
  - heading-independent role reading
  - object lift logic

## 3. baseline state

- baseline probe:
  - block_count: `1`
  - window_count: `1`
  - top question window: `0_0`
- downstream baseline:
  - question-inducing candidate: `0_0` 하나
  - pivot_windows: `0_0`
  - context unit refs: 전부 empty
- baseline failure summary:
  - single block collapse
  - weak window diversity
  - naming without support
  - empty-ref context unit

## 4. after segmentation support

- support probe:
  - block_count: `518`
  - window_count:
    - `w3/s1`: `516`
    - `w4/s2`: `258`
    - `w6/s3`: `172`
    - `w8/s4`: `129`
- top question windows became distributed:
  - `515_517`, `157_159`, `277_279`, `379_381`, `380_382`
- support 이후 top windows는 더 이상 `0_0` 단일 mega block에 묶이지 않았다

## 5. reusable attitude comparison

### A. question opening

- baseline:
  - single candidate `0_0`
  - score는 높았지만 사실상 collapse 위의 false concentration이었다
- after support:
  - high-score windows는 여러 개 생겼다
  - 하지만 기존 threshold 기준 question-inducing candidate는 `0개`가 되었다
- reading:
  - segmentation support는 `window diversity`를 회복시켰다
  - 하지만 `question-inducing candidate`를 안정적으로 살리기에는 segmentation alone이 부족했다

### B. relation movement

- baseline:
  - relation hints는 단일 block 안에 broad하게 묶여 있었다
- after support:
  - relation hints는 여러 window에 분산되며 남았다
  - `transition`, `execution_shift`, `question_generation` 태도 자체는 유지됐다
- reading:
  - relation movement는 segmentation support 후에도 살아남는 reusable attitude다
  - 다만 지금은 흐름 분화보다 broad tagging 성격이 여전히 강하다

### C. residue priority shift

- baseline:
  - discourse/filler residue가 존재했고 opening priority 문제로 읽혔다
- after support:
  - residue가 사라진 게 아니라 여러 window로 퍼졌다
  - support 이후 question-inducing candidate가 비어, residue deprioritization surface도 직접 비교할 대상이 약해졌다
- reading:
  - residue를 summary-stage priority 문제로 보는 태도는 유지된다
  - 하지만 segmentation alone은 residue-aware summary surface를 복구하는 충분조건이 아니었다

## 6. context unit / pivot / compression comparison

- baseline:
  - pivot_windows: `0_0`
  - context unit names survive but refs empty
- after support:
  - top windows는 분산됐지만
  - `question_inducing_candidates = 0`
  - `pivot_windows = []`
  - context unit `present_window_refs`는 여전히 전부 empty
- reading:
  - segmentation support만으로 context unit / pivot / compression은 거의 회복되지 않았다
  - 이건 다음 2순위가 pointer인 이유를 더 강하게 만든다

## 7. naming-without-support / empty-ref comparison

- naming-without-support:
  - baseline에서도 강했음
  - support 후에도 object naming은 여전히 AI dialogue vocabulary를 강하게 끌고 감
- empty-ref:
  - segmentation support 이후에도 context unit ref는 회복되지 않음
- reading:
  - `segmentation`은 collapse를 푸는 데는 유효했지만
  - `grounding` 문제는 `pointer` 축 없이는 해결되지 않는다

## 8. verdict

- what segmentation support actually recovered:
  - single block collapse 완화
  - window diversity 회복
  - relation movement를 볼 수 있는 분산 구조 확보
- what segmentation support did not recover:
  - stable question-inducing candidates
  - pivot / compression recovery
  - context unit ref grounding
  - naming-with-support coherence
- why pointer is still next:
  - support 이후에도 `이름은 있는데 ref가 없음` 문제가 핵심으로 남았다
  - 즉 segmentation 다음은 pointer가 맞다
- why object lift remains hold:
  - diversity는 생겼지만 grounded second-order support는 아직 약하다
  - 지금 단계에서 object naming을 더 올리면 오히려 overfire가 커질 수 있다

## 9. one-line summary

> segmentation support는 `claude_code_index`의 single block collapse를 실제로 완화했지만, question-inducing candidate / pivot / context-unit grounding을 회복시키기에는 부족했고, 그래서 다음 우선순위가 pointer라는 점과 object lift hold 이유가 더 선명해졌다.
