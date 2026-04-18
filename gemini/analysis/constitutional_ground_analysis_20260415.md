# Constitutional Ground Analysis & Comparison Report

Date: 2026-04-15
Actor: Gemini-CLI
Reason: Re-scanning all repository materials to identify constitutional foundations and comparing them with previous high-level summaries.

## 1. Identified Constitutional Materials (Source Evidence)
저장소 물리적 스캔을 통해 확인된 헌법적 근거 자산입니다.
- **`GEMINI.md`**: VECTORFL 7대 핵심 원칙 (Hierarchy of Thought, SSOT, Separation of Concerns 등).
- **`app/work/current_layer_baseline/engine_philosophy_declaration_v1.md`**: "정답보다 위치값 우선" 원칙 명시.
- **`app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`**: 판독 상태(Mixed/Canonical) 분류 기준.
- **`docs/policies/`**: `ANCHOR_V1.md`, `MEASUREMENT_RETENTION_POLICY.md` 등 구체적 운영 가이드라인.
- **`RUNLOG.jsonl`**: 헌법 제5조 '이유 중심 기록'의 실행 주체.

## 2. Core Pillars Re-Synthesized
물리적 재료를 기반으로 재정립한 헌법의 7대 기초입니다.
1. **Hierarchy of Thought**: 논리가 코드를 앞선다. (`work/` -> `main/`)
2. **Single Source of Truth (SSOT)**: `CONSTITUTION.md`가 최고 권위.
3. **Priority of Authority**: Constitution > Baseline > App.
4. **Separation of Concerns**: 4계층(Container, View, Styles, Service) 및 공간 분리.
5. **AI Pipeline & Guardrails**: Baseline 수정 불가(Read-Only) 및 기록 후 행동.
6. **Technical Standards**: RPC 기반 상태 변화 강제.
7. **Knowledge Classification**: Why/How/What의 구조적 분리.

## 3. Comparison with Previous Response

### A. 일반 요약 (Previous) vs. 실체 분석 (Current)
- **정밀도**: 앞선 답변은 5가지로 요약했으나, 실제 헌법은 7가지 세부 조항으로 구성되어 있으며 물리적 공간 분리 규칙이 훨씬 엄격함.
- **운영 로직**: 이전에는 '기록' 자체를 강조했으나, 실제 재료는 'Bridge 유무'와 '판독 숙성도'에 따른 상태 전이 규약이 헌법의 핵심 기술적 기초임을 보여줌.
- **물리적 강제**: 이전 답변은 원칙 중심이었으나, 실제 재료는 `baseline/` 폴더에 대한 AI의 접근 제한 등 물리적 가드레일을 명시함.

### B. 주요 차이점 요약
| 항목 | 이전 답변 | 현재 분석 (재료 기반) |
| :--- | :--- | :--- |
| 조항 수 | 5개 | 7개 + 세부 운영 계약 |
| 기록 대상 | 행동 위주 | 행동의 의도 + 상태 전이의 정당성 |
| 공간 개념 | 단순 폴더 구분 | 사고의 숙성 단계별 격리 (Work -> Refac -> Main) |

## 4. Conclusion
우리 헌법의 기초는 단순한 도덕적 지침이 아니라, **"AI의 자의적 판단을 물리적/논리적으로 봉쇄하고, 모든 지식의 유래를 추적 가능하게 만드는 시스템적 설계도"**입니다. 특히 `app/work`는 단순한 작업장이 아닌, 헌법이 보호하는 **'사고의 배양 공간'**으로서의 지위를 가집니다.

---
*Note: 모든 분석은 `gemini/` 폴더 내에만 기록되었으며, 타 폴더는 수정되지 않았습니다.*
