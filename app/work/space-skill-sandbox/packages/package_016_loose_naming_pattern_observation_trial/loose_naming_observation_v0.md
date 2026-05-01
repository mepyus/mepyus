# Loose Naming Pattern Observation Note (v0)

## 개요
Package 016에서는 강제적인 명명 규칙(Convention) 대신, 지금까지 관찰된 느슨한 명칭 패턴(Loose Naming Pattern)이 메타데이터 기반 리뷰(Metadata-first review)에 어떤 신호를 주는지 분석했습니다.

## 1. 식별력을 높이는 긍정적 패턴 (High-Signal Patterns)

- **`*_vN.md` (버전 명시형):** `priority_note_v0.md`, `landscape_report_v0.md` 등.
  - 관찰: "잠정적"이거나 "진행 중"인 상태를 암시하여, 리뷰어가 이를 베이스라인으로 오해하지 않게 하는 보호막 역할을 함.
- **`*_plan.md`, `*_decision.md` (의도/결정 명시형):** `codex_plan.md`, `first_tiny_script_decision_v0.md`.
  - 관찰: 패키지의 '사전 설계'와 '최종 선택'을 명확히 분리하여, 전체 맥락 파악 시간을 단축함.
- **`*_candidate.md` (후보 명시형):** `script_card_candidate_v0.md`.
  - 관찰: 해당 문서가 아직 승격되지 않은 '제안' 상태임을 명확히 함으로써 리뷰어의 비판적 사고를 유도함.
- **`*_result.md` (결과 명시형):** `analysis_result.md`, `smoke_test_result.md`.
  - 관찰: 실행 데이터와 요약 사이의 '가교' 역할을 하는 문서임을 쉽게 인지하게 함.

## 2. 혼동을 야기할 수 있는 패턴 (Confusion Risks)

- **`standard_name`과 유사한 변형:** `target_metadata_scan_report.md` (012).
  - 관찰: 스크립트는 이를 `metadata_scan_report.md`와 다른 "Core Authored Doc"으로 정확히 찾아냈으나, 인간 리뷰어는 리포트의 복사본인지 패키지 고유 문서인지 한눈에 알기 어려울 수 있음.
- **너무 일반적인 명칭:** `revision_result.md` (011).
  - 관찰: `revision`이 무엇에 대한 수정인지 파일명만으로는 알 수 없어, 결국 파일을 열어봐야 하는(Deep-read) 비용이 발생함.

## 3. 느슨한 패턴의 효용성 평가

- **충분성:** 현재의 `package_metadata_scan.sh` 로직(표준 기록물 외 모두 후보군) 하에서는, 명칭에 최소한의 힌트(`_v0`, `_plan` 등)만 있어도 리뷰 대상을 선정하는 데 충분히 유효한 신호를 제공함.
- **강제성 여부:** 강제 규칙으로 만들 경우 표현의 유연성을 저해할 수 있으므로, 현재는 **"유용한 후보군(Watch Signal)"**으로 남겨두는 것이 적절함.

## 4. 잠정적 권장 (Provisional Recommendations)

- 새로운 패키지 고유 문서를 만들 때, 가능한 한 `plan`, `result`, `note`, `candidate`, `v0`와 같은 키워드를 조합하는 것이 메타데이터 스캔 시 "의도가 담긴 문서"로 분류되는 데 유리함.
- 이는 규칙이 아닌, **"서로를 위한 배려 섞인 명명(Mindful Naming)"** 수준에서 장려됨.
