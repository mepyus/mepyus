# Gemini Instruction: External & Internal Material Batch Read v1

## 목적
외부 자료와 내부 작업 패킷을 독립적으로 심층 분리 판독한다.

## 대상 자료
1. Material 4: inputs/external_cases/oh_my_opencode_openai_community.txt
   - Surface: external_material_file
2. Material 5: inputs/external_cases/codex_pipeline.md
   - Surface: work_packet_internal (외부 자료가 아님을 주의)

## 가이드라인
- 각 자료를 독립적으로 처리한다.
- codex_pipeline.md는 내부 자산(work_packet_internal)이므로, 외부 자료처럼 다루지 말고 엔진의 파이프라인 명세로서 기술적 정합성을 검증한다.
- 결과는 sandbox/result.md로 저장한다.
- 반드시 Deep Validation Contract를 준수한다.
