# compare candidate enrichment field-spec review tightening v1

## 1. verdict

판정:
- **tighten into field_spec_draft_v2**

즉 이번 review 결과,
`field_spec_draft_v1`은 전체 방향은 타당하지만
그대로 keep하기보다는
몇몇 표현을 더 조여서 v2로 정리하는 편이 안전하다.

## 2. package structure choice

이번 패키지는 **2문서 구조**를 택했다.

구성:
- 이 문서:
  - review
  - inflation scan
  - keep/tighten decision
  - risk/correction/alignment 기록
- tightening 결과 문서:
  - [compare_candidate_enrichment_field_spec_draft_v2.md](/Users/sungsookim/universe/vectorfl_replica/docs/proposals/compare_candidate_enrichment_field_spec_draft_v2.md)

왜 이렇게 했는가:
- review 판단과 tightened draft를 한 문서에 겹치면
  무엇이 문제였고 무엇을 조였는지가 흐려질 수 있다
- broad package completion을 분명히 하기 위해
  review와 tightened result를 분리했다

## 3. field-spec review summary

### overall reading

- `field_spec_draft_v1`은
  compare model 중심 / payload shaping 보조 / non-goal 유지라는 큰 방향은 잘 지켰다
- 하지만 일부 표현은
  아직 field-like structure를 너무 빨리 상정하는 쪽으로 읽힐 여지가 있었다

### review focus

이번 review는 아래를 중심으로 봤다.

- layer 명칭이 사실상 concrete field name처럼 굳는지
- compare model 중심이 유지되는지
- payload shaping이 supporting role을 넘지 않는지
- UI consumer 상정이 숨어들지 않았는지
- non-goal이 계속 지켜지는지

### conclusion

- compare model 중심성과 non-goal은 유지됐다
- payload shaping도 보조 역할을 넘지 않았다
- 하지만 `field layer outline`과 `layer 1/2/3` 명칭은
  너무 이르게 contract shape를 구조화하는 인상을 줄 수 있었다

## 4. inflation scan

### 1. concrete-field drift

- 있음

근거:
- `layer 1 / layer 2 / layer 3` 식의 명명은
  아직 field spec draft라 하더라도
  사실상 concrete slot 구조처럼 읽힐 여지가 있다

### 2. schema drift

- 없음

근거:
- schema shape나 payload branch 설계로는 넘어가지 않았다

### 3. payload-centralization drift

- no critical drift

근거:
- payload shaping은 계속 supporting role로만 유지됐다

### 4. UI-led interpretation drift

- no critical drift

근거:
- UI consumer behavior나 layout 상정은 계속 비범위로 남았다

### 5. recommendation/workflow drift

- no critical drift

근거:
- non-goals는 계속 명시적으로 유지됐다

## 5. keep / tighten decision

판정:
- **tighten into field_spec_draft_v2**

왜 keep이 아닌가:
- v1은 안전하지만,
  `field layer outline`이 아직 too-structured하게 읽힐 여지가 있다
- broad package 이후 단계에서는
  이런 작은 구조화 신호가 concrete spec inflation으로 이어질 수 있다

왜 tighten인가:
- 지금 조이면
  compare candidate field-spec 트랙을
  다시 `information-band / layer quality` 수준으로 더 낮춰 둘 수 있다

## 6. tightening summary

v2에서 조이는 방향:

- `layer 1/2/3` 식의 계층 번호를 제거
- `field layer`보다 `information band` 쪽 표현으로 낮춤
- “필드가 무엇이냐”보다
  “어떤 종류의 information thickness를 허용하느냐”를 중심으로 다시 적음
- compare model 중심 / payload shaping 보조 / adapter mediation 비중심은 유지

즉:
- 방향은 유지
- 구조화 강도만 낮춘다

## 7. risk and correction record

### 이번 review에서 발견한 리스크

1. `layer 1/2/3`가 사실상 구조를 고정하는 신호처럼 읽힐 수 있었다
2. field-spec draft라는 이름이 shape memo보다 한 단계 더 구체적이라,
   작은 명명도 inflation으로 이어질 수 있었다

### 어떻게 수정했는가

- keep하지 않고 v2 tightening으로 갔다
- field-like outline을 information-band 수준으로 낮추는 방향을 택했다
- 이 correction은
  `spec inflation은 초기에 더 세게 자른다`는 working memory로 남긴다

## 8. alignment record

- supervisor starting judgment:
  이번 패키지는 v1 draft를 다시 읽고 keep/tighten 중 하나로 끝내라고 봤다.
- codex own judgment:
  전체 방향은 안전하지만, 일부 표현이 too-structured해서 tighten이 더 맞다고 봤다.
- disagreement or risk:
  `layer 1/2/3` 같은 명명은 작은 차이처럼 보여도 concrete spec drift를 부를 위험이 있었다.
- resolution:
  keep 대신 v2로 조이고, draft의 형태를 더 abstract한 information-band 수준으로 낮추기로 했다.

## 9. recommendation

다음 단계 추천:
- `field_spec_draft_v2`를 기준으로 한 **field-spec review recheck**

즉 바로 schema/구현으로 가지 않고,
조인 v2가 정말 inflation을 줄였는지 한 번 더 확인하는 단계가 맞다.
