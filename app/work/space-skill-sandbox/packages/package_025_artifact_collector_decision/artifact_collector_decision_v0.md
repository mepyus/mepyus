# Artifact Collector Decision Note (v0)

## 0. Status
- status: sandbox design candidate
- implementation_created: false
- prototype_approved: false
- judgment_tool_shift_risk: Low

## 1. Current Bottleneck Analysis
Package 001과 같이 다중 세션을 포함하는 패키지에서, 각 세션의 결과(`gemini_packet.md`, `handoff_log.md`, `codex_review_bundle.md`)를 확인하기 위해서는 수동으로 여러 디렉토리를 오가야 함. 이는 리뷰어의 인지 부하를 높이고, 전체 맥락 파악을 지연시키는 주요 병목으로 식별됨.

## 2. Technical Design

### A. Input / Output Boundary
- **Input:** `PACKAGE_DIR` (예: `app/work/space-skill-sandbox/packages/package_001_external_lens_reread/`)
- **Output:** `<PACKAGE_DIR>/collected_artifacts/` 디렉토리 생성 및 파일 복사.

### B. Logic & Strategy
1. **Target Identification:** `session_*` 패턴의 하위 디렉토리 탐색.
2. **Standard Artifacts:** 아래 파일명과 매칭되는 마크다운 파일만 수집.
   - `gemini_packet.md`
   - `handoff_log.md`
   - `codex_review_bundle.md`
   - `analysis_result.md` (존재할 경우)
3. **Collision Avoidance:** `session_XX_<original_name>` 형식으로 파일명을 변경하여 복사.
4. **Safety:**
   - 기존 `collected_artifacts/` 폴더가 존재할 경우 덮어쓰기 거부 (또는 사용자 승인 루프).
   - `PACKAGE_ROOT` 외부로의 파일 유출 차단.

## 3. Boundary & Philosophy Check
- **판단 배제:** 수집 대상은 파일명의 '형식적 매칭'에만 의존하며, 내용의 옳고 그름을 판단하지 않음. 이는 전형적인 'Transport/Discovery' 역할임.
- **Bloat 방지:** 패키지 루트에 직접 파일을 뿌리지 않고 별도 서브폴더를 사용함으로써 가독성을 유지함.
- **Minimal Brief 정렬:** 브리프 생성과 무관한 '결과 수집' 도구이므로 충돌 위험 없음.

## 4. Decision
**Recommendation:** `session_artifact_collector.sh` 도입을 강력히 권장함.

이 도구는 `package_metadata_scan.sh`가 제시한 '리뷰 시작점'을 실제로 '물리적 한 지점'으로 모아줌으로써, `Metadata-first Discovery` 철학을 완성하는 데 기여할 것으로 기대됨.

## 5. Next Step (If Approved)
- Package 026: `session_artifact_collector.sh` 프로토타입 구현 및 P001 대상 스모크 테스트.
