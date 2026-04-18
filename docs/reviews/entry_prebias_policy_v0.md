# Entry Prebias Policy v0

## 목적

이 문서는
classifier 이전 단계에서
`source-to-family hints` 와 `family-rooted alias` 가
어떻게 first entry를 기울이는지 정한다.

즉 이 문서는
`entry prebias layer`
를 위한 규칙이다.

## 왜 필요한가

현재 entry는 이미 아래 구조를 가진다.

- source artifact
- signal_kind
- classifier rule
- priority policy

하지만
[source_to_family_hints_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/source_to_family_hints_v0.md)
와
[family_rooted_signal_grammar_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/family_rooted_signal_grammar_v0.md)
를 추가하면서
classifier 앞에서도 family bias를 줄 수 있게 됐다.

이 bias가 아무 규칙 없이 섞이면
입구가 더 복잡해진다.

그래서
hint와 alias가 어디까지 영향을 주는지
먼저 고정해야 한다.

## 핵심 문장

entry prebias는
classifier를 대체하지 않는다.

다만 classifier가 보기 전에
어느 family/projection/route가 더 보존적이고 자연스러운지
미리 기울기를 준다.

## 입력 층

prebias는 아래 입력을 본다.

1. source artifact
2. source-to-family hints
3. signal_kind
4. family_rooted_alias
5. requested_outcome

출력은 확정 classification이 아니라
`preferred bias set`
이다.

## 최소 출력 필드

- `prebias_family_ids`
- `prebias_projection_ids`
- `prebias_route_ids`
- `prebias_strength`
- `prebias_reason`
- `classifier_override_allowed`

## 기본 원칙

### 1. hint beats bare signal

artifact가 직접 남긴 high-confidence family hint가 있으면
signal_kind의 default family보다 먼저 본다.

이유:

- source가 same-root 감각을 직접 가리킬 수 있기 때문이다

### 2. family-rooted alias strengthens but does not decide

alias는 family 방향을 강화하지만
혼자서 final family를 확정하지는 않는다.

즉 alias는
signal을 line 쪽으로 번역하는 보조 층이다.

### 3. preservation-oriented prebias wins early

entry 단계에서는 flattening보다 preservation 쪽 bias를 먼저 준다.

예:

- `input_family_preservation_conflict`
- `transition_family_closure_conflict`

### 4. requested_outcome can still override prebias

질문이 명백히 다른 층을 요구하면
classifier override가 prebias보다 강하다.

예:

- source hint가 input family를 가리켜도
- 질문이 blockage explanation이면
- transition family override 검토가 가능하다

### 5. low-confidence hint only nudges

hint_confidence가 낮으면
family를 확정하지 않고
projection 또는 route preference 정도만 준다.

## 우선순위

prebias 단계에서는 아래 순서를 따른다.

1. high-confidence source-to-family hints
2. family-rooted alias
3. signal_kind default family
4. requested_outcome-based override possibility
5. classifier rules

즉 prebias는
classifier 이전의 기울기이고,
최종 판정은 classifier가 한다.

## builder_choi 적용 예시

source:

- [builder_choi_interview_transcript_preprocess_comparison.json](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json)

hint:

- `candidate_family_ids = [fam_input_to_reading]`
- `candidate_projection_ids = [proj_preprocess_shaping]`
- `candidate_route_ids = [route_preprocess_compare_first]`
- `hint_confidence = high`

signal:

- `preprocess_ambiguity`

alias:

- `input_family_preservation_conflict`

이 조합이면 prebias output은 아래처럼 읽는다.

- `prebias_family_ids = [fam_input_to_reading]`
- `prebias_projection_ids = [proj_preprocess_shaping]`
- `prebias_route_ids = [route_preprocess_compare_first]`
- `prebias_strength = high`
- `classifier_override_allowed = true`

즉 이 케이스는
classifier가 보기 전부터
이미 input family 보존 쪽으로 강하게 기울어진다.

## v0 경계

prebias는 아직 runtime 엔진이 아니다.

현재는

- reasoning contract
- future classifier adapter rule

수준에 머문다.

즉 지금은 문서와 manifest 구조를 정렬하는 단계다.

## 한 줄 요약

entry prebias policy v0는
source hint와 family-rooted alias를 이용해
classifier 이전에 family/projection/route 쪽으로 약한 but explicit 기울기를 주는 규칙이다.
