# WORK_REFLUX_LOG - 2026-04-11

## 📋 Task: 엔진면 v2 업그레이드 (진단 및 유지보수 콘솔화)

### 1. 작업 의도 (Intent)
- 현재의 엔진면은 수동적인 정보 표시(Dashboard) 수준에 머물러 있음.
- 이를 AI 에이전트가 리포지토리를 직접 관리하고 정비하는 '능동적 콘솔(Console)'로 격상시켜야 함.
- 공간(Space) 내의 에너지 흐름(Attention)과 데이터의 뿌리(Lineage)를 추적 가능하게 만드는 것이 핵심.

### 2. 주요 변경 사항 (Proposed Changes)
- **Data Schema:** `attentionScore`, `scriptLink`, `deltaStatus` 필드 추가.
- **Inventory Panel:** 어텐션 히트맵 아이콘 적용 및 상태 시각화 강화.
- **Inspector Panel:** 스크립트 계보(Managed By) 및 실행 로그 섹션 추가.
- **Space Health:** 공간 숙성도 및 기준선 정합성 패널 신설.

### 3. 수행 기록 (Action Logs)
- [2026-04-11 14:30] `WORK_REFLUX_LOG.md` 생성. 작업 기준 고정.
- [2026-04-11 14:32] `engine-surface.types.ts` 확장 완료 (`attentionScore`, `scriptLink`, `deltaStatus`).
- [2026-04-11 14:35] `AssetInventoryPanel.tsx` 개선 완료 (Flame 아이콘 히트맵 반영).
- [2026-04-11 14:38] `live_manifest.json` 데이터 보강. `gemini/mock_test`에 어텐션 95 주입.
- [2026-04-11 14:45] `AssetInspectorPanel.tsx` v2 업그레이드 완료. System Lineage 및 Baseline Delta 섹션 추가.
- [2026-04-11 14:48] `live_manifest.json` 내 '규칙 위반(Violation)' 시나리오 자산 추가.
- [2026-04-11 14:55] `SpaceHealthPanel.tsx` 신설 및 엔진면 통합 완료. 전역 정합성 및 숙성도 시각화.
- [2026-04-11 15:05] 런타임 에러(ReferenceError) 해결 및 3단계 최종 성공 확인.
- [2026-04-11 16:15] 사용자면(User Surface) 리팩터링 시작. 헌법 3.1절(Goal Declaration) 기준 정렬 작업.
- [2026-04-11 16:17] `CommandHeaderPanel` 분해 및 `MaterialContextPanel` 신설 작업 수행.

### 5. [Critical Learning] Engine Surface Constitution (via Codex)
- **핵심 인식:** 엔진면은 대시보드가 아니라 "공간 컨트롤면"임. 
- **읽기 순서 고정:** Ingest Entry (입력) → Pipeline Status (처리) → Validation Return (환류) 순서로 정보 위계 재조정 필요.
- **라인의 재정의:** 라인을 '중간 운용 형성체'로 인식하고 4축(Origin, Meaning, Role, Maturity) 기반의 정보 노출 전략 수립.
- **제약 사항:** 직접 조작 버튼 배제, 'Surface Slot Candidate' 명시.

### 6. 수행 기록 (Action Logs)
- [2026-04-11 15:45] Codex 학습 자료 수용 완료. 엔진면 v3 정밀 교정 시작.
- [2026-04-11 15:48] `ValidationReturnPanel` 내 필드명을 `accepted_refs`, `hold_refs` 등으로 헌법에 맞게 정규화 예정.
