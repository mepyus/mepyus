# gemini_cli_bounded_task_catalog_v0.md

## 목적
Gemini CLI가 수행 가능한 구체적인 Task Catalog이다.

## Task Catalog
1. **Material Sorting**: 흩어진 재료를 surface별로 분류.
2. **Card Drafting**: 지정된 4줄 카드 형식으로 초안 작성.
3. **Validation Loop**: 테스트 material이 기준을 준수하는지 검증.
4. **Batch Processing**: 여러 재료를 독립된 worker_return 단위로 분리 처리.
5. **Self-Check**: 각 Task 결과물에 대한 자체 검증(Self-check) 수행.
6. **Note Append**: Trial note에 특정 섹션 추가.

## 금지 사항
- 위 Catalog를 벗어난 시스템적 행위는 일체 금지함.
