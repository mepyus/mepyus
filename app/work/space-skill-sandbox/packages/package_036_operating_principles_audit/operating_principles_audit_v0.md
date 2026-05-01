# Operating Principles Alignment Audit (v0)

## 0. 개요
본 문서는 샌드박스 유틸리티 라운드(Package 000~034)의 결과물을 초기 15개 운영 원칙과 대조하여, 무엇이 본체(Source-space)와 연결될 자격이 있는 '인터페이스 후보'인지, 무엇을 샌드박스에 남길지 판단합니다.

## 1. Audit 결과 (Candidate Matrix)

| 항목 | 인터페이스 후보(Candidate) | 샌드박스 유지(Sandbox-local) | 보류/폐기(Hold/Discard) |
| :--- | :---: | :---: | :---: |
| **Metadata-first Review** | O | | |
| **package_metadata_scan.sh** | O | | |
| **session_artifact_collector.sh** | O | | |
| **Manifest 기반 검증 방식** | O | | |
| **Gemini Reporting Tone Guard** | | O | |
| **임시 용어집(Glossary)** | | O | |
| **공식 워크플로우/자동화** | | | O |
| **그래프/온톨로지 구축** | | | O |

## 2. 인터페이스 후보 평가 (준비도)

- **Metadata-first Review 방식:** 이미 Gemini가 package-level signal을 스스로 회수하고 있어, 본체와의 인터페이스로서 매우 성숙함.
- **Utility Scripts (Scan/Collect):** 코드 자체는 매우 단순(KISS/YAGNI)하며, 본체 리뷰 워크플로우에서도 '작은 마찰 해결' 도구로 활용 가치가 높음. 단, Darwin 종속성은 차기 감사 대상.
- **Manifest Provenance:** 데이터의 신뢰성 검증을 위한 최소한의 운송 메타데이터로 적합함.

## 3. 샌드박스 유지 항목
- **Tone Guard:** Gemini의 과잉 표현 억제는 환경과 상황에 따라 미세하게 조정이 필요하므로, 본체에 강제하기보다 샌드박스 내에서 모델의 습성을 교정하는 용도로 유지.
- **용어집:** 본체의 공식 사전으로 승격하기엔 아직 휘발성이 강함. '임시 손잡이'로 계속 활용.

## 4. 폐기/Hold 항목
- **자동화/Router:** 시스템의 복잡도를 급격히 높이는 자동화 연결은 현재 지식 수준에서 시기상조임.
- **공식 Workflow 선언:** 실험적 유연성을 보존하기 위해 공식화하지 않음.

## 5. 결론 및 향후 방향
철학을 작은 실행 단위로 구현하는 데 성공했습니다. 이제 필요한 것은 이 후보군들을 본체(Source-space)와의 인터페이스로 승격하기 위한 안전한 검증(Codex reentry 검증)입니다.
