# SESSION_6_HANDOFF

## Goal (Session 6)
`CLI_SESSION_PROTOCOL_V0` 수립. 도구의 역할(Profile)과 작업 단위(Context Bundle)를 연결하는 실질적인 CLI 실행 규칙 수립.

## Profile 및 Bundle 활용
- Session 5의 `TOOL_ROLE_PROFILES_V0`를 기반으로, 각 도구별 작업 프로세스 정의.
- Session 4의 `CONTEXT_BUNDLE_ASSEMBLY_FLOW_V0`와 연결하여 CLI의 검색/셋업 순서 고정.

## Key Focus
- CLI가 상상하지 않고 '공간 검색'을 먼저 수행하도록 강제하는 트리거 매커니즘.
- Issue Log 기록 및 Handoff 전달 표준화.
- 도구의 출력을 수용할지 혹은 재작업할지 판단하는 'Review Gate' 연결.

## Next Steps
- 각 CLI 실행 세션의 표준 템플릿(Search-Do-Log-Handoff) 완성.
