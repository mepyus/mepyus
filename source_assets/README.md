# source_assets

이 폴더는 루트에 섞이기 쉬운 source asset 계열 md를 앞으로 분리해서 넣기 위한 상위 정리 폴더다.

중요:
- 이미 receipt / provenance / source_ref 에 걸린 기존 루트 md는 추적 안정성을 위해 당장 대량 이동하지 않는다.
- 대신 새 source asset 는 기본적으로 이 폴더 아래 적절한 하위 폴더에 둔다.
- 기존 루트 md는 `legacy canonical root assets` 로 보고, 분류 인덱스로 먼저 관리한다.

구성:
- `declarations/`
  - 선언문 source asset
- `baselines/`
  - 기준문 / baseline source asset
- `directives/`
  - 실행/점검 지시서 source asset
- `handoffs/`
  - handoff 문서
- `external_case_inputs/`
  - 외부 사례 first-pass 입력 source asset
- `session_notes/`
  - 세션 요약 / close note / 일시적 작업 정리
- `legacy_misc/`
  - 아직 분류가 덜 끝난 루트 md를 나중에 옮길 후보

운영 기준:
- 새 문서가 생성될 때 루트에 바로 두기보다 먼저 여기서 시작하는 것을 권장한다.
- 다만 canonical source path 안정성이 중요한 문서는 이동 전에 별도 정리 패스를 거친다.
- 새 source asset 를 만들 때는 문서 앞부분에 아래 두 값이 보이게 적는 것을 권장한다.
  - `source_asset_group`
  - `source_asset_path`

예:
- `source_asset_group: directives`
- `source_asset_path: source_assets/directives/<file>.md`
