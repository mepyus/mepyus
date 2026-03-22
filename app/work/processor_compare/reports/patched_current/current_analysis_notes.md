# Current Analysis Notes

## Scope

현재 메모는 `doc_001`부터 `doc_008`까지의 비교 실험에서 관찰된 핵심 경향을 임시 정리한 것이다.
정식 summary는 `comparison_summary.md`를 따르고, 이 문서는 calibration 관점의 해석 메모를 보강한다.

## Global Pattern

- Codex: 중간 granularity, 구조 보존, 보수적 점수
- ChatGPT: 세분화 경향, 높은 confidence, 낮은 ambiguity, scene schema 오용 반복
- Gemini: 대묶음 경향, 추상화 확대, meta/reflection 또는 비표준 scene 사용 경향

## doc_005

- Codex 10 fragment, ChatGPT 12 fragment, Gemini 9 fragment
- ChatGPT는 `요약/정의`, `문제/해법`, `Link 메커니즘/가치`를 더 잘게 나눴다
- Gemini는 `도입+정의`, `문제+해법`, `Link 메커니즘+가치`, `결론+메타 해석`으로 더 크게 묶는 경향을 보였다
- doc_005는 입력기 경계와 라벨기 차이를 가장 넓게 드러내는 calibration 문서로 유지한다

## doc_006

- Codex 11 fragment, ChatGPT 11 fragment, Gemini 8 fragment
- 구조가 분명한 기술 문서에서는 ChatGPT의 과세분화가 줄고 Codex와 granularity가 비슷해졌다
- Gemini는 여전히 구축 단계, 질의 단계, 비교 예시, 기술 과제/정리를 더 크게 묶었다
- Gemini는 `scene=process`를 사용해 schema를 어겼다
- doc_006은 구조가 분명한 장문 기술 문서에서 처리자 성향이 어떻게 달라지는지 확인하는 보조 calibration 문서다

## doc_007

- Codex 12 fragment, ChatGPT 14 fragment, Gemini 7 fragment
- 철학 개념사 문서에서는 ChatGPT의 과세분화가 다시 강해졌고, `플라톤 동굴 비유`, `매트릭스`, `푸코/마그리트`를 별도 fragment로 분리했다
- Gemini는 `화폐 예시`, `계보 전환`, `불안 정조`를 독립 fragment로 두지 않고 철학자별 큰 설명 블록으로 압축했다
- ChatGPT는 `scene=example`, `anchor_type=example`을 사용했고, Gemini는 `definition`, `historical_context`, `analysis`, `technical_reflection` 같은 비표준 scene을 사용했다
- doc_007은 비기술 장문에서 `정의/예시/계보 비교/문화적 불안` 경계가 어떻게 흔들리는지 보여주는 calibration 문서다

## doc_008

- Codex 15 fragment, ChatGPT 13 fragment, Gemini 8 fragment
- 문학 비평 장문에서는 ChatGPT가 예상보다 덜 잘게 자르고, 논지를 더 큰 압축 블록으로 묶었다
- Gemini는 여전히 `도입+문학관`, `생애+논지`, `우화 분석`, `결론` 같은 큰 구조 블록으로 읽었다
- 이번 문서에서는 ChatGPT의 평균 confidence가 Codex보다 낮고 ambiguity가 더 높아, 이전 장문들과 다른 `압축형/유보형` 읽기가 나타났다
- doc_008은 문학 비평 장문에서 `논증 단계 보존 vs 논지 압축` 차이를 보여주는 calibration 문서다

## Calibration Signals

- `요약/정의`
- `문제/해법`
- `메커니즘/가치`
- `과정 설명을 scene으로 어떻게 처리하는가`
- `철학자 내부 소단락을 어디까지 분리하는가`
- `문화 예시와 불안 정조를 example/reflection으로 어떻게 판정하는가`
- `문학 비평 장문에서 논증 단계와 해석 단계를 어디서 압축하는가`

위 항목들은 이후 장문 문서 비교에서 우선 점검할 기준선으로 유지한다.
