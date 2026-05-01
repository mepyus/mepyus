# Package Brief - Package 025

## Purpose
`session_artifact_collector.sh`의 상세 설계안을 작성하고, 도입 타당성을 결정한다. 이 도구는 세션별로 분산된 주요 문서들을 패키지 루트 수준으로 집약하여 리뷰 효율을 높이는 데 목적이 있다.

## Sessions
1. **Current Bottleneck Analysis:** 다중 세션 패키지(예: P001)에서의 수동 수집 비용 분석.
2. **Technical Design:** 수집 대상, 경로 규칙, 덮어쓰기 방지 및 안전장치 설계.
3. **Boundary & Philosophy Check:** 판단 배제 원칙 및 `Scriptable Unit` 가이드라인 준수 여부 검토.
4. **Decision Document:** 상세 설계 및 도입 권고안 작성.

## Boundaries
- sandbox only
- no script implementation (design only)
- no source-space modification
- no automatic promotion of collected artifacts

## Review Questions
- 수집 대상 선정이 '판단'을 포함하고 있지는 않은가?
- 수집된 결과물이 패키지 루트를 복잡하게 만들 위험(Bloat)은 없는가?
- 이 도구가 실제 리뷰 시간을 얼마나 단축할 수 있는가?
