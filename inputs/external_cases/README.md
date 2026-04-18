# external_cases

외부 사례 원문을 넣는 위치다.

예:
- 외부 강연 transcript
- 외부 회사/제품 사례 txt
- 외부 기술 설명 원문
- raw transcript 또는 정리 전 원문

권장:
- 파일명은 짧고 식별 가능하게 둔다.
- 예: `enterprise.txt`, `saltlux.txt`, `aifrontier_01_28.txt`

주의:
- 여기에는 raw source를 둔다.
- 판독 결과, 요약 결과, observation 결과는 여기 두지 않는다.
- 새로 넣는 canonical raw input은 가능하면 `txt` 또는 정리 전 raw text 형태로 두는 쪽을 우선한다.
- 현재 이 폴더 안에 있는 일부 `md` 파일은 예전 운영에서 들어온 혼합 입력 자산이다.
- 즉 `md` 가 모두 잘못된 것은 아니지만, 새 입력 기준으로는:
  - raw transcript / raw text / 원문 = 여기
  - 구조화된 참고 문서 / 별도 정리본 = `inputs/reference_docs/`
  - source input md / 지시용 md = `source_assets/external_case_inputs/`

빠른 기준:
- 새 외부 원문 넣기: 여기
- 내가 이미 정리한 외부 사례 md 넣기: `inputs/reference_docs/`
- Codex가 만드는 external case input source md: `source_assets/external_case_inputs/`
