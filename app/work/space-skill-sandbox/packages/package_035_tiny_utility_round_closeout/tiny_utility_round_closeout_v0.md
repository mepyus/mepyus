# Sandbox Tiny Utility Round Closeout (v0)

## 0. 개요
본 문서는 Package 008~034까지 수행된 샌드박스 유틸리티 라운드의 전체 정리본입니다. 본 라운드는 공식 워크플로우를 만드는 것이 아닌, 작업 중 발생하는 마찰(friction)을 줄이는 '실험적 보조 도구'의 운용 경계를 확립하는 데 목적이 있습니다.

## 1. 주요 산출물
- **package_metadata_scan.sh**: 파일 시스템 지형 탐색 및 리뷰 후보 식별용 Discovery Helper.
- **session_artifact_collector.sh**: 증거 수집 및 기원(Provenance) 보존용 Transport Helper.

## 2. 사용 경계 (Usage Boundaries)
- **필요 시 사용:** 모든 패키지에 적용하지 않음. flat/small 패키지에서는 사용을 지양함.
- **판단 금지:** 도구는 데이터(파일 목록, 시점, 경로)만 제공하며, 중요도나 최신성 판단은 전적으로 리뷰어의 영역임.
- **구조 제한:** Cross-package 참조, 자동화 연동, 그래프 확장 금지.

## 3. 핵심 위험 관리 (Watch Items)
- **과잉 확정:** "표준 도구", "검증됨" 등의 표현을 금지하고 "Candidate", "Candidate trial" 수준을 유지함.
- **환경 의존성:** Darwin stat/date 기반이므로 Linux 이식 시 검증 필요.
- **절대 경로 노출:** 공유/이식성을 위해 절대 경로를 Debug-only note로 다룸.

## 4. Codex 재진입 검증 체크리스트
- 도구가 의미 판단을 하고 있지 않은가?
- transport helper의 역할을 벗어나지 않았는가?
- manifest가 판단 근거만 제공하는가?
- 워크플로우에 대한 과잉 확정이 없는가?
