# Boundary Cases v1 Curation

최종 세트: `boundary_cases_v1_final.json`

목적:
- `scene / role / score` 경계가 실제로 갈릴 만한 짧은 문단을 모은다.
- 장문 문서보다 빠르게 라벨기 drift를 확인한다.
- 이후 Codex / ChatGPT / Gemini 공통 라벨링 입력으로 사용한다.

큐레이션 원칙:
- `boundary_pair` 분포는 생성 요청과 동일하게 유지
- 현실 문서 조각처럼 읽히는 문단 우선
- 지나치게 교과서적이거나 지나치게 메타적인 문단은 제외
- ChatGPT의 일상적이고 자연스러운 사례와 Gemini의 개념적 경계 사례를 혼합

선정 비율:
- `chatgpt`: 16개
- `gemini`: 14개

선정 이유:
- `chatgpt`는 일상 관찰, 회고, 조직/업무 장면이 자연스러워 실제 라벨링 스트레스 테스트에 유리했다.
- `gemini`는 정의형/추상형 문단에서 경계를 깔끔하게 흔드는 사례가 있어 일부 축에 유용했다.

주의 사항:
- [boundary_cases_v1.json](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/inputs/boundary_cases/raw_generations/chatgpt/boundary_cases_v1.json) 는 원본에 따옴표 이스케이프 오류가 1건 있다.
- 오류는 `bc_029`의 `case_text` 시작부에 있으며, 원본은 보존했다.
- 최종 세트에서는 해당 문자열만 정상화해 반영했다.

다음 사용 방식:
1. 이 최종 세트를 공통 입력으로 사용한다.
2. Codex / ChatGPT / Gemini가 같은 `case_text`를 라벨링한다.
3. 비교는 `scene -> role -> confidence/ambiguity -> stability` 순으로 본다.
