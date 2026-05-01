# gemini_cli_result_return_contract_v0.md

## 목적
Gemini CLI의 작업 결과를 Codex가 어떻게 읽을 것인가에 대한 계약.

## 계약 내용
1. 모든 결과는 `worker_return` surface를 가진다.
2. 독립된 material 처리를 위해 섹션별로 분리되어야 한다.
3. self-check 항목을 포함한다.
4. 최종 판단은 Gemini의 verdict를 참고할 뿐, Codex/사용자가 수행한다.
