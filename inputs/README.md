# inputs

이 폴더는 사람이 넣는 입력 재료의 기본 드롭존이다.

핵심 원칙:
- raw 입력은 먼저 `inputs/` 아래에 둔다.
- 해석 결과나 observer 결과는 `docs/` 또는 `runtime/`으로 간다.
- raw와 interpreted output을 섞지 않는다.

구성:
- `external_cases/`
  - 외부 사례 원문
  - transcript, txt, 복붙 원문, 외부 기술/회사/운영 사례
- `internal_notes/`
  - 내부 메모
  - 생각 조각, 초안, 작업 메모, 빠른 임시 입력
- `reference_docs/`
  - 구조화된 참고 문서
  - 별도 정리본, 참고용 md/txt/pdf 원문 후보

운영 기준:
- canonical source가 필요한 입력은 가능하면 여기서 시작한다.
- 기존 root source는 기록 보존 때문에 그대로 둘 수 있지만, 새 입력은 기본적으로 여기로 넣는다.
- 입력이 들어오면 이후 해석/관찰/판독 결과는 `docs/examples`, `docs/reports`, `runtime/observer`, `runtime/contracts` 등으로 분리해 남긴다.
