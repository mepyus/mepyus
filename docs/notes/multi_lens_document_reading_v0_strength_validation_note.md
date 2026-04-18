# multi lens document reading v0 strength validation note

## Purpose

이 note는 `multi_lens_document_reading_v0` skeleton의 현재 `reading_strength`
휴리스틱이 fixture 기준에서 어떻게 읽히는지 관찰만 남긴다.

이번 note는 heuristic patch가 아니라 observation 기록이다.

## Fixtures used

- `dialogue_continuation`
- `explanatory_mechanism`
- `argument_contrast`
- `mixed_document`

## Stable/thick line observation

- 실제 적용 lens는 stable/thick 두 개다
- `line_input_to_reading_organ`
- `line_transition_over_surface`
- 현재 heuristic에서는 keyword가 보이면 `strong`
- keyword가 없고 `linkage_confidence=low`이면 `weak`
- 나머지는 `absent`

## Candidate/thin line observation

- candidate/thin lens는 이번 skeleton에서 실제 reading 적용 대상이 아니다
- secondary metadata로만 남긴다
- 따라서 candidate/thin의 strength 분포는 이번 결과에서 산출하지 않는다

## Distribution summary

- 결과는 `/tmp/multi_lens_document_reading_strength_validation/validation_result.json`에 기록한다
- 현재 결과는 keyword-hit 여부에 크게 좌우된다
- strong/weak/absent 분포는 line evidence maturity가 아니라 starter heuristic output일 뿐이다

## What this does not prove

- `strong`이 나왔다고 해당 line이 실제로 성숙했다고 증명하지 않는다
- `absent`가 나왔다고 해당 line이 문서에 없다고 증명하지 않는다
- candidate/thin lens를 실제로 읽지 않았으므로 secondary line behavior를 검증했다고 볼 수 없다

## Next step

다음 단계는 stable/thick lens 두 개에 한해서 keyword map과 reading_basis를 조금 더 설명적으로 정리하는 bounded refinement다.
